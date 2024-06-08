# 알고리즘 템플릿
- 활용할 알고리즘
- BFS
- DFS (재귀 사용)
- 백트래킹 ( 재귀사용 )
- 투포인터
- 이진탐색
- 그리디
- DP
- MST
- 다익스트라
- 플로이드

## 풀기전에 
```
1. 아이디어 :: 어떻게 풀어나갈지
2. 시간 복잡도 : 최대수 대입시 2억개의 연산이 넘어가는지 (1억도 위험)
3. 변수 : 어떻게 사용할지
```

## 오답노트 작성
- 알고리즘 별 정리
- 문제유형을 스스로 요약(자기만의 언어로)
- 틀린 문제 주기적으로 풀기 -> 틀린건 맨날 틀림....
- 면접과 코테가 반복될 때 유용함


### 예시
- BFS
    - Flood Fill
        - 이어져있는 노드를 연결하는 문제
        - BFS 사용해서 이어져있는 노드 확인
        - 링크
    - 경찰과 도둑
        - 경찰은 쫓고, 도둑은 탈출
        - 도둑과 경찰이 동시에 같은 칸으로 이동했을 때, 그 칸은 더이상 이동 못함
        - 링크
    - 최소횟수
    - 조건
    - 0/1
    - ...




# 그래프
## BFS
그래프에서 좌표를 전후좌우 탐색하며 연속된 여부를 체크
- Queue에 저장
- 시간복잡도 : `O(V+E)`
```swift
let firstLine = readLine()!.split(separator: " ").map { Int($0)! }
let (n, m) = (firstLine[0], firstLine[1])
//n개의 row, m개의 column

var grid = [[Int]]()  // 그래프
for _ in 0..<n {
    let row = readLine()!.split(separator: " ").map { Int($0)! }
    grid.append(row)
}

// 방문여부배열
var visited = Array(repeating: Array(repeating: false, count: m), count: n) 
var numPictures = 0 // 그림의 개수
var maxArea = 0     // 최대 그림의 넓이
var area = 0

for j in 0..<n { // row y축
    for i in 0..<m { // column x축
        if canVisit(j, i) { // 방문가능여부 체크
            // 1이면 처리하는 부분
            let area = bfs(j, i) // 그림 하나당 한번 호출함
            numPictures += 1
            maxArea = max(maxArea, area) // 저장되어있던 maxArea와 area를 비교하여 갱신
        }
    }
}

print(numPictures)
print(maxArea)


func canVisit(_ y: Int, _ x: Int) -> Bool {
    return grid[y][x] == 1 && !visited[y][x]
}

func bfs(_ y: Int, _ x: Int) -> Int {

    var queue: [(Int, Int)] = [(y, x)] // 시작위치가 큐에 세팅
    
    let dy = [1, -1, 0, 0]
    let dx = [0, 0, 1, -1]

    visited[y][x] = true // 방문처리
    area = 1 // 최초 좌표의 너비를 더함

    while !queue.isEmpty {

        let current = queue.removeFirst()  // Dequeue 큐에서 현재 위치 추출
        for i in 0...3 {
            
            
            let y = current.0
            let x = current.1
            
            let ny = y + dy[i]
            let nx = x + dx[i]
            
            if (nx >= 0 && nx < m) && (ny >= 0 && ny < n) { // 범위 이탈 체크
                if canVisit(ny, nx) { // 현재 체크하는 상하좌우에 1이 있는지, 방문을 안했는지
                    visited[ny][nx] = true // 방문체크
                    queue.append((ny, nx)) // Enqueue 발견된 현재 위치를 큐에 추가 ( 큐의 순서대로 이접 4방향 체크 )
                    area += 1 // 방문X && 인접한 1을 발견할 때마다 1추가
                }
            }
        }
    }
    return area
}

```

<br><br>

## DFS
현재 기준점의 자식들을 순회하는 우선순위는 수집중인 노드의 첫번째 자식여부다.
깊게 자식을 타고 들어감

- Stack에 저장
- 재귀로도 해결 가능
    - 재귀는 항상 끝나는 시점을 정해야할것
- 시간복잡도 : `O(V+E)`
- 자료구조
    - 검색할 그래프
    - 방문 여부 그래프
    
    
### Stack
```swift

```

<br><br>

### 재귀
```swift
let firstLine = readLine()!
let n = Int(firstLine)!
var graph = [[Int]]()  // 2차원 배열로 도화지의 정보를 저장

for _ in 0..<n {
    let str = readLine()!
    var row = [Int]()
    for i in str {
        let t = String(i)
        row.append(Int(t)!)
    }
    graph.append(row)
}

let width = graph.count
var chkArr = Array(repeating: Array(repeating: false, count: width), count: width)

var result = [Int]()
var each = 0
for j in 0..<width { // row y축
    for i in 0..<width { // column x축
        if isCanVisit(j,i) {
            // 방문 체크
            chkArr[j][i] = true
            // DFS 로 크기 구하기
            each = 0
            dfs(j,i)
            // 크기 결과를 리스트에 넣기
            result.append(each)
        }
    }
}

result.sort()
print(result.count)
result.forEach{ print($0) }

func isCanVisit(_ y: Int,_ x: Int) -> Bool {
    return (graph[y][x] == 1 && chkArr[y][x] == false)
}

func isRange(_ y: Int, _ x: Int) -> Bool {
    return (x >= 0 && x < width) && (y >= 0 && y < width)
}

func dfs(_ y: Int,_ x: Int) {
    each += 1

    let dy = [0, 1, 0, -1]
    let dx = [1, 0, -1, 0]
    
    for k in 0...3 {
        let ny = y + dy[k]
        let nx = x + dx[k]
        
        if isRange(ny, nx) {
            if isCanVisit(ny, nx) {
                chkArr[ny][nx] = true
                dfs(ny, nx)
            }
        }
    }
}

```

<br><br>

## 백트래킹
모든 경우의 수를 확인해야할 때 사용한다. 
- 백트래킹은 N이 10언저리만 가능하기 때문에 문제에서 힌트를 얻을 수 있음
- 재귀는 항상 끝나는 시점을 정해야할것
- 시간복잡도
    - 중복이 가능한 경우 : `N^N`     -> N이 8까지 가능
    - 중복이 불가한 경우 : `N!`      -> N이 10까지 가능
- 자료구조
    - 방문여부 배열 : [Bool]
    - 선택값 배열 : [Int]
    
### 재귀
```swift
let inputArr = readLine()!.split(separator: " ").map{ Int($0)!}
let (n, m) = (inputArr[0], inputArr[1])

var result = [Int]()
var chkArr = Array(repeating: false, count: n+1)
print(chkArr)
recur(0)

func recur(_ num: Int) {
    if num == m {
        let s = result.map{ String($0)}
        print(s.joined(separator: " "))
        return
    }
    
    for i in 1...n {
        print("chk", chkArr)
        if !chkArr[i] {
            chkArr[i] = true
            result.append(i)
            recur(num + 1)
            chkArr[i] = false
            result.removeLast()
        }
    }
}

```

<br><br>

## 시뮬레이션

<br><br>

## 투 포인터
- 처음부터 생각하기 어려움
- 연속하는 특징이 있는지 체크한다. 
- 투포인터 문제의 종류
    - 두개 다 왼쪽에서 // 각각 왼쪽, 오른쪽 // 다른 배열
- 시간복잡도
    - 일반적 ->>> `O(N)`
    - 정렬 후 투포인터를 하는 경우가 있음 ->>> `O(N * lgN)`

```swift
let input = readLine()!.split(separator: " ").map{ Int($0)! }
let (n, k) = (input[0], input[1])
let nums = readLine()!.split(separator: " ").map{ Int($0)! }

var each = 0
var maxv = 0
// K개를 더해주기
for i in 0..<k {
    each += nums[i]
}
maxv = each
// 다음 인덱스를 더해주고, 이전 인덱스를 빼주기

for i in k..<n {
    each += nums[i]
    each -= nums[i-k]
    maxv = max(maxv, each)
}
print(maxv)

```

<br><br>

## 이진 탐색
어떤 값을 찾을 때 정렬의 특징을 이용해 빨리 찾음
- 정렬이 되어있을 경우, 어떤 값을 찾을 때 ::: O(N) ->> O(lgN)
- 처음부터 생각하기 어려움.. 
- 시간 복잡도를 따져보고 시간이 초과하는 거라면 이진탐색을 떠올리도록 한다.  
- 시간복잡도
    - N개의 수 정렬 ::: `O(NlgN)`
    - N개의 수열에서 이진 탐색::: `O(lgN)`
    - M개의 수를 N개의 수열에서 이진 탐색::: `O(M * lgN)`


```swift
let n = Int(readLine()!)!
var nums = readLine()!.split(separator: " ").map{ Int($0)!}
let m = Int(readLine()!)!
let targetList = readLine()!.split(separator: " ").map{ Int($0)!}

nums.sort()

for i in targetList {
    binarySearch(0, n-1, i)
}


func binarySearch(_ start: Int, _ end: Int, _ target: Int) {
    if start == end {
        nums[start] == target ? print(1) : print(0)
        return
    }
    
    let mid = (start + end) / 2
    if nums[mid] < target {
        binarySearch(mid+1, end, target)
    } else {
        binarySearch(start, mid, target)
    }
}

```

<br><br>

### 그리디
때로는 당장 눈앞의 최선이 최고의 결과를 가져온다.  
- 현재 차례의 최고의 답을 찾는 문제
- 어려운 이유 : 이게 왜 최고인지 증명하기가 어려운 경우가 많다.
- 반례가 있을 수 있는지 체크해볼 것
- 예시
    - 각기 다른 종류의 동전이 주어졌을 때, M원을 만드는 최소 개수
    - 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자
    - 전체 학생수 n중, 도난당한 학생배열 lost, 여벌의 체육복가져온 학생번호배열 reverse를통해  적절히 빌려 최대한 많은 학생수 구하기
    - 사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값
    - n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용 



```swift
let input3 = """
10 4790
1
5
10
50
100
500
1000
5000
10000
50000
"""

let totalArr = input3.split(separator: "\n")
//let firstLine = totalArr[0].split(separator: " ").map{ Int($0)!}

let firstLine = readLine()!.split(separator: " ").map{ Int($0)!}
var (coinRow, target) = (firstLine[0], firstLine[1])
//var coins = totalArr[1...].map{Int($0)!}.sorted(by: >)
var coins = [Int]()
for _ in (0..<coinRow) {
    let coin = Int(readLine()!)!
    coins.append(coin)
}
coins.sort(by: >)

var count = 0
for coin in coins {
    count += target / coin
    target = target % coin
}
print(count)
```

<br><br>

### DP
이전의 값을 저장해서 재활용하는 알고리즘
- 패턴을 직접 그려보면서 규칙찾기
- 점화식을 명확하게 세워야 풀 수 있다.  

```swift

let n = Int(readLine()!)!
var result = [0, 1, 2] // 초기값 3개는 지정하기
for i in 3...n+1 {
    result.append((result[i-1] + result[i-2])%10007)
}
print(result[n])

```

<br><br>

### MST
- 모든 노드를 잇는데 최소비용이 드는 것
- MST는 정형화된 풀이 방법이 있음
- 대부분 양방향 간선이 있는 양방향 그래프 문제
- 사용 알고리즘
    - Kruskal : 
        - 전체 간선 중 가장 작은 것 부터 연결하는 방법
        - Union - Find 라는 알고리즘을 사용하는데, 코드 구현이 복잡함
    - Prim : 현재 연결된 트리에 이어진 간선 중 가장 작은 것을 추가
- 기본문제 : 최소의 비용으로 모든 노드가 연결된 트리
- 시간 복잡도
    - Edge 리스트에 저장 : O(E)
    - Heap안 모든 Edge에 연결된 간선 확인 : O(E+E)
    - 간선을 힙에 삽입 : O(lgE) -> 모든 간선을 삽입 -> O(lgE * E) = ElgE
    - O(E+ 2E + ElgE ) = O(3E + ElgE) = O(E(3+lgE)) ->> O(ElgE)
- 사용 자료구조 : Heap
    - 시간복잡도: lg(E)
    - Heap을 구현해야한다. `sort`를 사용하면 시간초과로인해 커스텀 구조체 사용 추천

- Edge 저장리스트 -> [(Int, Int)]
- 정점(노드) 방문 리스트 -> [Bool]
- MST 비용 -> Int

swift로 푸는 경우 
```swift
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


### 실제 MST구현 코드
백준
```swift
/// 1. 아이디어
/// - MST 기본문제, 외우기
///     - 간선을 인접리스트에 집어넣기
///     - 힙에 시작점 넣기
///     - 힙이 빌때까지 아래 작업
///         - 힙의 최소값 꺼내서, 해당 노드 방문 안했다면
///             - 방문 표시, 해당 비용추가, 연결된 간선들을 힙에 새롭게 추가
///
/// 2. 시간복잡도
///  - MST: O(ElgE)
///
///
/// 3. 자료구조
///  - 간선 저장되는 인접리스트 : (무게, 노드 번호)
///  - 힙 : (무게, 노드번호)
///  - 방문여부 : [Bool]
///  - MST 결과값 : Int

let input = """
3 3
1 2 1
2 3 2
1 3 3
"""

//let lines = input.split(separator: "\n").map { String($0) }
//let firstLine = lines[0].split(separator: " ").map { Int($0)! }
let firstLine = readLine()!.split(separator: " ").map{ Int($0)!}

let (v, e) = (firstLine[0], firstLine[1])

// 인접 리스트 초기화
//var edges = Array(repeating: [(Int, Int)](), count: v + 1)
var edges = Array(repeating: [Edge](), count: v + 1)

for i in 1...e {
//    let edgeData = lines[i].split(separator: " ").map { Int($0)! }
    let edgeData = readLine()!.split(separator: " ").map { Int($0)! }
    let (a, b, c) = (edgeData[0], edgeData[1], edgeData[2])
    // 양방향(무방향) 그래프인 경우 a에서 b로, b에서 a로 두번 추가
//    edges[a].append((c, b))
//    edges[b].append((c, a))
    
    edges[a].append(Edge(cost: c, node: b))
    edges[b].append(Edge(cost: c, node: a))

}
// edges
// [[], [(1, 2), (3, 3)], [(1, 1), (2, 3)], [(2, 2), (3, 1)]]

//var heap = [(0,1)] // 노드 시작지점
var heap = Heap<Edge>()
heap.insert(Edge(cost: 0, node: 1))

// 방문 리스트 초기화
var chk = Array(repeating: false, count: v + 1)

var rs = 0 // 총 무게

while !heap.isEmpty {
//    heap.sort(by: <) // heap의 동작처럼 최소값 순으로 정렬 ->> 시간 초과...!!!
//    let (w, eachNode) = heap.removeFirst() // heap을 pop
    guard let edge = heap.extractMin() else { break }
    let (w, eachNode) = (edge.cost, edge.node)

//    if !chk[eachNode] {
//        chk[eachNode] = true
//        rs += w
//        for nextEdge in edges[eachNode] {
//            if !(chk[nextEdge.1]) {
//                heap.insert(nextEdge)
//
////                heap.append(nextEdge)
//            }
//        }
//    }
    
    if !chk[eachNode] {
        chk[eachNode] = true
        rs += w
        for nextEdge in edges[eachNode] {
            if !chk[nextEdge.node] {
                heap.insert(nextEdge)
            }
        }
    }

}

print(rs)


```

<br><br>

## 노드 간의 최소 비용 구하기
- 한 점 -> 여러 점 ::: 다익스트라 사용
- 여러 점 -> 여러 점 ::: 플로이드 사용

### 다익스트라
- 그냥 외워서 사용할것
- 중요한건.. 해당 문제가 다익스트라 문제인지 알아보는게 중요
- 한 점에서 다른 모든 노드 까지 가는데 최소비용

- 시간복잡도 : `ElgV`

```swift

let input = """
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
"""

//let lines = input.split(separator: "\n").map { String($0) }
//let firstLine = lines[0].split(separator: " ").map { Int($0)! }
let firstLine = readLine()!.split(separator: " ").map{ Int($0)!}

let (v, e) = (firstLine[0], firstLine[1])
//let startV = Int(lines[1])!
let startV = Int(readLine()!)!

// 인접 리스트 초기화
var edges = Array(repeating: [Edge](), count: v + 1)
var distance = Array(repeating: Int.max, count: v + 1)
distance[1] = 0 // 시작 노드의 거리는 0

for i in 1...e{
//    let edgeData = lines[i].split(separator: " ").map { Int($0)! }
    let edgeData = readLine()!.split(separator: " ").map { Int($0)! }
    let (a, b, c) = (edgeData[0], edgeData[1], edgeData[2])
    // 양방향(무방향) 그래프인 경우 a에서 b로, b에서 a로 두번 추가
//    edges[a].append((c, b))
//    edges[b].append((c, a))
    
    edges[a].append(Edge(cost: c, node: b))
//    edges[b].append(Edge(cost: c, node: a))

}

var heap = Heap<Edge>()
heap.insert(Edge(cost: 0, node: startV))

while !heap.isEmpty {
    //    let (w, eachNode) = heap.removeFirst() // heap을 pop
    guard let edge = heap.extractMin() else { break }
    let (w, eachNode) = (edge.cost, edge.node)
    // w: 현재 비용
    // eachNode : 현재 노드
    /// 그 노드에 대한 거리가 최신의 최소 거리(distance[eachNode])와 일치하지 않으면
    if w != distance[eachNode] {
        continue
    }
    
    for nextEdge in edges[eachNode] {
        // 현재 관리중인 노드의 거리가 더 크면 갱신
        if distance[nextEdge.node] > distance[eachNode] + nextEdge.cost {
            distance[nextEdge.node] = distance[eachNode] + nextEdge.cost
            let newEdge = Edge(cost: distance[nextEdge.node], node: nextEdge.node)
            heap.insert(newEdge)
        }
    }
}

for i in 1...v {
    if distance[i] == Int.max {
        print("INF")
    } else {
        print(distance[i])
    }
}





```

<br><br>

### 플로이드
모든 노드에서 다른 모든 노드까지 가는데의 최소비용 
- 시간 복잡도 O(V^3)
- 비슷: 다익스트라 ::  한 노드에서 다른 모든 노드 O(ElgV)
    - 한 시작점에서 다른 점들을 구하는 것
- 플로이드 ::: 모든 노드를 시작점으로 모든 노드까지의 최소비용을 계산

```swift
import Foundation


// 입력 받기
let n = Int(readLine()!)!
let m = Int(readLine()!)!

// 무한대를 나타내는 값
let INF = Int.max

// 거리 행렬 초기화
// n+1로 하는 경우는 하나 더 추가해서 인덱스를 편하게 사용하기 위함
var rs = Array(repeating: Array(repeating: INF, count: n + 1), count: n + 1)

// 자기 자신으로 가는 비용은 0으로 초기화
for i in 1...n {
    rs[i][i] = 0
}

// 간선 정보 입력 받기
for _ in 0..<m {
    let edgeData = readLine()!.split(separator: " ").map { Int($0)! }
    let a = edgeData[0]
    let b = edgeData[1]
    let c = edgeData[2]
    rs[a][b] = min(rs[a][b], c) // a에서 b로 가는 최소 비용 갱신
}

// 플로이드-워셜 알고리즘 적용
for k in 1...n {
    for j in 1...n {
        for i in 1...n {
            
            if rs[j][k] != INF && rs[k][i] != INF { // 오버플로우 방지
                let sum = rs[j][k] + rs[k][i]
                if rs[j][i] > sum {
                    rs[j][i] = sum
                }
            }

        }
    }
}

// 결과 출력
for j in 1...n {
    for i in 1...n {

        if rs[j][i] == INF {
            print("0", terminator: " ")
//            print("INF", terminator: " ")

        } else {
            print(rs[j][i], terminator: " ")
        }
    }
    print()
}

```

<br><br>
