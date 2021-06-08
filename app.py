#!/usr/bin/env python
# -*- encoding: utf-8
from os import mkdir
from telebot import TeleBot
from logging import basicConfig, error, info, INFO
from configparser import ConfigParser
from requests import exceptions
from yadisk.yadisk import YaDisk
from controller import Registration, ColumnSave
from SqlNunchucks import connect


class BOT:
    # Поля для доступа в функциях класса
    global LOG
    global CONF
    global DB
    global SESSION
    global YAID
    global YATOKEN

    # Журналирование ошибок
    LOG = basicConfig(filemode="error.log", level=INFO)

    # Настройки проекта
    CONF = ConfigParser()
    CONF.read('settings.ini')

    # Подключение к базе данных
    DB = connect.Connect(
        subd='mysql',
        dbname=CONF['DATABASE']['name'],
        host=CONF['DATABASE']['host'],
        port=CONF['DATABASE']['port'],
        user=CONF['DATABASE']['user'],
        password=CONF['DATABASE']['password']
    ).app()

    # Параметры для соединения с хранилищем
    YAID = CONF['DISK']['id']
    YATOKEN = CONF['DISK']['token']

    # Создание сессии подключения к Телеграм API
    SESSION = TeleBot(token=CONF['BOT']['token'])

    # Создание каталога для фото
    try:
        mkdir('media')
    except:
        pass


    @SESSION.message_handler(content_types=['text', 'photo'])
    def longpool(event):
        if event:
            Registration().app(db=DB, session=SESSION, event=event)
            ColumnSave().app(db=DB, session=SESSION, event=event, ya_id=YAID, ya_token=YATOKEN)

    try:
        # Цикл прослушки событий
        SESSION.polling(none_stop=True)
    except exceptions.ReadTimeout:
        pass


if __name__ == '__main__':
    BOT()

