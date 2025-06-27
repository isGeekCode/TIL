# Swift 2-3. 프로퍼티 옵저버 (`willSet`, `didSet`)

## ✅ 프로퍼티 옵저버란?

값이 **변경되기 직전** 또는 **변경된 직후**에 어떤 동작을 수행하고 싶을 때 사용하는 감시자(Observer)입니다.

Swift에서는 다음과 같은 옵저버를 제공합니다:

- `willSet`: 값이 **변경되기 직전** 호출됨
- `didSet`: 값이 **변경된 직후** 호출됨

> 주로 UI 업데이트, 로깅, 데이터 동기화 등의 목적으로 사용됩니다.


<br><br>

---


## ⚙️ 사용 예시

```swift
var name: String = "Pepper" {
    willSet {
        print("이름이 '\(name)'에서 '\(newValue)'로 바뀌려고 해요.")
    }
    didSet {
        print("이름이 '\(oldValue)'에서 '\(name)'로 바뀌었어요.")
    }
}
```

```swift
name = "Chili"
// willSet: 이름이 'Pepper'에서 'Chili'로 바뀌려고 해요.
// didSet:  이름이 'Pepper'에서 'Chili'로 바뀌었어요.
```

- `newValue`: 새로 설정될 값 (`willSet`에서 사용)
- `oldValue`: 이전 값 (`didSet`에서 사용)


<br><br>

---


## 💡 옵저버는 언제 사용 가능한가?

옵저버는 **저장 프로퍼티에만 적용**할 수 있으며,  
**초기값이 있는 변수(`var`)**에만 붙일 수 있습니다.

```swift
var age: Int = 0 {
    didSet {
        print("나이 변경: \(oldValue) → \(age)")
    }
}
```


<br><br>

---


## 🧠 연산 프로퍼티에는 사용할 수 없음

```swift
var area: Double {
    get {
        return width * height
    }
    set {
        // 연산 프로퍼티에는 willSet/didSet 사용 불가
    }
}
```

> 연산 프로퍼티는 값 자체를 저장하지 않기 때문에 감시가 불가능합니다.


<br><br>

---


## 📌 옵저버가 유용한 순간

| 상황 | 사용 이유 |
|------|----------|
| 텍스트 필드 값 변경 감지 | `didSet`을 활용해 UI 반영 |
| 로깅 | 변경 이력을 남기기 위해 사용 |
| 외부 값과 동기화 | 값 변경 시 API 호출 등 외부 연동 처리 |


<br><br>

---


## 🚨 주의사항

- `willSet`과 `didSet`은 **값이 변경될 때만 동작**합니다
- 값이 같다면 호출되지 않습니다

```swift
var number = 10 {
    didSet {
        print("값 바뀜")
    }
}

number = 10  // 같은 값 → 호출 안됨
number = 20  // 다른 값 → 호출됨
```


<br><br>

---


> 값 변화 감지는 옵저버로!  
> UI 반영이나 동기화 작업은 `didSet`이 특히 많이 사용돼요.


<br><br>

---


## 🔄 바인딩과 옵저버

`didSet`은 값의 변화를 감지해 뷰를 갱신하는 데 많이 사용됐습니다.  
초기 iOS 개발에서는 뷰와 모델을 **수동으로 바인딩**할 때 이 방식이 자주 쓰였어요.

```swift
var text: String = "" {
    didSet {
        label.text = text
    }
}
```

> 현재는 Combine, SwiftUI의 `@Published`, `@ObservedObject` 같은 **선언형 바인딩 도구**가 주로 사용됩니다.


<br><br>

---


## 🧬 리액티브 프로그래밍의 원형

`didSet`은 오늘날의 Combine이나 RxSwift 같은 **리액티브 프로그래밍**의 원조격입니다.

- 값이 바뀌면 자동으로 반응하는 흐름을 구성한다는 점에서,  
  `didSet`은 **리액티브의 가장 단순한 형태**라고 볼 수 있어요.

```swift
var isLoggedIn: Bool = false {
    didSet {
        loginButton.isHidden = isLoggedIn
    }
}
```

- 물론 Combine처럼 스트림을 연결하거나 다양한 연산자를 지원하지는 않지만,  
  UI나 상태 동기화를 위해 **값 변경 → 반응** 흐름을 최초로 보여준 구조입니다.

> 옵저버는 리액티브 프로그래밍의 뿌리이자, 단방향 데이터 흐름의 기초이기도 해요.

<br><br>

---

## 🤔 지금은 안 써도 될까?

`Combine`, `@Published`, `RxSwift` 같은 리액티브 프레임워크가 널리 쓰이면서  
`didSet`, `willSet` 같은 옵저버는 덜 사용되는 느낌이 들 수 있어요.  
하지만 **지금도 충분히 유효하고 실용적인 이유**가 있습니다.

### ✅ 프로퍼티 옵저버를 여전히 쓰는 이유

- **간단한 UI 바인딩에 효과적**  
  복잡한 선언형 바인딩보다 코드가 단순하고 직관적이에요.

- **라이브러리 없이도 가능**  
  Combine 등 외부 도구 없이도 반응형 구조 구현이 가능합니다.

- **디버깅/로깅 도구로 유용**  
  값 변화 추적을 빠르게 설정할 수 있어 디버깅에 많이 사용됩니다.

- **변경 시점 컨트롤에 유리**  
  값이 변경되기 전(`willSet`)이나 후(`didSet`)의 동작을 쉽게 제어할 수 있어요.

> 복잡한 구조에는 Combine이 좋고,  
> **작고 빠른 반응**에는 `didSet`이 여전히 강력한 선택입니다!
