import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()

personality = "Serious"

if os.path.exists("temp_personality.txt"):
    with open("temp_personality.txt", "r", encoding="utf-8") as f:
        personality = f.read().strip()

language = "English"

if os.path.exists("temp_language.txt"):
    with open("temp_language.txt", "r", encoding="utf-8") as f:
        language = f.read().strip()

# ---------------------------
# Paths
# ---------------------------

ARTICLE_PATH = "data/articles/latest_article.txt"
SCRIPT_PATH = "data/scripts/latest_script.txt"

# ---------------------------
# Check article exists
# ---------------------------

if not os.path.exists(ARTICLE_PATH):
    raise FileNotFoundError(
        f"Article not found: {ARTICLE_PATH}"
    )

# ---------------------------
# Read article
# ---------------------------

with open(ARTICLE_PATH, "r", encoding="utf-8") as f:
    article_text = f.read()

print(f"Using article: {ARTICLE_PATH}")
print(f"Article Length: {len(article_text)} characters")

# ---------------------------
# LLM
# ---------------------------

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

# ---------------------------
# Prompt
# ---------------------------

prompt = PromptTemplate.from_template(
"""
You are a professional television news anchor.

Anchor Personality:
{personality}

Language:
{language}

Instructions:

If personality is Serious:
- Calm
- Professional
- Objective

If personality is Breaking News:
- Urgent and energetic
- Focus on latest developments

If personality is Dramatic:
- More emotional
- Strong storytelling style

Requirements:
- Start naturally
- Easy to understand
- Around 120-150 words
- Focus only on important facts
- Generate the entire script in {language}

Article:
{article}
"""
)

chain = prompt | llm

response = chain.invoke(
    {
        "article": article_text[:4000],
        "personality": personality,
        "language": language
    }
)

script = response.content

print("\nScript generated successfully.")
print(f"Length: {len(script)} characters")

# ---------------------------
# Save script
# ---------------------------

os.makedirs("data/scripts", exist_ok=True)

with open(SCRIPT_PATH, "w", encoding="utf-8") as f:
    f.write(script)

print(f"\nScript saved to: {SCRIPT_PATH}")