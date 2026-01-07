# RN_WebView_003_웹과_앱이_대화하기_기초

## 🤔 이 문서를 읽기 전에
- **선수 지식**: `RN_WebView_001_WebView_기본_개념.md` 필수!
- **예상 소요 시간**: 1시간
- **난이도**: 🟡 초급
- **중요도**: ⭐⭐⭐⭐⭐ (최고!)

## 🎯 이 문서에서 배울 것
1. postMessage가 무엇이고 왜 필요한지
2. 웹(HTML/JS)에서 앱(React Native)으로 메시지 보내기
3. 앱(React Native)에서 웹(HTML/JS)으로 답장 보내기
4. 실제 동작하는 코드 작성하기

---

## 📖 본문

### 1. postMessage가 뭔가요?

#### 비유로 이해하기: 우편 배달

```
웹 (HTML/JS)          앱 (React Native)
    🏠                      🏢
     ↓                       ↑
   편지 쓰기              편지 읽기
     ↓                       ↑
┌─────────────────────────────────┐
│   postMessage (우체통)           │
└─────────────────────────────────┘
```

**일반적인 웹사이트:**
- 웹과 앱이 완전히 분리됨
- 웹에서 카메라 사용? → 불가능 (웹 API만 사용 가능)
- 웹에서 생체 인증? → 불가능

**WebView + postMessage:**
- 웹: "앱아, 카메라 좀 켜줘!"
- 앱: "알겠어, 사진 찍었어!" → 웹에 전달
- 웹: 받은 사진으로 업로드

#### 왜 필요한가?

**WebView만 있으면:**
```
웹 화면은 보이지만...
- 카메라 ❌
- 위치 정보 ❌
- 생체 인증 ❌
- 푸시 알림 ❌
```

**postMessage 통신 추가:**
```
웹 화면 + 네이티브 기능 사용!
- 카메라 ✅ (앱이 대신 실행)
- 위치 정보 ✅ (앱이 대신 가져옴)
- 생체 인증 ✅ (앱이 대신 처리)
- 푸시 알림 ✅ (앱이 관리)
```

---

### 2. 웹 → 앱: 메시지 보내기 (기초)

#### 웹 코드 (HTML/JavaScript)

```html
<!-- 웹 페이지 (HTML) -->
<!DOCTYPE html>
<html>
<head>
  <title>테스트 페이지</title>
</head>
<body>
  <h1>웹에서 앱으로 메시지 보내기</h1>
  <button onclick="sendToApp()">앱에 인사하기</button>

  <script>
    function sendToApp() {
      // 핵심! window.ReactNativeWebView.postMessage()
      window.ReactNativeWebView.postMessage('안녕하세요, 앱!');
    }
  </script>
</body>
</html>
```

**핵심 코드:**
```javascript
window.ReactNativeWebView.postMessage('메시지 내용');
```

**왜 `window.ReactNativeWebView`인가?**
- react-native-webview가 자동으로 주입하는 객체
- 일반 브라우저에서는 없음 (WebView 안에서만 존재)

#### React Native 코드

```typescript
// WebShell.tsx

import React, { useRef } from 'react';
import { WebView } from 'react-native-webview';

const WebShell = () => {
  const webViewRef = useRef<WebView>(null);

  // 웹에서 메시지 받기
  const handleMessage = (event: any) => {
    // 웹에서 보낸 메시지
    const message = event.nativeEvent.data;

    console.log('웹에서 받은 메시지:', message);
    // 출력: "안녕하세요, 앱!"

    // 알림으로 표시
    alert(`웹에서 메시지: ${message}`);
  };

  return (
    <WebView
      ref={webViewRef}
      source={{ uri: 'https://example.com' }}
      onMessage={handleMessage}  // 여기서 받음!
    />
  );
};
```

**핵심 포인트:**
1. `onMessage` prop에 핸들러 연결
2. `event.nativeEvent.data`에 실제 메시지
3. 문자열로 전달됨

#### 실행 흐름

```
1. 사용자가 웹 페이지의 버튼 클릭
   ↓
2. sendToApp() 함수 실행
   ↓
3. window.ReactNativeWebView.postMessage('안녕하세요, 앱!') 호출
   ↓
4. 메시지가 "우체통"에 들어감
   ↓
5. RN의 onMessage 핸들러 실행
   ↓
6. event.nativeEvent.data로 메시지 받음
   ↓
7. console.log 또는 alert 표시
```

---

### 3. 앱 → 웹: 답장 보내기

#### React Native에서 웹으로 보내기

```typescript
// WebShell.tsx

const WebShell = () => {
  const webViewRef = useRef<WebView>(null);

  const sendToWeb = (message: string) => {
    // webViewRef를 통해 웹으로 메시지 전송
    webViewRef.current?.postMessage(message);
  };

  const handleMessage = (event: any) => {
    const message = event.nativeEvent.data;
    console.log('웹에서 받음:', message);

    // 웹에 답장 보내기
    sendToWeb('안녕하세요, 웹! 저는 앱입니다.');
  };

  return (
    <WebView
      ref={webViewRef}
      source={{ uri: 'https://example.com' }}
      onMessage={handleMessage}
    />
  );
};
```

**핵심 코드:**
```typescript
webViewRef.current?.postMessage('메시지 내용');
```

#### 웹에서 받기

```html
<!DOCTYPE html>
<html>
<body>
  <h1>앱에서 메시지 받기</h1>
  <div id="result"></div>

  <script>
    // 앱에서 메시지 받기
    window.addEventListener('message', function(event) {
      const message = event.data;
      console.log('앱에서 받은 메시지:', message);

      // 화면에 표시
      document.getElementById('result').innerText = message;
    });
  </script>
</body>
</html>
```

**핵심 코드:**
```javascript
window.addEventListener('message', function(event) {
  const message = event.data;  // 앱에서 보낸 메시지
  console.log(message);
});
```

---

### 4. JSON 객체로 통신하기 (실전)

#### 단순 문자열의 한계

```javascript
// ❌ 이렇게 하면 복잡함
window.ReactNativeWebView.postMessage('카메라|사진촬영|고화질');

// 앱에서 파싱하기 어려움
const parts = message.split('|');
const action = parts[0];  // "카메라"
const type = parts[1];    // "사진촬영"
```

#### JSON 사용 (권장!)

**웹에서 보내기:**
```javascript
// 객체를 JSON 문자열로 변환
const data = {
  action: 'camera',
  type: 'photo',
  quality: 'high'
};

window.ReactNativeWebView.postMessage(JSON.stringify(data));
```

**앱에서 받기:**
```typescript
const handleMessage = (event: any) => {
  try {
    // JSON 문자열을 객체로 파싱
    const data = JSON.parse(event.nativeEvent.data);

    console.log('action:', data.action);    // "camera"
    console.log('type:', data.type);        // "photo"
    console.log('quality:', data.quality);  // "high"

    if (data.action === 'camera') {
      // 카메라 실행 로직
    }
  } catch (error) {
    console.error('JSON 파싱 실패:', error);
  }
};
```

**앱에서 웹으로 답장:**
```typescript
const sendResult = (success: boolean, photoUri?: string) => {
  const result = {
    success: success,
    photoUri: photoUri || null,
    timestamp: Date.now()
  };

  webViewRef.current?.postMessage(JSON.stringify(result));
};
```

**웹에서 받기:**
```javascript
window.addEventListener('message', function(event) {
  try {
    const result = JSON.parse(event.data);

    if (result.success) {
      console.log('사진 촬영 성공!');
      console.log('사진 경로:', result.photoUri);
    } else {
      console.log('사진 촬영 실패');
    }
  } catch (error) {
    console.error('JSON 파싱 실패:', error);
  }
});
```

---

### 5. 실전 예제: 카메라 요청하기

#### 전체 흐름

```
웹                            앱
 │                             │
 ├─ 버튼 클릭                  │
 ├─ "카메라 켜줘" 메시지 전송 →│
 │                             ├─ 메시지 받음
 │                             ├─ 카메라 권한 확인
 │                             ├─ 카메라 실행
 │                             ├─ 사진 촬영
 │                ← 사진 결과 전송 ┤
 ├─ 결과 받음                   │
 ├─ 화면에 사진 표시            │
 │                             │
```

#### 웹 코드 (완전한 예제)

```html
<!DOCTYPE html>
<html>
<head>
  <title>카메라 테스트</title>
  <style>
    button { padding: 20px; font-size: 18px; }
    #photo { max-width: 100%; margin-top: 20px; }
  </style>
</head>
<body>
  <h1>카메라 테스트</h1>
  <button onclick="requestCamera()">사진 촬영</button>
  <div id="status"></div>
  <img id="photo" />

  <script>
    // 앱에 카메라 요청
    function requestCamera() {
      const message = {
        type: 'camera',         // 요청 타입
        action: 'takePhoto',    // 사진 촬영
        reqId: Date.now()       // 요청 ID (응답 매칭용)
      };

      document.getElementById('status').innerText = '카메라 실행 중...';
      window.ReactNativeWebView.postMessage(JSON.stringify(message));
    }

    // 앱에서 결과 받기
    window.addEventListener('message', function(event) {
      try {
        const result = JSON.parse(event.data);

        if (result.type === 'camera' && result.action === 'takePhoto') {
          if (result.success) {
            // 사진 촬영 성공
            document.getElementById('status').innerText = '촬영 완료!';
            document.getElementById('photo').src = result.photoUri;
          } else {
            // 실패
            document.getElementById('status').innerText = '촬영 실패: ' + result.error;
          }
        }
      } catch (error) {
        console.error('메시지 파싱 실패:', error);
      }
    });
  </script>
</body>
</html>
```

#### React Native 코드

```typescript
// WebShell.tsx

import React, { useRef } from 'react';
import { WebView } from 'react-native-webview';
import { launchCamera } from 'react-native-image-picker';

const WebShell = () => {
  const webViewRef = useRef<WebView>(null);

  const handleMessage = async (event: any) => {
    try {
      const msg = JSON.parse(event.nativeEvent.data);

      // 카메라 요청 처리
      if (msg.type === 'camera' && msg.action === 'takePhoto') {
        await handleCameraRequest(msg.reqId);
      }
    } catch (error) {
      console.error('메시지 파싱 오류:', error);
    }
  };

  const handleCameraRequest = async (reqId: number) => {
    try {
      // 카메라 실행
      const result = await launchCamera({
        mediaType: 'photo',
        quality: 0.8,
      });

      if (result.assets && result.assets[0]) {
        // 성공
        const response = {
          type: 'camera',
          action: 'takePhoto',
          reqId: reqId,
          success: true,
          photoUri: result.assets[0].uri,
        };

        webViewRef.current?.postMessage(JSON.stringify(response));
      } else {
        // 취소
        sendError(reqId, '사용자가 취소했습니다');
      }
    } catch (error) {
      // 에러
      sendError(reqId, error.message);
    }
  };

  const sendError = (reqId: number, errorMessage: string) => {
    const response = {
      type: 'camera',
      action: 'takePhoto',
      reqId: reqId,
      success: false,
      error: errorMessage,
    };

    webViewRef.current?.postMessage(JSON.stringify(response));
  };

  return (
    <WebView
      ref={webViewRef}
      source={{ uri: 'https://example.com' }}
      onMessage={handleMessage}
    />
  );
};

export default WebShell;
```

---

## 💡 직접 해보기

### 실습 1: 간단한 메시지 주고받기

#### Step 1: 테스트 HTML 파일 만들기

```bash
# 프로젝트 루트에 test.html 생성
touch test.html
```

```html
<!-- test.html -->
<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body { font-family: Arial; padding: 20px; }
    button {
      padding: 15px 30px;
      font-size: 16px;
      margin: 10px 0;
      display: block;
      width: 100%;
    }
    #log {
      margin-top: 20px;
      border: 1px solid #ccc;
      padding: 10px;
      min-height: 100px;
    }
  </style>
</head>
<body>
  <h1>웹-앱 통신 테스트</h1>

  <button onclick="sendHello()">앱에 인사하기</button>
  <button onclick="sendData()">앱에 데이터 보내기</button>

  <h3>받은 메시지:</h3>
  <div id="log"></div>

  <script>
    // 로그 출력 함수
    function addLog(message) {
      const log = document.getElementById('log');
      const time = new Date().toLocaleTimeString();
      log.innerHTML += `[${time}] ${message}<br>`;
    }

    // 앱에 간단한 인사
    function sendHello() {
      addLog('→ 앱에 "안녕!" 전송');
      window.ReactNativeWebView.postMessage('안녕!');
    }

    // 앱에 JSON 데이터 전송
    function sendData() {
      const data = {
        type: 'test',
        message: '테스트 메시지입니다',
        timestamp: Date.now()
      };

      addLog('→ 앱에 JSON 전송: ' + JSON.stringify(data));
      window.ReactNativeWebView.postMessage(JSON.stringify(data));
    }

    // 앱에서 메시지 받기
    window.addEventListener('message', function(event) {
      addLog('← 앱에서 받음: ' + event.data);
    });

    // 페이지 로드 시
    addLog('페이지 로드 완료');
  </script>
</body>
</html>
```

#### Step 2: WebShell.tsx 수정

```typescript
// src/screens/WebShell.tsx

import React, { useRef } from 'react';
import { WebView } from 'react-native-webview';
import { Platform } from 'react-native';

const WebShell = () => {
  const webViewRef = useRef<WebView>(null);

  const handleMessage = (event: any) => {
    const message = event.nativeEvent.data;
    console.log('📩 웹에서 받음:', message);

    try {
      // JSON 파싱 시도
      const data = JSON.parse(message);
      console.log('📦 파싱된 데이터:', data);

      // 답장 보내기 (JSON)
      const response = {
        type: 'response',
        receivedMessage: message,
        platform: Platform.OS,  // 'ios' 또는 'android'
        timestamp: Date.now()
      };

      webViewRef.current?.postMessage(JSON.stringify(response));
    } catch (error) {
      // JSON이 아니면 그냥 문자열
      console.log('📝 일반 문자열:', message);

      // 답장 보내기 (문자열)
      webViewRef.current?.postMessage(`앱이 받았습니다: "${message}"`);
    }
  };

  return (
    <WebView
      ref={webViewRef}
      source={{
        uri: Platform.OS === 'android'
          ? 'file:///android_asset/test.html'  // Android
          : require('./test.html')             // iOS (경로 조정 필요)
      }}
      onMessage={handleMessage}
      javaScriptEnabled={true}
    />
  );
};

export default WebShell;
```

#### Step 3: 테스트 실행

```bash
# Android: test.html을 android/app/src/main/assets/ 폴더로 복사
mkdir -p android/app/src/main/assets
cp test.html android/app/src/main/assets/

# 앱 실행
npm run android:dev
```

#### Step 4: 확인 사항

1. **버튼 클릭 테스트**
   - "앱에 인사하기" 버튼 클릭
   - "받은 메시지" 영역에 앱의 답장 표시됨

2. **Console 확인**
   - Metro 터미널에서 로그 확인
   ```
   LOG  📩 웹에서 받음: 안녕!
   LOG  📝 일반 문자열: 안녕!
   ```

3. **JSON 테스트**
   - "앱에 데이터 보내기" 버튼 클릭
   - JSON 파싱 성공 로그 확인

---

### 실습 2: 요청-응답 패턴 구현

#### reqId를 사용한 요청 매칭

**웹 코드:**
```javascript
// 요청 저장소
const pendingRequests = {};

// 앱에 요청 보내기
function requestFromApp(action, data) {
  const reqId = Date.now() + Math.random();  // 고유 ID

  return new Promise((resolve, reject) => {
    // 요청 저장
    pendingRequests[reqId] = { resolve, reject };

    // 타임아웃 설정 (10초)
    setTimeout(() => {
      if (pendingRequests[reqId]) {
        delete pendingRequests[reqId];
        reject(new Error('요청 타임아웃'));
      }
    }, 10000);

    // 앱에 전송
    const message = {
      reqId: reqId,
      action: action,
      data: data
    };

    window.ReactNativeWebView.postMessage(JSON.stringify(message));
  });
}

// 앱에서 응답 받기
window.addEventListener('message', function(event) {
  try {
    const response = JSON.parse(event.data);

    // reqId로 매칭
    if (response.reqId && pendingRequests[response.reqId]) {
      const request = pendingRequests[response.reqId];
      delete pendingRequests[response.reqId];

      if (response.success) {
        request.resolve(response.data);
      } else {
        request.reject(new Error(response.error));
      }
    }
  } catch (error) {
    console.error('응답 처리 실패:', error);
  }
});

// 사용 예시
async function testRequest() {
  try {
    const result = await requestFromApp('getDeviceInfo', {});
    console.log('디바이스 정보:', result);
  } catch (error) {
    console.error('에러:', error);
  }
}
```

---

## 🐛 자주 하는 실수

### ❌ 실수 1: JSON.stringify 깜빡함

```javascript
// ❌ 잘못된 예 (객체를 그대로 전송)
const data = { name: '홍길동' };
window.ReactNativeWebView.postMessage(data);
// → "[object Object]" 문자열로 전송됨!

// ✅ 올바른 예
window.ReactNativeWebView.postMessage(JSON.stringify(data));
```

### ❌ 실수 2: event.data vs event.nativeEvent.data

```typescript
// ❌ 웹에서는 event.data
window.addEventListener('message', (event) => {
  console.log(event.nativeEvent.data);  // undefined!
  console.log(event.data);              // 올바름
});

// ❌ RN에서는 event.nativeEvent.data
onMessage={(event) => {
  console.log(event.data);              // undefined!
  console.log(event.nativeEvent.data);  // 올바름
}}
```

### ❌ 실수 3: webViewRef.current 체크 안 함

```typescript
// ❌ null일 수 있음
webViewRef.current.postMessage('안녕');  // 크래시!

// ✅ Optional chaining 사용
webViewRef.current?.postMessage('안녕');

// ✅ 또는 체크
if (webViewRef.current) {
  webViewRef.current.postMessage('안녕');
}
```

### ❌ 실수 4: try-catch 없이 JSON.parse

```typescript
// ❌ 위험
const data = JSON.parse(message);  // 잘못된 JSON이면 크래시!

// ✅ 안전
try {
  const data = JSON.parse(message);
  console.log(data);
} catch (error) {
  console.error('JSON 파싱 실패:', error);
}
```

---

## 🔗 참고 자료

### 공식 문서
- [react-native-webview 통신 가이드](https://github.com/react-native-webview/react-native-webview/blob/master/docs/Guide.md#communicating-between-js-and-native)

### 관련 문서
- 이전: `RN_WebView_001_WebView_기본_개념.md`
- **다음 (중요!)**: `RN_WebView_004_onMessage_핸들러_구조.md`
- 설계: `RN_WebView_005_메시지_구조_설계하기.md`

---

## ✅ 체크리스트

이 문서를 다 읽었다면 체크해보세요:

- [ ] postMessage가 웹-앱 통신의 핵심임을 이해했다
- [ ] 웹에서 `window.ReactNativeWebView.postMessage()` 사용법을 안다
- [ ] RN에서 `webViewRef.current?.postMessage()` 사용법을 안다
- [ ] JSON.stringify와 JSON.parse를 사용할 줄 안다
- [ ] reqId를 사용한 요청-응답 매칭을 이해했다
- [ ] 실습 예제를 따라해봤다
- [ ] 자주 하는 실수들을 알고 피할 수 있다

---

## 📌 핵심 요약

1. **postMessage = 웹 ↔ 앱 통신의 유일한 방법**
2. **웹 → 앱: `window.ReactNativeWebView.postMessage()`**
3. **앱 → 웹: `webViewRef.current?.postMessage()`**
4. **JSON 사용 필수: `JSON.stringify()` / `JSON.parse()`**
5. **reqId로 요청-응답 매칭**
6. **항상 try-catch로 안전하게 처리**

---

**다음 문서:** `RN_WebView_004_onMessage_핸들러_구조.md`에서 실전 핸들러 구조를 배웁니다!

**작성일**: 2026-01-07
**난이도**: 🟡 초급
**중요도**: ⭐⭐⭐⭐⭐ (최고!)
