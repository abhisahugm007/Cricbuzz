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
HEADERS = {
    "x-rapidapi-key": "62371bd802msh1aff245accb6d74p110b6bjsn82188bdbc6c5",
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
VENUES = "https://cricbuzz-cricket.p.rapidapi.com/venues/v1/{venue_id}"
