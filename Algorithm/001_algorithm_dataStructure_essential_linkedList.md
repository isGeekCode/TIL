# 기본적인 자료구조 - 연결 리스트 (Linked List)


**연결 리스트(Linked List)**는 **노드(Node)**라는 개체들이 연결된 구조로 데이터를 저장하는 자료구조.  각 노드는 데이터와 **다음 노드를 가리키는 참조(포인터)**로 이루어져 있다. 배열과 달리, 연결 리스트는 동적 크기를 가지며, 요소 삽입/삭제 시 메모리 재할당이 필요 없다는 장점이 있다.


## 연결 리스트의 주요 특징
- 동적 크기: 배열과 달리 연결 리스트는 크기가 가변적으로, 필요에 따라 노드를 추가하거나 삭제할 수 있다.
- 노드 기반 연결: 각 노드는 데이터와 다음 노드를 가리키는 포인터로 구성돼. 노드를 통해 연속된 데이터를 저장할 수 있다.
- 순차 접근: 인덱스를 통해 바로 접근하는 배열과 달리, 연결 리스트는 순차적으로 노드를 탐색해야 한다.


<br>

## 시간 복잡도
- 삽입/삭제: 특정 위치에 노드를 삽입하거나 삭제할 때는, O(1) 시간 복잡도로 가능하지만, 해당 위치로 이동할 때는 O(n) 시간이 소요된다.  즉, 탐색 후 삽입/삭제는 O(n) 시간이 걸린다.
- 접근: 특정 위치에 있는 요소에 접근하려면 O(n) 시간이 걸림 (처음부터 순차적으로 탐색).


<br>

## 연결 리스트 사용 예시 (Swift)
```swift
// 노드 구조체 정의
class Node<T> {
    var value: T
    var next: Node?

    init(value: T) {
        self.value = value
        self.next = nil
    }
}

// 연결 리스트 구조체 정의
class LinkedList<T> {
    var head: Node<T>?

    // 노드 추가 (맨 끝에 삽입)
    func append(_ value: T) {
        let newNode = Node(value: value)
        if head == nil {
            head = newNode
        } else {
            var current = head
            while current?.next != nil {
                current = current?.next
            }
            current?.next = newNode
        }
    }

    // 노드 삭제 (특정 값 삭제)
    func delete(_ value: T) {
        if head == nil {
            return
        }
        
        if head?.value == value {
            head = head?.next
            return
        }

        var current = head
        while current?.next != nil {
            if current?.next?.value == value {
                current?.next = current?.next?.next
                return
            }
            current = current?.next
        }
    }

    // 리스트 출력
    func printList() {
        var current = head
        while current != nil {
            print(current!.value)
            current = current?.next
        }
    }
}

// 사용 예시
let list = LinkedList<Int>()
list.append(10)
list.append(20)
list.append(30)
list.printList()  // 출력: 10, 20, 30

list.delete(20)
list.printList()  // 출력: 10, 30
```

## 중간 노드 삭제
연결 리스트에서 중간에 있는 노드를 삭제하려면, 해당 노드의 이전 노드와 다음 노드를 연결해야한다.  
삭제하고자 하는 노드를 찾은 뒤, 이전 노드의 다음 포인터를 삭제할 노드의 다음 포인터로 연결하면 된다.  

### 삭제 과정
1. 삭제할 노드의 앞쪽 노드를 찾음.
2. 앞쪽 노드의 포인터를 삭제할 노드의 다음 노드로 연결함.
3. 삭제할 노드는 더 이상 연결 리스트에 포함되지 않게 됨.


```swift
    // 노드 삭제 (특정 값 삭제)
    func delete(_ value: T) {
        if head == nil {
            return
        }
        
        if head?.value == value {
            head = head?.next
            return
        }

        var current = head
        while current?.next != nil {
            if current?.next?.value == value {
                current?.next = current?.next?.next
                return
            }
            current = current?.next
        }
    }
```
