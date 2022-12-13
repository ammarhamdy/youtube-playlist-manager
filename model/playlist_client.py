

# def get_videos_duration(api_service, videos_ids: list):
#     # request the target videos of the playlist.
#     video_request = api_service.videos().list(
#         part="contentDetails",
#         id=",".join(videos_ids)
#     )
#     # execute our video request.
#     video_response = video_request.execute()
#     # return the durations of videos.
#     return [
#         video_item['contentDetails']['duration']
#         for video_item in video_response['items']
#     ]


class PlaylistClient:
    def __init__(self, api_service, playlist_id):
        self.api_service = api_service
        self.playlist_id = playlist_id
        self.id_request = None
        self.videos_request = None
        self.videos_ids = []
        self.init_requestes()

    def init_requestes(self):
        # init the target playlist request.
        self.id_request = self.api_service.playlistItems().list(
            part="contentDetails",
            playlistId=self.playlist_id,
            maxResults=100,
            pageToken=None
        )
        self.videos_ids = self.get_videos_ids()
        # init the target videos request.
        self.videos_request = self.api_service.videos().list(
            part="snippet,statistics,contentDetails",
            id=",".join(self.videos_ids)
        )

    def get_videos_ids(self):
        """ return all ids of videos on the target playlist if it is not empty playlist """
        # execute our playlist ids request.
        try:
            id_respond = self.id_request.execute()
        except Exception as _:
            return []
        # check if that playlist is empty.
        if len(id_respond["items"]) < 0:
            return []
        else:
            return [
                item["contentDetails"]["videoId"]
                for item in id_respond["items"]
            ]

    def request(self):
        """ get details of target videos """
        # execute videos details request.
        if self.videos_ids:
            return True,  self.videos_request.execute()["items"]
        else:
            return False, "make sure that url for public playlist not private."



