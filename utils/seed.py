# -------------------------------

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import psycopg2
from datetime import datetime
from config import (
    PLAYER_SEARCH_URL,
    PLAYER_STATS_URL,
    DB_CONFIG,
)
from utils.helper import fetch_api_data, cricket_players_list


def search_player(name):
    params = {"plrN": name}
    res = fetch_api_data(PLAYER_SEARCH_URL, params)

    return res.get("player", [])[0] if res.get("player") else None


# -------------------------------
# 🧾 Seeder Logic
# -------------------------------
def seed_from_api():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    player_profiles = []
    for name in cricket_players_list:
        try:
            basic = search_player(name)
            if not basic:
                print(f"❌ No data for {name}")
                continue

            pid = basic["id"]
            profile = fetch_api_data(PLAYER_STATS_URL.format(player_id=pid))
            if not profile:
                print(f"❌ No profile data for {name}")
                continue

            profile.pop("bio", "")  # Remove bio to save space
            player_profiles.append(profile)
            # Seed team
            team_name = profile.get("intlTeam", "Unknown")

            teams_played = profile.get("teamNameIds", [])
            team_id = "-1"
            for team in teams_played:
                if team.get("teamName") == team_name:
                    team_id = team.get("teamId", "UNK")
                    print(f"Team ID: {team['teamId']}, Team Name: {team['teamName']}")

            cur.execute(
                "INSERT INTO teams (team_id, team_name, country) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING",
                (
                    team_id,
                    team_name,
                    team_name,
                ),
            )

            # Seed player
            cur.execute(
                """
                INSERT INTO players (player_id, full_name, role, batting_style, bowling_style, country)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT DO NOTHING
            """,
                (
                    pid,
                    profile.get("name", name),
                    profile.get("role", ""),
                    profile.get("bat", ""),
                    profile.get("bowl", ""),
                    team_name,
                ),
            )

            # Seed player_stats
            # cur.execute(
            #     """
            #     INSERT INTO player_stats (player_id, format, matches_played, runs, wickets, batting_average, strike_rate, centuries)
            #     VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            #     ON CONFLICT DO NOTHING
            # """,
            #     (pid, "Test", 100, 5000, 50, 45.0, 80.0, 15),
            # )

            # # Seed recent batting
            # for row in profile.get("recentBatting", {}).get("rows", []):
            #     match_id = row["values"][0]
            #     opp_team = row["values"][1]
            #     score = row["values"][2].split("&")[0].strip()
            #     format = row["values"][3]
            #     date_str = row["values"][4]
            #     try:
            #         match_date = datetime.strptime(date_str, "%d %b %y").date()
            #     except:
            #         match_date = None

            #     cur.execute(
            #         """
            #         INSERT INTO matches (match_id, series_id, team1_id, team2_id, winner_id, venue_id, match_date,
            #         match_desc, format, result, margin, victory_type, toss_winner_id, toss_decision)
            #         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            #         ON CONFLICT DO NOTHING
            #     """,
            #         (
            #             match_id,
            #             "S001",
            #             team_name[:3].upper(),
            #             opp_team[:3].upper(),
            #             team_name[:3].upper(),
            #             "V001",
            #             match_date,
            #             f"{team_name} vs {opp_team}",
            #             format,
            #             "",
            #             "",
            #             "",
            #             "",
            #             "",
            #         ),
            #     )

            #     cur.execute(
            #         """
            #         INSERT INTO innings (match_id, innings_number, batting_team_id, runs, wickets, overs)
            #         VALUES (%s, %s, %s, %s, %s, %s)
            #         ON CONFLICT DO NOTHING
            #     """,
            #         (match_id, 1, team_name[:3].upper(), 250, 5, 50.0),
            #     )

            #     cur.execute(
            #         """
            #         INSERT INTO batting_performance (match_id, player_id, innings_number, runs, balls_faced,
            #         strike_rate, position, not_out)
            #         VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            #         ON CONFLICT DO NOTHING
            #     """,
            #         (
            #             match_id,
            #             pid,
            #             1,
            #             int(score.split("(")[0]) if "(" in score else 30,
            #             (
            #                 int(score.split("(")[1].replace(")", ""))
            #                 if "(" in score
            #                 else 40
            #             ),
            #             75.0,
            #             3,
            #             False,
            #         ),
            #     )

            # # Seed recent bowling
            # for row in profile.get("recentBowling", {}).get("rows", []):
            #     match_id = row["values"][0]
            #     opp_team = row["values"][1]
            #     wickets = row["values"][2].split("&")[0].strip()
            #     format = row["values"][3]
            #     date_str = row["values"][4]
            #     try:
            #         match_date = datetime.strptime(date_str, "%d %b %y").date()
            #     except:
            #         match_date = None

            #     cur.execute(
            #         """
            #         INSERT INTO bowling_performance (match_id, player_id, innings_number, overs, runs_conceded,
            #         wickets, economy)
            #         VALUES (%s, %s, %s, %s, %s, %s, %s)
            #         ON CONFLICT DO NOTHING
            #     """,
            #         (
            #             match_id,
            #             pid,
            #             2,
            #             10.0,
            #             40,
            #             int(wickets.split("-")[0]) if "-" in wickets else 0,
            #             4.0,
            #         ),
            #     )

        except Exception as e:
            print(f"⚠️ Error for {name}: {e}")
            continue

    conn.commit()
    conn.close()
    print("✅ Seeding complete.")


# -------------------------------
# 🚀 Run Seeder
# -------------------------------
if __name__ == "__main__":
    seed_from_api()
