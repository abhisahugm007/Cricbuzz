def create_batting_table(cur):
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS batting_performance (
            match_id VARCHAR,
            player_id VARCHAR,
            innings_number INT,
            runs INT,
            balls_faced INT,
            strike_rate FLOAT,
            position INT,
            not_out BOOLEAN,
            FOREIGN KEY (match_id) REFERENCES matches(match_id),
            FOREIGN KEY (player_id) REFERENCES players(player_id)
        );
    """
    )
