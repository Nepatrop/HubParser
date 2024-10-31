import sqlite3


def view_database():
    conn = sqlite3.connect('../articles.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Таблицы в базе данных:")
    for table in tables:
        print(table[0])

    cursor.execute("SELECT * FROM hubs;")
    print("\nДанные в таблице hubs:")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.execute("SELECT * FROM articles;")
    rows = cursor.fetchall()
    print("\nДанные в таблице articles:")
    for row in rows:
        print(row)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    view_database()