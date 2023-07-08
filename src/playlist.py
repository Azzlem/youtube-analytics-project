import isodate

from src.channel import Channel


class PlayList:

    def __init__(self, playlist_id):
        self.__youtube = Channel.get_service()
        self.__playlist_id = playlist_id
        playlist_videos = self.__youtube.playlists().list(id=self.__playlist_id,
                                                          part='snippet',
                                                          maxResults=50,
                                                          ).execute()

        self.title = playlist_videos["items"][0]["snippet"]["title"]
        self.url = f"https://www.youtube.com/playlist?list={self.__playlist_id}"

    @property
    def total_duration(self):
        playlist_videos = self.__youtube.playlistItems().list(playlistId=self.__playlist_id,
                                                              part='contentDetails',
                                                              maxResults=50,
                                                              ).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        video_response = self.__youtube.videos().list(part='contentDetails,statistics',
                                                      id=','.join(video_ids)
                                                      ).execute()
        time = []
        for video in video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            time.append(duration)

        return time[0] + time[1] + time[2] + time[3]

    def show_best_video(self):
        playlist_videos = self.__youtube.playlistItems().list(playlistId=self.__playlist_id,
                                                              part='contentDetails',
                                                              maxResults=50,
                                                              ).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        video_response = self.__youtube.videos().list(part='contentDetails,statistics',
                                                      id=','.join(video_ids)
                                                      ).execute()
        like_count = 0
        url_mro_like = ""
        for video in video_response['items']:
            # YouTube video duration is in ISO 8601 format
            if int(video["statistics"]["likeCount"]) > like_count:
                like_count = int(video["statistics"]["likeCount"])
                url_mro_like = f"https://youtu.be/{video['id']}"

        return url_mro_like
