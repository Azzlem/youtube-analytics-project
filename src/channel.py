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

        api_key_my: str = os.getenv('API')

        youtube = build('youtube', 'v3', developerKey=api_key_my)

        r = youtube.channels().list(id="UC-OVMPlMA3-YCIeg4z5z23A", part="snippet, statistics").execute()

        def printj(dict_to_print: dict) -> None:
            """Выводит словарь в json-подобном удобном формате с отступами"""
            print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

        print(printj(r))
