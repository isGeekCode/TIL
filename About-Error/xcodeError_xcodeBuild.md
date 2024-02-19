# Xcode Error - xcode-select: error: tool 'xcodebuild' requires Xcode



## 에러내용
```
xcode-select: error: tool 'xcodebuild' requires Xcode, but active developer directory '/Library/Developer/CommandLineTools' is a command line tools instance

```
xcode-select 명령어를 실행하려고 하는데 active developer directory의 Command Line Tool을 찾을 수 없다는 말이다.  




## 해결방법

```
sudo xcode-select -s /Applications/Xcode.app/Contents/Developer
```

Applications 폴더에 있는 Xcode를 잡아서 내부 Command Line Tool을 실행시키는 방법이다.  

만약, 별도의 command Line Tool을 다운받아 사용하는거라면 해당 폴더를 잡아야한다.  



