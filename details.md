## Lambda

- `런타임 - python 3.7 선택`

- `IAM role : Lambda 호출`
  - 정책

    <img width="500" src="https://user-images.githubusercontent.com/42771578/127662049-50827b52-ccd8-405e-a456-8711cf82b071.png" alt="정책"/>

- `환경변수 등록`

- `트리거 추가`

  - `webhook 동작` >> `API Gateway 호출` >> `lambda함수 호출`
  - `EventBridge Cron 식으로 스케줄링` 

## S3

- `고유한 이름으로 생성`

- `내부 객체 생성 후 퍼블릭으로 설정` 

- `버킷 정책 생성`  
    ```
      - 정책 생성기 활용
      - action : GetObject, PutObject
      - resource : 버킷 내 객체(*)
    ```
- `모든 퍼블릭 액세스 차단` 

