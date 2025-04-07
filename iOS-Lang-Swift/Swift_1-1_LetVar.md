# 1-1. 변수와 상수 선언 (`let`, `var`)

## ✅ 개념 요약

| 선언 키워드 | 의미            | 변경 가능 여부 |
|-------------|------------------|----------------|
| `let`       | **상수** 선언     | ❌ 변경 불가     |
| `var`       | **변수** 선언     | ✅ 변경 가능     |

Swift는 타입 안전한 언어라서, 값을 선언하면 해당 타입에 고정됩니다.  
`let`으로 선언하면 **초기화된 이후 절대 변경할 수 없어요.**

---

## 🔤 사용 예시

```swift
let name = "Pepper"   // 상수
var age = 3           // 변수

age = 4               // ✅ OK
// name = "Apple"     // ❌ Error! 'let' 상수는 변경 불가
```

---

## 💡 타입 추론과 명시

```swift
let height = 180        // Int로 추론
let name = "Swift"      // String으로 추론

let score: Double = 95.5
var isPassed: Bool = true
```

---

## ⚠️ 주의할 점

### 1. `let`은 struct에서도 내부 변경 불가

```swift
struct User {
    var name: String
}

let user = User(name: "Pepper")
// user.name = "Siri"  // ❌ Error: 'user'는 변경 불가
```

### 2. `var`는 변경 가능

```swift
var user2 = User(name: "Pepper")
user2.name = "Siri"      // ✅ OK
```

---

## 🛠 실무 팁

- 가능한 한 **`let`을 기본으로 쓰고**, 정말 필요한 경우에만 `var`를 써라
- **불변성 유지**는 코드의 안정성과 예측 가능성을 높여줌
- ViewModel, UseCase 설계 시 `let` 사용을 기본 원칙으로 하자
