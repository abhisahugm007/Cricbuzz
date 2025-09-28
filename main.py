import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"

headers = {
    "x-rapidapi-key": "b991531185msh7f712198be1c663p121937jsnd531dcd49a71",
    "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com",
}

response = requests.get(url, headers=headers)

print(response.json())
