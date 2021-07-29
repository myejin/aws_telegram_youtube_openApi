import requests
import boto3
import os
import json
from datetime import datetime


def lambda_handler(event, context):
    chat_id = ""
    id_list = json.loads(os.environ["ID_LIST"]).values()
    try:
        if "detail-type" in event and event["detail-type"] == "Scheduled Event":
            video_set = get_videoset()
            for id in id_list:
                chat_id = id
                send_message(chat_id, video_set)
        else:
            resp = json.loads(event["body"])
            user_text = resp["message"]["text"]
            chat_id = resp["message"]["from"]["id"]

            if chat_id in id_list:
                user_text = user_text.strip()
                if user_text == "업데이트" and chat_id == int(os.environ["ME"]):
                    update_list()
                    send_message(chat_id, msg="update")
                elif user_text == "네" or user_text == "ㅇㅇ":
                    video_set = get_videoset()
                    send_message(chat_id, video_set)
                    send_message(chat_id, msg="feedback")
                elif user_text[-2:] == "검색":
                    video_set = crawl_url(user_text[:-2].strip())
                    send_message(chat_id, video_set)
                    send_message(chat_id, msg="feedback")
                elif user_text[0] == "*" and user_text[-1] == "*":
                    send_message(os.environ["ME"], msg=user_text)
                else:
                    send_message(chat_id, msg="greeting")
            elif user_text == os.environ["HIDDEN_MSG"]:
                send_message(os.environ["ME"], msg=f"[{user_text}]\nID : {chat_id}")

    except Exception as e:
        send_message(chat_id, msg=str(e))


def send_message(chat_id, video_set=None, msg=None):
    token = os.environ["BOT_TOKEN"]

    if msg == "'items'":
        msg = f"오늘 조회가능한 횟수를 초과했어요!!😉"
    elif msg == "greeting":
        msg = f"오늘의 메뉴가 궁금하세요?👩‍🍳\n\t랜덤검색 - '네' 또는 'ㅇㅇ' 입력\n\t메뉴검색 - '김치찌개 검색'"
    elif msg == "feedback":
        msg = f"만족/불만족 하셨다면 후기📝를 남겨주세요.\n[작성예시] *별 안에 후기를 써주세요.*"
    elif msg == "update":
        msg = "업데이트 완료"
    elif msg is None:
        video_pop = video_set.pop()
        now = time_message()
        msg = f"✨오늘 {now}메뉴 추천✨\n\n🍳{video_pop}\n\n메뉴를 다시 찾아볼까요?🥺\n\t랜덤검색 - '네' 또는 'ㅇㅇ' 입력\n\t메뉴검색 - '김치찌개 검색'"
    elif msg[0] == "*" and msg[-1] == "*":
        msg = "📨 사용자 후기\n\n" + msg[1:-1]
    elif msg[0] == "[":
        pass
    else:
        msg = "시스템 오류 발생!!"
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"
    resp = requests.get(url)


def crawl_url(query=None):
    video_list = []
    api_key = os.environ["KEY"]

    """특정메뉴 검색, 2개만 반환"""
    if query is not None:
        url = f"https://www.googleapis.com/youtube/v3/search?key={api_key}&part=id&channelId=UCyn-K7rZLXjGl7VXGweIlcA&maxResults=2&q={query}&type=video"
        resp = requests.get(url).json()
        items = resp["items"]

        for item in items:
            videoId = item["id"]["videoId"]
            url = f"https://www.youtube.com/watch?v={videoId}"
            video_list.append(url)
        return set(video_list)

    """업데이트 시 전체 크롤링"""
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


def time_message():
    hour = (datetime.now().hour + 9) % 24
    if 3 <= hour < 10:
        return "아침"
    elif 10 <= hour < 15:
        return "점심"
    elif 15 <= hour < 21:
        return "저녁"
    else:
        return "야식"


def get_videoset():
    s3 = boto3.client("s3")

    obj = s3.get_object(Bucket=os.environ["BUCKET"], Key=os.environ["BUCKET_KEY"])
    data = json.loads(obj["Body"].read())
    return set(data["urls"])


def update_list():
    s3 = boto3.client("s3")
    urls = crawl_url()
    Body = json.dumps({"urls": urls})
    s3.put_object(
        Bucket=os.environ["BUCKET"], Body=Body, Key=os.environ["BUCKET_KEY"], ContentType="json"
    )
    return Body
