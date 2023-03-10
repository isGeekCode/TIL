# KVC와 KVO

KVC (Key-Value Coding) 및 KVO (Key-Value Observing)는 iOS 개발에서 매우 유용한 개념이다.
## KVC (Key-Value Coding)

객체의 프로퍼티에 대한 접근을 키-값 쌍으로 처리하는 방법이다. 일반적으로 객체의 프로퍼티에 접근하기 위해서는 .(도트) 연산자를 사용하여 객체의 프로퍼티를 직접 참조해야한다. 하지만 KVC를 사용하면 Key를 사용하여 객체의 프로퍼티에 접근할 수 있다. 이를 통해 객체의 프로퍼티에 대한 Value를 쉽게 설정하거나 가져올 수 있다.

예를 들어, person 객체가 있고, name이라는 문자열 프로퍼티를 가지고 있다고 가정해보자. person 객체의 name 프로퍼티에 KVC를 사용하여 접근하려면 아래와 같이 코드를 작성할 수 있다.

```swift
person.setValue("John Doe", forKey: "name")
let name = person.value(forKey: "name") as? String

```
위 코드에서 setValue(_:forKey:)를 사용하여 person 객체의 name 프로퍼티를 설정하고, value(forKey:)를 사용하여 name 프로퍼티 값을 가져올 수 있다.

```swift
class Person: NSObject {
    var name: String = ""
    var age: Int = 0
}

let person = Person()
person.setValue("John Doe", forKey: "name")
person.setValue(30, forKey: "age")

let name = person.value(forKey: "name") as? String // "John Doe"
let age = person.value(forKey: "age") as? Int // 30
```



## KVO(Key-Value Observing)
객체의 프로퍼티 값 `변경`을 관찰하고, 변경 사항에 대한 알림을 받을 수 있는 기능이다. KVO를 사용하면 다른 객체의 프로퍼티 값 변경에 대한 알림을 수신하여, 이를 사용하여 적절한 대응을 할 수 있다.

예를 들어, person 객체의 name 프로퍼티가 변경될 때마다 이를 관찰하고, 변경 내용에 대한 로그를 출력하는 코드를 작성해보자.

```swift
class MyObserver: NSObject {
    @objc dynamic var name: String = ""
    
    override init() {
        super.init()
        self.addObserver(self, forKeyPath: "name", options: .new, context: nil)
    }
    
    deinit {
        self.removeObserver(self, forKeyPath: "name")
    }
    
    override func observeValue(forKeyPath keyPath: String?,
                               of object: Any?,
                               change: [NSKeyValueChangeKey : Any]?,
                               context: UnsafeMutableRawPointer?) {
        if keyPath == "name" {
            if let newValue = change?[.newKey] {
                print("name has changed to \(newValue)")
            }
        }
    }
}

let person = Person()
let observer = MyObserver()

person.name = "John Doe"
// "name has changed to John Doe" 출력

```

위 코드에서 MyObserver 클래스를 작성하여 name 프로퍼티에 대한 KVO를 설정했다. 이제 person 객체의 name 프로퍼티를 변경할 때마다, MyObserver 클래스에서 observeValue(forKeyPath:of:change:context:) 메서드가 호출된다.


다른 예
```swfit
class Car: NSObject {
    @objc dynamic var brand: String
    @objc dynamic var model: String
    @objc dynamic var price: Int
    
    init(brand: String, model: String, price: Int) {
        self.brand = brand
        self.model = model
        self.price = price
        super.init()
    }
}

class CarObserver: NSObject {
    @objc var car: Car
    
    init(car: Car) {
        self.car = car
        super.init()
        
        // car 객체의 프로퍼티 변경을 감지하기 위한 KVO 등록
        self.car.addObserver(self, forKeyPath: #keyPath(Car.brand), options: [.new, .old], context: nil)
        self.car.addObserver(self, forKeyPath: #keyPath(Car.model), options: [.new, .old], context: nil)
        self.car.addObserver(self, forKeyPath: #keyPath(Car.price), options: [.new, .old], context: nil)
    }
    
    deinit {
        // 등록한 KVO 제거
        self.car.removeObserver(self, forKeyPath: #keyPath(Car.brand))
        self.car.removeObserver(self, forKeyPath: #keyPath(Car.model))
        self.car.removeObserver(self, forKeyPath: #keyPath(Car.price))
    }
    
    // KVO 이벤트가 발생하면 호출됨
    override func observeValue(forKeyPath keyPath: String?, of object: Any?, change: [NSKeyValueChangeKey : Any]?, context: UnsafeMutableRawPointer?) {
        guard let keyPath = keyPath, let change = change else {
            return
        }
        
        let oldValue = change[.oldKey] ?? ""
        let newValue = change[.newKey] ?? ""
        
        print("Car's \(keyPath) property has changed from \(oldValue) to \(newValue)")
    }
}

let car = Car(brand: "BMW", model: "X5", price: 100000)
let carObserver = CarObserver(car: car)

car.brand = "Audi" // "Car's brand property has changed from BMW to Audi" 출력
car.model = "A8" // "Car's model property has changed from X5 to A8" 출력
car.price = 200000 // "Car's price property has changed from 100000 to 200000" 출력


```
위 예제에서는 Car 클래스와 CarObserver 클래스를 정의했다. Car 클래스는 브랜드, 모델, 가격 세 개의 프로퍼티를 가지며, CarObserver 클래스는 Car 객체를 받아 KVO를 이용해 프로퍼티 변경을 감지하고, 로그를 찍는다.

KVO를 사용하여 Car 객체의 프로퍼티 변경을 감지하려면, CarObserver 클래스에서 addObserver(_:forKeyPath:options:context:) 메서드를 이용하여 KVO를 등록해야 한다. 이후 프로퍼티가 변경될 때마다 observeValue(forKeyPath:of:change:context:) 메서드가 호출되어 로그를 찍는다.

마지막으로 Car 객체의 프로퍼티 값을 변경하면, 등록된 KVO가 작동하여 CarObserver 클래스의 observeValue(forKeyPath:of:change:context:) 메서드가 호출되어 로그를 찍는다

이처럼 KVO를 이용하면 객체의 프로퍼티 변경을 감지하여 이를 처리할 수 있고, 이를 통해 객체 간의 상호작용을 보다 쉽게 구현할 수 있다.

### 무조건 KVO를 하려면 NSObject를 써야할까

KVO는 Objective-C 런타임 기능 중 하나이므로, KVO를 사용하려면 KVO가 지원되는 Objective-C 런타임에서 구동되어야 한다. 따라서, KVO를 사용하기 위해서는 NSObject 클래스를 상속받은 클래스를 구현해야한다.

Swift 클래스는 기본적으로 NSObject 클래스를 상속받지 않다. 그러나, Swift에서는 @objc 키워드를 사용하여 클래스와 프로퍼티를 Objective-C와 호환되도록 만들 수 있다. 또 이를 통해 Swift 클래스에서도 KVO를 구현할 수 있다.

따라서, KVO를 사용하려면 NSObject 클래스를 상속받은 클래스를 구현해야하는 것은 아니며, @objc 키워드를 사용하여 Swift 클래스에서도 KVO를 구현할 수 있다. 하지만, @objc 키워드를 사용하면 Objective-C와의 호환성을 유지할 수 있으므로, 가능하면 사용하는 것이 좋다.
