import sys
import subprocess

PYTHON = sys.executable  # THIS forces venv python

print("\n=== AI News Anchor Pipeline ===\n")

print("Running news_fetcher.py...")
subprocess.run([PYTHON, "news_fetcher.py"])

print("\nRunning generate_script.py...")
subprocess.run([PYTHON, "generate_script.py"])

print("\nRunning generate_audio.py...")
subprocess.run([PYTHON, "generate_audio.py"])

print("\nDone!")
print("Script: news_script.txt")
print("Audio: audio/news_audio.mp3")