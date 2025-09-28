def create_matches_table(cur):
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS matches (
            match_id VARCHAR PRIMARY KEY,
            series_id VARCHAR,
            team1_id VARCHAR,
            team2_id VARCHAR,
            winner_id VARCHAR,
            venue_id VARCHAR,
            match_date DATE,
            match_desc TEXT,
            format TEXT,
            result TEXT,
            margin TEXT,
            victory_type TEXT,
            toss_winner_id VARCHAR,
            toss_decision TEXT,
            FOREIGN KEY (team1_id) REFERENCES teams(team_id),
            FOREIGN KEY (team2_id) REFERENCES teams(team_id),
            FOREIGN KEY (winner_id) REFERENCES teams(team_id),
            FOREIGN KEY (venue_id) REFERENCES venues(venue_id)
        );
    """
    )
