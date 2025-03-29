# 기본적인 자료구조 - 배열

배열(Array)  
배열은 같은 데이터 타입의 값들을 순차적으로 저장하는 선형 자료구조다. 배열의 각 값은 인덱스를 통해 접근하며, 인덱스는 0부터 시작한다. 배열은 연속된 메모리 공간에 저장되므로, 빠른 접근 속도를 제공한다.

<br>

### 배열의 주요 특징
- 인덱스 기반 접근: 배열은 인덱스를 사용해 각 요소에 **O(1)**의 시간 복잡도로 빠르게 접근한다.
    - 예: array[0]은 배열의 첫 번째 요소에 접근한다.
- 고정된 크기: 배열은 선언 시 크기가 고정되며, 배열의 크기를 변경하려면 새로운 배열을 생성해야 한다. Swift에서는 동적 크기의 배열을 지원하지만, 일반적인 배열은 고정 크기다.

<br>

### 삽입/삭제의 시간 복잡도
삽입/삭제: 배열의 중간에 요소를 삽입하거나 삭제할 경우, **O(n)**의 시간이 걸린다. 이는 삽입/삭제 후 나머지 요소를 이동해야 하기 때문이다.  
끝부분에 요소를 추가하는 경우는 **O(1)**의 시간이 걸린다.  
배열의 용도: 배열은 정렬, 탐색, 슬라이딩 윈도우 문제 등 다양한 알고리즘 문제에서 자주 사용된다.

<br>

### 배열 사용 예시 (Swift)
```swift
var numbers = [1, 2, 3, 4, 5]

// 1. 배열의 첫 번째 요소에 접근
print(numbers[0])  // 출력: 1

// 2. 배열의 끝에 값 추가 (append)
numbers.append(6)
print(numbers)  // 출력: [1, 2, 3, 4, 5, 6]

// 3. 배열의 중간에서 값 제거 (remove at index)
numbers.remove(at: 2)
print(numbers)  // 출력: [1, 2, 4, 5, 6]

// 4. 배열의 길이 (count)
print(numbers.count)  // 출력: 5

// 5. 배열의 모든 요소 순회 (for-in loop)
for number in numbers {
    print(number)  // 출력: 1, 2, 4, 5, 6
```

### 배열의 시간 복잡도
- **접근**: O(1) (인덱스를 통해 바로 접근 가능)
- **삽입/삭제**:
    - 배열 끝에 추가/제거: O(1)
    - 배열 중간에 삽입/삭제: O(n) (나머지 요소를 이동시켜야 함)

<br>

## 배열의 인덱스 교환

#### 1. 임시 변수를 사용한 값 교환 (전형적인 방식 - Swift/Python)
이 방식은 거의 모든 언어에서 사용하는 전형적인 값 교환 방식이야. 교환할 두 값을 임시 변수에 저장한 후, 서로 맞바꾸는 방식이야.

``` Swift
var numbers = [1, 2, 3, 4, 5]
let n = 1  // 두 번째 요소
let m = 3  // 네 번째 요소

// 임시 변수를 사용하여 값 교환
let temp = numbers[n]
numbers[n] = numbers[m]
numbers[m] = temp

print(numbers)  // 출력: [1, 4, 3, 2, 5]
``` 


``` python
arr = [1, 2, 3, 4, 5]
n, m = 1, 3  # 인덱스 1과 3

# 임시 변수를 사용하여 값 교환
temp = arr[n]
arr[n] = arr[m]
arr[m] = temp

print(arr)  # 출력: [1, 4, 3, 2, 5]
``` 

### 2. `swapAt()` 메서드를 사용한 값 교환 (Swift 전용)
Swift에서는 `swapAt()`이라는 메서드를 제공해서 두 인덱스의 값을 간단하게 교환할 수 있어.

``` swift
var numbers = [1, 2, 3, 4, 5]
let n = 1  // 두 번째 요소
let m = 3  // 네 번째 요소

// swapAt()을 사용하여 값 교환
numbers.swapAt(n, m)

print(numbers)  // 출력: [1, 4, 3, 2, 5]
```

### 3. 다중 할당을 사용한 값 교환 (Python 전용)
Python에서는 다중 할당을 사용해 간단히 값을 교환할 수 있다.

```python
arr = [1, 2, 3, 4, 5]
n, m = 1, 3  # 인덱스 1과 3



# 다중 할당을 사용한 값 교환
arr[n], arr[m] = arr[m], arr[n]

print(arr)  # 출력: [1, 4, 3, 2, 5]
``` 


### 비교 표

| 방식                           | 설명                                                                 | 장점                                                  | 단점                                                     |
| ------------------------------ | -------------------------------------------------------------------- | ----------------------------------------------------- | -------------------------------------------------------- |
| **임시 변수를 사용한 교환**     | 값을 교환할 때 임시 변수를 사용해서 두 값을 서로 맞바꾸는 전형적인 방식 | **언어에 상관없이 사용 가능**                         | 코드가 상대적으로 길어지고, 가독성이 떨어질 수 있음       |
| **`swapAt()` 메서드를 사용한 교환** | Swift에서 제공하는 내장 메서드로, 두 인덱스의 값을 간단히 교환함      | **코드가 간결**하고, **Swift 표준 라이브러리**의 일부분 | 다른 언어에서는 사용할 수 없음 (Swift 전용 기능)          |
| **다중 할당을 사용한 교환**      | Python에서 제공하는 간단한 값 교환 방식                             | **코드가 매우 간결**                                   | 다른 언어에서는 사용할 수 없음 (Python 전용 기능)          |


## 배열을 사용하는 상황

### 상황 1: 배열에서 최대값 찾기
문제 상황:
주어진 정수 배열에서 가장 큰 값을 찾아보자. 배열의 요소는 양수 또는 음수가 될 수 있어. 배열의 크기는 자유롭게 설정해도 돼.

예시:
`let nums = [3, 7, -2, 8, 1, 9, -5]`
위 배열에서 가장 큰 값을 찾아야 해. 배열의 인덱스를 사용하여 순차적으로 값을 비교하는 방식을 고민해보면 돼.


답변:
```swift
let nums = [3, 7, -2, 8, 1, 9, -5]

var maximum = nums[0]  // 배열의 첫 번째 요소로 초기화
for num in nums {
    print("num:: \(num)")
    if maximum < num {
        maximum = num
    }
}
print(maximum)  // 출력: 9



nums.max() // 동일한 시간복잡도
```


### 상황 2: 배열의 합 구하기
문제 상황:
주어진 정수 배열에서 모든 요소의 합을 구해보자. 배열의 크기는 자유롭게 설정할 수 있어.

예시:
`let nums = [1, 2, 3, 4, 5]`
배열의 모든 요소를 더한 합을 구하는 문제야. 각 요소를 순차적으로 더해가는 방법을 고민해보면 돼.

답변:

```swift
let nums = [1, 2, 3, 4, 5]

// for문 이용
var sums = 0  // 배열의 첫 번째 요소로 초기화

for num in nums {
    print("num:: \(num)")
    sums += num

}
print(sums)


// reduce 이용
nums.reduce(0, +) // 동일하게 O(n) 시간복잡도

```

###  상황 3: 이중 배열을 이용한 좌표 탐색
문제 상황:
주어진 2차원 배열에서 특정 값을 찾아서 그 좌표를 출력해보자. 배열의 크기는 자유롭게 설정할 수 있어. 여기서는 값이 1인 좌표를 찾는 문제야.

예시:
```swift
let matrix = [
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0]
]
```
이 배열에서 1이 있는 좌표를 찾아내야 해. 이중 for문을 사용해서 배열의 요소를 순회하며 해결할 수 있어.


답변:

```swift
import Foundation

let matrix = [
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0]
]

var answers = [(Int,Int)]() {
    didSet {
        print(answers)
    }
}
var currentX: Int
var currentY: Int

for yIndex in 0 ... matrix.count-1 {
    currentY = yIndex
    let row = matrix[yIndex]
    
    for xIndex in 0 ... row.count-1 {
        currentX = xIndex
        if row[xIndex] == 1 {
            let answer = (xIndex, yIndex)
            answers.append(answer)
        }
    }
}



// enumerated 기본형
//for (index, value) in matrix.enumerated() {
//
//    print("index:\(index)")
//    print("value:\(value)")
//}

for (yIndex, row) in matrix.enumerated() {
    if let xIndex = row.firstIndex(of: 1) {
        answers.append((xIndex, yIndex))
    }
}

```

## 상황 4: 배열 회전
문제 상황:
주어진 배열을 오른쪽으로 k번 회전시켜 보자. 배열의 크기는 자유롭게 설정할 수 있어. 배열을 회전한 후 새로운 배열을 출력해봐.

예시:
```swift
let nums = [1, 2, 3, 4, 5]
let k = 2
```

이 배열을 오른쪽으로 2번 회전시키면, 결과는 [4, 5, 1, 2, 3]이 돼야 해.


답변:

```swift
```


답변:

```swift
```
