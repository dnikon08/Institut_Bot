import Constants as keys
from telegram.ext import *
import Responses as R

print("PROGRAM START")
# context по идее уже необязателен в этой версии питона но оставим
# наборы команд


def start_command(update, context):
    update.message.reply_text('1')  # команда начала


def help_command(update, context):
    update.message.reply_text('2')  # команда помощи


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.simple_responses(text)
    update.message.reply_text(response)


def error(update,context):
    print(f"Update {update} caused error {context.error}")  # обработчик ошибок


def main():
    updater = Updater(keys.token, use_context=True)  # апдейтр запускает бота
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))  # обработчик команды с названием
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()  # проверяет ввод постоянно(можно поставить задержку)
    updater.idle()


main()








