#!/bin/bash

python HubParser/manage.py runserver 0.0.0.0:8000 &

echo "Django сервер запущен по адресу: http://localhost:8000"

wait