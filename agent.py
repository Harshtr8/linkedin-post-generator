import os
import json
import re
from typing import List, Dict, Any
from dotenv import load_dotenv
import google.generativeai as genai

from utils import sanitize_text, dedupe_hashtags, enforce_word_limit

# -------------------
# Load API Key
# -------------------
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise RuntimeError("❌ Missing GEMINI_API_KEY. Please set it in your .env file or environment variables.")

genai.configure(api_key=GEMINI_API_KEY)
MODEL_NAME = "models/gemini-2.5-pro"
model = genai.GenerativeModel(MODEL_NAME)

# -------------------
# System Rules
# -------------------
SYSTEM_RULES = """You are an expert LinkedIn content writer and editor.
Rules:
- Write for LinkedIn: short paragraphs, clear, scannable structure.
- Keep a professional yet human tone (avoid jargon & clichés).
- No profanity, hate, or sensitive claims.
- Prefer actionable insights and examples.
- If hashtags requested, include 3–6 relevant, specific hashtags.
- If CTA requested, add a natural call-to-action at the end.
- Emojis only if tone is Casual or Inspirational (max 2).
- Always return **valid JSON only** (no markdown)."""

# -------------------
# Build Prompt
# -------------------
def _build_prompt(
    topic: str,
    tone: str,
    audience: str | None,
    count: int,
    include_hashtags: bool,
    include_cta: bool,
    max_words: int,
    seed: str | None,
    style_notes: str | None,
) -> str:
    return f"""
{SYSTEM_RULES}

Task: Generate {count} distinct LinkedIn posts on the topic: "{topic}".

Tone: {tone}
Audience: {audience or "General LinkedIn professionals"}
MaxWordsPerPost: {max_words}
IncludeHashtags: {"Yes" if include_hashtags else "No"}
IncludeCTA: {"Yes" if include_cta else "No"}

AdditionalSeed: {seed or "None"}
StyleNotes: {style_notes or "None"}

Return JSON ONLY in this schema:
{{
  "posts": [
    {{
      "title": "Short, scroll-stopping line (max 10 words)",
      "body": "Main post body (<= {max_words} words, 2–5 short paragraphs)",
      "hashtags": ["#tag1", "#tag2"]  // include only if hashtags requested
    }}
  ]
}}
"""

# -------------------
# JSON Extraction
# -------------------
def _extract_json(text: str) -> dict:
    try:
        return json.loads(text)
    except Exception:
        pass

    # Capture JSON-like block with regex
    match = re.search(r'\{[\s\S]*\}', text)
    if match:
        try:
            return json.loads(match.group(0))
        except Exception:
            pass

    # Fallback: split text into chunks as fake posts
    chunks = [c.strip() for c in text.strip().split("\n\n") if c.strip()]
    posts = [{"title": c.splitlines()[0][:60], "body": c} for c in chunks]
    return {"posts": posts[:3]}

# -------------------
# Post-Processing
# -------------------
def _postprocess(posts: List[Dict[str, Any]], max_words: int, include_hashtags: bool) -> List[Dict[str, Any]]:
    cleaned: List[Dict[str, Any]] = []
    for p in posts:
        title = sanitize_text(p.get("title", ""))
        body = sanitize_text(p.get("body", ""))

        # enforce soft word limit
        body = enforce_word_limit(body, max_words)

        hashtags = p.get("hashtags") if include_hashtags else []
        if include_hashtags:
            hashtags = [h.strip() for h in (hashtags or []) if isinstance(h, str) and h.startswith("#")]
            hashtags = dedupe_hashtags(hashtags)[:6]

        cleaned.append({
            "title": title,
            "body": body,
            "hashtags": hashtags
        })

    return [c for c in cleaned if c["body"]]  # filter empty

# -------------------
# Main Generator
# -------------------
def generate_posts(
    topic: str,
    tone: str = "Professional",
    audience: str | None = None,
    count: int = 3,
    include_hashtags: bool = False,
    include_cta: bool = False,
    max_words: int = 180,
    seed: str | None = None,
    style_notes: str | None = None,
) -> List[Dict[str, Any]]:
    """Generate LinkedIn posts using Gemini 2.5 Pro"""
    
    prompt = _build_prompt(
        topic=topic,
        tone=tone,
        audience=audience,
        count=count,
        include_hashtags=include_hashtags,
        include_cta=include_cta,
        max_words=max_words,
        seed=seed,
        style_notes=style_notes,
    )

    response = model.generate_content(prompt)
    text = response.text or ""

    data = _extract_json(text)
    posts = data.get("posts", [])

    return _postprocess(posts, max_words=max_words, include_hashtags=include_hashtags)[:count]