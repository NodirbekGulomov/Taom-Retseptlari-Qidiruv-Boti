import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE = BASE_DIR / "data" / "db.sqlite3"


def get_connection():
    return sqlite3.connect(database=DATABASE)
