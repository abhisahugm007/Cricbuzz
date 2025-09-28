sql_queries = {
    # Beginner Level
    "1": {
        "label": "Find all players who represent India",
        "query": """
            SELECT full_name, role, batting_style, bowling_style
            FROM players
            WHERE country = 'India';
        """,
    },
    "2": {
        "label": "Show recent cricket matches",
        "query": """
            SELECT match_desc, team1_id, team2_id, venue_id, match_date
            FROM matches
            WHERE match_date >= CURRENT_DATE - INTERVAL '30 days'
            ORDER BY match_date DESC;
        """,
    },
    "3": {
        "label": "Top 10 highest run scorers in ODI cricket",
        "query": """
            SELECT player_name, runs, average
            FROM most_run_stats
            ORDER BY runs DESC
            LIMIT 10;
        """,
    },
    "4": {
        "label": "Venues with capacity > 30,000",
        "query": """
            SELECT name, city, country, capacity
            FROM venues
            WHERE capacity > 30000
            ORDER BY capacity DESC;
        """,
    },
    "5": {
        "label": "Matches won by each team",
        "query": """
            SELECT t.team_name, COUNT(m.match_id) AS wins
            FROM matches m
            JOIN teams t ON m.winner_id = t.team_id
            GROUP BY t.team_name
            ORDER BY wins DESC;
        """,
    },
    "6": {
        "label": "Count of players by role",
        "query": """
            SELECT role, COUNT(*) AS player_count
            FROM players
            GROUP BY role;
        """,
    },
    "7": {
        "label": "Highest individual score by format",
        "query": """
            SELECT format, MAX(runs) AS highest_score
            FROM batting_performance
            GROUP BY format;
        """,
    },
    "8": {
        "label": "Series started in 2024",
        "query": """
            SELECT name, host_country, match_type, start_date, total_matches
            FROM series
            WHERE EXTRACT(YEAR FROM start_date) = 2024;
        """,
    },
    # Intermediate Level
    "9": {
        "label": "All-rounders with >1000 runs and >50 wickets",
        "query": """
            SELECT p.full_name, ps.runs, ps.wickets, ps.format
            FROM player_stats ps
            JOIN players p ON ps.player_id = p.player_id
            WHERE ps.runs > 1000 AND ps.wickets > 50;
        """,
    },
    "10": {
        "label": "Last 20 completed matches",
        "query": """
            SELECT match_desc, team1_id, team2_id, winner_id, margin, victory_type, venue_id
            FROM matches
            ORDER BY match_date DESC
            LIMIT 20;
        """,
    },
    "11": {
        "label": "Compare player performance across formats",
        "query": """
            SELECT player_id,
                   SUM(CASE WHEN format = 'Test' THEN runs ELSE 0 END) AS test_runs,
                   SUM(CASE WHEN format = 'ODI' THEN runs ELSE 0 END) AS odi_runs,
                   SUM(CASE WHEN format = 'T20I' THEN runs ELSE 0 END) AS t20_runs,
                   AVG(batting_average) AS overall_avg
            FROM player_stats
            GROUP BY player_id
            HAVING COUNT(DISTINCT format) >= 2;
        """,
    },
    "12": {
        "label": "Team performance home vs away",
        "query": """
            SELECT t.team_name,
                   SUM(CASE WHEN v.country = t.country THEN 1 ELSE 0 END) AS home_matches,
                   SUM(CASE WHEN v.country != t.country THEN 1 ELSE 0 END) AS away_matches
            FROM matches m
            JOIN teams t ON m.team1_id = t.team_id OR m.team2_id = t.team_id
            JOIN venues v ON m.venue_id = v.venue_id
            GROUP BY t.team_name;
        """,
    },
    "13": {
        "label": "Partnerships with 100+ runs",
        "query": """
            SELECT p1.full_name AS batsman1, p2.full_name AS batsman2, pr.runs, pr.innings_number
            FROM partnerships pr
            JOIN players p1 ON pr.player1_id = p1.player_id
            JOIN players p2 ON pr.player2_id = p2.player_id
            WHERE pr.runs >= 100 AND ABS(pr.position1 - pr.position2) = 1;
        """,
    },
    "14": {
        "label": "Bowling performance at venues",
        "query": """
            SELECT bp.player_id, bp.venue_id,
                   AVG(bp.economy) AS avg_economy,
                   SUM(bp.wickets) AS total_wickets,
                   COUNT(bp.match_id) AS matches_played
            FROM bowling_performance bp
            GROUP BY bp.player_id, bp.venue_id
            HAVING COUNT(bp.match_id) >= 3;
        """,
    },
    "15": {
        "label": "Player performance in close matches",
        "query": """
            SELECT bp.player_id,
                   AVG(bp.runs) AS avg_runs,
                   COUNT(bp.match_id) AS close_matches
            FROM batting_performance bp
            JOIN matches m ON bp.match_id = m.match_id
            WHERE (m.victory_type = 'runs' AND CAST(SPLIT_PART(m.margin, ' ', 1) AS INT) < 50)
               OR (m.victory_type = 'wickets' AND CAST(SPLIT_PART(m.margin, ' ', 1) AS INT) < 5)
            GROUP BY bp.player_id;
        """,
    },
    "16": {
        "label": "Batting performance by year",
        "query": """
            SELECT player_id,
                   EXTRACT(YEAR FROM match_date) AS year,
                   AVG(runs) AS avg_runs,
                   AVG(strike_rate) AS avg_sr,
                   COUNT(match_id) AS matches
            FROM batting_performance bp
            JOIN matches m ON bp.match_id = m.match_id
            WHERE match_date >= '2020-01-01'
            GROUP BY player_id, year
            HAVING COUNT(match_id) >= 5;
        """,
    },
    # Advanced Level
    "17": {
        "label": "Toss win advantage analysis",
        "query": """
            SELECT toss_decision,
                   COUNT(*) FILTER (WHERE toss_winner_id = winner_id) * 100.0 / COUNT(*) AS win_pct
            FROM matches
            GROUP BY toss_decision;
        """,
    },
    "18": {
        "label": "Most economical bowlers in ODIs and T20s",
        "query": """
            SELECT player_id,
                   AVG(economy) AS avg_economy,
                   SUM(wickets) AS total_wickets
            FROM bowling_performance
            WHERE format IN ('ODI', 'T20I')
            GROUP BY player_id
            HAVING COUNT(match_id) >= 10;
        """,
    },
    "19": {
        "label": "Consistent batsmen (low std dev)",
        "query": """
            SELECT player_id,
                   AVG(runs) AS avg_runs,
                   STDDEV(runs) AS run_stddev
            FROM batting_performance
            WHERE match_date >= '2022-01-01' AND balls_faced >= 10
            GROUP BY player_id
            HAVING COUNT(match_id) >= 5;
        """,
    },
    "20": {
        "label": "Matches played and averages by format",
        "query": """
            SELECT player_id,
                   SUM(CASE WHEN format = 'Test' THEN 1 ELSE 0 END) AS test_matches,
                   SUM(CASE WHEN format = 'ODI' THEN 1 ELSE 0 END) AS odi_matches,
                   SUM(CASE WHEN format = 'T20I' THEN 1 ELSE 0 END) AS t20_matches,
                   AVG(batting_average) AS avg_bat
            FROM player_stats
            GROUP BY player_id
            HAVING SUM(CASE WHEN format IN ('Test', 'ODI', 'T20I') THEN 1 ELSE 0 END) >= 20;
        """,
    },
    "21": {
        "label": "Comprehensive player ranking",
        "query": """
            SELECT player_id,
                   ((runs * 0.01) + (batting_average * 0.5) + (strike_rate * 0.3)) +
                   ((wickets * 2) + ((50 - bowling_average) * 0.5) + ((6 - economy_rate) * 2)) AS total_score
            FROM player_stats;
        """,
    },
    "22": {
        "label": "Head-to-head match prediction",
        "query": """
            SELECT team1_id, team2_id,
                   COUNT(match_id) AS total_matches,
                   SUM(CASE WHEN winner_id = team1_id THEN 1 ELSE 0 END) AS team1_wins,
                   SUM(CASE WHEN winner_id = team2_id THEN 1 ELSE 0 END) AS team2_wins
            FROM matches
            WHERE match_date >= CURRENT_DATE - INTERVAL '3 years'
            GROUP BY team1_id, team2_id
        """,
    },
    "23": {
        "label": "Recent player form and momentum",
        "query": """
            SELECT player_id,
                   AVG(runs) FILTER (WHERE match_date >= CURRENT_DATE - INTERVAL '30 days') AS avg_last_5,
                   AVG(runs) FILTER (WHERE match_date >= CURRENT_DATE - INTERVAL '60 days') AS avg_last_10,
                   COUNT(*) FILTER (WHERE runs >= 50) AS fifties,
                   STDDEV(runs) AS consistency_score
            FROM batting_performance
            GROUP BY player_id;
        """,
    },
    "24": {
        "label": "Best batting partnerships",
        "query": """
            SELECT player1_id, player2_id,
                   AVG(runs) AS avg_partnership,
                   COUNT(*) FILTER (WHERE runs > 50) AS fifty_plus,
                   MAX(runs) AS highest,
                   COUNT(*) FILTER (WHERE runs > 50) * 100.0 / COUNT(*) AS success_rate
            FROM partnerships
            WHERE ABS(position1 - position2) = 1
            GROUP BY player1_id, player2_id
            HAVING COUNT(*) >= 5;
        """,
    },
    "25": {
        "label": "Time-series analysis of player performance",
        "query": """
            SELECT player_id,
                   DATE_TRUNC('quarter', match_date) AS quarter,
                   AVG(runs) AS avg_runs,
                   AVG(strike_rate) AS avg_sr
            FROM batting_performance
            JOIN matches ON batting_performance.match_id = matches.match_id
            GROUP BY player_id, quarter
            HAVING COUNT(*) >= 3;
        """,
    },
}
