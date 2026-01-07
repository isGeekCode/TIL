# RN_WebView_004_onMessage_핸들러_패턴과_설계

## 🤔 이 문서를 읽기 전에
- **선수 지식**: WebView 기본, postMessage 통신 (RN_WebView_003)
- **예상 소요 시간**: 45분
- **준비물**: `RN_WebView_003` 완독 필수

## 🎯 이 문서에서 배울 것
1. onMessage 핸들러를 구조화하는 방법
2. 3가지 메시지 구조 패턴
3. 메시지 분류 및 라우팅 전략
4. 확장 가능한 핸들러 설계하기
5. 프로젝트에 맞는 구조 선택하기

---

## 📖 본문

### 1. 왜 구조화가 필요한가?

#### 구조 없는 코드 (Bad)

```typescript
// ❌ 모든 메시지를 if-else로 처리 (유지보수 지옥)
const handleMessage = (event: any) => {
  const message = event.nativeEvent.data;

  if (message === '카메라') {
    openCamera();
  } else if (message === '위치') {
    getLocation();
  } else if (message === '생체인증') {
    biometric();
  } else if (message === '토큰저장') {
    saveToken();
  } else if (message === '토큰조회') {
    loadToken();
  } else if (message === '토큰삭제') {
    clearToken();
  } else if (message === '권한요청') {
    requestPermission();
  } else if (message === '설정열기') {
    openSettings();
  }
  // ... 100개 더...
};
```

**문제점:**
- 😱 메시지가 늘어날수록 코드 폭발
- 😱 비슷한 기능끼리 묶기 어려움
- 😱 에러 처리, 로깅 중복
- 😱 여러 개발자가 동시 작업 어려움

---

#### 구조화된 코드 (Good)

```typescript
// ✅ 메시지를 카테고리별로 분류하고 전담 핸들러로 위임
const handleMessage = async (event: any) => {
  try {
    const msg = JSON.parse(event.nativeEvent.data);
    const { type, action, payload } = msg;

    // 타입별로 전담 핸들러에 위임
    switch (type) {
      case 'permission':
        await handlePermission(action, payload);
        break;
      case 'auth':
        await handleAuth(action, payload);
        break;
      case 'media':
        await handleMedia(action, payload);
        break;
      case 'location':
        await handleLocation(action, payload);
        break;
    }
  } catch (error) {
    console.error('메시지 처리 실패:', error);
  }
};
```

**장점:**
- ✅ 관련 기능끼리 묶여있음
- ✅ 각 핸들러 파일을 분리 가능
- ✅ 에러 처리 한곳에서 관리
- ✅ 새 기능 추가 시 해당 핸들러만 수정

---

## 2. 메시지 구조 패턴 (3가지)

### 패턴 1: 단일 type 방식 (Simple)

**언제 사용:**
- 메시지 종류가 10개 이하
- 간단한 프로젝트
- 빠른 프로토타이핑

**메시지 구조:**
```typescript
// 웹에서
window.ReactNativeWebView.postMessage(JSON.stringify({
  type: 'openCamera'
}));

window.ReactNativeWebView.postMessage(JSON.stringify({
  type: 'getLocation'
}));

window.ReactNativeWebView.postMessage(JSON.stringify({
  type: 'requestBiometric'
}));
```

**핸들러 구조:**
```typescript
const handleMessage = async (event: any) => {
  const msg = JSON.parse(event.nativeEvent.data);

  switch (msg.type) {
    case 'openCamera':
      await openCamera();
      break;
    case 'getLocation':
      await getLocation();
      break;
    case 'requestBiometric':
      await requestBiometric();
      break;
  }
};
```

**장단점:**
- ✅ 간단함
- ✅ 학습 곡선 낮음
- ❌ 메시지 늘어나면 관리 어려움
- ❌ 비슷한 기능 그룹화 안 됨

---

### 패턴 2: Category + Action 방식 (Recommended)

**언제 사용:**
- 메시지 종류가 10개 이상
- 중대형 프로젝트
- 여러 개발자 협업

**메시지 구조:**
```typescript
// 웹에서
window.ReactNativeWebView.postMessage(JSON.stringify({
  category: 'media',       // 카테고리 (큰 분류)
  action: 'openCamera',    // 액션 (구체적인 동작)
  payload: { quality: 0.8 }
}));

window.ReactNativeWebView.postMessage(JSON.stringify({
  category: 'auth',
  action: 'saveToken',
  payload: { token: 'abc123' }
}));
```

**핸들러 구조:**
```typescript
// 메인 핸들러
const handleMessage = async (event: any) => {
  try {
    const msg = JSON.parse(event.nativeEvent.data);
    const { category, action, payload } = msg;

    switch (category) {
      case 'media':
        await handleMedia(action, payload);
        break;
      case 'auth':
        await handleAuth(action, payload);
        break;
      case 'permission':
        await handlePermission(action, payload);
        break;
      case 'location':
        await handleLocation(action, payload);
        break;
    }
  } catch (error) {
    console.error('메시지 처리 실패:', error);
  }
};

// 개별 핸들러 (파일 분리 가능)
async function handleMedia(action: string, payload: any) {
  switch (action) {
    case 'openCamera':
      await openCamera(payload);
      break;
    case 'selectPhoto':
      await selectPhoto(payload);
      break;
    case 'playVideo':
      await playVideo(payload);
      break;
  }
}

async function handleAuth(action: string, payload: any) {
  switch (action) {
    case 'saveToken':
      await saveToken(payload.token);
      break;
    case 'loadToken':
      const token = await loadToken();
      sendToWeb('auth', 'tokenLoaded', { token });
      break;
    case 'clearToken':
      await clearToken();
      break;
  }
}
```

**장단점:**
- ✅ 확장성 좋음
- ✅ 파일 분리로 협업 용이
- ✅ 코드 가독성 높음
- ❌ 초기 설정 다소 복잡

---

### 패턴 3: Domain-Based 방식 (Enterprise)

**언제 사용:**
- 대규모 프로젝트
- 복잡한 비즈니스 로직
- MSA (Microservices) 구조

**메시지 구조:**
```typescript
// 웹에서
window.ReactNativeWebView.postMessage(JSON.stringify({
  domain: 'user',           // 도메인 (비즈니스 영역)
  service: 'authentication', // 서비스
  method: 'login',          // 메서드
  params: { username, password }
}));

window.ReactNativeWebView.postMessage(JSON.stringify({
  domain: 'order',
  service: 'cart',
  method: 'add',
  params: { productId, quantity }
}));
```

**핸들러 구조:**
```typescript
// handlers/index.ts
import { UserDomainHandler } from './domains/user';
import { OrderDomainHandler } from './domains/order';

const domainHandlers = {
  user: new UserDomainHandler(),
  order: new OrderDomainHandler(),
};

const handleMessage = async (event: any) => {
  try {
    const msg = JSON.parse(event.nativeEvent.data);
    const { domain, service, method, params } = msg;

    const handler = domainHandlers[domain];
    if (handler) {
      await handler.execute(service, method, params);
    }
  } catch (error) {
    console.error('메시지 처리 실패:', error);
  }
};

// handlers/domains/user.ts
export class UserDomainHandler {
  async execute(service: string, method: string, params: any) {
    switch (service) {
      case 'authentication':
        return this.handleAuth(method, params);
      case 'profile':
        return this.handleProfile(method, params);
    }
  }

  private async handleAuth(method: string, params: any) {
    switch (method) {
      case 'login':
        return await this.login(params);
      case 'logout':
        return await this.logout();
    }
  }
}
```

**장단점:**
- ✅ 비즈니스 로직 명확히 분리
- ✅ 대규모 팀 협업 최적
- ✅ 테스트 용이
- ❌ 초기 구조 복잡
- ❌ 오버 엔지니어링 위험

---

## 3. 실전 예시: Category + Action 패턴 구현

### 3.1 폴더 구조

```
src/
└── webview/
    ├── handlers/
    │   ├── index.ts              # 메인 핸들러
    │   ├── authHandler.ts        # 인증 핸들러
    │   ├── mediaHandler.ts       # 미디어 핸들러
    │   ├── permissionHandler.ts  # 권한 핸들러
    │   └── locationHandler.ts    # 위치 핸들러
    ├── utils/
    │   └── sendToWeb.ts          # 웹으로 메시지 전송
    └── types.ts                   # 타입 정의
```

### 3.2 타입 정의

```typescript
// src/webview/types.ts

export interface WebMessage {
  category: string;
  action: string;
  payload?: any;
  reqId?: string | number;
}

export interface WebResponse {
  category: string;
  action: string;
  success: boolean;
  data?: any;
  error?: string;
  reqId?: string | number;
}
```

### 3.3 메인 핸들러

```typescript
// src/webview/handlers/index.ts

import { WebViewMessageEvent } from 'react-native-webview';
import { handleAuth } from './authHandler';
import { handleMedia } from './mediaHandler';
import { handlePermission } from './permissionHandler';
import { handleLocation } from './locationHandler';
import type { WebMessage } from '../types';

export const makeOnMessage = (ref: any, dependencies: any) => {
  return async (event: WebViewMessageEvent) => {
    try {
      const msg: WebMessage = JSON.parse(event.nativeEvent.data);
      const { category, action, payload, reqId } = msg;

      console.log(`[WebView] ${category}.${action}`, payload);

      switch (category) {
        case 'auth':
          await handleAuth(ref, action, payload, reqId);
          break;

        case 'media':
          await handleMedia(ref, action, payload, reqId);
          break;

        case 'permission':
          await handlePermission(ref, action, payload, reqId);
          break;

        case 'location':
          await handleLocation(ref, action, payload, reqId);
          break;

        default:
          console.warn(`알 수 없는 카테고리: ${category}`);
      }
    } catch (error) {
      console.error('[WebView] 메시지 처리 실패:', error);
    }
  };
};
```

### 3.4 개별 핸들러 예시

```typescript
// src/webview/handlers/authHandler.ts

import { sendToWeb } from '../utils/sendToWeb';
import { saveToken as saveTokenToKeychain, loadToken as loadTokenFromKeychain } from '../utils/secureStore';

export async function handleAuth(
  ref: any,
  action: string,
  payload: any,
  reqId?: string | number
) {
  switch (action) {
    case 'saveToken': {
      const { accessToken, refreshToken } = payload;
      await saveTokenToKeychain(accessToken, refreshToken);

      sendToWeb(ref, {
        category: 'auth',
        action: 'saveToken',
        success: true,
        reqId,
      });
      break;
    }

    case 'loadToken': {
      const tokens = await loadTokenFromKeychain();

      sendToWeb(ref, {
        category: 'auth',
        action: 'loadToken',
        success: true,
        data: tokens,
        reqId,
      });
      break;
    }

    case 'clearToken': {
      await clearTokenFromKeychain();

      sendToWeb(ref, {
        category: 'auth',
        action: 'clearToken',
        success: true,
        reqId,
      });
      break;
    }

    case 'biometric': {
      try {
        const result = await authenticateBiometric();

        sendToWeb(ref, {
          category: 'auth',
          action: 'biometric',
          success: result,
          reqId,
        });
      } catch (error) {
        sendToWeb(ref, {
          category: 'auth',
          action: 'biometric',
          success: false,
          error: error.message,
          reqId,
        });
      }
      break;
    }

    default:
      console.warn(`알 수 없는 auth action: ${action}`);
  }
}
```

```typescript
// src/webview/handlers/mediaHandler.ts

import { sendToWeb } from '../utils/sendToWeb';
import { launchCamera, launchImageLibrary } from 'react-native-image-picker';

export async function handleMedia(
  ref: any,
  action: string,
  payload: any,
  reqId?: string | number
) {
  switch (action) {
    case 'openCamera': {
      try {
        const result = await launchCamera({
          mediaType: 'photo',
          quality: payload?.quality || 0.8,
        });

        if (result.assets && result.assets[0]) {
          sendToWeb(ref, {
            category: 'media',
            action: 'openCamera',
            success: true,
            data: {
              uri: result.assets[0].uri,
              width: result.assets[0].width,
              height: result.assets[0].height,
            },
            reqId,
          });
        } else {
          sendToWeb(ref, {
            category: 'media',
            action: 'openCamera',
            success: false,
            error: '사용자가 취소했습니다',
            reqId,
          });
        }
      } catch (error) {
        sendToWeb(ref, {
          category: 'media',
          action: 'openCamera',
          success: false,
          error: error.message,
          reqId,
        });
      }
      break;
    }

    case 'selectPhoto': {
      // 유사한 로직...
      break;
    }

    default:
      console.warn(`알 수 없는 media action: ${action}`);
  }
}
```

### 3.5 sendToWeb 유틸

```typescript
// src/webview/utils/sendToWeb.ts

import type { WebResponse } from '../types';

export function sendToWeb(ref: any, response: WebResponse) {
  const message = JSON.stringify(response);

  ref.current?.postMessage(message);

  console.log(`[WebView → Web] ${response.category}.${response.action}`, {
    success: response.success,
    reqId: response.reqId,
  });
}
```

---

## 4. 웹 측 코드 (클라이언트)

### 4.1 요청-응답 래퍼

```javascript
// web/src/utils/nativeBridge.js

class NativeBridge {
  constructor() {
    this.pendingRequests = {};
    this.setupListener();
  }

  setupListener() {
    window.addEventListener('message', (event) => {
      try {
        const response = JSON.parse(event.data);
        const { reqId, success, data, error } = response;

        if (reqId && this.pendingRequests[reqId]) {
          const { resolve, reject } = this.pendingRequests[reqId];
          delete this.pendingRequests[reqId];

          if (success) {
            resolve(data);
          } else {
            reject(new Error(error || '알 수 없는 오류'));
          }
        }
      } catch (error) {
        console.error('응답 파싱 실패:', error);
      }
    });
  }

  request(category, action, payload = {}) {
    return new Promise((resolve, reject) => {
      const reqId = `${Date.now()}_${Math.random()}`;

      // 타임아웃 (10초)
      const timeout = setTimeout(() => {
        if (this.pendingRequests[reqId]) {
          delete this.pendingRequests[reqId];
          reject(new Error('요청 타임아웃'));
        }
      }, 10000);

      this.pendingRequests[reqId] = {
        resolve: (data) => {
          clearTimeout(timeout);
          resolve(data);
        },
        reject: (error) => {
          clearTimeout(timeout);
          reject(error);
        },
      };

      const message = {
        category,
        action,
        payload,
        reqId,
      };

      window.ReactNativeWebView.postMessage(JSON.stringify(message));
    });
  }
}

export const nativeBridge = new NativeBridge();
```

### 4.2 사용 예시

```javascript
// web/src/pages/LoginPage.jsx

import { nativeBridge } from '../utils/nativeBridge';

async function handleLogin() {
  try {
    // 1. 로그인 API 호출
    const response = await fetch('/api/login', {
      method: 'POST',
      body: JSON.stringify({ username, password }),
    });

    const { accessToken, refreshToken } = await response.json();

    // 2. 토큰을 앱에 저장 (Keychain)
    await nativeBridge.request('auth', 'saveToken', {
      accessToken,
      refreshToken,
    });

    console.log('로그인 성공 및 토큰 저장 완료');
  } catch (error) {
    console.error('로그인 실패:', error);
  }
}

async function handleBiometricLogin() {
  try {
    // 1. 생체 인증 요청
    const result = await nativeBridge.request('auth', 'biometric');

    if (result) {
      // 2. 저장된 토큰 조회
      const { accessToken } = await nativeBridge.request('auth', 'loadToken');

      // 3. 자동 로그인
      await loginWithToken(accessToken);
    }
  } catch (error) {
    console.error('생체 인증 실패:', error);
  }
}
```

---

## 💡 직접 해보기

### 실습: 간단한 핸들러 구조 만들기

**1단계: 메시지 타입 정의**
```typescript
// types.ts
export interface AppMessage {
  category: 'system' | 'feature' | 'data';
  action: string;
  payload?: any;
}
```

**2단계: 핸들러 작성**
```typescript
// handlers/systemHandler.ts
export async function handleSystem(action: string, payload: any) {
  switch (action) {
    case 'getVersion':
      return { version: '1.0.0', build: 42 };

    case 'openSettings':
      // 설정 앱 열기
      break;
  }
}

// handlers/index.ts
export const makeOnMessage = () => {
  return async (event: any) => {
    const msg = JSON.parse(event.nativeEvent.data);

    switch (msg.category) {
      case 'system':
        return await handleSystem(msg.action, msg.payload);
      case 'feature':
        return await handleFeature(msg.action, msg.payload);
    }
  };
};
```

---

## 🐛 자주 하는 실수

### ❌ 실수 1: 카테고리와 액션 혼동

```typescript
❌ 잘못된 예
switch (msg.category) {
  case 'saveToken':  // ← action을 category처럼 사용
    break;
}

✅ 올바른 예
switch (msg.category) {
  case 'auth':       // ← category
    if (msg.action === 'saveToken') {  // ← action
      ...
    }
    break;
}
```

### ❌ 실수 2: 에러 처리 누락

```typescript
❌ 에러 무시
async function handleMedia(action: string) {
  const result = await launchCamera();  // 실패하면 크래시!
}

✅ try-catch 필수
async function handleMedia(action: string, reqId: any) {
  try {
    const result = await launchCamera();
    sendSuccess(result, reqId);
  } catch (error) {
    sendError(error.message, reqId);
  }
}
```

---

## 🔗 참고 자료

### 관련 문서
- 이전: `RN_WebView_003_웹과_앱이_대화하기_기초.md`
- **다음 (실용)**: `RN_WebView_005_메시지_구조_설계하기.md`

---

## ✅ 체크리스트

- [ ] 구조화가 왜 필요한지 이해했다
- [ ] 3가지 메시지 패턴(Simple, Category+Action, Domain)을 알겠다
- [ ] Category + Action 패턴 구현 방법을 알겠다
- [ ] 핸들러를 파일별로 분리하는 방법을 알겠다
- [ ] 웹 측 NativeBridge 래퍼를 만들 수 있다

---

## 📌 핵심 요약

1. **구조화 = 유지보수성 향상**
2. **3가지 패턴:**
   - Simple: type만
   - Category + Action: 권장 (중대형)
   - Domain-Based: 대규모 프로젝트
3. **핸들러 분리:** 카테고리별 파일 분리
4. **웹 래퍼:** NativeBridge로 Promise 기반 통신
5. **에러 처리:** 모든 비동기 작업에 try-catch

---

**다음 문서:** `RN_WebView_005_메시지_구조_설계하기.md`에서 실제 프로젝트에 맞는 구조를 설계합니다!

**작성일**: 2026-01-07
**난이도**: 🟡 중급
