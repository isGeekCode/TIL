# 필수 알고리즘 - DFS: 깊이 우선 탐색(Depth-First Search)

## 그래프탐색 어떤것들이 연속해서 이어질 때, 모두 확인하는 방법

- 그래프탐색의 종류
    - BFS : 너비 우선 탐색(Breadth-First Search) -> 자신의 자식을 전체 살펴보는 방법
    - DFS : 깊이 우선 탐색(Depth-First Search) -> 자식의 자식을 깊게 살펴보는 방법

- Vertex와 Edge
    - Vertex : 노드
    - Edge : 이어지는 것



## 간단 구현 접근방법

### DFS 메서드 밖에 필요한 변수 (전역)
- 1. 전체 행(n), 전체 열(m)
- 2. 전체 자료(grid) - 2차원 배열
- 3. 전체 자료의 방문 여부(visited) - 2차원 배열

### DFS 메서드 안에 필요한 변수
- 1. 현재 좌표
- 2. 현재 좌표를 기준으로 더할 상하좌우 좌표 수정할 변수
    - 방법1 (타이핑 빠름):
        ```swift
        let dx = [0, 1, 0, -1]
        let dy = [1, 0, -1, 0]

        for i in 0..<4 {
            let nx = x + dx[i]
            let ny = y + dy[i]
        }
        ```
    - 방법2 (가독성 좋음):
        ```swift
        let directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for (dx, dy) in directions {
            let nx = x + dx
            let ny = y + dy
        }
        ```
- 3. 스택 방식을 사용할 경우 stack 변수 필요 (재귀는 불필요)

### 필요한 메서드
- 좌표가 방문할 대상에 해당하는지 체크하는 함수
- dfs 함수 (재귀 또는 스택 방식)

### 로직정리
1. 이중 for문을 이용한 최초 순회
2. 1에서 얻은 좌표가 방문할 대상에 해당하는지 체크
3. 2에서 방문대상에 해당한다면 dfs메서드 시작
    - dfs메서드에 진입하며 현재 좌표 방문 체크
    - 현재 좌표를 기준으로 4개의 인접 좌표를 for문으로 순회
        - 각 인접 좌표가 방문할 대상에 해당하는지 체크
        - 대상에 해당된다면 방문 여부 체크 후 재귀 호출 (또는 스택에 추가)
        - 더 이상 방문할 곳이 없을 때까지 깊게 탐색

<br><br>

## DFS
간단정리 : 루트노드에서 시작해서 다음 분기로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법.

### DFS 구동 원리

**핵심 개념:**
- **스택(Stack, LIFO) 또는 재귀** 사용: 마지막에 들어간 것부터 꺼냄
- **깊게 들어갔다가 되돌아오는(백트래킹)** 방식
- **한 번 호출로 연결된 한 덩어리 전체** 탐색 완료

**동작 방식 (재귀):**
1. 현재 위치 방문 체크
2. 인접한 노드 중 방문하지 않은 곳 발견
3. → 즉시 그곳으로 이동(재귀 호출) - 계속 깊게!
4. 더 이상 갈 곳이 없으면 이전 위치로 되돌아옴(백트래킹)
5. 다른 인접 노드 탐색
6. → 결과: 시작점과 연결된 모든 노드 방문 완료 (한 덩어리 끝!)

**동작 방식 (스택):**
- 재귀와 동일하지만, 함수 호출 대신 스택에 좌표를 직접 관리
- `stack.removeLast()`로 가장 최근 좌표부터 처리 → 깊게 탐색

**탐색 순서:**
- 1번 노드 → 2번(1의 자식) → 3번(2의 자식) → ... 끝까지
- → 되돌아와서 → 2번의 다른 자식 → ...
- 한 방향으로 끝까지 깊게 들어갔다 나옴

<img width="300" alt="dfs" src="https://github.com/isGeekCode/TIL/assets/76529148/9f27c948-1a04-481f-beee-96ae91e836ff">


## DFS의 구현

DFS는 두 가지 방식으로 구현 가능합니다:
1. **재귀 함수** 사용 (일반적으로 더 간단함)
2. **스택(Stack)** 사용

### DFS의 시간복잡도
O(V+E)

- 1번 Vertex와 이에 연결된 Edge를 모두 탐색
- 각 Vertex마다 연결된 모든 Edge를 확인하므로 V+E

### DFS의 자료구조
- 검색할 그래프
- 방문 여부 검색(재방문 금지)
- DFS를 실행할 Stack (또는 재귀 함수의 Call Stack)


## DFS 구현 예시 1: 재귀 방식

가장 일반적이고 간단한 방식입니다.

```swift
var visited = Array(repeating: Array(repeating: false, count: m), count: n)
var numAreas = 0
var maxArea = 0

func canVisit(_ x: Int, _ y: Int) -> Bool {
    return grid[x][y] == 1 && !visited[x][y]
}

func dfs(_ x: Int, _ y: Int) -> Int {
    let directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    visited[x][y] = true
    var area = 1

    for (dx, dy) in directions {
        let nx = x + dx
        let ny = y + dy

        if (nx >= 0 && nx < n) && (ny >= 0 && ny < m) {
            if canVisit(nx, ny) {
                area += dfs(nx, ny) // 재귀 호출로 깊이 우선 탐색
            }
        }
    }

    return area
}

// 메인 로직
for i in 0..<n {
    for j in 0..<m {
        if canVisit(i, j) {
            let area = dfs(i, j)
            numAreas += 1
            maxArea = max(maxArea, area)
        }
    }
}

print(numAreas)
print(maxArea)
```

## DFS 구현 예시 2: 스택 방식

재귀를 사용하지 않고 명시적으로 스택을 사용하는 방식입니다.

```swift
var visited = Array(repeating: Array(repeating: false, count: m), count: n)
var numAreas = 0
var maxArea = 0

func canVisit(_ x: Int, _ y: Int) -> Bool {
    return grid[x][y] == 1 && !visited[x][y]
}

func dfsWithStack(_ startX: Int, _ startY: Int) -> Int {
    let directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    var stack: [(Int, Int)] = [(startX, startY)]
    var area = 0

    visited[startX][startY] = true

    while !stack.isEmpty {
        let current = stack.removeLast() // 스택이므로 마지막 요소 제거
        area += 1

        for (dx, dy) in directions {
            let nx = current.0 + dx
            let ny = current.1 + dy

            if (nx >= 0 && nx < n) && (ny >= 0 && ny < m) {
                if canVisit(nx, ny) {
                    visited[nx][ny] = true
                    stack.append((nx, ny)) // 스택에 추가하여 나중에 탐색
                }
            }
        }
    }

    return area
}

// 메인 로직
for i in 0..<n {
    for j in 0..<m {
        if canVisit(i, j) {
            let area = dfsWithStack(i, j)
            numAreas += 1
            maxArea = max(maxArea, area)
        }
    }
}

print(numAreas)
print(maxArea)
```

## BFS vs DFS 비교

| 특징 | BFS | DFS |
|------|-----|-----|
| 자료구조 | Queue (FIFO) | Stack (LIFO) 또는 재귀 |
| 탐색 방식 | 너비 우선 (가까운 것부터) | 깊이 우선 (깊은 것부터) |
| 최단 경로 | 보장함 | 보장 안함 |
| 메모리 사용 | 많음 (넓게 저장) | 적음 (깊이만큼만) |
| 적합한 경우 | 최단 거리, 레벨 탐색 | 경로 존재 여부, 백트래킹 |

## DFS가 유용한 경우

1. **모든 경로를 탐색**해야 하는 경우
2. **백트래킹** 문제 (미로 찾기, 스도쿠 등)
3. **사이클 감지** 문제
4. **위상 정렬** 문제
5. 메모리가 제한적인 경우 (BFS보다 메모리 효율적)


## DFS 문제 풀이 예시

예시) [백준 2667 단지번호붙이기](https://www.acmicpc.net/problem/2667)

**참고:** 이 문제는 연결된 영역을 찾는 문제로 **BFS/DFS 둘 다 가능**합니다. 최단 거리가 필요한 게 아니므로 어떤 방법을 사용해도 됩니다.

- 문제
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

- 입력
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

- 예제 입력:
```
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
```

- 출력
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

- 예제 출력:
```
3
7
8
9
```

![](https://i.imgur.com/V6PibMP.png)

### 입력부분

#### 방법1: 공백 없이 붙어있는 입력 (이 문제의 경우)
```
0110100
0110101
```

```swift
let n = Int(readLine()!)!

var grid = Array(repeating: Array(repeating: 0, count: n), count: n)
for r in 0..<n {
    let line = Array(readLine()!)              // ["0","1","1"...] 문자 배열
    for c in 0..<n {
        grid[r][c] = Int(String(line[c]))!     // 0/1로 변환
    }
}
```

#### 방법2: 공백으로 구분된 입력인 경우
```
1 1 0 1 1
0 1 1 0 0
```

```swift
let firstLine = readLine()!.split(separator: " ").map { Int($0)! }
let (n, m) = (firstLine[0], firstLine[1])

var grid = [[Int]]()
for _ in 0..<n {
    let row = readLine()!.split(separator: " ").map { Int($0)! }
    grid.append(row)
}
```

#### 테스트용 입력값
```swift
// 편의상 사용하기 위한 입력값
//let n = 7
//var grid = [
//    [0,1,1,0,1,0,0],
//    [0,1,1,0,1,0,1],
//    [1,1,1,0,1,0,1],
//    [0,0,0,0,1,1,1],
//    [0,1,0,0,0,0,0],
//    [0,1,1,1,1,1,0],
//    [0,1,1,1,0,0,0],
//]
```

### 이중 포문을 이용해 순회하며 조건에 맞는 경우 dfs메서드 실행

```swift
var visited = Array(repeating: Array(repeating: false, count: n), count: n)
var complexSizes = [Int]() // 각 단지의 크기를 저장할 배열

for i in 0..<n {
    for j in 0..<n {
        if canVisit(i, j) {
            // 1이면 처리하는 부분
            let size = dfs(i, j)
            complexSizes.append(size)
        }
    }
}

// 오름차순 정렬
complexSizes.sort()

print(complexSizes.count) // 단지 수
for size in complexSizes {
    print(size) // 각 단지의 크기
}
```

### 방문가능 여부 체크 메서드 구현

여기서는 해당 부분에 1이고 방문하지 않은 경우에만 true를 리턴한다.

```swift
func canVisit(_ x: Int, _ y: Int) -> Bool {
    return grid[x][y] == 1 && !visited[x][y]
}
```

### dfs 메서드 구현 (재귀 방식)

해당 지점을 기준으로 4가지 방향으로 체크하며 재귀적으로 탐색

```swift
func dfs(_ x: Int, _ y: Int) -> Int {
    let dx = [0, 1, 0, -1]
    let dy = [1, 0, -1, 0]

    visited[x][y] = true // 방문 체크
    var count = 1 // 현재 집 카운트

    for i in 0..<4 {
        let nx = x + dx[i]
        let ny = y + dy[i]

        if (nx >= 0 && nx < n) && (ny >= 0 && ny < n) { // 범위 이탈 체크
            if canVisit(nx, ny) {
                count += dfs(nx, ny) // 재귀 호출로 연결된 집 카운트
            }
        }
    }

    return count
}
```

## DFS 고급 활용: 사이클 감지

DFS를 사용하면 그래프에서 사이클(순환)을 감지할 수 있습니다.

### 3가지 상태로 사이클 감지

일반적인 방문 여부(true/false) 대신 **3가지 상태**를 사용합니다:
- **0**: 미방문 (아직 방문 안함)
- **1**: 방문 중 (현재 DFS 탐색 경로에 있음)
- **2**: 방문 완료 (탐색 끝남)

### 사이클 감지 원리

- 다음 노드의 상태가 **1 (방문 중)**이면 → **사이클 발견!**
  - 현재 탐색 경로에서 다시 만났다는 뜻
- 다음 노드의 상태가 **2 (방문 완료)**면 → 괜찮음
  - 이미 탐색 완료된 다른 경로

### 구현 예시

```swift
var state = Array(repeating: 0, count: n+1)
var hasCycle = false

func dfs(_ v: Int) {
    state[v] = 1            // 방문 중 상태로 변경

    for nx in graph[v] {
        if state[nx] == 0 {
            // 미방문 노드 → 재귀 탐색
            dfs(nx)
        } else if state[nx] == 1 {
            // 방문 중인 노드를 다시 만남 → 사이클!
            hasCycle = true
            return
        }
        // state[nx] == 2 (방문 완료)면 무시
    }

    state[v] = 2            // 방문 완료 상태로 변경
}

// 사용 예시
for i in 1...n {
    if state[i] == 0 {
        dfs(i)
        if hasCycle {
            print("사이클 존재")
            break
        }
    }
}
```

### 핵심 포인트

1. **state[v] = 1** : DFS 진입 시 "방문 중" 표시
2. **state[nx] == 1** 체크: 현재 경로에서 다시 만남 = 사이클
3. **state[v] = 2** : DFS 종료 시 "방문 완료" 표시

이 방법은 **방향 그래프(Directed Graph)**에서 사이클을 감지할 때 유용합니다.
