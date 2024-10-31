import os
import sqlite3
from .models import Hub


def sync_hubs():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(base_dir, '..', 'articles.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='hubs';")
    table_exists = cursor.fetchone()

    if not table_exists:
        cursor.execute('''
            CREATE TABLE hubs (
                url TEXT PRIMARY KEY,
                period INTEGER DEFAULT 600
            )
        ''')

    django_hubs = Hub.objects.all()

    cursor.execute("DELETE FROM hubs")

    for hub in django_hubs:
        cursor.execute("INSERT INTO hubs (url, period) VALUES (?, ?)", (hub.url, hub.period))

    conn.commit()
    cursor.close()
    conn.close()