# Xcode - 빌드된 app파일은 어디에 있을까

## 생성된 앱은 뭐가 다를까



## app 파일 찾기
Xcode에서 빌드한 앱들의 정보는 아래 경로에서 찾을 수 있다.

```
/Users/{User Name}/Library/Developer/Xcode/DerivedData/{your app}/Build/Products/Debug-iphonesimulator
```

이때 Products 안에는 다양한 폴더가 생성되어있다.
- Debug-iphoneos
- Debug-iphonesimulator
- Release-iphoneos
- Release-iphonesimulator

이런 식으로 빌드한 종류에 따라 다르게 생성된다.  



DerivedData 폴더를 찾기 힘들다면

- Xcode의 Settings `⌘ + ,`
- Locations탭 - DerivedData - 하단 경로의 화살표

위 방법으로 찾아갈 수 있다.

<br><br>

## `.app`파일 열기

해당 폴더에 들어가보면 `[app이름].app` 파일과 `[app이름].swiftmodule` 파일이 있는데
그중 .app 파일의 마우스 오른쪽클릭하여 `패키지 내용 보기`를 클릭하면 내부 정보를 탐색하는 것이 가능하다.   

<br><br>

## HISTORY
- 231010: 초안작성
