# 2-4. 접근 제어자 (Access Control)

  

Swift에서는 코드의 ****접근 범위****를 제어할 수 있는 키워드를 제공합니다.  

이 접근 제어는 ****캡슐화(encapsulation)****를 가능하게 하여,  

불필요한 접근을 막고 유지보수를 쉽게 합니다.


<br><br>

---

## ✅ 접근 제어자의 종류
  

| 접근 제어자        | 설명                                |
| ------------- | --------------------------------- |
| `open`        | **가장 넓은 범위.** 다른 모듈에서 상속/오버라이딩 가능 |
| `public`      | 다른 모듈에서 접근은 가능, 상속/오버라이딩은 불가      |
| `internal`    | 같은 모듈 안에서만 접근 가능 (기본값)            |
| `fileprivate` | 같은 파일 안에서만 접근 가능                  |
| `private`     | 같은 스코프 안(클래스/구조체 등)에서만 접근 가능      |

  
<br><br>

---

## 🧪 간단 예시

  

```swift

class Person {

    private var name: String = "Pepper"

    fileprivate var age: Int = 30

    internal var job: String = "iOS Developer"

    public var company: String = "GeekCompany"

    open var favoriteColor: String = "Mint"

}

```

<br><br>

---

## 🔐 왜 사용할까?

- 외부에서 직접 접근하지 못하도록 막아야 할 데이터 보호
- 모듈 간 의존성을 줄이고 유지보수성 향상
- 오용 방지 및 캡슐화를 통한 안정성 확보

<br><br>

---

##  실전에서 자주 쓰는 조합

- 대부분은 `internal`을 기본으로 둠 (생략 가능)
- 외부 노출이 필요한 경우만 `public` 또는 `open`
- 파일 내 헬퍼 메서드 등은 `fileprivate`
- 진짜 외부 접근을 막고 싶은 건 `private`

  

```swift

class ViewController: UIViewController {

    private var userName: String = ""

    fileprivate func setupLayout() { ... }

    internal func bindViewModel() { ... }

    public func configure(with user: User) { ... }

}

```

  

> 실무에서는 보통 외부 공개 API는 `public`, 내부 전용은 `private` 또는 `fileprivate`로 나누는 게 일반적입니다.
  
<br><br>

---

## 외부에서 읽기만 가능하게 만들고 싶다면?

`private(set)` 접근 제어를 사용하면 **외부에서는 읽기만 가능하고**,  
**쓰기(set)는 내부에서만 가능**하게 만들 수 있습니다.

  

```swift

class Counter {

    private(set) var count: Int = 0

  

    func increment() {

        count += 1

    }

}

  

let counter = Counter()

print(counter.count)  // ✅ 읽기는 가능

counter.count = 10    // ❌ 오류: set은 private

```

  

> `private(set)`은 데이터를 보호하면서도 외부에 상태를 공개하고 싶은 경우 유용합니다.

<br><br>

---

## 📁 extension으로 파일을 분리할 때 주의점
  

Swift에서는 종종 기능을 역할별로 나누기 위해 `extension`을 별도 파일에 분리합니다.  

예를 들어 `MainViewController.swift`와 `MainVC+Layout.swift`로 나누는 경우입니다.


이때 **접근 제어자에 따라 extension에서 해당 멤버에 접근 가능한지 여부가 달라집니다.**

  

```swift

// MainViewController.swift

class MainViewController: UIViewController {

    private func fetchData() { ... }        // ❌ extension에서 접근 불가

    fileprivate func setUI() { ... }        // ❌ 다른 파일에서는 접근 불가

    internal func bind() { ... }            // ✅ 접근 가능

}

```

  

```swift

// MainVC+Layout.swift

extension MainViewController {

    func setupLayout() {

        // fetchData()     ❌ 접근 불가 (private)

        // setUI()         ❌ 접근 불가 (fileprivate은 같은 파일에서만)

        bind()             ✅ 접근 가능 (internal은 같은 모듈 내에서 가능)

    }

}

```


<br><br>

---

### 🔎 요약

| 접근 제어자| extension(다른 파일)에서 접근 가능? | 설명  |
|---------|--------|-------------|
| `private`     | ❌ 불가| 선언된 타입 내부에서만 사용 가능 |
| `fileprivate` | ❌ 불가| 같은 파일 안에서만 사용 가능     |
| `internal`    | ✅ 가능| 같은 모듈이면 접근 가능|
| `public`      | ✅ 가능| 외부 모듈도 접근 가능|

  

> 따라서 `extension`을 다른 파일에 작성할 계획이라면 `fileprivate` 대신 `internal`이나 `private(set)`을 고려하는 것이 좋습니다.
