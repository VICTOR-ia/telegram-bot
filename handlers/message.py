from telegram import Bot
from telegram import Update
from telegram import ParseMode

from utils import Commands

from handlers.subscribe import do_subscribe
from handlers.unsubscribe import do_unsubscribe
from handlers.subscriptions import do_subscriptions

is_subscribe_mode = False
is_unsubscribe_mode = False


def subscribe_button_handler(update: Update):
    update.message.reply_text(
        text='Enter *VK ID* of the page you want to subscribe',
        parse_mode=ParseMode.MARKDOWN

    )


def unsubscribe_button_handler(update: Update):
    update.message.reply_text(
        text='Enter *VK ID* of the page you want to unsubscribe',
        parse_mode=ParseMode.MARKDOWN
    )


def do_message(bot: Bot, update: Update):
    global is_subscribe_mode
    global is_unsubscribe_mode

    text = update.message.text

    if is_subscribe_mode:
        do_subscribe(bot, update)
        is_subscribe_mode = False
        return

    if is_unsubscribe_mode:
        do_unsubscribe(bot, update)
        is_unsubscribe_mode = False
        return

    if text == f'{Commands.subscribe.name.capitalize()} to VK page':
        is_subscribe_mode = True
        return subscribe_button_handler(update=update)

    if text == f'{Commands.unsubscribe.name.capitalize()} from VK page':
        is_unsubscribe_mode = True
        return unsubscribe_button_handler(update=update)

    if text == f'Check VK {Commands.subscriptions.name}':
        return do_subscriptions(bot=bot, update=update)

