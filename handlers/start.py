from telegram import Bot
from telegram import Update
from telegram import ParseMode
from telegram import ReplyKeyboardMarkup
from telegram import KeyboardButton

# Утилитарные перечисления, константы и методы
from utils import Commands


def do_start(bot: Bot, update: Update):
    chat_id = update.message.chat_id
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=f'{Commands.subscribe.name.capitalize()} to VK page'),
                KeyboardButton(text=f'{Commands.unsubscribe.name.capitalize()} from VK page')
            ],
            [
                KeyboardButton(text=f'Check VK {Commands.subscriptions.name}')
            ]
        ],
        resize_keyboard=True
    )

    bot.send_message(
        chat_id=chat_id,
        text='Hello!\n\nEnter *VK ID* of the page and press one of the commands below!',
        reply_markup=reply_markup,
        parse_mode=ParseMode.MARKDOWN
    )
