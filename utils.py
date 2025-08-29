import io
import re

# -------------------
# Simple Profanity Filter (extendable)
# -------------------
PROFANITY = {
    # simple mapping, can be extended
    "damn": "darn",
    "hell": "heck",
    "shit": "bad",
    "fuck": "bad",
}

def sanitize_text(text: str) -> str:
    """Cleans up text by removing profanity, fixing spacing."""
    out = text

    # replace profanity
    for bad, repl in PROFANITY.items():
        out = re.sub(rf"\b{re.escape(bad)}\b", repl, out, flags=re.IGNORECASE)

    # normalize whitespace
    out = re.sub(r"[ \t]+\n", "\n", out)  # remove trailing spaces
    out = re.sub(r"\n{3,}", "\n\n", out)  # collapse multiple newlines
    return out.strip()

# -------------------
# Word Limit
# -------------------
def enforce_word_limit(text: str, max_words: int) -> str:
    """Trim text to a maximum number of words, ending cleanly if possible."""
    words = re.findall(r"\S+", text)
    if len(words) <= max_words:
        return text

    trimmed = " ".join(words[:max_words])
    # try to end at a sentence boundary
    m = re.search(r"(.*?[\.!?])(\s|$)", trimmed)
    return (m.group(1) if m else trimmed).strip()

# -------------------
# Hashtags
# -------------------
def dedupe_hashtags(tags: list[str]) -> list[str]:
    """Remove duplicate hashtags (case-insensitive)."""
    seen = set()
    out = []
    for t in tags:
        tl = t.lower()
        if tl not in seen:
            out.append(t)
            seen.add(tl)
    return out

# -------------------
# Download as Text File
# -------------------
def download_posts_as_txt(posts: list[str]) -> io.BytesIO:
    """Prepare LinkedIn posts for download as .txt file."""
    buf = io.StringIO()
    for i, p in enumerate(posts, 1):
        buf.write(f"=== Post {i} ===\n{p}\n\n")
    raw = buf.getvalue()
    buf.close()
    out = io.BytesIO(raw.encode("utf-8"))
    return out
