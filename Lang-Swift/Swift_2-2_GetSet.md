# Swift 2-2. getter / setter

## 개념 정리

`getter`와 `setter`는 **연산 프로퍼티(Computed Property)**에서 값을 **읽거나(set)** **설정할 수 있도록** 해주는 메서드 블록입니다.

- `get` → 값을 읽을 때 실행
- `set` → 값을 변경할 때 실행



<br><br>

---

## ⚙️ 기본 예시

```swift
struct Temperature {
    var celsius: Double

    var fahrenheit: Double {
        get {
            return celsius * 1.8 + 32
        }
        set {
            celsius = (newValue - 32) / 1.8
        }
    }
}
```

- `fahrenheit`는 연산 프로퍼티
- `get`은 값을 읽을 때, `set`은 값을 설정할 때 호출
- `set`의 매개변수는 기본적으로 `newValue`라는 키워드 사용



<br><br>

---

## 🧠 set의 이름을 커스터마이징 할 수도 있어요

```swift
var temperatureInFahrenheit: Double {
    get {
        return celsius * 1.8 + 32
    }
    set(inputTemp) {
        celsius = (inputTemp - 32) / 1.8
    }
}
```

- `newValue` 대신 직접 이름을 정할 수 있음



<br><br>

---

## 📌 읽기 전용(get-only)

```swift
var area: Double {
    return width * height
}
```

- `get`만 존재하는 경우, **읽기 전용**
- `get` 키워드 생략 가능



<br><br>

---

## 📦 저장 프로퍼티와는 다름에 주의

- 저장 프로퍼티는 `get/set`을 구현할 수 없음
- `var name: String` 이런 건 내부에 `get/set`을 넣지 않음

---

## 🤔 연산 프로퍼티 vs 함수

```swift
var area: Double {
    return width * height
}

func area() -> Double {
    return width * height
}
```

- 같은 동작을 할 수 있음
- **"값처럼 사용하고 싶다"**면 연산 프로퍼티
- **"동작(행위)처럼 보이고 싶다"**면 함수



<br><br>

---

## 💡 마무리 요약

| 항목 | 설명 |
|------|------|
| `get` | 값을 읽을 때 동작 |
| `set` | 값을 저장할 때 동작 (입력은 `newValue`) |
| 읽기 전용 | `get`만 있는 연산 프로퍼티 |
| 메모리 | 실제 값 저장 X, 계산 결과 반환 |


<br><br>

---

> 연산 프로퍼티는 내부 로직을 숨기고 값처럼 사용할 수 있어 **코드 가독성과 캡슐화**에 유리합니다.
