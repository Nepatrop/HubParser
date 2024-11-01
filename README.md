# Тестовое задание HubParser
 
Проект включает в себя асинхронный парсер, Django-админку для управления хабами и Docker-контейнеризацию.

## Установка

### Предварительные требования

- git
- Docker
- Docker Compose

### Шаги установки

1. **Клонировать репозиторий**:

   ```bash
   git clone https://github.com/Nepatrop/HubParser.git
   cd HubParser
   ```

2. **Cобрать Docker-образ**:

   ```bash
   docker-compose up --build
   ```
   
После этого Django будет доступен по адресу http://localhost:8000.

При входе используются данные суперпользователя:
- логин: admin
- пароль: admin

В Django можно:

- Добавлять новые хабы.
- Удалять существующие хабы.
- Изменять существующие хабы.
- Указывать период обхода для каждого хаба.

Далее после указания хабов, можно запустить сам парсер - файл main.py в директории parser.

Он будет проходиться по указанным хабам с заданным периодом и парсить статьи в таблицу articles БД articles.bd в корне проекта.
