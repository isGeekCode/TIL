# Xcode Error - Unable to process request - PLA Update available

해당 앱을 테스트플라잇에 업로드하려고 할때, 이런 메세지가 생성됐다.

```
You currently don't have access to this membership resource. To resolve this issue, your team's Account Holder, 인 강, must agree to the latest Program License Agreement.

```

이런 경우엔 동일하게 appStoreConnect에서 앱 정보에 대한 새로운 작업을 할때 아래와 같은 화면이 발생한다.

<img width="600" alt="스크린샷 2023-06-20 오후 2 18 34" src="https://github.com/isGeekCode/TIL/assets/76529148/568723b0-4482-44b3-b528-ab49ff8f866c">



## 원인

이 경우는 App에 대한 마스터의 계정에서 갱신시, 비용 지불은 했지만
이때 갱신된 새로운 팀 정보, 라이센스 관련 동의를 하지않아서 생기는 원인이다.

## 해결방법

마스터 계정에서 해당 내용을 승인하면 된다. 
하지만.. 사업체로서 이걸 요청하는 구조라면 얼른 연락해서 승인받도록하자...

### 관련링크
[https://zosolution.tistory.com/95](https://zosolution.tistory.com/95)

## History
- 230620 : 초안작성
