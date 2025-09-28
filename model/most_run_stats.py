def create_most_run_stats_table(cur):
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS most_run_stats (
            player_id INT PRIMARY KEY,
            player_name VARCHAR(100),
            matches INT,
            innings INT,
            runs INT,
            average FLOAT
        );
    """
    )


# data = fetch_api_data(TOPSTATS, {"statsType": "mostRuns"})
# count = 0
# for player in data.get("values", []):
#     row = player["values"]
#     try:
#         player_id = int(row[0])
#         player_name = row[1]
#         matches = int(row[2])
#         innings = int(row[3])
#         runs = int(row[4])
#         average = float(row[5])

#         cursor.execute(
#             """
#             INSERT INTO most_run_stats (player_id, player_name, matches, innings, runs, average)
#             VALUES (%s, %s, %s, %s, %s, %s)
#             ON CONFLICT (player_id) DO NOTHING
#         """,
#             (player_id, player_name, matches, innings, runs, average),
#         )
#         count += 1
#     except Exception as e:
#         print(f"Error inserting player {player.get('name')}: {e}")
# conn.commit()
# print(f"Total {count} player inserted in database")
# conn.close
