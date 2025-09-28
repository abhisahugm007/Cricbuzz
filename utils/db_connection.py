import psycopg2

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from model import create_all_tables
from config import DB_CONFIG


conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor()


# Create all tables if not exsists
create_all_tables(cur)

# Commit changes and close connection
conn.commit()
conn.close()
