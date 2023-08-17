# Cocoa Design Pattern - Observer 옵저버 패턴

옵저버 패턴을 파티가 시작되었다는 상황으로 간단하게 설명해보려고 한다.

- 주체(Subject) 역할: 파티 주최자
- 옵저버(Observer) 역할: 친구들

파티 주최자는 파티가 시작되었을 때 친구들에게 알림을 보내야 한다. 

친구들은 '파티가 시작되었을 때 알림을 보내줘'라는 의사를 파티 주최자에게 알리고, 주최자는 파티가 시작되면 친구들에게 알림을 보낸다.

- 파티 주최자(Subject)는 파티 시작시 호출되는 startParty() 메서드를 가지고 있다. 이 메서드는 등록된 모든 친구들(옵저버들)에게 알림을 보내도록 구현되어 있다.

- 친구들(옵저버들)은 파티 주최자에게 구독(subscribe)하여 알림을 받기 원하는 의사를 표현한다.

- 파티 주최자는 친구들을 등록한다 : `addObserver()`

- 파티가 시작되었을 때 등록된 친구들에게 알림을 보낸다 : `notifyObservers()`

이렇게 옵저버 패턴을 사용하면 파티 주최자와 친구들 사이의 관계를 유연하게 만들 수 있고, 파티가 시작되었다는 알림을 받고 싶은 친구들은 주체(파티 주최자)와 의사소통하여 원하는 알림을 받을 수 있다.

## 사용법
```swift

// 옵저버(Observer) 프로토콜
protocol Observer: AnyObject {
    func update(temperature: Double)
}

// 구독할(Display) 클래스 - 옵저버(Observer) 역할
class Display: Observer {
    func update() {
        // update동작 구현
    }
}


// 주체(Subject) 프로토콜
protocol Subject {
    var observers: [Observer] { get set }
    func add(observer: Observer)
    func remove(observer: Observer)
    func notifyObservers()
}

class Thermometer: Subject {
    var observers: [Observer] = []
    var temperature: Double = 0.0 {
        didSet {
            notifyObservers()
        }
    }

    func add(observer: Observer) {
        observers.append(observer)
    }

    func remove(observer: Observer) {
        if let index = observers.firstIndex(where: { $0 === observer }) {
            observers.remove(at: index)
        }
    }

    func notifyObservers() {
        for observer in observers {
            observer.update(temperature: temperature)
        }
    }
}
```


## Observer패턴의 흐름



## Observer패턴의 한계성

이 패턴을 학습하다보니 느껴지는 점은  

굉장히 유용해보이는데, 막상 사용하려고 보면   

굳이...? 라는 생각이 들었다.  

그래서 한참을 물고 늘어졌다.  

소규모의 앱에서는 프로퍼티 옵저버나 NotificationCenter를 사용하는 것이 훨씬

효율적이지만

Observer패턴이 빛을 발하는 순간은 앱의 규모가 커졌을 때가 아닌가 싶다.  

Observer는 AnyObject의 타입으로 되어있기 때문에 정말 유연하게 사용할 수 있기 때문에,  
 
이 패턴은 앱의 규모가 커졌을 때, 필요한 패턴이 아닐까? 하는 생각이 든다.  


## 3개의 예제

### 🍊 예제1 : 애플스토어에서 고객들에게 알림
```swift

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        test()
    }

    func test() {
        // 애플 스토어 객체 생성 및 관찰자(고객) 객체들 생성
        let appleStore = AppleStore(observers: [])
        
        let first = Customer(id: "first")
        let second = Customer(id: "second")
        let third = Customer(id: "third")
        
        // 고객들이 애플 스토어를 관찰(구독)하도록 등록
        appleStore.subscribe(observer: first)
        appleStore.subscribe(observer: second)
        appleStore.subscribe(observer: third)
        
        // 애플 스토어에서 첫번째 알림 전달
        appleStore.notify(message: "첫번째 알림!!")
        
        // 세번째 고객이 애플 스토어 구독 해지
        appleStore.unSubscribe(observer: third)
        
        // 애플 스토어에서 두번째 알림 전달
        appleStore.notify(message: "두번째 알림!!")
    }
}

// 옵저버(Observer) 프로토콜
protocol Observer {
    var id: String { get set }
    func update(message: String)
}

// 고객
class Customer: Observer {
    var id: String
    
    // 초기화
    init(id: String) {
        self.id = id
    }
    
    // 알림을 수신하고 처리하는 메서드
    func update(message: String) {
        print("\(id) → \(message) 수신")
    }
}

// 주체 프로토콜
protocol Subject {
    var observers: [Observer] { get set }
    func subscribe(observer: Observer)
    func unSubscribe(observer: Observer)
    func notify(message: String)
}

// 애플 스토어
class AppleStore: Subject {

    var observers: [Observer]
    
    // 초기화
    init(observers: [Observer]) {
        self.observers = observers
    }
    
    // 관찰자(고객)를 구독목록에 추가
    func subscribe(observer: Observer) {
        self.observers.append(observer)
    }
    
    // 관찰자(고객)를 구독목록에서 제거
    func unSubscribe(observer: Observer) {
        if let idx = self.observers.firstIndex(where: { $0.id == observer.id}) {
            self.observers.remove(at: idx)
        }
    }
    
    // 애플 스토어에서 알림을 모든 관찰자(고객)들에게 전달
    func notify(message: String) {
        for observer in observers {
            observer.update(message: message)
        }
    }
}

```

### 🍊 예제2 : 온도가 변경됐을 때, 디스플레이에 알리는 예제

```swift
import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        testThermometer()
    }

    func testThermometer() {
        let thermometer = Thermometer()
        let display1 = Display()
        let display2 = Display()

        // 디스플레이 클래스들을 온도계의 관찰자로 등록
        thermometer.add(observer: display1)
        thermometer.add(observer: display2)

        // 온도 변경 및 관찰자에게 알림
        thermometer.temperature = 25.0
        thermometer.temperature = 30.0

        // 디스플레이 클래스들을 온도계의 관찰자에서 제거
        thermometer.remove(observer: display2)

        // 온도 변경 및 관찰자에게 알림
        thermometer.temperature = 27.5
    }
}

// 옵저버(Observer) 프로토콜
protocol Observer: AnyObject {
    func update(temperature: Double)
}

// 주체(Subject) 프로토콜
protocol Subject {
    var observers: [Observer] { get set }
    func add(observer: Observer)
    func remove(observer: Observer)
    func notifyObservers()
}

// 온도계(Thermometer) 클래스 - 주체(Subject) 역할
class Thermometer: Subject {
    var observers: [Observer] = []
    var temperature: Double = 0.0 {
        didSet {
            notifyObservers()
        }
    }

    func add(observer: Observer) {
        observers.append(observer)
    }

    func remove(observer: Observer) {
        if let index = observers.firstIndex(where: { $0 === observer }) {
            observers.remove(at: index)
        }
    }

    func notifyObservers() {
        for observer in observers {
            observer.update(temperature: temperature)
        }
    }
}

// 디스플레이(Display) 클래스 - 옵저버(Observer) 역할
class Display: Observer {
    func update(temperature: Double) {
        print("현재 온도: \(temperature)도")
    }
}


```

### 🍊 예제3 : 학생들 출석 체크 확인

```swift

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        
        testAttendance()
    }
    
    func testAttendance() {
        let attendanceChecker = AttendanceManager()
        let student1 = Student()
        let student2 = Student()
        
        // 학생들이 출석 체크를 관찰(구독)하도록 등록
        attendanceChecker.add(observer: student1)
        attendanceChecker.add(observer: student2)
        
        // 출석 여부 변경 및 관찰자에게 알림
        attendanceChecker.isAttending = true
        attendanceChecker.isAttending = false
        
        // 학생들을 출석 체크 관찰자에서 제거
        attendanceChecker.remove(observer: student2)
        
        // 출석 여부 변경 및 관찰자에게 알림
        attendanceChecker.isAttending = true
    }
}

// 옵저버(Observer) 프로토콜
protocol Observer: AnyObject {
    func update(isAttending: Bool)
}

// 출석 관리자(AttendanceManager) 클래스 - 주체(Subject) 역할
class AttendanceManager {
    var observers: [Observer] = []
    var isAttending: Bool = false {
        didSet {
            notifyObservers()
        }
    }
    
    func add(observer: Observer) {
        observers.append(observer)
    }

    func remove(observer: Observer) {
        if let index = observers.firstIndex(where: { $0 === observer }) {
            observers.remove(at: index)
        }
    }
    
    func notifyObservers() {
        for observer in observers {
            observer.update(isAttending: isAttending)
        }
    }
}

// 학생(Student) 클래스 - 옵저버(Observer) 역할
class Student: Observer {
    func update(isAttending: Bool) {
        if isAttending {
            print("출석했습니다.")
        } else {
            print("결석했습니다.")
        }
    }
}


```




## History
- 230727 : 초안작성
- 230728 : Observer패턴의 한계성 추가
