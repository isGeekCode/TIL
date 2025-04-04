# 필수 알고리즘 - 그리디 (Greedy)
이번에는 **그리디 알고리즘(Greedy Algorithm)**을 공부해보자.  
그리디는 **매 순간 최적이라고 생각되는 선택을 하는 방식**으로 문제를 해결하는 알고리즘이다.

일반적으로 전체적인 최적 해를 보장하지 않지만,  
문제의 조건에 따라 **그리디 방식이 정당화**되는 경우엔 매우 효율적이다.

가장 대표적인 예시로는 다음과 같다:
- 각기 다른 종류의 동전이 주어졌을 때, M원을 만드는 최소 동전 개수
- 회의실 배정 문제
- 배낭 문제 (일부 경우)

이 글에서는 대표 문제를 중심으로 그리디의 핵심 개념과 적용 방법을 정리해본다.

이 그리디 알고리즘(탐욕법)은 **현재 상황에서 지금 당장 좋은 것만 고르는 방법**을 의미한다.  
이 문제 유형의 특징은, **사전에 정확히 외우고 있지 않아도 직관적으로 풀 수 있는 가능성**이 높다는 점이다.

반면에 정렬, 최단 경로 알고리즘처럼 **정해진 로직을 알아야만 풀 수 있는 문제**들과는 다르게,  
그리디 문제는 문제에서 제공하는 조건을 잘 해석하고,  
선택 기준만 제대로 세우면 풀리는 경우가 많다.

물론, 이렇게 사전 지식 없이도 풀 수 있는 경우도 있지만  
실제로는 **많은 문제 유형을 접하며 훈련**하는 과정이 매우 중요하다.  

코딩 테스트에서 자주 출제되는 그리디 문제들은  
단순 구현보다는 **창의력**, 즉 **핵심 아이디어를 떠올리는 능력**을 요구한다.  
다시 말해, **현재 상황에서 가장 좋아 보이는 선택이 진짜 정답이 되는지**를 판단할 수 있어야 한다.

이 유형은 주로 “기준에 따라 좋은 것을 선택”하는 방식으로 문제를 풀게 되는데,  
문제에서 힌트처럼 **‘가장 큰 순서대로’**, **‘가장 작은 순서대로’** 와 같은 조건이 등장한다.  

따라서 **정렬 알고리즘**과 함께 출제되는 경우가 많으며,  
그리디 문제를 제대로 풀기 위해선 정렬과 함께 사고하는 습관도 중요하다.

<br><br>

## 기본 문제
백준 11047 동전

### 💰 예제 - 거스름돈 문제 (기본 그리디)

대표적인 그리디 문제로 **거스름돈 문제**가 있다.

**문제 설명**  
음식점의 계산을 도와주는 점원이 있다.  
카운터에는 거스름돈으로 사용할 동전 500원, 100원, 50원, 10원짜리가 무한히 존재한다고 가정한다.  
손님에게 줄 거스름돈이 `N`원일 때,  
**동전의 총 개수가 최소가 되도록 거슬러 줄 수 있는 방법**을 구하라.

단, `N`은 항상 10의 배수이다.

**접근 방법**  
- 가장 큰 단위부터 가능한 만큼 먼저 거슬러 준다.
- 남은 금액을 다음으로 큰 단위 동전으로 처리한다.
- 그리디 알고리즘의 대표적인 방식인 **큰 순서대로 정렬 후 처리** 방식이다.

```swift
/*
 [문제 해결 아이디어]
 1. 가장 큰 동전부터 순서대로 선택한다.
 2. 해당 동전으로 거슬러 줄 수 있는 최대 개수를 계산해 count에 더한다.
 3. 남은 금액은 해당 동전을 사용하고 남은 나머지로 갱신한다.
 4. 이를 반복하면 동전의 개수를 최소로 만들 수 있다.
*/
func getCoinCount(_ n: Int) -> Int {
    var amount = n
    var count = 0
    let coins = [500, 100, 50, 10]

    for coin in coins {
        count += amount / coin
        amount %= coin
    }
    return count
}

let result = getCoinCount(1260)
print(result) // 출력: 6
```

- 1260원은 500×2 + 100×2 + 50×1 + 10×1 → 총 6개의 동전
- 항상 가장 큰 단위부터 선택하므로, 이 문제는 그리디 알고리즘으로 정확하게 해결 가능

### 🔢 예제 - 큰 수의 법칙

전형적인 그리디 알고리즘 유형 중 하나는 **큰 수의 법칙**이다.

**문제 설명**  
다양한 수로 이루어진 배열이 있을 때,  
주어진 수들을 **M번 더하여 가장 큰 수를 만드는 법칙**이 있다.  
단, 배열의 특정 인덱스에 해당하는 수가 **연속해서 K번을 초과하여 더해질 수는 없다.**

**예시**  
- 배열: `[2, 4, 5, 4, 6]`
- M = 8, K = 3

가장 큰 수 6을 K=3번 더하고, 그 다음 큰 수인 5를 한 번 더하는 식으로  
`6 + 6 + 6 + 5 + 6 + 6 + 6 + 5 = 46`

※ 같은 수라도 인덱스가 다르면 별도로 간주한다.  
예: `[3, 4, 3, 4, 3]`, M=7, K=2 → 4와 4를 번갈아 사용해도 무방.

**입력 조건**

| 변수 | 조건 |
|------|------|
| N | 2 ≤ N ≤ 1,000 |
| M | 1 ≤ M ≤ 10,000 |
| K | 1 ≤ K ≤ 10,000 (항상 K ≤ M) |

**접근 방법**
- 가장 큰 수와 두 번째로 큰 수를 찾는다.
- 가장 큰 수를 K번 더하고, 그 다음 두 번째 수를 1번 더하는 사이클 반복
- `(K + 1)` 길이의 묶음이 몇 번 반복되는지를 이용해 총합 계산

다음 섹션에서 이 문제의 Swift 구현과 함께 자세히 설명해보자.

---

### 🧠 Swift 구현 예시 1: while + for 반복문 기반

```swift
let input = "5 8 3"
let numbers = "2 4 5 4 6"

let params = input.split(separator: " ").map { Int($0)! }
let (n, m, k) = (params[0], params[1], params[2])

var data = numbers.split(separator: " ").map { Int($0)! }
data.sort()  // 오름차순 정렬

let first = data[n - 1]   // 가장 큰 수
let second = data[n - 2]  // 두 번째로 큰 수

var result = 0
var remaining = m

while remaining > 0 {
    for _ in 0..<k where remaining > 0 {
        result += first
        remaining -= 1
    }

    if remaining > 0 {
        result += second
        remaining -= 1
    }
}

print(result) // 출력: 46
```

### ✨ Swift 구현 예시 2: 반복 패턴을 수학적으로 처리 (for + 나머지 패턴)

```swift
let input = "5 8 3"
let numbers = "2 4 5 4 6"

let params = input.split(separator: " ").map { Int($0)! }
let (n, m, k) = (params[0], params[1], params[2])

var data = numbers.split(separator: " ").map { Int($0)! }
data.sort(by: >)  // 내림차순 정렬

let first = data[0]
let second = data[1]

var result = 0

for i in 0..<m {
    if i % (k + 1) != k {
        result += first  // K번까지는 가장 큰 수
    } else {
        result += second // 그 다음은 두 번째 수
    }
}

print(result) // 출력: 46
```

이처럼 문제의 핵심 아이디어(가장 큰 수 K번 + 두 번째 수 1번)를  
`while`과 `for` 조합 또는 나머지 연산을 이용해 구현할 수 있다.



---

### ✨ Swift 구현 예시 3: 수학적 계산식 기반 (가장 효율적인 방식)

반복을 돌리지 않고, K번 가장 큰 수 + 1번 두 번째 큰 수의 **패턴을 수학적으로 계산**할 수 있다.

```swift
let input = "5 8 3"
let numbers = "2 4 5 4 6"

let params = input.split(separator: " ").map { Int($0)! }
let (n, m, k) = (params[0], params[1], params[2])

var data = numbers.split(separator: " ").map { Int($0)! }
data.sort(by: >)  // 내림차순 정렬

let first = data[0]
let second = data[1]

let groupCount = m / (k + 1)       // (K번 first + 1번 second) 묶음 반복 횟수
let remainder = m % (k + 1)        // 묶음으로 처리하고 남은 나머지 횟수

let result = groupCount * (first * k + second) + remainder * first
print(result) // 출력: 46
```

이 방식은 시간복잡도 측면에서 가장 효율적이며,  
그리디 패턴을 수식으로 정확히 구현한 형태이다.




### 🎴 예제 - 숫자 카드 게임

숫자 카드 게임은 여러 개의 숫자 카드 중에서 **가장 높은 숫자가 쓰인 카드 한 장을 뽑는 문제**이다.  
단, 게임의 룰을 지키며 선택해야 한다.

**문제 설명**
1. 숫자가 쓰인 카드들이 N x M 형태로 놓여 있다.
2. 먼저 뽑고자 하는 **카드가 포함된 행**을 선택한다.
3. 그다음 선택된 행에 포함된 카드 중 **가장 숫자가 낮은 카드**를 뽑아야 한다.
4. 따라서 처음에 행을 선택할 때, **각 행의 최소값 중 최댓값**이 되는 행을 골라야 한다.

**예시**
```
입력:
3 3
3 1 2
4 1 4
2 2 2

출력:
2
```

- 첫 번째 행 최소값: 1  
- 두 번째 행 최소값: 1  
- 세 번째 행 최소값: 2  
- 최종 선택 값: `max(1, 1, 2) = 2`

**접근 방법**
- 각 행에서 가장 작은 숫자를 선택
- 그 중에서 가장 큰 숫자를 결과로 반환
- 탐욕적으로 행 내 최소값만 비교하므로 그리디로 접근 가능

