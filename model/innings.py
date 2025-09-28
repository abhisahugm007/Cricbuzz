def create_innings_table(cur):
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS innings (
            match_id VARCHAR,
            innings_number INT,
            batting_team_id VARCHAR,
            runs INT,
            wickets INT,
            overs FLOAT,
            FOREIGN KEY (match_id) REFERENCES matches(match_id),
            FOREIGN KEY (batting_team_id) REFERENCES teams(team_id)
        );
    """
    )
