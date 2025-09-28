import streamlit as st


def show_home():
    st.title("🏏 Welcome to Cricbuzz LiveStats")
    st.markdown(
        """
    This dashboard gives you real-time cricket insights, player stats, and SQL-powered analytics.
    Use the sidebar to explore different modules.
    """
    )
