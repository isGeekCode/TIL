# 기본적인 자료구조 - 스택 (Stack)

**스택(Stack)**은 후입선출(LIFO: Last In, First Out) 원칙을 따르는 선형 자료구조야. 스택은 데이터의 순서를 처리할 때 유용하며, 주로 재귀 호출, 백트래킹 등의 알고리즘에서 많이 사용된다.  

<br>

## 스택의 주요 특징
- 후입선출(LIFO): 마지막에 삽입된 요소가 가장 먼저 제거된다.
- 동적 크기: 필요에 따라 요소를 추가하거나 삭제할 수 있다.
- 제한적인 접근: 스택은 맨 위(top) 요소만 접근할 수 있다.

<br>

## 주요 연산:
- push: 요소를 스택의 맨 위에 추가.
- pop: 스택의 맨 위에 있는 요소를 제거하고 반환.
- peek: 스택의 맨 위에 있는 요소를 제거하지 않고 반환.
- isEmpty: 스택이 비어있는지 확인.

<br>

## 스택의 시간 복잡도
- push, pop, peek: 모두 O(1) 시간 복잡도를 가진다.
- 스택의 맨 위에 요소를 추가하거나 제거하는 연산은 상수 시간 내에 이루어진다.
- 탐색: 스택 내부에서 특정 요소를 찾는 연산은 O(n) 시간이 걸린다.

<br>

## 스택 구현 예시 (Swift)
```swift
import Foundation

struct Stack <T> {
    private var array = [T]() {
        didSet {
            print("스택이 변경되었습니다. 현재 스택: \(array)")
        }
    }

    mutating func push(_ element: T) {
        array.append(element)
    }

    mutating func pop() -> T? {
        return array.popLast()
    }

    func peek() -> T? {
        return array.last
    }

    func isEmpty() -> Bool {
        return array.isEmpty
    }
}

// 스택 사용 예시
var stack = Stack<String>()

stack.push("기차")
// 스택이 변경되었습니다. 현재 스택: ["기차"]
stack.push("자동차")
// 스택이 변경되었습니다. 현재 스택: ["기차", "자동차"]

let peekItem = stack.peek()
print("최상위 요소 ::: \(peekItem ?? "없음")")
// 최상위 요소 ::: Optional("자동차")

let element1 = stack.pop()
print("삭제한 요소 ::: \(element1 ?? "없음")")
// 삭제한 요소 ::: Optional("자동차")
// 스택이 변경되었습니다. 현재 스택: ["기차"]

let element2 = stack.pop()
print("삭제한 요소 ::: \(element2 ?? "없음")")
// 삭제한 요소 ::: Optional("기차")
// 스택이 변경되었습니다. 현재 스택: []

let element3 = stack.pop()
print("삭제한 요소 ::: \(element3 ?? "없음")")
// 삭제한 요소 ::: nil

let peekItem2 = stack.peek()
print("최상위 요소 ::: \(peekItem2 ?? "없음")")
// 최상위 요소 ::: nil
```

## popLast()를 사용하는 이유
- 성능 효율성: O(1) 시간 복잡도로 마지막 요소를 제거할 수 있어 매우 빠르고 효율적이다.
- 안전성: 스택이 비어 있는 경우에도 nil을 반환해서 예외 상황을 안전하게 처리할 수 있다.
- 간결함: 배열에서 마지막 요소를 제거하는 작업을 쉽게 구현할 수 있다.
