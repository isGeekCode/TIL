# SNS Login - Kakao

- [카카오개발문서](https://developers.kakao.com/)
- [레퍼런스](https://www.zehye.kr/ios/2021/09/30/iOS_social_login/#1facebook)


## Kakao 개발자 사이트에서 앱 등록하기

[홈페이지 ‘내 어플리케이션’ 클릭] > [내 어플리케이션 추가하기 클릭] > [앱 이름 작성 후 저장]

1. 플랫폼 등록
[만들어 놓은 앱 선택] > [플랫폼 설정하기 클릭] > [iOS 플랫폼 등록 클릭] > [번들 ID 작성 후 저장]

2. 카카오 로그인 설정
[왼쪽 탭에서 카카오 로그인 클릭] > [활성화 설정 ON] > [활성화 버튼 클릭]


3. 동의항목 설정
[왼쪽 탭에서 동의항목 클릭] > [원하는 항목 설정 버튼 클릭] > [필수/선택 동의 선택 후 동의목적 필수 작성, 카카오 계정으로 정보수집 후 제공 체크박스 선택]

- 프로필 정보를 제외한 다른 동의 항목의 ‘필수 동의’설정은 사용이 불가능함
- 설정한 동의 항목 내역은 내가 만든 앱의 카카오 로그인 동의 화면에 반영됨
- 동의 목적은 참고 문구로 카카오 로그인 동의 화면에는 나타나지 않으나, 해당 동의 하ㅇ목 이용 권한 검수에 사용됨


## KakaoSDK 설치하기
터미널에서 vi Podfile을 통해 SDK 작성

```swift
pod 'KakaoSDKCommon', '= 2.0.5'
pod 'KakaoSDKAuth', '= 2.0.5'
pod 'KakaoSDKUser', '= 2.0.5'
```

> pod isntall하게 되면
> SDK에 필요한 외부라이브러리가 자동으로 설치된다 > Alamofire, DynamicCodable



## info.plist 설정하기

```swift
<key>LSApplicationQueriesSchemes</key>
  <array>
      <!-- 카카오톡으로 로그인 -->
      <string>kakaokompassauth</string>
      <!-- 카카오링크 -->
      <string>kakaolink</string>
  </array>
```

## URL Scheme 설정하기
앱 > 타겟 > info에서 URL Type + 버튼 클릭

- URL Schemes 항목에 네이티브 앱 키를 kakao{네이티브 앱 키} 형식으로 등록해준다.
- 네이티브 앱 키는 좀전에 카카오 개발자 홈페이지에서 내가 등록한 어플리케이션을 선택하면 확인할 수 있다.
- 이 설정을 누락한다면 카카오링크 메시지를 통해 앱을 실행하는 것이 불가능해진다.

## AppDelegate에 KakaoSDK 초기화

```swift
import KakaoSDKCommon



func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    KakaoSDKCommon.initSDK(appKey: "NATIVE_APP_KEY")
}
```


## AppDelegate만 사용하는 경우


```swift
import KakaoSDKAuth

...


class AppDelegate: UIResponder, UIWindowSceneDelegate {
   ...
   func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    if (AuthApi.isKakaoTalkLoginUrl(url)) {
      return AuthController.handleOpenUrl(url: url)
    }
   return false
   }
   ...
}

```


## SceneDelegate만 사용하는 경우



```swift
import KakaoSDKAuth
...
class SceneDelegate: UIResponder, UIWindowSceneDelegate {
    ...
    func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
        if let url = URLContexts.first?.url {
            if (AuthApi.isKakaoTalkLoginUrl(url)) {
                _ = AuthController.handleOpenUrl(url: url)
            }
        }
    }
    ...
}

```


## 카카오톡으로 로그인 구현하기



```swift
extension ViewController {
    @objc func kakaoLogin(_ sender: Any) {
        AuthApi.shared.loginWithKakaoTalk {(oauthToken, error) in
            if let error = error {
                print(error)
            } else {
                print("login kakao")
                _ = oauthToken
            }
        }
    }

    private func setUserInfo() {
        UserApi.shared.me {(user, error) in
            if let error = error {
                print(error)
            } else {
                print("me() success")
                _ = user
                print("nickname: \(user?.kakaoAccount?.profile?.nickname ?? "no nickname")")
                print("image: \(user?.kakaoAccount?.profile?.profileImageUrl)")
            }
        }
    }

    @objc func kakaoLogoutBtn(_ sender: Any) {
    UserApi.shared.logout{(error) in
        if let error = error {
            print(error)
        } else {
            print("kakao logout success")
        }
    }
}

```



## 카카오계정으로 로그인 구현하기
```


    @objc func kakaoLogin(_ sender: Any) {
        UserApi.shared.loginWithKakaoAccount {(oauthToken, error) in
                if let error = error {
                    print(error)
                }
                else {
                    print("loginWithKakaoAccount() success.")            

                    //do something
                    _ = oauthToken            
                }
        }
    }


```

## History
- 230813 : 초안작성
