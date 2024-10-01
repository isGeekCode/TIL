# 기본적인 자료구조 - 큐 (Queue)
**큐(Queue)**는 **선입선출(FIFO: First In, First Out)**의 원칙을 따르는 자료구조다.  
가장 먼저 들어온 데이터가 가장 먼저 나가며, 주로 대기열이나 리소스 관리 등에서 사용된다.  

<br>

## 큐의 주요 특징
- 선입선출(FIFO): 가장 먼저 들어온 요소가 가장 먼저 나감.
- 동적 크기: 필요에 따라 요소를 추가하거나 삭제할 수 있음.
- 제한적인 접근: 큐는 맨 앞과 맨 뒤에서만 요소를 추가하거나 제거할 수 있음.

<br>

## 주요 연산:
- enqueue: 큐의 끝에 요소를 추가.
- dequeue: 큐의 앞에서 요소를 제거하고 반환.
- peek: 큐의 맨 앞에 있는 요소를 제거하지 않고 확인.
- isEmpty: 큐가 비어있는지 확인.

<br>


## 시간 복잡도
- enqueue: O(1) – 큐의 끝에 요소를 추가.
- dequeue: O(1) – 큐의 앞에서 요소를 제거.
- peek: O(1) – 큐의 맨 앞 요소를 확인.
- isEmpty: O(1) – 큐가 비어있는지 확인.


<br>

## 큐 구현 예시 (Swift)
```swift
import Foundation

struct Queue<T> { 
    private var array = T { 
        didSet { 
            print("현재 데이터는 ::(array)")
         } 
    }

    // 요소를 큐의 끝에 추가
    mutating func enqueue(_ element: T) {
        array.append(element)
    }

    // 큐의 맨 앞 요소를 제거하고 반환
    mutating func dequeue() -> T? {
        return array.isEmpty ? nil : array.removeFirst()
    }

    // 큐의 맨 앞 요소를 확인 (제거하지 않음)
    func peek() -> T? {
        return array.isEmpty ? nil : array[0]
    }

    // 큐가 비어 있는지 확인
    func isEmpty() -> Bool {
        return array.isEmpty
    }
}

// 큐 사용 예시 
var queue = Queue<String>()

queue.enqueue("딸기") 
//현재 데이터는 ::["딸기"]

queue.enqueue("사과") 
//현재 데이터는 ::["딸기, 사과"]

let peekItem = queue.peek() 
print("peek된 Item은 (peekItem)") 
// peek된 Item은 Optional("딸기")

let dequeueItem = queue.dequeue()
// 현재 데이터는 ::["사과"] 
print("dequeue된 Item은 (dequeueItem)") 
// dequeue된 Item은 Optional("딸기")

let dequeueItem2 = queue.dequeue() 
// 현재 데이터는 ::[] 
print("dequeue된 Item은 (dequeueItem2)") 
// dequeue된 Item은 Optional("사과")

let dequeueItem3 = queue.dequeue() 
print("dequeue된 Item은 (dequeueItem3)") 
// dequeue된 Item은 nil
```
