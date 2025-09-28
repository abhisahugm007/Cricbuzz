import streamlit as st

# -------------------------------
# 📄 Page Imports
# -------------------------------
from pages.home import show_home
from pages.live_matches import show_live_matches
from pages.top_stats import show_top_stats
from pages.sql_dashboard import show_sql_dashboard
from pages.crud_operations import show_crud_operations

# -------------------------------
# 🧭 Sidebar Navigation
# -------------------------------
st.set_page_config(page_title="Cricbuzz LiveStats", layout="wide")
st.sidebar.title("📂 Navigation")
page = st.sidebar.selectbox(
    "Choose a page",
    [
        "🏠 Home",
        "📺 Live Matches",
        "📊 Top Stats",
        "🧮 SQL Dashboard",
        "🛠️ CRUD Operations",
    ],
)

# -------------------------------
# 🚀 Page Routing
# -------------------------------
if page == "🏠 Home":
    show_home()
elif page == "📺 Live Matches":
    show_live_matches()
elif page == "📊 Top Stats":
    show_top_stats()
elif page == "🧮 SQL Dashboard":
    show_sql_dashboard()
elif page == "🛠️ CRUD Operations":
    show_crud_operations()

st.markdown("""---""")
st.markdown(
    """
<div style='text-align: center; font-size: 14px; color: gray; padding-top: 10px;'>
    Made with ❤️ by <strong>Abhishek Sahu</strong><br>
    📧 <a href='mailto:abhisahuofficial@gmail.com'>abhisahuofficial@gmail.com</a> &nbsp; | &nbsp; 📞 <a href='tel:+91123456789'>+91 123456789</a><br>
    💼 <a href='https://www.linkedin.com/in/abhisheksahu007/' target='_blank'>LinkedIn</a> &nbsp; | &nbsp; 🧑‍💻 <a href='https://github.com/abhisahugm007/' target='_blank'>GitHub</a><br>
    <span style='font-size: 12px;'>🛠️ Cricbuzz LiveStats v1.0.0</span>
</div>
""",
    unsafe_allow_html=True,
)
