# Data Structure - Stack과 Queue

이 둘은 아주 기본적인 데이터구조다.  


## Stack
Stack은 L.I.F.O. (Last In First Out) 정책을 따른다. 

위에서 아래로 쌓아가는 형태로 구성된다.  
그래서 새로운 데이터가 추가되면 기존의 대이터 위에 쌓이게된다. 
그리고 기존의 데이터를 제외하려면 가장 위의 데이터부터 제외시키게 된다.   

- Push : 새롭게 위로 쌓는 것
- Pop : 기존의 것을 제외하는 것

<img width="300" alt="ezgif-3-7a4ed42308" src="https://github.com/isGeekCode/TIL/assets/76529148/8700a298-eaf3-45e1-b082-c3d222cb0efe">

iOS에서는 NavigationController의 NavigationStack이 이에 해당한다.  

### Swift로 Stack 구현하기
Array가 제공하는 메서드를 사용하면 Stack 구현이 가능하다.  
append를 통해 push, popLast를 통해 pop시킬 수 있다.  

```swift
// Element는 제네릭타입의 변수로 명시한 것임

struct Stack<Element> {
    private var elements: [Element] = []
    
    public var count: Int {
        return elements.count
    }
    
    // 배열에 추가
    public mutating func push(_ element: Element) {
        elements.append(element)
    }
    
    // 배열의 마지막을 제외
    public mutating func pop() -> Element? {
        return elements.popLast()
    }
}

var stack: Stack<Int> = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack)

for _ in 0...3 {
    print(stack.pop() as Any, stack)
}

```

<br><br>

## Queue

Queue는 OS(운영체제)에서 프로세스 스케쥴링에 사용하는 아주 기본적인 자료구조다.
Queue라는 단어를 사전에서 찾아보면 줄, 대기열이라고 나옵니다.

단어 그대로 줄 서는것과 비슷하게 동작한다. 

이 방식은 먼저 대기열에 추가된 요소는 가장 먼저 대기열에서 나가게 된다.  
이런 방식을 FIFO(First-In First-Out)라고 부른다. -> 파이포 라고 읽는다. 

- Enqueue : Queue에 데이터를 넣는(보내는) 작업
- Dequeue : Queue로부터 데이터를 빼는 작업

<img width="300" alt="ezgif-3-7136c770ec" src="https://github.com/isGeekCode/TIL/assets/76529148/c2d72069-6b7f-4218-9a58-1af0f68b84ca">

iOS에서 Queue는 GCD를 다루면서 Dispatchqueue.main.async 메서드를   


https://beepeach.tistory.com/m/285
추가 필요

## History
- 231201: 초안작성
