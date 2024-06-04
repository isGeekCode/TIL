# 알고리즘 템플릿


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
- 예시 : 각기 다른 종류의 동전이 주어졌을 때, M원을 만드는 최소 개수
- 반례가 있을 수 있는지 체크해볼 것
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

```swift
```

<br><br>

### MST

```swift
```

<br><br>

### 다익스트라

```swift
```

<br><br>

### 플로이드

```swift
```

<br><br>
