# Flutter - 세팅하기

## 1. Flutter  환경 세팅

## 1. 1. Flutter 설치
- 1.1.1. Homebrew로 설치하는 방법
- 1.1.2. 수동으로 설치하는 방법
- 1.1.3. FVM으로 설치하는 방법


<br><br>

### 1.1.1. Homebrew로 설치하는 방법

- Step1. brew 설치
- Step2. brew에서 flutter 설치 진행
```
brew install --cask flutter
```

- Step3. 설치 후 세팅은  2. Flutter 세팅에서 진행


<br><br>

### 1.1.2. 수동으로 설치하는 방법
fvm으로 관리하지않는 한, Flutter에서는 공식적으로 이 방법을 추천한다. 
- Step1. [Flutter 공식 사이트](https://flutter.dev/docs/get-started/install/macos)에서 stable버전 다운로드
- Step2. 다운받은 파일을 원하는 위치에 합축해제 (예: `/{원하는 폴더}/flutter`)
- Step3. 환경변수 설정 : .zshrc 또는 .bash_profile에 아래 내용 추가
    - 참고 : Users 를 포함한 전체경로로 설정하지 않는 경우 인식하지 못할 수 있음
    - `export PATH="$PATH:{원하는 폴더}/flutter/bin"`
    - `source .zshrc` 로 반영
- Step4. 설치 확인 : 1.2. 설치 확인 및 관련 세팅 에서 진행

```
$flutter --version

Flutter 3.32.2 • channel stable • https://github.com/flutter/flutter.git
Framework • revision 8defaa71a7 (7 days ago) • 2025-06-04 11:02:51 -0700
Engine • revision 1091508939 (12 days ago) • 2025-05-30 12:17:36 -0700
Tools • Dart 3.8.1 • DevTools 2.45.1
```

<br><br>

###  1.1.3. FVM으로 설치하는 방법

- [FVM 공식 사이트](https://fvm.app/)

2가지 설치방법이 존재
- 독립적 설치(standard)  `공식사이트에선 해당 설치 방법을 권장`
- pub package를 이용한 설치


<br><br>

#### 1.1.3.1. 독립적 설치
```
// 설치하기
brew tap leoafarias/fvm
brew install fvm

// 삭제하기
brew tap leoafarias/fvm
brew remove fvm
```

<br><br>

#### 1.1.3.2. Pub Package를 이용한 설치
해당 방법으로도 설치가 가능하지만 FVM을 이용하여  전역 Flutter 설치를 관리할 계획이라면 독립형으로 설치하여 관리하는 것을 추천.
-  [pub 공식 다운로드 경로](https://pub.dev/packages/fvm)
- 해당 경로에서 
- 설치 후 아래 명령어로 global하게 활성화
```
dart pub global activate fvm
```


## 1.2. 설치 확인 및 관련 세팅
### 1.2.1. Flutter 설치 확인
#### 1.2.1.1. FVM 이외의 설치 환경
-> FVM외의 환경이라면 이미 설치한 버전이 정해져있기 때문에 다운받은 버전으로 설치가 확인되어야 합니다.

```
// 설치된 Flutter의 경로(환경변수)확인
which flutter

// 설치된 Flutter의 버전 확인
flutter --version
```

<br><br>

#### 1.2.1.2. FVM 환경 설치 및 사용
- Step1. 설치할 폴더로 이동
- Step2. 사용가능한 Release 확인
```
fvm release
```
![|300](https://i.imgur.com/EzFDsNj.png)
- Step3. 플러터 SDK  설치
```
// 특정 버전 설치
fvm install 3.32.3

// Stable 채널 사용
fvm install stable
```
- Step4. 해당 버전 적용
📌 반드시 설치 폴더로 이동을 해주세요`프로젝트 환경에서 환경변수 경로가 꼬일 수 있습니다`
```
fvm use 3.32.3
```
- 해당 작업을 진행하면 아래와 같이 폴더가 생성됩니다.
    - Users/사용자 폴더 :  fvm폴더가 생성됩니다.
    - 프로젝트 폴더
        - .fvm : 현재 폴더에서 지정한 심볼릭링크, user fvm 폴더의 해당 SDK를 참조합니다.
        - .fvmrc : 사용할 Flutter 버전을 명시하는 곳
- Step5. 설치 확인
```
fvm flutter --version
```

<br><br>

### 1.2.2. Flutter Doctor
Flutter는 사용하기위한 환경의 세팅 여부를 확인할 수있도록 flutter doctor라는 것을 지원한다. 
```
// 일반 설치
flutter doctor

// fvm 사용한 경우
fvm flutter doctor
```

<br><br>


flutter doctor를 통해 아래 내용을 확인한다.
- Apple 환경 확인 
    - Xcode설치(필수) : 
        - 환경세팅
            - 사용할 xcode 명시
                - `sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer
            - 초기화
                - `sudo xcodebuild -runFirstLaunch`
            - 라이센스 서명
                - `sudo xcodebuild -license`
    -  Cocoa-Pods 설치 (필수)
        - brew, ruby 로 설치 가능(택1)
            - ruby : `sudo gem install cocoapods`
            - brew : `brew install cocoapods`
- Android 환경 확인
    - 안드로이드 스튜디오 설치 (필수)
    - tool chain 설치 (필수)
        - 안드로이드 스튜디오 / SDK Command-line Tools  설치하기
        - 터미널에서 다시 flutter doctor를 진행하면 License 동의가 필요하다는 안내메세지가 나온다. `--android-licenses`명령어로 진행한다. 
            - 해당 부분에서 에러가 발생할 수 있는데 아래와 같은 에러가 발생할 수 있다. 에러메세지에 필요한 내용이 표시된다. 
                - [링크 참고](https://velog.io/@oen/flutter-doctor-%EC%97%90%EB%9F%AC)
                - NDK를 설치 필요  : 안드로이드 스튜디오에서 설치 가능
                - 구버전인경우 jdk를 맞추라는 메세지도 나올 수 있다.  
- 웹브라우저 환경 확인 (필수)
- VSCode 설치 확인


<br><br>

### 1.2.3. IDE 설정 
-  IDE에 Dart / Flutter 설치하기
    - VSCode로 개발하는 경우
        - Extension에서 Flutter만 설치하면 된다.
        - ![|500](https://i.imgur.com/McFGk0x.png)
    - 안드로이드 스튜디오로 개발하는 경우
        - Plugin에서 Flutter를  설치한다. 
        - ![|500](https://i.imgur.com/53mCXhE.png)


<br><br>

VSCode 사용시 추천 확장프로그램
- Awesome Flutter Snippets: 유용한 Flutter 코드 스니펫 제공
- Flutter Widget Snippets: 위젯 코드 생성 지원
- Pubspec Assist: 의존성 관리 도우미
- Error Lens: 인라인 오류 하이라이팅
- Git Lens: Git 통합 향상

<br><br>

## 1.3. Flutter 삭제하기
### 1.3.1. FVM을 사용한 경우
- Step1. 플러터 삭제
```
// 특정 버전 삭제하기
fvm remove 3.32.3
```
- Step2. brew에서 fvm 삭제
```
brew tap leoafarias/fvm
brew remove fvm
```
- Step3. 캐시 삭제
    - Users/사용자 폴더 
        - FVM 폴더 삭제


<br><br>

###  1.3.2. 작업한 IDE에서 삭제하기
- VSCode : 설치한 extension 에서 삭제
- Android Studio : 설치한  PlugIn에서 삭제

<br><br>

## 1.4. 프로젝트 구성
### 1.4.1. 프로젝트 생성
#### 1.4.1.1. 프로젝트 생성하기
기본적인 프로젝트 네이밍은 대문자 및 특수문자를 포함할 수 없습니다. 허용되는 특수문자는 `_`만 가능하기 때문에
소문자로만  혹은 camel case 로 네이밍을 할 수 있습니다. 

##### 터미널을 이용한 생성
```
// 생성
flutter create my_first_app

// 이동
cd my_first_app
```


<br><br>

##### VSCode이용한 생성
`1.2.3. IDE설정`  선행작업 필요

1. Visual Studio Code를 실행합니다.
2. Command Palette(`Ctrl+Shift+P` 또는 `Cmd+Shift+P`)를 열고 “Flutter: New Project”를 입력하고 선택합니다.
3. 프로젝트 이름을 입력합니다 (예: “my_first_app”).
4. 프로젝트를 저장할 디렉토리를 선택합니다.
5. VS Code가 자동으로 새 Flutter 프로젝트를 생성합니다.

<br><br>

##### 안드로이드 스튜디오를 이용한 생성

`1.2.3. IDE설정`  선행작업 필요

1. Android Studio를 실행합니다.
2. “Create New Flutter Project”를 선택합니다.
3. “Flutter Application”을 선택하고 “Next”를 클릭합니다.
4. 프로젝트 이름과 저장 위치, Flutter SDK 경로를 지정하고 “Next”를 클릭합니다.
![|700](https://i.imgur.com/CcxGIup.png)


<br><br>

#### 1.4.1.2. SDK 경로 설정하기 
- FVM 을 사용하는 경우
    - `/{해당 프로젝트 폴더}/.fvm/flutter_sdk`
- 일반 설치인경우
    - `/{해당 프로젝트 폴더}/flutter/bin`

<br><br>

### 1.4.3. 플러터 실행하기
IDE를 사용하는 경우 해당 플러그인이 설치되어있다면 GUI 를 통해 조작이 가능합니다.

최초 정상 실행 성공하면 sample앱인 countapp이 실행됩니다. 

아래 내용은 터미널로 사용하는 방법입니다. 

- 프로젝트 디렉토리에서 다음 명령어를 실행
```
// 연결된 기기나 에뮬레이터에서 앱을 실행 
flutter run
```

여러 기기가 연결되어 있다면, 실행할 기기를 선택하라는 메시지가 표시됩니다.
기기 ID는 `flutter devices` 명령어로 확인할 수 있습니다.

```
// 특정 실기기로 빌드하기
flutter run -d <device_id>

// 웹으로 실행 하기
flutter run -d chrome

// windows
flutter run -d windows

// mac OS
flutter run -d macos

// linux
flutter run -d linux

```


기본적으로 `flutter run` 명령어는 디버그 모드로 앱을 실행합니다. 릴리즈 모드로 실행하려면 다음 명령어를 사용합니다:

```
flutter run --release
```

릴리즈 모드는 디버그 정보가 제거되고 성능이 최적화된 버전입니다.

<br><br>

### 1.4.4. 플러터 빌드하기

개발이 완료된 앱을 배포 가능한 형태로 빌드하려면 다음 명령어를 사용합니다:

Terminal window

```
// Android APK
flutter build apk

// Android App Bundle
flutter build appbundle

// iOS
flutter build ios

// 웹
flutter build web

// macOS
flutter build macos

// linux
flutter build linux
```
