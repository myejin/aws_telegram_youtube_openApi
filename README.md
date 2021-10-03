## 백파더 메뉴추천봇:iphone:
#### :fork_and_knife: 소개<br>
```
AWS Lambda 활용한 텔레그램 챗봇
```

&nbsp;&nbsp;<img width="190" alt="추천" src="https://user-images.githubusercontent.com/42771578/127655177-35eaa875-562f-483b-8269-0e018655a707.png">&nbsp;&nbsp;&nbsp;&nbsp;<img width="190" alt="이벤트" src="https://user-images.githubusercontent.com/42771578/127655190-99f1217c-f2f0-409c-bf34-fb242db864c8.png">&nbsp;&nbsp;<img width="190" alt="후기" src="https://user-images.githubusercontent.com/42771578/135743231-b45dc93f-109a-4045-83fa-f7b3a1e8f160.png">
<br><br>

#### :rice_ball: 개발 배경<br>
```
저녁메뉴 정하기 힘들어서 만들게 된 챗봇
유투브 채널 '백종원의 요리비책' 에서 영상 크롤링
똥손도 도전할 수 있는 요리법 랜덤 추천
```
<br>

#### :ramen: 사전 준비<br>
- `Telegram bot 생성 + bot_token과 chat_id 파싱`
- `YouTube Data API v3 KEY 발급`
- `AWS 계정 (Lambda, S3, API Gateway, EventBridge 사용)`
<br>

#### :curry: 실행 방법<br>
```
  1) AWS Lambda 에 bot.py 업로드
  2) AWS S3 버킷 생성 및 권한설정
  3) API Gateway와 연동하여 Webhook 세팅
  4) CloudWatch events 트리거 추가하여 원하는 시간대에 알람 요청 (선택)
```
##### &nbsp; [:white_check_mark: AWS 상세 세팅방법](https://github.com/myejin/Menu_Selector_Bot/blob/main/details.md)
  
<img width="382" alt="트리거" src="https://user-images.githubusercontent.com/42771578/126987497-674a63ab-beec-451f-81c1-a518381aa597.PNG">
<br>
