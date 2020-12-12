from telegram import Bot
from telegram import Update
from telegram import ParseMode

# Утилитарные перечисления, константы и методы
from utils import Commands

from handlers.subscribe import subscriptions


def do_unsubscribe(bot: Bot, update: Update):
    page_url = update.message.text.replace(Commands.unsubscribe.value, '')
    chat_id = update.message.chat_id

    if page_url in subscriptions:
        subscription = subscriptions.pop(page_url)
        subscription["interval"].cancel()

        # Сообщаем, что подписка отменена
        bot.send_message(
            chat_id=chat_id,
            text=f'You were successfully unsubscribed from *{subscription["name"]}*!',
            parse_mode=ParseMode.MARKDOWN
        )
    else:
        bot.send_message(
            chat_id=chat_id,
            text="You don't have such a subscription!",
            parse_mode=ParseMode.MARKDOWN
        )