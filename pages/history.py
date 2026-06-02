import streamlit as st
import sqlite3
import os

st.title("📚 Broadcast History")

conn = sqlite3.connect("ana.db")

cursor = conn.cursor()

cursor.execute("""
SELECT
title,
language,
personality,
video_path,
created_at
FROM broadcasts
ORDER BY id DESC
""")

rows = cursor.fetchall()

conn.close()

for row in rows:

    title, language, personality, video_path, created_at = row

    with st.container(border=True):

        st.subheader(title)

        st.write(
            f"🌍 {language} | 🎭 {personality}"
        )

        st.caption(created_at)

        if os.path.exists(video_path):

            st.video(video_path)

            with open(video_path, "rb") as file:

                st.download_button(
                    "⬇ Download",
                    file,
                    file_name=os.path.basename(video_path),
                    mime="video/mp4",
                    key=video_path
                )