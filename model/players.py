def create_players_table(cur):
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS players (
            player_id VARCHAR PRIMARY KEY,
            full_name TEXT,
            role TEXT,
            batting_style TEXT,
            bowling_style TEXT,
            country TEXT
        );
    """
    )
