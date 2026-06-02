from newspaper import Article
import os

# Read URL from Streamlit
with open("temp_url.txt", "r", encoding="utf-8") as f:
    url = f.read().strip()

from newspaper import Article, Config

config = Config()

config.browser_user_agent = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)

article = Article(
    url,
    config=config
)

article.download()
article.parse()

title = article.title
text = article.text

#print("\nTITLE:\n", title)
#print("\nARTICLE:\n", text)

# Create folder
os.makedirs("data/articles", exist_ok=True)

# Save article where generate_script.py expects it
article_path = "data/articles/latest_article.txt"

with open(article_path, "w", encoding="utf-8") as f:
    f.write(title + "\n\n" + text)

print(f"\nArticle saved to: {article_path}")