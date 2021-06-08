# -*- coding: utf-8 -*-
import json


def send(session: object=None, user_id: int=None, message: str=None, media: any=None, button: json=None):
    # Функция отправи сообщения
    if message is not None  and media == None and button == None:                           # Отправка сообщения без клавиатуры и вложений
        return session.send_message(chat_id=user_id, text=message)
    elif message is not None  and media is not None and button == None:                     # Отправка сообщения и вложения без клавиатуры
        return session.send_photo(chat_id=user_id, photo=media, caption=message)
    elif message is not None  and media == None and button is not None:                     # Отправка сообщения и вложения без клавиатуры
        return session.send_message(chat_id=user_id, text=message, reply_markup=button)
    elif message is not None  and media is not None and button is not None:                 # Отправка сообщения с клавиатурой и вложением
        return session.send_photo(chat_id=user_id, photo=media, caption=message, reply_markup=button)


class Download:
    def photo(self, session, event, path):
        file = session.get_file(event.photo[len(event.photo) - 1].file_id)
        save_file = session.download_file(file.file_path)
        src = path + event.photo[1].file_id + ".jpg"
        with open(src, 'wb') as f_obj:
            f_obj.write(save_file)
            f_obj.close()
        return src
