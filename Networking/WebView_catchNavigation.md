# WebView - 네비게이션컨트롤러 목록으로 웹뷰 관리하는 방법


네비게이션 컨트롤러는 기본적으로 viewControllers 라는 배열을 가지고 있다.

이 배열은 화면을 순서대로 넣어두고 사용한다.
최상단 화면은 배열의 마지막에 위치하고 이를 이용하여 화면 전환을 관리할 수 있다.
관련된 내용은
[[TIL : 네비게이션 컨트롤러로 화면관리하기]]()에서 확인하자.


동일한 방법인데 가끔 스키마를 아래처럼 JSON의 형태로 주는 경우가 있다.
## JSON 의 형태로 들어오는 경우
```
 location.href='myApp://?{"cmd":"refresh", "topYn":"Y", "popCount":"1"}'
 location.href='myApp://?{"cmd":"refresh", "topYn":"Y"}'
 location.href='myApp://?{"cmd":"refresh"}'
 location.href='myApp://?{"cmd":"refresh", "popCount":"1"}'
```


```swift

class ViewController {
    func webView(_ webView: WKWebView, decidePolicyFor navigationAction: WKNavigationAction, decisionHandler: @escaping (WKNavigationActionPolicy) -> Void) {

            let map = url.jsonDictionary

            switch url.scheme! {
            case "myApp":
                case "refresh":
                    let isTopRefresh = (map["topYn"] as? String)?.lowercased() == "y"
                    let popCountString = map["popCount"] as? String
                    let popCount = Int(popCountString ?? "0") ?? 0
                    self.refreshOtherWebviews(isTopRefresh: isTopRefresh, popCount: popCount)

                    decisionHandler(WKNavigationActionPolicy.cancel)
                    return
            default:
                    decisionHandler(WKNavigationActionPolicy.allow)
                    return
            }
    }
}

// JSON형태로 들어오는 스키마를 가져오는 함수
extension URL {
    var jsonDictionary: [String: AnyObject] {
        var jsonDictionary = [String: AnyObject]()
        
        if let components: [String] = self.absoluteString.removingPercentEncoding?.components(separatedBy: "://?"), components.count >= 2 {
            guard let data: Data = (components[1] as String).data(using: String.Encoding.utf8) else { return jsonDictionary }
            
            do {
                if let json = try JSONSerialization.jsonObject(with: data, options: .allowFragments) as AnyObject! {
                    jsonDictionary = json as! [String : AnyObject]
                }
            } catch let err as NSError {
                jsonDictionary = ["error": err.localizedDescription as NSString]
            }
        }
        
        return jsonDictionary
    }
}

extension ViewController {

    func webviewRefresh() {
        print("Refreshing web view... ")
        self.webView?.reload()
    }
    
    /// 네비게이션 컨트롤러에서 자신을 제외한 모든 SubVC의 웹뷰를 리프레시 처리
    func refreshOtherWebviews(isTopRefresh : Bool, popCount: Int = 0) {
        print("refreshWebView :::: isTopViewRefresh::\(isTopRefresh)")
        print("refreshWebView :::: popCount::\(popCount)")

        if isTopRefresh { webviewRefresh() }
        self.navigationController?.viewControllers
            .filter { $0 is JwWebViewController && $0 != self }
            .forEach { ($0 as! JwWebViewController).webviewRefresh() }

        if popCount != 0 {
            if let navigationController = self.navigationController {
                let controllers = navigationController.viewControllers
                if controllers.count > popCount {
                    let targetController = controllers[controllers.count - (popCount + 1)]
                    navigationController.popToViewController(targetController, animated: true)
                }
            }
        }
    }
}
```


## 쿼리의 형태로 들어오는 경우

```
 location.href='myApp://refresh?'
 location.href='myApp://refresh?topYn=y'
 location.href='myApp://refresh?topYn=y&popCount=1'
 location.href='myApp://refresh?popCount=1'

```


```swift

class ViewController {
    func webView(_ webView: WKWebView, decidePolicyFor navigationAction: WKNavigationAction, decisionHandler: @escaping (WKNavigationActionPolicy) -> Void) {
    
        let currQuery = navigationAction.request.url?.query ?? ""

        if url.contains("myApp") {
            if urlHost == "refresh" {
                let currQuery = url.query ?? ""

                let isTopRefresh: Bool
                if let topYn = currQuery.lowercased().components(separatedBy: "topyn=").last {
                    isTopRefresh = topYn == "y"
                } else {
                    isTopRefresh = false
                }

                let popCount: Int
                if let popCountString = currQuery.lowercased().components(separatedBy: "popcount=").last {
                    popCount = Int(popCountString) ?? 0
                } else {
                    popCount = 0
                }
                
                self.refreshOtherWebviews(isTopRefresh: isTopRefresh, popCount: popCount)
                
                decisionHandler(WKNavigationActionPolicy.cancel)
                return
            }
        } else {
            decisionHandler(WKNavigationActionPolicy.allow)
            return
        }
    }
    
    
    func reloadWebView() {
        mainWebView.reload()
    }

    /// 네비게이션 컨트롤러에서 자신을 제외한 모든 SubVC의 웹뷰를 리프레시 처리, 이후 종료처리
    func refreshOtherWebviews(isTopRefresh : Bool, popCount: Int = 0) {
        print("refreshWebView :::: isTopViewRefresh::\(isTopRefresh)")
        print("refreshWebView :::: popCount::\(popCount)")

        if isTopRefresh { reloadWebView() }
        self.navigationController?.viewControllers
            .filter { $0 is JwWebViewController && $0 != self }
            .forEach { ($0 as! JwWebViewController).reloadWebView() }

        if popCount != 0 {
            if let navigationController = self.navigationController {
                let controllers = navigationController.viewControllers
                if controllers.count > popCount {
                    let targetController = controllers[controllers.count - (popCount + 1)]
                    navigationController.popToViewController(targetController, animated: true)
                }
            }
        }
}

```
