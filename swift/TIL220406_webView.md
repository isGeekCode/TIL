App에서 웹페이지를 여는 방법

### 1. 앱에서 사파리앱을 실행

```swift
guard let url = URL(string: "http://zeddios.tistory.com"), UIApplication.shared.canOpenURL(url) else { return }

 UIApplication.shared.open(url, options: [:], completionHandler: nil)

```

### 2. WKWebView사용

```swift
import WebKit

guard let url = URL(string:"https://zeddios.tistory.com") else {return}

let request = URLRequest(url: url)

webView?.load(request)

```

WKWebView는 앱 안에서 보여주죠? 스레드는 앱과 별도로 돌아가긴 하지만요 :)

그리고 WKWebView는 info.plist에

```swift
1.
<key>NSAppTransportSecurity</key>
    <dict>
        <key>NSAllowsArbitraryLoads</key>
        <true/>
    </dict>
```

### 3. SFSafafriViewController로 열어줌

- **친숙한 Safari 인터페이스** : Safari처럼 맨위에는 웹 주소 텍스트 필드가 있으며, 아래에는 뒤로가기 / 앞으로가기 버튼과 공유버튼이 있습니다. Safari 아이콘을 누르면 Safari앱으로 현재 웹사이트가 열립니다.

(참고 : 웹주소 텍스트 필드는 편집 할 수 없다고 해요 :) 사용자는 링크를 누르거나 탐색버튼을 사용하여 탐색할 수는 있지만 **수동으로 URL을 입력할 수 는 없습니다.**)

```swift
import SafariServices

@IBAction func oepnSFSafariViewControllerAction(_ sender: Any) {

    guard let url = URL(string: "https://zeddios.tistory.com") else { return }

    let safariViewController = SFSafariViewController(url: url)

    present(safariViewController, animated: true, completion: nil)

 }
```
