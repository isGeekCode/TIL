# Swift - 키워드 inout
함수의 파라미터에 들어간 변수를 직접 참조하여 원본 변수를 변하게 하는 키워드

## 사용예
```swift
func square(number: inout Int) {
    number = number * number
}

var num = 5
square(number: &num)
print(num) /// "25"

```

Swift에서 함수를 사용할 때,

파라미터를 넣고 return값을 얻는 방식이 있다.

```swift
func doubleNumber(num: Int) -> Int {
    return num * 2
}
var myNumber = 5
myNumber = doubleNumber(num: myNumber)
print(myNumber) /// 10

```

위 함수 doubleNumber라는 함수에 5를 전달하면, 함수 내에서 이 값을 2배로 만들고 그 결과를 반환한다. 그런데, 만약 우리가 이 함수 내부에서 파라미터인 num의 값을 변경한다고 하면 어떻게 될까

```swift
func doubleNumber(num: Int) { /// Cannot assign to value: 'num' is a 'let' constant
    num = num * 2   // ERORR!!!!!
}

```

외부에 있는 변수에 선언하는건 가능하지만 파라미터로 받은 변수에 선언하는 것은 안된다는 에러가 발생한다. 

그렇다면, 함수 안에서 매개변수의 값을 변경하고, 그 변경된 값을 다시 원래의 변수에 반영할 수 있을까? 

그때 사용하는 것이 바로 `inout` 키워드이다.

### 사용법
이 inout 키워드를 함수에서 파라미터 앞에 붙여주면 함수 내부에서 파라미터에 다시 변수를 선언해도 에러가 발생하지않는다.
함수를 사용할 때는 함수의 파라미터에 넣은 변수앞에 `&`을 넣어준다. 
이렇게 하면 원래의 변수를 참조하겠다는 의미이다. 

```swift
func doubleNumber(num: inout Int) {
    num = num * 2
}
var myNumber = 5
doubleNumber(num: &myNumber)
print(myNumber) /// 10
```


## 또다른 예

### Count를 증가시켜주는 예시
```
func increment(_ number: inout Int) {
    number += 1
}

var myNumber = 5
increment(&myNumber)

print(myNumber)  // 출력 결과: 6
```



### 파라미터로 들어간 배열을 가지고 작업을 실행한 다음, 초기화 하는 예시

```swift
func appendAndReset(_ list: inout [Int], element: Int) {
    // 기존 배열에 새로운 요소를 추가합니다.
    list.append(element)
    print("After appending: ", list)
    
    // 배열의 모든 요소를 곱합니다.
    let product = list.reduce(1, *)
    print("Product of elements: ", product)
    
    // 그 후 배열을 초기화 합니다.
    list = []
    print("After resetting: ", list)
}

var numbers = [1, 2, 3]
print("Original: ", numbers)  // 출력: Original:  [1, 2, 3]

appendAndReset(&numbers, element: 4)
// 출력: After appending:  [1, 2, 3, 4]
// 출력: Product of elements:  24
// 출력: After resetting:  []

print("After function: ", numbers)  // 출력: After function:  []

```
