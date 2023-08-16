# GCD - OperationQueue를 이용한 비동기 작업


OperationQueue의 특별한 점은 이미 실행되었거나 완료된 작업을 추가할 수 없다는 것이다. 

만약 이미 실행한 작업과 동일한 동작을 수행하려면 새작업을 생성하여 추가해야한다. 

만약 동일한 작업을 실행하게 되면 아래와 같은 에러가 발생하며 앱이 종료된다. 

```swift
Thread 1: "*** -[NSOperationQueue addOperations:waitUntilFinished:]: 1 (of 3) operation is finished, executing, or already in a queue, and cannot be enqueued"

```



##사용법

### 간단한 사용법

```swift
let mainQueue = OperationQueue.main
mainQueue.addOperation {
    // UIView 클래스의 메서드 호출 등
    // UI 업데이트 작업
    print("test")
}
```


<br><br>

### 여러 작업을 직접 추가하기

```swift
let mainQueue = OperationQueue.main

mainQueue.addOperation {
    // 작업 1
    print("test1")
}

mainQueue.addOperation {
    // 작업 2
    print("test2")
}
```

만약 동일한 작업을 추가하고 싶다면 함수를 만들어서 실행하자

```SWIFT
        
let mainQueue = OperationQueue.main

mainQueue.addOperation {
    // 작업 1
    self.testFirst()
}

mainQueue.addOperation {
    // 작업 2
    self.testSecond()
}

mainQueue.addOperation {
    // 작업 1
    self.testFirst()
}

func testFirst() { print("test1") }

func testSecond() { print("test2") }
```

<br><br>

## BlockOperation 추가하기
OperationQueue.main에 추가한 BlockOperation 순서대로 실행한다. 
```
let mainQueue = OperationQueue.main

// 작업 1
let operation1 = BlockOperation {
    // 작업 내용
}

// 작업 2
let operation2 = BlockOperation {
    // 작업 내용
}

// 작업 추가
mainQueue.addOperation(operation1)
mainQueue.addOperation(operation2)
```



<br><br>

## 한 작업이 끝나기 전에는 다른작업을 못하게 하기

addDependency메서드를 통해 한 작업이 끝나기 전에는 해당 작업을 실행하지 못하게 할 수 있다.
- 예시
A는 B를 완료하기 전에는 실행할 수 없다.
```
A.addDependency(B)
```



```swift
let mainQueue = OperationQueue.main

let highPriorityOperation = BlockOperation {
    // 높은 우선순위 작업
    print("test1")
}

let lowPriorityOperation = BlockOperation {
    // 낮은 우선순위 작업
    print("test2")
}

lowPriorityOperation.addDependency(highPriorityOperation)
mainQueue.addOperations([lowPriorityOperation, highPriorityOperation], waitUntilFinished: false)

```




## DispatchQueue를 이용해 비동기 추가

```SWIFT
let mainQueue = OperationQueue.main
mainQueue.addOperation {
    // 비동기 작업 시작
    DispatchQueue.global().async {
        // 백그라운드 스레드에서 실행되어야 하는 작업
        // 작업이 완료되면 메인 스레드에서 UI 업데이트
        mainQueue.addOperation {
            // UIView 클래스의 메서드 호출 등
            // UI 업데이트 작업
        }
    }
}
```
