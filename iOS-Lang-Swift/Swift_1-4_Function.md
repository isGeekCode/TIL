
# 1-4. 함수 (Function)

함수는 반복되는 코드를 하나로 묶어 이름을 붙여 재사용성과 가독성을 높여주는 핵심 개념입니다.


---

## ✅ 기본 함수 정의

```swift
func sayHello() {
    print("Hello!")
}

sayHello() // "Hello!"
```

<br><br>


---

## ✅ 매개변수가 있는 함수

```swift
func greet(name: String) {
    print("Hi, \(name)!")
}

greet(name: "Pepper")
```

<br><br>


---

## ✅ 반환값이 있는 함수

```swift
func add(a: Int, b: Int) -> Int {
    return a + b
}

let sum = add(a: 3, b: 5)
print(sum) // 8
```

<br><br>


---

## ✅ 외부/내부 파라미터 이름

```swift
func multiply(_ a: Int, by b: Int) -> Int {
    return a * b
}

multiply(4, by: 2) // 8
```

<br><br>

---

## ✅ 기본값이 있는 매개변수

```swift
func greet(name: String = "Guest") {
    print("Hi, \(name)!")
}

greet()              // Hi, Guest!
greet(name: "Jane")  // Hi, Jane!
```

<br><br>


---

## ✅ inout 키워드

```swift
func doubleValue(_ number: inout Int) {
    number *= 2
}

var num = 10
doubleValue(&num)
print(num) // 20
```

<br><br>


---

## 💡 함수 설계에서 생각해볼 점

### 🎯 단일 책임 원칙 (Single Responsibility Principle)

함수는 하나의 기능만 하도록 설계하는 것이 좋습니다.  
너무 많은 역할을 가진 함수는 읽기 어렵고 재사용이 힘들어집니다.

잘못된 예:
```swift
func processUserInfo(name: String, age: Int) {
    print("Welcome, \(name)")
    saveToDatabase(name: name, age: age)
    sendWelcomeEmail(to: name)
}
```

개선된 예:
```swift
func greetUser(name: String) {
    print("Welcome, \(name)")
}

func saveUser(name: String, age: Int) {
    // ...
}

func notifyUser(name: String) {
    // ...
}
```

<br><br>


### 🧾 네이밍 컨벤션

- 함수 이름은 동사형으로 시작합니다 (e.g. `printName()`, `loadData()`)
- 이름만 봐도 역할이 드러나도록 작성합니다
- 함수 하나가 한 가지 책임을 가진다면, 그에 맞는 **짧고 명확한** 이름을 붙이기 쉽습니다
