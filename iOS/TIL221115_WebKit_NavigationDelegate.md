WKWebView에서 탐색 요청을 수락,로드 및 완료하는 과정에서 트리거되는 메서드들

```swift
import Foundation
import WebKit

// MARK: - NavigationDelegate

/// WKWebView에서 탐색 요청을 수락,로드 및 완료하는 과정에서 트리거되는 메서드들
extension MainViewController: WKNavigationDelegate {

    // MARK: - 1. navigation request를 허용 / 거절하기
    /// 지정된 action정보를 기반으로,  새 콘텐츠로 이동할 수 있는 권한을 요청하는 메서드.
    /// navigation request를 허용하거나 거부할 수 있다.
    /// - decisionHandler( .allow / .cancel / .download )
    func webView(_ webView: WKWebView, decidePolicyFor navigationAction: WKNavigationAction, decisionHandler: @escaping (WKNavigationActionPolicy) -> Void) {

        decisionHandler(.allow)
    }

    /**
     /// 지정된 환경설정(preferences) 및 action정보를 기반으로,  새 콘텐츠로 이동할 수 있는 권한을 요청하는 메서드.
     func webView(_ webView: WKWebView, decidePolicyFor navigationAction: WKNavigationAction, preferences: WKWebpagePreferences, decisionHandler: @escaping (WKNavigationActionPolicy, WKWebpagePreferences) -> Void) {
     }
    */


    /// 서버에서 navigation request에 대한 응답을 받고나서 새 콘텐츠로 이동할 수 있는 권한을 요청하는 메서드
    func webView(_ webView: WKWebView, decidePolicyFor navigationResponse: WKNavigationResponse, decisionHandler: @escaping (WKNavigationResponsePolicy) -> Void) {

    }

    // MARK: - 2. request의 로딩 진행률 추적하기
    /// 메인프레임에서 navigation이 시작됐음을 알린다.
    /// navigation request를 처리하기 위한 임시 허가(provisional)를 받은 후 , 해당 요청에 대한 응답을 받기전에 호출되는 메서드.
    func webView(_ webView: WKWebView, didStartProvisionalNavigation navigation: WKNavigation!) {
        print("MAIN_VC webview didStartProvisionalNavigation        \(String(describing: webView.url))")

    }


    /// 웹뷰가 request에 대한 서버 redirection을 수신했을을 알리는 메서드.
    func webView(_ webView: WKWebView, didReceiveServerRedirectForProvisionalNavigation navigation: WKNavigation!) {

    }


    /// 웹뷰가 메인 프레임에 대한 콘텐츠를 받기 시작할 때 호출되는 메서드
    /// 콘텐츠를 받기 시작할때 처리해줄 것이 있을 때 사용
    func webView(_ webView: WKWebView, didCommit navigation: WKNavigation!) {
        print("MAIN_VC webview didCommit \(String(describing: webView.url))")
    }


    /// - 웹뷰가 콘텐츠 받기(navigation)를 완료했을 때 호출되는 메서드
    /// - 웹페이지가 웹뷰에 완전히 보여주고 나면 호출
    /// - 완료후에 로딩뷰를 히든처리하는 곳
    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        print("MAIN_VC didfinish \(String(describing: webView.url))")
    }


    /// - 웹뷰가 콘텐츠 받기를 실패했을 때 호출되는 메서드
    /// - error 매개변수를 통해 에러 내용을 확인 가능
    func webView(_ webView: WKWebView, didFail navigation: WKNavigation!, withError error: Error) {

        print("MAIN_VC didFail is \(error)")
    }


    /// navigation중에 오류가 발생했을 을 알리는 메서드. didCommit이후에 발생하는 에러에 대해 호출한다.
    func webView(_ webView: WKWebView, didFailProvisionalNavigation navigation: WKNavigation!, withError error: Error) {

    }


    /// 웹뷰의 content프로세스가 종료되었음을 알리는 메서드
    func webViewWebContentProcessDidTerminate(_ webView: WKWebView) {

    }

    // MARK: - 5. 다운로드 진행률 처리하기
    /// navigation action이 다운로드 되었음을 알리는 메서드
    /// 다운로드 진행률 추적을 시작할 때 구현한다.
    @available(iOS 14.5, *)
    func webView(_ webView: WKWebView, navigationAction: WKNavigationAction, didBecome download: WKDownload) {

    }

    /// navigation response가 다운로드 되었음을 알리는 메서드
    @available(iOS 14.5, *)
    func webView(_ webView: WKWebView, navigationResponse: WKNavigationResponse, didBecome download: WKDownload) {

    }
}
```

1. `func webView(WKWebView, decidePolicyFor: WKNavigationAction, preferences: WKWebpagePreferences, decisionHandler: (WKNavigationActionPolicy, WKWebpagePreferences) -> Void)`

👉🏻 처음에 Action 으로 요청할때 해당 **navigation request 를 허용하거나 거부**

2. `func webView(WKWebView, didStartProvisionalNavigation: WKNavigation!)`

👉🏻 1번에서 `decisionHandler(.allow)` 로 허가 났으면 **navigation 시작**

3. `func webView(WKWebView, decidePolicyFor: WKNavigationResponse, decisionHandler: (WKNavigationResponsePolicy) -> Void)`

👉🏻 navigation request 에 대한 **응답을 받고 난 후, 이어서 새 콘텐츠로 이동을 허용하거나 거부**

4. `func webView(WKWebView, didCommit: WKNavigation!)`

👉🏻 3번에서 `decisionHandler(.allow)` 로 허가 났으면 **메인 프레임 내용 수신 시작**

5. `func webView(WKWebView, didFinish: WKNavigation!)`

👉🏻 **navigation 완료**
