import requests
from pprint import pprint
import config
import random
from telegram.ext import Updater, MessageHandler, Filters

video_list = []


def handler(update, context):
    user_text = update.message.text
    if user_text == "네" or user_text == "다시":
        send_message()


def bot_updater():
    token = config.CONFIG["BOT_TOKEN"]
    updater = Updater(token=token, use_context=True)
    updater.start_polling()
    echo_handler = MessageHandler(Filters.text, handler)
    updater.dispatcher.add_handler(echo_handler)


def send_message():
    global video_list
    idx = random.choice(range(len(video_list)))

    token = config.CONFIG["BOT_TOKEN"]
    chat_id = config.CONFIG["ChatId"]

    msg = "✨오늘 저녁메뉴 추천✨\n\n🍳" + video_list[idx] + "\n\n메뉴를 다시 찾아볼까요?🥺\n('네' 또는 '다시' 입력)"
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"
    resp = requests.get(url)


def crawl_url():
    channel_id = "UCyn-K7rZLXjGl7VXGweIlcA"
    api_key = config.CONFIG["KEY"]
    nextPageToken = ""
    video_list = []
    finished = False
    while not finished:
        url = f"https://www.googleapis.com/youtube/v3/search?key={api_key}&part=id&channelId={channel_id}&maxResults=100&q=간단+재료&type=video"
        if nextPageToken:
            url += f"&pageToken={nextPageToken}"

        resp = requests.get(url).json()
        pprint(resp)
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


if __name__ == "__main__":
    video_list = crawl_url()
    bot_updater()
