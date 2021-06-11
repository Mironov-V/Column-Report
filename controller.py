# -*- coding: utf-8 -*-
from abc import abstractmethod
from datetime import datetime
from yadisk import YaDisk
from functions import send, Download
from SqlNunchucks.dcl import Insert, Select


class Registration:
    def __init__(self):
        self.start_message = "Из какой вы колонны?"
        self.double_registrate = "Вы уже зарегистрированны"
        self.column_error="Это не должно быть строкой!"
        self.success = 'Отлично, вы успешно зарегистрировались!\n Пришлите фотографию с подписью вида "борт  dd.mm.yyyy" и я скину их Лёше и Ире.'


    def app(self, db, session, event):
        column = None
        try:
            user = Select(
                    db=db,
                    table='profile',
                    param_search='user_id',
                    where=['user_id', '=', str(event.from_user.id)]
            ).app()[0][0]
        except:
            user=1
            
        if user == event.from_user.id:
            if event.text == "/start":
                send(
                        session=session,
                        user_id=event.from_user.id,
                        message=self.double_registrate
                    )
        else:
            if event.text == "/start":
                send(
                        session=session,
                        user_id=event.from_user.id,
                        message=self.start_message
                    )
            
            try:
                if event.text != "/start":
                    column = int(event.text)
            except:
                send(session=session, user_id=event.from_user.id, message=self.column_error)

            if column:
                Insert(
                        db=db,
                        table='profile',
                        user_id=event.from_user.id,
                        column_id=event.text
                ).app()
                send(
                        session=session,
                        user_id=event.from_user.id,
                        message=self.success
                )


class ColumnSave:
    def __init__(self):
        self.success = "Данные успешно сохранены"
    def app(self, db, session, ya_id, ya_token, event):
        if event.photo and event.caption != None:
            ya_session = YaDisk(id=ya_id, token=ya_token)
            date_folder = datetime.today().strftime("%d.%m.%Y")
            column_folder = Select(
                db=db,
                table='profile',
                param_search='column_id',
                where=['user_id', '=', str(event.from_user.id)]
            ).app()[0][0]
            avto_folder = event.caption
            try:
                # Создание папки с датой
                ya_session.mkdir(f"/column_report/{date_folder}")
            except:
                pass

            try:
                # Создание папки для колонны
                ya_session.mkdir(f"/column_report/{date_folder}/Колонна-{column_folder}")
            except:
                pass

            try:
                # Создание папки с номером авто
                ya_session.mkdir(f"/column_report/{date_folder}/Колонна-{column_folder}/{avto_folder}")
            except:
                pass

            f_obj = Download().photo(
                session=session, event=event, path='media/'
            )

            ya_path = f"/column_report/{date_folder}/Колонна-{column_folder}/{avto_folder}/{f_obj}"

            with open(f"{f_obj}", "rb") as YaF_obj:
                ya_session.upload(YaF_obj, ya_path.replace("media/", ""))
                YaF_obj.close()
        
            send(session=session, user_id=event.from_user.id, message=self.success)
