def create_partnerships_table(cur):
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS partnerships (
            match_id VARCHAR,
            innings_number INT,
            player1_id VARCHAR,
            player2_id VARCHAR,
            runs INT,
            position1 INT,
            position2 INT,
            FOREIGN KEY (match_id) REFERENCES matches(match_id),
            FOREIGN KEY (player1_id) REFERENCES players(player_id),
            FOREIGN KEY (player2_id) REFERENCES players(player_id)
        );
    """
    )
