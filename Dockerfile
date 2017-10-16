FROM base/archlinux

MAINTAINER Vyacheslav Kruglov

USER root

# Обвновление списка пакетов
RUN pacman -Sy

# Установка Python3
RUN pacman -S python --noconfirm

# Копируем исходный код в Docker-контейнер
ADD ./ /var/www/html/

# Объявлем порт сервера
EXPOSE 8080

# Запускаем сервер
CMD python /var/www/html/src/httpd.py -r /var/www/html -n 4 -p 8080
