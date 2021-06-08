## Команды для создания базы и пользователя с правами на базу:
```
CREATE USER 'beis_pet'@'localhost' IDENTIFIED BY 'amritta2103';
CREATE DATABASE column_report;
GRANT ALL PRIVILEGES ON column_report.* TO 'beis_pet'@'localhost';
```

## Создание яндекс приложения
```
https://oauth.yandex.ru/
```

## Получение токена от яндекс диска:
```
https://oauth.yandex.ru/authorize?response_type=token&client_id=<ID>
```

```

```