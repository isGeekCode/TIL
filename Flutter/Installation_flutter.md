# Flutter - Installation

## M1기준


## 필요한 것들
- Android Studio
- Xcode
- Chrome
- VSCode
- VSCode Extension - Flutter
- Flutter SDK

## 안드로이드 스튜디오 설치

M1여부를 꼭 확인해서 다운로드할 것
[사이트링크](https://developer.android.com/studio)


- Flutter를 Install
- 설치 중간에 Dart 플러그인이 필요하다고한다.
- Install한다.

- 설치가 완료되면 새로 생긴 Restart IDE 버튼을 눌러 안드로이드 스튜디오 프로그램을 재시작


## Xcode

앱스토어에서 검색하여 다운로드

## Chrome, VSCode는 생략

## Flutter SDK 설치
[사이트링크](https://docs.flutter.dev/get-started/install/macos)
- Apple Silicon 클릭 및 다운로드
- 터미널을 열고 다운로드 받은 폴더로 이동
- 다운로드 받은 파일 압축 해제
- 환경변수 추가(기본 쉘을 그대로 쓰는경우 .zshrc
여기에는 다운로드 받은 폴더의 위치를 잘 적어준다. 

```
# flutter용 환경변수
export PATH=$PATH:~/Downloads/flutter/bin
```
- source ~/.zshrc
- 터미널 재시작
반영이 잘됐다면 이제 flutter 라고 쓰면 인식이 될거다.

- flutter doctor 입력후 상태 확인

## VSCode Flutter
- extension 플러터 설치

