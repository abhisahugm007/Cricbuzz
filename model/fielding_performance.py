def create_fielding_table(cur):
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS fielding_performance (
            match_id VARCHAR,
            player_id VARCHAR,
            catches INT,
            stumpings INT,
            FOREIGN KEY (match_id) REFERENCES matches(match_id),
            FOREIGN KEY (player_id) REFERENCES players(player_id)
        );
    """
    )
