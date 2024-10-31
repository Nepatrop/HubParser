import sqlite3


def initialize_hubs():
    hubs = [
        {"url": "https://habr.com/ru/feed/", "period": 600}
    ]

    conn = sqlite3.connect('articles.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hubs (
            url TEXT PRIMARY KEY,
            period INTEGER DEFAULT 600
        )
    ''')

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='articles';")
    if cursor.fetchone() is None:
        cursor.execute('''
                CREATE TABLE articles (
                    title TEXT,
                    date TEXT,
                    link TEXT PRIMARY KEY,
                    author_name TEXT,
                    author_link TEXT,
                    content TEXT,
                    hub_url TEXT
                )
            ''')

    for hub in hubs:
        try:
            cursor.execute('''
                INSERT INTO hubs (url, period)
                VALUES (?, ?)
            ''', (hub['url'], hub['period']))
        except sqlite3.IntegrityError:
            pass

    conn.commit()
    cursor.close()
    conn.close()