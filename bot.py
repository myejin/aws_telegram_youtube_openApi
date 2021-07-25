import requests
import random
import os


def lambda_handler(event, context):
    try:
        user_text = event["result"]["text"]
        if user_text == "네" or user_text == "다시":
            video_list = crawl_url()
            send_message(video_list)

    except Exception:
        send_message()


def send_message(video_list=None):
    token = os.environ["BOT_TOKEN"]
    chat_id = os.environ["ChatId"]

    msg = ""
    if video_list is None:
        msg = f"오늘 조회가능한 횟수를 초과했어요!!"
    else:
        idx = random.choice(range(len(video_list)))
        msg = "✨오늘 저녁메뉴 추천✨\n\n🍳" + video_list[idx] + "\n\n메뉴를 다시 찾아볼까요?🥺\n('네' 또는 '다시' 입력)\n"
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"
    resp = requests.get(url)


def crawl_url():
    video_list = []
    api_key = os.environ["KEY"]
    nextPageToken = ""
    finished = False

    while not finished:
        url = f"https://www.googleapis.com/youtube/v3/search?key={api_key}&part=id&channelId=UCyn-K7rZLXjGl7VXGweIlcA&maxResults=100&q=간단+재료&type=video"
        if nextPageToken:
            url += f"&pageToken={nextPageToken}"

        resp = requests.get(url).json()
        items = resp["items"]
        if "nextPageToken" in resp:
            nextPageToken = resp["nextPageToken"]
        else:
            finished = True

        for item in items:
            videoId = item["id"]["videoId"]
            url = f"https://www.youtube.com/watch?v={videoId}"
            video_list.append(url)
    return video_list
