# -------------------------------

import re
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import psycopg2
from datetime import datetime
from config import (
    PLAYER_BATTING_URL,
    PLAYER_BOWLING_URL,
    PLAYER_SEARCH_URL,
    PLAYER_STATS_URL,
    DB_CONFIG,
    VENUES,
)
from utils.helper import PLAYER_ID_SEED, VENUE_IDS, fetch_api_data, cricket_players_list


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
            # Check if player already exists
            cur.execute("SELECT * FROM players WHERE full_name = %s", (name,))
            if cur.fetchone():
                print(f"ℹ️ Player {name} already exists. Skipping...")
            else:
                basic = search_player(name)
                if not basic:
                    print(f"❌ No data for {name}")
                else:
                    pid = basic["id"]
                    profile = fetch_api_data(PLAYER_STATS_URL.format(player_id=pid))
                    if not profile:
                        print(f"❌ No profile data for {name}")
                    else:
                        profile.pop("bio", "")  # Remove bio to save space
                        player_profiles.append(profile)
                        # Seed team
                        team_name = profile.get("intlTeam", "Unknown")

                        teams_played = profile.get("teamNameIds", [])
                        team_id = "-1"
                        for team in teams_played:
                            if team.get("teamName") == team_name:
                                team_id = team.get("teamId", "UNK")
                                print(
                                    f"Team ID: {team['teamId']}, Team Name: {team['teamName']}"
                                )

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
        except Exception as e:
            print(f"⚠️ Error for {name}: {e}")
            continue

    # -------------------------------
    #       Venue Seeding
    # -------------------------------

    def parse_capacity(raw_capacity):
        if not raw_capacity:
            return 0
        # Extract only digits using regex
        match = re.search(r"\d+", raw_capacity.replace(",", ""))
        return int(match.group()) if match else 0

    cur.execute("SELECT * FROM venues")
    if cur.fetchone():
        print(f"ℹ️ Venues already seeded. Skipping...")
    else:
        with conn.cursor() as cur:
            for vid in VENUE_IDS:
                venue = fetch_api_data(VENUES.format(venue_id=vid))
                if not venue:
                    print("❌ API Limit reached or no venue data")
                else:
                    if venue:
                        cur.execute(
                            """
                            INSERT INTO venues (venue_id, name, city, country, capacity)
                            VALUES (%s, %s, %s, %s, %s)
                            ON CONFLICT (venue_id) DO NOTHING
                        """,
                            (
                                str(vid),
                                venue.get("ground", ""),
                                venue.get("city", ""),
                                venue.get("country", ""),
                                parse_capacity(venue.get("capacity", "0")),
                            ),
                        )

    # -------------------------------
    # 🧾 Seed player_stats from PLAYER_ID_SEED
    # -------------------------------
    def safe_int(val):
        return (
            int(val.replace(",", "")) if val and val.replace(",", "").isdigit() else 0
        )

    def safe_float(val):
        return float(val) if val and val.replace(".", "", 1).isdigit() else 0.0

    player_states = {}
    cur.execute("SELECT * FROM player_stats")
    if cur.fetchone():
        print(f"ℹ️ player_stats already seeded. Skipping...")
    else:
        for pid in PLAYER_ID_SEED:
            try:
                bat_data = fetch_api_data(PLAYER_BATTING_URL.format(player_id=pid))
                bowl_data = fetch_api_data(PLAYER_BOWLING_URL.format(player_id=pid))

                if not bat_data or not bowl_data:
                    print(f"❌ No stats for player ID {pid}")
                    continue
                player_states[pid] = {"batting": bat_data, "bowling": bowl_data}

                formats = bat_data["headers"][1:]  # ['Test', 'ODI', 'T20', 'IPL']
                bat_rows = {
                    row["values"][0]: row["values"][1:] for row in bat_data["values"]
                }
                bowl_rows = {
                    row["values"][0]: row["values"][1:] for row in bowl_data["values"]
                }

                for i, fmt in enumerate(formats):
                    matches = safe_int(bat_rows.get("Matches", ["0"])[i])
                    runs = safe_int(bat_rows.get("Runs", ["0"])[i])
                    batting_avg = safe_float(bat_rows.get("Average", ["0"])[i])
                    strike_rate = safe_float(bat_rows.get("SR", ["0"])[i])
                    centuries = safe_int(bat_rows.get("100s", ["0"])[i])
                    wickets = safe_int(bowl_rows.get("Wickets", ["0"])[i])

                    cur.execute(
                        """
                        INSERT INTO player_stats (
                            player_id, format, matches_played, runs, wickets,
                            batting_average, strike_rate, centuries
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        ON CONFLICT DO NOTHING
                    """,
                        (
                            pid,
                            fmt,
                            matches,
                            runs,
                            wickets,
                            batting_avg,
                            strike_rate,
                            centuries,
                        ),
                    )
                print(f"✅ Seeded stats for player ID {pid}")
            except Exception as e:
                print(f"⚠️ Error for player ID {pid}: {e}")
                continue
        print("✅ Player stats seeding complete.")
        print("Player States:", player_states)

    print(f"Total new players added: {len(player_profiles)}")
    print("All Player Data", player_profiles)
    conn.commit()
    conn.close()
    print("✅ Seeding complete.")


# -------------------------------
# 🚀 Run Seeder
# -------------------------------
if __name__ == "__main__":
    seed_from_api()
