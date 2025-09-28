def create_bowling_table(cur):
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS bowling_performance (
            match_id VARCHAR,
            player_id VARCHAR,
            innings_number INT,
            overs FLOAT,
            runs_conceded INT,
            wickets INT,
            economy FLOAT,
            FOREIGN KEY (match_id) REFERENCES matches(match_id),
            FOREIGN KEY (player_id) REFERENCES players(player_id)
        );
    """
    )
