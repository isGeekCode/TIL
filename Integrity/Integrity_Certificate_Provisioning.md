# Integrity - 인증서와 프로비저닝 프로파일 (Certificate & Provisioning Profile ) 

## 이건 어디서 사용할까?


1. 보통 앱 타겟에서 Automatically manage signing에 체크가 되어있다.  

<img width="561" alt="스크린샷 2023-03-28 오후 11 03 12" src="https://user-images.githubusercontent.com/76529148/228265752-538433b5-eb23-4541-a0e9-66dc69383785.png">


2. 배포방법에 따라 앱을 Re-sign 할때도 Automatically manage signing에 체크가 되어있다.   

<img width="805" alt="스크린샷 2023-03-28 오후 11 01 55" src="https://user-images.githubusercontent.com/76529148/228265734-4ed45452-4951-4b9b-8c3d-c21ed00c5ede.png">




이 부분이 체크가 되어있으면 Xcode에서 자동으로 Profile, App ID, Certificate을 생성 및 업데이트 하게 되어있다.

개발자가 인식하고 있지 않더라도 위 착업을 하고 있다.

-> 2023.03.28



참고 링크 (1) : [Line Engineering - 심민영 : iOS 코드 서명에 대해서](https://engineering.linecorp.com/ko/blog/ios-code-signing) 
참고 링크 (2) : [Let'Swift 2022 - 강수진 : 인증서와 프로비저닝 프로파일]
(https://www.youtube.com/watch?v=Kbx_lBhhwDA)

