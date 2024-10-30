import requests
import sqlite3
from bs4 import BeautifulSoup
from datetime import datetime


def parse_articles():
    url = "https://habr.com/ru/feed/"

    response = requests.get(url)
    page_data = BeautifulSoup(response.text, 'html.parser')
    articles = page_data.find_all('article', class_='tm-articles-list__item')

    conn = sqlite3.connect('articles.db')
    cursor = conn.cursor()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS articles (
                title TEXT,
                date TEXT,
                link TEXT PRIMARY KEY,
                author_name TEXT,
                author_link TEXT,
                content TEXT
            )
        ''')

    for article in reversed(articles):
        subject = article.find('div', class_='tm-article-snippet tm-article-snippet')
        if subject is None:
            continue

        title = subject.h2.a.span.text
        link = 'https://habr.com' + subject.h2.a['href']
        user_name = subject.find('a', class_='tm-user-info__username').text
        user_link = 'https://habr.com' + subject.find('a', class_='tm-user-info__username')['href']
        date = subject.find('a', class_='tm-article-datetime-published tm-article-datetime-published_link').time['title']

        article_response = requests.get(link)
        article_data = BeautifulSoup(article_response.text, 'html.parser')
        content_div = article_data.find('div', class_='tm-article-body')
        if content_div:
            content = content_div.get_text(separator='\n', strip=False)
        else:
            content = ""

        try:
            cursor.execute('''
                       INSERT INTO articles (title, date, link, author_name, author_link, content)
                       VALUES (?, ?, ?, ?, ?, ?)
                   ''', (title, date, link, user_name, user_link, content))
        except sqlite3.IntegrityError:
            pass

    conn.commit()
    cursor.close()
    conn.close()

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Статьи успешно сохранены в базу данных. {current_time}")