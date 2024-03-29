안전하게 배열에 접근하는 방법

일반적으로 배열에 index를 통해 접근하는 상황을 최소화해야하는 것이 옳지만 어쩔 수 없는 상황이 발생하곤 한다.

Swift에서는 좀 더 안전한 처리를 위해 함수 단에서 `guard`를 지원합니다.

하지만 `Array`의 경우 `index`를 통해 접근해서 가져오는 값이 `Optional`타입이 아니기 때문에 접근하는 `index`가 유효하지 않은 경우에는 꼼짝없이 `Fatal error: Index out of range`메세지가 발생합니다.

```swift
let arr = [1,2,3,4]
arr[4] // Fatal error: Index out of range
```

예를 들어 API통신을 통해 배열이 생성되는데 생성한 배열에 값이 추가 되지않은 경우, 호출을 하게 되면 앱이 종료 될 수가 있습니다. 추가적으로 예외처리를 해줄 수는 있겠지만 처음부터 안전한 방법을 만들면 추가적인 예외처리가 없어도 되겠죠.

해당 `Array`를 `index`를 통해 접근했을 때 `Optional`타입으로 반환 해주면

명시적인 장치를 통해서 해당 index에 값이 존재하지 않는 상황에 대한 예외 처리를 진행할 수 있기 때문에 비교적 안전하게 배열에 접근을 진행할 수 있습니다.

아래 `Extension`을 추가하면 해당 배열에 접근하려는 `index`가 유효한지 판단한 뒤 유효할 경우 실제 `Element`를 반환하고 아닌 경우 `nil` 값을 넘겨주게 됩니다.

```swift
extension Collection {
    subscript (safe index: Index) -> Element? {
        return indices.contains(index) ? self[index] : nil
    }
}
```

실제로 적용한 예는 아래와 같습니다.

```swift
let arr = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa"]

func getElementCount(_ index: Int) -> Int {
    guard let value = arr[safe: index] else { return 0 }
    return value.count
}

(-5..<10).forEach {
    print("\($0) : \(getElementCount($0))")
}

/*
[RESULT]
-2 : 0
-1 : 0
0 : 1
1 : 2
2 : 3
3 : 4
4 : 5
5 : 6
6 : 0
7 : 0
*/

```

## 📌 추가적으로 안전하게 배열에 접근하는 방법

### **1. isNotEmpty**

: 해당 배열에 값이 들어 있는지 파악하는 방식으로 위의 에러를 피할 수 있습니다.

```swift
...
if people.isNotEmpty {
  ...
  print(people[0].name)
  ...
  people.remove(people[0])
}
```

이렇게 한다면 안전하겠지만 대신 print문에서 0번째 인덱스를 접근하는 첨자 참조 크래시가 발생할 수도 있습니다.

이에 아래에는 조금 더 안전한 방법입니다.

### 2. safe [Depricated]

: safe로 해당 배열이 있는지 판단하고 접근 ( 위에서 소개한 내용 )

`중간에 중간에 있는 인덱스를 안전하게 조회/접근할 때`

```swift
if let person = people[safe: 0] {
  ...
  print(person.name)
  ...
  people.remove(person)
}
```

safe로 해당 배열의 인덱스 값이 있는지 안전하게 조회하고 접근하여 사용한다면 print에서 첨자 참조 크래시를 방지할 수 있습니다.

### 3. first

: 인덱스의 첫번째 요소 접근

```swift
if let person = people.first {
  ...
  print(person.name)
  ...
  people.remove(person)
}
```

이렇게 옵셔널 바인딩 부분에서 first로 접근한다면 첨자 참조 크래시도 나지 않고 안전하게 접근 및 사용할 수 있습니다.

이렇게 간단한 배열 조회에도 다양하고 \ 접근하는 방법에 대해 알아봤습니다.

