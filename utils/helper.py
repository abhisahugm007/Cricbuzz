import requests

import requests
import sys
import os

# Add the parent directory to sys.path so Python can find config.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import HEADERS
import streamlit as st


def fetch_api_data(url, params={}):
    try:
        response = requests.get(url, headers=HEADERS, params=params)
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
    "Steven Smith",
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


VENUE_IDS = [19, 50, 87, 31, 335, 512, 80, 132, 34, 22]
PLAYER_ID_SEED = [
    "1413",
    "265",
    "9311",
    "1739",
    "7662",
    "8095",
    "8019",
    "2258",
    "6557",
    "8359",
    "12160",
    "6326",
]
