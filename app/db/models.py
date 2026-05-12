from app.db.base import get_connection


def create_retseptlar_table():
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS retseptlar (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nomi TEXT,
                ingredient TEXT,
                vaqt INTEGER,
                murakkablik TEXT
            );
        """)
