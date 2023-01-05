# 📌 component()

`Apple Document`

[https://developer.apple.com/documentation/swift/1641199-readline](https://developer.apple.com/documentation/swift/1641199-readline)



### parameter : separatedBy

**`separator` : 구분기호 입력**

- `구분자를 기준으로 무조건 단어로 처리한다.`
    - **구분자를 “ ”로 할경우 스페이스를 기준으로 양 옆을 단어로 인식**
    - 띄어쓰기 하나만 있어도 배열의 갯수가 2개로 인식
    - 구분자를 삭제 ( split은 구분자 포함 )

```swift
var s = "this is powerful pineapple" 
print(s.components(separatedBy: "p")) 
// ["this is ", "owerful ", "inea", "", "le"]

var t = "  this is powerful pineapple" 
print(t.components(separatedBy: " ")) 
// ["", "", "this", "is", "powerful", "pineapple"]

var r = " "
print(r.components(separatedBy: " ").count)
//2

var u = "  this  is powerful pineapple"
print(u.split(separator: " "))
// ["this", "is", "powerful", "pineapple"]
```

### Return Value : [ String ]

주어진 구분 기호로 나눈 부분 문자열들을 포함한 배열을 반환

An `NSArray`object containing substrings from the receiver that have been divided by `separator`

# 📌 split()

### Split()

### **Return Value : [ Sub String ]**

An array of subsequences, split from this collection’s elements.

주어진 구분 기호로 나눈 문자열들을 포함한 배열을 반환

### **Discussion**

The resulting array consists of `maxSplits + 1` subsequences at most.

For an example, see `[split(separator:maxSplits:omittingEmptySubsequences:)](https://developer.apple.com/documentation/swift/set/1689075-split)`.



### ⭐️ Split함수는 다양한 parameter를 지원한다.

- separator → 구분기호
- maxSplits → separator 단위로 얼마나 나눌것인지 지정
- omittingEmptySubsequence → 결과값에서 빈 시퀀스의 포함유무를 Bool로 결정
    - False일경우 빈 칸을 빈요소로 추가
- Split이 Components 보다 처리 시간이 짧음

### ⭐️ import를 하지 않아도 된다.

splite함수는 swift 표준 라이브러리 (swift Standard Libary)에 들어 있기 때문에 따로 import Foundation을 할 필요가 없다.

```swift
let Message = "Hello  I'm Gikko, Have a nice day!"
// Hello 다음에 띄어쓰기 두개

var result1 = Message.split(separator: " ")
print(result1) 
/// ["Hello", "I'm", "Gikko,", "Have", "a", "nice", "day!"]

var result2 = Message.split{ $0 == " " }
print(result2) 
///  ["Hello", "I'm", "Gikko,", "Have", "a", "nice", "day!"]

var result3 = Message.split(separator: " ")
print(result3) 
/// ["Hello", "I'm", "Gikko,", "Have", "a", "nice", "day!"]

var result4 = Message.split(separator: " ").map(String.init)
print(result4) 
/// ["Hello", "I'm", "Gikko,", "Have", "a", "nice", "day!"]

import Foundation
var result5 = message.components(separatedBy: " ")
print(result5)  
/// ["Hello", "", "I\'m", "Gikko,", "Have", "a", "nice", "day!"]

```


### ⭐️  readLine함수를 이용하여 입력받을때

```swift
// 1.
var read = readLine()!
var arr = read.characters.split(separator: " ").map(String.init)
print(arr)

//2.
var read = readLine()
var arr = read.split(separator:" ")
print(arr)

```

```swift
import Foundation

var read = readLine()
var arr = read.components(separatedBy: [" ","/",",","-","."])
```

### ⭐️  map()함수와 같이 사용하는 이유

`링크 : [map함수의 기본형태 및 사용법](https://www.notion.so/74763eaa560d44b5842e2e867f1a9c7c)`

map()함수는  입력값을 변형해서 반환을 할 수 있는 함수이다.

특히 Array를 가져올때, 연산 등을 하기 위해서는 숫자형이 필요한데 이때 Int나 Double형과 같이 타입을 바꿔줄 수 있다.

```swift
let cast = ["Vivien", "Marlon", "Kim", "Karl"]
let lowercaseNames = cast.map { $0.lowercased() }
// 'lowercaseNames' == ["vivien", "marlon", "kim", "karl"]
let letterCounts = cast.map { $0.count }
// 'letterCounts' == [6, 6, 3, 4]

// split - ReturnType: [SubString] 
var nums = readLine()!.split(separator: " ").map {Int($0)!} 
// components - ReturnType: [String] 
var nums = readLine()!.components(separatedBy: " "). map {Int($0)!}

```

`map(_:)`함수는 각 요소에 접근하여 주어진 클로져의 동작을 적용시켜주게 된다.

따라서 `1 2 4 5 3 6`라는 입력값이 있을때 , 숫자형 배열로 저장하려면 다음처럼 하면 된다.

**`let** inputArray = readLine()!.split(separator: " ").map{**Int**($0)!}`
