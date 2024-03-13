# Android Studio 완전삭제


### 터미널 삭제 명령어
> rm -Rf 파일명
> 'rm'은 remove의 약어로, 파일이나 디렉토리를 삭제하는 명령어다.
> 'Rf'의 'R'은 recursive의 약자로, '재귀'라는 뜻이며, 파일을 포함하고 있는 모든 디렉토리를 삭제한다는 뜻이다. 그리고 'f'는 아무 메세지를 보여주지 않고, 무조건 지우는 명령어 이다.

<br><br>

## 📍 어플리케이션 삭제
Andorid Studio 어플리케이션을 삭제하는 명령어

rm -Rf /Applications/Android\ Studio.app


<br><br>

## 📍 환경 설정 삭제
모든 Andorid Studio 관련 환경 설정 삭제
(여기서 * 표시는 그 앞에 있는 문자열로 시작하는 모든 폴더 및 파일임)

rm -Rf ~/Library/Preferences/AndroidStudio*


<br><br>

## 📍 .plist 파일 삭제
Andorid Studio의 프로퍼티 리스트(.plist) 파일 삭제

rm -Rf ~/Library/Preferences/com.google.android.*
애뮬레이터의 프로퍼티 리스트(.plist) 파일 삭제

rm -Rf ~/Library/Preferences/com.android.*

## 📍 플러그인 삭제
Andorid Studio의 플러그인 삭제

rm -Rf ~/Library/Application\ Support/AndroidStudio*

<br><br>

## 📍 로그 삭제
Andorid Studio의 로그 삭제

rm -Rf ~/Library/Logs/AndroidStudio*

<br><br>

## 📍 캐시 삭제
Andorid Studio의 캐시 삭제

rm -Rf ~/Library/Caches/AndroidStudio*

<br><br>

## 📍 이전 버전 삭제
이전 버전의 Andorid Studio 삭제

rm -Rf ~/.AndroidStudio*

<br><br>

## 📍 프로젝트 삭제
모든 안드로이드 프로젝트 삭제

rm -Rf ~/AndroidStudioProjects

<br><br>

## 📍 gradle 관련 파일 삭제
gradle 관련 파일(캐시 or 래퍼) 삭제

rm -Rf ~/.gradle

## 📍 AVD 및 키 저장소 삭제
AVD(가상 장치) 및 키 저장소 삭제

rm -Rf ~/.android

<br><br>

## 📍 SDK 도구 삭제
Android SDK 도구 삭제

rm -Rf ~/Library/Android*

<br><br>

## 📍 인증 토큰 삭제
애뮬레이터 콘솔 인증 토큰 삭제

rm -Rf ~/.emulator_console_auth_token

<br><br>

👏 여기까지 삭제했으면 내 컴퓨터에서 안드로이드 스튜디오와 기타 관련 있는 파일들(설치 시 응용프로그램의 이름을 변경했을 경우 제외)은 지워졌을 것이다.
