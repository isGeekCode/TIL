# Array - 빠르게 **빈 배열 만들기**

**반드시 배열의 타입을 명시해야 한다.**

빈 배열은 세 가지 형태로 만들 수 있다.

```swift
//let emptyArray = [] // error: 타입 명시가 돼 있지 않음. (형식 추론 X)

let emptyArray: [Int] = []// 정식 문법 사용
let emptyArray2 = Array<Int>()// 단축 문법 사용
let emptyArray3 = [Int]()
```


