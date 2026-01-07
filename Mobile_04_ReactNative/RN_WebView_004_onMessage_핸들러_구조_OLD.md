# RN_WebView_004_onMessage_핸들러_구조

## 🤔 이 문서를 읽기 전에
- **선수 지식**: WebView 기본 개념, Props 이해
- **예상 소요 시간**: 45분
- **준비물**: `src/webview/handlers/onMessage.ts` 파일

## 🎯 이 문서에서 배울 것
1. onMessage 핸들러의 전체 구조
2. 8가지 메시지 카테고리 (PERM, WEBVIEW, NAV, APP, CALL, AUTH, MEDIA, GEO)
3. 각 카테고리의 action별 처리 방법
4. 웹↔앱 양방향 통신 패턴

---

## 📖 본문

### 1. onMessage 핸들러 전체 구조

#### 1.1 큰 그림

```
┌─────────────────────────────────────────────────┐
│              웹 (JavaScript)                     │
│                                                  │
│  window.ReactNativeWebView.postMessage(          │
│    JSON.stringify({                              │
│      type: 'PERM',                               │
│      action: 'REQUEST',                          │
│      payload: { scopes: ['camera'] }             │
│    })                                            │
│  )                                               │
└──────────────────┬──────────────────────────────┘
                   │
                   │ postMessage
                   ↓
┌─────────────────────────────────────────────────┐
│        React Native (onMessage 핸들러)           │
│                                                  │
│  1. JSON 파싱                                    │
│  2. type에 따라 분기 (8가지)                      │
│     - PERM → handlePermissions                  │
│     - WEBVIEW → handleWebView                   │
│     - NAV → handleNavigation                    │
│     - APP → handleApp                           │
│     - CALL → handleCall                         │
│     - AUTH → handleAuth                         │
│     - MEDIA → handleMedia                       │
│     - GEO → handleGeo                           │
│  3. action에 따라 세부 처리                       │
│  4. 결과를 sendToWeb()으로 응답                   │
└─────────────────────────────────────────────────┘
```

---

### 1.2 makeOnMessage 함수 구조

```typescript
// src/webview/handlers/onMessage.ts

interface HandlerParams {
  ref: React.RefObject<WebView>;      // WebView 참조
  navigation: NavigationProp<any>;    // React Navigation
  hardReload: () => void;             // 하드 리로드 함수
  setCacheKey: (key: any) => void;    // 캐시 키 변경
  setShotPath?: (path: any) => void;  // 카메라 촬영 결과
  setCameraOpen?: (open: boolean) => void; // 카메라 모달 제어
}

export const makeOnMessage = ({ ref, navigation, hardReload, setCacheKey, setShotPath, setCameraOpen }: HandlerParams) =>
  async (e: WebViewMessageEvent) => {
    try {
      // 1. JSON 파싱
      const msg = JSON.parse(e.nativeEvent.data);
      const { type, action, payload } = msg || {};

      // 2. type에 따라 분기
      switch (type) {
        case 'PERM':
          await handlePermissions(ref, action, payload);
          break;
        case 'WEBVIEW':
          await handleWebView(ref, action, hardReload, setCacheKey);
          break;
        case 'NAV':
          handleNavigation(ref, action, navigation, payload);
          break;
        case 'APP':
          await handleApp(ref, action, payload);
          break;
        case 'CALL':
          handleCall(action, payload);
          break;
        case 'AUTH':
          await handleAuth(ref, action, payload);
          break;
        case 'MEDIA':
          await handleMedia(ref, action, payload, setShotPath, setCameraOpen);
          break;
        case 'GEO':
          await handleGeo(ref, action);
          break;
      }
    } catch {
      // 에러 무시 (JSON 파싱 실패 등)
    }
  };
```

**왜 고차 함수로 만들었나?**
```typescript
// WebShell.tsx에서 사용
const onMessage = useCallback(
  makeOnMessage({ ref, navigation, hardReload, setCacheKey, setShotPath, setCameraOpen }),
  []
);

<WebView onMessage={onMessage} ... />
```

- `ref`, `navigation` 등을 클로저로 캡처
- `useCallback`과 함께 사용하여 불필요한 재생성 방지

---

## 2. 8가지 메시지 카테고리

### 2.1 PERM - 권한 관리

#### 지원하는 action

| action | 설명 | 웹 → 앱 | 앱 → 웹 |
|--------|------|---------|---------|
| `REQUEST` | 권한 요청 | `{scopes: ['camera', 'photos']}` | `{granted: [...], denied: [...], blocked: [...]}` |
| `CHECK` | 권한 확인 | `{scopes: ['camera']}` | `{granted: [...], denied: [...], blocked: [...]}` |
| `OPEN_SETTINGS` | 설정 앱 열기 | - | - |

#### 웹에서 사용 (예시)

```javascript
// 웹 (JavaScript)

// 1. 카메라 권한 요청
window.ReactNativeWebView.postMessage(JSON.stringify({
  type: 'PERM',
  action: 'REQUEST',
  payload: { scopes: ['camera', 'photos'] }
}));

// 2. 결과 수신 (CustomEvent 리스너)
window.addEventListener('NATIVE_EVENT', (e) => {
  const { category, event, data } = e.detail;

  if (category === 'PERM' && event === 'RESULT') {
    const { granted, denied, blocked } = data;

    console.log('허용된 권한:', granted);    // ['camera']
    console.log('거부된 권한:', denied);     // ['photos']
    console.log('영구 차단 권한:', blocked); // []

    if (blocked.length > 0) {
      alert('권한이 차단되었습니다. 설정에서 허용해주세요.');

      // 설정 앱 열기
      window.ReactNativeWebView.postMessage(JSON.stringify({
        type: 'PERM',
        action: 'OPEN_SETTINGS'
      }));
    }
  }
});
```

#### 네이티브 처리 (간소화)

```typescript
async function handlePermissions(ref, action, payload) {
  switch (action) {
    case 'REQUEST': {
      const scopes: string[] = payload?.scopes || [];
      const result = await requestPermissions(scopes);
      // result: { granted: ['camera'], denied: ['photos'], blocked: [] }
      sendToWeb(ref, 'PERM', 'RESULT', result);
      break;
    }

    case 'CHECK': {
      const scopes: string[] = payload?.scopes || [];
      const result = await checkPermissions(scopes);
      sendToWeb(ref, 'PERM', 'RESULT', result);
      break;
    }

    case 'OPEN_SETTINGS': {
      await openSettings(); // iOS: Settings.app, Android: 앱 설정 화면
      break;
    }
  }
}
```

---

### 2.2 WEBVIEW - 웹뷰 제어

#### 지원하는 action

| action | 설명 | 웹 → 앱 | 앱 → 웹 |
|--------|------|---------|---------|
| `CLEAR_CACHE` | 캐시 삭제 + 리마운트 | - | - |
| `RELOAD` | 하드 리로드 (캐시 포함) | - | - |

#### 웹에서 사용 (예시)

```javascript
// 웹 (JavaScript)

// 1. 캐시 삭제 (로그아웃 시 유용)
window.ReactNativeWebView.postMessage(JSON.stringify({
  type: 'WEBVIEW',
  action: 'CLEAR_CACHE'
}));

// 2. 강제 새로고침
window.ReactNativeWebView.postMessage(JSON.stringify({
  type: 'WEBVIEW',
  action: 'RELOAD'
}));
```

#### 네이티브 처리

```typescript
async function handleWebView(ref, action, hardReload, setCacheKey) {
  switch (action) {
    case 'CLEAR_CACHE': {
      await clearSiteData(ref); // localStorage, sessionStorage, 쿠키 삭제
      setCacheKey((key: any) => key + 1); // WebView 리마운트
      break;
    }

    case 'RELOAD': {
      hardReload(); // key 변경으로 완전 재시작
      break;
    }
  }
}
```

**CLEAR_CACHE vs RELOAD 차이:**

| 동작 | CLEAR_CACHE | RELOAD |
|------|-------------|--------|
| localStorage 삭제 | ✅ | ❌ |
| 쿠키 삭제 | ✅ | ❌ |
| WebView 리마운트 | ✅ | ✅ |
| 사용 시점 | 로그아웃, 데이터 초기화 | 일반 새로고침 |

---

### 2.3 NAV - 네비게이션

#### 지원하는 action

| action | 설명 | 웹 → 앱 | 앱 → 웹 |
|--------|------|---------|---------|
| `backBtnController` | 뒤로가기 | - | - |
| `TO_TMP` | 임시 화면 이동 (예시) | - | - |

#### 웹에서 사용 (예시)

```javascript
// 웹 (JavaScript)

// 1. 커스텀 뒤로가기 (모달 닫기 등)
window.backBtnController = function() {
  if (isModalOpen) {
    closeModal();
  } else {
    // 네이티브에 뒤로가기 요청
    window.ReactNativeWebView.postMessage(JSON.stringify({
      type: 'NAV',
      action: 'backBtnController'
    }));
  }
};
```

#### 네이티브 처리

```typescript
function handleNavigation(ref, action, navigation, payload) {
  switch (action) {
    case 'backBtnController': {
      ref.current?.goBack(); // WebView history.back()
      break;
    }

    case 'TO_TMP': {
      navigation.navigate('Tmp'); // React Navigation으로 화면 전환
      break;
    }
  }
}
```

---

### 2.4 APP - 앱 정보/제어

#### 지원하는 action

| action | 설명 | 웹 → 앱 | 앱 → 웹 |
|--------|------|---------|---------|
| `webViewClose` | 앱 종료 | - | - |
| `OPEN_URL` | 외부 URL 열기 | `{url: 'https://...'}` | - |
| `GET_VERSION` | 앱 버전 정보 | - | `{App Version, Build Number, Bundle Id}` |

#### 웹에서 사용 (예시)

```javascript
// 웹 (JavaScript)

// 1. 앱 버전 확인
window.ReactNativeWebView.postMessage(JSON.stringify({
  type: 'APP',
  action: 'GET_VERSION'
}));

window.addEventListener('NATIVE_EVENT', (e) => {
  const { category, event, data } = e.detail;

  if (category === 'APP' && event === 'GET_VERSION') {
    console.log('앱 버전:', data['App Version']);      // "1.0.0"
    console.log('빌드 번호:', data['Build Number']);    // "42"
    console.log('번들 ID:', data['Bundle Id']);         // "com.example.myapp"
  }
});

// 2. 외부 URL 열기 (Safari/Chrome)
window.ReactNativeWebView.postMessage(JSON.stringify({
  type: 'APP',
  action: 'OPEN_URL',
  payload: { url: 'https://google.com' }
}));

// 3. 앱 종료
window.ReactNativeWebView.postMessage(JSON.stringify({
  type: 'APP',
  action: 'webViewClose'
}));
```

#### 네이티브 처리

```typescript
async function handleApp(ref, action, payload) {
  switch (action) {
    case 'webViewClose': {
      BackHandler.exitApp(); // 앱 종료
      break;
    }

    case 'OPEN_URL': {
      if (payload?.url) {
        Linking.openURL(payload.url); // Safari/Chrome 열기
      }
      break;
    }

    case 'GET_VERSION': {
      const versionInfo = {
        'App Version': DeviceInfo.getVersion(),
        'Build Number': DeviceInfo.getBuildNumber(),
        'Bundle Id': DeviceInfo.getBundleId(),
      };
      sendToWeb(ref, 'APP', 'GET_VERSION', versionInfo);
      break;
    }
  }
}
```

---

### 2.5 CALL - 외부 앱 연동

#### 지원하는 action

| action | 설명 | 웹 → 앱 | 앱 → 웹 |
|--------|------|---------|---------|
| `PHONE` | 전화 걸기 | `{tel: '01012345678'}` | - |
| `SMS` | 문자 보내기 | `{tel: '010...', body: '안녕하세요'}` | - |
| `EMAIL` | 이메일 보내기 | `{to: 'test@example.com', subject: '제목', body: '내용'}` | - |

#### 웹에서 사용 (예시)

```javascript
// 웹 (JavaScript)

// 1. 전화 걸기
function callPhone(number) {
  window.ReactNativeWebView.postMessage(JSON.stringify({
    type: 'CALL',
    action: 'PHONE',
    payload: { tel: number }
  }));
}

// 2. 문자 보내기
function sendSMS(number, message) {
  window.ReactNativeWebView.postMessage(JSON.stringify({
    type: 'CALL',
    action: 'SMS',
    payload: {
      tel: number,
      body: message
    }
  }));
}

// 3. 이메일 보내기
function sendEmail(to, subject, body) {
  window.ReactNativeWebView.postMessage(JSON.stringify({
    type: 'CALL',
    action: 'EMAIL',
    payload: {
      to: to,
      subject: subject,
      body: body
    }
  }));
}
```

#### 네이티브 처리

```typescript
function handleCall(action, payload) {
  switch (action) {
    case 'PHONE': {
      if (payload?.tel) {
        Linking.openURL(`tel:${payload.tel}`);
      }
      break;
    }

    case 'SMS': {
      if (payload?.tel) {
        // iOS와 Android의 SMS URL 스킴이 다름
        const sms =
          Platform.OS === 'ios'
            ? `sms:${payload.tel}&body=${encodeURIComponent(payload.body || '')}`
            : `sms:${payload.tel}?body=${encodeURIComponent(payload.body || '')}`;
        Linking.openURL(sms);
      }
      break;
    }

    case 'EMAIL': {
      let mail = `mailto:${payload.to}`;

      if (payload.subject) {
        mail += `?subject=${encodeURIComponent(payload.subject)}`;
      }

      if (payload.body) {
        mail += `${payload.subject ? '&' : '?'}body=${encodeURIComponent(payload.body)}`;
      }

      Linking.openURL(mail);
      break;
    }
  }
}
```

---

### 2.6 AUTH - 인증/토큰

#### 지원하는 action

| action | 설명 | 웹 → 앱 | 앱 → 웹 |
|--------|------|---------|---------|
| `SET_TOKEN` | 토큰 저장 (Keychain) | `{accessToken, refreshToken}` | `{accessToken, refreshToken}` |
| `GET_TOKEN` | 토큰 조회 | - | `{accessToken, refreshToken}` |
| `CLEAR_TOKEN` | 토큰 삭제 | - | `{cleared: true}` |
| `OPEN_BIOMETRICS` | 생체 인증 | - | `{result: true/false}` |

#### 웹에서 사용 (예시)

```javascript
// 웹 (JavaScript)

// 1. 로그인 후 토큰 저장
async function loginSuccess(accessToken, refreshToken) {
  window.ReactNativeWebView.postMessage(JSON.stringify({
    type: 'AUTH',
    action: 'SET_TOKEN',
    payload: {
      accessToken: accessToken,
      refreshToken: refreshToken
    }
  }));
}

// 2. 앱 시작 시 토큰 조회
window.ReactNativeWebView.postMessage(JSON.stringify({
  type: 'AUTH',
  action: 'GET_TOKEN'
}));

window.addEventListener('NATIVE_EVENT', (e) => {
  const { category, event, data } = e.detail;

  if (category === 'AUTH' && event === 'TOKEN') {
    if (data?.accessToken) {
      console.log('저장된 토큰 발견:', data.accessToken);
      // 자동 로그인 처리
    } else {
      console.log('저장된 토큰 없음');
      // 로그인 화면 표시
    }
  }
});

// 3. 로그아웃 시 토큰 삭제
function logout() {
  window.ReactNativeWebView.postMessage(JSON.stringify({
    type: 'AUTH',
    action: 'CLEAR_TOKEN'
  }));
}

// 4. 생체 인증 (지문/Face ID)
window.ReactNativeWebView.postMessage(JSON.stringify({
  type: 'AUTH',
  action: 'OPEN_BIOMETRICS'
}));

window.addEventListener('NATIVE_EVENT', (e) => {
  const { category, event, data } = e.detail;

  if (category === 'AUTH' && event === 'OPEN_BIOMETRICS') {
    if (data?.result === true) {
      console.log('생체 인증 성공');
      // 자동 로그인 또는 결제 진행
    } else {
      console.log('생체 인증 실패');
    }
  }
});
```

#### 네이티브 처리

```typescript
async function handleAuth(ref, action, payload) {
  switch (action) {
    case 'SET_TOKEN': {
      if (payload?.accessToken) {
        // Keychain (iOS) / KeyStore (Android)에 안전하게 저장
        await saveTokens(payload.accessToken, payload.refreshToken);

        // 저장 완료 응답
        sendToWeb(ref, 'AUTH', 'TOKEN', {
          accessToken: payload.accessToken,
          refreshToken: payload.refreshToken || '',
        });
      }
      break;
    }

    case 'GET_TOKEN': {
      const tokens = await loadTokens();
      sendToWeb(ref, 'AUTH', 'TOKEN', tokens);
      break;
    }

    case 'CLEAR_TOKEN': {
      await clearTokens();
      sendToWeb(ref, 'AUTH', 'CLEARED', null);
      break;
    }

    case 'OPEN_BIOMETRICS': {
      const ok = await authenticateBiometric(); // Face ID / Touch ID / 지문
      sendToWeb(ref, 'AUTH', 'OPEN_BIOMETRICS', { result: ok });
      break;
    }
  }
}
```

---

### 2.7 MEDIA - 미디어

#### 지원하는 action

| action | 설명 | 웹 → 앱 | 앱 → 웹 |
|--------|------|---------|---------|
| `OPEN_CAMERA` | 카메라 열기 | - | `{uri: '...', base64: '...'}` |
| `KEYBOARD_SHOW` | 키보드 강제 표시 | `{selector: '#input'}` | - |
| `KEYBOARD_HIDE` | 키보드 숨김 | - | - |
| `CHANGE_VOLUME` | 볼륨 변경 감지 | - | `{volume: 0.7}` |

#### 웹에서 사용 (예시)

```javascript
// 웹 (JavaScript)

// 1. 카메라 열기
function openCamera() {
  window.ReactNativeWebView.postMessage(JSON.stringify({
    type: 'MEDIA',
    action: 'OPEN_CAMERA'
  }));
}

window.addEventListener('NATIVE_EVENT', (e) => {
  const { category, event, data } = e.detail;

  if (category === 'MEDIA' && event === 'PHOTO_RESULT') {
    const { uri, base64 } = data;
    console.log('촬영된 이미지:', uri);
    // 이미지 업로드 또는 미리보기 표시
  }

  if (category === 'MEDIA' && event === 'ERROR') {
    if (data?.code === 'NO_PERMISSION') {
      alert('카메라 권한이 필요합니다.');
    }
  }
});

// 2. 키보드 강제 표시 (iOS에서 유용)
window.ReactNativeWebView.postMessage(JSON.stringify({
  type: 'MEDIA',
  action: 'KEYBOARD_SHOW',
  payload: { selector: '#search-input' }
}));

// 3. 볼륨 변경 감지
window.ReactNativeWebView.postMessage(JSON.stringify({
  type: 'MEDIA',
  action: 'CHANGE_VOLUME'
}));

window.addEventListener('NATIVE_EVENT', (e) => {
  const { category, event, data } = e.detail;

  if (category === 'MEDIA' && event === 'CHANGE_VOLUME') {
    console.log('현재 볼륨:', data.volume); // 0.0 ~ 1.0
  }
});
```

#### 네이티브 처리

```typescript
async function handleMedia(ref, action, payload, setShotPath, setCameraOpen) {
  switch (action) {
    case 'OPEN_CAMERA': {
      triggerHaptic(4); // 햅틱 피드백
      try {
        await ensureCameraPermissions(); // 권한 확인/요청
        setShotPath?.(null);
        setCameraOpen?.(true); // 카메라 모달 표시
      } catch (err) {
        sendToWeb(ref, 'MEDIA', 'ERROR', {
          code: 'NO_PERMISSION',
          message: String(err),
        });
      }
      break;
    }

    case 'KEYBOARD_SHOW': {
      const selector = payload?.selector;
      showKeyboard(ref, selector); // injectJavaScript로 포커스
      break;
    }

    case 'KEYBOARD_HIDE': {
      hideKeyboard(ref);
      break;
    }

    case 'CHANGE_VOLUME': {
      const currentVolume = await VolumeManager.getVolume();
      sendToWeb(ref, 'MEDIA', 'CHANGE_VOLUME', {
        volume: currentVolume.volume,
      });

      // 볼륨 변경 리스너 등록
      VolumeManager.addVolumeListener(result => {
        sendToWeb(ref, 'MEDIA', 'CHANGE_VOLUME', { volume: result.volume });
      });
      break;
    }
  }
}
```

---

### 2.8 GEO - 위치 정보

#### 지원하는 action

| action | 설명 | 웹 → 앱 | 앱 → 웹 |
|--------|------|---------|---------|
| `GET_LOCATION` | 현재 위치 조회 | - | `{latitude, longitude, accuracy}` |

#### 웹에서 사용 (예시)

```javascript
// 웹 (JavaScript)

// 위치 조회
window.ReactNativeWebView.postMessage(JSON.stringify({
  type: 'GEO',
  action: 'GET_LOCATION'
}));

window.addEventListener('NATIVE_EVENT', (e) => {
  const { category, event, data } = e.detail;

  if (category === 'GEO' && event === 'GET_LOCATION') {
    const { latitude, longitude, accuracy } = data;
    console.log('위도:', latitude);
    console.log('경도:', longitude);
    console.log('정확도:', accuracy, 'm');
  }

  if (category === 'GEO' && event === 'GET_LOCATION_ERROR') {
    console.error('위치 조회 실패:', data.message);
    // GPS 꺼짐, 권한 없음, 타임아웃 등
  }
});
```

#### 네이티브 처리

```typescript
async function handleGeo(ref, action) {
  switch (action) {
    case 'GET_LOCATION': {
      try {
        const coord = await getCurrentLocation({
          enableHighAccuracy: true,  // GPS 사용
          timeoutMs: 12000,           // 12초 타임아웃
          maximumAgeMs: 0,            // 캐시 사용 안 함
        });
        // coord: { latitude: 37.5665, longitude: 126.9780, accuracy: 10 }
        sendToWeb(ref, 'GEO', 'GET_LOCATION', coord);
      } catch (err: any) {
        sendToWeb(ref, 'GEO', 'GET_LOCATION_ERROR', {
          code: err?.code,      // TIMEOUT, PERMISSION_DENIED, POSITION_UNAVAILABLE
          message: err?.message,
        });
      }
      break;
    }
  }
}
```

---

## 3. sendToWeb 함수 - 앱에서 웹으로 메시지 보내기

### 3.1 sendToWeb 구조

```typescript
// src/webview/utils/sendToWeb.ts

export function sendToWeb(
  ref: React.RefObject<WebView>,
  category: string,
  event: string,
  data: any
) {
  const message = {
    category,
    event,
    data,
  };

  ref.current?.injectJavaScript(`
    (function() {
      const event = new CustomEvent('NATIVE_EVENT', {
        detail: ${JSON.stringify(message)}
      });
      window.dispatchEvent(event);
    })();
    true;
  `);
}
```

### 3.2 사용 예시

```typescript
// 네이티브에서 웹으로 권한 결과 전송
sendToWeb(ref, 'PERM', 'RESULT', {
  granted: ['camera'],
  denied: ['photos'],
  blocked: []
});

// 웹에서 수신
window.addEventListener('NATIVE_EVENT', (e) => {
  const { category, event, data } = e.detail;
  // category: 'PERM'
  // event: 'RESULT'
  // data: { granted: ['camera'], denied: ['photos'], blocked: [] }
});
```

---

## 💡 직접 해보기

### 실습 1: 메시지 카테고리 맵 만들기

`src/webview/handlers/messageCategories.ts` 파일 생성:

```typescript
export const MESSAGE_CATEGORIES = {
  PERM: {
    name: '권한 관리',
    actions: ['REQUEST', 'CHECK', 'OPEN_SETTINGS'],
  },
  WEBVIEW: {
    name: '웹뷰 제어',
    actions: ['CLEAR_CACHE', 'RELOAD'],
  },
  NAV: {
    name: '네비게이션',
    actions: ['backBtnController', 'TO_TMP'],
  },
  APP: {
    name: '앱 정보/제어',
    actions: ['webViewClose', 'OPEN_URL', 'GET_VERSION'],
  },
  CALL: {
    name: '외부 앱 연동',
    actions: ['PHONE', 'SMS', 'EMAIL'],
  },
  AUTH: {
    name: '인증/토큰',
    actions: ['SET_TOKEN', 'GET_TOKEN', 'CLEAR_TOKEN', 'OPEN_BIOMETRICS'],
  },
  MEDIA: {
    name: '미디어',
    actions: ['OPEN_CAMERA', 'KEYBOARD_SHOW', 'KEYBOARD_HIDE', 'CHANGE_VOLUME'],
  },
  GEO: {
    name: '위치 정보',
    actions: ['GET_LOCATION'],
  },
} as const;
```

### 실습 2: 웹 브릿지 래퍼 만들기

웹에서 사용하기 쉽도록 래퍼 함수 작성:

```javascript
// 웹 (JavaScript)

class NativeBridge {
  // 권한 요청
  static requestPermissions(scopes) {
    return new Promise((resolve) => {
      const handler = (e) => {
        const { category, event, data } = e.detail;
        if (category === 'PERM' && event === 'RESULT') {
          window.removeEventListener('NATIVE_EVENT', handler);
          resolve(data);
        }
      };

      window.addEventListener('NATIVE_EVENT', handler);

      window.ReactNativeWebView.postMessage(JSON.stringify({
        type: 'PERM',
        action: 'REQUEST',
        payload: { scopes }
      }));
    });
  }

  // 앱 버전 조회
  static getAppVersion() {
    return new Promise((resolve) => {
      const handler = (e) => {
        const { category, event, data } = e.detail;
        if (category === 'APP' && event === 'GET_VERSION') {
          window.removeEventListener('NATIVE_EVENT', handler);
          resolve(data);
        }
      };

      window.addEventListener('NATIVE_EVENT', handler);

      window.ReactNativeWebView.postMessage(JSON.stringify({
        type: 'APP',
        action: 'GET_VERSION'
      }));
    });
  }

  // 전화 걸기
  static callPhone(number) {
    window.ReactNativeWebView.postMessage(JSON.stringify({
      type: 'CALL',
      action: 'PHONE',
      payload: { tel: number }
    }));
  }
}

// 사용 예시
const result = await NativeBridge.requestPermissions(['camera', 'photos']);
console.log(result.granted); // ['camera']

const version = await NativeBridge.getAppVersion();
console.log(version['App Version']); // "1.0.0"

NativeBridge.callPhone('01012345678');
```

---

## 🐛 자주 하는 실수

### ❌ 실수 1: JSON.stringify 빠뜨림

```javascript
❌ 잘못된 코드
window.ReactNativeWebView.postMessage({
  type: 'PERM',
  action: 'REQUEST'
});

✅ 올바른 코드
window.ReactNativeWebView.postMessage(JSON.stringify({
  type: 'PERM',
  action: 'REQUEST'
}));
```

### ❌ 실수 2: 응답 대기 안 함

```javascript
❌ 잘못된 코드
window.ReactNativeWebView.postMessage(JSON.stringify({
  type: 'PERM',
  action: 'REQUEST',
  payload: { scopes: ['camera'] }
}));

// 바로 카메라 사용 시도 → 권한 없으면 크래시!
openCamera();

✅ 올바른 코드
window.ReactNativeWebView.postMessage(JSON.stringify({
  type: 'PERM',
  action: 'REQUEST',
  payload: { scopes: ['camera'] }
}));

window.addEventListener('NATIVE_EVENT', (e) => {
  const { category, event, data } = e.detail;

  if (category === 'PERM' && event === 'RESULT') {
    if (data.granted.includes('camera')) {
      openCamera(); // 권한 있을 때만 카메라 열기
    }
  }
});
```

### ❌ 실수 3: 에러 처리 안 함

```javascript
❌ 잘못된 코드
window.ReactNativeWebView.postMessage(JSON.stringify({
  type: 'GEO',
  action: 'GET_LOCATION'
}));

window.addEventListener('NATIVE_EVENT', (e) => {
  const { category, event, data } = e.detail;

  if (category === 'GEO' && event === 'GET_LOCATION') {
    showMap(data.latitude, data.longitude);
    // GET_LOCATION_ERROR 무시 → 아무 일도 안 일어남
  }
});

✅ 올바른 코드
window.addEventListener('NATIVE_EVENT', (e) => {
  const { category, event, data } = e.detail;

  if (category === 'GEO') {
    if (event === 'GET_LOCATION') {
      showMap(data.latitude, data.longitude);
    } else if (event === 'GET_LOCATION_ERROR') {
      alert(`위치 조회 실패: ${data.message}`);
    }
  }
});
```

---

## 🔗 참고 자료

### 프로젝트 파일
- `src/webview/handlers/onMessage.ts` (핵심!)
- `src/webview/utils/sendToWeb.ts`
- `src/webview/permissions.ts`
- `src/lib/secureStore.ts`

### 관련 문서
- 이전: `RN_WebView_003_웹과_앱이_대화하기_기초.md`
- 다음: `RN_Native_001_Native_Module_이해하기.md`

---

## ✅ 체크리스트

이 문서를 다 읽었다면 체크해보세요:

- [ ] onMessage 핸들러의 8가지 카테고리를 이해했다
- [ ] 각 카테고리의 주요 action을 알겠다
- [ ] sendToWeb 함수로 앱→웹 통신하는 방법을 알겠다
- [ ] 웹에서 NATIVE_EVENT 리스너로 응답 받는 방법을 알겠다
- [ ] 권한 요청 (PERM) 플로우를 이해했다
- [ ] 토큰 저장 (AUTH) 방법을 알겠다
- [ ] 외부 앱 연동 (CALL) 방법을 알겠다

---

## 📌 핵심 요약

1. **8가지 카테고리:** PERM, WEBVIEW, NAV, APP, CALL, AUTH, MEDIA, GEO
2. **메시지 구조:** `{type, action, payload}`
3. **웹→앱:** `window.ReactNativeWebView.postMessage(JSON.stringify(...))`
4. **앱→웹:** `sendToWeb(ref, category, event, data)`
5. **웹 수신:** `window.addEventListener('NATIVE_EVENT', ...)`
6. **에러 처리:** 항상 _ERROR 이벤트도 처리

---

**다음 문서:** `RN_Native_001_Native_Module_이해하기.md`로 이어집니다!

**작성일**: 2026-01-07
**난이도**: 🟡 중급
