from dadata import Dadata
import os
import set_db as db
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

URL = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address"
TOKEN = os.getenv('TOKEN')
LANGUAGE = "ru"


def request(token, language):
    with Dadata(token) as dadata:
        user_request = input("\nВведите адрес: ")
        result = dadata.suggest("address", user_request, language=language)
        for id, hunt in enumerate(result, 1):
            print(f'{id}: {hunt["value"]}')

        user_choice = int(input("\nУкажите номер соответствующего адреса: "))
        lat = result[user_choice - 1]["data"]["geo_lat"]
        lon = result[user_choice - 1]["data"]["geo_lon"]
        print(f'\nШирота: {lat} с.ш.\n'
              f'Долгота: {lon} в.д.\n')


def settings():
    user_choice = int(input("\n1. Изменить язык и выполнить запрос.\n"
                            "2. Узнать URL сервиса.\n"
                            "3. Вернуться на главную .\n"
                            "Укажите номер операции:  "))
    if user_choice == 1:
        lang = db.set_language()
        request(TOKEN, lang)
    elif user_choice == 2:
        print(f"Базовый URL к сервису dadata: {db.check_url()}")
    else:
        pass



db.create_table()
is_on = True
while is_on:
    task = int(input("\n1. Узнать координаты по адресу.\n"
                     "2. Настройки.\n"
                     "3. Завершить работу.\n"
                     "Укажите номер операции:  "))
    if task == 1:
        request(TOKEN, LANGUAGE)
    elif task == 2:
        settings()
    elif task == 3:
        is_on = False
    else:
        print("Неверный запрос, повторите попытку!\n")
