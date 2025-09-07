# 딥링크 

## 개요  
딥링크(Deep Link)는 사용자가 앱 내 특정 화면이나 기능으로 직접 이동할 수 있도록 하는 상위 개념이다. 

기술적으로는 커스텀 스킴, 유니버설 링크, 앱 링크, 지연된(Deferred) 딥링크 등 다양한 구현 방법을 포함한다. 또한, Firebase Dynamic Link, AppsFlyer OneLink와 같은 외부 딥링크 솔루션도 존재하여, 보다 복잡한 트래킹과 사용자 유입 경로 관리가 가능하다.


<br>

구현 관점에서는 크게 두 방식으로 구분한다.

<br>

- **URI Scheme 기반** : `myapp://path?...` 형태의 앱 고유 스킴을 사용한다.
- **도메인 기반(서버 경유)** : `https://...` 형태의 링크를 사용하며 유니버설 링크(iOS), 앱 링크(Android), MMP 트래킹 링크(원링크/다이나믹 링크 등)를 포괄한다.

<br>

딥링크는 단순히 앱을 여는 것을 넘어, 특정 화면으로 이동하거나 앱 내 특정 동작까지 수행하게 할 수 있다. 이를 통해 사용자 경험을 개선하고, 앱 내 원하는 위치로 곧바로 연결하는 역할을 한다.


- Step 1. 사용자에게 링크 전달
- Step 2. 링크 전달
- Step 3. 전하고자 했던 링크로 사용자 유입


사용자나 기획자 입장에서는 딥링크가 모두 동일하게 보인다. 링크를 클릭하면 앱이 열리고 원하는 화면으로 이동한다고 이해한다. 그러나 개발자는 어떤 구현 방식을 사용할지 구체적으로 확인해야 한다. 이러한 차이를 이해하고 요구사항을 명확히 하는 것이 중요하다.


## 딥링크의 활용

딥링크는 다음과 같은 목적에 사용한다.
- **첫 진입 비용 축소**: 앱 실행 후 곧바로 목표 화면/상태로 이동해 전환율을 높인다.
- **맥락 보존**: 광고/공유/알림의 의도를 앱 내 동작으로 그대로 이어간다.
- **측정과 개인화**: 유입 채널/캠페인 파라미터를 전달해 측정하고, 사용자 맞춤 동작을 수행한다.

<br><br>

### 공통 유입/호출 경로
외부 → 앱으로 들어오는 대표 경로는 다음과 같다.
- **웹/메시징/광고의 링크 탭**: 브라우저·인앱 브라우저·SNS·메신저 등에서 링크를 탭한다. (URI 스킴 또는 도메인 기반 딥링크)
- **QR 코드**: 오프라인에서 QR → 링크 → 앱 진입.
- **이메일/SMS**: 캠페인 링크를 통해 진입.
- **앱 설치 전/후 시나리오**: 미설치 시 스토어 Fallback, 설치 후 첫 실행에서 딥링크 복원(Deferred Deep Link).

<br><br>

### 그 외
딥링크 외에도 앱을 특정 화면으로 여는 수단이 있다. 이 문서에서는 개념만 언급하고, 상세 구현은 별도 문서에서 다룬다.
- **푸시 알림 딥링크**: 알림 탭 시 특정 목적지로 열도록 payload에 경로/파라미터를 담는다. *(별도 문서 예정)*
- **하이브리드 Web↔Native 통신**: WebView 내부에서 JavaScript → 네이티브 호출(`WKScriptMessageHandler`), 또는 네이티브 → JavaScript 실행. *(별도 문서 예정)*

<br><br>

아래에 URI Scheme 방식과 도메인 기반(유니버설/앱 링크) 방식을 각각 설명한다.

## URI Scheme 방식
URI Scheme은 초기에 사용된 딥링크 구현방식이다.   

앱 고유의 URI Scheme을 정의하여, 해당 스킴이 포함된 링크를 클릭했을 때 앱이 실행되도록 한다.

아래와 같이 별다른 제약없이 개발자가 직접 원하는 스킴을 정해서 만들 수 있다.

```
someName://home
someName://home?user=123

someApp://search/DgQzwlKP
someApp://open?file=abc

kakaotalk://me
```

URI Scheme의 패턴을 구현할 때는 웹에서 사용하는 URL 규칙과 동일한 방식으로 구성하는 경우가 많다.

기본 패턴은 `{scheme}://{path}?param=value` 형태이며, 스킴은 앱을 식별하는 고유 이름이고, path와 파라미터로 앱 내 특정 기능이나 데이터를 지정한다.

예시:
```
sampleApp://user/profile?uid=5678
sampleApp://search?query=shoes&page=2
```

이처럼 URI Scheme을 일관된 URL 패턴으로 설계하면, 각 플랫폼의 기본 파서/엔트리 포인트를 그대로 활용할 수 있다.

- iOS: `URLComponents`로 파싱, `application(_:open:options:)` 또는 `SceneDelegate.scene(_:openURLContexts:)`에서 진입 처리  
- Android: `Uri.parse()`로 파싱, `intent-filter` 매칭 후 `Intent.getData()`로 진입 처리

자세한 구현 내용은 하단 참고

### URI Scheme의 한계

1. 앱이 설치되어 있어야만 동작

2. 아무나 원하는 scheme을 만들 수 있어서, 동일한 scheme을 가진 앱과의 혼선이 생길 수 있다.   

    2-1. 동일한 scheme이 있다면
    - 안드로이드 : 어떤 앱으로 열지 선택창 발생
    - iOS : 가장 최근 설치한 앱이 열림
    
3. 보안 측면에서 외부에서 악의적으로 스킴을 호출할 위험이 존재한다.  
   카카오톡에서 사용하는 kakaotalk://xxx 와 동일한 URI Scheme을 만들어서 내 앱이 실행되도록 어뷰징




## 중간 서버(도메인) 경유 방식

위에서 말한 문제점을 보완하기 위해 생긴 방법이다.

각 OS는 이를 아래와 같은 방식으로 제공한다. 

- iOS : 유니버셜링크 
- Android : 앱링크


이 링크들은 항상 웹사이트 형태의 딥링크 URL로 만들어진다.  

```
https://example.com/chat
https://link.sampleapp.com/products/123
https://myapp.com/events?id=456
```
  
고유한 웹사이트 주소(도메인)로 만들어 지기 때문에 유일하다.  
다만, 이 도메인이 이 앱의 소유자라는 것을 인증해야 원활히 동작하게 된다. 

### 소유자 인증
해당 주소의 도메인 소유자 확인을 위해서는
Android, iOS에서 각각 인증하는 과정을 거쳐야 한다.

해당 도메인에 앱의 고유 id(패키지)정보가 포함되어 있는 파일을 업로드하도록 하고 해당 파일을 확인해서 인증처리하는 방식으로 진행된다.


### 실행동작
- **앱 설치 O**: 해당 딥링크 목적 화면 실행  
- **앱 설치 X**  
  - 웹서비스 존재: 해당 웹 페이지로 랜딩  
  - 웹서비스 없음: OS별 스토어로 이동처리(Play Store/App Store)

### 문제점

앱링크(App Link)와 유니버설 링크(Universal Link)는 URI Scheme의 한계를 보완했지만, 이 방식에도 여러 문제가 존재한다.

1. 브라우저 주소 입력창에 딥링크를 직접 복사/입력하는 경우 동작하지 않는다.  
2. OS 기본 브라우저(Safari, Chrome 등)에서는 의도대로 동작하더라도, 자체 브라우저를 사용하는 앱(카카오톡, 페이스북, 인스타그램 등)에서는 정상 동작하지 않는 경우가 있다.  
3. 앱 마케팅을 위한 활용 시, URI Scheme / Universal Link / App Link를 앱 및 브라우저 별로 다르게 설정해야 한다는 번거로움이 있다.  
   - Safari(iOS)에서는 Universal Link가 잘 동작하지만, URI Scheme은 제한적이다.  
   - Chrome(Android)에서는 App Link가 안정적으로 동작하나, 일부 서드파티 브라우저에서는 URI Scheme만 동작하기도 한다.  
4. Universal Link의 제약
   - 주소창에 링크를 직접 붙여넣기 하면 동작하지 않는다.  
   - JavaScript로 트리거할 경우 리다이렉트되지 않는다.  
   - 앱 내에서 `openURL`과 같이 프로그래밍 방식으로 열 경우 동작하지 않는다.  
5. URI Scheme은 앱이 설치되지 않은 경우 Fallback 처리가 불가능하여, 아무런 동작도 일어나지 않는다.  

이처럼 앱/브라우저/플랫폼별로 지원 여부가 다르기 때문에, 상황에 따라 다른 형태의 딥링크를 적용해야 하는 번거로움이 발생한다.

이때, 이 단점을 보완하는 방법이 MMP를 활용하는 방법이다.  

## MMP의 활용

앱 마케팅에서 딥링크를 문제없이 사용하기 위해서는 단순히 기술을 도입하는 것을 넘어, 환경별 차이와 사용자 흐름까지 고려해야 한다. 이를 위해 MMP의 도움을 받는 경우가 많다.

### MMP란?
MMP는 Mobile Measurement Partner의 약자로, 모바일 마케팅 성과를 측정하고 최적화할 수 있도록 지원하는 외부 플랫폼이다.  
- 광고 클릭부터 앱 설치, 앱 내 행동(구매, 회원가입 등)까지 전체 전환 과정을 추적한다.  
- 딥링크 기능을 지원해 캠페인별 트래킹 링크를 만들고, Fallback과 Deferred Deep Link까지 관리할 수 있다.  
- 대표적인 MMP 서비스로는 **AppsFlyer, Adjust, Branch, Airbridge** 등이 있다.  


### 지연된 딥링크 (Deferred Deep Link)
유니버설/앱 링크 기반으로 설치 전후를 이어주는 패턴이다.  
MMP를 사용하는 이유 중 하나가 이 기능을 사용하기 위해서가 아닐까 한다. 

그러면 사용자는 마케팅에 활용된 링크를 눌렀을때, 앱설치를 해야하더라도 앱설치를 완료하고나면 의도했던 링크로 이동까지 할수가 있다. 


## 딥링크를 문제없이 사용하기 위한 조건

- **앱 내부 라우팅 일관성**  
  어떤 방식의 딥링크(URI Scheme, Universal Link, App Link)로 진입하더라도  
  앱 내부 라우터가 동일하게 URL → 화면으로 매핑되도록 설계해야 한다.  
  👉 앱의 책임: 모든 진입 루트를 올바르게 처리할 수 있도록 라우팅 구현.

- **MMP 기반 트래킹 링크 제공**  
  MMP는 사용자의 환경(OS, 브라우저, 인앱 여부, 설치 여부 등)을 감지하여  
  상황에 맞는 딥링크 형태(Universal/App Link, URI Scheme, Fallback 등)를 제공해야 한다.  
  👉 MMP의 책임: 유입 경로를 분석해 **현재 상황에서 동작 가능한 링크**를 제공.


### 실무 플로우

1. 사용자가 **MMP 트래킹 링크 클릭**  
2. MMP가 **환경 감지** (OS / 브라우저 / 인앱 여부 / 설치 여부 추정)  
3. 분기 처리  
   - 지원 O → **Universal/App Link** 직접 진입  
   - 지원 불확실/불가 → **랜딩 페이지 표출**  
     - “앱으로 열기” 버튼 → **URI 스킴 시도**  
     - 실패 시 → **스토어 Fallback**  
4. 설치 완료 후 첫 실행 → **Deferred Deep Link**로 원래 목적지 복원 


# iOS 구현

## iOS - URI Scheme 방식

### A. 커스텀 스킴 등록 및 처리
1) **URL Types 등록**  
   - Xcode → TARGETS → *Info* → *URL Types* 추가  
   - *Identifier*: `com.example.myapp.scheme`  
   - *URL Schemes*: `myapp`  

identifier 에는 패키지명을 넣어주고, URL Schemes부분에는 원하는 스키마명을 입력한다. 


2) **진입 처리(AppDelegate/SceneDelegate)**  
```swift
// AppDelegate.swift (iOS 13 미만 또는 SceneDelegate를 사용하지않는 경우)
func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    handleDeepLink(url)
    return true
}

// SceneDelegate.swift (iOS 13+)
func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
    guard let url = URLContexts.first?.url else { return }
    handleDeepLink(url)
}


private func handleDeepLink(_ url: URL) {
    // 공통 파싱/로깅
    guard let comps = URLComponents(url: url, resolvingAgainstBaseURL: false) else { return }
    print("[DeepLink] raw:", url.absoluteString)
    print("[DeepLink] scheme:", comps.scheme ?? "-")
    print("[DeepLink] host:", comps.host ?? "-")
    print("[DeepLink] path:", comps.path)
    print("[DeepLink] queryItems:", comps.queryItems as Any)
}


/**

[DeepLink] raw: myapp://user?profile?uid=1&page=3
[DeepLink] scheme: myapp
[DeepLink] host: user
[DeepLink] path: 
[DeepLink] queryItems: Optional([profile?uid=1, page=3])
profile?uid : 1
page : 3

*/


```


---

#### B. 유니버설 링크 설정 및 처리
1) **Associated Domains 활성화**  
   - Xcode → TARGETS → *Signing &amp; Capabilities* → +Capability → **Associated Domains**  
   - 도메인 추가: `applinks:myapp.com`, `applinks:link.myapp.com` 등

2) **AASA(Apple App Site Association) 파일 제공**  
   - 경로: `https://myapp.com/.well-known/apple-app-site-association`  
   - Content-Type: `application/json` (확장자 `.json` 없음)  
   - 최소 예시:
```json
{
  "applinks": {
    "apps": [],
    "details": [
      {
        "appID": "TEAMID.com.example.myapp",
        "paths": ["*", "/products/*", "/events/*"]
      }
    ]
  }
}
```

3) **UserActivity 진입 처리**  
```swift
// AppDelegate (iOS 12 이하) 또는 SceneDelegate (iOS 13+)
func application(_ application: UIApplication, continue userActivity: NSUserActivity,
                 restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
    guard userActivity.activityType == NSUserActivityTypeBrowsingWeb,
          let url = userActivity.webpageURL else { return false }
    handleDeepLink(url)   // 기존 공통 처리 호출
}

// SceneDelegate (권장)
func scene(_ scene: UIScene, continue userActivity: NSUserActivity) {
    guard userActivity.activityType == NSUserActivityTypeBrowsingWeb,
          let url = userActivity.webpageURL else { return }
    handleDeepLink(url)   // 기존 공통 처리 호출
}
```

> 원칙: **입구는 분리(openURL vs continueUserActivity), 라우팅은 공통(DeepLinkRouter)**.  
> AASA 반영 후 iOS가 캐시하므로 변경 테스트 시 기기 재부팅 또는 설정→Safari→고급→웹사이트 데이터에서 도메인 캐시 삭제.

---

#### C. 공통 라우팅 규약 샘플
- 경로 규칙  
  - `/user/profile?uid=<string>`  
  - `/search?query=<string>&page=<int>`  
- 필수/선택 파라미터  
  - `uid`(필수), `query`(선택), `page`(선택, 기본값 1)  
- 인코딩  
  - 쿼리 값은 **Percent-encoding** 적용. 내부에서 `URLQueryItem` 사용 권장.  

```swift
// 안전한 쿼리 구성 예시
var comps = URLComponents(string: "https://myapp.com/search")!
comps.queryItems = [
    URLQueryItem(name: "query", value: "men's shoes"),
    URLQueryItem(name: "page", value: "2")
]
```

---

#### D. 테스트 체크리스트
- 스킴 진입: 메모 앱에 `myapp://user/profile?uid=1` 붙여넣고 탭 → 화면 진입 확인  
- 유니버설 링크 진입: 메모/메일/메시지 등에서 `https://myapp.com/user/profile?uid=1` 탭 → 앱 열림 확인  
- 주소창 직접 입력: 유니버설 링크는 동작하지 않을 수 있음(사파리 정책) → 웹 랜딩/Fallback 확인  
- 인앱 브라우저(카카오/인스타/페북): 유니버설 링크 미지원 시 랜딩 페이지 → “앱으로 열기(스킴)” 버튼 동작 확인  
- 설치 유도: 미설치 단말에서 링크 탭 → 스토어 Fallback → 설치 후 첫 실행 시 **Deferred Deep Link** 경로 복원 확인  
- AASA/경로 제약: 허용 `paths` 외 경로는 웹으로 열리는지 확인  

---

#### E. 흔한 이슈와 대응
- **AASA 캐시**: 파일 수정 후에도 즉시 반영되지 않음 → 기기 재시작 또는 캐시 삭제  
- **ATS/SSL**: AASA 도메인은 TLS 필요. 인증서/체인 문제 시 매칭 실패  
- **도메인 다중 운영**: `applinks:` 항목을 모든 서브도메인에 추가  
- **앱 내에서 openURL로 유니버설 링크 열기**: 사파리 정책상 리다이렉트 불가 → 내부에서 직접 라우터 호출  
- **URI만 존재하는 외부 링크 처리**: 유니버설 링크 우선, 필요 시 스킴 백업 경로 유지

## Android  
- **커스텀 스킴(Custom Scheme)**: iOS와 유사하게 앱 고유 스킴을 등록해 앱을 호출하는 방식이다.  
- **App Link**: Android의 유니버설 링크 개념으로 HTTP/HTTPS 링크를 통해 앱 또는 웹으로 연결한다.  
- **Deferred Deep Link**: 유니버설 링크(App Link)를 기반으로 구현되며, 앱 미설치 상태에서 링크 클릭 시 설치 후에도 특정 화면으로 이동하도록 동작하는 기능이다.  

## 4. 차이와 혼선  
기획자는 딥링크를 사용자 경험과 마케팅 관점에서 바라본다. 반면 개발자는 딥링크를 구현하는 다양한 기술적 방법에 집중한다. 같은 ‘딥링크’라는 용어가 상위 개념으로 사용되면서, 세부 구현 방식이나 플랫폼별 차이를 구분하지 않아 혼란이 발생한다.

## 5. 정리  
딥링크는 앱 내 특정 위치로 직접 연결하는 상위 개념이다. 이를 구현하는 방법은 다양하며, 기획자와 개발자가 명확한 소통과 정의를 통해 이해를 맞추는 것이 중요하다. 딥링크는 사용자 경험 향상을 위한 필수 요소이며, 스킴, 유니버설 링크, 앱 링크, 디퍼드 딥링크 등 다양한 기술적 방법으로 구현된다.


## HISTORY
- 250907 : 초안작성 ( Android 문서 생성시 OS 별로 분리 예정 )