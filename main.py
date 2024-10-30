import time

from parser import parse_hub


def main():
    while True:
        articles_data = parse_hub()
        for article in articles_data:
            print(f"Заголовок: {article['title']}")
            print(f"Дата: {article['date']}")
            print(f"Ссылка: {article['link']}")
            print(f"Автор: {article['author_name']}")
            print(f"Ссылка на автора: {article['author_link']}")
            print("-" * 80)

        time.sleep(600)

if __name__ == "__main__":
    main()