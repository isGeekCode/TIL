# Swift - 참조(Strong, weak, unowned)


아주 간단한 예로 설명하자면..

엄마와 나를 예로 들어보자. 

- Strong
    - 엄마와 아이가 손을 꼭 잡고 있다고 가정해보자. 
    - 엄마가 어디로 가든지 아이도 따라가야한다.
    - 엄마가 아이 손을 잡고 있으면, 아이는 어디에도 가지 않고 엄마와 함께 있는 것이다. 

<br><br>

-  Weak
    - 엉마와 아이가 손을 잡고 있다고 가정해보자. 
    - 아이가 다른 곳에 가고 싶어하면 손을 놔줄 수 있다고 한다. 
    - 아이가 어딘가 가고 싶다고 결정하면, 아이는 자유롭게 이동할 수 있고, 엄마와 아이가 잡은 손은 자연스럽게 분리된다. 
    - 아이가 손을 놓고 이동하면, 엄마와 아이는 연결되어있지 않게 된다. 


<br><br>

- Unowned
    - 엄마와 아이는 항상 같이 다닌다.
    - 엄마 없이는 절대 집을 나서지 않는다. 
    - 만약 엄마가 여행을 가서 집을 비우면, 아이도 함께 가야한다.
    - 엄마가 없으면, 아이도 어디에도 갈 수 없게 된다. 
    - 만약 엄마가 사라지면, 큰 문제에 직면하게 된다. 

<br><br>

<br><br>

## Strong
기본적으로 대부분의 객체 참조에는 strong 참조가 사용된다.  
객체가 확실하게 필요하고, 메모리에서 유지되어야할 때, 사용한다.  
컨트롤러가 모델 데이터를 참조하거나, 컬렉션에서 객체를 관리할 때 주로 사용된다.  

```swift
class Person {
    var name: String

    init(name: String) {
        self.name = name
    }
}

var person1: Person? = Person(name: "John")
var person2: Person? = person1  // person2는 person1을 strong 참조

```
여기서 person2는 person1을 strong 참조하므로, person1은 메모리에서 유지된다.  


<br><br>

## weak
주로 두 객체 간의 순환 참조를 방지하기 위해 사용된다.  

- 특징
- weak 참조는 참조하는 객체가 메모리에서 해제될 때 자동으로 nil로 설정된다.  
    - 이는 참조하고 있는 객체에 더 이상 접근할 수 없음을 의미하며, 메모리 안전성을 제공한다.
- weak 참조는 주로 delegate 패턴이나 클로저 내에서 참조 사이클을 방지할 때 된다.  
- 참조하는 객체가 옵셔널이기 때문에, 항상 nil 검사를 해야 합니다.


```swift
class ViewController: UIViewController {
    weak var delegate: SomeDelegate?
}


// 혹은

class Employee {
    var name: String
    weak var manager: Manager?

    init(name: String) {
        self.name = name
    }
}

class Manager {
    var name: String
    var team: [Employee] = []

    init(name: String) {
        self.name = name
    }

    func manage(employee: Employee) {
        team.append(employee)
        employee.manager = self
    }
}

```
여기서 Employee 클래스는 Manager를 weak 참조하여, 매니저가 사라지면 manager 속성이 nil이 된다. 


- 어떤 상황에서 주로 사용할까?? 
- Delegate 패턴: 가장 흔한 사용 예는 delegate 패턴
    - 예를 들어, UITableView의 delegate나 dataSource는 weak 참조로 설정된다.  
    - delegate가 보통 컨트롤러와 같이 뷰보다 더 긴 생명주기를 가지고 있기 때문에 순환 참조를 방지하기 위해서다.  
- UI 컴포넌트에서 부모-자식 관계
    - 뷰 컨트롤러에서 여러 자식 뷰를 관리할 때, 이 자식 뷰들이 부모 뷰 컨트롤러를 참조해야 하는 경우가 있다.  
    - 이때 weak 참조를 사용하여 부모 뷰 컨트롤러와의 순환 참조를 방지할 수 있다.
- 클로저에서의 캡처 리스트
    - 클로저 내에서 self(자기 자신)를 참조할 때 순환 참조를 피하기 위해 weak을 사용한다.  
    - 예를 들어, 비동기 작업이 완료된 후에 어떤 작업을 수행해야 할 때, 클로저 내에서 self를 weak으로 참조하면 작업이 끝난 후에 객체가 필요 없어지면 자동으로 메모리에서 해제될 수 있다.  





<br><br>

## unowned
weak 참조와 유사하지만, 참조하는 객체가 같은 생명주기를 가질 때 사용된다.  
이는 주로 두 객체가 서로를 참조하지만 하나가 다른 하나 없이는 존재하지 않을 때 사용된다.  


- 특징:
    - unowned 참조는 참조하는 객체가 메모리에서 해제된 후에도 자동으로 nil로 설정되지 않는다.  
    - 따라서 참조된 객체가 이미 해제된 상태에서 접근하려고 하면 런타임 오류가 발생할 수 있다.  
    - unowned는 참조하는 객체와 참조되는 객체가 동시에 메모리에서 해제될 것이라는 보장이 있을 때 한다. 
    - unowned는 옵셔널이 아니므로 nil 검사를 할 필요가 없다.  

- 어디에 사용할까
    - 객체 간의 종속적인 관계
        - unowned는 참조하는 객체가 참조되는 객체와 동일한 또는 더 긴 생명주기를 가질 때 사용된다.  
        - 예를 들어, 부모 객체가 자식 객체를 생성하고, 자식 객체가 부모 객체를 참조해야 할 때, 부모 객체가 먼저 메모리에서 해제될 가능성이 없는 경우 unowned 참조를 사용할 수 있다.  

    - 초기화가 완료된 후에는 nil이 될 가능성이 없는 경우
        - 어떤 클래스의 인스턴스가 다른 인스턴스 없이는 존재할 수 없는 경우
        - 예를 들어 고객과 그 고객의 신용 카드의 관계와 같이, unowned를 사용하여 신용 카드가 고객 없이 존재하지 않음을 보장할 수 있다.  


```swift
class CreditCard {
    let number: UInt64
    unowned let customer: Customer

    init(number: UInt64, customer: Customer) {
        self.number = number
        self.customer = customer
    }
}

class Customer {
    let name: String
    var card: CreditCard?

    init(name: String) {
        self.name = name
    }

    func issueCard(number: UInt64) {
        self.card = CreditCard(number: number, customer: self)
    }
}

let customer = Customer(name: "John")
customer.issueCard(number: 1234567890123456)

```

CreditCard 클래스는 Customer를 unowned로 참조하여, 고객이 존재하는 한 크레딧 카드도 함께 존재하게 된다. 


이렇게 weak과 unowned 참조는 각각 상황에 맞게 선택하여 사용해야 하며, 객체의 생명주기와 메모리 관리 전략을 정확하게 이해하는 것이 중요하다.  





