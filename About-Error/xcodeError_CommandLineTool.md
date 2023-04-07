# Git - command line tools are already installed (사실 git 에러 아님)

## 발견

TIL을 치려고 하는데 `git add .` 을 입력했지만 에러코드가 발생.

깃을 만지는데 왜 xcode어쩌고 하는 에러가 발생하지??

## 원인

MacOS 업데이트 후 아주 높은 확률로 git을 비롯한 다수의 개발 툴들이 다 xcrun 에러를 뱉는다. 이는 각 도구들의 문제가 아닌 `CommandLineTools`를 식별하지 못해 발생한 문제

이렇게 되면 깃 말고도 각종 도구들도 작동하질 않게 된다. 

결국 Xcode 에러라고 봐야하나 Git 에러는 아닌것이다. 

`xcode-select: error: command line tools are already installed, use "Software Update" to install updates`

위 메세지가 나오는 경우는 이미 커맨드 라인 툴이 설치되어있는 상태이다. 

command line tools을 업데이트 하라는 의미인데, 간단하게 터미널을 통해 해당 디렉토리를 완전히 지운 후 재설치할 수 있다.

### CommandLineTool 삭제하기

```swift
sudo rm -rf /Library/Developer/CommandLineTools
```

### 재설치하기

```swift
sudo xcode-select --install
```

위 코드를 입력하면 아래와 같은 메세지가 발생한다.

![image.webp](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/dfb0b7af-0eb9-4a98-bdd9-893b7a9dcbd1/image.webp)

설치를 누르면 사용권 계약을 확인하고 자동으로 설치가 진행된다.

무섭게 긴 소요시간이 뜨지만 의외로 금방 사라진다. 

설치가 완료되면 바로 된다는 사람들이 많았지만 난 바로 되지않았다.

아래 에러가 이어졌다.

# CommandLineTools  권한주기

### **xcode-select: error: tool 'xcodebuild' requires Xcode, but active developer directory '/Library/Developer/CommandLineTools' is a command line tools instance**

Xcode를 커맨드로 빌드하는 과정에서 CommandLineTools를 사용하지 못한다는 에러이다.

터미널에서 다음으로 권한을 준다.

```swift
sudo xcode-select -s /Applications/Xcode.app/Contents/Developer
```

→ 그냥 복붙을 하는 경우 폴더를 잘 인식못하는 경우가 있었다. 

# 레퍼런스

- [https://investechnews.com/2021/06/15/mac-xcode-setup/](https://investechnews.com/2021/06/15/mac-xcode-setup/)
- [https://investechnews.com/2021/06/15/mac-commandlinetools-setup-error/](https://investechnews.com/2021/06/15/mac-commandlinetools-setup-error/)
- [https://drehzr.tistory.com/793](https://drehzr.tistory.com/793)
