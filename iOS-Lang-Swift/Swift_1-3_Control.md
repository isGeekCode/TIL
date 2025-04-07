# 1-3. 조건문과 반복문

조건에 따라 코드를 분기하거나, 특정 코드를 반복 실행할 수 있는 흐름 제어 구문을 다룹니다.


<br>

---


## 조건문

### if / else if / else
- 가장 기본적인 조건 분기 방식입니다.
- 조건이 true인 블록만 실행됩니다.

```swift
let score = 85

if score == 100 {
    print("Perfect!")
} else if score >= 80 {
    print("Great!")
} else {
    print("Keep trying!")
}
```


<br><br>

---



### switch
- 하나의 값을 기준으로 여러 조건을 나누고 싶을 때 유용합니다.
- enum이나 패턴 매칭과도 자주 사용됩니다.

```swift
let fruit = "banana"

switch fruit {
case "apple":
    print("🍎 Apple")
case "banana":
    print("🍌 Banana")
case "orange":
    print("🍊 Orange")
default:
    print("Unknown fruit")
}
```


<br><br>

---


## 반복문 기초

### for-in
- 정해진 횟수나 컬렉션을 순회할 때 사용합니다.
- 숫자 범위 (`1...5`)를 주면 해당 횟수만큼 반복됩니다.
- 향후 index를 다루는 방법(`enumerated()`)도 존재하지만 이는 이후에 다룹니다.

```swift
// 범위 연산자를 이용해서 수 자체를 순회할 수 있다.
for i in 1...5 {
    print("Iteration: \(i)")
}

// 지정한 컬렉션을 순회할 수 있다.
let names = ["Alice", "Bob", "Charlie"]
for name in names {
    print("Hello, \(name)")
}
```

<br><br>

---


### while
- 조건이 true인 동안 계속 실행됩니다.
- 조건을 먼저 평가하고, 만족하면 블록을 반복합니다.

```swift
var count = 0
while count < 3 {
    print("Count is \(count)")
    count += 1
}
```


<br><br>

---


## 반복문 조합 패턴

### repeat-while
- 무조건 한 번 실행한 후 조건을 검사합니다.
- 입력 유도 등 최소 1회 실행이 필요한 상황에 유용합니다.

```swift
var index = 0
repeat {
    print("Index is \(index)")
    index += 1
} while index < 3
```


<br><br>

---



### for-in + where
- 정해진 횟수 안에서 특정 조건을 만족하는 항목만 실행할 수 있습니다.

// 짝수만 출력
```swift
for number in 1...10 where number % 2 == 0 {
    print(number)  // 2, 4, 6, 8, 10
}
```
