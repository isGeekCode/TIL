# RN_WebView_001_WebView_기본_개념

## 🤔 이 문서를 읽기 전에
- **선수 지식**: `RN_시작_001`, `RN_시작_002` 읽음
- **예상 소요 시간**: 45분
- **난이도**: 🟡 초급 (중요!)

## 🎯 이 문서에서 배울 것
1. WebView가 정확히 무엇인지 (브라우저와의 차이점)
2. WebShell.tsx 파일 구조 완벽 이해
3. WebView 주요 Props 설정 방법
4. START_URL, ALLOW_HOSTS의 의미

---

## 📖 본문

### 1. WebView가 정확히 뭔가요?

#### 일반 브라우저 vs WebView

**비유로 이해하기:**

```
일반 브라우저 (Chrome, Safari)
= 독립적인 집 (주소창, 탭, 북마크 등 다 있음)

WebView
= 액자 속 그림 (앱 안에 끼워 넣은 미니 브라우저)
```

**차이점 표:**

| 항목 | 일반 브라우저 | WebView |
|------|--------------|---------|
| 주소창 | ✅ 있음 | ❌ 없음 |
| 뒤로가기 버튼 | ✅ 있음 | ❌ 없음 (앱에서 구현해야 함) |
| 북마크 | ✅ 있음 | ❌ 없음 |
| 탭 | ✅ 여러 개 가능 | ❌ 하나만 |
| 앱과 통신 | ❌ 불가능 | ✅ 가능! (핵심!) |

**WebView의 핵심 능력:**
```
웹 (HTML/JS)  ←→  앱 (React Native)
      postMessage 통신 가능!
```

---

### 2. WebShell.tsx 파일 분석하기

#### 전체 구조 미리보기

```typescript
// src/screens/WebShell.tsx (간략 버전)

import { WebView } from 'react-native-webview';

const WebShell = () => {
  // 1. 상태 관리
  const webViewRef = useRef(null);
  const [isLoading, setIsLoading] = useState(true);

  // 2. WebView 렌더링
  return (
    <WebView
      ref={webViewRef}
      source={{ uri: START_URL }}
      onMessage={onMessage}
      onLoad={() => setIsLoading(false)}
      // ... 기타 props
    />
  );
};
```

#### 단계별 코드 분석

**1단계: import 문**

```typescript
import React, { useRef, useState, useEffect } from 'react';
import { WebView } from 'react-native-webview';
import { START_URL, ALLOW_HOSTS } from '../webview/constants';
```

- `WebView`: react-native-webview 패키지에서 제공
- `START_URL`: 앱이 처음 로드할 URL
- `ALLOW_HOSTS`: 허용된 도메인 목록

**2단계: webViewRef 생성**

```typescript
const webViewRef = useRef<WebView>(null);
```

**왜 ref를 쓰나요?**
- WebView를 직접 제어하기 위해
- 예: 앱에서 웹으로 메시지 보내기
```typescript
// ref를 통해 WebView 메서드 호출
webViewRef.current?.postMessage('안녕!');
```

**3단계: 상태 관리**

```typescript
const [isLoading, setIsLoading] = useState(true);
const [canGoBack, setCanGoBack] = useState(false);
```

- `isLoading`: 로딩 화면 표시 여부
- `canGoBack`: 뒤로가기 가능 여부

**4단계: WebView 컴포넌트 렌더링**

```typescript
<WebView
  ref={webViewRef}
  source={{ uri: START_URL }}
  onMessage={(event) => onMessage(webViewRef, event)}
  onLoad={() => setIsLoading(false)}
  javaScriptEnabled={true}
  domStorageEnabled={true}
  // ...
/>
```

---

### 3. WebView 주요 Props 이해하기

#### source - 어디를 로드할까?

```typescript
source={{ uri: START_URL }}

// START_URL = "https://example.com"
```

**가능한 형태:**
```typescript
// 1. 외부 URL
source={{ uri: 'https://google.com' }}

// 2. 로컬 HTML 파일
source={require('./index.html')}

// 3. HTML 문자열
source={{ html: '<h1>Hello</h1>' }}
```

#### javaScriptEnabled - JS 실행 허용

```typescript
javaScriptEnabled={true}  // 필수!
```

**왜 필수인가?**
- 웹 페이지는 대부분 JavaScript 사용
- false로 하면 웹 사이트가 제대로 안 돔
- React로 만든 웹사이트는 100% JavaScript

#### domStorageEnabled - localStorage 사용

```typescript
domStorageEnabled={true}  // 권장
```

**왜 필요한가?**
- 웹에서 localStorage, sessionStorage 사용 가능
- 로그인 토큰 등을 저장할 때 필요

#### onMessage - 웹에서 메시지 받기 (핵심!)

```typescript
onMessage={(event) => {
  const message = event.nativeEvent.data;
  console.log('웹에서 받은 메시지:', message);
}}
```

**웹에서 이렇게 보내면:**
```javascript
// 웹 코드
window.ReactNativeWebView.postMessage('안녕!');
```

**앱에서 받을 수 있음:**
```typescript
// RN 코드
onMessage={(event) => {
  console.log(event.nativeEvent.data);  // "안녕!"
}}
```

#### onLoad, onLoadStart, onLoadEnd

```typescript
onLoadStart={() => {
  console.log('로딩 시작!');
  setIsLoading(true);
}}

onLoad={() => {
  console.log('로딩 완료!');
  setIsLoading(false);
}}

onError={(syntheticEvent) => {
  console.error('로딩 실패:', syntheticEvent.nativeEvent);
}}
```

**실행 순서:**
```
1. onLoadStart (로딩 시작)
   ↓
2. (웹 페이지 로딩 중...)
   ↓
3. onLoad (로딩 완료)
```

#### onNavigationStateChange - URL 변경 감지

```typescript
onNavigationStateChange={(navState) => {
  console.log('현재 URL:', navState.url);
  setCanGoBack(navState.canGoBack);
}}
```

**언제 실행되나?**
- 페이지 이동 시
- 브라우저 히스토리 변경 시

---

### 4. START_URL과 ALLOW_HOSTS 이해하기

#### constants.ts 파일 보기

```typescript
// src/webview/constants.ts

import Config from 'react-native-config';

// 앱이 처음 로드할 URL
export const START_URL = Config.BASE_URL || 'https://example.com';

// 허용된 도메인 목록
export const ALLOW_HOSTS = [
  'example.com',
  'www.example.com',
  // 개발/스테이징 환경
  'dev.example.com',
  'stg.example.com',
];

// 앱 권한 안내 화면 표시 여부 저장 키
export const PERMISSION_GUIDE_SHOWN_KEY = '@permission_guide_shown';
```

#### START_URL - 시작 페이지

**역할:**
- 앱이 켜지면 제일 먼저 로드하는 URL
- 웹사이트의 메인 페이지

**환경별 분기:**
```typescript
// .env.dev
BASE_URL=https://dev.example.com

// .env.stg
BASE_URL=https://stg.example.com

// .env.prd
BASE_URL=https://example.com
```

**Config.ENV에 따라 자동으로 바뀜!**

#### ALLOW_HOSTS - 허용된 도메인

**왜 필요한가?**
- 보안상 특정 도메인만 허용
- 악성 사이트로의 리다이렉트 방지

**동작 방식:**
```typescript
// 사용자가 링크 클릭
웹에서: <a href="https://google.com">구글</a>

// onShouldStartLoadWithRequest에서 검사
if (!ALLOW_HOSTS.includes(hostname)) {
  // 차단! 또는 외부 브라우저로 열기
  return false;
}
```

**예시 코드:**
```typescript
// src/webview/handlers/onShouldStart.ts

export function onShouldStartLoadWithRequest(request: any) {
  const url = new URL(request.url);
  const hostname = url.hostname;

  // 허용된 도메인인지 확인
  const isAllowed = ALLOW_HOSTS.some(host =>
    hostname.includes(host)
  );

  if (!isAllowed) {
    // 외부 브라우저로 열기
    Linking.openURL(request.url);
    return false;  // WebView에서는 열지 않음
  }

  return true;  // WebView에서 열기
}
```

---

### 5. WebShell.tsx 전체 흐름 정리

#### 앱이 켜질 때부터 WebView가 보이기까지

```
1. 앱 실행
   ↓
2. App.tsx 렌더링
   ↓
3. StackNavigation 로드
   ↓
4. (최초 실행이면) PermissionGuide 표시
   ↓
5. WebShell.tsx 렌더링
   ↓
6. WebView 컴포넌트 생성
   ↓
7. START_URL 로딩 시작 (onLoadStart)
   ↓
8. LoadingView 표시 (isLoading = true)
   ↓
9. 웹 페이지 로딩 완료 (onLoad)
   ↓
10. LoadingView 숨김 (isLoading = false)
   ↓
11. WebView 화면 표시!
```

#### 다이어그램

```
┌─────────────────────────────────────┐
│         WebShell 컴포넌트            │
│  ┌───────────────────────────────┐  │
│  │  isLoading = true?           │  │
│  │    YES → LoadingView 표시     │  │
│  │    NO  → WebView 표시         │  │
│  └───────────────────────────────┘  │
│                                     │
│  ┌───────────────────────────────┐  │
│  │        <WebView>              │  │
│  │  source={{ uri: START_URL }}  │  │
│  │  onMessage={...}              │  │
│  │  onLoad={...}                 │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
```

---

## 💡 직접 해보기

### 실습 1: START_URL 바꿔보기

1. **constants.ts 파일 열기**
   ```bash
   code src/webview/constants.ts
   ```

2. **START_URL 임시 변경**
   ```typescript
   // 기존
   export const START_URL = Config.BASE_URL || 'https://example.com';

   // 테스트용으로 변경
   export const START_URL = 'https://www.naver.com';
   ```

3. **앱 재실행**
   ```bash
   # Metro 재시작 (Ctrl+C 후)
   npm start

   # 앱 실행
   npm run android:dev  # 또는 ios:dev
   ```

4. **결과 확인**
   - 네이버가 뜨면 성공!
   - WebView가 제대로 작동하는 것

5. **원복하기**
   ```typescript
   export const START_URL = Config.BASE_URL || 'https://example.com';
   ```

### 실습 2: 로딩 시 콘솔 로그 찍기

1. **WebShell.tsx 파일 열기**

2. **onLoadStart에 로그 추가**
   ```typescript
   <WebView
     // ... 기존 props
     onLoadStart={() => {
       console.log('🚀 WebView 로딩 시작!');
       setIsLoading(true);
     }}

     onLoad={() => {
       console.log('✅ WebView 로딩 완료!');
       setIsLoading(false);
     }}
   />
   ```

3. **Metro 터미널에서 로그 확인**
   ```
   LOG  🚀 WebView 로딩 시작!
   LOG  ✅ WebView 로딩 완료!
   ```

### 실습 3: JavaScript 비활성화 테스트

1. **WebView Props 수정**
   ```typescript
   <WebView
     javaScriptEnabled={false}  // JS 비활성화
     // ...
   />
   ```

2. **앱 실행**

3. **결과**
   - 웹 페이지가 제대로 안 보임
   - React로 만든 사이트는 하얀 화면

4. **다시 true로 변경**
   ```typescript
   javaScriptEnabled={true}
   ```

---

## 🐛 자주 하는 실수

### ❌ 실수 1: ref를 제대로 연결 안 함

```typescript
// ❌ 잘못된 예
const webViewRef = useRef(null);

<WebView
  // ref 연결 안 함!
  source={{ uri: START_URL }}
/>

// 나중에 이렇게 하면 에러
webViewRef.current.postMessage('안녕');  // ❌ null 참조
```

```typescript
// ✅ 올바른 예
const webViewRef = useRef(null);

<WebView
  ref={webViewRef}  // ref 연결!
  source={{ uri: START_URL }}
/>

// 이제 사용 가능
webViewRef.current?.postMessage('안녕');  // ✅
```

### ❌ 실수 2: onMessage 이벤트 구조 헷갈림

```typescript
// ❌ 잘못된 예
onMessage={(event) => {
  console.log(event);  // 객체가 복잡함
}}

// ✅ 올바른 예
onMessage={(event) => {
  const message = event.nativeEvent.data;  // 여기에 실제 데이터!
  console.log(message);
}}
```

### ❌ 실수 3: ALLOW_HOSTS에 프로토콜 포함

```typescript
// ❌ 잘못된 예
export const ALLOW_HOSTS = [
  'https://example.com',  // 프로토콜 포함 (X)
];

// ✅ 올바른 예
export const ALLOW_HOSTS = [
  'example.com',  // 도메인만
];
```

---

## 🔗 참고 자료

### 공식 문서
- [react-native-webview GitHub](https://github.com/react-native-webview/react-native-webview)
- [WebView Props 전체 목록](https://github.com/react-native-webview/react-native-webview/blob/master/docs/Reference.md)

### 관련 문서
- 이전: `RN_시작_002_내_컴퓨터에서_실행하기.md`
- **다음 (중요!)**: `RN_WebView_003_웹과_앱이_대화하기_기초.md`

---

## ✅ 체크리스트

이 문서를 다 읽었다면 체크해보세요:

- [ ] WebView가 미니 브라우저임을 이해했다
- [ ] WebShell.tsx의 전체 구조를 파악했다
- [ ] webViewRef가 왜 필요한지 안다
- [ ] javaScriptEnabled, domStorageEnabled의 역할을 안다
- [ ] onMessage가 웹-앱 통신의 핵심임을 안다
- [ ] START_URL과 ALLOW_HOSTS의 차이를 안다
- [ ] START_URL을 바꿔서 테스트해봤다

---

## 📌 핵심 요약

1. **WebView = 앱 안의 미니 브라우저**
2. **webViewRef = WebView 제어 핸들**
3. **onMessage = 웹→앱 통신 핵심**
4. **START_URL = 시작 페이지**
5. **ALLOW_HOSTS = 보안 설정 (허용 도메인)**

---

**다음 문서:** `RN_WebView_003_웹과_앱이_대화하기_기초.md`에서 드디어 양방향 통신을 배웁니다!

**작성일**: 2026-01-07
**난이도**: 🟡 초급
**중요도**: ⭐⭐⭐ (매우 중요!)
