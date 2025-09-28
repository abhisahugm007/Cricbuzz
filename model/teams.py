def create_teams_table(cur):
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS teams (
            team_id VARCHAR PRIMARY KEY,
            team_name TEXT,
            country TEXT
        );
    """
    )
