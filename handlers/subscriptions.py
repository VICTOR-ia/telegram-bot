from telegram import Bot
from telegram import Update
from telegram import ParseMode

from utils import Commands

from handlers.subscribe import subscriptions


def do_subscriptions(bot: Bot, update: Update):
    chat_id = update.message.chat_id
    subscriptions_str = ""

    for subscription in subscriptions:
        link = 'https://vk.com/'
        _subscription = subscription.split('_')
        link += '\\_'.join(_subscription)
        subscriptions_str += f'*{subscriptions[subscription]["name"]}*\n{link}\n\n'

    bot.send_message(
        chat_id=chat_id,
        text=subscriptions_str if len(subscriptions_str) != 0 else f'{Commands.subscriptions.name.capitalize()} list is empty!',
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True
    )
