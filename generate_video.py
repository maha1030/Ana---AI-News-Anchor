import os
import sys
from datetime import datetime

from moviepy.editor import (
    AudioFileClip,
    VideoFileClip,
    ImageClip,
    TextClip,
    CompositeVideoClip
)

import pysrt

if sys.platform == "win32":
    os.environ["IMAGEIO_FFMPEG_EXE"] = r"C:\Users\R Amutha\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.1-full_build\bin\ffmpeg.exe"

# -----------------------------------
# Load latest generated audio
# -----------------------------------

with open("latest_audio.txt", "r") as f:
    AUDIO_PATH = f.read().strip()

BG_PATH = "video/background.mp4"
AVATAR_PATH = "video/avatar.png"
SRT_PATH = "subtitles/news.srt"

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

OUTPUT_PATH = f"video/history/broadcast_{timestamp}.mp4"

os.makedirs("video/history", exist_ok=True)

# -----------------------------------
# Create Video
# -----------------------------------

def create_video():

    print("=" * 60)
    print("USING AUDIO:", AUDIO_PATH)
    print("OUTPUT VIDEO:", OUTPUT_PATH)
    print("=" * 60)

    audio = AudioFileClip(AUDIO_PATH)

    print("Audio Duration:", audio.duration)

    # Background video WITHOUT audio
    bg_clip = VideoFileClip(BG_PATH).without_audio()

    bg = (
        bg_clip
        .loop(duration=audio.duration)
        .resize(height=720)
    )

    # Avatar
    avatar = (
        ImageClip(AVATAR_PATH)
        .set_duration(audio.duration)
        .resize(height=300)
        .set_position(("center", "bottom"))
    )

    subtitles = []

    # -----------------------------------
    # Subtitles
    # -----------------------------------

    if os.path.exists(SRT_PATH):

        try:

            subs = pysrt.open(SRT_PATH)

            for sub in subs:

                start_time = sub.start.ordinal / 1000

                duration = (
                    sub.end.ordinal -
                    sub.start.ordinal
                ) / 1000

                txt = (
                    TextClip(
                        sub.text,
                        fontsize=40,
                        color="white",
                        bg_color="black",
                        font="Arial"
                    )
                    .set_start(start_time)
                    .set_duration(duration)
                    .set_position(("center", "bottom"))
                )

                subtitles.append(txt)

        except Exception as e:
            print("Subtitle Error:", e)

    # -----------------------------------
    # Final Video
    # -----------------------------------

    final = CompositeVideoClip(
        [bg, avatar] + subtitles
    )

    final = final.set_audio(audio)

    final.write_videofile(
        OUTPUT_PATH,
        fps=24,
        codec="libx264",
        audio_codec="aac",
        temp_audiofile="temp_audio.m4a",
        remove_temp=True
    )

    # Save latest video path
    with open("latest_video.txt", "w") as f:
        f.write(OUTPUT_PATH)

    # Cleanup
    audio.close()
    bg_clip.close()
    final.close()

    print("Video saved:", OUTPUT_PATH)


if __name__ == "__main__":
    create_video()