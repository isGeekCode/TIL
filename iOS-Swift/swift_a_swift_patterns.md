# Swift - 스위프트에서 사용하는 패턴들

## 값 바인딩(Value Binding) 패턴

let 또는 var 키워드와 함께 사용하여 값을 추출하고 변수에 부여(바인딩)하는 패턴이다.
```swift
let x = 10
var y = "Hello"
```

## 와일드카드(Wildcard) 패턴:

_ (언더스코어)를 사용하여 어떤 값에도 일치하는 패턴이다.
```swift
let _ = 20
```



## 옵셔널 바인딩(Optional Binding) 패턴:

if let 또는 guard let과 함께 사용하여 옵셔널 값을 안전하게 추출하고 바인딩하기위한 패턴이다.

```swift
if let name = optionalName { ... }
```

## 타입 패턴(Type Pattern):

값의 타입을 확인하여 매칭시키는 패턴이다.
is, as, case let과 함께 사용하여 값의 타입을 비교하거나 다운캐스팅할 수 있다.
```swift
// 예1
let value: Any = 42

if value is Int {
    print("value is an Integer")
} else if value is String {
    print("value is a String")
} else {
    print("value is of another type")
}

// 예2
let value: Any = "Hello"

if let stringValue = value as? String {
    print("value is a String: \(stringValue)")
} else {
    print("value is not a String")
}

// 예3
enum Result {
    case success(value: Int)
    case failure(error: Error)
}

let result: Result = .success(value: 42)

switch result {
case let .success(value):
    print("Result is a success with value: \(value)")
case let .failure(error):
    print("Result is a failure with error: \(error)")
}

```

## 튜플 패턴(Tuple Pattern):

여러 값의 조합에 대한 패턴이다.
튜플이란 여러개의 값들을 그룹화해서 하나의 값으로 표현할수 있는 데이터 타입이다.
튜플 패턴을 사용하면 여러 값을 동시에 추출하고 매칭할 수 있다.
```swift
// 예1
 let (x, y) = (3, 5)
 
// 예2
let person = ("John", 30)

// 튜플 값의 분해
let (name, age) = person
print("Name: \(name), Age: \(age)")

// 튜플 값의 매칭
switch person {
case ("John", 30):
    print("Person is John, 30 years old")
case (_, 20...30):
    print("Person is between 20 and 30 years old")
default:
    print("Person does not match any known pattern")
}
```

## 범위 패턴(Range Pattern):

값이 특정 범위에 속하는지 확인하는 패턴이다.
`..<` 또는 `...`연산자와 함께 사용하여 범위를 지정한다.

```swift
case 1...10:

case ..<5:
```

## 식별자 패턴(Identifier Pattern):

특정 값에 대한 식별자로 매칭하는 패턴이다.
이 패턴은 값을 추출하거나, 변수나 상수의 이름을 이용하여 비교할 때 사용한다. 
예: 
```swift
// 예1
case .success(let value):, case .failure(let error):

// 예2
let name = "John"

// 값의 추출과 바인딩
if case let extractedName = name {
    print("Extracted name: \(extractedName)")
}

// 값의 비교
if name == "John" {
    print("The name is John")
} else {
    print("The name is not John")
}

// 예3
let array: [Any] = [10, "Hello", 3.14, "Swift"]

for case let value as Int in array {
    print("Integer value: \(value)")
}

for case let value as String in array {
    print("String value: \(value)")
}

```

## 열거형 케이스 패턴(Enum Case Pattern):

특정 열거형 케이스와 매칭하는 패턴이다.
case 키워드와 함께 열거형 케이스를 지정하여 매칭한다.
사실상 식별자 패턴의 한 종류이다.

```swift
// 예1
enum Result {
    case success(value: Int)
    case failure(error: Error)
}

let result: Result = .success(value: 42)

switch result {
case .success(_):
    print("Result is a success")
case .failure(let error):
    print("Result is a failure with error: \(error)")
}


// 예2
enum Result {
    case success(value: Int)
    case failure(error: Error)
}

let result: Result = .success(value: 42)

switch result {
case .success(let value):
    print("Result is a success with value: \(value)")
case .failure(let error):
    print("Result is a failure with error: \(error)")
}

```

## 소변수 바인딩 패턴(Constant Binding Pattern)

값이 특정 패턴과 일치하는 경우, 해당 값을 상수에 바인딩하는 패턴이다.

let 키워드와 함께 사용하여 매칭된 값을 상수로 바인딩한다.

사실상 이 패턴도 일종의 식별자 패턴이다.
```swift
// 예1
let point = (x: 10, y: 20)

if case let (x, y) = point {
    print("x: \(x), y: \(y)")
}

// 예2
enum Result {
    case success(value: Int)
    case failure(error: Error)
}

let result: Result = .success(value: 42)

if case .success(let value) = result {
    print("Result is a success with value: \(value)")
}

```

## 조건 패턴(Condition Pattern)

특정 조건을 만족하는 경우에만 매칭을 수행하는 패턴이다. 
조건문에 사용하는 여러 구문뿐 아니라 옵셔널 캐스팅을 하는 과정에서도 많이 사용한다. 

### if let과 if case let
- if let
    - if let 구문은 옵셔널 값의 안전한 추출과 함께 조건을 추가하는 용도로 사용된다. 특정 값이 옵셔널이고 그 값이 존재하는 경우에만 코드 블록을 실행할 수 있다. 이때, 값이 옵셔널에서 추출되어 상수나 변수에 할당되는 것은 조건 패턴의 일종이다.
- if case let
    - if case let 구문은 열거형 등의 패턴 매칭에서 특정 케이스에 대한 매칭을 수행하고, 매칭된 연관 값을 바인딩하는 용도로 사용된다. 특정 케이스에 매칭되고, 해당 케이스의 연관 값을 바인딩하여 추가적인 조건 검사나 처리를 수행할 수 있다. 이 역시 조건 패턴의 일종으로 볼 수 있다.

```swift
// 예1 if let 구문
let value: Int? = 42

if let unwrappedValue = value, unwrappedValue > 0 {
    print("Value is a positive number: \(unwrappedValue)")
} else {
    print("Value is nil or not a positive number")
}


// 예2 if case let 구문
enum Result {
    case success(value: Int)
    case failure(error: Error)
}

let result: Result = .success(value: 42)

if case .success(let value) = result, value > 0 {
    print("Result is a success with a positive value: \(value)")
}
```

### switch let과 switch case let
- switch let
    - switch let은 옵셔널 바인딩을 사용하여 값이 있는 경우에만 매칭하고 해당 값을 바인딩하는 역할을 한다. 이를 통해 옵셔널 값의 안전한 추출과 동시에 매칭을 수행할 수 있다.
- switch case let
    - switch case let은 열거형 등의 패턴 매칭에서 특정 케이스에 대한 매칭을 수행하고, 해당 케이스의 연관 값을 바인딩하는 역할을 한다. 이를 통해 특정 케이스에 대한 값의 추출과 동시에 매칭을 수행할 수 있다.
```swift
// 예1 switch let 구문
let optionalValue: Int? = 42

switch optionalValue {
case let value?:
    print("Value is not nil: \(value)")
case nil:
    print("Value is nil")
}

// 예2 switch case let 구문
enum Result {
    case success(value: Int)
    case failure(error: Error)
}

let result: Result = .success(value: 42)

switch result {
case let .success(value):
    print("Result is a success with value: \(value)")
case .failure(let error):
    print("Result is a failure with error: \(error)")
}
```

### for case let
for-in 구문을 통해 시퀀스의 요소들을 순회하면서 패턴 매칭과 함께 조건을 추가하여 특정 요소들만을 처리할 수 있다.

가독성을 위해 for in 안에 if let을 사용하면 동일한 동작을 수행한다.
```swift
// 예1
let numbers = [1, 2, 3, 4, 5, 6]

for case let number in numbers where number % 2 == 0 {
    print("Even number: \(number)")
}

// 예2
let items: [Any] = [1, "Hello", 3.14, true]

for item in items {
    if let number = item as? Int {
        print("Found an integer: \(number)")
    } else if let string = item as? String {
        print("Found a string: \(string)")
    } else if let float = item as? Float {
        print("Found a float: \(float)")
    } else {
        print("Unknown item")
    }
}

// 예3 위 코드를 for case let으로 하면 아래와 같다.
let items: [Any] = [1, "Hello", 3.14, true]

for case let number as Int in items {
    print("Found an integer: \(number)")
}

for case let string as String in items {
    print("Found a string: \(string)")
}

for case let float as Float in items {
    print("Found a float: \(float)")
}

for case _ in items {
    print("Unknown item")
}


// 예4 네비게이션 컨트롤러에 속한 내가 원하는 VC찾기
if let navigationController = self.navigationController {
    for viewController in navigationController.viewControllers {
        if let mainViewController = viewController as? MainViewController {
            // MainViewController와 매치되는 경우에 대한 처리
            // ...
            break // 원하는 동작 수행 후 반복문 종료
        }
    }
}

// 예5 위 내용을 for case let으로 사용하면 아래와 같다.
if let navigationController = self.navigationController {
    for case let mainViewController as MainViewController in navigationController.viewControllers {
        // MainViewController와 매치되는 경우에 대한 처리
        // ...
        break // 원하는 동작 수행 후 반복문 종료
    }
}

```

## 타입캐스팅 패턴(Type Casting Pattern)
캐스팅 패턴(Type Casting Pattern)은 Swift에서 패턴 매칭을 수행할 때, 특정 값이 특정 타입 또는 그 타입의 하위 타입인지 확인하는 패턴이다. 

타입 캐스팅 패턴을 사용하여 값을 특정 타입으로 다운캐스팅하거나 타입 체크를 수행할 수 있다.

타입 캐스팅 패턴은 is와 as 연산자를 사용하여 구현한다.

- `is`연산자를 이용한 타입체크
    - `value is Type` 형식으로 사용한다. value가 Type이거나 Type의 서브클래스인 경우에 true를 반환한다.
- `as`연산자를 이용한 타입체크
    - `value as? Type` 혹은 `value as! Type` 형식으로 사용한다.
    - value를 Type으로 다운캐스팅한다.
    - `as?`는 다운캐스팅이 실패할 경우 nil을 반환하고, `as!`는 다운캐스팅이 실패할 경우 런타임 오류가 발생한다.

```swift
// 예1 is
let value: Any = 42

if value is Int {
    print("value is an Int")
} else {
    print("value is not an Int")
}

// 예2 as?
let value: Any = 42

if let intValue = value as? Int {
    print("intValue is an Int with value \(intValue)")
} else {
    print("value cannot be converted to Int")
}

// 예3 as!
let value: Any = 42

let intValue = value as! Int
print("intValue is an Int with value \(intValue)")

```

### as? Int와 as Int? 의 차이

- as? Int
    - Optional 타입으로 다운캐스팅을 시도한다. 다운캐스팅이 실패하면 nil을 반환한다.
- as Int?
    - Optional 값을 암시적으로 언래핑한다. 다운캐스팅이 실패하면 nil을 반환한다.

```swift
let value: Any = "42"

let intValue1 = value as? Int
let intValue2 = value as Int?

print(intValue1) // nil 
print(intValue2) // nil 
```


### as! Int와 as Int!의 차이
- as! Int
    - 강제 언래핑을 수행하는 다운캐스팅을 시도한다. 다운캐스팅이 실패할 경우 런타임 오류가 발생한다. 반드시 성공할 것을 확신하고 사용해야한다.
- as Int!
    - 암시적으로 언래핑된 옵셔널 타입이므로, 옵셔널 값을 사용할 때마다 암시적으로 강제 언래핑된다. 사용시에는 일반(non-optional) 타입으로 취급된다.
    - 다운캐스팅이 실패할 경우에도 컴파일 시에는 오류가 발생하지 않지만, 실행 시에 암시적으로 강제 언래핑되어 런타임 오류가 발생할 수 있다. 
```swift
let value: Any = "42"

let intValue1 = value as! Int 
let intValue2 = value as Int! 


print(intValue1) // 컴파일시 오류발생
print(intValue2) // nil
```
intValue2처럼 암시적으로 언래핑된 옵셔널 타입을 사용하는 경우, 다운캐스팅이 실패할 경우에도 런타임 오류가 발생하지 않는다.

## 옵셔널 패턴(Optional Pattern)
옵셔널 패턴(Optional Pattern)은 옵셔널 값의 존재 여부를 검사하고, 값이 있는 경우에만 패턴 매칭을 수행하는 패턴이다.
nil인지 아닌지를 확인하여 매칭합니다.

주로 if let이나 guard let을 함께 사용한다.

```swift
// 예1
let optionalValue: Int? = 42

if let value = optionalValue {
    // 옵셔널 값이 존재하는 경우
    print("Value exists: \(value)")
} else {
    // 옵셔널 값이 없는 경우
    print("Value is nil")
}

//예2
guard let value = optionalValue else {
    print("Value is nil")
    return
}

// 옵셔널 값이 존재하는 경우
print("Value exists: \(value)")
```

## 소유자 패턴(Ownership Pattern)

소유권(Ownership)에 기반하여 값을 소유하거나 참조하는 패턴이다.
값의 소유자(owner)를 확인하여 매칭합니다.
소유자 패턴은 객체 간의 의존성을 관리하고 표현하는 패턴으로 이해할 수 있다.
객체 간의 의존성은 한 객체가 다른 객체를 사용하거나 참조함으로써 발생한다.

```swift
class Person {
    let name: String
    
    init(name: String) {
        self.name = name
    }
    
    deinit {
        print("Person \(name) deallocated")
    }
}

weak var weakPerson: Person? = Person(name: "John")
        
if case let strongPerson? = weakPerson {
    print("Strong reference to \(strongPerson.name)")
} else {
    print("Weak reference is nil")
}

```
위 코드에서 `weak var weakPerson: Person? = Person(name: "John")`
중에서 `weak var` 부분은 변수` weakPerson`을 약한 참조로 선언하고 있다는 것을 의미한다. 이것은 `weak` 키워드를 통해 표시되며, 변수가 `Person` 객체를 약하게 참조하도록 지정한다. 

이렇게 약한 참조를 선언하면 해당 변수는 참조하는 객체를 강하게 소유하지 않고, 참조되는 객체가 메모리에서 해제되면 자동으로 nil 값을 갖게 된다. 이는 약한 참조의 주요 특징이며, 주로 순환 참조 등 메모리 관리와 관련된 상황에서 사용된다.

`if case let strongPerson? = weakPerson` 부분에서는 패턴 매칭을 통해 `weakPerson`을 약한 참조로부터 강한 참조(strongPerson)로 매칭한다.

만약 `weakPerson`이 참조하는 객체가 아직 해제되지 않은 상태라면(nil이 아니라면), 패턴 매칭이 성공하고 `strongPerson`에 강한 참조가 할당된다. 그리고 해당 객체의 이름을 출력한다. 반대로, `weakPerson`이 nil인 경우에는 패턴 매칭이 실패하고 "Weak reference is nil"이 출력된다.

정리하자면
- Person 클래스
    - Person 클래스는 사람을 나타내는 클래스다.
    - name 프로퍼티를 가지고 있으며, 초기화될 때 값이 할당된다.
    - deinit 메서드를 가지고 있으며, 인스턴스가 메모리에서 해제될 때 호출된다.
- 약한 참조(Weak Reference)
    - weakPerson 변수는 Person 객체를 약한 참조로 참조한다.
    - 약한 참조는 해당 객체를 강하게 소유하지 않으며, 참조되는 객체가 메모리에서 해제되면 자동으로 nil이 된다.
- 소유자 패턴의 활용
    - if case let strongPerson? = weakPerson을 통해 소유자 패턴을 활용한다.
    - 패턴 매칭을 수행하여 weakPerson의 값을 약한 참조로부터 가져온다.
    - 패턴 매칭이 성공하고 값이 존재한다면(weakPerson이 nil이 아니라면), strongPerson 상수에 값을 할당한다.
이렇게 매칭이 성공하고 값이 존재하는 경우, strongPerson은 해당 객체의 강한 참조를 나타내며 해당 객체의 속성에 접근할 수 있다.

소유자 패턴은 객체 간의 의존성을 명확히 표현하고, 메모리 관리를 안전하게 처리할 수 있도록 도와준다. 객체의 생성과 소멸, 메모리 사용 등을 적절하게 관리하여 코드의 안정성과 가독성을 높일 수 있다.



## 표현식 패턴(Expression Pattern)
 매칭에서 특정 표현식이나 조건을 충족하는지를 판단하는 패턴이다. 일반적으로 패턴 매칭에서 사용되는 패턴은 특정 값이나 구조를 나타내는 것이지만, 표현식 패턴은 값을 평가하고 결과에 따라 패턴을 매칭시킬 수 있다.
 
### switch문과 사용하는 표현식 패턴
 switch 문에서 `case`절에 표현식 패턴을 사용하면, 해당 표현식을 평가하고 결과에 따라 매칭 여부를 결정한다.
```swift
let number = 6

switch number {
case let x where x % 2 == 0:
    print("\(x) is an even number")
default:
    print("\(number) is not an even number")
}
```

### enum과 사용하는 표현식 패턴
표현식 패턴을 사용하여 enum의 케이스에 매칭하면, 각 케이스에 따른 다양한 동작을 수행할 수 있다. 이를 통해 코드를 더 유연하고 표현력있게 작성할 수 있다.
```swift
enum Weather {
    case sunny(temperature: Double)
    case cloudy(temperature: Double)
    case rainy
}

let todayWeather = Weather.cloudy(temperature: 25)

switch todayWeather {
case .sunny(let temperature) where temperature > 30:
    print("It's a hot and sunny day!")
case .sunny(let temperature):
    print("It's a sunny day with temperature \(temperature) degrees")
case .cloudy(let temperature):
    print("It's a cloudy day with temperature \(temperature) degrees")
case .rainy:
    print("It's a rainy day")
}

```
위의 코드에서 Weather라는 enum은 여러 가지 케이스를 가지며, sunny, cloudy, rainy 케이스가 있다. 각 케이스는 연관된 값을 가지거나 특정 조건을 나타낼 수 있다.

todayWeather 변수는 Weather.cloudy(temperature: 25) 케이스를 가지고 있다. switch 문에서 todayWeather를 패턴 매칭하여 해당하는 케이스에 따른 동작을 수행한다.

표현식 패턴을 사용하여 `case .sunny(let temperature) where temperature > 30:`과 같이 케이스에 조건을 추가할 수 있다. 이를 통해 특정 조건을 만족하는 경우에만 매칭되도록 할 수 있다.

## History
- 230608 : 초안작성
