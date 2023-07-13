# Cocoa Design Pattern - Delegate 델리게이트 패턴

Delegate 패턴이란, 
특정 용도로 객체를 하나만 생성하여, 공용으로 사용하고 싶을 때 사용하는 디자인 패턴이다.

## Delegate패턴 예시(1) : Class with ViewController 
- ViewController에 구현한 Cless에 있어 ViewController가 대신 함수를 가지고 있는 경우이다.   
- 해당 함수는 ViewController의 ViewDidLoad 안에서 `MyClass()`객체의 함수를 시작하게 되어있다.
- 만약 자동으로 하는 것이 아니라 터치를 통해 Class 내부에서 동작을 하게 할 거라면 발동조건을 아래처럼 ViewDidLoad에 넣지 않아도된다. 

### 1. Delegate 프로토콜 만들기
프로토콜을 만드는 것은 이 프로토콜을 채택한다면 구현해야하는 필수 조건을 만드는 과정이다.
```swift
protocol MyDelegate {
    func didReceiveData(data: String)
}
```
### 2. Delegate 프로토콜을 채택하는 클래스 만들기

```swift
class MyClass {
    var delegate: MyDelegate?
    
    func sendData() {
        delegate?.didReceiveData(data: "Hello, World!")
    }
}

```
### 3. Delegate 객체 만들기
```swift
class ViewController: UIViewController, MyDelegate {

    let myObject = MyClass()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        myObject.delegate = self
        myObject.sendData()
    }
    
    func didReceiveData(data: String) {
        print(data)
    }
}


```

여기까지만 해도되는데 아래처럼 연결하는 경우가 있다.

### 4. Delegate 객체와 MyClass 인스턴스 연결하기

```swift
let myObject = MyClass()
let myDelegateObject = MyDelegateObject()

myObject.delegate = myDelegateObject
myObject.sendData() // "Hello, World!" 출력
```


## Delegate패턴 예시(2) : VC with VC 
화면이동간 init 시점에 데이터를 보낼 수 있어 자주 사용하는 방법이다. 

### 1. Delegate 프로토콜 만들기
프로토콜을 만드는 것은 이 프로토콜을 채택한다면 구현해야하는 필수 조건을 만드는 과정이다.
```swift
protocol MyDelegate {
    func doSomething()
}
```
### 2. Delegate 프로토콜을 채택하는 A ViewController 만들기
- Class옆에는 프로토콜명을 적어서 채택해준다
- 정해진 프로토콜의 필수조건을 구현해준다. 
```swift
class AViewController: UIViewController, MyDelegate {
    
    func doSomething() {
        print("AViewController에서 수행된 doSomething 함수")
    }
}

```
### 3. A VC 와 B VC 를 연결하고 A VC 입장에서 delegate를 self로 지정해준다.  
```swift
class AViewController: UIViewController, MyDelegate {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        let bViewController = BViewController()
        bViewController.delegate = self
        self.navigationController?.pushViewController(bViewController, animated: true)
    }
    
    func doSomething() {
        print("AViewController에서 수행된 doSomething 함수")
    }
}

```

### 4. Delegate를 위임할 B ViewController 구현하기

```swift
class BViewController: UIViewController {
    
    var delegate: MyDelegate?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        delegate?.doSomething()
    }
}

```
