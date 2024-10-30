import time
from parser import parse_articles


def main():
    while True:
        parse_articles()
        time.sleep(600)

if __name__ == "__main__":
    main()