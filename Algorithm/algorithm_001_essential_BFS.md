# 필수 알고리즘 - BFS: 너비 우선 탐색(Breadth-First Search)

## 그래프탐색 어떤것들이 연속해서 이어질 때, 모두 확인하는 방법

- 그래프탐색의 종류
    - BFS : 너비 우선 탐색(Breadth-First Search) -> 자신의 자식을 전체 살펴보는 방법
    - DFS : 깊이 우선 탐색(Depth-First Search) -> 자식의 자식을 깊게 살펴보는 방법

- Vertex와 Edge
    - Vertex : 노드
    - Edge : 이어지는 것
    


## 간단 구현 접근방법

### BFS 메서드 밖에 필요한 변수 (전역)
- 1. 전체 행(n), 전체 열(m)
- 2. 전체 자료(grid) - 2차원 배열
- 3. 전체 자료의 방문 여부(visited) - 2차원 배열

### BFS 메서드 안에 필요한 변수
- 1. 검색할 queue
- 2. 현재 좌표
- 3. 현재 좌표를 기준으로 더할 상하좌우 좌표 수정할 변수
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

### 필요한 메서드
- 좌표가 방문할 대상에 해당하는지 체크하는 함수
- bfs 함수

### 로직정리
1. 이중 for문을 이용한 최초 순회
2. 1에서 얻은 좌표가 방문할 대상에 해당하는지 체크
3. 2에서 방문대상에 해당한다면 bfs메서드 시작
    - bfs메서드에 진입하며 현재 좌표 방문 체크, 현재 좌표를 Queue에 추가
    - Queue에 존재하는 좌표를 기준으로 4개의 인접 좌표를 for문으로 순회
        - 각 인접 좌표가 방문할 대상에 해당하는지 체크
        - 대상에 해당된다면 방문 여부 체크
        - 각 좌표를 Queue에 추가하여 다음 순서에서 해당 좌표의 인접 좌표를 수집하도록 처리

<br><br>

## BFS
간단정리 : 루트노드에서 시작해서 인접한 노드를 먼저 탐색하는 방법.

### BFS 구동 원리

**핵심 개념:**
- **큐(Queue, FIFO)** 사용: 먼저 들어간 것부터 꺼냄
- **가까운 것(같은 레벨)부터 넓게** 탐색
- **한 번 호출로 연결된 한 덩어리 전체** 탐색 완료

**동작 방식:**
1. 시작점을 큐에 넣고 방문 체크
2. 큐에서 하나 꺼내서 상하좌우 인접 노드 확인
3. 방문하지 않은 인접 노드를 큐에 추가 (먼저 발견한 것부터 들어감)
4. 큐가 빌 때까지 2-3 반복
5. → 결과: 시작점과 연결된 모든 노드 방문 완료 (한 덩어리 끝!)

**탐색 순서:**
- 시작점 → 거리 1인 노드들 → 거리 2인 노드들 → ...
- 레벨별로 넓게 퍼지며 탐색

<img width="300" alt="bfs" src="https://github.com/isGeekCode/TIL/assets/76529148/4771699e-e800-41ba-86d2-cc2da2988acc">

<br><br>

## BFS의 구현(with Queue)
- 시작점에 연결된 Vertex(노드)찾기
- 찾은 vertex를 Queue를 사용해서 저장
- Queue의 앞 순서부터 뽑아서 반복

### BFS의 시간복잡도
O(V+E)

- 1번 Vertex와 이에 연결된 Edge a,b
- 이를 이용해 a,b Edge에 연결된 Vertex 2, 5 가 추가됨
    - 2번 Vertex와 이에 연결된 Edge d, c
        - 이를 이용해 d,c Edge에 연결된 Vertex 3이 추가됨. (5는 이미 있음)
    - 5번 Vertex와 이에 연결된 Edge (c), f
        - 이를 이용해 c, f Edge에 연결된 Vertex 4가 추가됨.

### BFS의 자료구조
- 검색할 그래프
- 방문 여부 검색(재방문 금지)
- BFS를 실행할 Queue

## BFS가 유용한 경우

1. **최단 거리/최단 경로** 문제 (가중치가 없는 그래프)
   - BFS는 가까운 노드부터 탐색하므로 **최단 거리를 보장**
   - DFS는 경로를 찾을 수는 있지만 최단 경로를 보장하지 않음
2. **레벨별 탐색**이 필요한 경우
   - 같은 depth의 노드들을 먼저 탐색 (DFS는 불가능)
3. **모든 노드를 방문**해야 하는 경우 (DFS도 가능)
   - 연결된 영역(컴포넌트)의 개수나 크기를 구하는 문제
   - 예: 그림의 개수와 최대 넓이, 섬의 개수, 단지 번호 붙이기

## BFS 문제 풀이 예시

예시) [백준 1926 그림](https://www.acmicpc.net/problem/1926)

**참고:** 이 문제는 연결된 영역을 찾는 문제로 **BFS/DFS 둘 다 가능**합니다. 최단 거리가 필요한 게 아니므로 어떤 방법을 사용해도 됩니다.

 - 문제
 어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.


 
 - 입력
 첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. (단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)

 
 - 예제 입력 :
 ```
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
 ```

 
 
 - 출력
 첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라. 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.


 
 - 예제 출력 :
```
 4
 9
```

### 입력부분

#### 방법1: 공백으로 구분된 입력 (이 문제의 경우)
```
1 1 0 1 1
0 1 1 0 0
```

```swift
let firstLine = readLine()!.split(separator: " ").map { Int($0)! }
let (n, m) = (firstLine[0], firstLine[1])

var grid = [[Int]]()  // 2차원 배열로 도화지의 정보를 저장
for _ in 0..<n {
    let row = readLine()!.split(separator: " ").map { Int($0)! }
    grid.append(row)
}
```

#### 방법2: 공백 없이 붙어있는 입력인 경우
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

#### 테스트용 입력값
```swift
// 편의상 사용하기 위한 입력값
//let (n, m) = (6, 5)
//var grid = [
//    [1,1,0,1,1],
//    [0,1,1,0,0],
//    [0,0,0,0,0],
//    [1,0,1,1,1],
//    [0,0,1,1,1],
//    [0,0,1,1,1],
//]
```


### 이중 포문을 이용해 순회하며 조건에 맞는 경우 bfs메서드 실행
```swift
var visited = Array(repeating: Array(repeating: false, count: m), count: n)
var numPictures = 0 // 그림의 개수
var maxArea = 0     // 최대 그림의 넓이

for i in 0..<n { // 열
    for j in 0..<m { // 행
        if canVisit(i, j) {
            // 1이면 처리하는 부분
            let area = bfs(i, j) // 그림 하나당 한번 호출함
            numPictures += 1
            maxArea = max(maxArea, area) // 저장되어있던 maxArea와 area를 비교하여 갱신
        }
    }
}

print(numPictures)
print(maxArea)

```

### 방문가능 여부 체크 메서드 구현
여기서는 해당 부분에 1이고 방문하지 않은 경우에만 true를 리턴한다.
```swift
func canVisit(_ x: Int, _ y: Int) -> Bool {
    return grid[x][y] == 1 && !visited[x][y]
}
```



### bfs 메서드 구현
해당 지점을 기준으로 4가지 방향으로 체크
인근 4방향에 1이며, 방문하지 않은 조건을 달성하면 
queue에 해당 좌표 추가

인근에 3개가 발견되면 queue에 3개 좌표가 추가 
queue에 들어온 좌표들의 인근 좌표들을 연속적으로 계산
더이상 주변에 발견이 안될 때까지 체크 -> 그림 1개라는 뜻


```swift
func bfs(startX: Int, startY: Int) -> Int {
    let directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    var queue: [(Int, Int)] = [(startX, startY)] // 시작위치가 큐에 세팅
    var area = 0

    visited[startX][startY] = true // 방문여부 배열에 체크
    area = 1

    while !queue.isEmpty {
        let current = queue.removeFirst()
        
        for (dx, dy) in directions {

            let nx = current.0 + dx
            let ny = current.1 + dy
            
            if (nx >= 0 && nx < n) && (ny >= 0 && ny < m) { // 범위 이탈 체크
                if canVisit(nx, ny) { // 현재 체크하는 상하좌우에 1이 있는지, 방문을 안했는지
                    visited[nx][ny] = true // 방문체크
                    queue.append((nx, ny)) // 발견된 현재 위치를 큐에 추가 ( 큐의 순서대로 이접 4방향 체크 )
                    area += 1 // 방문X && 인접한 1을 발견할 때마다 1추가
                }
            }
        }
    }
    return area
}
```

