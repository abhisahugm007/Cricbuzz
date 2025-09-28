def create_player_stats_table(cur):
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS player_stats (
            player_id VARCHAR,
            format TEXT,
            matches_played INT,
            runs INT,
            wickets INT,
            batting_average FLOAT,
            strike_rate FLOAT,
            centuries INT,
            FOREIGN KEY (player_id) REFERENCES players(player_id)
        );
    """
    )
