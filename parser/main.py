import os
import asyncio
import sqlite3
from parser import parse_articles
from datahubs import initialize_hubs


async def main_loop():
    initialize_hubs()

    conn = sqlite3.connect('../articles.db')
    cursor = conn.cursor()

    cursor.execute("SELECT url, period FROM hubs")
    hubs = cursor.fetchall()

    conn.close()

    tasks = []
    for hub in hubs:
        url, period = hub
        task = asyncio.create_task(parse_hub(url, period))
        tasks.append(task)

    await asyncio.gather(*tasks)

async def parse_hub(url, period):
    while True:
        try:
            await parse_articles(url)
        except Exception as e:
            print(f"Ошибка парсинга {url}: {e}")
        await asyncio.sleep(period)


if __name__ == "__main__":
    asyncio.run(main_loop())