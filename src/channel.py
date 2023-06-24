import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        api_key_my_youtube: str = os.getenv('API_YOUTYBE')

        youtube = build('youtube', 'v3', developerKey=api_key_my_youtube)

        result = youtube.channels().list(id=self.__channel_id, part="snippet, statistics").execute()

        result = json.dumps(result, indent=2, ensure_ascii=False)

        print(result)

    def init_new_object(self):
        api_key_my_youtube: str = os.getenv('API_YOUTYBE')
        youtube = build('youtube', 'v3', developerKey="AIzaSyB48i_Psq2qTM74Yjfjy88WyKxB0DFJE84")
        result = youtube.channels().list(id=self.__channel_id, part="snippet, statistics").execute()
        return [
            result["items"][0]["snippet"]["title"],
            result["items"][0]["snippet"]["description"].split(":)")[0],
            result["items"][0]["statistics"]["subscriberCount"],
            result["items"][0]["statistics"]["videoCount"],
            result["items"][0]["statistics"]["viewCount"]
        ]

    @property
    def name_zorro(self):
        return self.__channel_id

    @property
    def title(self):
        result = Channel.init_new_object(self)
        return result[0]

    @property
    def description(self):
        result = Channel.init_new_object(self)
        return result[1]

    @property
    def url(self):
        return f"https://www.youtube.com/channel/{self.__channel_id}"

    @property
    def video_count(self):
        result = Channel.init_new_object(self)
        return result[3]

    @property
    def view_count(self):
        result = Channel.init_new_object(self)
        return result[4]

    @property
    def subscriber_count(self):
        result = Channel.init_new_object(self)
        return result[2]

