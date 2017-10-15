FROM ubuntu:16.04

MAINTAINER Vyacheslav Kruglov

USER root

# Обвновление списка пакетов
RUN apt-get -y update

# Установка Python3
RUN apt-get install -y python3

# Копируем исходный код в Docker-контейнер
ADD ./ /var/www/html/

# Объявлем порт сервера
EXPOSE 80

# Запускаем сервер
CMD python3 /var/www/html/src/httpd.py -r /var/www/html
