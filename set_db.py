import sqlite3 as sq

URL = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address"
LANGUAGE = "ru"

def create_table():
    with sq.connect("settings.db") as con:
        cur = con.cursor()

        cur.execute("""DROP TABLE IF EXISTS settings""")
        cur.execute("""CREATE TABLE IF NOT EXISTS settings (
            url TEXT,
            language TEXT
        )""")

        cur.execute("INSERT INTO settings VALUES(?, ?)", [URL, LANGUAGE])



def check_url():
    try:
        db = sq.connect("settings.db")
        cur = db.cursor()
        cur.execute("SELECT url FROM settings")
        result = cur.fetchone()
        return result[0]
    except sq.Error as error:
        print("Ошибка при работе с Базой Данных", error)
    finally:
        cur.close()
        db.close()


def set_language():
    user_set_lang = int(input("Укажите язык (1: ru / 2: en): "))
    try:
        db = sq.connect("settings.db")
        cur = db.cursor()
        cur.execute("SELECT language FROM settings")
        result = cur.fetchone()
        if result[0] == "ru" and user_set_lang == 2:
            language = "en"
            cur.execute("UPDATE settings SET language = ?", (language,))
            cur.execute("SELECT language FROM settings")
            result = cur.fetchone()
            return result[0]
        elif result[0] == "en" and user_set_lang == 1:
            language = "ru"
            cur.execute("UPDATE settings SET language = ?", (language,))
            cur.execute("SELECT language FROM settings")
            result = cur.fetchone()
            return result[0]
        else:
            print("Текущий выбор соответствует настройкам.")
    except sq.Error as error:
        print("Ошибка при работе с Базой Данных", error)
    finally:
        cur.close()
        db.close()







