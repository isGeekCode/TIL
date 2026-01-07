# RN_Firebase_001_FCM_푸시_알림_기초

## 🤔 이 문서를 읽기 전에
- **선수 지식**: React Native 기본, Firebase 개념
- **예상 소요 시간**: 40분
- **준비물**: Firebase 프로젝트 (실습 시)

## 🎯 이 문서에서 배울 것
1. FCM (Firebase Cloud Messaging)이 무엇인지
2. 푸시 알림 권한 요청하기 (iOS)
3. FCM 토큰 가져오기
4. 3가지 푸시 상태 처리 (포그라운드, 백그라운드, 종료)
5. 푸시 클릭 시 페이지 이동하기

---

## 📖 본문

### 1. FCM이 뭐야?

#### 한 줄 요약
**"구글에서 제공하는 무료 푸시 알림 서비스"**

#### 푸시 알림 흐름

```
1. 서버에서 FCM 서버로 푸시 전송 요청
   ↓
2. FCM 서버가 디바이스에 푸시 전달
   ↓
3. 앱에서 푸시 수신/표시
   ↓
4. 사용자가 푸시 클릭
   ↓
5. 앱 실행 + 특정 페이지 이동
```

**자세한 다이어그램:**
```
┌─────────────────┐
│   백엔드 서버    │
│                 │
│  "신규 메시지   │
│   도착했습니다" │
└────────┬────────┘
         │ POST /fcm/send
         │ {
         │   to: "FCM_TOKEN_ABC123",
         │   notification: { title: "메시지", body: "내용" }
         │ }
         ↓
┌──────────────────────────────┐
│     FCM 서버 (Google)         │
│                               │
│  - 토큰 검증                  │
│  - 디바이스 라우팅            │
│  - 재시도 처리                │
└──────────┬───────────────────┘
           │
           │ Push Notification
           ↓
    ┌─────────────────┐
    │   사용자 디바이스  │
    │                  │
    │  📱 iPhone       │
    │  🤖 Android      │
    └────────┬─────────┘
             │
             │ 푸시 수신
             ↓
      ┌───────────────┐
      │   React Native │
      │   앱 (FCM SDK) │
      │                │
      │  - 포그라운드  │
      │  - 백그라운드  │
      │  - 종료 상태   │
      └───────────────┘
```

---

### 2. FCM 토큰이 뭐야?

#### FCM 토큰 = 디바이스 고유 주소

```
디바이스마다 고유한 FCM 토큰 할당:

예시:
dKj8xN2... (iOS - iPhone 14 Pro)
f9sL3mP... (Android - Galaxy S23)
a2bC4dE... (iOS - iPad Air)

→ 서버는 이 토큰으로 특정 디바이스에 푸시 전송
```

**토큰 생명주기:**
```
1. 앱 최초 설치 → FCM 토큰 생성
2. 서버에 토큰 등록
3. 앱 재설치, OS 업데이트 등 → 토큰 갱신
4. 서버에 갱신된 토큰 업데이트 (중요!)
```

---

## 3. 권한 요청 (iOS만)

### 3.1 iOS는 권한 필수

```typescript
// src/lib/messaging.ts

import messaging from '@react-native-firebase/messaging';
import { Platform } from 'react-native';

/**
 * 푸시 알림 권한 요청
 * iOS: 사용자에게 권한 팝업 표시
 * Android: 자동 허용
 */
export async function requestPushPermission(): Promise<boolean> {
  try {
    if (Platform.OS === 'ios') {
      const authStatus = await messaging().requestPermission();

      const enabled =
        authStatus === messaging.AuthorizationStatus.AUTHORIZED ||
        authStatus === messaging.AuthorizationStatus.PROVISIONAL;

      if (enabled) {
        console.log('[FCM] 푸시 알림 권한 허용됨');
      } else {
        console.log('[FCM] 푸시 알림 권한 거부됨');
      }

      return enabled;
    }

    // Android는 기본적으로 허용
    return true;
  } catch (error) {
    console.error('[FCM] 푸시 알림 권한 요청 실패:', error);
    return false;
  }
}
```

### 3.2 권한 상태 확인

```typescript
// 현재 권한 상태 확인 (요청하지 않고 조회만)
const authStatus = await messaging().hasPermission();

switch (authStatus) {
  case messaging.AuthorizationStatus.AUTHORIZED:
    console.log('푸시 알림 허용됨');
    break;
  case messaging.AuthorizationStatus.DENIED:
    console.log('푸시 알림 거부됨');
    break;
  case messaging.AuthorizationStatus.NOT_DETERMINED:
    console.log('아직 권한 요청 안 함');
    break;
  case messaging.AuthorizationStatus.PROVISIONAL:
    console.log('임시 권한 (iOS 12+ 조용한 알림)');
    break;
}
```

### 3.3 App.tsx에서 권한 요청

```typescript
// App.tsx

import { useEffect } from 'react';
import { requestPushPermission, getFCMToken } from './src/lib/messaging';

function App() {
  useEffect(() => {
    // 앱 시작 시 푸시 알림 권한 요청
    (async () => {
      const granted = await requestPushPermission();

      if (granted) {
        // 권한 허용되면 FCM 토큰 가져오기
        const token = await getFCMToken();
        console.log('FCM 토큰:', token);

        // TODO: 서버에 토큰 전송
        // await sendTokenToServer(token);
      }
    })();
  }, []);

  return <StackNavigation />;
}
```

---

## 4. FCM 토큰 가져오기

### 4.1 기본 구현

```typescript
// src/lib/messaging.ts

/**
 * FCM 토큰 가져오기
 * 서버에 등록하여 푸시 알림을 보낼 수 있도록 합니다.
 */
export async function getFCMToken(): Promise<string | null> {
  try {
    const token = await messaging().getToken();
    console.log('[FCM] FCM 토큰:', token);
    return token;
  } catch (error) {
    console.error('[FCM] FCM 토큰 가져오기 실패:', error);
    return null;
  }
}
```

### 4.2 서버에 토큰 전송

```typescript
// src/api/push.ts

export async function registerFCMToken(token: string, userId: string) {
  try {
    const response = await fetch('https://api.example.com/push/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        fcm_token: token,
        user_id: userId,
        platform: Platform.OS,  // 'ios' or 'android'
        app_version: DeviceInfo.getVersion(),
      }),
    });

    if (response.ok) {
      console.log('[API] FCM 토큰 등록 성공');
    } else {
      console.error('[API] FCM 토큰 등록 실패:', response.status);
    }
  } catch (error) {
    console.error('[API] FCM 토큰 전송 오류:', error);
  }
}
```

### 4.3 토큰 갱신 리스너

```typescript
// src/lib/messaging.ts

/**
 * FCM 토큰 갱신 리스너 등록
 * 토큰이 변경되면 서버에 업데이트해야 합니다.
 */
export function setupTokenRefreshListener(
  onTokenRefresh: (token: string) => void
) {
  const unsubscribe = messaging().onTokenRefresh(token => {
    console.log('[FCM] FCM 토큰 갱신됨:', token);
    onTokenRefresh(token);
  });

  return unsubscribe;
}
```

**App.tsx에서 사용:**
```typescript
useEffect(() => {
  // 토큰 갱신 리스너
  const unsubscribe = setupTokenRefreshListener(async (newToken) => {
    console.log('새 토큰:', newToken);
    // 서버에 갱신된 토큰 전송
    await registerFCMToken(newToken, userId);
  });

  return () => unsubscribe();
}, [userId]);
```

---

## 5. 푸시 상태별 처리 (3가지)

### 5.1 상태 구분

| 상태 | 설명 | 알림 표시 | 처리 방법 |
|------|------|-----------|-----------|
| **포그라운드** | 앱 실행 중 (화면 보는 중) | ❌ (수동 표시 필요) | `onMessage` |
| **백그라운드** | 앱이 백그라운드에 있음 | ✅ (자동) | `onNotificationOpenedApp` |
| **종료** | 앱이 완전히 종료됨 | ✅ (자동) | `getInitialNotification` |

---

### 5.2 포그라운드 푸시 수신

```typescript
// src/lib/messaging.ts

/**
 * 포그라운드 푸시 알림 수신 리스너
 * 앱이 실행 중일 때 푸시를 받으면 호출됩니다.
 */
export function setupForegroundPushListener() {
  const unsubscribe = messaging().onMessage(async remoteMessage => {
    console.log('[FCM] 포그라운드 푸시 수신:', remoteMessage);

    // 알림 데이터
    const title = remoteMessage.notification?.title;
    const body = remoteMessage.notification?.body;
    const data = remoteMessage.data;

    console.log('제목:', title);
    console.log('내용:', body);
    console.log('커스텀 데이터:', data);

    // 필요 시 사용자에게 알림 표시 (직접 구현)
    Alert.alert(title || '알림', body || '');

    // 또는 커스텀 UI 표시
    // showInAppNotification(title, body);
  });

  return unsubscribe;
}
```

**WebShell.tsx에서 사용:**
```typescript
// src/screens/WebShell.tsx

useEffect(() => {
  const unsubscribe = setupForegroundPushListener();
  return () => unsubscribe();
}, []);
```

---

### 5.3 백그라운드 푸시 클릭

```typescript
// src/lib/messaging.ts

/**
 * 백그라운드에서 푸시 클릭 시 리스너
 * 앱이 백그라운드 상태에서 푸시를 클릭하면 호출됩니다.
 */
export function setupBackgroundPushClickListener() {
  const unsubscribe = messaging().onNotificationOpenedApp(async remoteMessage => {
    console.log('[FCM] 백그라운드 푸시 클릭:', remoteMessage);

    const campaign = remoteMessage.data?.push_campaign || 'unknown';
    const targetUrl = remoteMessage.data?.url;

    // Analytics 이벤트 전송
    await logEvent(ANALYTICS_EVENTS.PUSH_CLICK, {
      push_campaign: campaign,
    });

    // 특정 페이지로 이동
    if (targetUrl) {
      // WebView에 페이지 이동 명령 전송
      // ref.current?.injectJavaScript(`
      //   window.location.href = "${targetUrl}";
      //   true;
      // `);
    }
  });

  return unsubscribe;
}
```

**WebShell.tsx에서 사용:**
```typescript
useEffect(() => {
  const unsubscribe = setupBackgroundPushClickListener();
  return () => unsubscribe();
}, []);
```

---

### 5.4 앱 종료 상태 푸시 클릭

```typescript
// src/lib/messaging.ts

/**
 * 앱이 종료된 상태에서 푸시 클릭 처리
 * 앱이 완전히 종료되어 있을 때 푸시를 클릭하면 호출됩니다.
 */
export async function handleBackgroundPushClick(): Promise<{
  campaign: string;
  url?: string;
} | null> {
  try {
    const remoteMessage = await messaging().getInitialNotification();

    if (remoteMessage) {
      const campaign = remoteMessage.data?.push_campaign || 'unknown';
      const url = remoteMessage.data?.url;

      console.log('[FCM] 종료 상태 푸시 클릭:', campaign);

      return { campaign, url };
    }

    return null;
  } catch (error) {
    console.error('[FCM] 종료 상태 푸시 클릭 처리 실패:', error);
    return null;
  }
}
```

**WebShell.tsx에서 사용:**
```typescript
const [initialURL, setInitialURL] = useState<string | null>(null);

useEffect(() => {
  (async () => {
    // 푸시 클릭으로 앱 시작
    const pushData = await handleBackgroundPushClick();

    if (pushData?.url) {
      console.log('푸시 클릭으로 앱 시작, URL:', pushData.url);
      setInitialURL(pushData.url);

      // Analytics 이벤트 전송
      await logEvent(ANALYTICS_EVENTS.PUSH_CLICK, {
        push_campaign: pushData.campaign,
      });
    }
  })();
}, []);

// WebView source에 적용
<WebView
  source={{ uri: initialURL || BASE_URL + START_PATH }}
  ...
/>
```

---

## 6. 푸시 메시지 구조

### 6.1 서버에서 보내는 형식

```json
{
  "to": "FCM_TOKEN_ABC123",
  "notification": {
    "title": "신규 메시지",
    "body": "홍길동님이 메시지를 보냈습니다.",
    "sound": "default"
  },
  "data": {
    "push_campaign": "new_message_2025",
    "url": "https://example.com/messages/12345",
    "message_id": "12345",
    "sender_name": "홍길동"
  }
}
```

### 6.2 앱에서 받는 형식

```typescript
// remoteMessage 객체 구조

interface RemoteMessage {
  notification?: {
    title?: string;      // "신규 메시지"
    body?: string;       // "홍길동님이 메시지를 보냈습니다."
    android?: {
      sound?: string;
    };
    ios?: {
      sound?: string;
    };
  };

  data?: {
    [key: string]: string;
    // push_campaign: "new_message_2025"
    // url: "https://example.com/messages/12345"
    // message_id: "12345"
    // sender_name: "홍길동"
  };

  messageId: string;     // FCM 메시지 고유 ID
  sentTime?: number;     // 전송 시간 (timestamp)
  ttl?: number;          // Time to Live
}
```

---

## 7. 실전 통합 예시

### 7.1 App.tsx - 초기 설정

```typescript
// App.tsx

import { useEffect } from 'react';
import {
  requestPushPermission,
  getFCMToken,
  setupTokenRefreshListener,
  setupForegroundPushListener,
} from './src/lib/messaging';
import { registerFCMToken } from './src/api/push';

function App() {
  useEffect(() => {
    // 1. 푸시 권한 요청 & 토큰 등록
    (async () => {
      const granted = await requestPushPermission();

      if (granted) {
        const token = await getFCMToken();
        if (token) {
          await registerFCMToken(token, 'USER_ID_123');
        }
      }
    })();

    // 2. 포그라운드 푸시 수신 리스너
    const unsubscribeForeground = setupForegroundPushListener();

    // 3. 토큰 갱신 리스너
    const unsubscribeTokenRefresh = setupTokenRefreshListener(async (newToken) => {
      await registerFCMToken(newToken, 'USER_ID_123');
    });

    return () => {
      unsubscribeForeground();
      unsubscribeTokenRefresh();
    };
  }, []);

  return <StackNavigation />;
}
```

### 7.2 WebShell.tsx - 푸시 클릭 처리

```typescript
// src/screens/WebShell.tsx

export default function WebShell() {
  const ref = useRef<WebView>(null);
  const [initialURL, setInitialURL] = useState<string | null>(null);

  // 종료 상태 푸시 클릭 처리
  useEffect(() => {
    (async () => {
      const pushData = await handleBackgroundPushClick();

      if (pushData?.url) {
        setInitialURL(pushData.url);

        await logEvent(ANALYTICS_EVENTS.PUSH_CLICK, {
          push_campaign: pushData.campaign,
        });
      }
    })();
  }, []);

  // 백그라운드 푸시 클릭 처리
  useEffect(() => {
    const unsubscribe = setupBackgroundPushClickListener();
    return () => unsubscribe();
  }, []);

  return (
    <WebView
      ref={ref}
      source={{ uri: initialURL || BASE_URL + START_PATH }}
      ...
    />
  );
}
```

---

## 💡 직접 해보기

### 실습 1: 테스트 푸시 보내기 (Firebase Console)

1. Firebase Console → Cloud Messaging
2. "Send test message" 클릭
3. FCM 토큰 입력 (앱에서 출력된 토큰)
4. 제목, 본문 입력
5. "Test" 클릭

**확인사항:**
- 포그라운드: 앱 실행 중일 때 알림 받는지 확인
- 백그라운드: 앱 백그라운드일 때 알림 표시되는지 확인
- 클릭: 알림 클릭 시 앱 열리는지 확인

### 실습 2: 커스텀 데이터로 페이지 이동

**서버에서 보내는 푸시:**
```json
{
  "to": "FCM_TOKEN",
  "notification": {
    "title": "신규 주문",
    "body": "주문 #12345가 접수되었습니다."
  },
  "data": {
    "push_campaign": "new_order",
    "url": "https://example.com/orders/12345"
  }
}
```

**앱에서 처리:**
```typescript
messaging().onNotificationOpenedApp(remoteMessage => {
  const url = remoteMessage.data?.url;

  if (url) {
    ref.current?.injectJavaScript(`
      window.location.href = "${url}";
      true;
    `);
  }
});
```

---

## 🐛 자주 하는 실수

### ❌ 실수 1: 토큰을 서버에 안 보냄

```typescript
❌ 잘못된 코드
const token = await getFCMToken();
console.log('토큰:', token);
// 여기서 끝! 서버에 안 보냄 → 푸시 못 받음

✅ 올바른 코드
const token = await getFCMToken();
if (token) {
  await registerFCMToken(token, userId);  // 반드시 서버에 전송!
}
```

### ❌ 실수 2: 토큰 갱신 처리 안 함

```typescript
❌ 잘못된 코드
// 앱 시작 시 한 번만 토큰 가져옴
// → 토큰 갱신되면 서버가 옛날 토큰으로 푸시 보냄 → 실패!

✅ 올바른 코드
setupTokenRefreshListener(async (newToken) => {
  await registerFCMToken(newToken, userId);  // 갱신된 토큰 다시 전송
});
```

### ❌ 실수 3: iOS 권한 요청 안 함

```typescript
❌ 잘못된 코드
// iOS에서 권한 요청 안 함
const token = await getFCMToken();  // ❌ 권한 없으면 토큰 못 받음!

✅ 올바른 코드
const granted = await requestPushPermission();  // 먼저 권한 요청

if (granted) {
  const token = await getFCMToken();  // 권한 있을 때만 토큰 가져오기
}
```

---

## 🔗 참고 자료

### 공식 문서
- [React Native Firebase - Messaging](https://rnfirebase.io/messaging/usage)
- [Firebase Cloud Messaging 문서](https://firebase.google.com/docs/cloud-messaging)

### 프로젝트 파일
- `src/lib/messaging.ts`
- `src/lib/analytics.ts` (ANALYTICS_EVENTS)

---

## ✅ 체크리스트

이 문서를 다 읽었다면 체크해보세요:

- [ ] FCM이 무엇인지 이해했다
- [ ] FCM 토큰의 역할을 알겠다
- [ ] iOS에서 푸시 권한 요청하는 방법을 알겠다
- [ ] 3가지 푸시 상태(포그라운드, 백그라운드, 종료)를 이해했다
- [ ] onMessage로 포그라운드 푸시를 처리하는 방법을 알겠다
- [ ] onNotificationOpenedApp으로 백그라운드 푸시 클릭을 처리하는 방법을 알겠다
- [ ] getInitialNotification으로 종료 상태 푸시를 처리하는 방법을 알겠다
- [ ] 토큰 갱신 리스너를 등록하는 방법을 알겠다

---

## 📌 핵심 요약

1. **FCM 토큰 = 디바이스 고유 주소** (서버에 반드시 전송)
2. **iOS는 권한 필수**, Android는 자동 허용
3. **3가지 상태:**
   - 포그라운드: `onMessage`
   - 백그라운드: `onNotificationOpenedApp`
   - 종료: `getInitialNotification`
4. **토큰 갱신:** `onTokenRefresh` 리스너 등록 필수
5. **푸시 구조:** `notification` (제목/본문) + `data` (커스텀 데이터)

---

**작성일**: 2026-01-07
**난이도**: 🟡 중급
