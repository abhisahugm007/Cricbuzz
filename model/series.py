def create_series_table(cur):
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS series (
            series_id VARCHAR PRIMARY KEY,
            name TEXT,
            host_country TEXT,
            match_type TEXT,
            start_date DATE,
            total_matches INT
        );
    """
    )
