from datetime import datetime


def simple_responses(input_text):
    user_message = str(input_text).lower()
    if user_message in "привет":
        return "Привет!"  # тут у бота наверное прописать приветствие с набором возможных команд
    if user_message in "помощь":
        return "список команд"  # опять дублируем команды?
    if user_message in ("время", "сколько сейчас времени"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)  # ТЕСТОВАЯ ФУНКЦИЯ

    return "Я не понимаю введи существующую команду!"  # возвращает строку если введена не одна из строк выше
