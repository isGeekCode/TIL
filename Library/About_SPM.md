# About Swift PackageManager

Xcode11부터 사용가능, Apple에서 공식지원한다.

- 설치과정이 **매우짧음**
- 어떤 오픈소스를 사용하고 있는지 보기 편함
- 아직 지원하지 않는 라이브러리가 많음

## 깃으로 SPM 설치하기

공부날짜: 2022년 5월 24일 오후 4:19

1. 원하는 깃의 브랜치에서 Git 링크를 가져온다.
2. 설치할 Xcode 프로젝트 - Target - General - Frameworks,Libraries, and Embedded Content + 버튼
3. 하단 Add Other - Add Package Dependency

<img width="519" alt="스크린샷_2022-05-24_오후_3 48 23" src="https://user-images.githubusercontent.com/76529148/169972685-974d0107-ec62-4d25-b0da-97fdc328ec89.png">
    
4. 복사해온 깃주소 붙여넣기
    
![스크린샷_2022-05-24_오후_4 14 30](https://user-images.githubusercontent.com/76529148/169972677-5c5ca5a0-7077-48ff-abd2-a34fbf1c57e6.png)
    
5. SPM은 버전, 브랜치, 커밋 ID를 입력해서 특정 버전, 커밋, 브랜치의 라이브러리를 추가를 할 수 있습니다.
    
    브랜치로 관리를 진행하고 있는 경우 브랜치 명을 입력해서 해당 브런치로 라이브러리 추가 가능
    
![스크린샷_2022-05-24_오후_4 17 03](https://user-images.githubusercontent.com/76529148/169972669-00e8652b-6711-4fce-b609-55e5d0ee5daf.png)

추가가 완료가 되면 왼쪽 프로젝트 네비게이터에서 SPM으로 추가한 라이브러리를 확인 할 수 있습니다.

6. 프레임워크 사용방법은 사용하려는 소스파일에서 상단에 import를 통해 사용이 가능

## Pod -> SPM 마이그레이션

SPM을 어떻게 만들었느냐에 따라 달라진다.

### POD 제거
- Podfile을 열고 기존 생성되어있던 문구를 주석처리하거나 지운다.
- 터미널 해당 프로젝트 폴더에서 `pod install`을 입력하면 현재 기입된 정보로 갱신된다. 

### 레거시 코드 제거(생략가능)
굳이 코드를 지울필요가 없는 게 확실하다면 굳이 지울필요는 없지만
빌드 확인을 위해 주석처리는 해야할 필요가 있다.


### SPM 추가
상단 [[깃으로 SPM 설치하기]](#깃으로-SPM-설치하기) 참고

추가하지 않을 경우 `dyld[]: Library not loaded:` 에러가 발생한다. 


### SPM에 대한 코드 세팅
POD과 SPM 내부의 코드가 다를 수 있기 때문에 코드를 확인한다. 

----
여기까지가 보편적인 상황이지만 이 SPM을 생성한 구조에 따라 추가 작업을 진행해야하는 경우가 있다.

## SDK의 bundle 파일을 수동으로 가져와야하는 경우
설계상, SDK의 bundle 파일을 수동으로 가져와야하는 경우가 있다. 
이럴때에는 Build Phases - Copy Bundle Resources 에서 수동으로 추가를 해줘야한다.
그렇지않으면 아래 에러가 발생할 수 있다.

```
Thread 1: "Cannot create an NSPersistentStoreCoordinator with a nil model"
// 번역
스레드 1: "모델이 없는 NSPersistentStoreCoordinator를 만들 수 없습니다."
```

이때 파일을 새로 생성해서 복사하는게 아니라 참조하자. 
추가적으로 아래 항목처럼 다른 타겟에서 추가할경우 copy Bundle에 새로운 파일을 추가하지말고, 기존 추가했던 파일을 클릭하면나오는 우측 패널에서 타겟을 추가하자.

### 추가적인 Target에서 SPM을 추가하는 경우 
한 프로젝트 내에서 해당 라이브러리를 이미 설치한 경우, 이미 설치되어있다는 메세지가 등장할 수 있다.
그런 경우에는 이미 추가된 파일을 직접 추가한다.

상단 [[깃으로 SPM 설치하기]](#깃으로-SPM-설치하기) 에서 

3. 하단 Add Other - Add Package Dependency 이걸 선택하는 것이 아니라  Add files 을 선택한다.

이미 SPM이 추가된 라이브러리라면 프로젝트 네비게이터의 하단에 있는 Package Dependencies (왼쪽 하단) 에 추가된 라이브러리를 볼 수 있다. 이 라이브러리의 폴더위치로 이동해서 xcframework 파일을 갖고 있는 폴더를 찾는다.

Add files 에서는 이 xcframework를 담고 있는 폴더를 추가하면 다시 선택했을 때, 라이브러리 아이콘이 생성된다. 


## History
- 230712 : SPM 수동 번들 가져오기 내용 추가
