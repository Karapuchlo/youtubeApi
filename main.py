import os
import pytest

from googleapiclient.discovery import build


# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('API_KEY')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)

import json

#print(json.dumps(channel, indent=2, ensure_ascii=False))

class YoutubeChannel:
    def __init__(self, id):
        self.id = id

    def print_info(self):
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))
        # здесь можно добавить код для получения информации о канале по его id
        # и выводить результат в нужном формате

channel_id = 'UCdKuE7a2QZeHPhDntXVZ91w'    # kuplinov
channel = YoutubeChannel(channel_id)
channel.print_info()  # => Information about Youtube channel with id UC-9-kyTW8ZkZNDHQJ6FgpwQ:
#   <какая--то информация о канале>
