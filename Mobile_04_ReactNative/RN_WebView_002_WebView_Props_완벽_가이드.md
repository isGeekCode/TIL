# RN_WebView_002_WebView_Props_완벽_가이드

## 🤔 이 문서를 읽기 전에
- **선수 지식**: WebView 기본 개념 (RN_WebView_001 읽었음)
- **예상 소요 시간**: 40분
- **준비물**: 실제 WebShell.tsx 코드

## 🎯 이 문서에서 배울 것
1. WebView의 25가지 주요 Props 완벽 이해
2. 각 Props가 왜 필요한지
3. 실무에서 어떻게 사용하는지
4. Props를 잘못 설정하면 생기는 문제

---

## 📖 본문

### 1. WebView Props 전체 지도

#### Props 카테고리 (6가지)

```
┌────────────────────────────────────────┐
│         WebView Props (25개)           │
├────────────────────────────────────────┤
│ 1️⃣ 기본 설정 (5개)                      │
│   - source, userAgent, ref, key        │
│                                        │
│ 2️⃣ JavaScript 제어 (4개)                │
│   - javaScriptEnabled, domStorageEnabled│
│   - injectedJavaScriptBeforeContentLoaded│
│                                        │
│ 3️⃣ 생명주기 이벤트 (6개)                 │
│   - onLoadStart, onLoad, onLoadEnd     │
│   - onLoadProgress, onError, onHttpError│
│                                        │
│ 4️⃣ 네비게이션 제어 (4개)                 │
│   - onNavigationStateChange            │
│   - onShouldStartLoadWithRequest       │
│   - allowsBackForwardNavigationGestures│
│                                        │
│ 5️⃣ 통신 및 보안 (4개)                    │
│   - onMessage, originWhitelist         │
│   - sharedCookiesEnabled               │
│                                        │
│ 6️⃣ 고급 기능 (6개)                       │
│   - onOpenWindow, setSupportMultipleWindows│
│   - onContentProcessDidTerminate       │
│   - onRenderProcessGone                │
│   - webviewDebuggingEnabled            │
└────────────────────────────────────────┘
```

---

## 2. 기본 설정 Props (필수 5개)

### 2.1 source - 어디를 로드할까?

```typescript
source={{ uri: initialURL ? initialURL : BASE_URL + START_PATH }}
```

**역할:**
- WebView가 로드할 웹페이지 URL 지정

**실무 패턴:**
```typescript
// 패턴 1: 고정 URL
source={{ uri: 'https://example.com' }}

// 패턴 2: 딥링크 처리 (initialURL 있으면 우선)
source={{ uri: initialURL ? initialURL : BASE_URL + START_PATH }}

// 패턴 3: 로컬 HTML
source={{ html: '<h1>Hello</h1>' }}
```

**주의 사항:**
- ❌ `source="https://example.com"` (문자열로 직접 전달 불가)
- ✅ `source={{ uri: "https://example.com" }}` (객체로 전달)

---

### 2.2 userAgent - 앱임을 알려주는 신호

```typescript
// 실제 코드
useEffect(() => {
  const loadUserAgent = async () => {
    const baseUserAgent = await DeviceInfo.getUserAgent();

    if (Platform.OS === 'android') {
      setUserAgent(`${baseUserAgent} myapp MyApp/(Android)`);
    } else if (Platform.OS === 'ios') {
      setUserAgent(`${baseUserAgent} myapp MyApp/(iOS)`);
    }
  };

  loadUserAgent();
}, []);

// WebView에 적용
<WebView userAgent={userAgent} ... />
```

**왜 필요한가?**
1. **웹 서버가 앱인지 브라우저인지 구분**
   ```javascript
   // 웹 서버에서 (Node.js 예시)
   const userAgent = req.headers['user-agent'];

   if (userAgent.includes('MyApp')) {
     // 앱에서 온 요청
     // → 앱 전용 응답 (푸시 토큰 등록 UI 표시)
   } else {
     // 브라우저에서 온 요청
     // → 웹 전용 응답 (모바일 앱 다운로드 배너 표시)
   }
   ```

2. **Analytics 구분**
   - Google Analytics에서 "iOS 앱", "Android 앱" 트래픽 분리

**실제 UserAgent 예시:**
```
// iOS
Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15
(KHTML, like Gecko) Mobile/15E148 myapp MyApp/(iOS)

// Android
Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36
(KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36 myapp MyApp/(Android)
```

---

### 2.3 ref - WebView 조종간

```typescript
const ref = useRef<WebView>(null);

// 1. 웹뷰 새로고침
ref.current?.reload();

// 2. 뒤로가기
ref.current?.goBack();

// 3. 앞으로 가기
ref.current?.goForward();

// 4. JavaScript 실행
ref.current?.injectJavaScript(`
  alert('Hello from Native!');
  true;
`);
```

**실무 활용 예시:**

```typescript
// 예시 1: 하드웨어 백버튼 처리 (Android)
BackHandler.addEventListener('hardwareBackPress', () => {
  if (canGoBackRef.current) {
    ref.current?.injectJavaScript(`
      if (typeof window.backBtnController === 'function') {
        window.backBtnController(); // 웹에서 정의한 커스텀 백버튼 로직
      } else {
        window.history.back(); // 기본 뒤로가기
      }
      true;
    `);
    return true;
  }
  return false;
});

// 예시 2: 딥링크로 페이지 이동 (웜 스타트)
const onUrl = async ({ url }: { url: string }) => {
  ref.current?.injectJavaScript(`
    window.location.href = ${JSON.stringify(url)};
    true;
  `);
};
```

---

### 2.4 key - WebView 리마운트의 비밀

```typescript
const [cacheKey, setCacheKey] = useState(0);

<WebView
  key={cacheKey}  // 키가 바뀌면 컴포넌트 완전히 새로 생성
  ...
/>

// 강제 리로드 (캐시까지 날림)
const hardReload = () => {
  setCacheKey(prev => prev + 1);  // 0 → 1 → 2 → ...
};
```

**일반 reload() vs key 변경:**

| 방법 | 효과 | 사용 시점 |
|------|------|-----------|
| `ref.current?.reload()` | 페이지만 새로고침 (컴포넌트 유지) | 일반 새로고침 |
| `setCacheKey(k => k + 1)` | WebView 컴포넌트 완전 재생성 | 캐시 삭제, 백화 현상 복구 |

**실무 활용:**
```typescript
// Android 백화 현상 복구
useEffect(() => {
  if (Platform.OS !== 'android') return;

  const handleAppStateChange = (nextAppState: string) => {
    if (nextAppState === 'active' && loading) {
      // WebView 백화 복구: 강제 remount
      setCacheKey(k => k + 1);
      setLoading(false);
    }
  };

  const subscription = AppState.addEventListener('change', handleAppStateChange);
  return () => subscription.remove();
}, [loading]);
```

---

### 2.5 originWhitelist - 어떤 도메인을 허용할까?

```typescript
originWhitelist={['*']}
```

**가능한 값:**
```typescript
// 1. 모든 URL 허용 (가장 자유로움)
originWhitelist={['*']}

// 2. 특정 프로토콜만 허용
originWhitelist={['https://*', 'http://*', 'myapp://*']}

// 3. 특정 도메인만 허용
originWhitelist={['https://example.com', 'https://api.example.com']}
```

**주의:**
- `onShouldStartLoadWithRequest`와 다름!
- `originWhitelist`: **iframe, redirect 등 모든 요청**에 적용
- `onShouldStartLoadWithRequest`: **사용자 클릭, 명시적 네비게이션**만 처리

---

## 3. JavaScript 제어 Props

### 3.1 javaScriptEnabled - JavaScript 실행 허용

```typescript
javaScriptEnabled={true}
```

**반드시 true로 설정:**
- React Native WebView에서 JavaScript를 꺼두면 99% 작동 안 함
- `postMessage`, `window.ReactNativeWebView` 모두 JavaScript 필요

---

### 3.2 domStorageEnabled - localStorage 사용

```typescript
domStorageEnabled={true}
```

**왜 필요한가?**
```javascript
// 웹에서 (JavaScript)
localStorage.setItem('token', 'abc123');  // ❌ domStorageEnabled=false면 에러
localStorage.getItem('token');            // ❌ domStorageEnabled=false면 에러
```

**반드시 true로 설정:**
- 대부분의 웹 앱은 `localStorage` 사용
- 로그인 토큰, 사용자 설정 등 저장

---

### 3.3 sharedCookiesEnabled - 쿠키 공유

```typescript
sharedCookiesEnabled={true}
```

**역할:**
- WebView와 네이티브(Safari/Chrome)의 쿠키 공유
- 소셜 로그인 시 유용

**예시:**
```
1. WebView에서 로그인 → 쿠키 저장
2. Safari로 링크 열기 → 쿠키 공유됨 → 로그인 상태 유지
```

---

### 3.4 injectedJavaScriptBeforeContentLoaded - 미리 주입

```typescript
// constants.ts
export const injected = `
  window.isNativeApp = true;
  window.platform = '${Platform.OS}';

  // 웹에서 사용할 수 있는 전역 변수 설정
  window.nativeVersion = '1.0.0';

  true; // 반드시 true 반환
`;

// WebShell.tsx
<WebView
  injectedJavaScriptBeforeContentLoaded={injected}
  ...
/>
```

**실행 시점:**
```
1. WebView 로딩 시작
2. ✅ injectedJavaScriptBeforeContentLoaded 실행 (HTML 파싱 전!)
3. HTML 파싱
4. DOM 생성
5. 웹의 <script> 실행
```

**실무 활용:**
```javascript
// 웹에서 (JavaScript)
if (window.isNativeApp) {
  console.log('앱에서 실행 중!');
  console.log('플랫폼:', window.platform);  // 'ios' or 'android'
} else {
  console.log('브라우저에서 실행 중!');
}
```

---

## 4. 생명주기 이벤트 Props

### 4.1 로딩 생명주기 순서

```
1. onLoadStart
   ↓
2. onLoadProgress (여러 번 호출, progress: 0.1 → 0.5 → 1.0)
   ↓
3. onLoad (DOM 로딩 완료)
   ↓
4. onLoadEnd (모든 리소스 로딩 완료)
```

---

### 4.2 onLoadStart - 로딩 시작

```typescript
onLoadStart={() => {
  setLoading(true);
  setErrorMsg(null);

  // 네이티브 스플래시 숨김
  if (NativeModules.SplashModule) {
    NativeModules.SplashModule.hide();
  }
}}
```

**왜 스플래시를 여기서 숨기나?**
- iOS/Android 앱 시작 시 네이티브 스플래시 화면 표시됨
- WebView 로딩 시작하면 곧 화면이 보이므로 스플래시 제거
- 너무 늦게 제거하면 "무한 스플래시" 버그 발생

---

### 4.3 onLoadProgress - 진행률 추적

```typescript
onLoadProgress={e => {
  const progress = e.nativeEvent.progress; // 0.0 ~ 1.0

  // 100% 완료 시 로딩 해제
  if (progress >= 1) {
    setLoading(false);
  }
}}
```

**실무 팁:**
- 로딩바 구현 시 유용
- `progress >= 1` 체크로 onLoadEnd 대신 사용 가능

---

### 4.4 onLoad vs onLoadEnd

| 이벤트 | 시점 | 사용 예시 |
|--------|------|-----------|
| `onLoad` | DOM 로딩 완료 | JavaScript 실행 가능 시점 |
| `onLoadEnd` | 이미지 등 모든 리소스 로딩 완료 | 완전한 로딩 완료 |

```typescript
onLoad={() => {
  setLoading(false);  // 보통 여기서 로딩 해제
}}

onLoadEnd={() => {
  setLoading(false);  // 또는 여기서 (더 안전)
}}
```

---

### 4.5 onError - 에러 처리

```typescript
onError={syntheticEvent => {
  const { nativeEvent } = syntheticEvent;

  // 에러 분류
  const { category } = mapWebViewError(
    nativeEvent?.description,
    nativeEvent?.statusCode
  );

  setErrorCategory(category);
  setErrorMsg(nativeEvent?.description || '알 수 없는 에러');
  setLoading(false);
}}
```

**주요 에러 타입:**
```typescript
// mapWebViewError 구현 예시
export type WebErrorCategory =
  | 'NETWORK'      // 네트워크 연결 없음
  | 'TIMEOUT'      // 타임아웃
  | 'SSL'          // SSL 인증서 오류
  | 'NOT_FOUND'    // 404
  | 'SERVER'       // 5xx 서버 오류
  | 'UNKNOWN';     // 알 수 없음

export function mapWebViewError(
  description: string,
  statusCode?: number
): { category: WebErrorCategory } {
  // iOS 에러 메시지 예시
  if (description?.includes('A server with the specified hostname could not be found')) {
    return { category: 'NETWORK' };
  }

  // Android 에러 메시지 예시
  if (description?.includes('ERR_NAME_NOT_RESOLVED')) {
    return { category: 'NETWORK' };
  }

  // HTTP 상태 코드로 분류
  if (statusCode === 404) {
    return { category: 'NOT_FOUND' };
  }

  if (statusCode && statusCode >= 500) {
    return { category: 'SERVER' };
  }

  return { category: 'UNKNOWN' };
}
```

**에러 UI 표시:**
```typescript
{!!errorMsg && (
  <View style={styles.overlay}>
    <ErrorView
      message={errorMsg}
      category={errorCategory}
      onRetry={handleRetry}
      onOpenSettings={() => openSettings()}
    />
  </View>
)}
```

---

### 4.6 onHttpError - HTTP 오류

```typescript
onHttpError={event => {
  // 400, 500번대 HTTP 오류 시 호출
  console.log('HTTP Error:', event.nativeEvent.statusCode);
  setLoading(true);  // 일시적 오류일 수 있으므로 로딩 유지
}}
```

**onError vs onHttpError:**

| 이벤트 | 발생 조건 | 예시 |
|--------|-----------|------|
| `onError` | WebView 자체 오류 (네트워크, DNS 등) | 인터넷 없음, 도메인 못 찾음 |
| `onHttpError` | HTTP 상태 코드 오류 (4xx, 5xx) | 404, 500 |

---

## 5. 네비게이션 제어 Props

### 5.1 onNavigationStateChange - 페이지 이동 감지

```typescript
onNavigationStateChange={event => {
  // 1. 뒤로가기 가능 여부 업데이트
  onNavStateChange(event);

  // 2. 현재 URL 저장
  currentUrlRef.current = event.url || '';

  // 3. 홈 페이지 여부 체크 (뒤로가기 처리용)
  try {
    const currentUrl = new URL(event.url);
    const homeUrl = new URL(HOME_PATH);

    isHomeRef.current =
      currentUrl.origin === homeUrl.origin &&
      currentUrl.pathname === homeUrl.pathname;
  } catch {
    isHomeRef.current = false;
  }
}}
```

**event 객체 구조:**
```typescript
interface WebViewNavigation {
  url: string;           // 현재 URL
  title: string;         // 페이지 제목
  loading: boolean;      // 로딩 중인가?
  canGoBack: boolean;    // 뒤로갈 수 있나?
  canGoForward: boolean; // 앞으로 갈 수 있나?
}
```

---

### 5.2 onShouldStartLoadWithRequest - 링크 클릭 제어

```typescript
// makeOnShouldStart 구현 (간소화)
export const makeOnShouldStart = (allowHosts: string[]) => {
  return (event: any) => {
    const { url } = event;

    // 1. 허용된 도메인인지 체크
    try {
      const urlObj = new URL(url);
      const hostname = urlObj.hostname;

      const isAllowed = allowHosts.some(host =>
        hostname === host || hostname.endsWith(`.${host}`)
      );

      if (isAllowed) {
        return true;  // WebView 내에서 로딩
      }
    } catch {}

    // 2. 외부 링크는 브라우저로 열기
    if (url.startsWith('http://') || url.startsWith('https://')) {
      Linking.openURL(url);
      return false;  // WebView에서 로딩 안 함
    }

    // 3. 커스텀 스킴 처리 (전화, 문자 등)
    if (url.startsWith('tel:') || url.startsWith('sms:')) {
      Linking.openURL(url);
      return false;
    }

    return true;
  };
};

// 사용
const onShouldStart = useCallback(makeOnShouldStart(ALLOW_HOSTS), []);

<WebView onShouldStartLoadWithRequest={onShouldStart} ... />
```

**실무 활용:**
```typescript
// constants.ts
export const ALLOW_HOSTS = [
  'example.com',
  'www.example.com',
  'api.example.com',
  'dev.example.com',
  'stg.example.com',
];

// WebShell.tsx
// example.com 링크 → WebView 내에서 열림
// google.com 링크 → Safari/Chrome으로 열림
```

---

### 5.3 allowsBackForwardNavigationGestures - iOS 제스처

```typescript
allowsBackForwardNavigationGestures={true}
```

**효과:**
- iOS에서 화면 가장자리 스와이프로 뒤로가기 가능
- iPhone의 Safari와 동일한 UX

---

## 6. 통신 Props

### 6.1 onMessage - 웹으로부터 메시지 받기

```typescript
const onMessage = useCallback(
  _makeOnMessage({
    ref,
    navigation,
    hardReload,
    setCacheKey,
    setShotPath,
    setCameraOpen
  }),
  []
);

<WebView onMessage={onMessage} ... />
```

**웹에서 메시지 보내기:**
```javascript
// 웹 (JavaScript)
window.ReactNativeWebView.postMessage(JSON.stringify({
  category: 'MEDIA',
  type: 'CAMERA_OPEN',
  data: {}
}));
```

**네이티브에서 받기:**
```typescript
// makeOnMessage 구현 (간소화)
export const makeOnMessage = (deps: any) => {
  return (event: any) => {
    const message = JSON.parse(event.nativeEvent.data);

    if (message.category === 'MEDIA' && message.type === 'CAMERA_OPEN') {
      deps.setCameraOpen(true);
    }
  };
};
```

**자세한 내용:**
- `RN_WebView_003_웹과_앱이_대화하기_기초.md` 참고
- `RN_WebView_004_onMessage_핸들러_구조.md` 참고 (다음 문서)

---

## 7. 고급 Props

### 7.1 onOpenWindow - 새 창 열기 (target="_blank")

```typescript
javaScriptCanOpenWindowsAutomatically={true}
setSupportMultipleWindows={true}

onOpenWindow={e => {
  const newTargetUrl = e?.nativeEvent?.targetUrl ?? '';

  // KCP 인증 팝업
  if (newTargetUrl.includes('/membership/NhnKcpReq')) {
    navigation.navigate('WebPopup', { url: newTargetUrl });
  }

  // 애플 로그인 팝업
  if (newTargetUrl.includes('appleid.apple.com')) {
    navigation.navigate('WebPopup', { url: newTargetUrl });
  }
}}
```

**웹에서:**
```html
<!-- target="_blank"로 새 창 열기 -->
<a href="/membership/NhnKcpReq" target="_blank">KCP 인증</a>

<script>
  // 또는 JavaScript로
  window.open('/membership/NhnKcpReq', '_blank');
</script>
```

**실무 패턴:**
1. 팝업이 필요한 URL 패턴 정의
2. `onOpenWindow`에서 URL 체크
3. React Navigation으로 별도 화면(WebPopup) 표시

---

### 7.2 onContentProcessDidTerminate (iOS)

```typescript
onContentProcessDidTerminate={() => ref.current?.reload()}
```

**언제 발생하나?**
- iOS WebView 프로세스가 메모리 부족 등으로 종료될 때
- 자동 복구: reload() 호출

---

### 7.3 onRenderProcessGone (Android)

```typescript
onRenderProcessGone={event => {
  const { didCrash } = event.nativeEvent;

  if (didCrash) {
    setLoading(true);  // 또는 setCacheKey(k => k + 1)로 완전 재시작
  }
}}
```

**언제 발생하나?**
- Android WebView 렌더 프로세스 크래시
- 자동 복구: 리로드 또는 리마운트

---

### 7.4 webviewDebuggingEnabled - 디버깅 모드

```typescript
const isDebugMode = __DEV__ || Config.ENV === 'dev';

<WebView
  webviewDebuggingEnabled={isDebugMode ? true : false}
  ...
/>
```

**효과:**
- **Android:** Chrome DevTools 연결 가능 (`chrome://inspect`)
- **iOS:** Safari 개발자 도구 연결 가능

**주의:**
- 프로덕션에서는 반드시 `false`
- 보안 위험 (JavaScript 콘솔 노출)

---

## 💡 직접 해보기

### 실습 1: Props 체크리스트 만들기

WebShell.tsx를 열고 아래 Props가 모두 설정되어 있는지 확인:

```typescript
// 필수 Props (5개)
- [ ] source
- [ ] userAgent
- [ ] ref
- [ ] key
- [ ] originWhitelist

// JavaScript (3개)
- [ ] javaScriptEnabled
- [ ] domStorageEnabled
- [ ] injectedJavaScriptBeforeContentLoaded

// 생명주기 (4개 이상)
- [ ] onLoadStart
- [ ] onLoadProgress
- [ ] onLoad / onLoadEnd
- [ ] onError

// 네비게이션 (2개)
- [ ] onNavigationStateChange
- [ ] onShouldStartLoadWithRequest

// 통신 (1개)
- [ ] onMessage
```

### 실습 2: 에러 분류기 만들기

`src/webview/utils/mapWebViewError.ts` 파일을 만들고:

```typescript
export type WebErrorCategory =
  | 'NETWORK'
  | 'TIMEOUT'
  | 'NOT_FOUND'
  | 'SERVER'
  | 'UNKNOWN';

export function mapWebViewError(
  description: string,
  statusCode?: number
): { category: WebErrorCategory; message: string } {
  // TODO: 에러 분류 로직 구현

  return {
    category: 'UNKNOWN',
    message: description
  };
}
```

---

## 🐛 자주 하는 실수

### ❌ 실수 1: injectedJavaScript 끝에 true 안 붙임

```typescript
❌ 잘못된 코드
injectedJavaScriptBeforeContentLoaded={`
  window.isNativeApp = true;
`}

✅ 올바른 코드
injectedJavaScriptBeforeContentLoaded={`
  window.isNativeApp = true;
  true;  // 반드시 필요!
`}
```

### ❌ 실수 2: onError에서 loading 상태 안 바꿈

```typescript
❌ 잘못된 코드
onError={event => {
  setErrorMsg(event.nativeEvent.description);
  // setLoading(false); ← 이거 안 하면 무한 로딩!
}}

✅ 올바른 코드
onError={event => {
  setErrorMsg(event.nativeEvent.description);
  setLoading(false);  // 반드시 필요!
}}
```

### ❌ 실수 3: ref.current 체크 안 함

```typescript
❌ 잘못된 코드
ref.current.reload();  // ref.current가 null이면 크래시!

✅ 올바른 코드
ref.current?.reload();  // Optional chaining 사용
```

---

## 🔗 참고 자료

### 공식 문서
- [React Native WebView - Props](https://github.com/react-native-webview/react-native-webview/blob/master/docs/Reference.md)

### 관련 문서
- 이전: `RN_WebView_001_WebView_기본_개념.md`
- 다음: `RN_WebView_004_onMessage_핸들러_구조.md`

---

## ✅ 체크리스트

이 문서를 다 읽었다면 체크해보세요:

- [ ] WebView의 25가지 주요 Props를 카테고리별로 이해했다
- [ ] source, userAgent, ref, key의 역할을 알겠다
- [ ] 생명주기 이벤트 순서를 이해했다 (onLoadStart → onLoadProgress → onLoad → onLoadEnd)
- [ ] onError와 onHttpError의 차이를 알겠다
- [ ] onShouldStartLoadWithRequest로 외부 링크를 처리하는 방법을 알겠다
- [ ] onOpenWindow로 팝업을 처리하는 방법을 알겠다
- [ ] key 변경으로 WebView를 완전히 재시작하는 방법을 알겠다

---

## 📌 핵심 요약

1. **필수 5개:** source, userAgent, ref, key, originWhitelist
2. **생명주기:** onLoadStart → onLoadProgress → onLoad → onLoadEnd
3. **에러 처리:** onError (네트워크), onHttpError (HTTP 상태)
4. **네비게이션:** onShouldStartLoadWithRequest (외부 링크 제어)
5. **팝업:** onOpenWindow + javaScriptCanOpenWindowsAutomatically
6. **디버깅:** webviewDebuggingEnabled (개발 환경만)

---

**다음 문서:** `RN_WebView_004_onMessage_핸들러_구조.md`로 이어집니다!

**작성일**: 2026-01-07
**난이도**: 🟡 중급
