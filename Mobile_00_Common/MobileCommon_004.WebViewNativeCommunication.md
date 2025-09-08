# WebView ↔ Native 통신 공통

## 1. 개요

순수 웹사이트와 달리, 애플리케이션이 모바일 앱으로 배포되는 경우 웹사이트는 앱 내부의 사용자 클릭이나 제스처 이벤트를 직접 포착할 수 없다. 따라서 앱 자체가 이러한 네이티브 사용자 상호작용 이벤트를 포착하여 웹 레이어로 전달해야 한다.

하이브리드 환경에서는 결국 웹과 앱이 서로의 기능을 호출해야 하며, 통신 방식은 크게 **단방향(Web→App)** 과 **양방향(Web↔App)** 으로 나눌 수 있다.

- 단방향
    - (웹 → 앱): URL Intercept
- 양방향 
    - (웹 → 앱): JS Bridge
    - (앱 → 웹): evaluateJavaScript

<br>

## 2. 왜 사용하는가
- **네이티브 기능 접근**: 카메라, 연락처, 위치, 파일, 클립보드 등
- **일관된 UX**: 웹·앱 어디서든 동일한 액션을 제공
- **측정/로그 수집**: 행동 이벤트를 공통 포맷으로 수집
- **오프라인/에러 복원력**: 재시도·타임아웃·큐잉으로 신뢰성 확보

대표 유입/호출 경로
- 웹 UI 버튼 → 앱 기능 호출(Web→App)
- 앱 로직 결과 → 웹 화면 갱신(App→Web)
- 인앱 브라우저/외부 브라우저에서 동작 차이 흡수

<br>


## 3.1 단방향 통신 (웹 → 앱)
**URL Intercept** 방식. 

웹뷰에서 URL을 호출하면, 앱은 이를 관측하고 있다가 해당 요청을 웹뷰에서 로드할지 여부를 사전에 결정할 수 있다.

호출하는 URL의 형태는 커스텀 스키마든 HTTPS 링크든 상관없이 분기 처리가 가능하다. 

해당 요청인 경우,  **웹뷰 로딩을 취소**하고, 네이티브 로직으로 우회하는 방법이다.


- 장점
    - 오래 전부터 사용하던 방식이기때문에 범용적이다.
    - JS를 사용하는 방식과 달리 한 군데에 추가하는 것으로 확장이 간편하다. 
- 단점
    - 콜백이나 실패 처리 없이 결과 확인이 불가능
    - 연속 호출 시 일부 요청이 무시될 수 있다. 
    - 보장을 원한다면 JSBridge 방식을 권장.

**주요 활용 사례**
- 카메라·바코드 스캐너 같은 네이티브 기능 호출
- 별도 서브 WebView를 띄워 특정 플로우를 분리 처리
- 결제 PG사 페이지 이동 (예: 이니시스, 페이코 등)


### 흐름 요약 (단방향)
1) 웹 → 앱 호출

```
// 현재 탭에서 이동
window.location.href = "barcode://scan?mode=qr";
```


2-1) 웹 → 앱 응답 : iOS

```swift
func webView(_ webView: WKWebView, decidePolicyFor nav: WKNavigationAction,
             decisionHandler: @escaping (WKNavigationActionPolicy) -> Void) {
    guard let url = nav.request.url else { return decisionHandler(.allow) }
    
    // 1) 커스텀 스키마 (예: 바코드 스캐너 호출)
    if url.scheme == "barcode" {
        NativeFeatures.shared.handleScanner(url: url)     
        decisionHandler(.cancel) 
        return
    }
    
    // 2) 특정 결제 도메인(이니시스 예시)
    if url.host?.contains("inicis.com"){
        // 결제 전용 서브 WebView를 띄우거나 네이티브 모듈 호출
        PaymentHandler.shared.handleInicis(url: url)
        decisionHandler(.cancel)
        return
    }
    
    decisionHandler(.allow)
}
```

2-1) 웹 → 앱 응답 : Android
```kotlin
override fun shouldOverrideUrlLoading(view: WebView, request: WebResourceRequest): Boolean {
    val url = request.url

    if (url.scheme == "barcode") {
        NativeFeatures.handleScanner(url)
        return true  
    }

    if (url.host?.contains("inicis.com") == true) {
        PaymentHandler.handleInicis(url)
        return true  
    }

    return false // 기본적으로 웹뷰에서 로드
}
```

<br><br>

## 3.2 양방향 통신 (웹 ↔ 앱)
**JavaScript**를 기반으로 양방향 통신 및 콜백을 모두 지원한다.
- **웹 → 앱**: 네이티브에 구현한 JavaScript 브릿지를 통해 수신
  - iOS: `WKScriptMessageHandler` 를 통해 수신
  - Android: `addJavascriptInterface`로 등록한 Java/Kotlin 메서드에서 수신  
- **앱 → 웹**: `evaluateJavaScript` 로 웹에 정의된 JS 함수 호출



- iOS 호출 예시:
```js
window.webkit?.messageHandlers?.barcode?.postMessage({ id: "req-1", action: "scan", payload: { mode: "qr" } });
```
- Android 호출 예시:
```js
window.AndroidBridge.barcode(JSON.stringify({...}))
```



### 흐름 요약 : 앱 → 웹  
- 네이티브에서 웹뷰 내 JavaScript 함수를 호출하여 웹에 결과나 이벤트를 전달한다.  
  - iOS 예시:
    ```swift
    webView.evaluateJavaScript("showText('Hello from iOS')", completionHandler: nil)
    ```
  - Android 예시:
    ```kotlin
    webView.evaluateJavascript("showText('Hello from Android')", null)
    ```


## HISTORY
- 250908: 구조 개편(단방향/양방향), 공통 설계·체크리스트 추가. OS별 상세는 별도 문서로 분리 예정.
