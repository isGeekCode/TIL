# 필수 알고리즘 - BFS: 너비 우선 탐색(Breath-first search)

## 그래프탐색 어떤것들이 연속해서 이어질 때, 모두 확인하는 방법

- 그래프탐색의 종류
    - BFS : 너비 우선 탐색(Breath-first search) -> 자신의 자식을 전체 살펴보는 방법
    - DFS : 깊이 우선 탐색(Depth-first search) -> 자식의 자식을 깊게 살펴보는 방법

- Vertex와 Edge
    - Vertex : 노드
    - Edge : 이어지는 것
    
    
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
