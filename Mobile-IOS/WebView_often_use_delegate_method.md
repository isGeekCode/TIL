# WebView - 자주 사용하는 메서드

## load( \_: )

HTML 파일을 읽어들일 때 사용. 쉽게 말해 웹페이지를 로드한다고 생각을 하시면 될 거 같습니다.

비동기 메서드라 동시에 다른 로직을 처리할 수 있어 앱이 자연스럽게 진행이 되어가는 장점이 있습니다.

```swift
func load(_ request: URLRequest) -> WKNavigation?
```

## \***\*loadHTMLString(\_:baseURL:)\*\***

말 그대로 HTMLString을 읽어오는 메서드로 직접 웹페이지를 로드해서 웹페이지로 이동을 하거나 개발자가 만든 URL로 이동하게 함

- 첫 번째불러올 웹페이지 url을 읽어오는 것입니다.
- 두 번째relative URL을 해결할 때 사용되는 기본 URL

```swift
func loadHTMLString(_ string: String,
            baseURL: URL?) -> WKNavigation?
```

## isLoading

웹페이지의 로딩진행여부를 확인하는 프로퍼티

```swift
var isLoading: Bool
```

## stopLoading()

웹페이지가 로딩 중일 때 중단을 하고자 사용을 하는 메서드입니다.

만약 load 메서드가 실행 중이다가 이 메서드가 호출이 되면 load메서드는 실행이 중단돼버립니다.

```swift
func stopLoading()
```

## reload()

이 메서드는 현재 웹페이지를 리로딩하게 해주는 동작 메서드로 멈춘 로딩을 다시 시작하게 해주는 메서드입니다.

```swift
func reload() -> WKNavigation?
```

## goBack()

현재 웹페이지에서 뒤로 가기 버튼의 기능을 하는 메서드로 현재 웹페이지에서 뒤로 보내주게 됩니다.

만약 현재 웹페이지에서 뒤로가기 아이템이 없다면 nil을 반환하게 되어 아무 동작도 하지를 않습니다.

## goForward()

이 메서드는 현재 웹페이지에서 앞으로 가기 버튼의 기능과 같은 메서드입니다.

위 goBack()과 같이 만약 이 페이지가 끝에 있는 마지막 페이지여서 앞으로 갈 아이템이 없다면 nil을 반환하게 돼 아무 동작을 하지 않습니다.

## backForwardList

```swift
var backForwardList: WKBackForwardList
```

backForwardList 타입은 WKBackForwardList클래스 타입으로 이 클래스 타입은 웹뷰에서 방문했던 웹페이지의 리스트를 관리하는 객체입니다.

따라서 방문했던 웹페이지를 가기 위해서 해당 프로퍼티를 사용하면 될 것 같습니다.

# Delegate메서드

# 1. WKNavigationDelegate

[https://developer.apple.com/documentation/webkit/wknavigationdelegate](https://developer.apple.com/documentation/webkit/wknavigationdelegate)

해당 프로토콜에서 웹페이지 로딩이 호출될 때 사용되는 메서드

1. webView(\_:decidePolicyFor:descisionHandler:) 웹페이지를 읽어올지 탐색여부를 결정하는 메서드
2. webView(\_:didStartProvisionNavigation:)웹뷰가 콘텐츠 탐색을 시작할 때 호출
3. webView(_:didCommit:)_ 웹뷰가 콘텐츠를 받기 시작할때 호출
4. webView(\_:didFinish:)웹뷰가 콘텐츠 받기를 완료했을 때 호출
5. webView(\_:didFail:withError:)웹 뷰가 콘텐츠를 받기 실패했을 때 호출

이 메서드는 load메서드를 통해 웹페이지를 로딩했을 때 호출이 되고 만약 웹페이지 안에서 다른 페이지로 넘어갔을 때도 호출이 됩니다.

그런데 만약에 웹 전체를 교체하는 게 아니라 AJAX방식인 부분적인 웹 부분만 교체하는 방식의 웹뷰라면 델리게이트 메서드 호출 순서가 다를 수가 있어 조심하게 다뤄야 합니다

### webView(\_:decidePolicyFor:descisionHandler:)

```swift
optional func webView(_ webView: WKWebView,
      decidePolicyFor navigationAction: WKNavigationAction,
          preferences: WKWebpagePreferences,
      decisionHandler: @escaping (WKNavigationActionPolicy, WKWebpagePreferences
```

웹뷰가 웹페이지를 읽어올지 탐색여부를 결정하는 메서드

- Parameter
  - webView: 해당 웹뷰
  - navigationAction:
    - 탐색 요청을 트리거한 작업에 대한 세부 정보를 포함하고 있는 객체
    - URLRequest로부터 URL을 호출할 때 해당 매개변수로 접근
  - preferences
    - 새로운 웹페이지를 보여줄 때 사용하는 기본 환경설정 정보
  - decisionHandler
    - 함수 타입으로 특정 인자 값을 넣어 호출을 함으로써 웹페이지의 로딩 여부를 결정. 이 매개변수를 사용하면 특정 url을 들어가는 웹페이지를 차단을 할 수 있는데 그 방법은 해당 함수의 인자 값을. cancel로 바꿔서 호출하면 됩니다.

### decisionHandler 사용법

1. 차단을 하고 싶으면decisionHandler(. cancel)
2. 허용을 하고 싶으면decisionHandler(. allow)

만약 특정 urldmf 차단을 하고 싶으면 아래와 같이 코드를 작성하며 됩니다.

```swift
optional func webView(_ webView: WKWebView, decidePolicyFor navigationAction: WKNavigationAction, preferences: WKWebpagePreferences,
decisionHandler: @escaping (WKNavigationActionPolicy )-> Void) {

guard let url = navigationAction.request.url?.absoluteString else { return }

    if url.start(with: “http”) {

    decisionHandler(.cancel)

    }
}
```

- navigationAction의 매개변수를 통해서 request 했던 url을 읽어와 해당 URL이 http이 시작을 하면 decisionHandler(. cancel)을 통해 차단을 하는 방식입니다.

### webView(\_:didStartProvisionNavigation:)

```swift
optional func webView(_ webView: WKWebView,
didStartProvisionalNavigation navigation: WKNavigation!)
```

웹뷰가 콘텐츠를 로드하기 시작할 때 호출되는 메서드

### webView(\_:didCommit:)

```swift
optional func webView(_ webView: WKWebView,
            didCommit navigation: WKNavigation!)
```

- 웹뷰가 메인 프레임을 위한 콘텐츠를 받기 시작할 때 호출되는 메서드로 콘텐츠를 받기 시작할때 처리해줄 것이 있을 때 사용을 하면 됩니다.
- 로딩 상태를 표시해주는 액티비티 인디케이터 뷰를 사용할 때에도 사용이 되는 메서드
  → **액티비티 인디케이터 뷰를 사용하는 목적은 웹페이지를 로딩할 때 시간이 꽤 걸리는 경우가 있어 사용자에게 앱이 죽은 게 아니라 로딩이 되어있다는 것을 보여주기 위해 액티비티 인디케이터 뷰를 사용하게 됩니다.**

### webView(\_:didFinish:)

```swift
optional func webView(_ webView: WKWebView,
            didFinish navigation: WKNavigation!)
```

- 웹뷰가 콘텐츠 데이터를 받아오는 것을 모두 마쳤을 때 호출되는 메서드입니다. 즉 웹페이지가 웹뷰에 완전히 보여주고 나면 호출이 된다고 생각을 하시면 됩니다.
- 또 이때 didCommit때 보여줬던 액티비티 인디케이터 뷰를 보여줬는데요, 만약 웹뷰에 모두 로딩이 되었는데도 로딩이 계속되면 사용자가 당황 하겠죠? 그러므로 **인디케이터뷰를 숨겨주는 코드를 여기에 작성을 해주면 됩니다.**

### webView(\_:didFail:withError:)

```swift
optional func webView(_ webView: WKWebView,
              didFail navigation: WKNavigation!,
            withError error: Error)
```

- 이 메서드는 콘텐츠 로딩이 실패를 했을 때 호출이 되는 메서드로 웹페이지를 불러오는 도중에 실패했을 때 호출이 되는 메서드입니다.
- 세 번째 매개변수인 withError를 통해 에러를 확인할 수 있어 에러가 발생했을 때 해당 메서드를 통해서 에러를 확인할수 있습니다.

### \***\*webView(\_:didFailProvisionalNavigation:withError:)\*\***

```swift
optional func webView(_ webView: WKWebView,
didFailProvisionalNavigation navigation: WKNavigation!,
            withError error: Error)
```

- 위의 didFail메서드와 같이 에러가 발생했을때 호출되는 메서드
- 웹페이지 로딩되었을 때 호출되는 것이 아니라 URL이 잘못되었거나 네트워크 오류가 발생해 웹페이지 자체를 아예 불러오지 못했을 때 호출되는 메서드입니다.
- 마찬가지로 error 매개변수를 통해 무슨 에러인지 확인 가능
-

# 2. WKUIDelegate

[https://developer.apple.com/documentation/webkit/wkuidelegate](https://developer.apple.com/documentation/webkit/wkuidelegate)

사용자의 유저 인터페이스를 보여주는 유저 인터페이스의 요소들을 보여주기 위한 메서드로 말 그대로 UIDelegate라고 생각을 하시면 될 거 같습니다.

1. webView(\_:createWebViewWith:for:windowFeatures:)새로운 웹뷰를 만들어주는 메서드
2. webViewDidClose(\_:)webView창이 성공적으로 닫혔음을 알려줍니다.
3. webView(\_:runJavaScriptAlertPanelWithMessage:initiatedBtFrame:completionHandler:)자바스크립트 알람 패널을 보여줍니다.
4. webView(\_:runOpenPanelWith:initiatedByFrame:completionHandler:)패널에 파일을 업로드하는 것을 보여줍니다.

### webView(\_:createWebViewWith:for:windowFeatures:)

```swift
optional func webView(_ webView: WKWebView,
    createWebViewWith configuration: WKWebViewConfiguration,
                  for navigationAction: WKNavigationAction,
       windowFeatures: WKWindowFeatures) -> WKWebView?
```

새로운 웹뷰를 만들어주는 메서드

**Parameters**

- webView
  - 델리게이트 메서드를 호출할 웹뷰
- configuration
  - 새로운 웹뷰를 만들 때 사용할 구성
- navigationAction
  - 새로운 웹뷰를 만들어서 호출할 때 야기할 행동
- windowFeatures
  - 웹페이지의 요구 특징

### webViewDidClose(\_:)webView

```swift
optional func webViewDidClose(_ webView: WKWebView)
```

창이 성공적으로 닫혔음을 앱에 알려주는 메서드

### webView(\_:runJavaScriptAlertPanelWithMessage:initiatedBtFrame:completionHandler:)

```swift
optional func webView(_ webView: WKWebView,
runJavaScriptAlertPanelWithMessage message: String,
     initiatedByFrame frame: WKFrameInfo,
    completionHandler: @escaping () -> Void)
```

자바스크립트의 알람 패널을 보여주는 메서드.

**Parameters**

- webView
  - 델리게이트 메서드를 호출할 웹뷰
- message
  - 보여줄 메시지
- frame
  - 자바스크립트 프로세스가 호출을 시작한 프레임에 대한 정보
- completionHandler
  - 알림 창 패널이 사라지고 난 후에 호출될 클로저 함수

### webView(\_:runOpenPanelWith:initiatedByFrame:completionHandler:)

```swift
optional func webView(_ webView: WKWebView,
     runOpenPanelWith parameters: WKOpenPanelParameters,
     initiatedByFrame frame: WKFrameInfo,
    completionHandler: @escaping ([URL]?) -> Void)
```

파일 업로드 패널을 보여주는 메서드입니다

**Parameters**

- webView
  - 델리게이트 메서드를 호출할 웹뷰
- parameters
  - 파일 업로드 control을 보여주는 파라미터
- frame
  - 파일 업로드 호출을 시작하면 불려지는 파라미터
- completionHandler
  - 열려있던 패널이 사라지고 불려지는 후행 클로저로 만약에 사용자가 OK를 선택하면 통과하게 됩니다.
