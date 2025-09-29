import sqlite3
import os

DB_PATH = "data/court_data.db"

def init_db():
    os.makedirs("data", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            court_type TEXT,
            case_type TEXT,
            case_number TEXT,
            case_year TEXT,
            result TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_query(court_type, case_type, case_number, case_year, result):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('INSERT INTO queries (court_type, case_type, case_number, case_year, result) VALUES (?, ?, ?, ?, ?)',
              (court_type, case_type, case_number, case_year, str(result)))
    conn.commit()
    conn.close()

def get_all_queries():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT court_type, case_type, case_number, case_year FROM queries ORDER BY id DESC')
    rows = c.fetchall()
    conn.close()
    return [dict(row) for row in rows]