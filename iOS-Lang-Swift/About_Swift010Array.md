# Swift - Array 모아보기

## 배열 생성하기

### 빈 배열 생성하기

**반드시 배열의 타입을 명시해야 한다.**

빈 배열은 세 가지 형태로 만들 수 있다.

```swift
//let emptyArray = [] // error: 타입 명시가 돼 있지 않음. (형식 추론 X)

let emptyArray: [Int] = []// 정식 문법 사용
let emptyArray2 = Array<Int>()// 단축 문법 사용
let emptyArray3 = [Int]()
```

<br><br>

### 값이 있는 배열 생성하기

```swift
var numbers: [Int] = [1, 2, 3, 4, 5] // Int 타입의 배열
var strings: [String] = ["Apple", "Banana", "Cherry"] // String 타입의 배열

// 특정 크기와 초기값을 가진 배열을 생성할 수도 있다.
var threeDoubles = Array(repeating: 0.0, count: 3) // [0.0, 0.0, 0.0]
```

<br><br>

### 같은 값이 연속적으로 들어가있는 배열 생성하기
`Array(repeating:count:)`생성자를 이용하면 연속된 어레이를 생성가능하다.

```swift
var numbers = Array(repeating: 3, count: 5)
// [3, 3, 3, 3, 3]
```

<br><br>

### 반복된 배열 만들기
`let arr = Array(repeating: a, count: b)`

- a : 제네릭타입으로 모든 데이터타입이 가능
- b : 반복할 횟수

a의 값을 b번 반복한 배열을 생성한다. 

<br><br>

예시1)

Bool타입을 연속 3개 만드는 경우. 
```swift
let arr = Array(repeating: false, count:3)
// [false, false, false]
```

<br><br>

### 반복된 이중 배열 만들기
주로 알고리즘으로 확인여부를 체크할 때 구현한다.  

```swift
var arr = Array(repeating: Array(repeating: false, count: m), count: n)
```

예시)
Bool타입 배열을 5개 연속해서 만들고, 해당 배열을 3개 만드는 경우. 

```swift
var arr = Array(repeating: Array(repeating: false, count: 5), count: 3)
// [
//   [false, false, false, false, false],
//   [false, false, false, false, false],
//   [false, false, false, false, false],
// ]
```

<br><br>

## 배열 처리하기

### 요소 추가하기
```swift
var fruits = ["Apple"]
fruits.append("Banana") // ["Apple", "Banana"]
fruits += ["Cherry", "Durian"] // ["Apple", "Banana", "Cherry", "Durian"]
```

### 요소 접근하기
```swift
let firstFruit = fruits[0] // "Apple"
```

### 요소 변경하기
```swift
fruits[1] = "Blueberry" // ["Apple", "Blueberry", "Cherry", "Durian"]
```


### 요소 제거하기
```swift
fruits.remove(at: 2) // "Cherry"를 제거, ["Apple", "Blueberry", "Durian"]
```


### 배열 순회하기
```swift
for fruit in fruits {
    print(fruit)
}
```

### 원하는 위치에 삽입하기
```swift
var fruits = ["Apple", "Blueberry", "Cherry", "Durian"]
fruits.insert("Melon", at:2) =  // ["Apple", "Blueberry", "Melon", "Cherry", "Durian"]
```


<br><br>

## 배열의 요소를 서로 교환하기
배열에서 특정 요소 두개를 서로 교환하는 경우가 있다. 
이때, 교환할 요소가 i번째와 j번째라고 했을 때, 아래와 같이 3가지 방법이 있다. 

### 1. 직접 교환
임시 배열을 생성하여 교환할 값들을 저장하여, 원본 arr에 접근하여 변경  
```swift
let tempArr = [originArr[i], originArr[j]]
arr[j] = tempArr[0]
arr[i] = tempArr[1]
```

<br><br>

### 2. 튜플을 이용한 교환
튜플을 사용하면 임시로 저장하는 공간이 없이 두 요소를 교환 가능하다.   
```swift
(resultArr[i], resultArr[j]) = (resultArr[j], resultArr[i])
```

<br><br>

### 3. swapAt(_:_:)메서드를 이용한 교환
swapAt메서드의 파라미터는 원본 배열의 index가 들어간다. 별도의 메모리가 저장되지 않기 때문에 효율적이다.  

```swift
arr.swapAt(i, j) 
```
swapAt 메서드의 시간복잡도는 𝑂(1) 이다.  

<br><br>

## 열거형 Enumerated()
[애플문서](https://developer.apple.com/documentation/swift/array/enumerated())
배열에 정의되어있는 메서드다. 

배열을 열거형으로 만들면서 배열의 index와 element를 파라미터로 리턴하는 메서드이다. 
문자열자체를 열거형으로 변환하여도 동일하게 적용이 가능하다. 
```swift
let strArr = ["S", "w", "i", "f", "t"]
for (n, c) in strArr.enumerated() {
    print("\(n): '\(c)'")
}
// Prints "0: 'S'"
// Prints "1: 'w'"
// Prints "2: 'i'"
// Prints "3: 'f'"
// Prints "4: 't'"


for (n, c) in "Swift".enumerated() {
    print("\(n): '\(c)'")
}

// Prints "0: 'S'"
// Prints "1: 'w'"
// Prints "2: 'i'"
// Prints "3: 'f'"
// Prints "4: 't'"

```


# 배열과 관련된 실용적 사용방법

## 문자열 -> 배열
### components(separatedBy:)
- components(separatedBy:) 메서드는 String 타입에서 사용되며, 문자열을 주어진 구분자에 따라 분할하여 [String]을 반환한다.  
- 이 메서드는 Foundation 프레임워크에 정의되어 있다.
```swift
import Foundation

let data = "Apple,Banana,Cherry"
let fruits = data.components(separatedBy: ",") // ["Apple", "Banana", "Cherry"]
```

<br><br>


### split(separator:)
`split(separator: some RegexComponent, maxSplits: Int = .max, omittingEmptySubsequences: Bool = true)`
- separator : 구분자
- maxSplits : 최대 분할 수 제한
- omittingEmptySubsequences : 빈 부분 문자열을 결과에서 제외할지 여부


<br><br>

### 결과에 빈칸이 들어오는 경우
- componets를 사용하는 경우
```swift
let data = " Apple Banana Cherry "
let parts = data.components(separatedBy: " ")
// 결과: ["", "Apple", "Banana", "Cherry", ""]

let nonEmptyParts = parts.filter { !$0.isEmpty }
// 결과: ["Apple", "Banana", "Cherry"]

```

<br><br>

- split을 사용하는 경우
```swift
let data = " Apple Banana Cherry "
let parts = data.split(separator: " ")
// 결과: ["Apple", "Banana", "Cherry"]

let fruitStrings = parts.map { String($0) }
// 결과: ["Apple", "Banana", "Cherry"]
```
split을 사용하는 경우, 반환타입이 String이 아닌 Substring타입이라 문자열로서 사용해야한다면 타입변환을 해주여야한다.  

<br><br>

## 배열의 특정 내용 포함 여부 확인하기
### contains(:) 메서드 
컬렉션에 특정 요소가 포함되어 있는지 여부를 확인할 때 사용된다.  
```swift
let fruits = ["Apple", "Banana", "Cherry"]
let containsApple = fruits.contains("Apple") // true
let containsOrange = fruits.contains("Orange") // false
```

<br><br>

### contains(where:) 메서드 
배열 내의 복잡한 객체나 특정 조건을 기반으로 요소의 존재 여부를 확인하는 경우 사용된다.  
클로저가 생성되면서 매개변수로 배열의 요소가 들어가게 된다.  
클로저 표현식으로 사용하면 $0이 배열의 요소가 된다.  
```swift
struct Fruit {
    var name: String
    var isTropical: Bool
}

let fruits = [Fruit(name: "Apple", isTropical: false),
              Fruit(name: "Banana", isTropical: true),
              Fruit(name: "Cherry", isTropical: false)]

// isTropical이 true인 값 포함여부
let containsTropicalFruit = fruits.contains { $0.isTropical } // true

// isTropical이 false인 값 포함여부
let containsNonTropicalFruit = fruits.contains { !$0.isTropical } // true


// name에 a가 포함된 값 걸러내기
let tropicalFruits = fruits.filter { $0.name.lowercased().contains("a") }
/*
[__lldb_expr_3.Fruit(name: "Apple", isTropical: false),
 __lldb_expr_3.Fruit(name: "Banana", isTropical: true)]
*/

// isTropical이 true인 값 걸러내기
let tropicalFruits = fruits.filter { $0.isTropical }
/*
[__lldb_expr_3.Fruit(name: "Banana", isTropical: true)]
*/


// isTropical이 false인 값 걸러내기
let nonTropicalFruits = fruits.filter { !$0.isTropical }
/*
[__lldb_expr_3.Fruit(name: "Apple", isTropical: false),
 __lldb_expr_3.Fruit(name: "Cherry", isTropical: false)]
*/
```

<br><br>

## 고차함수를 이용한 고급 배열 처리
### filter(:)
filter 메소드는 배열의 요소 중 조건에 맞는 요소만을 골라내어 새로운 배열을 생성한다. 
```swift
let numbers = [1, 2, 3, 4, 5, 6]
let evenNumbers = numbers.filter { $0 % 2 == 0 } // [2, 4, 6]
```


### map(:)
배열의 각 요소에 대해 주어진 변환을 적용하고 그 결과로 새 배열을 생성한다. 
```swift
let squaredNumbers = numbers.map { $0 * $0 } // [1, 4, 9, 16, 25, 36]
```

### reduce(:)
메소드는 배열의 모든 요소를 결합하여 하나의 값으로 만듭니다. 이 메소드는 초기값과 함께 적용할 결합 함수를 받는다. 

```swift
let sum = numbers.reduce(0, { $0 + $1 }) // 21
let multi =  numbers.reduce(1, { $0 * $1 })
//축약
let sum = numbers.reduce(0, +) // 21
let multi =  numbers.reduce(1, *)

```
reduce의 첫 번째 인자는 초기값이고, 두 번째 인자는 두 요소를 결합하는 클로저이다.  여기서 $0은 누적값(현재까지의 합), $1은 배열의 현재 요소를 나타낸다.  

### 혼합해서 사용해보기 
예제 : 고급 배열 처리 방법을 사용하여, 문자열 배열에서 글자 수가 5개 이상인 문자열을 대문자로 변환하고, 그 결과를 하나의 문자열로 결합


### flatMap
주로 중첩된 배열을 단일 수준의 배열로 평탄화(flatten)하는 데 사용된다.
```swift
let nestedNumbers = [[1, 2, 3], [4, 5], [6]]
let flattenedNumbers = nestedNumbers.flatMap { $0 }
// 결과: [1, 2, 3, 4, 5, 6]
```

- 옵셔널 값 포함 배열을 평탄화
flatMap을 사용하면 옵셔널을 제거하고 값을 평탄화할 수 있다. 
다만 Swift 4.1 이후에는 compactMap이 이러한 용도로 더 적합하다.
```swift
let nestedOptionalArrays: [[Int?]] = [[1, nil, 3], [nil, 5], [6]]
let flattenedAndUnwrapped = nestedOptionalArrays.flatMap { $0.compactMap { $0 } }
// 결과: [1, 3, 5, 6]
```

- 중첩된 요소에 대한 변환
중첩된 배열의 각 요소에 대해 변환을 수행한 후 평탄화하려는 경우에도 flatMap을 사용할 수 있다
```swift
let nestedStrings = [["a", "b", "c"], ["d", "e"], ["f"]]
let uppercased = nestedStrings.flatMap { $0.map { $0.uppercased() } }
// 결과: ["A", "B", "C", "D", "E", "F"]
```


### compactMap

```swift
let words = ["Apple", "Banana", "Cherry", "Date"]
let processed = words.filter { $0.count >= 5 }
                      .map { $0.uppercased() }
                      .reduce("") { $0 + $1 + " " }
// "APPLE BANANA CHERRY "
```
