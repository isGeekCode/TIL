# XCFramework 생성하기


## 프로젝트 생성하기

프로젝트 생성하기 - Framework 를 선택한다.

<img width="600" alt="스크린샷 2024-02-19 오후 3 43 13" src="https://github.com/isGeekCode/TIL/assets/76529148/38bad105-7cb2-4e1a-85ad-eaacba0a965d">


<br><br>

## Swift파일 생성 및 프레임워크 구현
swift파일을 생성하고, 사용할 내부 클래스 및 메서드를 구현한다.    

작성시에는 class 혹은 func의 접근제한자를 public 또는 open으로 사용해야 외부에서 사용이 가능하다.  

<img width="600" alt="스크린샷 2024-02-19 오후 1 58 17" src="https://github.com/isGeekCode/TIL/assets/76529148/f4e72282-f90c-4978-83de-e2b0d2420c4c">


<br><br>

## Build Setting 변경

1. Build Options - Build Libraries for Distribution=YES
2. Deployment - Skip install=NO

> ‼️ 주의할 점: 여기에 최소버전을 반드시 확인하자. 나중에 적용한 후, 빌드시 에러가 발생한다.  

<br><br>

## Archive 생성하기

이제 생성한 프로젝트파일을 아카이브 할 차례다.  

터미널을 켜고,  프로젝트 파일이 담긴 폴더로 이동시킨다.  

아래 순서를 따라 xcodebuild 명령어를 통해 아래 과정을 진행한다.  
제시된 명령어에서 TestFrameworkA라고 명시된 부분은 프로젝트이름이니 변경해서 사용하자.  

- iOS Archive
- iOS Simulator Archive
- XCFramework 생성


아카이브를 성공하면 `** ARCHIVE SUCCEEDED **` 메세지를 출력한다.  

이 때, command line tool의 경로를 잘 못 잡아 아래 에러가 발생할 수 있다.

에러가 발생한다면 간단히 해결할 수 있으니 확인할 것.
[xcode-select: error: tool 'xcodebuild' requires Xcode](https://github.com/isGeekCode/TIL/blob/main/About-Error/xcodeError_xcodeBuild.md)


### iOS Archive 생성

```
xcodebuild archive\
 -project TestFrameworkA.xcodeproj\
 -scheme TestFrameworkA\
 -configuration Release\
 -sdk iphoneos\
 -destination 'generic/platform=iOS'\
 -archivePath ./build/TestFrameworkA.framework-iphoneos.xcarchive
```

<br><br>

### iOS Simulator Archive 생성

```
xcodebuild archive\
 -project TestFrameworkA.xcodeproj\
 -scheme TestFrameworkA\
 -configuration Release\
 -sdk iphonesimulator\
 -destination 'generic/platform=iOS Simulator'\
 -archivePath ./build/TestFrameworkA.framework-iphonesimulator.xcarchive
```

<br><br>

### XCFramework 생성하기
```
xcrun xcodebuild -create-xcframework \
-framework './build/TestFrameworkA.framework-iphoneos.xcarchive/Products/Library/Frameworks/TestFrameworkA.framework' \
-framework './build/TestFrameworkA.framework-iphonesimulator.xcarchive/Products/Library/Frameworks/TestFrameworkA.framework' \
-output './build/TestFrameworkA.xcframework'
```

성공한다면 `xcframework successfully written out to:<경로>` 메세지를 출력한다.  

<br><br>

해당 폴더로 가보자.  아래 그림과 같이 build 폴더 안에  위에서 명령어로 생성한 xcarchive 2개, xcframework 파일이 존재한다.  

- 빨강색 : 생성된 파일들 (xcarchive 2개, xcframework)
- 초록색 : 사용할 xcframework

<img width="600" alt="스크린샷 2024-02-20 오전 8 56 51" src="https://github.com/isGeekCode/TIL/assets/76529148/7d4b7455-c1c8-4f19-a4f1-f51c65f0fffe">


여기서 생성한 TestFrameworkA.xcframework을 확인할 수 있다.

마치 폴더처럼 보인다.   

이 파일이 우리가 사용할 프레임워크파일이다.  


<br><br>

## 생성한 XCFramework 적용하기

### 적용할 앱 준비하기

여기서는 TestApp 이라는 앱을 준비했다.  

<br><br>

### 프로젝트에 생성한 xcframework를 추가

앞서 준비한 xcframework파일을 내부 프로젝트로 넣어준다. 

framework폴더를 따로 생성해서 명시해주자.  

복사할 때, Copy items if needed를 체크해야하는 데,  

직접 테스트해보니 복사를 하는데 

Copy items if needed 여부를 항상 보여주지 않고 참조타입으로 추가가 되는 상황이 발생했다.   

이럴 땐, 아래와 같이 해결해볼 수 있다.  
- Finder로 프로젝트 폴더에 먼저 xcframework파일을 복제해 넣는다.
- 이미 내 프로젝트 폴더에 있는 파일을 Xcode내에 드래그한다. (이러면 인식한다.)
- 여기서 Copy items if needed를 체크하든 안하든 동일한 결과가 발생한다. (이미 내 폴더에 있는 걸 추가했기 때문)

카피가 완료되면 아래 그림과 같이 보여진다.  

> 참고로 xcframework파일은 파랑색, 일반 framework는 노랑색이다. 

<br>

<img width="500" alt="스크린샷 2024-02-19 오후 2 53 58" src="https://github.com/isGeekCode/TIL/assets/76529148/b0af4ad7-c5bf-4655-b679-05c39841a6e1">


<br><br>

## 타겟 - General Setting

앱 타겟을 누르고 General 탭 하단의 Frameworks, Libraries, and embeded Content에 추가된 

Embed 상태를 Embed & Sign 으로 되어있는지 확인한다.  

> 이 부분은 다이나믹, 스태틱에 따라 달라질 수 있으니 참고하자. 

<br><br>

## 프레임워크 사용하기
적용한 프로젝트를 import한다.  

그리고 테스트 코드를 적용해 실행해본다.  

<img width="635" alt="스크린샷 2024-02-20 오전 10 00 08" src="https://github.com/isGeekCode/TIL/assets/76529148/18afcd1a-9aa1-4f10-88c4-10d85058d7b1">

