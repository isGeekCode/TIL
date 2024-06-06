# 필수 알고리즘 - 플로이드 (Floyd)

모든 노드에서 다른 모든 노드까지 가는데의 최소비용 
- 시간 복잡도 O(V^3)
- 비슷: 다익스트라 ::  한 노드에서 다른 모든 노드 O(ElgV)
    - 한 시작점에서 다른 점들을 구하는 것
- 플로이드 ::: 모든 노드를 시작점으로 모든 노드까지의 최소비용을 계산


## 팁
- 그래프 거리문제가 나올때
    - 한점 -> 여러점 ::: 다익스트라
    - 여러점 -> 여러점 ::: 플로이드


## 작동원리
- 노드j -> 노드 i 비용 배열 만들기 , 초기값 :: INF
- 간선의 값을 비용 배열에 반영
- 모든 노드에 대해 해당 노드를 거쳐 가면서 비용이 작아질 경우에 갱신


<img width="461" alt="스크린샷 2024-06-06 오전 1 32 42" src="https://github.com/isGeekCode/TIL/assets/76529148/222082c3-afe3-43a8-b896-330f9673995c">

- 위 노드에 대하여 표를 만들면 아래와 같다. 아래 표는 각 j의 노드에서 i의 다른 노드까지의 거리를 나타냈다.  
- 초기값은 INF로 되어있다.  
- 각 간선의 비용을 배열에 반영했다.  

<img width="459" alt="스크린샷 2024-06-06 오후 12 01 11" src="https://github.com/isGeekCode/TIL/assets/76529148/57a48a44-da72-4469-892c-74e0951ac684">

1노드에 인접한 2번과 3번 노드 외에도 4번에 갈 수 있다. 
1 -> 2 -> 5 = 2 + 5
1 -> 3 -> 4 = 5 + 6

더 적은 비용은 1 -> 2 -> 5 경로이기 때문에 해당 값을 1 -> 5 위치에 갱신해준다.   
이런 방식으로 각 노드에서 모든 노드로 가는 비용을 업데이트 해준다. 

<img width="477" alt="스크린샷 2024-06-06 오후 12 01 16" src="https://github.com/isGeekCode/TIL/assets/76529148/2272ff1a-59d4-4b38-9367-9b5e5d57ec49">

그러면 시간 복잡도는 아래와 같이 된다. 

- 거치는 노드 :::: For Loop V
- 시작하는 노드 :::: For Loop V
- 끝나는 노드 :::: For Loop V

그래서 플로이드의 시간복잡도는 O(V^3)이 디된다.  

### 핵심 코드

```swift

// 입력 받기
let n = Int(readLine()!)! // 노드 수
let m = Int(readLine()!)! // 간선 수

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
for _ in 0..<m { // 간선의 개수 만큼
    let edgeData = readLine()!.split(separator: " ").map { Int($0)! }
    let a = edgeData[0]
    let b = edgeData[1]
    let c = edgeData[2]
    rs[a][b] = min(rs[a][b], c) // a에서 b로 가는 최소 비용 갱신
}

// 플로이드-워셜 알고리즘 적용
for k in 1...n { // 거치는 값
    for j in 1...n { // 시작
        for i in 1...n { // 도착
            
            if rs[j][k] != INF && rs[k][i] != INF { // 오버플로우 방지
                let sum = rs[j][k] + rs[k][i]
                if rs[j][i] > sum { // 현재 값보다 경유하는 비용이 더 작다면
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

<img width="545" alt="스크린샷 2024-06-06 오후 12 21 30" src="https://github.com/isGeekCode/TIL/assets/76529148/1ad389ce-a0b9-42cf-95c9-05d7403ee3b4">

## 기본문제
백준 11404 플로이드


