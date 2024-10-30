import time
from parser import parse_articles
from datahubs import initialize_hubs

def main():
    initialize_hubs()
    while True:
        parse_articles()
        time.sleep(600)

if __name__ == "__main__":
    main()