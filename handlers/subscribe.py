from telegram import Bot
from telegram import Update
from telegram import ParseMode
from telegram import InputMediaPhoto

# requests - для http запросов, на которых работает VK API
# json - для форматирования JSON строки (возвращает VK API) в dict
import requests
import json

# Утилитарные перечисления, константы и методы
from utils import SetInterval
from utils import Commands
from utils import StatusCodes
from utils import FETCH_INTERVAL

# Токен авторизации для VK
from config import VK_TOKEN

subscriptions = {}


def do_subscribe(bot: Bot, update: Update):
    # Получаем url страницы
    page_url = update.message.text.replace(Commands.subscribe.value, '')
    chat_id = update.message.chat_id
    group_name = None
    latest_post_id = None

    def fetch_posts():
        response = requests.get(
            f'https://api.vk.com/method/wall.get?domain={page_url}&count=1&offset=1&extended=1&v=5.84&access_token={VK_TOKEN}'
        )
        print(f'{page_url}{response}')
        # При успешном ответе обрабатываем данные
        if response.status_code == StatusCodes.success.value:
            nonlocal latest_post_id
            nonlocal group_name

            posts = response.content
            parsed_data = json.loads(posts)

            # Берем первый пост из списка (он и так состоит из одного поста)
            group_name = parsed_data.get('response').get('groups')[0].get('name')
            post = parsed_data.get('response').get('items')[0]
            post_id = post['id']

            # Если нет id последнего поста, то это первый фетч
            if not latest_post_id:
                latest_post_id = post_id

                # Сообщаем, что подписка оформлена
                bot.send_message(
                    chat_id=chat_id,
                    text=f'You were successfully subscribed to *{group_name}*!',
                    parse_mode=ParseMode.MARKDOWN
                )

            # Если id предыдущего поста != id текущего поста, то отправляем новый пост
            elif post_id != latest_post_id:
                latest_post_id = post_id

                # Вытаскиваем текст и фотографии
                caption = f'*{group_name}*\n\n{post.get("text")}'
                photos = []

                for index, attachment in enumerate(post.get('attachments', []), start=0):
                    url = attachment.get('photo').get('sizes')[-1].get('url')
                    photos.append(
                        InputMediaPhoto(media=url, caption=caption if not index else None, parse_mode=ParseMode.MARKDOWN)
                    )

                if len(photos) == 0:
                    bot.send_message(
                        chat_id=chat_id,
                        text=caption,
                        parse_mode=ParseMode.MARKDOWN
                    )
                else:
                    bot.send_media_group(
                        chat_id=update.message.chat_id,
                        media=photos
                    )

    # Фетчим данные каждые N секунд и храним его, если понадобится отменить подписку
    fetch_posts()
    interval = SetInterval(FETCH_INTERVAL, fetch_posts)
    subscriptions[page_url] = {
        'name': group_name,
        'interval': interval
    }
