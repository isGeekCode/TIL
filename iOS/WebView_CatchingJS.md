# WebView - WKWebView에서 보내는 JS를 캐치하는 방법

웹에서 보내는 javascript를 캐치하려면 미리 등록을 해야한다.

이때 javascript를 보낼때 message에 javascript를 보내고 body값을 함께 NSDictionary (JSON) 형태로 보내주면 그걸 파싱해서 받을 수 있다.

```swift
// MARK: - WKScriptMessageHandler
extension MainViewController: WKScriptMessageHandler {

    /// message name: javascript 명
    /// 이렇게 사용하려면 javascript 명을 미리 등록을 해야한다.
    func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) {

        print("get message at main vc \(message.name)")

        if message.name == Configs.MessageName.AppWebPopupOpen {
            print("MAIN:: Sub Web View PopUp OPEN")

            if let dict = message.body as? NSDictionary {
                print("\(dict)")
                if let moveUrlStr = dict["url"] as? String, let moveUrl = URL(string: moveUrlStr) {
                    print("moveUrl:: \(moveUrl)")
```

# JS등록과정

MainVC에서 웹뷰를 init 하는 부분을 살펴보면

1. **config**라는 WKWebViewConfiguration를 새성하고
2. **contentController**라는 WKUserContentController를 생성해

3. **contentController** 여기에 LeakAvoider———— 뒤에 해당하는 javascript를 등록시켜준다.

→ LeakAvoider는 순환참조를 방지하기 위해 사용하는 오픈소스 이다.

1. 그리고 **config**.userContentController에 **contentController** 를 등록한다.

```swift
extension MainViewController {

    public func initWebView() {

        let config = WKWebViewConfiguration.init()
        let contentController = WKUserContentController()

        //js -> native
        ///leakAvoider를 사용하는 이유 약한 참조로 전환
        contentController.add(LeakAvoider(delegate: self), name: Configs.MessageName.AppWebPopupOpen)
        config.userContentController = contentController
```

조금만 더 자세히 정리필요
