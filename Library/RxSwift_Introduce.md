# ReactiveX: RxSwift Introduce


ReactiveX는 원래 MS에서 만들었다.

흐름을 마블로 표현한다.

<img width="854" alt="스크린샷 2022-12-06 오후 3 46 23" src="https://user-images.githubusercontent.com/76529148/208298562-fa7fa723-0b76-4ee7-acd9-c0f2d144227e.png">


[https://reactivex.io/intro.html](https://reactivex.io/intro.html)

## Docs

주요기능을 가진 다섯가지요소가 있다.

- Observable
- Operators
- Single
- Subject
- Scheduler

## RxSwift는

- Observable을 알면 다 사용할 수 있다.
- Operators를 알면 더 잘 쓸수 있다.
- Scheduler를 알면 여러 군데 활용이 가능하다
- Subject를 알면 뭔가를 만들 수 있다.

→Single은…. 알면좋고 몰라도 상관없다…

### Language 지원

Language를 대부분 지원해서
RxSwift를 사용할 줄 알면 대부분 응용이 가능하다.

Docs는 한국어 지원이 되어서 쉽게 확인이 가능하다

# 설치

### Pod

```swift
// Podfile

target 'RxSwiftIn4Hours' do
  # Comment the next line if you're not using Swift and don't want to use dynamic frameworks
  use_frameworks!

  # Pods for AppName
  
  pod 'RxSwift'

end
```

## Observable

Observable 한국어 Docs

[https://reactivex.io/documentation/ko/observable.html](https://reactivex.io/documentation/ko/observable.html)

ReactiveX에서 옵저버는 Observable을 구독한다.

### 동기와 비동기

[https://github.com/isGeekCode/TIL/blob/main/ComputerScience/synchronous_Asynchronous.md](https://github.com/isGeekCode/TIL/blob/main/ComputerScience/synchronous_Asynchronous.md)

Sync가 동기이고 Async가 비동기이다. 

DispatchQueue에는 2가지 2가지가 있다.

- SerialQueue(직렬큐)
- Concurrent Queue (동시큐)

DispatchQueue.global() → Concurrency이다. → 동시에 수행

ConcurrencyQueue 

- ConcurrencySync
- ConcurrencyAsync

SerialQueue

- SerialSync
- SerialAsync

비동기처리하는 과정은 생각보다 번거로워서 여러 Utility들을 사용한다. 

- Promise
- Bolts
- RxSwift
