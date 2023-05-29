# Terminal Error - xcrun: error: active developer path...

상황
- 평소처럼 깃사용을 위해 git pull을 입력했는데 아래와 같이 나왔다.

```
xcrun: error: active developer path ("/Applications/Xcode_13.4.app/Contents/Developer") does not exist
Use `sudo xcode-select --switch path/to/Xcode.app` to specify the Xcode that you wish to use for command line developer tools, or use `xcode-select --install` to install the standalone command line developer tools.
See `man xcode-select` for more details.
```

- 최근 Xcode 13.4에서 Xcode 14로 바꾼게 원인인 것 같다.

## 해결방법
이 에러 메시지는 Xcode 개발 도구를 사용하는 명령줄 도구에서 활성 개발자 경로가 현재 존재하지 않는다는 것을 나타낸다.

즉, Xcode 설치 경로가 변경되었거나 삭제되었을 가능성이 있다.

아래 4가지로 해결이 가능하다.

- Xcode 개발 도구를 설치하기
xcode-select --install

- Xcode의 경로를 다시 설정하기
xcode-select --reset 

- Command Line Tool에서 사용할 Xcode를 지정하기
sudo xcode-select --switch path/to/Xcode.app

- Xcode를 새로 설치하거나 업그레이드한 경우,개발자 경로를 다시 지정하기
sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer 

- [해당 에러 참고 : Git - Command Line Tools are already installed (사실 git 에러 아님)](https://github.com/isGeekCode/TIL/blob/b352734b768db08414617f140e4f6bc07e99e879/Error/xcodeError_CommandLineTool.md)
