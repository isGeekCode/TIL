# 기본 문제 해결 - 그래프 탐색(Graph Search)

탐색이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 말함.  
프로그래밍에서는 그래프, 트리 등의 자료 구조 안에서 탐색하는 문제가 자주 나온다.  
대표적으로는 DFS(깊이 우선 탐색), BFS(너비 우선 탐색)를 들 수 있다.

이 원리를 제대로 이해해야 탐색 유형의 문제를 풀 수 있다.  
하지만 그러기 위해서는 기본 자료구조인 **Stack**, **Queue**, 그리고 **재귀함수**에 대한 이해가 전제되어야 한다.

→ 그래서 본격적인 탐색 문제 풀이에 들어가기 전에, 먼저 이 세 가지를 간단히 살펴보자.

---

## 🔍 자료구조 기초: Stack과 Queue

자료구조란 데이터를 표현하고 관리하고 처리하기 위한 구조를 의미한다.  
이 중 **스택(Stack)**과 **큐(Queue)**는 자료구조의 기초 개념으로, 두 핵심 연산을 중심으로 동작한다.

- **데이터 삽입 (push)**  
- **데이터 삭제 (pop)**

하지만 실제로 사용할 때는 다음과 같은 예외 상황도 함께 고려해야 한다:

- **오버플로 (Overflow)**: 특정 자료구조가 수용할 수 있는 데이터 크기를 초과할 때 발생  
- **언더플로 (Underflow)**: 비어 있는 상태에서 데이터를 삭제하려고 할 때 발생

이러한 기본 개념을 이해하고 나면, DFS와 BFS와 같은 탐색 알고리즘을 구현할 때 더 쉽게 응용할 수 있다.

---

## 🧱 스택(Stack)의 개념

스택은 흔히 **박스 쌓기**에 비유된다.  
아래에서 위로 차곡차곡 박스를 쌓고, 아래 있는 박스를 꺼내려면 **반드시 위에 있는 박스부터 꺼내야 한다.**

이러한 구조를 **선입후출 (FILO)** 또는 **후입선출 (LIFO)** 구조라고 부른다.

- **FILO**: First-In, Last-Out
- **LIFO**: Last-In, First-Out

즉, **나중에 넣은 데이터가 먼저 나오는 구조**로, 함수 호출 스택, 실행 취소(undo) 기능 등에 자주 사용된다.

---

말로 간단하게 써보면,  
`[]` 이 빈 스택 안에 다음과 같은 연산을 수행한다고 가정해보자.

- 삽입(5), 삽입(2), 삽입(3), 삽입(7), 삭제(), 삽입(1), 삽입(4)

이 과정을 따라가 보면, 스택의 변화는 다음과 같다:

```
[]  
→ [5]  
→ [5, 2]  
→ [5, 2, 3]  
→ [5, 2, 3, 7]  
→ [5, 2, 3]       // 7 삭제  
→ [5, 2, 3, 1]  
→ [5, 2, 3, 1, 4]
```

즉, 가장 나중에 들어간 7이 먼저 빠져나가는 구조임을 확인할 수 있다.

```swift
// ✅ 스택 동작 흐름 요약
// - stack 배열을 선언한다
// - append() 메서드로 데이터를 넣는다 (push)
// - removeLast() 메서드로 마지막 데이터를 꺼낸다 (pop)
// - 최종적으로 남은 스택 상태를 출력한다
/// 스택 예제 (Swift)
var stack: [Int] = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.removeLast()
stack.append(1)
stack.append(4)

print(stack) // [5, 2, 3, 1, 4]
```

> Swift에서는 `append()`로 push, `removeLast()`로 pop을 수행한다.

Swift에서는 별도로 Stack을 구현하지 않아도, 배열의 기본 메서드인 `append()`와 `removeLast()`를 사용하여 스택 자료구조와 동일하게 활용할 수 있다.

---

## 🧱 큐(Queue)의 개념

큐는 흔히 **줄 서기**에 비유된다.  
먼저 들어온 데이터가 먼저 나가는 구조로, **선입선출 (FIFO)** 구조라고 부른다.

- **FIFO**: First-In, First-Out

즉, **먼저 넣은 데이터가 먼저 나오는 구조**로, 프린터 작업 대기열, 프로세스 스케줄링 등에 자주 사용된다.

---

큐의 변화를 살펴보면,  
`[]` 이 빈 큐 안에 다음과 같은 연산을 수행한다고 가정해보자.

- 삽입(5), 삽입(2), 삽입(3), 삽입(7), 삭제(), 삽입(1), 삽입(4)

이 과정을 따라가 보면, 큐의 변화는 다음과 같다:

```
[]  
→ [5]  
→ [5, 2]  
→ [5, 2, 3]  
→ [5, 2, 3, 7]  
→ [2, 3, 7]       // 5 삭제  
→ [2, 3, 7, 1]  
→ [2, 3, 7, 1, 4]
```

즉, 가장 먼저 들어간 5가 먼저 빠져나가는 구조임을 확인할 수 있다.

```swift
// ✅ 큐 동작 흐름 요약
// - queue 배열을 선언한다
// - append() 메서드로 데이터를 넣는다 (enqueue)
// - removeFirst() 메서드로 가장 앞의 데이터를 꺼낸다 (dequeue)
// - 최종적으로 남은 큐 상태를 출력한다
/// 큐 예제 (Swift)
var queue: [Int] = []

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.removeFirst()
queue.append(1)
queue.append(4)

print(queue) // [2, 3, 7, 1, 4]
```

> Swift에서는 `append()`로 데이터를 넣고, `removeFirst()`로 데이터를 꺼내는 방식으로 큐를 구현할 수 있다.

---

## 🔁 재귀함수 (Recursion)

DFS와 BFS를 구현하려면 **재귀 함수**에 대한 이해도 중요하다.  
재귀함수란 **자기 자신을 다시 호출하는 함수**를 의미한다.

가장 간단한 구조는 다음과 같다:

```swift
func recursionFunc() {
    print("1")
    recursionFunc()
}
```

이 코드를 실행하면 `"1"`이 무한히 출력되다가 결국 **스택 오버플로(Stack Overflow)** 오류가 발생한다.  
→ 왜냐하면 함수가 자신을 무한히 호출하고 종료되지 않기 때문이다.

---

## ⛔️ 재귀함수의 종료 조건

재귀 함수에서 가장 중요한 개념은 **종료 조건**이다.  
언제 종료할지를 명확하게 설정하지 않으면 무한 루프에 빠진다.

따라서 재귀 함수 초반에는 반드시 종료 조건을 먼저 작성해야 한다:

```swift
func recursionFunc() {
    if 종료조건 {
        return
    }
    print("1")
    recursionFunc()
}
```

종료 조건은 문제에 따라 달라지지만, 항상 **첫 번째 조건문으로 배치**하는 습관을 들이자.

---

## 💡 재귀 함수 예제: 팩토리얼 (Factorial)

DFS와 같이 재귀로 구현되는 대표적인 알고리즘을 이해하기 전에,  
가장 간단한 재귀 함수 예제인 **팩토리얼(Factorial)** 문제를 먼저 살펴보자.

팩토리얼 기호는 `!`를 사용하며,  
예를 들어 `n!`은 다음과 같은 수학적 의미를 가진다:

```
n! = 1 × 2 × 3 × ... × (n-1) × n
```

- 예: `5! = 1 × 2 × 3 × 4 × 5 = 120`

수학적으로 **0! = 1! = 1**이라는 성질이 있다.  
→ 이 성질을 이용하면 종료 조건을 갖춘 재귀 함수로 쉽게 구현할 수 있다.

```swift
// ✅ 재귀로 팩토리얼 계산
// - n이 1 이하일 경우 1을 반환한다 (종료 조건)
// - 아니라면 n * factorial(n-1) 값을 반환
// - 호출이 끝날 때까지 스택처럼 쌓이고, 끝난 뒤 역순으로 계산
/// 팩토리얼 재귀 함수 (Swift)
func factorial(_ n: Int) -> Int {
    if n <= 1 {
        return 1
    }
    return n * factorial(n - 1)
}

print(factorial(5)) // 출력: 120
```

- `factorial(5)`는 내부적으로 `factorial(4)` → `factorial(3)` → ... 으로  
  계속 함수를 호출한 후, 역으로 결과값을 곱해가며 리턴하는 방식이다.
- 이처럼 **재귀 호출이 스택처럼 쌓였다가 역순으로 계산되며 풀리는 구조**를 갖는다는 점이 핵심이다.

---

## 🔀 반복문 방식과 재귀 방식 비교

팩토리얼 계산은 재귀 함수뿐 아니라 반복문으로도 동일하게 구현할 수 있다.  
두 방식은 개념적으로는 다르지만 결과적으로는 같은 값을 반환한다.

### ✅ 반복문 방식

```swift
// ✅ 반복문으로 팩토리얼 계산
// - result를 1로 초기화
// - 1부터 n까지 반복하며 result에 곱해나감
// - 최종적으로 계산된 값 반환
func factorialIterative(_ n: Int) -> Int {
    var result = 1
    for i in 1...n {
        result *= i
    }
    return result
}

print(factorialIterative(5)) // 출력: 120
```

- 루프를 통해 1부터 n까지 차례로 곱해 나가는 방식
- **스택 오버플로 걱정 없이 안정적**이며, 대부분의 환경에서 빠르게 실행됨

---

### 🔁 재귀 방식

```swift
// ✅ 재귀로 팩토리얼 계산 (함수 분리 버전)
// - 종료 조건: n <= 1 → 1 반환
// - 아닌 경우: n * factorialRecursive(n - 1) 반환
// - 호출을 통해 스택처럼 쌓이고, 되돌아오며 계산
func factorialRecursive(_ n: Int) -> Int {
    if n <= 1 {
        return 1
    }
    return n * factorialRecursive(n - 1)
}

print(factorialRecursive(5)) // 출력: 120
```

- 함수가 자기 자신을 호출하면서 계산을 미뤄두고,  
  호출이 끝난 후 **스택을 따라 되돌아가며 계산을 수행**

---

### 📌 두 방식의 비교

| 항목| 반복문 방식| 재귀 방식|
|----|----|----|
| 이해 난이도       | 비교적 쉬움 | 종료 조건 설정이 중요|
| 안정성           | 매우 높음 | 스택 오버플로 위험 존재|
| 실행 성능         | 보통 더 빠름 | 함수 호출 오버헤드로 느릴 수 있음  |
| 사용 예시         | 대부분의 루프 기반 계산 문제  | 트리, 그래프 탐색 등에 적합|

> 💡 일반적인 수치 계산에서는 반복문이 더 효율적이며,  
> 트리 구조 탐색 등은 재귀 방식이 간결하고 직관적이다.

---

## 🔎 재귀 함수와 점화식

두 방식의 차이는 무엇일까?  
재귀 방식은 코드가 **더 간결해진다**는 특징이 있다.  

이는 **수학의 점화식(Recurrence Relation)**을 그대로 코드로 옮겼기 때문이다.

### 📘 점화식이란?

점화식이란 특정 함수를 **자신보다 더 작은 변수에 대한 함수와의 관계로 표현한 것**을 의미한다.  
이 개념은 나중에 배울 **DP(동적 프로그래밍)**와도 이어지기 때문에 매우 중요하다.

팩토리얼을 수학적 점화식으로 표현하면 다음과 같다:

- n이 0 혹은 1일 때:  
  `factorial(n) = 1`
- n이 1보다 클 때:  
  `factorial(n) = n × factorial(n - 1)`

이 점화식을 그대로 코드로 옮기면 자연스럽게 재귀 함수가 완성된다.

> ✅ 일반적으로 우리는 **점화식에서 종료 조건**을 찾을 수 있다.  
> 팩토리얼 예시에서는 **n이 0 혹은 1일 때**가 종료 조건이다.

팩토리얼은 n이 양의 정수일 때만 유효하기 때문에,  
n이 1 이하인 경우에는 `1`을 반환할 수 있도록 재귀 함수를 작성해야 한다.

→ **재귀 함수에서는 반드시 종료 조건을 구현해야 한다는 점**을 다시 한 번 기억하자.

---

## 🌐 DFS (Depth-First Search, 깊이 우선 탐색)

DFS는 그래프에서 **깊은 부분을 우선적으로 탐색하는 알고리즘**이다.  
이해를 위해 먼저 **그래프의 기본 구조**를 살펴보자.

---

### 📌 그래프란?

그래프는 **노드(Node)**와 **간선(Edge)**으로 구성된 자료구조이다.  
- 노드는 **정점(Vertex)**이라고도 부른다.
- 간선은 노드 간의 **연결 관계**를 의미한다.

> 처음 접하는 사람에게는 다소 생소한 개념일 수 있지만,  
> 현실 세계에서 **도시 간 연결된 도로**로 비유하면 이해하기 쉽다.

예를 들어,  
A 도시에서 B 도시로 가기 위해 두 도시 사이에 도로가 있다면,  
이를 **노드 A와 B 사이에 간선이 존재하는 것**으로 생각하면 된다.

---

### 📘 그래프 표현 방식

프로그래밍에서 그래프를 표현하는 방식은 대표적으로 **2가지**가 있다:

| 방식 | 설명 | 특징 |
|------|------|------|
| 인접 행렬 | 2차원 배열을 사용하여 노드 간의 연결 관계를 표현 | 구현이 단순하지만, 메모리 사용 많음 |
| 인접 리스트 | 리스트를 사용하여 각 노드에 연결된 노드를 표현 | 메모리 효율적, 노드가 많을 때 유리 |

먼저 인접 행렬 방식은 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식이다.  
연결된 그래프를 인접 행렬로 표현할 때, Python에서는 2차원 리스트로 구현할 수 있다.  
연결이 되어있지 않은 노드끼리는 무한의 비용이라고 작성한다.  
실제 코드에서는 논리적으로 정답이 될 수 없는 큰 값 중에서 999999999, 또는 987654321 등의 값으로 초기화하는 경우가 많다.  
이렇게 그래프를 인접 행렬 방식으로 처리할 때는 다음과 같이 데이터를 초기화한다.

|   | 0   | 1   | 2   |
|---|-----|-----|-----|
| 0 | 0   | 7   | 5   |
| 1 | 7   | 0   | 무한 |
| 2 | 5   | 무한 | 0   |

```python
# Python 예시
INF = 999999999

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)
```

```swift
// Swift 예시
let INF = 999999999

let graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)
```

## 인접리스트 방식

이건 데이터를 어떤 방식으로 저장할까?  
인접 리스트 방식에서는 모든 노드에 연결된 노드의 정보를 차례대로 연결하여 저장한다.

예를 들어, 다음과 같은 가중치 그래프가 있다고 가정하자.

- 0번 노드: 1번 노드와 가중치 7, 2번 노드와 가중치 5로 연결
- 1번 노드: 0번 노드와 가중치 7로 연결
- 2번 노드: 0번 노드와 가중치 5로 연결

이를 인접 리스트 방식으로 표현하면 다음과 같다:

```
0 → 1(7) → 2(5)  
1 → 0(7)  
2 → 0(5)

# Python 코드로 인접 리스트 초기화 예시
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장 (노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1에 연결된 정보 저장
graph[1].append((0, 7))

# 노드 2에 연결된 정보 저장
graph[2].append((0, 5))

print(graph)


// Swift 코드로 인접 리스트 초기화 예시
var graph = Array(repeating: [(Int, Int)](), count: 3)

// 노드 0에 연결된 노드 정보 저장 (노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

// 노드 1에 연결된 정보 저장
graph[1].append((0, 7))

// 노드 2에 연결된 정보 저장
graph[2].append((0, 5))

print(graph)
```

인접 리스트 방식은 노드가 많고 간선이 적은 **희소 그래프**에서 메모리 효율이 뛰어난 방식이다.

---

## 📊 인접 행렬 vs 인접 리스트 비교 (코딩 테스트 관점)

그래프를 표현할 때 인접 행렬 방식과 인접 리스트 방식 중 어떤 것을 선택할지는 상황에 따라 다르며, 특히 **메모리와 속도 측면에서의 차이**를 이해하고 있어야 한다.

| 항목 | 인접 행렬 (Adjacency Matrix) | 인접 리스트 (Adjacency List) |
|------|--------|------------------|
| 메모리 사용량 | 모든 관계를 저장하므로 노드 수가 많을수록 메모리 낭비가 발생할 수 있음 | 연결된 정보만 저장하므로 메모리를 효율적으로 사용함 |
| 연결 여부 확인 속도 | O(1) — 두 노드가 연결되었는지 바로 확인 가능 | O(k) — 연결된 노드를 하나씩 순회해야 함 (k: 연결된 노드 수) |
| 구현 난이도 | 2차원 배열로 단순하게 구현 가능 | 리스트 구조로 노드마다 append가 필요 |
| 적합한 그래프 | 간선 수가 많은 **밀집 그래프(Dense Graph)** | 간선 수가 적은 **희소 그래프(Sparse Graph)** |

> ✅ 코딩 테스트에서는 그래프 크기(N)와 간선 수(M)의 범위를 보고  
> 어떤 방식이 유리할지 빠르게 판단하는 것이 중요하다.


## 🔍 DFS의 동작 원리

1. **탐색 시작 노드를 스택에 삽입**하고 방문 처리를 한다.  
   // 스택 상태: [1]
2. **스택의 최상단 노드에서 방문하지 않은 인접 노드가 있으면**, 그 인접 노드를 스택에 넣고 방문 처리한다.  
   방문하지 않은 인접 노드가 없다면 스택에서 최상단 노드를 꺼낸다.  
   // 스택 상태: [1, 2]
3. 이 과정을 **더 이상 수행할 수 없을 때까지 반복**한다.  
   // 스택 상태: [1, 2, 7]

> 🧠 "방문 처리"란, 스택에 한 번 삽입되어 처리된 노드가 **다시 삽입되지 않도록** 체크하는 것을 의미한다.  
> 이를 통해 각 노드를 **한 번씩만 탐색**하도록 보장할 수 있다.

DFS는 이처럼 **최대한 깊숙이 탐색**한 후, **더 이상 갈 수 없을 때 되돌아오는 백트래킹(backtracking)** 구조를 가진다.


아래 그래프를 보자


해당 그래프는 총 8개의 노드와 다음 간선들로 구성되어 있다

간선리스트
```
1 - 2  
1 - 3  
1 - 8  
2 - 7  
3 - 4  
3 - 5  
4 - 5  
6 - 7  
7 - 8  
```

각 노드에 연결된 간선들을 확인할수있는데 이게 어떤 순서로 스택에 삽입하고 방문처리를 할까  
1. 시작노드인 1을 스택에 삽입하고 방문처리를 한다.  
   // 스택 상태: [1]
2. 스택의 최상단 1에 방문하지않은 인접노드 2,3,8이 있다. 이중에서 가장 작은 노드인 2를 스택에 넣고 방문처리한다.  
   // 스택 상태: [1, 2]
3. 스택의 최상단 노드인 2에 방문하지않은 인접노드 7이 있다. 따라서 7번 노드를 스택에 넣고 방문처리한다.  
   // 스택 상태: [1, 2, 7]
4. 스택의 최상단 노드인 7에 방문하지않은 노드인 6과 8이 있다. 이중에서 가장 작은 노드인 6을 스택에 넣고 방문처리한다.  
   // 스택 상태: [1, 2, 7, 6]
5. 스택의 최상단 노드인 6에 방문하지않은 인접노드가 없다. 따라서 스택에서 6번 노드를 꺼낸다.  
   // 스택 상태: [1, 2, 7]
6. 스택의 최상단 노드인 7에 방문하지않은 인접노드 8이 있다. 그래서 8번 노드를 스택에 넣고 방문처리한다.  
   // 스택 상태: [1, 2, 7, 8]
7. 스택의 최상단 노드인 8에 방문하지않은 인접노드가 없다. 따라서 스택에서 8번 노드를 꺼낸다.  
   // 스택 상태: [1, 2, 7]
8. 스택의 최상단 노드인 7에 방문하지않은 인접노드가 없다. 따라서 스택에서 7번 노드를 꺼낸다.  
   // 스택 상태: [1, 2]
9. 스택의 최상단 노드인 2에 방문하지않은 인접노드가 없다. 따라서 스택에서 2번 노드를 꺼낸다.  
   // 스택 상태: [1]
10. 스택의 최상단 노드인 1에 방문하지않은 인접노드 3이 있다. 그래서 3번 노드를 스택에 넣고 방문처리한다.  
   // 스택 상태: [1, 3]
11. 스택의 최상단 노드인 3에 방문하지않은 인접노드 4와 5가 있다. 이 중에서 가장 작은 노드인 4를 스택에 넣고 방문처리한다.  
   // 스택 상태: [1, 3, 4]
12. 스택의 최상단 노드인 4에 방문하지않은 인접노드 5가 있다. 그래서 5번 노드를 스택에 넣고 방문처리한다.  
   // 스택 상태: [1, 3, 4, 5]
13. 남아있는 노드에 방문하지않은 인접노드가 없다. 따라서 모든 노드를 차례대로 꺼내면 다음과 같다.  
   // 스택 상태: [] (5 → 4 → 3 → 1 순으로 pop 예상)

👉 결과적으로 노드의 탐색 순서(스택에 들어간 순서)는 다음과 같다:  
`1 → 2 → 7 → 6 → 8 → 3 → 4 → 5`


DFS(깊이 우선 탐색) 알고리즘은 **스택 자료 구조에 기초**한다는 점에서 구현이 간단하다.  
실제로는 스택을 명시적으로 사용하지 않고도 재귀를 통해 동일한 로직을 수행할 수 있다.  
DFS는 탐색을 수행함에 있어 **노드의 수가 N개일 경우 O(N)**의 시간 복잡도를 가진다는 특징이 있다.


이걸 인접 리스트로 표현해보자
```swift
let graph = [
    [],          // 0번 노드는 사용하지 않음
    [2, 3, 8],   // 1
    [1, 7],      // 2
    [1, 4, 5],   // 3
    [3, 5],      // 4
    [3, 4],      // 5
    [7],         // 6
    [2, 6, 8],   // 7
    [1, 7]       // 8
]
```

잠깐 얘기하자면 인접행렬로 하면 아래와 같다
```
let graph = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0], // 0번 노드 (사용 안함)
    [0, 0, 1, 1, 0, 0, 0, 0, 1], // 1번 노드
    [0, 1, 0, 0, 0, 0, 0, 1, 0], // 2번 노드
    [0, 1, 0, 0, 1, 1, 0, 0, 0], // 3번 노드
    [0, 0, 0, 1, 0, 1, 0, 0, 0], // 4번 노드
    [0, 0, 0, 1, 1, 0, 0, 0, 0], // 5번 노드
    [0, 0, 0, 0, 0, 0, 0, 1, 0], // 6번 노드
    [0, 0, 1, 0, 0, 0, 1, 0, 1], // 7번 노드
    [0, 1, 0, 0, 0, 0, 0, 1, 0]  // 8번 노드
]
```

노드가 많을 수록 엄청 비효율적으로 변하니 명심!!


다시 인접 리스트로 해결해보면 

---

## 🧭 DFS 구현 흐름 (말코딩 → 코드)

먼저 DFS를 구현하기 전, 전형적인 흐름을 말코딩으로 정리해보자.

```text
// DFS 말코딩 요약
1. 현재 노드를 방문 처리한다.
2. 현재 노드와 연결된 다른 노드를 하나씩 확인한다.
3. 연결된 노드 중 방문하지 않은 노드가 있다면, 그 노드를 대상으로 DFS를 수행한다.
→ 위 과정을 재귀적으로 반복한다.
```

이제 이 흐름을 실제 코드로 옮겨보자.

### ✅ Python 코드

```python
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],          # 0번 노드는 사용하지 않음
    [2, 3, 8],   # 1
    [1, 7],      # 2
    [1, 4, 5],   # 3
    [3, 5],      # 4
    [3, 4],      # 5
    [7],         # 6
    [2, 6, 8],   # 7
    [1, 7]       # 8
]

visited = [False] * 9
dfs(graph, 1, visited)  # 출력: 1 2 7 6 8 3 4 5
```

---

### ✅ Swift 코드

```swift
func dfs(_ graph: [[Int]], _ v: Int, _ visited: inout [Bool]) {
    visited[v] = true
    print(v, terminator: " ")

    for i in graph[v] {
        if !visited[i] {
            dfs(graph, i, &visited)
        }
    }
}

let graph = [
    [],          // 0번 노드는 사용하지 않음
    [2, 3, 8],   // 1
    [1, 7],      // 2
    [1, 4, 5],   // 3
    [3, 5],      // 4
    [3, 4],      // 5
    [7],         // 6
    [2, 6, 8],   // 7
    [1, 7]       // 8
]

var visited = Array(repeating: false, count: 9)
dfs(graph, 1, &visited)  // 출력: 1 2 7 6 8 3 4 5
```


> DFS는 구현이 간단하지만, **그래프 구성 방식(인접 리스트 등)**과 함께 **방문 여부 체크**가 핵심 포인트다!



<br><br>


---

## 🌐 BFS (Breadth-First Search, 너비 우선 탐색)

BFS는 "너비 우선 탐색"이라는 의미를 가지며,  
쉽게 말해 **가까운 노드부터 탐색하는 알고리즘**이다.

DFS는 **최대한 멀리 있는 노드를 먼저 탐색**하는 방식인데,  
BFS는 그 반대로 **가까운 노드를 먼저 탐색**하는 것이 특징이다.

이를 위해 **선입선출(FIFO)** 구조인 **큐(Queue)** 자료구조를 사용한다.

BFS는 인접한 노드를 반복적으로 큐에 넣는 방식으로 동작하며,  
이 과정을 통해 **자연스럽게 가까운 노드부터 차례로 탐색**할 수 있다.

---

### 🔁 BFS 동작 흐름

1. 탐색 시작 노드를 **큐에 삽입**하고 **방문 처리**한다.  
2. 큐에서 노드를 꺼내고,  
   해당 노드에 **인접한 노드 중 방문하지 않은 노드를 모두 큐에 삽입**하고 방문 처리한다.  
3. 이 과정을 **더 이상 수행할 수 없을 때까지 반복**한다.

> ✅ DFS는 스택 기반으로 "깊이 우선",  
> ✅ BFS는 큐 기반으로 "너비 우선" 탐색이라는 점이 핵심이다.

---

## 🧭 BFS 동작 순서 (큐 시뮬레이션 기반)

아래는 BFS 알고리즘이 인접 리스트를 기반으로 어떤 순서로 동작하는지를 단계별로 설명한 내용이다. 각 단계마다 큐의 상태를 함께 표시하여 시각적으로 이해할 수 있도록 구성하였다.

```swift
let graph = [
    [],          // 0번 노드는 사용하지 않음
    [2, 3, 8],   // 1
    [1, 7],      // 2
    [1, 4, 5],   // 3
    [3, 5],      // 4
    [3, 4],      // 5
    [7],         // 6
    [2, 6, 8],   // 7
    [1, 7]       // 8
]
```

### BFS 탐색 순서 (시작 노드: 1)

1. 시작 노드인 `1`을 큐에 삽입하고 방문 처리를 한다.  
   **큐 상태**: `[1]`

2. 큐에서 `1`을 꺼내고, 방문하지 않은 인접 노드 `2, 3, 8`을 모두 큐에 삽입하고 방문 처리한다.  
   **큐 상태**: `[2, 3, 8]`

3. 큐에서 `2`를 꺼내고, 인접 노드 `1, 7` 중 방문하지 않은 노드 `7`을 큐에 삽입하고 방문 처리한다.  
   **큐 상태**: `[3, 8, 7]`

4. 큐에서 `3`을 꺼내고, 인접 노드 `1, 4, 5` 중 방문하지 않은 노드 `4, 5`를 큐에 삽입하고 방문 처리한다.  
   **큐 상태**: `[8, 7, 4, 5]`

5. 큐에서 `8`을 꺼내고, 인접 노드 `1, 7`은 모두 방문한 상태이므로 아무것도 하지 않는다.  
   **큐 상태**: `[7, 4, 5]`

6. 큐에서 `7`을 꺼내고, 인접 노드 `2, 6, 8` 중 방문하지 않은 노드 `6`을 큐에 삽입하고 방문 처리한다.  
   **큐 상태**: `[4, 5, 6]`

7. 큐에서 `4`를 꺼내고, 인접 노드 `3, 5`는 모두 방문한 상태이므로 아무것도 하지 않는다.  
   **큐 상태**: `[5, 6]`

8. 큐에서 `5`를 꺼내고, 인접 노드 `3, 4`는 모두 방문한 상태이므로 아무것도 하지 않는다.  
   **큐 상태**: `[6]`

9. 큐에서 `6`을 꺼내고, 인접 노드 `7`은 이미 방문했으므로 아무것도 하지 않는다.  
   **큐 상태**: `[]`

### ✅ 최종 탐색 순서 (BFS 결과)

`1 → 2 → 3 → 8 → 7 → 4 → 5 → 6`

---

## 🧭 BFS 구현 흐름 (말코딩 → 코드)

먼저 BFS를 구현하기 전, 전형적인 흐름을 말코딩으로 정리해보자.

```text
// BFS 말코딩 요약
1. 시작 노드를 큐에 삽입하고 방문 처리한다.
2. 큐에서 노드를 꺼내고, 인접한 노드를 순회하면서
   아직 방문하지 않은 노드들을 큐에 삽입하고 방문 처리한다.
3. 큐가 빌 때까지 이 과정을 반복한다.
→ 인접 노드를 큐에 넣을 때 방문 처리를 함께 해야 중복 탐색을 방지할 수 있다.
```

이제 이 흐름을 실제 코드로 옮겨보자.

### ✅ Python 코드

```python
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],          # 0번 노드는 사용하지 않음
    [2, 3, 8],   # 1
    [1, 7],      # 2
    [1, 4, 5],   # 3
    [3, 5],      # 4
    [3, 4],      # 5
    [7],         # 6
    [2, 6, 8],   # 7
    [1, 7]       # 8
]

visited = [False] * 9
bfs(graph, 1, visited)  # 출력: 1 2 3 8 7 4 5 6
```

---

### ✅ Swift 코드

```swift
import Foundation

func bfs(_ graph: [[Int]], _ start: Int, _ visited: inout [Bool]) {
    var queue: [Int] = [start]
    visited[start] = true

    while !queue.isEmpty {
        let v = queue.removeFirst()
        print(v, terminator: " ")

        for i in graph[v] {
            if !visited[i] {
                queue.append(i)
                visited[i] = true
            }
        }
    }
}

let graph = [
    [],          // 0번 노드는 사용하지 않음
    [2, 3, 8],   // 1
    [1, 7],      // 2
    [1, 4, 5],   // 3
    [3, 5],      // 4
    [3, 4],      // 5
    [7],         // 6
    [2, 6, 8],   // 7
    [1, 7]       // 8
]

var visited = Array(repeating: false, count: 9)
bfs(graph, 1, &visited)  // 출력: 1 2 3 8 7 4 5 6

---

## 📌 그래프 탐색 치트시트 (Graph Search Cheatsheet)

### 🔎 그래프 탐색이란?
- 많은 데이터 중 **원하는 데이터를 찾는 과정**
- 대표 알고리즘: **DFS (깊이 우선 탐색)**, **BFS (너비 우선 탐색)**
 
---

### 🧱 기본 자료구조

| 자료구조 | 특징 | 사용 메서드 (Swift) |
|----------|------|----------------------|
| Stack    | 후입선출 (LIFO) | `append()`, `removeLast()` |
| Queue    | 선입선출 (FIFO) | `append()`, `removeFirst()` |

---

### 📐 그래프 표현 방식

| 방식 | 설명 | 메모리 | 연결확인속도 |
|------|------|--------|------------------|
| 인접 행렬 | 2차원 배열로 연결 표현 | O(N²) | O(1) |
| 인접 리스트 | 리스트로 연결 표현 | O(N+M) | O(k) (연결된 노드 수) |

- **밀집 그래프**: 인접 행렬
- **희소 그래프**: 인접 리스트

> ✅ 노드 수 `N`, 간선 수 `M`을 보고 선택

---

### 🧭 DFS (Depth-First Search)

| 항목 | 설명 |
|------|------|
| 탐색방식 | 최대한 깊이 들어간 뒤, 더 이상 갈 곳 없으면 되돌아감 |
| 자료구조 | **Stack** (또는 **재귀**) |
| 방문순서 | 깊이 우선 |
| 구현 난이도 | 간단함 (재귀로 처리 가능) |
| 시간복잡도 | **O(N)** (노드 수 기준) |

**DFS 말코딩 요약**:
1. 현재 노드를 방문 처리
2. 인접 노드 중 방문 안한 노드에 대해 DFS 호출
3. 재귀적으로 반복

---

### 🧭 BFS (Breadth-First Search)

| 항목 | 설명 |
|------|------|
| 탐색방식 | 가까운 노드부터 순차적으로 탐색 |
| 자료구조 | **Queue** |
| 방문순서 | 너비 우선 |
| 구현 난이도 | 간단함 (반복문 사용) |
| 시간복잡도 | **O(N)** (노드 수 기준) |

**BFS 말코딩 요약**:
1. 시작 노드를 큐에 삽입하고 방문 처리
2. 큐에서 노드 꺼내고 인접 노드 탐색
3. 방문 안한 노드는 큐에 삽입하고 방문 처리

---

### 🎯 언제 DFS, 언제 BFS?

| 상황 | DFS | BFS |
|------|-----|-----|
| 경로 찾기 (모든 경우 탐색) | ✅ | ❌ |
| 최단 거리 찾기 | ❌ | ✅ |
| 재귀 기반 백트래킹 | ✅ | ❌ |
| 미로, 퍼즐, 조합 | ✅ | ❌ |
| 레벨 순서 탐색 | ❌ | ✅ |

---

### 🧠 기억할 것!

- ✅ DFS는 재귀 or 스택 기반  
- ✅ BFS는 큐 기반  
- ✅ 방문 여부는 항상 따로 `visited` 배열로 체크  
- ✅ DFS는 백트래킹, BFS는 최단거리에서 자주 등장  
- ✅ Swift에서 스택은 `append` / `removeLast`, 큐는 `append` / `removeFirst`로 구현
```

> BFS는 큐를 기반으로 동작하며, 방문 체크와 함께 큐에 넣는 타이밍이 핵심이다.
