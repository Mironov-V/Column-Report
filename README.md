## Команды для создания базы и пользователя с правами на базу:
```
CREATE USER brooks WITH PASSWORD 'amritta3113';
CREATE DATABASE column_report;
GRANT ALL PRIVILEGES ON DATABASE "column_report" TO brooks;
```

## Создание яндекс приложения
```
https://oauth.yandex.ru/
```

## Получение токена от яндекс диска:
```
https://oauth.yandex.ru/authorize?response_type=token&client_id=<ID>
```