### Lambda

---

- `런타임 - python 3.7 선택`

- `IAM role : Lambda 호출`

  - 정책

    <img src="details.assets/image-20210730222628711.png" alt="image-20210730222628711" style="zoom:67%;" />

- `환경변수 등록`

- `트리거 추가`

  - `webhook 동작` >> `API Gateway 호출` >> `lambda함수 호출`
  - `EventBridge Cron 식으로 스케줄링` 

### S3

---

- `고유한 이름으로 생성`
- `내부 객체 생성 후 퍼블릭으로 설정` 
- `버킷 정책 생성 - GetObject, PutObject` 
- `모든 퍼블릭 액세스 차단` 

