# SNS Login - Naver

- [네이버개발문서](https://developers.naver.com/products/login/api/)
- [레퍼런스](https://www.zehye.kr/ios/2021/09/30/iOS_social_login/#1facebook)


## 내 어플리케이션 등록하기

### 상단 Application 탭에서 어플리케이션 등록 선택

<img width="600" alt="N1" src="https://github.com/isGeekCode/TIL/assets/76529148/5d23d1de-2771-4368-ab89-c0fb165860f5">



### 어플리케이션 이름과 사용 API > 네이버 아이디 로그인 선택 후 저장

<img width="600" alt="N2" src="https://github.com/isGeekCode/TIL/assets/76529148/aa3adcdc-612c-4079-86d1-cd5fa4d9e33e">


### 네아로 선택 시 제공 정보 선택 필수, 선택 체크박스 지정

<img width="600" alt="N3" src="https://github.com/isGeekCode/TIL/assets/76529148/95c325c6-404e-4866-ac11-f4f0f5f39321">


### 로그인 오픈 API 서비스 환경 > iOS로 선택

<img width="600" alt="N4" src="https://github.com/isGeekCode/TIL/assets/76529148/e38b1eee-9745-468c-82d0-235c459c72a5">


- 다운로드 URL: 앱이 스토어에 올라가 있을 경우 그 URL을 작성하면 되며, 앱스토어에 등록되어 있지 않다면 개발 페이지 등의 사이트 주소를 작성
- URL Scheme: URL Scheme의 경우 프로젝트의 URL Types로 등록을 해야 한다.
주의할 점은 반드시 소문자로 작성해야한다는 점이다.


- 필요할 경우, Xcode에 URL Scheme 세팅 


<img width="600" alt="N5" src="https://github.com/isGeekCode/TIL/assets/76529148/2eb8f6a8-82b2-4689-84e0-24229f4264ce">


## NaverSDK 설치

### CocoaPOD

- PODfile에 아래 텍스트 추가
```
 pod 'naveridlogin-sdk-ios'

```


### info.plist 설정하기

```swift
<key>LSApplicationQueriesSchemes</key>
  <array>
    <string>naversearchapp</string>
    <string>naversearchthirdlogin</string>
  </array>
```

### AppDelegate에 NaverSDK 초기화

```swift
import NaverThirdPartyLogin

class AppDelegate: UIResponder, UIApplicationDelegate {

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        NaverThirdPartyLoginConnection.getSharedInstance().isInAppOauthEnable = true
        NaverThirdPartyLoginConnection.getSharedInstance().isNaverAppOauthEnable = true

        let instance = NaverThirdPartyLoginConnection.getSharedInstance()
        instance?.isNaverAppOauthEnable = true
        instance?.isInAppOauthEnable = true

        instance?.serviceUrlScheme = kServiceAppUrlScheme
        instance?.consumerKey = kConsumerKey
        instance?.consumerSecret = kConsumerSecret
        instance?.appName = kServiceAppName

        return true
    }
}

```


- kServiceAppUrlScheme: 애플리케이션 등록할 때 입력한 URL Scheme
- kConsumerKey: 애플리케이션 등록 후 발급받은 클라이언트 아이디
- kConsumerSecret: 애플리케이션 등록 후 발급받은 클라이언트 시크릿
- kServiceAppName: 애플리케이션 이름


위 설정을 위해서 NaverThirdPartyConstantForApp.h 파일로 이동한다.

- 해당 위치에서 이 값들을 수정한다. 

<img width="600" alt="N7" src="https://github.com/isGeekCode/TIL/assets/76529148/4d23af2f-ad55-4301-90f7-799c5f59bd60">

## AppDelegate만 지원하는 경우

```swift
import NaverThirdPartyLogin


func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
      NaverThirdPartyLoginConnection.getSharedInstance()?.application(app, open: url, options: options)
      return true
}
```

## SceneDelegate를 지원하는 경우
```swift
import NaverThirdPartyLogin


func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
  NaverThirdPartyLoginConnection
    .getSharedInstance()?
    .receiveAccessToken(URLContexts.first?.url)
}
```

## 동작구현

- `oauth20ConnectionDidFinishRequestACTokenWithAuthCode()`: 로그인에 성공했을 경우 호출되는 함수
- `oauth20ConnectionDidFinishRequestACTokenWithRefreshToken()`: 접근 토큰을 갱신할 때 호출되는 함수
- `oauth20ConnectionDidFinishDeleteToken()`: 토큰 삭제를 하면 호출되는 함수(로그아웃에 사용)
- `oauth20Connection(_ oauthConnection: NaverThirdPartyLoginConnection!, didFailWithError error: Error!)`: 네아로에 모든 에러에 호출되는 함수


```swift
extension ViewController: NaverThirdPartyLoginConnectionDelegate {
    @objc func naverLogin(_ sender: Any) {
        naverConnection?.delegate = self
        naverConnection?.requestThirdPartyLogin()
    }

    @objc func naverLogoutBtn(_ sender: Any) {
        naverConnection?.requestDeleteToken()
    }

    func oauth20ConnectionDidFinishRequestACTokenWithAuthCode() {
        print("Success Login")
        self.getInfo()
    }

    func oauth20ConnectionDidFinishRequestACTokenWithRefreshToken() {
        self.getInfo()
    }

    func oauth20ConnectionDidFinishDeleteToken() {
        print("logout")
    }

    func oauth20Connection(_ oauthConnection: NaverThirdPartyLoginConnection!, didFailWithError error: Error!) {
        print("error = \(error.localizedDescription)")
    }

    func getInfo() {
        // 현재 토큰이 유효한지 확인 > default로 1시간
        guard let isValidAccessToken = naverConnection?.isValidAccessTokenExpireTimeNow() else { return }

        if !isValidAccessToken {
            return
        }

        guard let tokenType = naverConnection?.tokenType else { return }
        guard let accessToken = naverConnection?.accessToken else { return }

        let urlStr = "https://openapi.naver.com/v1/nid/me"
        let url = URL(string: urlStr)!

        let authorization = "\(tokenType) \(accessToken)"
        let req = AF.request(url, method: .get, parameters: nil,
          encoding: JSONEncoding.default, headers: ["Authorization": authorization])

        req.responseJSON {(response) in
            print(response)

            guard let result = response.value as? [String: AnyObject] else { return }
            guard let object = result["response"] as? [String: AnyObject] else { return }
            let name = object["name"] as? String
            let id = object["id"] as? String
            let image = object["profile_image"] as? String

            print("name: ", name ?? "no name")
            print("id: ", id ?? "no id")
            print("image: \(image)")
        }
    }  
}
```


## History
- 230813 : 초안작성
