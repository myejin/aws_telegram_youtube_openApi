import requests
import os
import json


def lambda_handler(event, context):
    chat_id = ""
    id_list = json.loads(os.environ["ID_LIST"]).values()
    try:
        if "detail-type" in event and event["detail-type"] == "Scheduled Event":
            video_set = crawl_url()
            for id in id_list:
                chat_id = id
                send_message(chat_id, video_set)
        else:
            resp = json.loads(event["body"])
            user_text = resp["message"]["text"]
            chat_id = resp["message"]["from"]["id"]

            if chat_id in id_list:
                if user_text == "메뉴검색" or user_text == "네" or user_text == "ㅇㅇ":
                    video_set = crawl_url()
                    send_message(chat_id, video_set)
                else:
                    send_message(chat_id, msg="greeting")

    except Exception as e:
        send_message(chat_id, msg=str(e))


def send_message(chat_id, video_set=None, msg=None):
    token = os.environ["BOT_TOKEN"]

    if msg == "'items'":
        msg = f"오늘 조회가능한 횟수를 초과했어요!!😉"
    elif msg == "greeting":
        msg = f"오늘의 메뉴가 궁금하세요?👩‍🍳\n('메뉴검색' 또는 '네' 또는 'ㅇㅇ' 입력)"
    elif msg is None:
        video_pop = video_set.pop()
        msg = f"✨오늘 저녁메뉴 추천✨\n\n🍳{video_pop}\n\n메뉴를 다시 찾아볼까요?🥺\n('메뉴검색' 또는 '네' 또는 'ㅇㅇ' 입력)"
    else:
        msg = "시스템 오류 발생!!"
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"
    resp = requests.get(url)


def crawl_url():
    video_set = set()
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
            video_set.add(url)
    return video_set
