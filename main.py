import os
import pytest
from google.oauth2.credentials import Credentials
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
        self.name = None
        self.description = None
        self.link = None
        self.subscribers = None
        self.video_count = None
        self.view_count = None
        self.url =None

    @classmethod
    def get_service(cls):
        credentials = Credentials.from_authorized_user_file('path/to/credentials.json',
                                                               ['https://www.googleapis.com/auth/youtube.readonly'])
        return build('youtube', 'v3', credentials=credentials)

        youtube = YoutubeChannel.get_service()
        request = youtube.channels().list(
            part="snippet,statistics",
            id=channel_id
        )
        response = request.execute()
        item = response['items'][0]

        self.name = item['snippet']['title']
        self.description = item['snippet']['description']
        self.link = f"https://www.youtube.com/channel/{channel_id}"
        self.subscribers = int(item['statistics']['subscriberCount'])
        self.video_count = int(item['statistics']['videoCount'])
        self.view_count = int(item['statistics']['viewCount'])



    def to_json(self):
        data = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "link": self.link,
            "subscribers": self.subscribers,
            "video_count": self.video_count,
            "view_count": self.view_count
        }
        with open("channel.json", "w") as file:
            json.dump(data, file)

    def print_info(self):
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))
        # здесь можно добавить код для получения информации о канале по его id
        # и выводить результат в нужном формате

if __name__ == '__main__':
    channel_id = 'UCdKuE7a2QZeHPhDntXVZ91w'    # kuplinov
    channel = YoutubeChannel(channel_id)
    channel.print_info()  # => Information about Youtube channel with id UCdKuE7a2QZeHPhDntXVZ91w:
#   <какая--то информация о канале>
    print(channel.description)
    print(channel.video_count)
    print(channel.url)