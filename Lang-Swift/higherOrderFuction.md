# 고차함수 - Higher Order Function : Map, Filter, Reduce, Sort, FlatMap 

iOS의 Higher Order Function은 함수를 인자로 받거나 함수를 반환하는 함수를 말한다. 이것은 함수형 프로그래밍의 개념 중 하나로, 함수를 데이터처럼 다룰 수 있게한다.

iOS에서 가장 많이 사용되는 Higher Order Function은 아래와 같다.

map(): 컬렉션 내의 모든 요소를 변경하여 새로운 컬렉션을 생성한다.
filter(): 주어진 조건에 맞는 요소만으로 새로운 컬렉션을 생성한다.
reduce(): 컬렉션의 모든 요소를 하나의 값으로 줄여준다.
sort(): 컬렉션의 요소를 정렬한다.
flatMap(): 다차원 컬렉션을 단일 컬렉션으로 평탄화하여 반환한다.


# Map
map 함수는 배열의 각 요소를 변환하여 새로운 배열을 만들어 반환하는 함수다. 이를 통해, 기존 배열의 요소를 변환하거나, 새로운 데이터 타입의 배열을 만들 수 있다.

### 정수 배열에서 각 요소를 2배로 변환하기
```swift
let numbers = [1, 2, 3, 4, 5]
let doubledNumbers = numbers.map({ $0 * 2 })
print(doubledNumbers) // [2, 4, 6, 8, 10]
```

### 정수 배열에서 각 요소를 문자열로 변환하여 새로운 배열을 만들기
```swift
let numbers = [1, 2, 3, 4, 5]
let stringNumbers = numbers.map({ String($0) })
print(stringNumbers) // ["1", "2", "3", "4", "5"]
```

### 문자열 배열에서 각 요소를 대문자로 변환하여 새로운 배열 만들기

```swift
let words = ["apple", "banana", "orange"]
let capitalizedWords = words.map({ $0.uppercased() })
print(capitalizedWords) // ["APPLE", "BANANA", "ORANGE"]
```

# Filter
배열의 요소 중 조건에 맞는 요소만 추출하여 새로운 배열을 만드는 함수다.

### 배열요소중 짝수만 가져오기
```swift
let numbers = [1, 2, 3, 4, 5]
let evenNumbers = numbers.filter({ $0 % 2 == 0 })
print(evenNumbers) // [2, 4]
```

### 문자열 배열에서 길이가 5 이상인 요소만 추출하기
```swift
let words = ["apple", "banana", "orange", "grape", "pear"]
let longWords = words.filter({ $0.count >= 5 })
print(longWords) // ["apple", "banana", "orange"]
```

### 배열에서 특정값 제거하기
```swift
let numbers = [1, 2, 3, 4, 5, 6]
let filteredNumbers = numbers.filter({ $0 != 3 })
print(filteredNumbers) // [1, 2, 4, 5, 6]
```


### Optional 제거하기
```swift
let numbers: [Int?] = [1, nil, 3, nil, 5]
let filteredNumbers = numbers.filter({ $0 != nil })
print(filteredNumbers) // [1, 3, 5]
```


### 중복값 제거하기
아래 처럼 할 수 있지만 굉장히 비효율적이라 이럴땐 Set를 이용하여 더 간단히 해결가능하다.
```swift
let numbers = [1, 2, 3, 2, 4, 1, 5]
let uniqueNumbers = numbers.filter({ (index: Int) -> Bool in
    let isFirstIndex = numbers.firstIndex(of: index) == numbers.lastIndex(of: index)
    return isFirstIndex
})
print(uniqueNumbers) // [3, 4, 5]
```

Set이용하기
```swift
let numbers = [1, 2, 3, 2, 4, 1, 5]
let uniqueNumbers = Array(Set(numbers))
print(uniqueNumbers) // [5, 4, 3, 2, 1]
```


# Reduce
reduce 메서드는 배열의 모든 요소를 어떠한 방식으로든 하나의 값으로 줄여주는 함수다.

### 배열의 모든 요소 곱하기 

```swift
Copy code
let numbers = [1, 2, 3, 4, 5]
let product = numbers.reduce(1, { x, y in
    x * y
})
print(product) // 120
```

### 배열의 최대값/최소값 찾기
 

```swift
let numbers = [3, 9, 2, 8, 6, 5]
let maxNumber = numbers.reduce(numbers[0], { x, y in
    x > y ? x : y
})
print(maxNumber) // 9
```

### 배열의 문자열 합치기
 

```swift
let strings = ["Hello", ", ", "world", "!"]
let combinedString = strings.reduce("", { x, y in
    x + y
})
print(combinedString) // "Hello, world!"

```

# Sort
배열을 정렬하는 함수. 기본적으로 오름차순으로 정렬한다.

### 배열 정렬하기

```swift
var numbers = [5, 3, 4, 1, 2]
numbers.sort()
print(numbers) // [1, 2, 3, 4, 5]

```


### 문자열 배열을 길이를 기준으로 정렬하는 방법
```swift
var words = ["apple", "banana", "orange", "grape", "pear"]
words.sort(by: { $0.count < $1.count })
print(words) // ["pear", "apple", "grape", "banana", "orange"]

```
이렇게 sort를 사용하여, 배열을 비교할 수 있는 조건에 따라 정렬할 수 있다. sort 메서드의 인자로는 비교 함수를 사용할 수 있다. 

### 구조체 비교하기
```swift
struct Person {
    var name: String
    var age: Int
}

var people = [
    Person(name: "Tom", age: 30),
    Person(name: "Jerry", age: 20),
    Person(name: "Lucy", age: 25),
    Person(name: "Mike", age: 35)
]

people.sort(by: { $0.age < $1.age })
print(people) // [Person(name: "Jerry", age: 20), Person(name: "Lucy", age: 25), Person(name: "Tom", age: 30), Person(name: "Mike", age: 35)]


```

### 내림차순 정렬하기

```swift
var numbers = [5, 3, 4, 1, 2]
numbers.sort(by: >)
print(numbers) // [5, 4, 3, 2, 1]

```

### 특정 요소 우선 정렬하기

```swift
var words = ["apple", "banana", "orange", "grape", "pear"]
words.sort(by: {
    if $0 == "orange" { // $0은 첫 번째 비교 요소, $1은 두 번째 비교 요소
        return true // $0이 "orange"인 경우 true 반환
    } else if $1 == "orange" {
        return false // $1이 "orange"인 경우 false 반환
    } else {
        return $0 < $1 // 나머지 요소는 사전순으로 비교
    }
})
print(words) // ["orange", "apple", "banana", "grape", "pear"]

```
위 코드에서 sort 메서드는 문자열 배열 words를 인자로 받는다. 클로저에서는 "orange" 요소를 우선 정렬하고, 나머지 요소는 사전순으로 정렬한다. 클로저에서는 $0이 "orange"인 경우 true를 반환하여 $0을 더 앞쪽으로 배치한다. $1이 "orange"인 경우 false를 반환하여 $1을 더 뒤쪽으로 배치한다. 이렇게 sort 함수의 클로저에서 특정 요소를 우선 정렬할 수 있다.


# flatMap
 flatMap은 배열의 각 요소를 변환하여 새로운 배열을 만들고, 이를 하나의 배열로 평탄화하는 함수. 즉, 다차원 배열을 단일 배열로 만들어 준다.

### 2차원 배열을 flatMap을 사용하여 단일 배열로 변환하기
```swift
let numbers = [[1, 2], [3, 4], [5, 6]]
let flattenedNumbers = numbers.flatMap({ $0 })
print(flattenedNumbers) // [1, 2, 3, 4, 5, 6]

```
클로저에서는 각 배열을 반복하여 하나의 배열로 합쳐주는데, $0은 배열을 나타낸다. 이렇게 flatMap을 사용하여 2차원 배열을 단일 배열로 만들 수 있다.

### 문자열 배열에서 공백을 제거한 후 문자열의 길이를 반환하기
```swift
let words = ["apple", "banana", "orange"]
let wordLengths = words.flatMap({ $0.trimmingCharacters(in: .whitespaces) })
                    .map({ $0.count })
print(wordLengths) // [5, 6, 6]

```
이렇게 flatMap을 사용하여 배열의 요소를 변환하고, 새로운 배열을 만들 수 있다. flatMap은 이러한 방식으로, 배열의 요소를 변환하는 데에도 많이 사용된다.

<br><br>

# Map 예제
iOS UIKit DevTutorial에 있는 소스 참고 : CollectionView 생성부분

- [Creating a list view
](https://developer.apple.com/tutorials/app-dev-training/creating-a-list-view)




```swift
/*
mutating func appendSections(_ identifiers: [SectionIdentifierType])
*/
        
        var snapshot = Snapshot()
        snapshot.appendSections([0])
        
        /*
        var reminderTitles = [String]()
        for reminder in Reminder.sampleData {
            reminderTitles.append(reminder.title)
        }
        snapshot.appendItems(reminderTitles)
        */
        snapshot.appendItems(Reminder.sampleData.map { $0.title })

```

<br><br>


## CompactMap

고차함수로 배열을 전환하는 작업은 빈번하다.  

이 변환 중에는 nil이 발생할 수가 있는데,  

comapctMap은 map과 달리 nil을 자동으로 필터링한다.  

두가지 사례를 보자 
```swift
// MARK: CompactMap
let mixedValues = ["1", "two", "3", "four"]
let numbers = mixedValues.compactMap { Int($0) }
// 결과: [1, 3]


// MARK: Map
let mixedValues = ["1", "two", "3", "four"]
let numbers = mixedValues.map { Int($0) }
// 결과: [Optional(1), nil, Optional(3), nil]
```


## 고차함수로 데이터 배열만들기

보통 테스트를 위해 더미데이터를 만드는 경우가 많다.  
이 때, 중요한것은 반드시 인자가 $0로 들어가야한다는 것이다. 

```swift

```


## History
- 231123 : compactMap 추가
