import time
import asyncio
from parser import parse_articles
from datahubs import initialize_hubs


async def main_loop():
    initialize_hubs()
    while True:
        await parse_articles()
        await asyncio.sleep(600)

if __name__ == "__main__":
    asyncio.run(main_loop())