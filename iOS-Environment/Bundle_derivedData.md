# Xcode - 빌드된 app파일은 어디에 있을까

## 생성된 앱은 뭐가 다를까

### embedded.mobileprovision

이 파일은 iOS 앱을 배포하고 실행하기 위해 Apple의 코드 서명 및 인증 프로세스를 관리하는 중요한 파일 중 하나이다.

- 앱의 Bundle ID (Bundle Identifier)
    - 앱의 고유 식별자인 Bundle ID가 포함된다. 이 식별자는 앱 스토어에 등록된 앱을 식별하는 데 사용된다.
- 개발자 및 개발 팀 정보
    - 앱을 개발한 개발자 또는 개발 팀의 정보가 포함된다. 이 정보는 Apple의 개발자 프로그램에 등록한 개발자 또는 팀을 식별한다.
- 디바이스 ID
    - 이 mobileprovision 파일이 허용하는 디바이스의 목록이 포함된다. 이를 통해 앱을 개발 중 또는 Ad Hoc 배포를 통해 특정 디바이스에 설치할 수 있는 디바이스 목록을 지정할 수 있다.
- 앱의 서명 정보
    - 파일에는 앱의 서명 및 인증 정보가 들어있다. 이 정보는 앱이 신뢰할 수 있는 앱으로 간주되도록 하는 데 필요하다.
- 유효 기간
    - mobileprovision 파일에는 앱이 언제까지 실행될 수 있는지에 대한 유효 기간 정보가 포함된다. 개발자 프로필 및 배포 프로필의 경우 기간이 다를 수 있다.
- 권한과 역할: 파일에는 이 mobileprovision을 사용하여 개발자 또는 팀이 어떤 유형의 앱 개발 또는 배포 권한을 가지는지에 대한 정보도 들어있다.

### Nib 파일
Nib파일은 Nextstep Interface Builder 의 약자이다. 
Xib파일은 Xcode Interface Builder 의 약자이다. 

Nib파일은 실제 Xcode에서 개발을 할 때에는 보이지않는 파일인데,
바이너리 파일로 이루어져있다.

실제로 Xcode의 스토리보드 작업을 할때에는 xml파일로 이루어진 Xib파일을 가지고 작업을 한다. 

그리고 앱배포시 Xib파일은 Nib파일로 저장되게 된다. 

### Storyboardc 파일

Xcode에서 작업했던 Storyboard파일은 빌드시 storyboardc 파일로 저장이 된다.

이 파일은 패키지 파일로 되어있고, 이 패키지를 열면 nib파이로가 nib파일을 관리하는 plist파일이 존재한다. 

아래는 

- Main.storyboardc


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
