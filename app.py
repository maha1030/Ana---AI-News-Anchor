import streamlit as st
from news_api import get_news
from database import init_db

st.markdown("""
<div style="
padding:30px;
border-radius:20px;
background:linear-gradient(135deg,#232526,#414345);
color:white;
margin-bottom:30px;
">

<h1>🎙 ANA - AI News Anchor</h1>

<p>
The Next Generation of AI Journalism.
Transforming live news articles into
AI-generated broadcasts in multiple
languages and styles.
</p>

</div>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="AI News Anchor",
    layout="wide"
)

init_db()

st.markdown("""
<style>

.card-title {
    min-height: 90px;
    font-size: 18px;
    font-weight: bold;
}

.card-desc {
    min-height: 120px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("### Today's News")

# -------------------------
# Styling
# -------------------------
st.markdown("""
<style>

/* News Cards */

div[data-testid="stVerticalBlockBorderWrapper"]{
    border-radius:18px;
    border:1px solid rgba(255,255,255,0.08);
    padding:10px;
    background-color:#1E1E1E;
    transition:all 0.3s ease;
}

/* Hover Effect */

div[data-testid="stVerticalBlockBorderWrapper"]:hover{
    transform:translateY(-4px);
    box-shadow:0px 8px 20px rgba(0,0,0,0.4);
}

/* Section Headers */

h2{
    margin-top:30px;
    margin-bottom:20px;
}

/* Card Title */

.card-title{
    min-height:90px;
    font-size:18px;
    font-weight:600;
    line-height:1.4;
}

/* Card Description */

.card-desc{
    min-height:110px;
    color:#CFCFCF;
    font-size:14px;
}

/* Buttons */

.stButton button{
    width:100%;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# News Section Function
# -------------------------
def show_news_section(title, category=None):

    st.header(title)

    articles = get_news(category)

    if not articles:
        st.warning("No news available.")
        return

    # 3 cards per row
    for i in range(0, min(len(articles), 6), 3):

        cols = st.columns(3)

        for j in range(3):

            if i + j >= len(articles):
                break

            article = articles[i + j]

            with cols[j]:

                with st.container(border=True):

                    # News Image
                    if article.get("urlToImage"):
                        st.markdown(
                            f"""
                            <img src="{article['urlToImage']}"
                                style="
                                width:100%;
                                height:220px;
                                object-fit:cover;
                                border-radius:10px;">
                            """,
                            unsafe_allow_html=True
                        )

                    # Title
                    st.markdown(
                        f"""
                        <div class="card-title">
                            {article['title']}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    # Description
                    if article.get("description"):

                        st.markdown(
                            f"""
                            <div class="card-desc">
                                {article['description'][:150]}...
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    # Read Article Button
                    st.link_button(
                        "📖 Read Article",
                        article["url"]
                    )

                    # Generate Broadcast Button
                    if st.button(
                        "🎙️ Generate Broadcast",
                        key=f"{title}_{i}_{j}"
                    ):

                        st.session_state["selected_url"] = article["url"]

                        st.switch_page("pages/generate_broadcast.py")

                        st.divider()


# -------------------------
# Sections
# -------------------------
show_news_section(
    "🔥 Breaking News"
)

show_news_section(
    "💼 Business",
    "business"
)

show_news_section(
    "💻 Technology",
    "technology"
)

show_news_section(
    "⚽ Sports",
    "sports"
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