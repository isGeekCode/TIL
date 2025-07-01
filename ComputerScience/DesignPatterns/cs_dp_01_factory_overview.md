# Factory Pattern 개요

## 1. 패턴 개요

- **Factory Pattern**은 객체 생성 로직을 별도 **팩토리 클래스나 메서드로 분리**하는 디자인 패턴이다.
- 객체 생성을 클라이언트 코드로부터 **캡슐화**하여, 사용하는 측은 구체적인 클래스에 의존하지 않고 객체를 생성할 수 있다.
- 주로 **조건에 따라 다른 객체를 반환**하거나, **객체 생성을 하위 클래스에 위임**할 때 사용된다.

🧠 쉽게 말해  
햄버거 가게에서 "불고기버거 주세요"라고 하면, 손님은 만드는 과정을 몰라도 결과만 받는다.  
**팩토리**는 이렇게 내부 생성 과정을 감추고 결과만 전달하는 역할이다.

---

## 2. 패턴의 장점

- **객체 생성 책임 분리**: 생성 로직이 코드 전반에 흩어지지 않음
- **유연한 구조**: 조건에 따라 생성 객체가 바뀌는 경우 적합
- **결합도 감소**: 클라이언트는 생성 로직 또는 구체 타입을 몰라도 됨

---

## 3. 주의사항

- 클래스 수가 늘어나 코드가 복잡해질 수 있음
- 단순한 상황에서는 과한 설계가 될 수 있음

---

## 4. 사용 예시

- `ImageFactory`: 포맷에 따라 다른 이미지 뷰 객체 생성 (jpg, png 등)
- `DialogFactory`: 상황에 맞는 팝업 생성 (에러, 경고, 확인 등)
- `TransportFactory`: 입력에 따라 자동차, 자전거, 기차 반환

---

## 5. 전통적 설계 방식 (GoF 방식)

GoF(Gang of Four)에서는 **Factory Method Pattern**을 다음처럼 정의한다:

- **공통 인터페이스 또는 추상 클래스** 기반
- **객체 생성 책임을 하위 클래스나 외부 팩토리에 위임**
- **다형성과 캡슐화**를 활용하여 유연한 확장성 확보

> ✅ 핵심은 단순한 생성 분리가 아니라,  
> **"다형성 기반의 객체 생성을 캡슐화하여 클라이언트 코드로부터 숨기는 것"**이다.


### Swift 예시

```swift
protocol Transport {
    func move()
}

class Car: Transport {
    func move() { print("Drive car") }
}

class Bike: Transport {
    func move() { print("Ride bike") }
}

enum TransportType {
    case car, bike
}

class TransportFactory {
    static func makeTransport(type: TransportType) -> Transport {
        switch type {
        case .car: return Car()
        case .bike: return Bike()
        }
    }
}

// 사용
let transport = TransportFactory.makeTransport(type: .car)
transport.move()  // "Drive car"
```

---

### 📌 인터페이스 또는 추상 클래스가 필요한 이유

전통적인 Factory Method Pattern에서는 **다형성(polymorphism)** 기반 설계가 핵심이다. 이를 위해서는 반드시 공통된 타입, 즉 **인터페이스 또는 추상 클래스**를 사용해야 한다.

- **다형성 활용**: 공통 타입만 알고 다양한 객체(Car, Bike 등)를 처리 가능  
- **확장에 유리**: 새로운 타입을 추가하더라도 기존 코드를 수정하지 않고 확장 가능  
- **유지보수 용이**: 생성자에 대한 변경 없이 공통 인터페이스만 따르도록 설계 가능  
- **의존성 역전**: 클라이언트는 구체 구현이 아닌 추상 타입에 의존함으로써 유연성 확보

💡 반면, 현대적인 실용 코드에서는 단순히 생성 책임을 분리하는 목적으로 Factory를 쓰기도 하며, 이 경우 인터페이스 사용은 필수는 아니다. 그러나 **GoF 기준의 엄격한 의미에서는 인터페이스/추상 클래스가 필수적 요소**이다.



---

## HISTORY
- 250701 : 초안작성
