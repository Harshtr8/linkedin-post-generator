import streamlit as st
from agent import generate_posts
from utils import download_posts_as_txt

# -------------------
# Streamlit Page Config
# -------------------
st.set_page_config(page_title="LinkedIn Post Generator", layout="wide")
st.title("🤖 LinkedIn Post Generator")

# -------------------
# Sidebar Controls
# -------------------
with st.sidebar:
    st.header("⚙️ Settings")
    post_count = st.slider("Number of posts", 3, 6, 3)
    tone = st.selectbox("Tone", ["Professional", "Casual", "Inspirational", "Persuasive", "Analytical"], 0)
    audience = st.text_input("Target audience (optional)", placeholder="e.g., Startup founders, B2B marketers")
    add_hashtags = st.checkbox("Add relevant hashtags")
    add_cta = st.checkbox("Add a strong call-to-action")
    max_words = st.slider("Max words per post", 120, 350, 180, step=10)

# -------------------
# Main Input Section
# -------------------
st.write("Enter a topic and generate multiple LinkedIn-ready post options 👇")

topic = st.text_input("Topic (required)", placeholder="e.g., Cold-start strategies for marketplaces")

col1, col2 = st.columns([1, 1])
with col1:
    seed = st.text_input("Optional seed details", placeholder="Any key points, examples, or angle to include")
with col2:
    style_notes = st.text_input("Optional style notes", placeholder="e.g., Use bullets; avoid buzzwords")

# -------------------
# Generate Posts Button
# -------------------
generate_clicked = st.button("Generate Posts")

if generate_clicked:
    if not topic.strip():
        st.error("⚠️ Please enter a topic.")
        st.stop()

    with st.spinner("✍️ Generating LinkedIn posts..."):
        posts = generate_posts(
            topic=topic.strip(),
            tone=tone,
            audience=audience.strip() or None,
            count=post_count,
            include_hashtags=add_hashtags,
            include_cta=add_cta,
            max_words=max_words,
            seed=seed.strip() or None,
            style_notes=style_notes.strip() or None,
        )

    if not posts:
        st.error("❌ Could not generate posts. Please try again with different inputs.")
    else:
        st.success(f"✅ Generated {len(posts)} LinkedIn posts.")
        all_text = []
        for idx, p in enumerate(posts, 1):
            st.markdown(f"### Option {idx}: {p.get('title','')}".strip())
            st.write(p.get("body", "").strip())
            if p.get("hashtags"):
                st.caption(" ".join(p["hashtags"]))
            st.divider()

            # prepare text for download
            rendered = p.get("title", "").strip()
            if rendered:
                rendered += "\n"
            rendered += p.get("body", "").strip()
            if p.get("hashtags"):
                rendered += "\n" + " ".join(p["hashtags"])
            all_text.append(rendered.strip())

        # -------------------
        # Download Button
        # -------------------
        buf = download_posts_as_txt(all_text)
        st.download_button(
            label="⬇️ Download all posts as .txt",
            data=buf.getvalue(),
            file_name="linkedin_posts.txt",
            mime="text/plain",
        )

# -------------------
# Footer
# -------------------
st.markdown("---")
st.caption("🚀 Built with Streamlit + Google Gemini 2.5 Pro")