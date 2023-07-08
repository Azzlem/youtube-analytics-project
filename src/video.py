from src.channel import Channel


class Video:
    """Класс для видео ютуб"""
    def __init__(self, video_id: str):
        """Экземпляр инициализируется id видео. Дальше все данные будут подтягиваться по API."""
        youtube = Channel.get_service()
        result = youtube.videos().list(id=video_id, part="snippet, statistics").execute()
        self.video_id = video_id
        self.title: str = result["items"][0]["snippet"]["title"]
        self.url = f"https://www.youtube.com/watch?v={self.video_id}"
        self.view_count: int = result["items"][0]["statistics"]["viewCount"]
        self.like_count: int = result["items"][0]["statistics"]["likeCount"]

    def __str__(self):
        """Возвращает строку с названием видео"""
        return self.title


class PLVideo(Video):
    """Класс для плейлиста видео ютуб, дочерний от Video"""
    def __init__(self, video_id: str, playlist_id: str):
        """Расширяет функционал класса Video добавлением id плейлиста"""
        super().__init__(video_id)
        self.channel_id = playlist_id


