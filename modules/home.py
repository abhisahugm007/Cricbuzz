import streamlit as st

# from utils.helper import show_footer


def show_home():
    st.markdown(
        "<h1 style='text-align: center;'>🏏 Cricbuzz LiveStats</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        """
    <div style='text-align: center; font-size: 18px;'>
        Real-time cricket insights, player analytics, and SQL-powered dashboards<br>
        <span style='color: #00BFFF;'>Built for fans, analysts, and developers alike</span>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("### 🔍 What You Can Explore")
    st.markdown(
        """
    - 📺 **Live Matches**: Real-time scores and match details  
    - 📊 **Top Stats**: Format-wise batting and bowling leaders  
    - 🧮 **SQL Dashboard**: Run custom queries on seeded data  
    - 🛠️ **CRUD Operations**: Add, update, or delete player stats  
    """
    )

    st.markdown("### 🚀 Getting Started")
    st.info(
        "Use the sidebar to navigate between modules. All data is powered by the Cricbuzz API and stored in a PostgreSQL backend."
    )

    # show_footer()
