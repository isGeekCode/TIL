# 알고리즘 - 버블정렬 : Bubble Sort(작성중)



## 언제 사용??


## 동작 원리
- 1. 주어진 배열에서 가장 작은 값을 찾는다.
- 2. 가장 작은 값과 배열의 첫 번째 요소를 교환한다.
- 3. 두 번째 요소부터 다시 가장 작은 값을 찾아 두 번째 요소와 교환한다.
- 4. 이와 같은 과정을 배열의 마지막 요소까지 반복한다.


## 세부설명

여기서 필요한 과정은 2가지다.


### 어떻게 가장 작은 숫자를 찾을 건지



## 소스코드
```swift
var array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

for i in 0..<array.count {
    for j in 0..<array.count - 1 - i {
        if array[j] > array[j + 1] {
            let temp = array[j]
            array[j] = array[j + 1]
            array[j + 1] = temp
        }
    }
}

for element in array {
    print(element, terminator: " ")
}
```

### 로그
