"""YouTube API v3.

Class and method to retrieve data from the youtube api.    
"""

import requests


class YouTube:
    def __init__(self, channel_id: str, api_key: str):
        self.BASE_URL = "https://youtube.googleapis.com/youtube/v3/"
        self.channel_id = channel_id
        self.api_key = api_key

    def _generate_url(self):
        return f"https://youtube.googleapis.com/youtube/v3/channels?part=brandingSettings%2CcontentDetails%2CcontentOwnerDetails%2Cid%2Clocalizations%2Csnippet%2Cstatistics%2Cstatus%2CtopicDetails&id={self.channel_id}&key={self.api_key}"

    def get_channel_data(self):
        url = self._generate_url()
        return requests.get(url)

    def get_playlist_data(self, playlist_id):
        return f"https://www.googleapis.com/youtube/v3/playlistItems?part=id%2CcontentDetails%2Csnippet%2Cstatus&key={self.api_key}&playlistId={playlist_id}&maxResults=50"
