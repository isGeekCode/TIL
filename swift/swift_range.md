# Swift - Range 함수 사용하기


range 함수는 Swift에서 문자열 내에서 특정 부분을 찾을 때 사용된다.

## 전체 문자열에서 특정 부분의 범위 찾기
```swift
let str = "Hello, World!"
if let range = str.range(of: "World") {
    print("찾은 범위: \(range)")
}
```
여기서 `range`는 `str`중에서 `World`에 해당하는 범위값을 가지고 있다.
실제로 `range`를 print하면 `Index(_rawBits: 458765)..<Index(_rawBits: 786445)` 이런 값을 보여주지만 실제로는 `7..<12`를 의미한다. 

사실상 범위를 찾는 것만 수행하지 않고 아래 내용들처럼 범위를 찾아 이후, 추가적인 작업을 수행한다.


## `Range<String.Index>` 타입
range 함수의 리턴값은 `Range<String.Index> `이다. 

이 타입은 문자열 내에서 특정 부분을 나타내는 범위를 나타낸다. 
이 범위는 원본 문자열에 대한 참조로서 시작 인덱스와 끝 인덱스를 가지고 있다.

이때 String.Index는 문자열 내에서 문자의 위치값을 가지고 있는 변수이고, 한 문자사이 혹은 문자 앞뒤에 대한 위치를 가리킬수 있어서 인덱스기반의 작업을 수행할 수 있다. 

이 Index는 첫글자를 0으로 시작한다. 

### startIndex, endIndex
배열에서 .first와 .last처럼 첫번째와 마지막 위치를 가리키는 프로퍼티이다. 

### upperBound, lowerBound
range의 프로퍼티로 upperBound를 사용하면 해당범위보다 다음 글자 하나를 말한다.
upperbound...를 사용하면 해당범위 다음 전체를 의미한다. 

반대로 lowerBound는 해당 범위보다 이전을 말하고 ...역시 동일하게 사용한다. 
주로 특정 `String[특정range.upperBound...]`의 형태로 사용한다. 
String[] 안에 담는 것은 Subscript 라는 부분 문자열을 추출하는 기능이다.
### index(before:), index(after:)
주어진 인덱스의 이전, 이후 인덱스를 반환한다.


### distance(from:to:)
주어진 두 index 사이의 거리를 반환한다. 


### `index(_ i: String.Index, offsetBy distance: Int)` 메서드
해당 값의 리턴값은 `String.Index`값이다. 즉, 특정 index를 만드는 메서드이다. 
와일드카드 패턴에 들어간 값을 기준으로 `offsetBy`의 값만큼 이동한 index를 생성한다. 
  
예시)
- `str.index(str.startIndex, offsetBy: 5)`
- `index(str.endIndex, offsetBy: -5)`


### `Range<String.Index>`타입 변수
시작index와 끝 index 에 범위연산자를 사용하여 범위의 값을 가진 타입이다.

범위연산자 `...`,`..<`,`..` 들을 모두 사용가능하지만 주로 `...`, `..<`을 사용한다. 


```
let str = "Hello, World!"
let searchRange = str.startIndex..<str.index(str.startIndex, offsetBy: 5)
print(searchRange) // 0..<5
```
- str.startIndex는 첫번째 문자를 의미한다. 
- `str.startIndex..<str.index()`로 범위를 지정했는데, 여기 명시된 `str.index(str.startIndex, offsetBy: 5)`는 시작 Index로부터 5만큼 이동한 위치를 말한다. 


## 특정 범위 내에서 다시 특정 부분의 범위 찾기
`str.range(of: String)`함수는 사실 파라미터를 여러개 가지고 있다. 범위안에서 또 다시 특정범위를 찾으려면 
`str.range(of: String, range: Range<String.Index>)`의 형태로 사용한다. 


직접 `Range<String.Index>`타입의 범위를 지정할 수도 있다.
```swift
let str = "Hello, World!"
let searchRange = str.startIndex..<str.index(str.startIndex, offsetBy: 5)
if let range = str.range(of: "Hello", range: searchRange) {
    print("찾은 범위: \(range)") // 0..<5 에 해당하는 값
}
```
위 코드에서 searchRanges는 범위를 지정하는 `Range<String.Index>`타입 변수이다. 
searchRange라는 `Range<String.Index>`타입 변수를 range파라미터에 담아 사용한다. 


## 찾은 범위에서 수행하는 작업들

!! 기억해야할 것은 range의 

### 검색 결과를 사용하여 문자열을 추출하거나 조작하는 경우
```swift
let str = "Hello, World!"
if let range = str.range(of: "World") {
    let substring = str[range] // "World"
    // 해당 부분을 사용하여 다양한 작업을 수행할 수 있습니다.
    // 예: 추출한 문자열을 가공, 수정, 출력 등
    print("추출한 문자열: \(substring)")  // "World"
}

```


### 특정 부분을 대체하는 경우

```swift
var str = "Hello, World!"
if let range = str.range(of: "World") {
    str.replaceSubrange(range, with: "Swift")
    // "World"를 "Swift"로 대체
    print("변경된 문자열: \(str)") //Hello, Swift
}

```
### 문자열에서 특정 부분을 삭제하는 경우

```swift
var str = "Hello, World!"
if let range = str.range(of: "World") {
    str.removeSubrange(range)
    // "World"를 삭제
    print("변경된 문자열: \(str)") // Hello, 
}

```


## 그밖의 options를 이용한 range함수

- .caseInsensitive: 대소문자를 구분하지 않고 검색한다.
- .diacriticInsensitive: 발음 기호를 무시하고 검색한다.
- .anchored: 검색된 결과가 문자열의 시작 부분에 위치해야 한다.
- .numeric: 숫자를 유니코드 순서로 비교하여 검색한다.
- .regularExpression: 정규식을 사용하여 검색한다.

```swift


let str = "Hello, World!"
let range1 = 0..<5
let range2 = 0...5
let range3 = 0..5


// range1: 0..<5
if let range = str.range(of: "o", options: .caseInsensitive, range: range1) {
    print("range1에서 찾은 범위: \(range)")
}

```

## History
- 230620 : 초안작성
