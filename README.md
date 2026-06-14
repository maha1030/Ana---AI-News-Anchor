# 🎙️ ANA - AI News Anchor

ANA (AI News Anchor) is an AI-powered news broadcasting platform that transforms live news articles into professional multilingual news broadcasts.

The application automatically extracts news content from online articles, generates anchor-style scripts using Large Language Models (LLMs), converts scripts into natural-sounding speech with neural Text-to-Speech, and creates downloadable video broadcasts with synchronized subtitles.

---

## ✨ Features

* 📰 Real-time news aggregation
* 🔗 Generate broadcasts from any news article URL
* 🤖 AI-powered script generation using Groq LLMs
* 🎭 Multiple anchor personalities

  * Serious
  * Breaking News
  * Dramatic
* 🌍 Multilingual support

  * English
  * Hindi
  * Bengali
  * Tamil
* 🎤 Neural Text-to-Speech using Edge-TTS
* 📝 Automatic subtitle generation
* 🎬 Automated video generation using MoviePy
* 📚 Broadcast history management using SQLite
* ⬇️ Download generated video broadcasts
* 🎨 Interactive Streamlit interface

---

## 🏗️ System Workflow

```text
News Article
      ↓
Article Extraction
      ↓
AI Script Generation
      ↓
Multilingual Text-to-Speech
      ↓
Subtitle Generation
      ↓
Video Rendering
      ↓
Broadcast History Storage
```

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI & NLP

* LangChain
* Groq API

### News Processing

* NewsAPI
* Newspaper3k

### Speech Synthesis

* Edge-TTS

### Video Generation

* MoviePy
* FFmpeg
* ImageIO

### Database

* SQLite

### Version Control

* Git
* GitHub

---

## 📂 Project Structure

```text
ANA/
│
├── app.py
├── database.py
├── news_api.py
├── news_fetcher.py
├── generate_script.py
├── generate_audio.py
├── generate_video.py
│
├── pages/
│   ├── generate_broadcast.py
│   └── history.py
│
├── video/
│   ├── avatar.png
│   └── background.mp4
│
├── audio/
├── subtitles/
├── data/
│
└── requirements.txt
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/maha1030/Ana---AI-News-Anchor.git
cd Ana---AI-News-Anchor
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
NEWS_API_KEY=your_news_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📸 Screenshots

Add screenshots here after generating a few broadcasts.

Examples:

* Home Page
* News Feed Dashboard
* Broadcast Generation Page
* Generated Video Output
* Broadcast History

---

## 🚀 Future Enhancements

* AI avatar lip-syncing
* Cloud-based video rendering
* Personalized news recommendations
* User authentication
* Podcast generation support
* Cloud storage integration

---

## 👩‍💻 Author

**Maha**

Built to explore the intersection of Artificial Intelligence, Journalism, Speech Synthesis, and Automated Media Generation.

---

## 📄 License

This project is licensed under the MIT License.
