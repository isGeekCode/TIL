# 📦 주요 pub 패키지 인덱스

Flutter 실전에서 사용하거나 테스트해본 pub 패키지들을 카테고리별로 정리합니다.  
설정 방식, 사용 이유, 채택 여부 등을 간략히 메모합니다.

---

## 🌐 네트워크

- `http` – 가장 기본적인 HTTP 요청을 지원하는 경량 패키지  
    - https://pub.dev/packages/http
    - BSD License

- `dio` – 요청 인터셉터, 폼데이터, 에러 핸들링 등 고급 기능을 포함한 HTTP 클라이언트  
    - https://pub.dev/packages/dio
    - MIT License
- `retrofit` – REST API 요청을 인터페이스 기반으로 선언적으로 구성할 수 있도록 도와주는 라이브러리
    – retrofit 방식 사용을 위해 필요 
    - https://pub.dev/packages/retrofit 
    - MIT License
- `retrofit_generator` – retrofit 코드 생성을 위한 빌드 타임 코드 생성기  
    – retrofit 방식 사용을 위해 필요 
    - https://pub.dev/packages/retrofit_generator 
    - MIT License
- `build_runner` – 코드 생성 및 빌드 프로세스를 자동화하는 도구  
    – retrofit, json_serializable 코드 생성용 
    – retrofit 방식 사용을 위해 필요  
    - https://pub.dev/packages/build_runner
    - BSD License
- `json_serializable` – JSON과 Dart 객체 간 자동 변환을 지원하는 코드 생성 라이브러리  
    – retrofit 방식 사용을 위해 필요  
    - https://pub.dev/packages/json_serializable
    - BSD License


---

## 🌍 웹뷰

- `webview_flutter` – Flutter 앱 내에서 웹 콘텐츠를 표시하는 공식 웹뷰 플러그인, 커스터마이징 한계로 사용하지 않기로 결정  
- `flutter_inappwebview` – 다양한 기능과 커스텀 옵션을 제공하는 인앱 웹뷰 플러그인, 결제 처리 등 레퍼런스 확인됨. 커스텀 자유로워 채택
    - https://pub.dev/packages/flutter_inappwebview/changelog

---

## 🧼 런처 & 스플래시 설정

- `flutter_native_splash` – 앱 시작 시 표시되는 스플래시 화면을 쉽게 설정할 수 있는 라이브러리  
    – `icons_launcher`와 호환 이슈로 사용하지 않음  
    - https://pub.dev/packages/flutter_native_splash
    - MIT License

- `icons_launcher` – 앱 아이콘 및 런처 아이콘을 자동 생성해주는 도구, 위와 동일한 이유로 제외  
    - https://pub.dev/packages/icons_launcher
    - MIT License
---

## 🏷 앱 식별자 및 구성

- `change_app_package_name` – Android 및 iOS 앱의 패키지명(번들 아이디)을 변경할 수 있게 도와주는 라이브러리  
    - https://pub.dev/packages/change_app_package_name
    - BSD License

---

## 💾 로컬 저장소

- `shared_preferences` – 간단한 key-value 형태로 데이터를 로컬에 저장하고 불러올 수 있는 라이브러리  
    - https://pub.dev/packages/shared_preferences/install
    - BSD License

---

## ✨ 애니메이션

- `lottie` – JSON 기반의 벡터 애니메이션을 Flutter 앱에서 쉽게 재생할 수 있게 해주는 라이브러리  
    - https://pub.dev/packages/lottie/example
    - MIT License


## History
- 250702: 패키지 설명 보완 및 카테고리 정비  
    - 각 pub 패키지에 대해 간단한 기능 설명 추가  
    - `flutter_inappwebview` 채택 이유 명시  
    - `flutter_native_splash`, `icons_launcher` 제외 사유 기록  
    - 문서 전체적으로 정리된 카테고리별 구성 유지
