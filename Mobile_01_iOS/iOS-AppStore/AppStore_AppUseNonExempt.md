# AppStore - 수출 규정 준수 정보

최초로 앱을 테스트플라잇에 올렸을 때,
AppStoreConnect에서 테스터 등록 등등의 일을 처리해야 한다. 

그런데 테스트플라잇에 업로드된 앱을 보면,  아래처럼 `수출 규정 관련 문서 누락`이라는 문구가 있는 경우가 생긴다.  
아마 최초에는 누구나 생길 것이다.  

<img width="300" alt="스크린샷 2024-02-13 오전 8 15 23" src="https://github.com/isGeekCode/TIL/assets/76529148/88f0acc0-38a1-41ad-b5e1-bcd0a4cbcc5f">

<br><br>

관리를 눌러보면 아래와 같은 화면이 발생하게 된다.  

<img width="701" alt="스크린샷 2024-02-13 오전 8 15 35" src="https://github.com/isGeekCode/TIL/assets/76529148/1224f139-6c6c-416a-8e00-406214e0730d">

<br><br>

여기서 하단의 추가 정보를 클릭하면 애플 문서로 자세한 내용을 확인할 수 있다. 

[추가정보](https://developer.apple.com/documentation/security/complying_with_encryption_export_regulations)

이런 내용이 들어있다.   
TestFlight에 앱을 제출하게 되면 우리는 미국에 있는 서버에 앱을 업로드 하게 된다.  
미국이나 캐나다 외부에서 앱을 배포하게 되면 소재지에 상관없이 그 앱 자체는 미국 수출법의 적용을 받게된다.   

그래서 만약 이 앱이 암호화를 사용, 액세스,  포함, 구현하는 등의 경우,  이는 암호화 소프트웨어의 수출로 간주된다고 한다.  
<br><br>

그렇기 때문에 앱을 업로드할 때,  앱의 암호화 알고리즘의 유형을 물어보는 것이다.  

그러니 특별히 암호화작업을 하지않았으면 "위에 언급된 알고리즘에 모두 해당하지 않음"을 체크하면 된다.  

그럼에도 불구하고, 매번 테스트플라잇에 업로드 할 때마다, 해당 내용을 물어보는 경우가 있다. 

그걸 방지하기위해 프로젝트파일의 Info.plist에 직접 프로퍼티로 삽입을 할 수가 있다.  

`App Uses Non-Exempt Encryption`키를 추가해서 값으로 No로 넣는 것인데, 

소스코드로 넣게되면, 아래 코드를 삽입하면 된다.   

```swift
<key>ITSAppUsesNonExemptEncryption</key>
<false/>
```

