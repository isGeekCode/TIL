# External Link (외부링크) - 커스텀 앱스키마 만들기, 사용하기

Target - info 에서 하단의 URL Types에 내용을 추가한다. 

<img width="700" alt="스크린샷 2023-01-11 오후 1 15 43" src="https://user-images.githubusercontent.com/76529148/211722963-8a77980f-bb45-4ce6-9751-2f4175910bf9.png">

- identifier: 앱의 identifier
- URL Schemes: 앱이름

입력하고 나면 사파리나 크롬에서 url에 `앱이름://` 의 형태로 입력을 할때 앱을 열겠냐는 얼럿이 생성된다. 

## 앱스키마로 파라미터 넘기기

안드로이드의 경우 스키마 이름과 호스트 이름을 각각 지정하여 **'스키마://호스트?파라미터'** 형식이었지만, 

iOS는 호스트네임이 빠져서 **'스키마://?파라미터'** 로 보내면 된다.

`스키마이름://?abc=def`

이때 abc는 key값 def는 value값이다. 

앱스키마로 앱이 열리면 아래 `Appdelegate`의 함수 에서 실행되는데 `urlComponent`와 `items`를 이용하여 데이터를 아래와 같이 다룰 수 있다. 

```swift
@available(iOS 9.0, *)
public func application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {

    let urlComponents = URLComponents(url: url, resolvingAgainstBaseURL: false)
    let items = urlComponents?.queryItems


    let title = items?.first?.name
    let text = items?.first?.value

    return true
}
```

### 외부링크의 캐치

위 예시에서 나온것처럼 함수를 사용할 수 있지만 iOS 9.0부터 가능하기 때문에 아래와 같이 선언해서 사용한다.

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    
    // 아래 함수를 호출
    return application(app, open: url, sourceApplication: options[UIApplication.OpenURLOptionsKey.sourceApplication] as? String, annotation: "")
}

// 실제 사용하는 함수
func application(_ application: UIApplication, open url: URL, sourceApplication: String?, annotation: Any) -> Bool {

    let urlString = url.absoluteString
    print("External Link :: \(urlString)")
    // 외부링크를 캐치한 후 동작을 구현하는 곳
    return true
}
```

## DeepLink

딥링크란 앱 내부의 특정 화면으로 이동하는 기능이다. 예를 들어, SNS에서 공유된 링크를 클릭하면 앱 내부의 특정 컨텐츠 화면으로 이동하는 것이다.

-> 23.04.05
