# 여러가지 접근권한요청

앱을 만들고 테스트를 하다보면

갑작스런 쓰레드에러가 나는 경우가 있다.

UIView를 그리는데 있어 에러가는 경우는 Xcode에서 친절하게 보라색으로 표시해주지만

카메라, 사진첩 등 따로 권한을 요청해야만 하는 경우가 있다.

웹뷰를 사용하는 경우, 웹에서 따로 실행시켜준다면 넘어갈 수 있지만

- 사진을 찍는 경우: 카메라 사용 권한
- 동영상을 찍는 경우: 마이크 사용 권한

위와 같은 내용 뿐만 아니라 정말 다양한 권한들이 있다.

### 세팅방법

info.plist에 내용을 추가 하기만하면 정상작동한다.

<img width="1036" alt="스크린샷 2022-11-17 오후 2 28 29" src="https://user-images.githubusercontent.com/76529148/202377136-15e48782-45de-4d80-b919-d3bc21fe1ee2.png">

### 다양한 접근권한

아래와 같이 다양한 권한이 존재한다.

[애플 문서](https://developer.apple.com/documentation/bundleresources/information_property_list/protected_resources)

- 블루투스 : Privacy - Bluetooth Always Usage Description
- 캘린더 : Privacy - Calendars Usage Description
- 미리알림 : Privacy - Reminders Usage Description
- 카메라 : Privacy - Camera Usage Description
- 마이크 : Privacy - Microphone Usage Description
- 연락처 : Privacy - Contacts Usage Description
- FaceID : Privacy - Face ID Usage Description
- Desktop 폴더 : Privacy - Desktop Folder Usage Description
- Document 폴더 : Privacy - Documents Folder Usage Description
- 네트워크 볼륨파일 : Privacy - Network Volumes Usage Description
- 이동식 볼륩 : Privacy - Removable Volumes Usage Description
- FileProvider도메인 : Privacy - Access to a File Provider Domain Usage Description
- 건강 기록 : Privacy - Health Records Usage Description
- 건강 공유 : Privacy - Health Share Usage Description
- 상태업데이트 : Privacy - Health Update Usage Description
- 위치사용 : Privacy - Location Usage Description
- 위치 항상 사용 및 앱 사용시 사용: Privacy - Location Always and When In Use Usage Description
- 위치 사용 포그라운드에서 앱 사용시 : Privacy - Location When In Use Usage Description
- 위치에 대한 임시 액세스 요청 : Privacy - Location Temporary Usage Description Dictionary
- 미디어 라이브러리 : Privacy - Media Library Usage Description
- 모션 : Privacy - Motion Usage Description
- 로컬 네트워크 : Privacy - Local Network Usage Description
- NFC스캔 : Privacy - NFC Scan Usage Description
- 사진첩에 추가 : Privacy - Photo Library Additions Usage Description
- 사진첩 사용 : Privacy - Tracking Usage Description
- 사용추적 : Privacy - AppleEvents Sending Usage Description
- 시스템관리 : Privacy - System Administration Usage Description
- Siri사용 : Privacy - Siri Usage Description
- 음성인식 : Privacy - Speech Recognition Usage Description
- Video Subscriber계정 : Privacy - Video Subscriber Account Usage Description
- ID 사용 : Privacy - Identity Usage Description
