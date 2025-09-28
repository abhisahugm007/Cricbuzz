# config.py

# Database Configuration
DB_CONFIG = {
    "host": "localhost",
    "database": "cricbuzz",
    "user": "postgres",
    "password": "root",
    "port": 5432,
}


# API Credentials
RAPIDAPI_KEY = "b991531185msh7f712198be1c663p121937jsnd531dcd49a71"
RAPIDAPI_HOST = "cricbuzz-cricket.p.rapidapi.com"

HEADERS = {
    "x-rapidapi-key": "b991531185msh7f712198be1c663p121937jsnd531dcd49a71",
    "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com",
}

# API URL's
LIVE_URL = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"

SERIES_URL = "https://cricbuzz-cricket.p.rapidapi.com/series/v1/international"

SCORECARD_URL = "https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/{match_id}/scard"

PLAYER_SEARCH_URL = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/search"

PLAYER_STATS_URL = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/{player_id}"

PLAYER_BATTING_URL = (
    "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/{player_id}/batting"
)

PLAYER_BOWLING_URL = (
    "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/{player_id}/bowling"
)
TOPSTATS = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/topstats/0"
