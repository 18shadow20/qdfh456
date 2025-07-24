## Установка и настройка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/18shadow20/qdfh456.git
cd qdfh456
```
Создайте и активируйте виртуальное окружение:

2.Создайте и активируйте виртуальное окружение:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Создайте базу данных MySQL и пользователя:
```sql
CREATE DATABASE mydatabase CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'mypassword';
GRANT ALL PRIVILEGES ON mydatabase.* TO 'myuser'@'localhost';
FLUSH PRIVILEGES;
```
5. Настройте подключение в settings.py:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
6. Выполните миграции:
```
python manage.py migrate
```
7. Запустите сервер разработки:
```bash
python manage.py runserver
```
8. Перейдите по адресу:

/upload/ — для загрузки JSON-файла
/records/ — для просмотра всех записей в таблице


Запуск через uWSGI и nginx (опционально)

Из-за технических ограничений на моём компьютере не удалось настроить VirtualBox с Debian и развернуть uWSGI + nginx.
Для разработки и тестирования использовался встроенный сервер Django (runserver).