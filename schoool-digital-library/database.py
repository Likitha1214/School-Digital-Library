import sqlite3

def create_database():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject TEXT,
        chapter TEXT,
        filename TEXT
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()