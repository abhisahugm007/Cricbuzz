import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pandas as pd
import psycopg2
import streamlit as st

from utils.db_connection import DB_CONFIG


# Helper function
def get_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    return conn, conn.cursor()


def fetch_one(player_id=None, player_name=None):
    conn, cursor = get_connection()
    query = "SELECT * FROM most_run_stats WHERE 1=1"
    params = []
    if player_id:
        query += " AND player_id=%s"
        params.append(player_id)
    if player_name:
        query += " AND player_name ILIKE %s"
        params.append(f"%{player_name}%")
    cursor.execute(query, tuple(params))
    row = cursor.fetchall()
    cursor.close()
    conn.close()
    return row


# -------------------
# CRUD Operations
# -------------------


# CREATE
def insert_data(player_id, player_name, matches, innings, runs, average):
    conn, cursor = get_connection()
    try:
        cursor.execute(
            """
            INSERT INTO most_run_stats (player_id, player_name, matches, innings, runs, average)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (player_id) DO NOTHING
            """,
            (player_id, player_name, matches, innings, runs, average),
        )
        conn.commit()
        st.success(f"✅ Player {player_name} inserted successfully!")
    except Exception as e:
        st.error(f"❌ Error inserting player {player_name}: {e}")
    finally:
        cursor.close()
        conn.close()


# READ
def read_data(player_id=None, player_name=None):
    conn, cursor = get_connection()
    query = "SELECT * FROM most_run_stats WHERE 1=1"
    params = []
    if player_id:
        query += " AND player_id=%s"
        params.append(player_id)
    if player_name:
        query += " AND player_name ILIKE %s"
        params.append(f"%{player_name}%")
    cursor.execute(query, tuple(params))
    rows = cursor.fetchall()
    df = pd.DataFrame(
        rows,
        columns=["player_id", "player_name", "matches", "innings", "runs", "average"],
    )
    cursor.close()
    conn.close()
    return df


# UPDATE
def update_data(
    player_id, player_name=None, matches=None, innings=None, runs=None, average=None
):
    conn, cursor = get_connection()
    try:
        # Fetch existing data
        cursor.execute("SELECT * FROM most_run_stats WHERE player_id=%s", (player_id,))
        old = cursor.fetchone()
        if not old:
            st.error(f"❌ No record found with Player ID {player_id}")
            return

        old_dict = {
            "player_id": old[0],
            "player_name": old[1],
            "matches": old[2],
            "innings": old[3],
            "runs": old[4],
            "average": old[5],
        }

        # Use old values if new not provided
        new_player_name = player_name if player_name else old_dict["player_name"]
        new_matches = matches if matches else old_dict["matches"]
        new_innings = innings if innings else old_dict["innings"]
        new_runs = runs if runs else old_dict["runs"]
        new_average = average if average else old_dict["average"]

        cursor.execute(
            """
            UPDATE most_run_stats
            SET player_name=%s, matches=%s, innings=%s, runs=%s, average=%s
            WHERE player_id=%s
            """,
            (
                new_player_name,
                new_matches,
                new_innings,
                new_runs,
                new_average,
                player_id,
            ),
        )
        conn.commit()
        st.success(f"✅ Player ID {player_id} updated successfully!")
    except Exception as e:
        st.error(f"❌ Error Updating player: {e}")
    finally:
        cursor.close()
        conn.close()


# DELETE
def delete_data(player_id, confirmation_text):
    conn, cursor = get_connection()
    try:
        cursor.execute(
            "SELECT player_name FROM most_run_stats WHERE player_id=%s", (player_id,)
        )
        row = cursor.fetchone()
        if not row:
            st.error(f"❌ No player found with ID {player_id}")
            return
        player_name = row[0]

        if confirmation_text.strip() == f"Delete {player_name}":
            cursor.execute(
                "DELETE FROM most_run_stats WHERE player_id=%s", (player_id,)
            )
            conn.commit()
            st.success(f"🗑️ Player {player_name} deleted successfully!")
        else:
            st.warning(f"⚠️ Type exactly: Delete {player_name} to confirm.")
    except Exception as e:
        st.error(f"❌ Error Deleting player with ID {player_id}: {e}")
    finally:
        cursor.close()
        conn.close()


# -------------------
# Streamlit UI
# -------------------
def show_crud_operations():
    st.set_page_config(page_title="Cricket CRUD", page_icon="🏏", layout="wide")
    st.title("🏏 Cricket Player Stats - CRUD Dashboard")

    tab1, tab2, tab3, tab4 = st.tabs(["➕ Insert", "📖 Read", "✏️ Update", "🗑️ Delete"])

    # INSERT
    with tab1:
        st.subheader("Insert New Player")
        with st.form("insert_form", clear_on_submit=True):
            c1, c2 = st.columns(2)
            with c1:
                player_id = st.number_input("Player ID", step=1)
                player_name = st.text_input("Player Name")
                matches = st.number_input("Matches", step=1)
            with c2:
                innings = st.number_input("Innings", step=1)
                runs = st.number_input("Runs", step=1)
                average = st.number_input("Average", format="%.2f")
            submit = st.form_submit_button("Insert Player 🚀")
            if submit:
                insert_data(player_id, player_name, matches, innings, runs, average)

    # READ
    with tab2:
        st.subheader("Search Players")
        search_id = st.text_input("Search by Player ID")
        search_name = st.text_input("Search by Player Name")
        df = read_data(
            player_id=int(search_id) if search_id.strip().isdigit() else None,
            player_name=search_name if search_name.strip() else None,
        )
        st.dataframe(df, use_container_width=True)

    # UPDATE
    with tab3:
        st.subheader("Update Player Data")
        with st.form("update_form"):
            player_id = st.number_input("Player ID (to update)", step=1)
            st.markdown("👉 Leave optional field blank if you don't want to update it")
            player_name = st.text_input("New Player Name (optional)")
            matches = st.number_input("Matches (optional)", step=1, value=0)
            innings = st.number_input("Innings (optional)", step=1, value=0)
            runs = st.number_input("Runs (optional)", step=1, value=0)
            average = st.number_input("Average (optional)", format="%.2f", value=0.00)
            submit = st.form_submit_button("Update Player ✏️")
            if submit:
                update_data(
                    player_id,
                    player_name if player_name else None,
                    matches if matches > 0 else None,
                    innings if innings > 0 else None,
                    runs if runs > 0 else None,
                    average if average > 0 else None,
                )

    # DELETE
    with tab4:
        st.subheader("Delete Player")
        with st.form("delete_form"):
            player_id = st.number_input("Player ID (to delete)", step=1)
            confirmation_text = st.text_input(
                "Type confirmation (e.g., Delete Virat Kohli)"
            )
            submit = st.form_submit_button("Delete Player 🗑️")
            if submit:
                delete_data(player_id, confirmation_text)
