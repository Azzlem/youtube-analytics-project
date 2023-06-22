import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        api_key_my_youtube: str = os.getenv('API_YOUTYBE')

        youtube = build('youtube', 'v3', developerKey=api_key_my_youtube)

        result = youtube.channels().list(id=self.channel_id, part="snippet, statistics").execute()

        result = json.dumps(result, indent=2, ensure_ascii=False)

        print(result)
