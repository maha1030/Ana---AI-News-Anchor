import streamlit as st
import subprocess
import sys
import os
import time
from database import init_db
import sqlite3

PYTHON = sys.executable

st.set_page_config(
    page_title="AI News Anchor",
    layout="wide"
)

init_db()

def save_broadcast(
    title,
    language,
    personality,
    article_path,
    script_path,
    audio_path,
    video_path
):

    conn = sqlite3.connect("ana.db")

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO broadcasts
    (
        title,
        language,
        personality,
        article_path,
        script_path,
        audio_path,
        video_path
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
    (
        title,
        language,
        personality,
        article_path,
        script_path,
        audio_path,
        video_path
    ))

    conn.commit()
    conn.close()

st.title("🎙️ Hey Ana here!")
st.markdown("_I Read the Web So You Don't Have To. I generate news broadcasts from any news article._")

# -------------------------
# Inputs
# -------------------------

selected_url = st.session_state.get("selected_url", "")

url = st.text_input(
    "Enter News URL",
    value=selected_url
)

personality = st.selectbox(
    "Anchor Personality",
    [
        "Serious",
        "Breaking News",
        "Dramatic"
    ]
)

language = st.selectbox(
    "Language",
    [
        "English",
        "Hindi",
        "Bengali",
        "Tamil"
    ]
)

# -------------------------
# Pipeline Runner
# -------------------------

def run_script(script_name):

    result = subprocess.run(
        [PYTHON, script_name],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        st.error(f"Error in {script_name}")
        st.code(result.stderr)
        st.stop()

    return result.stdout


# -------------------------
# Generate Button
# -------------------------

if st.button("Generate News Broadcast"):

    if not url.strip():
        st.error("Please enter a News URL.")
        st.stop()

    # Save URL for news_fetcher.py
    with open("temp_url.txt", "w", encoding="utf-8") as f:
        f.write(url)
        
    with open("temp_personality.txt", "w", encoding="utf-8") as f:
        f.write(personality)

    with open("temp_language.txt", "w", encoding="utf-8") as f:
        f.write(language)

    start_time = time.time()
    
    st.subheader("Generating News Broadcast")

    progress = st.progress(0)
    status = st.empty()

    status.info("📄 Fetching article...")
    run_script("news_fetcher.py")
    progress.progress(25)

    status.info("✍️ Generating script...")
    run_script("generate_script.py")
    progress.progress(50)

    status.info("🎤 Generating audio...")
    run_script("generate_audio.py")
    progress.progress(75)

    status.info("🎬 Generating video...")
    run_script("generate_video.py")
    progress.progress(100)

    elapsed = round(time.time() - start_time, 1)

    status.success(
        f"✅ Broadcast generated in {elapsed} seconds!"
    )
    
    with open("latest_video.txt", "r") as f:
        video_path = f.read().strip()

    with open("latest_audio.txt", "r") as f:
        audio_path = f.read().strip()

    article_path = "data/articles/latest_article.txt"
    script_path = "data/scripts/latest_script.txt"

    with open(article_path, "r", encoding="utf-8") as f:
        title = f.readline().strip()

    save_broadcast(
        title,
        language,
        personality,
        article_path,
        script_path,
        audio_path,
        video_path
    )

    # ==================================
    # Layout
    # ==================================

    col1, col2, col3 = st.columns([1, 1, 1])

    # ==================================
    # COLUMN 1
    # ==================================

    with col1:

        st.subheader("Anchor")

        avatar_path = "video/avatar.png"

        if os.path.exists(avatar_path):
            st.image(
                avatar_path,
                caption="AI News Anchor",
                width="stretch"
            )

    # ==================================
    # COLUMN 2
    # ==================================

    with col2:

        st.subheader("Article")

        article_path = "data/articles/latest_article.txt"

        if os.path.exists(article_path):

            with open(article_path, "r", encoding="utf-8") as f:

                st.text_area(
                    "Latest Article",
                    f.read(),
                    height=250
                )

        st.subheader("Generated Script")

        script_path = "data/scripts/latest_script.txt"

        if os.path.exists(script_path):

            with open(script_path, "r", encoding="utf-8") as f:

                st.text_area(
                    "News Script",
                    f.read(),
                    height=250
                )

    # ==================================
    # COLUMN 3
    # ==================================

    with col3:

        st.subheader("Audio")

        if os.path.exists(audio_path):
            st.audio(audio_path)

        st.subheader("Video")

        if os.path.exists(video_path):
            st.video(video_path)
            
            with open(video_path, "rb") as file:
                st.download_button(
                    "⬇ Download Video",
                    file,
                    file_name="news_broadcast.mp4",
                    mime="video/mp4"
                )
            
st.markdown("---")

st.markdown(
    """
    <div style='text-align: center; color: gray; padding: 20px;'>
        <p>ANA - AI News Anchor</p>
        <p>Built by Maha</p>
        <p>© 2026 Ana. All Rights Reserved.</p>
    </div>
    """,
    unsafe_allow_html=True
)