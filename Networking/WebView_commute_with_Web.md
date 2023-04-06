# WebView - Safari로 웹뷰 디버깅하는 방법
웹에서 앱으로 스키마 보내기

## 웹뷰 디버깅

### 현재 웹뷰의 콘솔창 띄우기
사파리 - 개발자용 - 나의 기기 이름 - 현재 띄운 웹페이지 클릭

### 맥 사파리에서 개발자용 탭이 보이지않는 경우
 KOR : 사파리 - 설정 - 고급 에서 메뉴 막대에서 개발자용 메뉴보기 체크를 해야한다.
 ENG : Preferences - General - Show Develop menu in menu bar

### 개발자용 탭에 나의 기기에서 `기기에서 웹속성 활성화`라고 나오는 경우 

 KOR : 설정 - 사파리 - 고급 - 웹속성 스위치를 활성화한다.
 ENG : Setting - Safari - Advanced - Web Inspector (활성화)

## 콘솔창

관리자도구를 누르면 콘솔창이 보인다.

이 콘솔창에 특정 키를 넣어 입력할 수 있다



### 웹뷰 새로고침

- 좌측 상단의 새로고침 버튼
- 콘솔창 입력 → 강력 새로고침 : window.location.reload()

- 콘솔에서 네이티브로 message를 보내는 테스트도 가능
  - 아래 메시지를 입력하고 엔터를 치면, Xcode에서 메시지 수신 확인이 가능

```swift
window.webkit.messageHandlers.HandlerName.postMessage

window.webkit.messageHandlers.HandlerName.postMessage('test')

```

이 방법은 나중에 소개하도록 하겠습니다!

### 1. 콘솔에서 네이티브로 alert보내기

```swift
window.alert("GeekCode")
```

VC에서 `runJavaScriptAlertPanelWithMessage` 함수를 구현하지않으면 앱이 죽을 수 있다.

<img width="1239" alt="스크린샷 2022-11-18 오후 2 06 09" src="https://user-images.githubusercontent.com/76529148/202650402-56a1a2f4-831c-47e3-875e-a08c1c91716d.png">

![스크린샷 2022-11-18 오후 2 07 54](https://user-images.githubusercontent.com/76529148/202650272-63ee1126-c368-4a9b-b298-263814fcdf18.png)

### 2. 콘솔에서 웹뷰내 tag에 접근하기

google의 intput의 placeholder도 채워줄 수 있다.

`getElementsByTagName(name);` 함수는 특정 tag명을 가지고 있는 dom 요소에 접근하는 메서드이다.

```swift
document.getElementsByTagName('input')[0].placeholder = "GeekCode"
```

<img width="999" alt="스크린샷 2022-11-18 오후 1 34 02" src="https://user-images.githubusercontent.com/76529148/202650137-37728146-b87e-47ab-8c8a-864058ca3690.png">

### 디버그창에서 스키마 보내기

세팅되어있는 스키마를 디버그창에서 보내면서 테스트를 할 수가 있다.

```swift
location.href=”<내용>”
```

아래처럼 세팅되어있다면 바코드스캔을 실행하기위해 url에 “barcodeScan”을 입력해 보내면 실행된다.

```swift
func webView(_ webView: WKWebView, decidePolicyFor navigationAction: WKNavigationAction, decisionHandler: @escaping (WKNavigationActionPolicy) -> Void) {

			guard let currWholeUrl = navigationAction.request.url else { decisionHandler(.cancel)
			            return
			        }

			let url = currWholeUrl.absoluteString
			        if url.contains("barcodeScan") {
			            // 바코드 스캔 로직
			            let msg = "barcodeScan Signal is Cached"
			            let alertController = UIAlertController(title: "", message: msg, preferredStyle: .alert)
			            let cancelAct = UIAlertAction(title: "cancel", style: .cancel) { UIAlertAction in
			                print("cancel")
			            }
			            let confirmAct = UIAlertAction(title: "confirm", style: .default) { UIAlertAction in
			                print("okay")
			            }
			            [ cancelAct,confirmAct ].forEach { alertController.addAction($0) }
			            present(alertController, animated: true, completion: nil)
			        }
}
```

<img width="854" alt="스크린샷 2022-11-18 오후 3 02 19" src="https://user-images.githubusercontent.com/76529148/202649971-44be4b1f-9ae7-4a38-bbcc-e7a8c5c1ec1b.png">

## 웹에서 앱으로 얼럿 띄우기

- UIDelegate를 이용하는 방법
- 브릿지를 이용해 WKScriptMessageHandler 이용하는 방법

### **Alert수신**

위에 테스트코드로 작성한것처럼 특정 스키마가 들어올때, 얼럿을 구현할 수있지만.

직접적으로 웹에서 띄울수 있는 Alert은 alert, confirm, prompt 3가지가 있다.

WkWebView에 UIDelegate를 위임시켜주고 아래 함수들을 세팅한다.

- runJavaScriptAlertPanelWithMessage
- runJavaScriptConfirmPanelWithMessage
- runJavaScriptTextInputPanelWithPrompt

```swift
extension ViewController: WKUIDelegate{

    func webView(_ webView: WKWebView, runJavaScriptAlertPanelWithMessage message: String, initiatedByFrame frame: WKFrameInfo, completionHandler: @escaping () -> Void) {
        let alert = UIAlertController(title: "", message: message, preferredStyle: .alert)
        let okAction = UIAlertAction(title: "확인", style: .default) { (action) in
            completionHandler()
        }
        alert.addAction(okAction)
        self.present(alert, animated: true, completion: nil)
    }

    func webView(_ webView: WKWebView, runJavaScriptConfirmPanelWithMessage message: String, initiatedByFrame frame: WKFrameInfo, completionHandler: @escaping (Bool) -> Void) {
        let alert = UIAlertController(title: "", message: message, preferredStyle: .alert)
        let okAction = UIAlertAction(title: "확인", style: .default) { (action) in
            completionHandler(true)
        }
        let cancelAction = UIAlertAction(title: "취소", style: .default) { (action) in
            completionHandler(false)
        }
        alert.addAction(okAction)
        alert.addAction(cancelAction)
        self.present(alert, animated: true, completion: nil)
    }

    func webView(_ webView: WKWebView, runJavaScriptTextInputPanelWithPrompt prompt: String, defaultText: String?, initiatedByFrame frame: WKFrameInfo, completionHandler: @escaping (String?) -> Void) {
        let alert = UIAlertController(title: "", message: prompt, preferredStyle: .alert)
        let okAction = UIAlertAction(title: "확인", style: .default) { (action) in
            if let text = alert.textFields?.first?.text {
                completionHandler(text)
            } else {
                completionHandler(defaultText)
            }
        }
        alert.addAction(okAction)
        self.present(alert, animated: true, completion: nil)
    }

}
```

구현을 위해서는 AlertController로 넘어온 Message와 Completion을 이용해 구현하면 된다.

참고:

- [https://jingyu.tistory.com/2](https://jingyu.tistory.com/2)
- 브릿지 이용하기: [https://swieeft.github.io/2020/07/29/WKWebViewBridge.html](https://swieeft.github.io/2020/07/29/WKWebViewBridge.html)
- [https://github.com/sujinnaljin/TIL/blob/master/Swift/웹뷰와 자바스크립트 연동 (Native <-> JavaScript 통신 방법).md](<https://github.com/sujinnaljin/TIL/blob/master/Swift/%EC%9B%B9%EB%B7%B0%EC%99%80%20%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8%20%EC%97%B0%EB%8F%99%20(Native%20%3C-%3E%20JavaScript%20%ED%86%B5%EC%8B%A0%20%EB%B0%A9%EB%B2%95).md>)
