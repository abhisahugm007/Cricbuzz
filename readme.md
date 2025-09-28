# Cricbuzz Data Seeder

This project seeds cricket player, team, and venue data into a PostgreSQL database using data fetched from APIs.

---

## 🚀 Features

- Fetches player, team, and venue data from Cricbuzz-like APIs
- Seeds data into PostgreSQL tables
- Handles player stats for multiple formats (Test, ODI, T20, IPL)
- Robust error handling and duplicate prevention

---

## 🛠️ Requirements

- Python 3.8+
- [PostgreSQL](https://www.postgresql.org/) (database running and accessible)
- pip (Python package manager)
- Internet connection (for API calls)

---

## 📦 Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/cricbuzz-seeder.git
cd cricbuzz-seeder
```

### 2. Install Python Dependencies

```sh
pip install -r requirements.txt
```

**Example `requirements.txt`:**
```
psycopg2
requests
streamlit
```

### 3. Configure Database

Edit `config.py` and set your PostgreSQL credentials:

```python
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "user": "your_db_user",
    "password": "your_db_password",
    "dbname": "your_db_name"
}
```

### 4. Create Database Tables

Run the following script to create all required tables:

```sh
python -c "from model import create_all_tables; import psycopg2; from config import DB_CONFIG; conn = psycopg2.connect(**DB_CONFIG); cur = conn.cursor(); create_all_tables(cur); conn.commit(); conn.close()"
```

Or, create a script (e.g., `create_tables.py`) with:

```python
import psycopg2
from config import DB_CONFIG
from model import create_all_tables

conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor()
create_all_tables(cur)
conn.commit()
conn.close()
```

Then run:

```sh
python create_tables.py
```
or run belown

python utils/db_connection.py
### 5. Seed the Data

Run the seeder script:

```sh
python utils/seed.py
```

---

## 📝 Notes

- Make sure your database is running and accessible.
- The seeder fetches data from external APIs; ensure you have a stable internet connection.
- If you want to re-seed, you may need to clear the tables or drop/recreate the database.

---

## 🧩 Project Structure

```
Cricbuzz/
│
├── config.py
├── model/
│   ├── __init__.py
│   ├── players.py
│   └── ... (other table definitions)
├── utils/
│   ├── seed.py
│   ├── helper.py
│   └── ...
├── requirements.txt
└── README.md
```

---

## 🙋‍♂️ Troubleshooting

- **ImportError:**  
  Ensure all required variables are defined and exported in the correct files.
- **Database Connection Error:**  
  Check your `DB_CONFIG` and that PostgreSQL is running.
- **API Errors:**  
  Check your internet connection and API endpoint URLs.

---

## 📄 License

MIT License

---

## 👤 Author

- [Abhishek Sahu](https://github.com/abhisahugm007/Cricbuzz)
