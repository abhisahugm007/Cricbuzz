import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import LIVE_URL, SCORECARD_URL
from utils.helper import fetch_api_data


# -------------------------------
# 🔌 API Integration Placeholder
# -------------------------------
def fetch_live_matches():
    Live_match = fetch_api_data(LIVE_URL)
    matches = []

    for type_match in Live_match.get("typeMatches", []):
        for series_match in type_match.get("seriesMatches", []):
            series_data = series_match.get("seriesAdWrapper", {})
            for match in series_data.get("matches", []):
                info = match.get("matchInfo", {})
                matches.append(
                    {
                        "match_id": info.get("matchId"),
                        "match_desc": info.get("matchDesc"),
                        "match_format": info.get("matchFormat"),
                        "team1": info.get("team1", {}).get("teamName"),
                        "team2": info.get("team2", {}).get("teamName"),
                        "venue": info.get("venueInfo", {}).get("ground"),
                        "status": info.get("status"),
                    }
                )
    print(f"Fetched {matches} live matches.")
    return matches


def fetch_scorecard(match_id):
    scorecard_url = SCORECARD_URL.format(match_id=match_id)
    scard = fetch_api_data(scorecard_url)
    scorecards = []

    for match_scard in scard.get("scorecard", []):
        if match_scard.get("inningsid"):
            batting = [
                {
                    "Name": b["name"],
                    "Runs": b["runs"],
                    "Balls": b["balls"],
                    "4s": b["fours"],
                    "6s": b["sixes"],
                    "SR": float(b["strkrate"]),
                    "Dismissal": b["outdec"] or "Do not Bat",
                }
                for b in match_scard.get("batsman", [])
            ]

            bowling = [
                {
                    "Name": bw["name"],
                    "Overs": bw["overs"],
                    "Maidens": bw["maidens"],
                    "Runs": bw["runs"],
                    "Wickets": bw["wickets"],
                    "Economy": float(bw["economy"]),
                }
                for bw in match_scard.get("bowler", [])
            ]

            scorecards.append(
                {
                    "Innings": match_scard["batteamname"],
                    "Score": f"{match_scard['score']}/{match_scard['wickets']} ({match_scard['overs']} ov)",
                    "Run Rate": match_scard["runrate"],
                    "Extras": match_scard.get("extras", {}).get("total", 0),
                    "Batting": batting,
                    "Bowling": bowling,
                }
            )
    return scorecards


# -------------------------------
# 🖥️ Streamlit UI
# -------------------------------
def show_live_matches():
    st.set_page_config(page_title="Live Cricket Scores", layout="wide")
    st.title("🏏 Cricbuzz Live Match Dashboard")

    matches = fetch_live_matches()

    if not matches:
        st.info("No live matches at the moment.")
        return

    # 🔐 Ensure unique labels by embedding match_id
    match_labels = [
        f"{m['team1']} vs {m['team2']} - {m['match_desc']} ({m['match_format']}) [ID: {m['match_id']}]"
        for m in matches
    ]
    match_map = {label: m for label, m in zip(match_labels, matches)}

    selected_label = st.selectbox("Select a live match:", options=match_labels)
    selected_match = match_map[selected_label]
    match_id = selected_match["match_id"]

    # 🏟️ Match Info
    st.markdown(f"### 📍 {selected_match['team1']} vs {selected_match['team2']}")
    st.markdown(f"**Match Format:** {selected_match['match_format']}")
    st.markdown(f"**Venue:** {selected_match['venue']}")
    st.markdown(f"**Status:** {selected_match['status']}")

    # 📊 Scorecard
    scorecards = fetch_scorecard(match_id)
    if not scorecards:
        st.warning("No scorecard data available.")
        return

    for sc in scorecards:
        st.subheader(f"Innings: {sc['Innings']}")
        st.markdown(
            f"**Score:** {sc['Score']} | **Run Rate:** {sc['Run Rate']} | **Extras:** {sc['Extras']}"
        )

        st.markdown("#### 🏏 Batting Scorecard")
        st.dataframe(pd.DataFrame(sc["Batting"]), use_container_width=True)

        st.markdown("#### 🎯 Bowling Scorecard")
        st.dataframe(pd.DataFrame(sc["Bowling"]), use_container_width=True)
