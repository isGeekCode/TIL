# 1급 객체함수

Swift는 객체지향, 함수형, 프로토콜 프로그래밍을 사용한다. 



## 1급객체의 3가지 특징

1. 변수나 상수에 대입할 수 있다.
2. 함수의 반환값으로 자신을 사용할 수 있다.
3. 함수의 인자값으로 자신을 사용할 수 있다.

이걸 함수에 대입하면 아래와 같다


## 1급객체함수의 3가지 특징

1. 변수나 상수에 대입할 수 있다.
2. 함수의 반환값으로 함수를 사용할 수 있다.
3. 함수의 인자값으로 함수를 사용할 수 있다.



## 1. 변수나 상수에 대입할 수 있다.

```swift
func checkContainStore(storeName: String) -> Bool {
    let storeArray = ["CU", "GS25", "ministop", "sevenEleven"]
    return storeArray.contains(storeName) ? true : false
}
```

아래 처럼 변수에 함수의 이름을 넣어줄 수 있다.

```swift
// 1번: 아직 파라미터가 없는 함수를 변수에 넣어주는 경우
let isContainStore = checkContainStore
// 사용법
let isSevenEleven = isContainStore("sevenEleven")
// let isSevenEleven = isContainStore(storeName: "sevenEleven") //ERROR
print(isSevenEleven) // True

// 2번: 파라미터가 이미 들어간 함수를 변수에 넣어주는 경우
let isGS = checkContainStore(storeName: "GS")
print(isGS) //True
```



## 2. 함수의 반환 타입으로 함수를 사용할 수 있다

### 예시 1

아래와 같이 String을 반환하는 함수가 있다.

```swift
func currentStore() -> String {
  return "근처에 있음"
}

func noCurrentStore() -> String {
  return "근처에 없음"
}
```

아래함수의 return에 사용해보자

checkContainStore의 반환타입에  `() -> String` 라고 명시했다.

checkContainStore 함수의 반환값은 `() -> String` 라는 함수라는 의미이다. 

```swift
func checkContainStore(storeName: String) -> ( () -> String ) {
    let storeArray = ["CU", "GS25", "ministop", "sevenEleven"]
    return storeArray.contains(storeName) ? currentStore : noCurrentStore
```

### 예시 2

아래 계산기에 사용할 사칙연산함수들이다. 

```swift
func plus(a: Int, b: Int) -> Int {
    return a + b
}

func minus(a: Int, b: Int) -> Int {
    return a - b
}

func multiply(a: Int, b: Int) -> Int {
    return a * b
}

func divide(a: Int, b: Int) -> Int {
    return a / b
}
```

이 함수들을 calculate라는 함수의 return에 대입하고, 실행할때는 매개변수를 담아서 호출 연산자를 붙여주면 실행할 수 있다.

calculate(operand: String) 의 반환값이 위에있는 사칙연산함수들이다.  `(Int, Int) -> Int`

```swift
func calculate(operand: String) -> (Int, Int) -> Int {
    switch operand {
    case "+": return plus
    case "-": return minus
    case "*": return multiply
    case "/": return divide
    default: return plus
    }
}

//사용방법
let result = calculate(operand: "-")(4,3)  // 1
```



## 3. 함수의 파라미터로 함수를 사용할 수 있다

```swift
//파라미터에 대입될 함수
func Value(_ name: String) -> String {
    return "내 이름은 \(name)"
}
```

아래 getName함수의 파라미터 nameValue에 들어갈 타입을 대입할 함수의 타입으로 할당한다.

`(String) → String`  

그러면 nameValue의 파라미터에 해당하는 함수 `Value()`를 넣을 수 있다.

```swift

func getName(nameValue: (String) -> String, name: String) -> String {
    return nameValue(name)
}

var result = getName(nameValue: Value(_:), name: "철수")
print(result)
```
