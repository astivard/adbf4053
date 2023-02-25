# Инструкция по развертыванию тестового задания

> Данная инструкция успешно проверена на реальном сервере. Вы можете посмотреть на итоговое приложение по адресу http://138.197.188.54/ 
> 
> Доступные URL:
> 
> - http://138.197.188.54/form/ - создание формы
> - http://138.197.188.54/data/ - вывод данных всех введенных форм в JSON

### Первоначальная настройка сервера с Ubuntu:

1.  Войти в систему как root:
```
ssh root@your_server_ip_or_domain
```
Ввести пароль root.

2. Разрешить SSH соединения для брэндмауэра:
```
ufw allow OpenSSH
```
3. Включить брэндмауэр:
```
ufw enable
```
### Установка NGINX:
1. Обновить локальный индекс пакетов:
```
sudo apt update
```
2. Установить NGINX:
```
sudo apt install nginx
```
3. Настроить брандмауэр:
```
sudo ufw allow 'Nginx Full'
```

### Деплой приложения на Flask с помощью Nginx и Gunicorn:
1. Установить необходимые пакеты:
```
sudo apt install python3-pip python3-venv python3-dev build-essential libssl-dev libffi-dev python3-setuptools postgresql libpq-dev
```
2. Создать каталог для приложения и перейти в него:
```
mkdir ~/myproject
cd ~/myproject
```
3. Созадть виртуальное окружение и активировать его:
```
python3 -m venv venv
source venv/bin/activate
```
4. Установить необходимые пакеты:
```
pip install wheel gunicorn psycopg2
```
5. Запустить программную оболочку PostgreSQL:
```
sudo su - postgres
psql
```
6. Добавить пароль суперпользователя PostgreSQL:
```
alter user postgres password 'root';
```
7. Создать базу данных:
```
create database inputsdata;
```
8. Выйти из программной оболочки (Ctrl + D):
```
exit
exit
```
9. Склонировать репозиторий с проектом:
```
git clone https://github.com/astivard/adbf4053.git
```
10. Перейти в родительскую папку проекта:
```
cd adbf4053/
```
11. Установить необходимые пакеты:
```
pip install -r requirements.txt
```
12. Разрешить доступ к порту 5000:
```
sudo ufw allow 5000
```
13. Запустить приложение для создания БД:
```
python3 src/app.py
```
14. Выключить виртуальное окружение:
```
deactivate
```
15. Создать юнит-файл:
```
sudo nano /etc/systemd/system/myproject.service
```
16. Добавить следующее содержимое и сохранить:
```
[Unit]
Description=Gunicorn instance to serve myproject
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=/root/myproject/adbf4053/src
Environment="PATH=/root/myproject/venv/bin"
ExecStart=/root/myproject/venv/bin/gunicorn --workers 3 --bind unix:myproject.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target
```
17. Запустить созданную службу Gunicorn и включить её запуск при загрузке:
```
sudo systemctl start myproject
sudo systemctl enable myproject
```
18. Создать файл конфигурации Nginx:
```
sudo nano /etc/nginx/sites-available/myproject
```
19. Добавить следующее содержимое (в server_name следует указать IP-адрес вашего сервера или его доменное имя):
```
server {
    listen 80;
    server_name your_server_ip_or_domain;

    location / {
        include proxy_params;
        proxy_pass http://unix:/root/myproject/adbf4053/src/myproject.sock;
    }
}
```
20. Сохранить конфигурацию и выйти.
21. Включить конфигурацию блока сервера Nginx (связать файл конфигурации с sites-enabled каталогом):
```
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
```
22. Перезапустить Nginx чтобы прочитать новую конфигурацию:
```
sudo systemctl restart nginx
```
22. Удалить доступ через порт 5000:
```
sudo ufw delete allow 5000
```
23. Добавить доступ к файлу сокета Gunicorn:
```
sudo chmod 755 /root
```
24. Перейти по адресу приложения и проверить его работоспособность:
```
http://your_server_ip_or_domain
```
