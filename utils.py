"""Utils for the main application"""

import json
import re

import requests
import youtube_api_v3 as yt
from settings import API_KEY


def get_info_from_subscriptions():
    with open("extracts/subscription.json", "r", encoding="utf-8") as f:
        channels = json.load(f)

    for channel in channels:
        print(channel["title"])
        youtube = yt.YouTube(channel["link"], API_KEY)
        response = youtube.get_channel_data()
        output_json = json.loads(response.text)
        file_name = output_json["items"][0]["snippet"]["title"].replace(" ", "_").lower()
        file_name = re.sub(r"/W", "_", file_name)
        print(file_name)
        with open(f"extracts/z_{file_name}.json", "w", encoding="utf-8") as f:
            f.write(response.text)

def get_channel_id_from_video(video_url):
    video_id = video_url.split("v=")[1]
    api_url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={API_KEY}"
    breakpoint()
    response = requests.get(api_url)
    data = response.json()

    channel_id = data['items'][0]['snippet']['channelId']
    print("Channel ID:", channel_id)

    with open("D:/UserFiles/Projects/Python/daily_feeds/feeds/scraper/crawler/youtube/subscriptions.txt", "a") as f:
        f.write(f"{channel_id}\n")
