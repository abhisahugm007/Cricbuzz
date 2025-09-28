from model.most_run_stats import create_most_run_stats_table
from .players import create_players_table
from .player_stats import create_player_stats_table
from .teams import create_teams_table
from .matches import create_matches_table
from .venues import create_venues_table
from .series import create_series_table
from .innings import create_innings_table
from .batting_performance import create_batting_table
from .bowling_performance import create_bowling_table
from .fielding_performance import create_fielding_table
from .partnerships import create_partnerships_table


def create_all_tables(cur):
    create_most_run_stats_table(cur)
    create_players_table(cur)
    create_player_stats_table(cur)
    create_teams_table(cur)
    create_venues_table(cur)
    create_matches_table(cur)
    create_series_table(cur)
    create_innings_table(cur)
    create_batting_table(cur)
    create_bowling_table(cur)
    create_fielding_table(cur)
    create_partnerships_table(cur)
