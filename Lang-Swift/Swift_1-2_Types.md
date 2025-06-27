# 1-2. 기본 타입

일단 아래와 같이 타입을 나눌 수 있습니다.

- 문자형
    - String
- 숫자형
    - Int
    - Float
    - Double
- 논리형
    - Bool
    
또한 각각의 데이터를 묶어줄 **콜렉션 타입**이라는 것도 있는데,  
아래와 같은 것들이 이에 속합니다.

- 콜렉션타입
    - Array
    - Dictionary
    - Set
    - String
    

엥 String 도 콜렉션이에요? 
-> 문자(Character)가 순서대로 나열된 형태로, 컬렉션처럼 순회할 수 있습니다.


<br><br>

---

### 문자열 (String)

```swift
let greeting: String = "Hello, Swift"
var name = "Pepper"
print("Hi, \(name)")  // 문자열 보간
```

- 문자열 보간: `\(값)` 형식으로 값 삽입
- `.count`, `.uppercased()`, `.hasPrefix()` 등 다양한 메서드 사용 가능

> Swift에는 `Character`라는 타입도 존재합니다. 
> 이는 문자 하나만을 담는 타입으로, `String`은 여러 `Character`로 이루어진 컬렉션 타입입니다.  
> 한 글자 단위로 문자열을 다룰 때 유용하게 쓰이며, `for char in string`처럼 문자열을 순회하면 각 글자가 `Character`로 분리됩니다.

<br><br>


---

### 숫자형 (Int, Double, Float)

```swift
let year: Int = 2025
var score = 100
let pi: Double = 3.14159
let height: Float = 175.5
```

- 32비트/64비트 환경에서 자동 최적화됨
- `Double`이 기본 (64bit), `Float`은 가볍지만 정밀도 낮음
- `+`, `-`, `*`, `/`, `%` 사칙연산 가능

<br>

> 실무에서는 UI 프레임 계산 등에 `CGFloat`를 많이 사용하게 됩니다.  
> `CGFloat`는 내부적으로 플랫폼에 따라 `Float` 또는 `Double`로 구성되며, UIKit에서는 주로 이 타입이 쓰입니다.  
> 숫자 간 타입 변환 시에는 명시적 형변환이 필요할 수 있습니다.

<br><br>

---

### 불리언 (Bool)

```swift
let isLogin: Bool = true
var isDarkMode = false
```

- `true`, `false` 두 가지 값
- 조건문에서 핵심적으로 사용됨

<br><br>


---

### 콜렉션 타입 간단히 보기

```swift
let numbers: [Int] = [1, 2, 3]
var fruits = ["Apple", "Banana"]

var person: [String: String] = [
  "name": "Pepper",
  "job": "iOS Developer"
]

var animals: Set<String> = ["dog", "cat", "dog"]
```

- 배열, 딕셔너리, 집합의 간단한 사용법
- 값 타입으로 복사됨
- 콜렉션 타입 공통 메서드 사용가능
    - `.isEmpty`, `.count`
    - `.first`, `.last`
    - `.contains()`
    - `.sorted()`
    - `.map()`



<br><br>


---


## 💡 타입 추론 vs 명시

```swift
let name = "Pepper"     // String으로 추론됨
let age: Int = 30       // 타입 명시
```

 - Swift는 대부분 추론하지만, 명시하면 **코드 안정성과 의도 전달에 좋음**  
 - 컴파일러가 타입 추론에 들이는 비용을 줄일 수 있어, 빌드 속도나 일부 경우 연산 효율 측면에서도 유리할 수 있습니다.
 
