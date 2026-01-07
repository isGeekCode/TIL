# RN_WebView_005_메시지_구조_설계하기

## 🤔 이 문서를 읽기 전에
- **선수 지식**: WebView 통신 기초, 핸들러 패턴 (RN_WebView_003, 004)
- **예상 소요 시간**: 50분
- **준비물**: 프로젝트 기능 목록

## 🎯 이 문서에서 배울 것
1. 프로젝트에 맞는 메시지 구조 선택하기
2. 카테고리 나누는 기준
3. 실전 메시지 설계 프로세스
4. 확장 가능한 구조 만들기
5. 네이밍 컨벤션

---

## 📖 본문

### 1. 프로젝트 분석부터 시작

#### Step 1: 필요한 네이티브 기능 나열

**질문지:**
```
❓ 우리 앱에서 웹이 사용할 네이티브 기능은?

예시:
✅ 카메라 (사진 촬영, 동영상)
✅ 갤러리 (사진 선택)
✅ 위치 정보
✅ 생체 인증
✅ 푸시 알림 토큰 관리
✅ 토큰 저장 (Keychain/Keystore)
✅ 카메라/위치 권한 요청
✅ 외부 URL 열기 (브라우저, 전화, 문자)
✅ 앱 버전 정보
✅ 앱 재시작
✅ 네트워크 상태 확인
```

#### Step 2: 비슷한 기능끼리 그룹화

```
📦 미디어 관련
- 카메라
- 갤러리
- 동영상 녹화

📦 인증/보안
- 생체 인증
- 토큰 저장
- 토큰 조회
- 토큰 삭제

📦 권한
- 카메라 권한
- 위치 권한
- 알림 권한
- 설정 앱 열기

📦 위치
- 현재 위치 조회
- 위치 추적 시작/종료

📦 시스템
- 앱 버전 정보
- 네트워크 상태
- 앱 재시작

📦 외부 연동
- 브라우저 열기
- 전화 걸기
- 문자 보내기
- 이메일 보내기
```

---

### 2. 메시지 구조 선택 결정 트리

```
시작
 │
 ├─ 기능이 5개 이하? ──→ YES ──→ Simple 패턴 (type만)
 │                      │
 │                      NO
 │                      ↓
 ├─ 팀 규모 1-2명? ─────→ YES ──→ Simple 패턴 고려
 │                      │
 │                      NO
 │                      ↓
 ├─ 기능이 50개 이상? ──→ YES ──→ Domain-Based 패턴
 │                      │
 │                      NO
 │                      ↓
 └─ 대부분의 경우 ─────→ Category + Action 패턴 ✅ 권장!
```

---

### 3. Category + Action 패턴 설계 (단계별)

#### Step 1: 카테고리 정의

**좋은 카테고리 기준:**
- ✅ 명확한 책임 (Single Responsibility)
- ✅ 서로 겹치지 않음 (Mutually Exclusive)
- ✅ 5-10개 정도 (너무 많으면 오버 엔지니어링)

**예시 1: 전자상거래 앱**
```typescript
카테고리 목록:
1. auth        // 인증 (로그인, 토큰, 생체인증)
2. media       // 미디어 (카메라, 갤러리)
3. permission  // 권한 (카메라, 위치, 알림)
4. location    // 위치 (GPS)
5. payment     // 결제 (인앱결제, PG 연동)
6. social      // 소셜 (공유, SNS 로그인)
7. system      // 시스템 (앱 정보, 재시작)
8. external    // 외부 연동 (전화, 문자, 브라우저)
```

**예시 2: 메신저 앱**
```typescript
카테고리 목록:
1. auth        // 인증
2. chat        // 채팅 (메시지 읽음, 입력 중 표시)
3. media       // 미디어
4. permission  // 권한
5. notification // 푸시 알림
6. contact     // 연락처 (주소록 접근)
7. voip        // 음성/영상 통화
8. system      // 시스템
```

**예시 3: 뉴스 앱**
```typescript
카테고리 목록:
1. auth        // 인증
2. content     // 콘텐츠 (북마크, 좋아요)
3. media       // 미디어 (이미지 저장)
4. permission  // 권한
5. share       // 공유
6. notification // 푸시 알림
7. system      // 시스템
```

---

#### Step 2: 액션 정의

**각 카테고리별 액션 나열:**

```typescript
// auth 카테고리
auth: {
  saveToken        // 토큰 저장
  loadToken        // 토큰 조회
  clearToken       // 토큰 삭제
  biometric        // 생체 인증
  checkBiometric   // 생체 인증 가능 여부
}

// media 카테고리
media: {
  openCamera       // 카메라 열기
  selectPhoto      // 사진 선택
  selectVideo      // 동영상 선택
  recordVideo      // 동영상 녹화
}

// permission 카테고리
permission: {
  request          // 권한 요청 (payload에 scopes)
  check            // 권한 확인
  openSettings     // 설정 앱 열기
}

// location 카테고리
location: {
  getCurrent       // 현재 위치 조회
  startTracking    // 위치 추적 시작
  stopTracking     // 위치 추적 종료
}

// system 카테고리
system: {
  getVersion       // 앱 버전
  getDeviceInfo    // 디바이스 정보
  restart          // 앱 재시작
  clearCache       // 캐시 삭제
  checkNetwork     // 네트워크 상태
}

// external 카테고리
external: {
  openURL          // 브라우저 열기
  callPhone        // 전화 걸기
  sendSMS          // 문자 보내기
  sendEmail        // 이메일 보내기
}
```

---

#### Step 3: 메시지 인터페이스 정의

```typescript
// src/webview/types.ts

// 웹 → 앱
export interface WebMessage {
  category: string;
  action: string;
  payload?: any;
  reqId?: string;
}

// 앱 → 웹
export interface AppResponse {
  category: string;
  action: string;
  success: boolean;
  data?: any;
  error?: string;
  reqId?: string;
}

// 카테고리 타입 (안전성)
export type MessageCategory =
  | 'auth'
  | 'media'
  | 'permission'
  | 'location'
  | 'system'
  | 'external';

// 액션 타입 (카테고리별)
export type AuthAction =
  | 'saveToken'
  | 'loadToken'
  | 'clearToken'
  | 'biometric'
  | 'checkBiometric';

export type MediaAction =
  | 'openCamera'
  | 'selectPhoto'
  | 'selectVideo'
  | 'recordVideo';

// ... (다른 카테고리도 동일하게)
```

---

### 4. 실전 문서화 (필수!)

#### API 문서 작성 (Markdown)

```markdown
# WebView 통신 API 명세

## auth 카테고리

### saveToken
토큰을 보안 저장소에 저장합니다.

**요청:**
\`\`\`json
{
  "category": "auth",
  "action": "saveToken",
  "payload": {
    "accessToken": "eyJhbGc...",
    "refreshToken": "eyJhbGc..."
  },
  "reqId": "req_123"
}
\`\`\`

**응답 (성공):**
\`\`\`json
{
  "category": "auth",
  "action": "saveToken",
  "success": true,
  "reqId": "req_123"
}
\`\`\`

**응답 (실패):**
\`\`\`json
{
  "category": "auth",
  "action": "saveToken",
  "success": false,
  "error": "Keychain에 저장 실패",
  "reqId": "req_123"
}
\`\`\`

---

### biometric
생체 인증을 요청합니다.

**요청:**
\`\`\`json
{
  "category": "auth",
  "action": "biometric",
  "payload": {
    "reason": "로그인을 위해 생체 인증이 필요합니다"
  },
  "reqId": "req_456"
}
\`\`\`

**응답:**
\`\`\`json
{
  "category": "auth",
  "action": "biometric",
  "success": true,
  "data": {
    "authenticated": true,
    "biometryType": "FaceID"  // or "TouchID", "Fingerprint"
  },
  "reqId": "req_456"
}
\`\`\`

---

## media 카테고리

### openCamera
카메라를 열어 사진을 촬영합니다.

**요청:**
\`\`\`json
{
  "category": "media",
  "action": "openCamera",
  "payload": {
    "quality": 0.8,         // 0.0 ~ 1.0
    "maxWidth": 1920,
    "maxHeight": 1080
  },
  "reqId": "req_789"
}
\`\`\`

**응답 (성공):**
\`\`\`json
{
  "category": "media",
  "action": "openCamera",
  "success": true,
  "data": {
    "uri": "file:///path/to/photo.jpg",
    "width": 1920,
    "height": 1080,
    "fileSize": 524288
  },
  "reqId": "req_789"
}
\`\`\`
```

---

### 5. 네이밍 컨벤션

#### 카테고리 이름

**권장:**
- ✅ 단수형: `auth` (not `auths`)
- ✅ 소문자: `permission` (not `Permission`)
- ✅ 명사: `location`, `media`, `system`
- ✅ 짧고 명확: `auth` > `authentication`

**비권장:**
- ❌ 복수형: `permissions`
- ❌ 대문자: `AUTH`, `Permission`
- ❌ 동사: `authenticate`
- ❌ 축약어: `perm` (명확하지 않음)

---

#### 액션 이름

**권장:**
- ✅ 동사로 시작: `saveToken`, `getLocation`
- ✅ camelCase: `openCamera` (not `open_camera`)
- ✅ 명확한 동사: `save`, `load`, `get`, `set`, `open`, `close`

**비권장:**
- ❌ 명사만: `token` (무슨 액션인지 불명확)
- ❌ snake_case: `save_token`
- ❌ 모호한 동사: `do`, `handle`

**패턴:**
```typescript
// CRUD 패턴
create...   // 생성
read... / get...  // 조회
update... / set...  // 수정
delete... / remove...  // 삭제

// 상태 제어
start...    // 시작
stop...     // 종료
pause...    // 일시정지
resume...   // 재개

// UI 제어
open...     // 열기
close...    // 닫기
show...     // 표시
hide...     // 숨김

// 요청
request...  // 요청
check...    // 확인
verify...   // 검증
```

---

### 6. 확장성 고려 사항

#### 버전 관리

**메시지에 버전 추가:**
```typescript
interface WebMessage {
  category: string;
  action: string;
  version?: string;  // "1.0", "2.0"
  payload?: any;
  reqId?: string;
}
```

**버전별 처리:**
```typescript
export async function handleAuth(action: string, payload: any, version?: string) {
  if (version === '2.0') {
    // 새로운 로직
  } else {
    // 기존 로직 (하위 호환성)
  }
}
```

---

#### Deprecated 액션 처리

```typescript
export async function handleMedia(action: string, payload: any) {
  switch (action) {
    case 'takePhoto':  // @deprecated v2.0부터 openCamera 사용
      console.warn('[Deprecated] takePhoto는 v2.0부터 deprecated. openCamera를 사용하세요.');
      return await handleOpenCamera(payload);

    case 'openCamera':
      return await handleOpenCamera(payload);
  }
}
```

---

### 7. 테스트 가능한 구조

#### 핸들러 테스트

```typescript
// handlers/authHandler.test.ts

import { handleAuth } from './authHandler';
import { saveToken } from '../utils/secureStore';

jest.mock('../utils/secureStore');

describe('handleAuth', () => {
  it('saveToken 액션이 토큰을 저장한다', async () => {
    const mockRef = { current: { postMessage: jest.fn() } };
    const payload = {
      accessToken: 'token123',
      refreshToken: 'refresh456',
    };

    await handleAuth(mockRef, 'saveToken', payload, 'req1');

    expect(saveToken).toHaveBeenCalledWith('token123', 'refresh456');
    expect(mockRef.current.postMessage).toHaveBeenCalledWith(
      expect.stringContaining('"success":true')
    );
  });
});
```

---

## 💡 직접 해보기

### 실습: 내 프로젝트 메시지 구조 설계

#### Step 1: 기능 목록 작성

```
내 프로젝트: [프로젝트명]

필요한 기능:
1. ___________
2. ___________
3. ___________
...
```

#### Step 2: 카테고리 분류

```
카테고리 1: _________
- 기능 A
- 기능 B

카테고리 2: _________
- 기능 C
- 기능 D
```

#### Step 3: types.ts 작성

```typescript
// src/webview/types.ts

export type MessageCategory =
  | '___________'
  | '___________'
  | '___________';

export interface WebMessage {
  category: MessageCategory;
  action: string;
  payload?: any;
  reqId?: string;
}
```

#### Step 4: API 문서 작성

```markdown
# 내 프로젝트 WebView API

## [카테고리명]

### [액션명]
설명...

**요청:**
\`\`\`json
...
\`\`\`

**응답:**
\`\`\`json
...
\`\`\`
```

---

## 🐛 자주 하는 실수

### ❌ 실수 1: 카테고리가 너무 많음

```typescript
❌ 나쁜 예 (15개 카테고리)
category: 'camera' | 'gallery' | 'location' | 'map' |
          'token' | 'biometric' | 'cameraPermission' |
          'locationPermission' | ...

✅ 좋은 예 (6개 카테고리)
category: 'media' | 'location' | 'auth' | 'permission' | 'system'

// camera, gallery → media로 통합
// token, biometric → auth로 통합
// cameraPermission, locationPermission → permission으로 통합
```

### ❌ 실수 2: 액션이 너무 세분화

```typescript
❌ 나쁜 예
'saveFrontCameraPhoto'
'saveBackCameraPhoto'
'saveHighQualityPhoto'
'saveLowQualityPhoto'

✅ 좋은 예
'openCamera'

payload: {
  camera: 'front' | 'back',
  quality: 0.8
}
```

### ❌ 실수 3: 네이밍 일관성 없음

```typescript
❌ 일관성 없음
'getLocation'   // get 동사
'loadToken'     // load 동사
'fetchProfile'  // fetch 동사
→ 모두 조회인데 동사가 다름!

✅ 일관성 있음
'getLocation'
'getToken'
'getProfile'
→ 모두 get으로 통일
```

---

## 🔗 참고 자료

### 관련 문서
- 이전: `RN_WebView_004_onMessage_핸들러_패턴과_설계.md`
- 실전: `RN_Native_001_Native_Module_이해하기.md`

---

## ✅ 체크리스트

- [ ] 프로젝트 기능을 나열했다
- [ ] 비슷한 기능끼리 그룹화했다
- [ ] 5-10개 정도의 카테고리로 정리했다
- [ ] 각 카테고리별 액션을 정의했다
- [ ] 메시지 타입을 TypeScript로 정의했다
- [ ] API 문서를 작성했다 (Markdown)
- [ ] 네이밍 컨벤션을 정했다

---

## 📌 핵심 요약

1. **프로젝트 분석 먼저:** 기능 나열 → 그룹화
2. **카테고리는 5-10개:** 너무 많으면 복잡함
3. **액션 네이밍:** 동사 + camelCase
4. **문서화 필수:** API 명세 작성
5. **확장성 고려:** 버전 관리, deprecated 처리
6. **일관성 유지:** 네이밍 규칙 정하고 지키기

---

**작성일**: 2026-01-07
**난이도**: 🟡 중급
**중요도**: ⭐⭐⭐⭐⭐ (반드시 프로젝트 시작 전에 설계!)
