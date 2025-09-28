import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import psycopg2
import pandas as pd
from utils.sql_queries import sql_queries
from config import DB_CONFIG


# -------------------------------
# 🔧 Run DB Query
# -------------------------------
def run_query(query):
    conn = psycopg2.connect(**DB_CONFIG)
    try:
        df = pd.read_sql_query(query, conn)
        return df
    except Exception as e:
        st.error(f"Query failed: {e}")
        return None
    finally:
        conn.close()


# -------------------------------
# 🎯 UI Layout
# -------------------------------
def show_sql_dashboard():
    st.set_page_config(page_title="Cricket SQL Analytics", layout="wide")
    st.title("🏏 Cricket SQL Analytics Dashboard")

    st.markdown(
        """
    Welcome to the interactive cricket analytics platform. Choose a question from the dropdown below and click **Execute Query** to view results.
    """
    )

    selected_qid = st.selectbox(
        "Choose a SQL Question",
        options=list(sql_queries.keys()),
        format_func=lambda x: f"{x}. {sql_queries[x]['label']}",
    )
    query = sql_queries[selected_qid]["query"]

    with st.expander("📄 Preview SQL Query"):
        st.code(query, language="sql")

    if st.button("🚀 Execute Query"):
        result_df = run_query(query)
        if result_df is not None and not result_df.empty:
            st.success(
                f"✅ Query executed successfully! Found {len(result_df)} records."
            )
            st.dataframe(result_df, use_container_width=True)
            st.download_button(
                "📥 Download CSV",
                result_df.to_csv(index=False),
                file_name="query_results.csv",
            )
        else:
            st.warning("No results found or query failed.")

    st.markdown("---")
    st.caption("Built by Abhishek Sahu • Powered by real cricket data and PostgreSQL")
