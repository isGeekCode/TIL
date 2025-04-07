# 1-5. 옵셔널 (Optional)

Swift에서는 **값이 있을 수도 있고 없을 수도 있음(nil)**을 표현하기 위해 옵셔널을 사용합니다.

## 왜 필요할까?

실제로 앱을 만들다 보면 외부 API로부터 데이터를 받을 때 값이 없는 경우가 흔합니다.  
예를 들어 어떤 유저는 `profileImage`가 있을 수 있고, 어떤 유저는 등록하지 않아 없을 수도 있습니다.

또는 구조체로 설명하자면, 예를 들어:

```swift
struct Person {
    var name: String
    var bag: String? // 가방이 있을 수도 있고, 없을 수도 있음
}

let man = Person(name: "John", bag: nil)
```

이처럼 옵셔널은 "존재할 수도 있고, 존재하지 않을 수도 있음"이라는 **현실 세계의 불확실성**을 반영하는 데 꼭 필요한 개념입니다.

---

## ✅ 옵셔널의 기본 사용

```swift
var name: String? = "Pepper"
print(name) // Optional("Pepper")
```

- `String?`는 "이 문자열이 있을 수도 있고, 없을 수도 있음"을 의미합니다.
- 값이 없을 경우 `nil`이 들어갈 수 있습니다.


<br>

옵셔널은 초기값이 없어도 사용가능

```swift
var nickname: String?  // 초기값 없이 선언 → 기본값은 nil
print(nickname)        // nil
```

- 물론 명시적으로 `= nil`을 써도 동일한 의미입니다.

```swift
name = nil
print(name) // nil
```

<br><br>

---

## ✅ 옵셔널을 안전하게 꺼내는 방법

### 1. 강제 언래핑 (`!`)

```swift
let name: String? = "Pepper"
print(name!) // ⚠️ 강제로 꺼냄 (비추천)
```

- `nil`일 경우 앱이 크래시 납니다. 되도록 피하세요.

### 2. 옵셔널 바인딩 (`if let`)
if문을 이용해 꺼내는 방법입니다. 

```swift
let name: String? = "Pepper"

if let unwrappedName = name {
    print("Hello, \(unwrappedName)")
} else {
    print("No name")
}
```




### 3. `guard let`

```swift
func greet(_ name: String?) {
    guard let name = name else {
        print("No name")
        return
    }
    print("Hello, \(name)")
}
```

- 함수 초반에 옵셔널 해제하고, 이후 코드를 깔끔하게 유지할 수 있습니다.


<br><br>

---


## ✅ nil 병합 연산자 (`??`)

> `??` 연산자는 "nil 병합 연산자" 또는 "닐 콜레싱(nil coalescing)" 연산자라고도 불립니다.

옵셔널 값이 `nil`일 경우, 기본값을 제공하여 안전하게 처리할 수 있습니다.

```swift
let nickname: String? = nil
let displayName = nickname ?? "Anonymous"
print(displayName) // "Anonymous"
```

- 위 코드에서 `nickname`이 nil이면 `"Anonymous"`가 사용됩니다.
- 주로 **옵셔널 파싱 시 지역 변수로 처리할 때** 자주 사용됩니다.


<br><br>

---


## ✅ 옵셔널 체이닝

```swift
struct User {
    var profile: Profile?
}
struct Profile {
    var name: String
}

let user: User? = User(profile: Profile(name: "Pepper"))
let username = user?.profile?.name
print(username) // Optional("Pepper")
```

- 옵셔널이 중첩된 구조에서 안전하게 접근할 수 있게 해주는 문법입니다.


<br><br>

---


## 🔍 옵셔널 선언 시 주의점

옵셔널 타입으로 선언한 변수는 실제 사용 시 **항상 언래핑이 필요**합니다.  
특히 함수 내부에서 옵셔널 파라미터를 받는 경우, 지역 변수에 바인딩하여 사용해야 오류를 방지할 수 있습니다.

예시:
```swift
func greet(name: String?) {
    // 옵셔널 파라미터를 지역 변수로 언래핑
    guard let name = name else {
        print("No name")
        return
    }
    print("Hello, \(name)")
}
```
