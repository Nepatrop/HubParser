import requests
from bs4 import BeautifulSoup


def parse_hub():
    url = "https://habr.com/ru/feed/"

    response = requests.get(url)
    page_data = BeautifulSoup(response.text, 'html.parser')
    articles = page_data.find_all('article', class_='tm-articles-list__item')

    articles_data = []
    for article in articles:
        subject = article.find('div', class_='tm-article-snippet tm-article-snippet')
        if subject is None:
            continue

        title = subject.h2.a.span.text
        link = 'https://habr.com' + subject.h2.a['href']
        user_name = subject.find('a', class_='tm-user-info__username').text
        user_link = 'https://habr.com' + subject.find('a', class_='tm-user-info__username')['href']
        date = subject.find('a', class_='tm-article-datetime-published tm-article-datetime-published_link').time['title']

        articles_data.append({
            'title': title,
            'date': date,
            'link': link,
            'author_name': user_name,
            'author_link': user_link
        })

    return articles_data