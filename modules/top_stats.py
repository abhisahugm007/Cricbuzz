import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import (
    PLAYER_BATTING_URL,
    PLAYER_BOWLING_URL,
    PLAYER_SEARCH_URL,
    PLAYER_STATS_URL,
)
from utils.helper import fetch_api_data


# -------------------------------
# 🔌 API Integration
# -------------------------------
def fetch_player_search(query):
    querystring = {"plrN": query}
    return fetch_api_data(PLAYER_SEARCH_URL, querystring)


def fetch_player_profile(player_id):
    return fetch_api_data(PLAYER_STATS_URL.format(player_id=player_id))


def fetch_batting_stats(player_id):
    return fetch_api_data(PLAYER_BATTING_URL.format(player_id=player_id))


def fetch_bowling_stats(player_id):
    return fetch_api_data(PLAYER_BOWLING_URL.format(player_id=player_id))


# -------------------------------
# 🖥️ Streamlit UI
# -------------------------------
def show_top_stats():
    st.set_page_config(page_title="Player Profile", layout="wide")
    st.title("🏏 Cricket Player Statistics")

    search_query = st.text_input("Search Player by Name")

    if search_query:
        results = fetch_player_search(search_query)
        print("results--->", results)
        if not results:
            st.warning("Possibly API limit reached. Please try again later.")
            st.stop()
        players = results.get("player", [])

        if not players:
            st.warning("No players found.")

        else:
            player_options = {
                f"{p.get('name', '')} ({p.get('teamName', '')})": p.get("id", "")
                for p in players
            }
            selected_player = st.selectbox(
                "Select Player:", options=list(player_options.keys())
            )
            player_id = player_options[selected_player]

            profile = fetch_player_profile(player_id)
            batting_data = fetch_batting_stats(player_id)
            bowling_data = fetch_bowling_stats(player_id)

            tab1, tab2, tab3 = st.tabs(
                ["👤 Profile", "🏏 Batting Stats", "🎯 Bowling Stats"]
            )

            # -------------------------------
            # 👤 Profile Tab
            # -------------------------------
            with tab1:
                st.markdown(
                    f"## {profile.get('name', '')} ({profile.get('nickName', '')})"
                )
                st.markdown(f"**Country:** {profile.get('intlTeam', '')}")
                st.markdown(f"**Date of Birth:** {profile.get('DoB', '')}")
                st.markdown(f"**Birthplace:** {profile.get('birthPlace', '')}")
                st.markdown(f"**Height:** {profile.get('height', '')}")
                st.markdown(f"**Role:** {profile.get('role', '')}")
                st.markdown(f"**Batting Style:** {profile.get('bat', '')}")
                st.markdown(f"**Bowling Style:** {profile.get('bowl', '')}")

                st.markdown("### 🏆 Teams Played For")
                st.write(profile.get("teams", "N/A"))

                st.markdown("### 📊 ICC Rankings")
                bat = profile.get("rankings", {}).get("bat", {})
                bowl = profile.get("rankings", {}).get("bowl", {})
                allr = profile.get("rankings", {}).get("all", {})

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown("#### 🏏 Batting")
                    st.markdown(f"- **Test Best Rank:** {bat.get('testBestRank', '')}")
                    st.markdown(f"- **ODI Best Rank:** {bat.get('odiBestRank', '')}")
                    st.markdown(f"- **T20 Best Rank:** {bat.get('t20BestRank', '')}")
                    st.markdown(f"- **Current ODI Rank:** {bat.get('odiRank', '')}")
                    st.markdown(f"- **ODI Diff Rank:** {bat.get('odiDiffRank', '')}")

                with col2:
                    st.markdown("#### 🎯 Bowling")
                    st.markdown(f"- **T20 Best Rank:** {bowl.get('t20BestRank', '')}")

                with col3:
                    st.markdown("#### 🧢 All-Round")
                    st.markdown(f"- **T20 Best Rank:** {allr.get('t20BestRank', '')}")

                st.markdown(
                    f"[🌐 View Full Profile]({profile.get('appIndex', {}).get('webURL', '')})"
                )

            # -------------------------------
            # 🏏 Batting Stats Tab
            # -------------------------------
            with tab2:
                excluded_rows = ["Balls", "Not Out", "Ducks", "300s", "400s"]
                if not batting_data or "values" not in batting_data:
                    st.warning("No batting data available for this player.")
                else:
                    batting_values = batting_data.get("values", [])
                    filtered_batting = [
                        row["values"]
                        for row in batting_values
                        if row["values"][0] not in excluded_rows
                    ]

                    batting_df = pd.DataFrame(
                        [row[1:] for row in filtered_batting],
                        columns=["Test", "ODI", "T20", "IPL"],
                        index=[row[0] for row in filtered_batting],
                    )

                    st.markdown("### 🏏 Batting Career Summary")
                    if "Matches" in batting_df.index:
                        total_matches = pd.to_numeric(
                            batting_df.loc["Matches"], errors="coerce"
                        ).sum()
                        st.metric("Total Matches", int(total_matches))
                    if "Runs" in batting_df.index:
                        total_runs = pd.to_numeric(
                            batting_df.loc["Runs"], errors="coerce"
                        ).sum()
                        st.metric("Total Runs", int(total_runs))

                    avg = (
                        batting_df.loc["Average"]
                        if "Average" in batting_df.index
                        else {}
                    )
                    sr = batting_df.loc["SR"] if "SR" in batting_df.index else {}

                    st.markdown(
                        f"**Average:** Test - {avg.get('Test', '')}, ODI - {avg.get('ODI', '')}, T20 - {avg.get('T20', '')}, IPL - {avg.get('IPL', '')}"
                    )
                    st.markdown(
                        f"**Strike Rate:** Test - {sr.get('Test', '')}, ODI - {sr.get('ODI', '')}, T20 - {sr.get('T20', '')}, IPL - {sr.get('IPL', '')}"
                    )

                    st.markdown("### 📊 Batting Career Statistics")
                    st.dataframe(batting_df, use_container_width=True)

            # -------------------------------
            # 🎯 Bowling Stats Tab
            # -------------------------------
            with tab3:
                if not bowling_data or "values" not in bowling_data:
                    st.warning("No Bowling data available for this player.")
                else:
                    bowling_values = bowling_data.get("values", [])
                    bowling_df = pd.DataFrame(
                        [row["values"][1:] for row in bowling_values],
                        columns=["Test", "ODI", "T20", "IPL"],
                        index=[row["values"][0] for row in bowling_values],
                    )

                    st.markdown("### 🎯 Bowling Career Summary")
                    if "Wickets" in bowling_df.index:
                        total_wickets = pd.to_numeric(
                            bowling_df.loc["Wickets"], errors="coerce"
                        ).sum()
                        st.metric("Total Wickets", int(total_wickets))

                    bbi = bowling_df.loc["BBI"] if "BBI" in bowling_df.index else {}
                    avg = bowling_df.loc["Avg"] if "Avg" in bowling_df.index else {}
                    eco = bowling_df.loc["Eco"] if "Eco" in bowling_df.index else {}

                    st.markdown(
                        f"**Best Bowling:** Test - {bbi.get('Test', '')}, ODI - {bbi.get('ODI', '')}, T20 - {bbi.get('T20', '')}, IPL - {bbi.get('IPL', '')}"
                    )
                    st.markdown(
                        f"**Average:** Test - {avg.get('Test', '')}, ODI - {avg.get('ODI', '')}, T20 - {avg.get('T20', '')}, IPL - {avg.get('IPL', '')}"
                    )
                    st.markdown(
                        f"**Economy:** Test - {eco.get('Test', '')}, ODI - {eco.get('ODI', '')}, T20 - {eco.get('T20', '')}, IPL - {eco.get('IPL', '')}"
                    )

                    st.markdown("### 📊 Bowling Career Statistics")
                    st.dataframe(bowling_df, use_container_width=True)
