# Flutter - Installation

## 필요한 것들
- Android Studio
- Xcode
- Chrome
- VSCode
- VSCode Extension - Flutter
- Flutter SDK



# M1기준

## 안드로이드 스튜디오 설치

M1여부를 꼭 확인해서 다운로드할 것
[사이트링크](https://developer.android.com/studio)


- Flutter를 Install
- 설치 중간에 Dart 플러그인이 필요하다고한다.
- Install한다.

- 설치가 완료되면 새로 생긴 Restart IDE 버튼을 눌러 안드로이드 스튜디오 프로그램을 재시작
- 잘 됐다면 프로젝트 생성에서 플러터 프로젝터로 생성가능해진다.


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
export PATH="$PATH:~/Downloads/flutter/bin"
```
- source ~/.zshrc
- 터미널 재시작
반영이 잘됐다면 이제 flutter 라고 쓰면 인식이 될거다.

- flutter doctor 입력후 상태 확인

## VSCode Flutter
- extension 플러터 설치




# Intel 기준

## 안드로이드 스튜디오 설치

Intel 여부를 꼭 확인해서 다운로드할 것
[사이트링크](https://developer.android.com/studio)
[참고링크](https://space-engineers-developer.tistory.com/10)


- Flutter를 Install
- 설치 중간에 Dart 플러그인이 필요하다고한다.
- Install한다.

- 설치가 완료되면 새로 생긴 Restart IDE 버튼을 눌러 안드로이드 스튜디오 프로그램을 재시작
- 잘 됐다면 프로젝트 생성에서 플러터 프로젝터로 생성가능해진다.

<br><br>


## 플러터 SDK 설치
[사이트링크](https://docs.flutter.dev/get-started/install/macos)
- Intel 클릭 및 다운로드
- 터미널을 열고 다운로드 받은 폴더로 이동 (Downloads 폴더 권장)
- pc내에 development(권장) 폴더를 생성하여 해당 폴더로 이동처리
- development 디렉토리로 이동하여 압축해제

```
cd ~/development

unzip flutter_macos_3.16.5-stable.zip
```

### 경로 설정
- 현재 사용중인 셸 확인
- vim 에디터로 실행
```
vim ~/.zshrc
export PATH="$PATH:/Users/나의폴더명/flutter/bin"

source ~/.zshrc
```
- 설치된 경로가 잡히는지 버전체크
```
flutter --version
```
- flutter doctor 이용해 나머지 설치여부 확인
어떤것이 설치가 더 필요한지 진단이 나온다. 

<br><br>

## Issue

### Android toolchain
```
[!] Android toolchain - develop for Android devices (Android SDK version 32.0.0)
    ✗ cmdline-tools component is missing
      Run `path/to/sdkmanager --install "cmdline-tools;latest"`
      See https://developer.android.com/studio/command-line for more details.
```
 
- SDK Manager 이동
 <img width="500" alt="스크린샷 2024-03-13 오전 10 19 25" src="https://github.com/isGeekCode/TIL/assets/76529148/0cdbd767-e9c1-4f7b-87fc-abe041486005">

- Hide Obsolete Packages 해제
- Android SDK Command-line Tools(latest) 체크 후 설치
  <img width="500" alt="img1 daumcdn-4" src="https://github.com/isGeekCode/TIL/assets/76529148/e38fa7d7-47bd-45b9-a4ae-e746b9752571">  

<br><br>

### Android toolchain - Some Android licenses not accepted
```
flutter doctor --android-licenses
```

위와 같이 입력해도 라이센스에 대한 동의 과정이 진행이 안된다면,  
플러터의 버전과 안드로이드 스튜디오의 버전이 안맞아서 그럴 것이다.  

버전을 맞춰주고, 
특별한 일이 없다면 둘다 최신화 하면 바로 해결된다.  


