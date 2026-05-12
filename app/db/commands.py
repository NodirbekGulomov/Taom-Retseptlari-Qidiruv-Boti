from app.db.base import get_connection


def clean_retseptlar_table():
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM retseptlar")


def add_retsept(nomi, ingredient, vaqt, murakkablik):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO retseptlar (nomi, ingredient, vaqt, murakkablik) VALUES (?, ?, ?, ?)
        """, (nomi, ingredient, vaqt, murakkablik))


def search_by_taom(nomi):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT nomi, ingredient, vaqt, murakkablik
            FROM retseptlar
            WHERE LOWER(nomi) LIKE '%' || LOWER(?) || '%'
        """, (nomi,))
        return cur.fetchall()


def search_by_ingredient(ingredient):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT nomi, ingredient, vaqt, murakkablik
            FROM retseptlar
            WHERE LOWER(ingredient) LIKE '%' || LOWER(?) || '%'
        """, (ingredient,))
        return cur.fetchall()
