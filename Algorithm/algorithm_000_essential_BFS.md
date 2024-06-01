# 필수 알고리즘 - BFS: 너비 우선 탐색(Breath-first search)

## 그래프탐색 어떤것들이 연속해서 이어질 때, 모두 확인하는 방법

- 그래프탐색의 종류
    - BFS : 너비 우선 탐색(Breath-first search) -> 자신의 자식을 전체 살펴보는 방법
    - DFS : 깊이 우선 탐색(Depth-first search) -> 자식의 자식을 깊게 살펴보는 방법

- Vertex와 Edge
    - Vertex : 노드
    - Edge : 이어지는 것
    


## 간단 구현 접근방법
- 필요한 변수
    - 1. 전체 행, 전체 열
    - 2. 전체 자료
    - 3. 전체 자료의 방문 여부
    - 4. 검색할 queue
    - 5. 현재 좌표
    - 6. 현재 좌표를 기준으로 더할 상하좌우 좌표 수정할 변수 
        - `let directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]`
- 필요한 메서드
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


현재 기준점에 연결된 자식들을 순회한다. 더이상 순회할 게 없다면
첫번째 자식에 연결된 자식을 기준으로 다시 여기에 연결된 자식들을 순회한다.
1. 이때, 이전에 수집했던 내용이라면 제외하며 수집한다.
2. 이때, 현재 노드의 자식들을 순회할때, 순서를 확인하자

<img width="300" alt="bfs" src="https://github.com/isGeekCode/TIL/assets/76529148/4771699e-e800-41ba-86d2-cc2da2988acc">

<br><br>

## DFS
현재 기준점의 자식들을 순회하는 우선순위는 수집중인 노드의 첫번째 자식여부다.
예시 ) 

1번 노드의 첫번째 자식(2)에게 또 자식이 있다면 2번 자식 다음엔 1번노드의 다른 자식이 아닌 2번 자식의 첫번째 자식에게 이동된다. 

2번 자식의 첫번째 자식에게 이동후 더이상 자식이 없다면 다시 하나 거슬러 올라가 2번 자식의 두번째 자식에게 이동한다. 

이런식으로 깊게 타고 내려가는 것이 특징이다. 
   
<img width="300" alt="dfs" src="https://github.com/isGeekCode/TIL/assets/76529148/9f27c948-1a04-481f-beee-96ae91e836ff">


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


예시) [백준 1926 그림](https://www.acmicpc.net/problem/1926)
 
 - 문제
 어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.


 
 - 입력
 첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. (단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)

 
 - 예제 입력 :
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
 
 
 - 출력
 첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라. 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.


 
 - 예제 출력 :
 4
 9


### 입력부분
 
```swift
let firstLine = readLine()!.split(separator: " ").map { Int($0)! }
let (n, m) = (firstLine[0], firstLine[1])

var grid = [[Int]]()  // 2차원 배열로 도화지의 정보를 저장
for _ in 0..<n {
    let row = readLine()!.split(separator: " ").map { Int($0)! }
    grid.append(row)
}

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

