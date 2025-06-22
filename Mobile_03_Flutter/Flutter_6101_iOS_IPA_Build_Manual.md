# Flutter-iOS 릴리즈 빌드 및 .ipa 수동 생성 가이드

이 문서는 Flutter 프로젝트에서 `fvm`을 사용하여 iOS용 `.ipa` 파일을 수동으로 생성하는 절차를 설명합니다.


<br><br>

---

## 🎯 목적

Flutter iOS 앱을 실기기 테스트 또는 Apple Configurator 배포를 위해 `.ipa` 파일로 포장하는 수동 방법을 정리합니다.


<br><br>

---

## 🛠️ 전제 조건

- Flutter 및 fvm 설치 완료
- iOS 개발 환경 설정 완료 (Xcode, 개발자 계정 등)
- `Runner.xcworkspace` 기준 프로젝트
- 연결된 실기기 혹은 `.ipa` 파일 설치 툴 (Apple Configurator 등)


<br><br>

---

## 🔧 빌드 및 패키징 절차

### 1. 릴리즈 빌드 수행

```bash
fvm flutter build ios --release
```

- 결과: `build/ios/iphoneos/Runner.app` 생성

### 2. `.ipa` 파일 수동 생성

```bash
cd build/ios/iphoneos
mkdir Payload
cp -r Runner.app Payload/
zip -r Runner.ipa Payload
```

- `Payload/Runner.app` 구조는 Apple이 요구하는 `.ipa` 포맷
- 압축 결과물인 `Runner.ipa` 파일이 실기기 설치용으로 사용됨


<br><br>

---

## 📱 설치 방법 예시

### ▸ Apple Configurator 사용
1. `.ipa` 파일을 Apple Configurator로 열기
2. USB로 연결된 iPhone에 드래그 앤 드롭

### ▸ Xcode > Devices and Simulators
- `.ipa` 파일을 기기 이름 위에 드래그하여 설치 가능


<br><br>

---

## ⚠️ 유의사항

- `Runner.app`에 서명 포함 여부 확인
  - `embedded.mobileprovision` 파일 포함 필수
- 서명되지 않았거나, UDID가 provisioning profile에 포함되지 않으면 설치 불가
- 테스트 기기에서 “신뢰되지 않은 개발자” 경고 발생 시 설정에서 수동 승인 필요

<br><br>

---

## HISTORY
- 260623: 초안작성
