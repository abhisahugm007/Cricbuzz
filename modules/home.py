# import streamlit as st

# # from utils.helper import show_footer


# def show_home():
#     st.markdown(
#         "<h1 style='text-align: center;'>🏏 Cricbuzz LiveStats</h1>",
#         unsafe_allow_html=True,
#     )
#     st.markdown(
#         """
#     <div style='text-align: center; font-size: 18px;'>
#         Real-time cricket insights, player analytics, and SQL-powered dashboards<br>
#         <span style='color: #00BFFF;'>Built for fans, analysts, and developers alike</span>
#     </div>
#     """,
#         unsafe_allow_html=True,
#     )

#     st.markdown("### 🔍 What You Can Explore")
#     st.markdown(
#         """
#     - 📺 **Live Matches**: Real-time scores and match details
#     - 📊 **Top Stats**: Format-wise batting and bowling leaders
#     - 🧮 **SQL Dashboard**: Run custom queries on seeded data
#     - 🛠️ **CRUD Operations**: Add, update, or delete player stats
#     """
#     )

#     st.markdown("### 🚀 Getting Started")
#     st.info(
#         "Use the sidebar to navigate between modules. All data is powered by the Cricbuzz API and stored in a PostgreSQL backend."
#     )

#     # show_footer()


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
        A modular cricket analytics dashboard powered by Cricbuzz API, PostgreSQL, and Streamlit.<br>
        <span style='color: #00BFFF;'>Track live matches, explore player stats, and run custom SQL queries—all in one place.</span>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("### 🛠️ Tools & Technologies Used")
    st.markdown(
        """
    - **Frontend**: Streamlit  
    - **Backend**: Python, PostgreSQL  
    - **API Source**: Cricbuzz (via RapidAPI)  
    - **ETL & Seeding**: Custom Python scripts  
    - **Modular Design**: Multi-page architecture with centralized routing  
    """
    )

    st.markdown("### 📋 How to Use")
    st.markdown(
        """
    - Use the **sidebar dropdown** to navigate between modules:
        - 🏠 Home  
        - 📺 Live Matches  
        - 📊 Top Stats  
        - 🧮 SQL Dashboard  
        - 🛠️ CRUD Operations  
    - All data is fetched live or seeded into your database for analytics.
    - You can run SQL queries, view top performers, and manage player records.
    """
    )

    st.markdown("### 📁 Project Documentation & Folder Structure")
    st.markdown(
        """
    Full source code, setup instructions, and architecture overview are available on GitHub:  
    🔗 [View Project Repository](https://github.com/abhisahugm007/Cricbuzz)
    """
    )

    st.markdown("### 🧑‍💻 About the Developer")
    st.markdown(
        """
    <div style='font-size: 15px;'>
        Developed by <strong>Abhishek Sahu</strong><br>
        📧 <a href='mailto:abhisahuofficial@gmail.com'>abhisahuofficial@gmail.com</a>  
        📞 <a href='tel:+91123456789'>+91 123456789</a><br>
        💼 <a href='https://www.linkedin.com/in/abhisheksahu007/' target='_blank'>LinkedIn</a>  
        🧑‍💻 <a href='https://github.com/abhisahugm007/' target='_blank'>GitHub</a><br>
        <span style='font-size: 13px; color: gray;'>© Cricbuzz LiveStats v1.0.0</span>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # show_footer()
