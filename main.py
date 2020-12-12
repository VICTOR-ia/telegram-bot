from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler

# Токен авторизации для Telegram
from config import TG_TOKEN

# Утилитарные перечисления
from utils import Commands

# Хендлеры для событий бота
from handlers.start import do_start
from handlers.subscribe import do_subscribe
from handlers.unsubscribe import do_unsubscribe
from handlers.message import do_message
from handlers.subscriptions import do_subscriptions


def main():
    updater = Updater(
        token=TG_TOKEN,
    )

    start_handler = CommandHandler(Commands.start.name, do_start)
    subscribe_handler = CommandHandler(Commands.subscribe.name, do_subscribe)
    unsubscribe_handler = CommandHandler(Commands.unsubscribe.name, do_unsubscribe)
    subscriptions_handler = CommandHandler(Commands.subscriptions.name, do_subscriptions)
    message_handler = MessageHandler(Filters.text, do_message)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(subscribe_handler)
    updater.dispatcher.add_handler(unsubscribe_handler)
    updater.dispatcher.add_handler(subscriptions_handler)
    updater.dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

