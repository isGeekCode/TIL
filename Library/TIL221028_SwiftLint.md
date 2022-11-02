# SwiftLint 세팅하기

다른 개발자와 협업을 하는 경우, 각자 다른 코드 스타일을 가지고 있기 때문에 자칫 가독성을 해칠 수가 있다.

그래서 SwiftLint는 현업에서도 매우 유용한 라이브러리다.

SwiftLint에 대한 내용은 https://github.com/realm/SwiftLint 이곳에 아주 상세하게 나와있다. 심지어 한글도 지원된다.!!

## SwiftLint 설정하기

공식문서를 보면 다양한 설치방법이 소개되어있다.

가장 자주 사용하는 방법은 CocoaPods이나 Brew를 사용할 수 있다.

## CocoaPods

CocoaPods를 사용하면 최신 버전 외에도 SwiftLint의 특정 버전을 설치할 수 있기 때문에 이 방법을 권장한다.

→ Homebrew는 최신 버전만 설치 가능

Podfile에 아래 내용을 추가하고 터미널에서 pod install을 실행한다.

```
pod 'SwiftLint'
```

이를 실행하면 다음번 `pod install` 실행 시 SwiftLint 바이너리 및 `Pods/`에 있는 디펜던시들을 다운로드하고, Script Build Phases에서 `${PODS_ROOT}/SwiftLint/swiftlint` 명령을 사용할 수 있게 된다.

### **프로젝트명 -> TARGETS -> Build Phases -> + 클릭 -> New Run Script Phase**

새로 생긴 Run Script의 이름을 **SwiftLint**로 바꾼다

아래 Script를 작성한다.

<img width="383" alt="스크린샷 2022-10-28 오후 4 36 11" src="https://user-images.githubusercontent.com/76529148/198532399-1f139139-27d6-4095-b3a4-3e9fa011a935.png">

```swift
${PODS_ROOT}/SwiftLint/swiftlint
```

이렇게 했을 때 SwiftLint 바이너리 및 그에 종속된 바이너리들과 스위프트 바이너리까지 `Pods/` 디렉터리에 추가되기 때문에, git 등의 SCM에 이런 디렉터리들을 체크인하는 것은 권장하지 않음.

### 세팅완료

빌드시 SwiftLint에서 어떤 부분이 룰에 어긋나는 지 알려준다.

## Brew

Homebrew는 최신 버전만 설치 가능

터미널에서 brew를 통해 설치한다.

```swift
brew install swiftlint
```

Brew를 통해 설치를 하면 아래와 같은 경고가 뜨게 된다.

```swift
warning: SwiftLint not installed, download from https://github.com/realm/SwiftLint
```

HomeBrew를 통해 설치하는 경우 바이너리들을 brew의 경로에 저장한다. `/opt/homebrew/bin`
그렇기때문에 SwiftLint가 어디 있는지 찾는 것을 Xcode에 알려주기 위해, build phase에서 `/opt/homebrew/bin`
를 `PATH` 환경 변수에 동시에 추가하여야 한다.

### **프로젝트명 -> TARGETS -> Build Phases -> + 클릭 -> New Run Script Phase**

새로 생긴 Run Script의 이름을 **SwiftLint**로 바꾼다

아래 Script를 작성한다.

```swift
export PATH="$PATH:/opt/homebrew/bin"
if which swiftlint > /dev/null; then
  swiftlint
else
  echo "warning: SwiftLint not installed, download from https://github.com/realm/SwiftLint"
fi
```

SwiftLint phase를 'Compile Sources' 단계 직전으로 옮겨 컴파일 전에 에러를 빠르게 찾고 싶어 할 것이다. 하지만, SwiftLint는 컴파일러의 구문 분석 단계를 완벽히 수행하는 유효한 Swift 코드를 실행하기 위해 설계되었다. 따라서, 'Compile Sources' 전에 SwiftLint를 실행하면 일부 부정확한 오류가 발생할 수도 있다

만약 위반 사항(violations)을 자동으로 수정하는 것을 원한다면, 스크립트에 `swiftlint` 대신 `swiftlint --fix && swiftlint`을 적는다. 이는 프로젝트의 수정 가능한 모든 위반 사항들이 수정되고 나머지 위반 사항에 대한 경고가 표시된다는 것을 의미한다.

<img width="518" alt="스크린샷 2022-10-28 오후 4 33 08" src="https://user-images.githubusercontent.com/76529148/198532386-660e8e68-73f5-406c-80b8-58dd7dd34960.png">

오늘처럼 설치를 하면 SwiftLint에서 기본적으로 세팅되어있는 기능만 검사를 하게 된다.
이 외에 내가 원하는 조건을 위해서는 따로 조건을 입력해야하는데 다른 글에서 다시 소개해야겠다.

++++++++++

다음글: [SwiftLint 세팅하기](https://github.com/isGeekCode/TIL/blob/main/Library/TIL221101_SwiftLintCustomRule.md)

---

### GitHooks

GitHook이란 git을 관리할때 특정 상황들을 트리거로 사용자가 규칙을 정할 수 있게 해주는 Git자체기능 중 하나이다.

**주로 사용되는 훅**

- pre-commit : 커밋시 가장 먼저 실행되는 훅
- prepare-commit-msg : 커밋 메세지를 생성하고 편집기 실행전에 실행
- post-merge : Merge가 끝나고 실행되는 훅

SwiftLint의 세팅과 연결해 깃 커밋전에 SwiftLint 검사를 하도록 세팅해서 내가 원하는 컨벤션만 깃에 저장될 수 있도록 설정 할 수 있다.
