def create_venues_table(cur):
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS venues (
            venue_id VARCHAR PRIMARY KEY,
            name TEXT,
            city TEXT,
            country TEXT,
            capacity INT
        );
    """
    )
