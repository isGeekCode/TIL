# 동시성 프로그래밍 : Concurrency 톺아보기


전체적인 맥락은 아래와 같다.  
1. 경유지인 Queue에 대한 설명
    - GCD와 Operation
2. 출발지에서 경유지인 Queue로 보내는 방법
    - Sync / Async
    - 경유지 Queue의 종류와 성질
3. 경유지 Queue에서 Thread로 분배하는 방법
    - Serial / Concurrent


## 스레드와 Queue

회사를 예를 들어 보자.  

노동자 = Thread  
일 = Task  
노동자 1 = Main Thread(Thread1)    
노동자 2 = Thread2  
...  

아래처럼 Main Thread에 업무가 전부 집중되어있다고 생각해보자.  
다른 Thread는 놀고있는게 포인트!!  

<br><br>

- Main Thread(Thread1)
    - Task1 : 단순연산
    - Task2 : 네트워킹(이미지 다운로드)
    - Task3 : print
    - Task4 : 시간이 오래걸리는 작업
- Thread2
- Thread3

<br><br>

//TODO
UI는 왜 메인스레드에서 다뤄야만 하는가? 는 뒤에서 설명

<br><br>

### UI그리기도 바쁜데 왜 task를 다 주는가?  
코드작성 시 별도의 처리를 안했다면 Task는 전부 Main Thread에서 처리를 하게 된다.  
 
즉, 별도의 처리를 안한다면 잉여 스레드가 많이 생기고 Main Thread가 과부하가 발생한다.  

메인 스레드에 몰린 작업들을 다른 스레드에서도 동시에 작업 하도록 하는 것! 이게 동시성 프로그래밍이다.  



iOS에서는 다행히도 작업을 한 곳에 보내기만 하면된다. 
그러면 알아서 OS가 다른 스레드로 분산처리를 해준다.  

보내지는 그 한 곳이 바로 Queue(대기행렬)다.  

그래서 이제 우리가 해야할 것은 task를 Queue에 넣는 것이다.  

Queue의 특성은 선입선출이다.  

<br><br>

## GCD (Grand Central Dispatch)

GCD는 우리가 Queue에 작업을 보내면 그에 따른 스레드를 적절히 생성해서 분배해주는 첫번째 방법이다.

GCD에서 사용하는 Queue의 이름이 바로 DispatchQueue다. 

과정을 설명하자면,

DispatchQueue에 작업을 추가하면 GCD는 작업에 맞는 스레드를 자동으로 생성해서 실행하고, 작업이 종료되면 스레드를 제거하게 된다.  

Dispatch라는 단어의 사전적 의미는 아래와 같다.  
- 1.(특별한 목적을 위해)보내다
- 2. 파견, 발송

DispatchQueue로 보내는 방법은 아래 코드와 같다.  
```swift
DispatchQueue.global().async {
  // Task
  print("Task1 시작")
  print("Task1 의 중간작업 1")
  print("Task1 의 중간작업 2")
  print("Task1 종료")
}
```

<br><br>

코드에 나오는 부분을 설명하자면 
- DispatchQueue : iOS에서 동시성 프로그래밍을 돕기위해 제공하는 Queue
- global : DispatchQueue의 한 종류
- async : 비동기

그렇다면 문장으로 해석해 보면, 이런 느낌의 명령이라는 걸 알 수 있다.   
`Global`-`DispatchQueue`에 `비동기`로 `Task`를 보낸다.  


<br><br>

## Operation 
앞서서 우리가 Queue에 작업을 보내면 그에 따른 스레드를 적절히 생성해서 분배해주는 첫번째 방법이 GCD라고 소개했다.  

Operation도 비슷한 기능을 한다.  
Operation에 사용하는 Queue의 이름은 Operation Queue라고 부른다.  

Operation도 내부적으론 GCD 위에서 동작하지만 기능이 더 추가된 형태다.  

- 동시에 실행할 수 있는 동작의 최대 수 지정하기
- 동작 일시중지 및 취소하기

이게 더 기능이 많고 좋아보이지만, 구현하기가 더 복잡하다.  

그렇기 때문에 상황에 따라 적합한 걸 사용하면 된다.  

그러면 지금까지 배운 Queue의 종류는 두가지다. 
- Dispatch Queue
- Operation Queue

<br><br>

# Sync와 Async
앞에서 보내질 `경유지`인 Queue에 대해서 설명했는데 이번엔 보내는 방법에 대해 알아보자.  

앞에서 설명한 바로는,  
Task들을 Queue로 보내기만 하면 GCD에서 알아서 분배한다고 한다.  
아래와 같이 Task가 Main Thread에 쏠려있다고 가정해보자. 

- Main Thread(Thread1)
    - Task1 : 단순연산
    - Task2 : 네트워킹(이미지 다운로드)
    - Task3 : print
    - Task4 : 시간이 오래 걸리는 작업
- Thread2
- Thread3

<br><br>

여기에서 Task1을 DispatchQueue에 보낸다고 했을 때,

Queue로 Task를 보낸 직후의 Main Thread의 행동은 두가지로 나뉘어 진다.  
- 1번 : 바로 쌓여있는 다음 일을 한다.  
- 2번 : Dispatch Queue에 보낸 일이 끝날때까지 기다린 후, 쌓여있는 다음 일을 한다.  

이게 비동기와 동기의 개념이다.  

<br><br>

## Async

1번 행동이 비동기의 개념이다.  
보낸 Task에 걸릴 시간동안 또 다른일을 하게 된다.  

위에서 본 코드가 바로 이 동작이다.  
```swift
DispatchQueue.global().async {
  // Task
}
```

<br><br>

코드에 나오는 부분을 다시 설명하자면 
- DispatchQueue : iOS에서 동시성 프로그래밍을 돕기위해 제공하는 Queue
- global : DispatchQueue의 한 종류
- async : 비동기


그렇다면 문장으로 해석해 보면, 이런 느낌의 명령이라는 걸 알 수 있다.   
`Global`-`DispatchQueue`에 `비동기`로 `Task`를 보낸다.  


다시 이 작업을 정리해서 말하면, 이런 의미가 될 수 있다.  
> 원래 작업이 진행되고 있던 Main Thread에서
> Global DispatchQueue로 Task를 보낸후,  
> 해당 작업이 끝나길 기다리지않고 바로 다음 Task를 이어서 진행한다. 
  
  
그러면 이런 작업이 있다고 생각해보자.  

- Task1 : 1초 걸리는 작업
- Task2 : 2초 걸리는 작업
- Task3 : 3초 걸리는 작업

이걸 메인 스레드에서 혼자 처리하게 되면  
아마 최소 6초는 걸릴 것이라 예상할 수 있겠다.  


이 업무를 코드라인로 정의해보자.  
<br><br>

```swift
// Task1: 1초 동안 지연되는 작업
func task1() {
    print("Task 1 시작")
    Thread.sleep(forTimeInterval: 1)  // 1초 대기
    print("Task 1 완료")
}

// Task2: 2초 동안 지연되는 작업
func task2() {
    print("Task 2 시작")
    Thread.sleep(forTimeInterval: 2)  // 2초 대기
    print("Task 2 완료")
}

// Task3: 3초 동안 지연되는 작업
func task3() {
    print("Task 3 시작")
    Thread.sleep(forTimeInterval: 3)  // 3초 대기
    print("Task 3 완료")
}
```

이걸 실행한다 했을 때, 이렇게 표현할 수 있다.  

```swift
// 전역 DispatchQueue를 사용하여 작업을 비동기적으로 실행
let queue = DispatchQueue.global()

queue.async {
    task1()
}

queue.async {
    task2()
}

queue.async {
    task3()
}
```

이러면 Main Thread에서는 첫번째 코드라인(task1)을 실행하고,  
바로 두번째 코드라인인 task2를 실행시키면서 계속해서 넘어가게 된다.  
그러면 결론적으로 DispatchQueue로 보내버리는데 드는 시간은   
6초가 아닌 0.00044초 정도로 메인스레드의 업무가 종료된다.  

<br><br>

로그를 찍어보자.  
```swift
// 전역 DispatchQueue를 사용하여 작업을 비동기적으로 실행
let queue = DispatchQueue.global()

print("DispatchQueue로 Task1 보내기")
queue.async {
    task1()
}
print("DispatchQueue로 Task2 보내기")

queue.async {
    task2()
}
print("DispatchQueue로 Task3 보내기")

queue.async {
    task3()
}
print("DispatchQueue로 보내기 완료")

```

<br><br>
그러면 로그가 경우에 따라 다른 순서로 나오는 걸 볼 수 있다.  

```
DispatchQueue로 Task1 보내기
DispatchQueue로 Task2 보내기
DispatchQueue로 Task3 보내기
DispatchQueue로 보내기 완료
Task 1 시작
Task 2 시작
Task 3 시작
Task 1 완료
Task 2 완료
Task 3 완료
```

또다른 경우로 이렇게도 찍힌다.

```
DispatchQueue로 Task1 보내기
DispatchQueue로 Task2 보내기
Task 1 시작
DispatchQueue로 Task3 보내기
DispatchQueue로 보내기 완료
Task 2 시작
Task 3 시작
Task 1 완료
Task 2 완료
Task 3 완료
```

그렇다는건 DispatchQueue로 보내는 것 까진 순차적으로 보내더라도,  
보내진 클로저 내부의 Task가 언제 시작하고 언제 끝나는지는   
그 각각의 스레드에 달렸다는 것이다.   

그리고 Swift에서는 이 Task가 끝나는 시점은 Completion 혹은 Completion Handler를 통해 알 수 있다.  

<br><br>

## Sync

- 1번 : 바로 쌓여있는 다음 일을 한다.  ->>> `비동기`
- 2번 : Dispatch Queue에 보낸 일이 끝날때까지 기다린 후, 쌓여있는 다음 일을 한다.  

아까 정의된 Main Thread의 행동 유형중 나머지 하나는 `동기`다. 

어떤 작업을 Queue로 보내고 다음일을 실행하는 비동기`Async`와는 달리  
동기`Sync`는 Queue에 보낸 작업이 완료될 때까지 기다린 후,  
다음 줄로 넘어간다.  

이걸 코드로 보면 아래와 같다.  

```swift
DispatchQueue.global().sync {
  // task
}
```

<br><br>

이걸 다시 해석하면,
> 원래의 작업이 진행되고 있던 메인스레드에서  
> global Dispatch Queue로 task를 보내고 난후,   
> 다음 코드라인 실행을 위해 해당 작업이 끝나길 기다린다.  

<br><br>

그럼 위에서 정의한 Task를 동기적으로 실행되도록 구현해보자.   

```swift
// Task1: 1초 동안 지연되는 작업
func task1() {
    print("Task 1 시작")
    Thread.sleep(forTimeInterval: 1)  // 1초 대기
    print("Task 1 완료")
}

// Task2: 2초 동안 지연되는 작업
func task2() {
    print("Task 2 시작")
    Thread.sleep(forTimeInterval: 2)  // 2초 대기
    print("Task 2 완료")
}

// Task3: 3초 동안 지연되는 작업
func task3() {
    print("Task 3 시작")
    Thread.sleep(forTimeInterval: 3)  // 3초 대기
    print("Task 3 완료")
}


// 전역 DispatchQueue를 사용하여 작업을 비동기적으로 실행
let queue = DispatchQueue.global()

print("DispatchQueue로 Task1 보내기")
queue.sync {
    task1()
}

print("DispatchQueue로 Task2 보내기")
queue.sync {
    task2()
}

print("DispatchQueue로 Task3 보내기")
queue.sync {
    task3()
}
print("모든 작업 완료")
```

<br><br>

이 작업에 대한 로그는 아래와 같다.  

```swift
DispatchQueue로 Task1 보내기
Task 1 시작
Task 1 완료
DispatchQueue로 Task2 보내기
Task 2 시작
Task 2 완료
DispatchQueue로 Task3 보내기
Task 3 시작
Task 3 완료
모든 작업 완료
```

이것이 동기처리과정이다.   

기껏 DispatchQueue로 보내놓고서 왜 기다리는 걸까?  
Main Thread에서 처리하는 거랑 똑같은거 아닌가??? 라는 생각이 들 수 있다.  

맞다. 그래서 동기적으로 보내는 코드를 짜더라도 실질적으로는 Main Thread에서 처리를 한다고 한다.  

<br><br>

### 그렇다면 비동기처리는 왜 필요한가
비동기로 처리할 때 좋은 점은 시간 절약이다.  

시간절약이 가장 많이 드는 작업의 대부분은 서버와의 통신이기 떄문에  
네트워크와 관련된 작업들은 내부적으로 비동기적으로 구현되어있다.  

생각해보면 우리가 따로 네트워킹을 하는데 있어서 `async`를 명시한 적이 없다.  

아래 코드를 보자.  

```swift
URLSession.shared.dataTask(with: request) { (data, response, error) in

}
```

이렇게 URLSession으로 통신을 한다는 것은  
내부적으로는 `다른 스레드 사용 + 비동기 구현`이 되어있는 걸 사용한다는 것이다.  


<br><br>

## Serial / Concurrent


1. 경유지인 Queue에 대한 설명
2. 출발지에서 경유지인 Queue에 보내는 방법 
3. 경유지 Queue에서 Thread로 분배하는 방법

앞선 내용을 살펴보면,
1번과 2번까지 설명했다.  

그리고 이 메서드를 통해 클로저로 task를 Queue로 보냈다.  
```swift
// Task를 global DispatchQueue로 동기적으로 보냄 
DispatchQueue.global().sync { } 

// Task를 global DispatchQueue로 비동기적으로 보냄 
DispatchQueue.global().async { }
```

<br><br>

이제 Queue에는 task들이 쌓이게 되는데 이걸 이제 스레드에 분배해야한다.  

이걸 GCD 혹은 Operation에서 두가지 중 한 방법으로 분배를 하게 된다. 
- 방법1 : 한 개의 스레드에 몰아 넣는다. 
- 방법2 : 여러 개의 스레드에 나눈다.  

이 둘 중 어떤 방식을 선택할 지는 Queue의 특성에 따라 결정된다.  

- Serial : 직렬
    - 만약 Serial Queue라면 (보통 메인스레드에서) 분산처리시킨 작업을 다른 한개의 스레드에서 처리하는 Queue
- Concurrent : 동시
    - 만약 Concurrent Queue라면 (보통 메인스레드에서) 분산처리시킨 작업을 다른 여러개의 스레드에서 처리하는 Queue

<br><br>

### 언제 사용하나요?
그렇다면 언제 Serial, Concurrent Queue를 사용할까?  
분산처리를 하는거면 Concurrent 가 좋지 않을까?  

어떤 Queue를 사용할 것인지에 대한 핵심 포인트는 바로 `작업 순서의 중요도`에 있다. 

- Serial Queue
    - Serial Queue 에 담긴 작업들은 `오직 하나의 스레드`에만 분배된다.  
    - 모든 작업들이 그 전 작업이 끝나길 기다렸다가 하나씩 실행되기 때문에 task의 시작과  종료에 대한 순서 예측이 가능하다.  
- Concurrent Queue
    - Concurrent Queue 에 담긴 작업들은 여러 개의 스레드에 분배된다.  
    - 선입선출이라는 Queue 특성상 순서대로 분배되어 실행되긴하지만 끝나는 순서는 알 수가 없다.  
    

GCD와 관련하여 검색을 해보면 아래 네가지 개념이 주로 나온다.  
- Sync : 동기
- Async : 비동기
- Serial : 직렬
- Concurrent : 병렬(동시)

사실 개념을 살펴봤을 때, 
`Sync / Async` 이렇게 한세트
`Serial / Concurrent` 이렇게 한세트이지만 

뭔가  `serial — sync` , `async — concurrent`
이렇게 연관되어 보일 수 있다.  

비동기(Async)란, 동시(Concurrernt)와 아예 별개의 말이다.  

- Sync / Async : 작업을 보내는 시점에서 기다릴지 말지에 대해 다루는 것
- Serial / Concurrent : Queue(대기열)로 보내진 작업들을 여러 개의 스레드로 보낼지, 한개의 스레드로 보낼 지에 대해 다루는 것

그렇다면 이렇게 네가지 조합이 나올 수 있다.

- SerialQueue.sync
- ConcurrentQueue.sync
- SerialQueue.async
- ConcurrentQueue.async

귀찮지만 전부 설명을 해보자.  

<br><br>

### SerialQueue.sync
- sync : 메인 스레드의 작업 흐름이 queue에 넘긴 태스크가 끝날때까지 멈춰있고,  
- Serial Queue : 넘겨진 task는 queue에 먼저 담겨있던 작업들과 같은 스레드에 보내지기 때문에 해당 작업들이 모두 끝나야 실행 

<br>

### ConcurrentQueue.sync
- sync
    - 메인 스레드의 작업 흐름이 queue에 넘긴 태스크가 끝날때까지 멈춰있고,  
- Concurrent Queue
    - 넘겨진 task는 queue에 먼저 담겨있던 작업들과 다른 스레드에 보내질 수 있기 때문에 해당 작업들이 모두 끝나지 않아도 실행 

<br>

### SerialQueue.async
- async
    - 메인 스레드의 작업 흐름이 태스크를 queue에 넘기자마자 반환되고,  
- Serial Queue
    - 넘겨진 task는 queue에 먼저 담겨있던 작업들과 같은 스레드에 보내지기 때문에 해당 작업들이 모두 끝나야 실행  

<br>

### ConcurrentQueue.async
- async
    - 메인 스레드의 작업 흐름이 태스크를 queue에 넘기자마자 반환되고,  
- Serial Queue
    - 넘겨진 task는 queue에 먼저 담겨있던 작업들과 다른 스레드에 보내질 수 있기 때문에 해당 작업들이 모두 끝나지 않아도 실행 

<br>

이렇게 조합에 따라 이런 동작을 할 수 있게 되는 것이다.  
그렇다면 Serial / Concurrent는 어떻게 결정이 나는 것일까??  
바로 보내진 Queue의 종류에 따라 결정된다.  

<br><br>

# DispatchQueue의 종류
실제로 iOS 에서 제공하는 Dispatch Queue의 종류는 세가지가 있다

- 메인큐
- 글로벌큐
- 커스텀(프라이빗)큐

이 큐의 종류에 따라 특성이 달라지기 때문에  
작업의 특성, 원하는 일 처리에 따라 Queue(대기열)의 특성에 맞게 작업을 넣어야한다.  

아주 간단하게 정리하자면 아래와 같다.  

- 메인큐 : Serial의 특성을 가진 Queue
- 글로벌큐 : Concurrent의 특성을 가진 Queue
- 커스텀(프라이빗)큐 : 디폴트로 Serial 특성을 가진 Queue. 하지만 Concurrent 로 설정 가능

<br><br>

## Main Queue
- 오직 한개만 존재한다.  
- Serial의 특성을 가진 Queue
- 이 곳에 할당된 task들은 메인스레드에서 처리된다.  

앞선 설명중 코드 작성시 별도의 처리를 하지않는 이상 모든 작업은 메인스레드가 작업한다고 했다.  
이 말은 이 task들이 우선 메인 queue에 할당되는 것을 의미한다.  

만약 `print("hello world")`라는 코드가 있다면

```swift
DispatchQueue.main.sync {
    print("hello world")
}

// 이렇게 하면 실제로는 에러가 나긴한다.  
```

이런 식으로 동작한다는 것이다.  

메인 큐의 특성이 Serial이라는걸 이해가 안된다면 아래처럼 이해해보자..

- 메인 큐에서 task는 메인 스레드로만 보냄
- 메인 스레드는 오직 한개 밖에 없음
- 따라서 메인 큐에 있는 task들을 다른 곳에 분산시킬래도 분산 시킬만한데가 없음
- 큐의 특성은 무조건 Serial이 됨 (분산은 Concurrent의 특징)

<br><br>

## Global Queue
- Concurrent 특성을 가진 Queue
- QoS (Quality Of Service)에 따라 여러개의 종류로 나뉨 (6종류)

메인 큐와 달리 Concurrent 특성을 갖고있다.  
그렇다면 여러개의 스레드로 task 를 분산시키니, 작업을 보낼 때 순서가 중요하지않은 것들은 글로벌 큐로 보내면 된다.  

글로벌 큐는 아래와 같이 그냥도 사용할 있고, qos를 지정해 작업의 중요도를 결정할 수도 있다.  
```swift
DispatchQueue.global().async { }

DispatchQueue.global(qos: .utility).async { }
```

<br><br>

그렇다면 QoS의 종류를 살펴보자. 

### QoS의 종류
- userInteractive
- userInitiated
- default
- utility
- background
- unspectified


<br><br>

- userInteractive  
    - 사용자와 직접 상호작용하는 작업
    - `ex. UI업데이트, 애니메이션 등`
    - 사용자의 행동에 대한 즉각적인 반응이 기대되지만, 이를 메인 스레드 에서 처리할 때 많은 로드가 걸리는 작업들을 userInteractive에서 처리해 바로 동작하는 것처럼 보이게 함.


- userInitiated  
    - 클릭할 때 작업을 수행하는 것과 같은 즉각적인 결과가 필요한 작업 
    - `ex. 저장된 문서열기`  
    - 하지만 userInteractive보다는 조금 오래걸릴 수 있고  유저가 어느정도 이를 인지하고 있음

- default  
    - 일반적인 작업

- utility  
    - 보통 progress bar와 함께 길게 실행되는 작업 `ex. 데이터 다운로드`

- background  
    - 유저가 직접적으로 인지하지 않는 시간이 덜 중요한 작업.
    - `ex. 동기화 및 백업`

- unspectified  
    - QoS 정보가 없음을 나타냄. 
    - 거의 사용할 일이 없다.  

<br><br>

이렇게 설정한 qos에 따라 각각의 queue에는 task들이 들어가 있을 것이다.  
  
이런 식으로 구현되어있다고 생각해보자.  
- `DispatchQueue.global(qos: .userInitiated)` -> 우선순위 비교적 높음
    - Task 1
    - Task 2
    - Task 3
    - Task 4
- `DispatchQueue.global()`  -> 우선순위 비교적 낮음
    - Task 5
    - Task 6

<br><br>

그럼 이 task들은 아래처럼 thread에 배치된다.  

- Main Thread (Thread 1)
- Thread 2
    - Task 1
- Thread 3
    - Task 2
- Thread 4
    - Task 3
- Thread 5
    - Task 4
- Thread 6
    - Task 5
- Thread 7
    - Task 6

이렇게 우선순위가 더 높은 일에 더 많은 스레드를 배치하게 된다.  

참고로 `.global(qos:)`형식으로 qos를 지정하는 방법 외에도, `.async(qos:)`이런 식으로도 task의 qos를 지정할 수 있다.  


<br><br>
    
### Custom Queue
- 커스텀으로 만든다. 
- 디폴트로 Serial 특성을 가진 Queue. 하지만 Concurrent 로 설정 가능.
- Qos 설정 가능

커스텀 큐는 생성할 때에 label을 인자에 넣음으로 생성할 수 있다.  
```swift
let customSerialQueue = DispatchQueue(label: "Hello")
```

<br><br>

또한 아래처럼 Concurrent로도 설정할 수 있다.  
```swift
let customSerialQueue = DispatchQueue(label: "Hello", attributes: .concurrent)
```

<br><br>

qos를 따로 넣지않은 경우는 OS가 알아서 추론한다.  물론 아래처럼 설정가능하다. 
```swift
let customSerialQueue = DispatchQueue(label: "Hello",
                        qos: .background,
                        attributes: .concurrent)
```


<br><br>

### 정리

- Main Queue
    - 오직 한개만 존재
    - Serial 특성을 가진 Queue
    - 이곳에 할당된 task는 메인 스레드에서 처리 (UI 업데이트 내용 처리)
- Global Queue
    - Concurrent 특성을 가진 Queue
    - Qos (Quality Of Service)에 따라 여러개의 종류로 나뉨 (6종류)
- Custom Queue
    - 커스텀으로 만듦
    - 디폴트로 Serial 특성을 가진 Queue. 하지만 Concurrent 로 설정 가능.
    - Qos 설정 가능


<br><br><br>

# GCD 사용시 주의사항

## 1. UI는 main 스레드에서 처리한다

메인스레드가 UI를 담당하는 것은 iOS 뿐 아니라 다른 OS에서도 해당하는 내용이다.  

그래서 UI관련 업데이트 작업은 main 스레드에서 진행해야한다.  

예를 들어, 이미지 등을 global에서 다운받아오더라도, UI를 업데이트시켜주는 작업은 main 스레드에서 진행해야한다.  

<br><br>

```swift
URLSession.shared.dataTask(with: request) { data, response, error in
    guard let data = data, error == nil else { return }
    
    DispatchQueue.main.async() {
        self.imageView.image = UIImage(data: data)
    }
}.resume()
```

이런 코드가 있다고 가정하자.  

<br><br>

URLSession은 Operation Queue이고 모든 것이 background thread에서 동작하기 때문에 
UI업데이트 하는 작업을 main 스레드에서 한다고 명시하지않으면 아래와 같은 에러가 발생한다. 

```swift
URLSession.shared.dataTask(with: request) { data, response, error in
    guard let data = data, error == nil else { return }
    
    // DispatchQueue.main.async() {
        self.imageView.image = UIImage(data: data)
        // ERROR!! UIImageView.image must be used from main thread only
    // }
}.resume()
```

<br><br>

## 2. sync 메서드에 대한 2가지 주의사항

### 2-1. Main Queue에서 다른 Queue로 작업을 보낼때 sync를 사용하면 안된다.  

아래 작업을 하지말라는 말이다.  
```swift
// Main Thread에서

DispatchQueue.global().sync { }

```

<br><br>

차근차근 살펴보자.  
Sync로 보낸다는 것은 해당 작업이 끝날 때까지 기다린다 라는 의미였다. 
그런데 메인스레드는 UI를 업데이트 해줘야하는 곳인데,  
이 스레드에서 다른 작업들이 끝날때까지 기다린다는 것은  
해당 작업이 끝날 때까지 UI업데이트가 지연된다는 의미이고, 결국 화면이 버벅여 보일것이ㅏㄷ.  
그러니 Main Thread에서는 항상 async로 작업을 보내자.  

<br><br>

### 2-2. 현재와 같은 Queue에 sync로 작업을 보내면 안된다. 
같은 queue에 동기적으로 작업을 보낸다는건 아래와 같은 상황이다. 


```swift

DispatchQueue.global().async { 

    // Task A
    DispatchQueue.global().sync {
        // Task B
    }
}

```

<br><br>

global큐에서 global큐로 작업을 보내고 있다. 

이게 왜 문제가 되는지 살펴보자.  

- Step1
일단 TaskA를 global 큐로 보냈기 때문에, 해당작업은 `적당한` 스레드에 할당된 후  수행될 것이다.  

```swift
DispatchQueue.global().async { // Task A }
```
이  TaskA는 Global Queue로 보내졌다가 `적당한`스레드에 할당될 것이다. 

> Thread2에 배정되었다고 가정하자. 

- Step2
Thread2에서 TaskA를 수행하다보니 안에는 TaskB를 global큐로 보내는 작업이 들어있었다.  
이제 TaskB를 Global Queue 보내주자. 

- Step3 
Global Queue로 보내려는데, 보내는 방식이 Sync로 되어있다.
그래서 TaskB가 스레드에 할당되어 작업이 끝날 때까지는 다음 동작을 수행하지말고 기다려야한다. 

```swift
DispatchQueue.global().async { 

    // Task A ::: 현재 예제에서는 Thread2에 할당되었다고 가정
    DispatchQueue.global().sync {
        // Task B
    }
    // 다음 실행될 코드라인이다.  이전 작업인 TaskB가 끝나기 전까지는 이부분이 실행될 수 없다.  
}
```

Task A를 수행하고 있던 Thread2는 TaskB가 끝날 때까지 멈춰있다. 

이제 GCD는 Global Queue에 들어온 Task B를 어디 Thread로 할당할지 고민하게 된다.  
그런데???? GCD는 이 Task B를 Thread2로 할당하게 된다. 

> 할당된 스레드에서 작업을 시작해야하는데, 
> 이 스레드가 멈춰있는 스레드라면, 이 스레드는 이제 데드락이다.  

<br><br>

아래처럼 Queue에서 사용하고 있는 Thread객체는 정해져있다.  
예를 들어 Default Global Queue는 Thread 2,3,4만 사용하고, Background Global Queue는 Thread 5,6번만 사용하는 식으로 말이다.  

- Default Global Queue
    - Thread 2
    - Thread 3
    - Thread 4
- Background Global Queue
    - Thread 5
    - Thread 6
    
    <br><br>
    
따라서 같은 Queue에 보내면 같은 Thread에 배치될 수가 있는데, 이 때 해당 스레드가 Sync로 인해 멈춰있는 상황이라면 데드락 상황이 발생하게 된다. 물론 다른 스레드에 배치되면 이현상이 발생하지 않는다.  
이렇게 현재와 같은 Queue에 sync로 작업을 보내면 데드락상황이 발생할 수 있기 때문에,  
같은 Queue에는 sync로 작업을 보내지 말아야한다.  

참고로 Global Queue는 QoS에 따라 각각 다른 Queue객체를 생성한다.  
즉, `DispatchQueue.global(qos: .utility)`와 `DispatchQueue.global()`은 다른 큐가 된다.  
그래서 각각 다른 QoS의 Queue라면 스레드가 겹칠 일이 없다.  

```swift
//데드락 발생 가능성 있음
DispatchQueue.global().async {
  DispatchQueue.global().sync 
}
//데드락 발생 가능성 없음
DispatchQueue.global(qos: .utility).async {
  DispatchQueue.global().sync 
}
```

<br><br>

## 2-3. main Thread에서 DispatchQueue.main.sync를 사용하면 안된다. 
2-1.과 비슷한 상황이다.  
 
코드 작성시 별도의 처리를 안했다면 Main Thread에서 작업을 하는 것라고 앞서 말했다.   

근데 여기서 만약 `DispatchQueue.main.sync { }` 를 사용한다는 것은 에러를 발생시킨다.  

- `DispatchQueue.main`: main 큐로 태스크로 보낸다. 이때 main 큐는 직렬 큐이기 때문에 task 를 동일한 스레드 (메인 스레드)에만 할당한다.
- `.sync` : 해당 task 가 끝날때까지 메인 스레드는 일단 기다린다

그래서 아래와 같은 데드락 상황이 발생한다.  

1. 메인 스레드에서 “끝날때까지 기다리고 있을게~” 하고 task 를 메인 큐에 보냄
2. 메인 큐의 task는 메인 스레드로 할당 (직렬 큐)
3. 근데 메인 스레드는 기다리고 있는 상태
4. 결국 아무것도 진행되지 못하는 데드락 상황 발생

<br><br>

## 3. 객체에 대한 캡처를 주의한다.  
동작해야할 Task를 Queue로 보낸다는 것은 결국 클로저를 보내는 것이다.  

```swift

DispatchQueue.global().async { 
    // Task : 작업의 한 단위
}
```
따라서 객체에 대한 캡처 현상이 발생할 수 있게 되고, 자칫하면 retail Cycle이 발생할 수 있다.  그래서 약한참조를 위해 아래처럼 처리한다.  
```swift
DispatchQueue.global().async { [weak self] in
    // Task : 작업의 한 단위
}
```

<br><br>

## 4. 비동기 작업에서 Completion  Handler의 존재이유
주의사항이라기보다는 completion Handler가 왜필요한지 살펴보자.  

우리는 이제 .async를 통해 비동기로 작업을 보낼 수 있다는 걸 알게됐다.  
비동기로 보낸다는 뜻은 해당작업이 끝날 때까지 기다리지않고 남아있는 다른 작업을 실행하겠다는 의미였다. 
그럼 다른 작업을 하다가도 보낸 작업이 끝났다면, 그 시점을 파악해서 마저 필요한 작업을 해줘야하지 않을
까

그건 Completion Handler를 통해 알 수 있다.  

즉, Completion Handler는  어떤 작업이 끝났음을 야ㅏㄹ리는 클로저로, 비동기 메서드에는 항상 있다고 생각하면된다.  

> Swift에서는 Completion, completionHandler, explicit callback 이라고 부르는 클로저를 통해 해당 시점을 알려준다.  


<br><br>

    
    
    
    
    
    
    
## 색인
- GCD란 무엇인가요?
- GCD에서 사용되는 용어들
- GCD의 기본 개념과 동작 방식
- GCD의 큐 종류: Serial Queue와 Concurrent Queue
- GCD의 주요 API: dispatch_queue_t, dispatch_async, dispatch_sync
- GCD의 그룹 기능: dispatch_group_t, dispatch_group_async, dispatch_group_notify
- DispatchQueue 클래스: 큐 생성 및 비동기 작업 처리
- DispatchGroup 클래스: 그룹으로 묶어서 작업 관리
- DispatchSemaphore 클래스: 작업 실행 허용 개수 제한
    - dispatch_semaphore_t, dispatch_semaphore_wait, dispatch_semaphore_signal
- DispatchSource 클래스: 이벤트 모니터링 및 작업 실행
- DispatchBarrier 함수: 큐 내 작업 실행 순서 제어
    - dispatch_barrier_async, dispatch_barrier_sync
- GCD의 타이머 기능: dispatch_source_t, dispatch_source_create, dispatch_source_set_timer
- dispatchWorkItem 클래스: 작업 실행과 취소, 일시 중지, 재개, 결과값 가져오기 등
[TIL: GCD - dispatchWorkItem 정리내용](https://github.com/isGeekCode/TIL/commit/b64f10055c31d81e6249fa5f57a9f43a2b909816?short_path=ce70c04#diff-ce70c046c202de3bdcd893c84fae959478311b24ff7553d386fd19e12be98a81)

## 주요 객체
DispatchQueue 클래스: GCD 큐를 나타내며, 비동기 작업을 처리하는 데 사용된다.
DispatchGroup 클래스: 여러 개의 작업을 그룹으로 묶어서 관리하고, 모든 작업이 완료될 때까지 기다릴 수 있다.
DispatchSemaphore 클래스: 특정 작업의 실행 허용 개수를 제한하는 데 사용된다.
DispatchSource 클래스: 타이머나 파일 디스크립터 등의 이벤트를 모니터링하고, 이벤트가 발생할 때마다 작업을 실행할 수 있다.
DispatchBarrier 함수: 큐 내 작업의 실행 순서를 제어하는 데 사용된다.


## History
- 230308: 초안작성
- 231204: GCD 톺아보기
