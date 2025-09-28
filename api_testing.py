import requests
import pandas as pd

from config import LIVE_URL, RAPIDAPI_HOST, RAPIDAPI_KEY, SCORECARD_URL

match_id = 119834

scorecard_url = SCORECARD_URL.format(match_id=match_id)

headers = {"x-rapidapi-key": RAPIDAPI_KEY, "x-rapidapi-host": RAPIDAPI_HOST}

Live_Matchs_response = requests.get(scorecard_url, headers=headers)

data = Live_Matchs_response.json()
print(data)
