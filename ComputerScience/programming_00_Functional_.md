함수형 프로그래밍이란
- [](https://www.youtube.com/watch?v=HZkqMiwT-5A&t=2s/)






## 서론 : 기존의 교육

- Immutable Data
- First Class Functions
- Tail Call Optimization

- Pure Function
- Higher-Order Function
- Recursing, Currying

- Parallelization
- Lazy Evaluation

<br><br>

### Immutable Data
불변의 데이터를 만들고 바꾸지말아라. 그러면 병행처리에 도움이 된다.
```SWIFT
let foo = "bar"
```

<br><br>

### 순수함수
같은 input에 대해서 동일한 output을 가져오는 함수를 말한다.

외부 환경에 영향을 받지 않기 떄문에 사이드 이펙트가 적다.


```SWIFT
func Log(_name: String) {
    print("Hello: \(name))
}
```

<br><br>

### 1급객체로 취급
함수 자체를 받을 수 있다.
```SWIFT
let adder: (Int, Int) -> Int = { $0 + $1 }

func  twice() -> (Int) -> Int {
    return { value in
        return value * 2
    }    
}


```

<br><br>

### 평가를 뒤로 늦출 수 있다.

```swift
func heavyJob() -> String {
    return "This is heavy Job"
}

// DEBUG지만 실제로는 실행되긴한다.
func Log(_ message: String) {
    #if DEBUG
        print(message)
    #endif
}

Log(heavyJob())

// 함수 자체를 넘기면 실행 자체가 안된다. 불핋요한 작업 수행을 안해도 된다.
func LazyLog(_ message: () -> String {
    #if DEBUG
        print(message())
    #endif
}

Log(heavyJob)

```


<br><br>

### 고차함수

```swift
func LazyLog(_ message: () -> String {
    #if DEBUG
        print(message())
    #endif
}

[1,2,3,4,5]
    .filter { $0 % 2 == 0 }
    .map { $0 * $0 }
    .reduce(0, +)
```
우리가 자주 사용하는데 이미.. 하고 있는건가?


<br><br>

### Recursing : Tail Call Optimization

FP에서는 필요해 따라( 효율을 위해) 재귀함수를 사용하기도 한다.


```swift
func sum(_ numbers: [Int]) -> Int {

    guard numbers.count > 0 else { return 0 }
    let head = numbers.first!
    let rest = Array(numbers.dropFirst())
    return head + sum(rest) 
}
```

<br><br>

###  Currying

```swift
// 파라미터 3개를 받는 함수 1개
func _calculate(_ method: (Int, Int) -> Int, v1: Int, v2: Int) -> Int {
    return method(v1, v2)
}

// 파라미터 하나를 받는 함수 3개로 쪼개는 기법
func calculate(_ method: @escaping (Int, Int) -> Int) -> ( Int ) -> ( Int ) -> Int {

    return { v1 in
        return { v2 in
            return method(v1, v2)
        }
    }
}

let addResult = calculate(+)(10)(3)
print(addResult) // 출력: 13

let adder = calculate(+)
let add10 = adder(10)

print(add10(3)) // 출력: 13
print(add10(5)) // 출력: 15


let multi = calculate(*)
print(multi(2)(3)) // 출력: 6

let double = multi(2)
print(double(15)) // 출력: 30
print(double(20)) // 출력: 40
```

<br><br><br>

보통 이정도만 설명하고 이런게 함수형 프로그래밍이라고 말하고 입문이 끝난다.

그러면 위에서 알아본 이 개념들을 나열하고 타이틀을 적어보자.

<br><br>

- Language Features →  
어떻게 할수 있는게 없다. 언어의 기능이다.
    - Immutable Data
    - First Class Functions
    - Tail Call Optimization

-  Programming Techniques → 
FP가 아니더라도 쓸 수 있는 프로그래밍 기법이다.
    - Pure Function
    - Higher-Order Function
    - Recursing, Currying

- Advantages of FP → 
이것들은 위에 있는 것들을 사용하다보면 얻을 수 있는 이득이다.
    - Parallelization : 병행처리
    - Lazy Evaluation : 늦은 평가
  
  
그렇다면 저걸 다하면 FP를 할 줄 아는 것인가?

<br><br>

---

<br><br>

## What is Functional Programming
 
> 함수를 이용해서 사이드 이펙트가 없도록 선언형 프로그래밍을 하는 것
- Function
- No Side-Effect
- Declarative Programming

위 세가지 요소를 한 단어로 표현하는 본질은 `No Side-Effect` 이다.

<br><br>

### 📌 Function : 함수를 사용한다는 것
기존에 사용하는 것은 object에 그가 소유하고있는 메소드를 호출하는 방식으로 사용했다.

그런데 FP는 함수를 먼저 쓰고 데이터를 집어 넣는 느낌이라고 보면된다. 
```swift
// Non-FP
account.deposit()
user.logic()

// FP
deposit(account)
user(User)
```

<br><br>

### 📌 No Side-Effect : Mudularzation / Stateless

1. OOP

Object가 orient한 프로그래밍이다.
Object들로 프로그래밍이 구성되고 Object들의 연관 관계로 이루어진다.

어떠한 기능 하나에 연관되어있는 Object들끼리 모으게 되면 하나의 Module이라고 부른다. 
Module의 최소단위는 Object 하나이다. 하나가 기능하나를 가질 수 있기 때문이다. 

<img width="600" alt="스크린샷 2023-08-07 오후 4 27 10" src="https://github.com/isGeekCode/TIL/assets/76529148/b56b5ea1-1397-48ce-a2f7-9a757a4441fe">


이 Object 하나의 구성은 멤버변수와 메서드로 나누어진다. 
그래서 이 메서드가 수행될 떄는 멤버변수를 사용해서 수행이 되고 여기 있는 값들을 바꾸게 된다. 
때문에 메서드의 수행결과는 멤버변수가 어떤 상태를 갖고있느냐에 따라서 결과가 달라진다. 
Object하나가 스스로 State를 가지고 있다는 뜻이 된다.
- Object
    - State : 멤버변수
    - Method() : 메서드

<br><br>

2. FP
함수는 Input과 Output이 있고,
그 Input에 대한 Output이 서로 연결되어서 
하나의 커다란 Output을 만들어낸다. 

여기서 말하는 함수는 순수함수를 말한다. 
그래서 여기는 스스로의 State가 없다. 상태에 따라 값이 달라지는 경우가 없다. 
그래서 모듈화의 최소단위는 Function하나가 된다. 

만약 UnitTest를 하게된다고 가정하게 되면,

- OOP의 경우
    - State가 어떤 경우의 수를 가지는지를 모두 나열해서, 그걸 모두 증명하는 UnitTest를 만들어야한다.
    - 검증된 Object들로만 구성된 프로그램은 잘 돌아갈 것이다. 

- FP의 경우
    - 어떤 경우 하나에 대해서만 정확하게 나오는지에 대해서만 확인하면된다. 
    - 검증된 Function으로 구성된 프로그램은 잘 돌아갈 것이다. 

<br>

> 결국 차이점은 State의 유무이다. 

State가 없도록 프로그래밍하는 것이 FP의 본질이고,

그걸 Side-Effect가 없다고 표현할 수 있다.


<br><br>

## 📌 Imperative VS Declarative 

- 명령형 : HOW
어떻게 원하는 결과를 얻어낼지 과정을 프로그래밍 
```swift
moveForward()
moveForward()
turnRight()
moveForward()
```

- 선언형 : WHAT
어떤 결과를 얻고 싶은지 선언하는 프로그래밍
```swift
gotIt()
```

<br><br><br>

## 예제: FizzBuzz

```swift
var i = 1
while i <= 100 {
    if i % 3 == 0 && i % 5 == 0 {
        print("fizzbuzz")
    } else if i % 3 == 0 {
        print("fizz")
    } else if i % 5 == 0 {
        print("buzz")
    } else {
        print("\(i)")
    }
    i += 1
}
```
위와 같은 코드가 있다. 이걸 FP로변형해보자. 아까 강조했던 FP의 3개 키워드를 다시 보자.
- 함수이용
- 사이드이펙없고
- 선언형으로 
  
  
  <br><br>
  
### 사이드이펙트 없애기
여기선 i = 1 이라는 State를 가지고 있다. 이거부터 없애보자. 
```swift
(1...100).forEach { i in
    if i % 3 == 0 && i % 5 == 0 {
        print("fizzbuzz")
    } else if i % 3 == 0 {
        print("fizz")
    } else if i % 5 == 0 {
        print("buzz")
    } else {
        print("\(i)")
    }
}
```
이렇게 수정하면 외부에 있던 변수가 사라져서 외부의 i가 다른 값이 들어올 수가 없다.   


 <br><br>
 
### 함수를 이용하기
그다음 함수형프로그래밍이니까 함수를 사용해보자.
fizz와 buzz를 확인하는 함수를 만들자.

fizz와 buzz라는 문자열을 리턴하는 함수이다.  
하지만 여전히 구현부는 명령형으로 만들어져있다.

 
```swift
let fizz: (Int) -> String = { i in i % 3 == 0 ? "fizz" : "" }
let buzz: (Int) -> String = { i in i % 5 == 0 ? "buzz" : "" }

(1...100).forEach { i in
    let fizzbuzz = fizz(i) + buzz(i)
    let output = fizzbuzz.isEmpty ? "\(i)" : fizzbuzz
    print(output)
}
```

함수 2개를 새로 생성
- 출력하는 함수 생성
- fizz buzz 비교했던 부분을 함수로 분리

과정은 모르지만 원하는 것은 이거다.
`(1...100).map(fizzBuzz).forEach(log)`


```swift
let fizz: (Int) -> String = { i in i % 3 == 0 ? "fizz" : "" }
let buzz: (Int) -> String = { i in i % 5 == 0 ? "buzz" : "" }

let fizzBuzz: (Int) -> String = { i in { s in s.isEmpty ? "\(i)" : s }(fizz(i) + buzz(i)) }

let log: (String) ->  () = { print($0) }

// 프로그램
(1...100).map(fizzBuzz).forEach(log)

/*
// fizzBuzz부분 개행처리
let fizzBuzz: (Int) -> String = { i in
    { s in
        s.isEmpty ? "\(i)" : s
    } (fizz(i) + buzz(i))
}
*/
```


좀더 코드를 정리해보자.
타입이 명확한 부분은 타입추론을 할 수가 있기 때문에 생략가능하다.
 ```swift
let fizz = { $0 % 3 == 0 ? "fizz" : "" }
let buzz = { $0 % 5 == 0 ? "buzz" : "" }

let fizzBuzz = 
    { i in { s in s.isEmpty ? "\(i)" : s }(fizz(i) + buzz(i)) }

let output = { print($0) }

// 프로그램
(1...100).map(fizzBuzz).forEach(output)

```

- One more Step

### Monade
기술이라기 보단 개념에 대한 용어다.
뭔가를 하나로 감쌌다는 개념이다. 
Swift의 대표적인 모나드는 Optional이다. 
옵셔널은 value가 있거나 null이거나 두가지의 상태를 가지고 있는데 Optional이라는 하나로 감쌌다.

```swift
func + (_ s1: String?, _ s2: String?) -> (String?) {
    if s1 == nil, s2 == nil { return nil }
    if s1 != nil, s2 == nil { return s1 }
    if s1 == nil, s2 != nil { return s2 }
    return s1! + s2!

let fizz = { $0 % 3 == 0 ? "fizz" : "" }
let buzz = { $0 % 5 == 0 ? "buzz" : "" }

let fizzBuzz = { i in fizz(i) + buzz(i) ?? "\(i)" }
let output = { print($0 ?? "") }

}

```

```swift
```


```swift
```


```swift
```


```swift
```

History
- 230807: 초안작성


