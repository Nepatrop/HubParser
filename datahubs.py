import sqlite3


def initialize_hubs():
    hubs = [
        "https://habr.com/ru/hub/python/",
        "https://habr.com/ru/hub/programming/",
        "https://habr.com/ru/feed/"
    ]

    conn = sqlite3.connect('articles.db')
    cursor = conn.cursor()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS hubs (
                url TEXT PRIMARY KEY
            )
        ''')

    for hub in hubs:
        try:
            cursor.execute('''
                    INSERT INTO hubs (url)
                    VALUES (?)
                ''', (hub,))
        except sqlite3.IntegrityError:
            pass

    conn.commit()
    cursor.close()
    conn.close()