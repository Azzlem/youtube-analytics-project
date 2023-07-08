from src.channel import Channel
import os


class Video:
    def __init__(self, video_id: str):
        youtube = Channel.get_service()
        result = youtube.videos().list(id=video_id, part="snippet, statistics").execute()
        self.video_id = video_id
        self.title = result["items"][0]["snippet"]["title"]
        self.__channel_id = result["items"][0]["snippet"]["channelId"]
        self.url = f"https://www.youtube.com/watch?v={self.video_id}&ab_channel{self.__channel_id}"
        self.view_count = result["items"][0]["statistics"]["viewCount"]
        self.like_count = result["items"][0]["statistics"]["likeCount"]

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, video_id: str, channel_id: str):
        super().__init__(video_id)
        self.channel_id = channel_id


