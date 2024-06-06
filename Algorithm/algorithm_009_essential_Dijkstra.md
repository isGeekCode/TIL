# 필수 알고리즘 - 다익스트라 (Dijkstra)

한 노드에서 다른 노드까지 가는데 최소비용  

<img width="461" alt="스크린샷 2024-06-06 오전 1 32 42" src="https://github.com/isGeekCode/TIL/assets/76529148/222082c3-afe3-43a8-b896-330f9673995c">


1 -> 2 :: 2가 든다.   
1 -> 3 :: 3이 든다.  
1 -> 4 :: (1)번으로 선택 :: 7이 든다.  
- (1) 1 -> 2 -> 4  :: 2 + 5 :: 7  
- (2) 1 -> 3 -> 4  :: 3 + 6 :: 9  
1 -> 5 :: 단방향만 가능하므로 갈 수 없다.   

최소비용 ::: `[2, 3, 7, X]`  

## 작동원리
- 간선(edge)저장 :: 인접리스트, 거리배열 : 초기값은 무한대로 설정, 힙 시작점 추가 [(0,1)]  

거리배열 초기값:::[INF, INF, INF, INF, INF]  

<img width="461" alt="스크린샷 2024-06-06 오전 1 32 42" src="https://github.com/isGeekCode/TIL/assets/76529148/222082c3-afe3-43a8-b896-330f9673995c">

힙 :::[(0,1)] // 시작점.. 1번에서 1만큼 가려면 0만큼 든다...  

힙은 가장 앞에있는 것으로 최대값 최소값을 구한다.    
거리배열 갱신 : [0, INF, INF, INF, INF]  
- 힙에서 노드를 때면서 간선을 통할때, 거리가 짧아진다면!  

->1번 노드를 빼서,, 1번과 간선으로 연결된 노드들을 갈때, 거리가 더 짧아진다면  
1 -> 2 ::: 2가 든다.   
거리배열 갱신 : [0, 2, INF, INF, INF]  
그리고 힙에 추가  
힙 갱신:::[(2,2)]  
1 -> 3 ::: 3이 든다.  
거리배열 갱신 : [0, 2, 3, INF, INF]  
힙 갱신:::[(2,2), (3,3)]  

여기까지 1번 노드에 대한 진행이 끝

이제 힙에 최소값인 2번 노드에 연결된 간선을 처리한다.   
->2번 노드를 빼서,, 2번과 간선으로 연결된 노드들을 갈때, 거리가 더 짧아진다면  
2 -> 4 ::: 이것은 1 -> 2 -> 4 로 가는 거기 때문에 기존의 2 + 5 ::: 7이 든다.   
거리배열 갱신 : [0, 2, 3, 7, INF]  
힙 갱신:::[(3,3), (7,4)]    
2 -> 3 ::: 이것은 1 -> 2 -> 3 으로 가는 것이 2 + 4 ::: 6 인데 이것 보다 1 -> 3 이 3이드는 비용이 더 적다.  
그렇기 때문에 이미 거리배열에서 3만큼 간다고 되어있어서 갱신할 필요가 없다.   
여기까지 2번 노드에 대한 진행이 끝  

이제 힙에 최소값인 3번 노드에 연결된 간선을 처리한다.   
->3번 노드를 빼서,, 3번과 간선으로 연결된 노드들을 갈때, 거리가 더 짧아진다면  
3 -> 4 ::: 이것은 1 -> 3 -> 4 로 가는 거기 때문에 기존의 3 + 6 ::: 9기 든다. 하지만 4로 가는 것은 1 2 4로가는게 기존에 이미 7이 더 적다고 판단되어있기 때문에 갱신 X  
거리배열 그대로  : [0, 2, 3, 7, INF]  
힙 갱신:::[(7,4)]  
2 -> 3 ::: 이것은 1 -> 2 -> 3 으로 가는 것이 2 + 4 ::: 6 인데 이것 보다 1 -> 3 이 3이드는 비용이 더 적다.  
그렇기 때문에 이미 거리배열에서 3만큼 간다고 되어있어서 갱신할 필요가 없다. 
여기까지 3번 노드에 대한 진행이 끝


<br><br>

이제 힙에 최소값인 4번 노드에 연결된 간선을 처리한다. 
->4번 노드를 빼서,, 4번과 간선으로 연결된 노드들을 갈때, 거리가 더 짧아진다면  
4번에서는 갈 수 있는 그래프가 없음.  
거리배열 그대로  : [0, 2, 3, 7, INF]  
힙 갱신:::[]  

마지막 1번에서는 5번으로 갈 수 있는 길 자체가 없기 대문에 INF 그대로 남겨둔다.  
결과 [0, 2, 3, 7, INF]

<br><br>

## 핵심 코드
```swift
import Foundation

let input = """
3 3
1 2 1
2 3 2
1 3 3
"""

let lines = input.split(separator: "\n").map { String($0) }
let firstLine = lines[0].split(separator: " ").map { Int($0)! }
//let firstLine = readLine()!.split(separator: " ").map{ Int($0)!}

let (v, e) = (firstLine[0], firstLine[1])

// 인접 리스트 초기화
//var edges = Array(repeating: [(Int, Int)](), count: v + 1)
var edges = Array(repeating: [Edge](), count: v + 1)
var distance = Array(repeating: Int.max, count: v + 1)
distance[1] = 0 // 시작 노드의 거리는 0

for i in 1...e {
    let edgeData = lines[i].split(separator: " ").map { Int($0)! }
//    let edgeData = readLine()!.split(separator: " ").map { Int($0)! }
    let (a, b, c) = (edgeData[0], edgeData[1], edgeData[2])
    // 양방향(무방향) 그래프인 경우 a에서 b로, b에서 a로 두번 추가
//    edges[a].append((c, b))
//    edges[b].append((c, a))
    
    edges[a].append(Edge(cost: c, node: b))
    edges[b].append(Edge(cost: c, node: a))

}
// edges
// [[], [(1, 2), (3, 3)], [(1, 1), (2, 3)], [(2, 2), (3, 1)]]

var heap = Heap<Edge>()
heap.insert(Edge(cost: 0, node: 1))

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

print(distance)




```
