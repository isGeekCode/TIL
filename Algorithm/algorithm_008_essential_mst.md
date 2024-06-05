# 필수 알고리즘 - MST (Minimum Spanning Tree)

Spanning Tree = 모든 노드가 연결된 트리

## 풀이
- MST는 정형화된 풀이 방법이 있음
- 대부분 양방향 간선이 있는 양방향 그래프 문제

## MST
최소의 비용으로 모든 노드가 연결된 트리

어떻게 최소 비용을 알 수 있을까????

아래와 같은 트리 구조가 있다고 가정해보자.  

<img width="512" alt="mst_original" src="https://github.com/isGeekCode/TIL/assets/76529148/d0c7b4b6-488d-4cb2-a577-8d207fec4df9">

각각의 노드에는 숫자가 달려있고, 각 사이에는 숫자가 정해진 간선이 있다.  


이 최소 비용을 구하는 방법은 Kruskal과 Prim 이 있다.  

<br><br>

### Kruskal
- 전체 간선 중 가장 작은 것 부터 연결하는 방법
- 이미 노드가 연결된 간선이라면 패스한다.  

- 과정
    - 가장 작은 간선은 1이다. 1-5 노드 연결
    - 1-5 노드에 인접한 간선 중 작은 간선 2, 3중  2번을 연결
    - 2-1-5 에 인접한 간선 3,4,5 중 3번을 연결
    - 2-1-3-5 에 인접한 간선 4는 이미 연결되어있음 -> 패스
    - 간선 5,6 번중 5번 연결

- 단점
    - Kruskal -> Union - Find 라는 알고리즘을 사용하는데, 코드 구현이 복잡함....
    - 그래서 Prim으로 주로 해결


_<img width="526" alt="mst_krustal" src="https://github.com/isGeekCode/TIL/assets/76529148/f5f1ce31-6703-41a3-902b-c19506446746">_


<br><br>

### Prim
- 현재 연결된 트리에 이어진 간선 중 가장 작은 것을 추가하는 과정
- 이미 노드가 연결된 간선이라면 패스한다.

- 과정
    - 1번노드에서 시작한다고 했을때,
    - 1번 노드에 연결된 가장 작은 간선은 1이다. 1-5 노드 연결
    - 1-5 노드에 인접한 간선 중 작은 간선 2, 3중  2번을 연결
    - 2-1-5 에 인접한 간선 3,4,5 중 3번을 연결
    - 2-1-3-5 에 인접한 간선 4는 이미 연결되어있음 -> 패스
    - 간선 5,6 번중 5번 연결

<img width="537" alt="mst_prim" src="https://github.com/isGeekCode/TIL/assets/76529148/f3712e18-ca45-4590-bbdc-436e049bdda1">

<br><br>

### 간선 중 가장 작은 것을 다루는 방법
heap 자료구조를 이용하게 된다.  
| 1, 5 |   -> 1번 비용을 갖는 5번 노드와의 간선
| 2, 2 |   -> 2번 비용을 갖는 2번 노드와의 간선

<br><br>

## Heap
- 최대값, 최소값을 빠르게 계산하기 위한 자료구조
- 이진트리구조 :: 한개의 노드에 최대 2개의 노드가 연결된다.  
- 처음에 저장할 때부터 최대, 최소값을 결정하도록 한다. 
- 시간복잡도: lg(E)

<br>

Heap은 아래와 같이 노드에 최대 2개의 노드가 연결된다.  

<img width="500" alt="heap_original" src="https://github.com/isGeekCode/TIL/assets/76529148/18c7fb06-fc9b-4f4c-ac10-a99989e62a39">

<br>

Heap에서는 새로운 값을 입력하거나 삭제할 때, 최대값, 최소값을 비교하여 주입, 추출된다.  


<img width="942" alt="heap_add" src="https://github.com/isGeekCode/TIL/assets/76529148/d0a15b7e-8734-4b03-9d09-fba5b6249252">

<br>

### 핵심코드

<img width="512" alt="mst_original" src="https://github.com/isGeekCode/TIL/assets/76529148/d0c7b4b6-488d-4cb2-a577-8d207fec4df9">


1번 노드에는 5번 노드(1번 edge),   2번 노드(2번 edge), 3번 노드 (3번 edge) 가 있다. 
2번 노드에는 1번 노드(2번 edge),  3번 노드(4번 edge), 4번 노드 (5번 edge) 가 있다. 
3번 노드에는 1번 노드(3번 edge),  2번 노드(4번 edge), 4번 노드 (6번 edge) 가 있다. 
4번 노드에는 2번 노드(5번 edge),  3번 노드(6번 edge) 가 있다. 
5번 노드에는 1번 노드(1번 edge) 가 있다. 


각각의 간선 edge가 1번 edge는 1의 비용, 2번 edge 는 2의 비용을 나타낼때,  prim을 사용해보면 
아래 처럼 진행이 된다.  

swift에는 heap이 따로 없기 때문에 배열을 가지고 관리한다.  


|| HEAP |
| ~~(0,1)~~ |
| (1,5) |
| (2,2) |
| (3,3) |



```swift

import Foundation

var heap = [(0, 1)] // 시작지점 (비용, 노드번호)
let nodeCount = 5 // 전체 노드 수
var chk = [Bool](repeating: false, count: nodeCount + 1 ) // 노드 개수 + 1 (노드 번호가 1부터 시작한다고 가정)
// check ->> [false, false, false, false, false, false]
var rs = 0

// 각 노드에 연결된 간선과 비용
var edge = [
    [],
    [(1, 5), (2, 2), (3, 3)],  // 1번 노드
    [(2, 1), (4, 3), (5, 4)],  // 2번 노드
    [(3, 1), (4, 2), (6, 4)],  // 3번 노드
    [(5, 2), (6, 3)],          // 4번 노드
    [(1, 1)]                   // 5번 노드
]

while !heap.isEmpty {
    // 최소 힙 구현을 위해 정렬하여 첫 요소를 사용
    heap.sort { $0.0 < $1.0 }
    let (w, nextNode) = heap.removeFirst() // heap배열에선 첫번쨰 요소를 제거하고, 제거하는 요소를 리턴

    if !chk[nextNode] { // 방문하지 않은 노드
        chk[nextNode] = true
        rs += w // 현재 비용을 합산
        
        for nextEdge in edge[nextNode] {
            let (cost, connectedNode) = nextEdge
            if !chk[connectedNode] {
                heap.append((cost, connectedNode))
            }
        }
    }
}

print("Minimum Spanning Tree Cost: \(rs)")
```

## 기본문제
백준 1197 최소 스패닝 트리

### 아이디어
- 간선을 인접 리스트형태로 저장 
    - 1번 노드 -> [(w,v)]
    - 2번 노드 -> [(w,v), ~, ~]
    - 전체 인접 리스트 = [1번노드 정보, 2번 노드 정보]
- 시작점부터 힙에 넣기
- 힙이 빌때까지
    - 해당 노드 방문 안한곳인 경우
        - 방문체크, 비용추가, 연결된 간선 새롭게 추가


### 시간 복잡도
- Edge 리스트에 저장 : O(E)
- Heap안 모든 Edge에 연결된 간선 확인 : O(E+E)
- 간선을 힙에 삽입 : O(lgE) -> 모든 간선을 삽입 -> O(lgE * E) = ElgE
- O(E+ 2E + ElgE ) = O(3E + ElgE) = O(E(3+lgE)) ->> O(ElgE)

### 자료구조
- Edge 저장리스트 -> [(Int, Int)]
- 정점(노드) 방문 리스트 -> [Bool]
- MST 비용 -> Int


## 발생하는 문제!

Heap(우선순위 큐)을 swift에서 사용하려면 Array로 구현해야하는데, 
여기서 Heap의 추가 제거시 정렬을 sort로 하게되면.... 그 부분에서 시간복잡도가 초과하게 된다. 
그래서 실제 Heap처럼 동작하기 위한 구조체를 구현해야한다.  하..

```swift
import Foundation

/// `Heap`은 최소 힙을 구현하는 제네릭 구조체. `Comparable` 프로토콜을 준수하는 타입 T에 대해 작동.
struct Heap<T: Comparable> {
    /// 힙의 내부 배열. 모든 요소는 이 배열에 저장.
    private var items: [T] = []
    
    /// 힙이 비어 있는지 확인. 비어있으면 true를 반환.
    var isEmpty: Bool {
        return items.isEmpty
    }
    
    /// 새 요소를 힙에 삽입.
    /// - Parameter element: 힙에 삽입할 요소.
    mutating func insert(_ element: T) {
        items.append(element)  // 배열의 끝에 새 요소 추가
        siftUp(from: items.count - 1)  // 삽입된 요소를 적절한 위치로 이동시키기 위해 siftUp 메서드를 호출.
    }
    
    /// 힙에서 최소 요소를 제거하고 반환
    /// - Returns: 힙의 최소 요소. 힙이 비어 있다면 nil을 반환
    mutating func extractMin() -> T? {
        guard !items.isEmpty else { return nil }  // 힙이 비어있으면 nil 반환
        if items.count == 1 {
            return items.removeFirst()  // 요소가 하나뿐이면 바로 제거하고 반환
        }
        let min = items[0]  // 최소 요소(루트 요소) 저장
        items[0] = items.removeLast()  // 마지막 요소를 루트 위치로 이동
        siftDown(from: 0)  // 새 루트를 적절한 위치로 이동시키기 위해 siftDown 메서드를 호출
        return min  // 최소 요소 반환
    }
    
    /// 주어진 인덱스의 요소를 부모와 비교하며 위로 이동
    /// - Parameter index: sift up을 시작할 배열 인덱스
    private mutating func siftUp(from index: Int) {
        var childIndex = index
        let child = items[childIndex]  // 삽입된 요소
        var parentIndex = (childIndex - 1) / 2
        
        while childIndex > 0 && items[parentIndex] > child {
            items[childIndex] = items[parentIndex]  // 부모 요소가 자식 요소보다 크면 위치 교환
            childIndex = parentIndex
            parentIndex = (childIndex - 1) / 2
        }
        
        items[childIndex] = child
    }
    
    /// 주어진 인덱스의 요소를 자식과 비교하며 아래로 이동
    /// - Parameter index: sift down을 시작할 배열 인덱스
    private mutating func siftDown(from index: Int) {
        var parentIndex = index
        let length = items.count
        let element = items[parentIndex]
        
        while true {
            let leftChildIndex = 2 * parentIndex + 1
            let rightChildIndex = leftChildIndex + 1
            var smallestIndex = parentIndex
            
            if leftChildIndex < length && items[leftChildIndex] < items[smallestIndex] {
                smallestIndex = leftChildIndex
            }
            if rightChildIndex < length && items[rightChildIndex] < items[smallestIndex] {
                smallestIndex = rightChildIndex
            }
            if smallestIndex == parentIndex {
                break  // 추가 교환 필요 없으면 종료
            }
            items[parentIndex] = items[smallestIndex]
            items[smallestIndex] = element
            parentIndex = smallestIndex
        }
    }
}

func exam(sample: Int) {
    var minHeap = Heap<Int>()
    minHeap.insert(10)
    minHeap.insert(5)
    minHeap.insert(15)
//    print(minHeap.extractMin()) // 5
//    print(minHeap.extractMin()) // 10
//    print(minHeap.extractMin()) // 15

}


// MARK: 추가해 사용할 비교군 Comparable 프로토콜을 채택해야한다. 
// 이후 비교 연산자를 구현하여 비교할 수 있도록 구현한다.  
// 여기서는 cost를 이용해서 비교한다.  
struct Edge: Comparable {
    let cost: Int
    let node: Int

    // Comparable 프로토콜 요구사항 구현
    static func < (lhs: Edge, rhs: Edge) -> Bool {
        return lhs.cost < rhs.cost
    }
}

func exam(sample: Edge) {
    // Edge 구조체를 활용한 사용 예시
    var minHeap = Heap<Edge>() // 최소 힙 생성

    // 여러 간선을 힙에 추가
    minHeap.insert(Edge(cost: 10, node: 2))
    minHeap.insert(Edge(cost: 5, node: 3))
    minHeap.insert(Edge(cost: 2, node: 4))
    minHeap.insert(Edge(cost: 7, node: 5))
    minHeap.insert(Edge(cost: 3, node: 6))

    // 최소 비용 간선부터 추출하여 출력
    while !minHeap.isEmpty {
        if let edge = minHeap.extractMin() {
            print("Edge to node \(edge.node) with cost \(edge.cost)")
        }
    }

    // 예상 출력:
    // Edge to node 4 with cost 2
    // Edge to node 3 with cost 5
    // Edge to node 6 with cost 3
    // Edge to node 5 with cost 7
    // Edge to node 2 with cost 10

}

```

 
