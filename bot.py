import requests
from pprint import pprint
import config
import random

API_KEY = config.CONFIG["KEY"]
channelId = "UCyn-K7rZLXjGl7VXGweIlcA"

url = f"https://www.googleapis.com/youtube/v3/search?key={API_KEY}&part=id&channelId={channelId}&maxResults=100&q=간단&type=video"
resp = requests.get(url).json()
items = resp["items"]

idx = random.choice(range(50))
videoId = items[idx]["id"]["videoId"]
url = f"https://www.youtube.com/watch?v={videoId}"
print(url)  # 챗봇으로 넘겨


nextPageToken = resp["nextPageToken"]
url = f"https://www.googleapis.com/youtube/v3/search?key={API_KEY}&part=id&channelId={channelId}&maxResults=100&q=간단&type=video&pageToken={nextPageToken}"
resp = requests.get(url).json()
items = resp["items"]

idx = random.choice(range(50))
videoId = items[idx]["id"]["videoId"]
url = f"https://www.youtube.com/watch?v={videoId}"
print(url)  # 챗봇으로 넘겨
