# XCode - 전처리문 사용하기

전처리문이란 코드를 빌드하기 전에 컴파일러가 처리하는 명령문이다. 코드를 실행하기 전에 코드의 일부를 수정하거나 제외하는 등의 작업을 수행한다. 이를 통해 코드의 유연성을 높이고, 코드를 효율적으로 관리할 수 있다.

전처리문은 #으로 시작하는 특별한 문법을 사용한다. 코드사이에 이런 문법을 사용하여 여기서부턴 특정 타겟이나 특정빌드 시뮬레이터 에게만 범위를 적용할 수 있다.

그래서 코드의 일부를 무시하거나, 코드를 조건부로 컴파일하거나, 상수를 정의하거나, 헤더 파일을 포함시키는 등의 작업을 수행할 수 있다.

iOS 전처리문은 Objective-C 및 Swift 언어 모두에서 사용될 수 있다. 일반적으로, iOS 전처리문은 빌드 설정 및 환경 변수, 디버그 정보, 로깅 등과 관련된 작업을 수행한다. 

예를 들어, 디버그 모드에서만 실행되는 코드를 작성하기 위해 전처리문을 사용할 수 있다. 또한, 헤더 파일을 포함시켜 코드를 모듈화하거나, 상수를 정의하여 코드의 가독성을 높일 수도 있다.

## Debug 모드에서만 실행되는 코드
```swift
#ifdef DEBUG
    NSLog(@"Debugging mode is enabled.");
#endif
```

## 타겟 세팅하기

1. 프로젝트 설정에서 플래그 추가하기
Xcode에서 프로젝트를 선택하고, Build Settings 탭을 연다. Search Paths 섹션에서 Preprocessor Macros 옵션으로 간다. Preprocessor Macros 옵션을 클릭하면, Debug와 Release 설정에서 각각 다른 전처리문 플래그를 추가할 수 있다.
기본적으로는  Debug 부분에 `DEBUG=1`라고 써있을 것이다. 그래서 위에 있는 **debug모드에서만 실행되는 코드**를 사용할수 있는 것이다.

여기는 달고 싶은 플래그를 다는 곳이다. 만약 COCOAPODS라는 플래그에도 반응하도록 하고 싶다면 뒤에 COCOAPODS=1을 추가한다. 아래와 같이 붙여준다.

```swift
DEBUG=1 COCOAPODS=1
```
그러면 아래와 같이 사용이 가능하다
```swift

#ifdef COCOAPODS
    // COCOAPODS이 정의되어 있을 때 실행되는 코드
#else
    // COCOAPODS이 정의되어 있지 않을 때 실행되는 코드
#endif
```

2. 코드에서 플래그 정의하기
Objective-C 소스 코드에서 직접 플래그를 정의할 수도 있다.
```swift
#define MY_FLAG 1


#ifdef MY_FLAG
    // MY_FLAG가 정의되어 있을 때 실행되는 코드
#else
    // MY_FLAG가 정의되어 있지 않을 때 실행되는 코드
#endif

```


## 시뮬레이터
### Swift
```swift
#if targetEnvironment(simulator)
    // 시뮬레이터 전용 코드 블록
#else
    // 실제 기기 전용 코드 블록
#endif
```
### ObjC
```swift
#if TARGET_OS_SIMULATOR
    // 시뮬레이터 전용 코드 블록
#else
    // 실제 기기 전용 코드 블록
#endif
```
## OS

```swift
#if os(iOS)
    // iOS 전용 코드 블록
#elseif os(macOS)
    // macOS 전용 코드 블록
#else
    // 기타 플랫폼 전용 코드 블록
#endif
```
```swift
```
