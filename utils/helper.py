import requests

import requests
import sys
import os

# Add the parent directory to sys.path so Python can find config.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import RAPIDAPI_HOST, RAPIDAPI_KEY
import streamlit as st


def fetch_api_data(url, params={}):
    try:
        headers = {"x-rapidapi-key": RAPIDAPI_KEY, "x-rapidapi-host": RAPIDAPI_HOST}
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None


cricket_players_list = [
    "Virat Kohli",
    "Rohit Sharma",
    "Shubman Gill",
    "KL Rahul",
    "Shreyas Iyer",
    "Suryakumar Yadav",
    "Rishabh Pant",
    "MS Dhoni",
    "Hardik Pandya",
    "Ravindra Jadeja",
    "Ravichandran Ashwin",
    "Jasprit Bumrah",
    "Mohammed Shami",
    "Mohammed Siraj",
    "Kuldeep Yadav",
    "Steve Smith",
    "David Warner",
    "Travis Head",
    "Marnus Labuschagne",
    "Glenn Maxwell",
    "Pat Cummins",
    "Mitchell Starc",
    "Josh Hazlewood",
    "Adam Zampa",
    "Alex Carey",
    "Joe Root",
    "Ben Stokes",
    "Jos Buttler",
    "Jonny Bairstow",
    "Jofra Archer",
    "Mark Wood",
    "Moeen Ali",
    "Sam Curran",
    "Chris Woakes",
    "Babar Azam",
    "Mohammad Rizwan",
    "Shaheen Afridi",
    "Shadab Khan",
    "Imam-ul-Haq",
    "Kane Williamson",
    "Devon Conway",
    "Trent Boult",
    "Tim Southee",
    "Mitchell Santner",
]
