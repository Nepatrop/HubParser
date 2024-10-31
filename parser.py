import aiohttp
import asyncio
import sqlite3
from bs4 import BeautifulSoup
from datetime import datetime


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def parse_articles(url):
    async with aiohttp.ClientSession() as session:
        tasks = []
        response = await fetch(session, url)
        page_data = BeautifulSoup(response, 'html.parser')
        articles = page_data.find_all('article', class_='tm-articles-list__item')

        for article in reversed(articles):
            subject = article.find('div', class_='tm-article-snippet tm-article-snippet')
            if subject is None:
                continue

            title = subject.h2.a.span.text
            link = 'https://habr.com' + subject.h2.a['href']
            user_name = subject.find('a', class_='tm-user-info__username').text
            user_link = 'https://habr.com' + subject.find('a', class_='tm-user-info__username')['href']
            date = subject.find('a', class_='tm-article-datetime-published tm-article-datetime-published_link').time['title']

            tasks.append(fetch_article_content(session, title, date, link, user_name, user_link, url))

            if len(tasks) >= 5:
                await asyncio.gather(*tasks)
                tasks = []

        if tasks:
            await asyncio.gather(*tasks)

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Статьи c {url} сохранены в БД. {current_time}")

async def fetch_article_content(session, title, date, link, user_name, user_link, hub_url):
    article_response = await fetch(session, link)
    article_data = BeautifulSoup(article_response, 'html.parser')
    content_div = article_data.find('div', class_='tm-article-body')

    if content_div:
        content = content_div.get_text(separator='\n', strip=False)
    else:
        content = ""

    conn = sqlite3.connect('articles.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO articles (title, date, link, author_name, author_link, content, hub_url)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (title, date, link, user_name, user_link, content, hub_url))
    except sqlite3.IntegrityError:
        pass

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    asyncio.run(parse_articles())