## 백파더 메뉴추천봇:iphone:
#### :fork_and_knife: 소개<br>
```
pass
```
<br>

#### :rice_ball: 개발 배경<br>
```
저녁메뉴 정하기 힘들어서 만들게 된 챗봇
유투브 채널 '백종원의 요리비책' 에서 영상 크롤링
똥손도 도전할 수 있는 요리법 랜덤 추천
```
<br>

#### :ramen: 사전 준비<br>
- `Telegram bot 생성 + chat_id 파싱`
- `YouTube Data API v3 KEY 발급`
<br>

#### :curry: 실행 방법<br>
```
  1) AWS Lambda 에 bot.py 업로드
  2) API Gateway와 연동하여 Webhook 세팅
  3) CloudWatch events 트리거 추가하여 원하는 시간대에 알람 요청 (선택)
```
<img width="382" alt="트리거" src="https://user-images.githubusercontent.com/42771578/126987497-674a63ab-beec-451f-81c1-a518381aa597.PNG">
<br>
