# Swift - Class와 Struct

## 클래스란

클래스는 class라는 키워드를 사용한다.  

```swift
class Person {
    var name: String = ""
}
```

<br><br>


### 기본 생성

클래스 이름 뒤에 콜론(:)을 써주고 부모 클래스 이름을 써서 타입을 지정한다. 
```swift
var personVar: Person = Person()
```
혹은 타입은 생략할 수 있다.

```swift
var personVar = Person()
```

아래는 불변하는 값인 let으로 만들어보자

```swift
let personVar: Person = Person()
```
역시 타입은 생략할 수 있다.

```swift
let personVar = Person()
```

<br><br>

## 생성자 init
해당 내용은 [TIL: Initialization](https://github.com/isGeekCode/TIL/blob/main/iOS-Swift/about_Swift002Init.md)참고


<br><br>

### 상속

상속(Subclassing)이란 부모의 특성을 자녀가 물려받는 것을 말한다.  

프로그래밍에서의 상속도 비슷한 의미를 가진다.  

상속을 받는 경우, 부모의 변수와 메서드, 프로토콜 등등의 특징을 모두 물려받는다.

그래서 자식클래스는 부모클래스의 모든 요소들을 사용가능하다. 

상속을 하려면 상속받을 클래스 이름 뒤에 콜론(:)을 써주고 부모 클래스 이름을 쓰면 된다.

만약 상속받은 메서드를 다르게 사용하기 위해선 func 앞에 override 키워드를 추가한다. 


```swift
class Animal {
    var name: String
    
    init(name: String) {
        self.name = name
    }
    
    func makeSound() {
        print("Animal makes a sound")
    }
}

class Dog: Animal {
    override func makeSound() {
        print("Dog barks")
    }
}

class Cat: Animal {
    override func makeSound() {
        print("Cat meows")
    }
}

let dog = Dog(name: "Buddy")
let cat = Cat(name: "Whiskers")

print(dog.name)  // Output: Buddy
dog.makeSound()  // Output: Dog barks

print(cat.name)  // Output: Whiskers
cat.makeSound()  // Output: Cat meows
```

만약 부모클래스에서 선언했던 메서드도 동작을 하려면 override 메서드 내에서 `super.메서드`형태로 호출한다.
이때 탑다운 방식에 따라 `super.메서드` 의 위치에 맞게 호출이 된다. 
```
class Animal {
    var name: String
    
    init(name: String) {
        self.name = name
    }
    
    func makeSound() {
        print("Animal makes a sound")
    }
}

class Dog: Animal {
    override func makeSound() {
        super.makeSound()
        print("Dog barks")
    }
}

let dog = Dog(name: "Buddy")

print(dog.name)  // Output: Animal makes a sound  Buddy
dog.makeSound()  // Output: Dog barks
```

<br><br>

## 소멸자 Deinit

구조체는 프로퍼티에 맞는 이니셜라이저를 제공하지만  

클래스는 그렇지 않아서 클래스를 생성할 때, 인스턴스의 저장 프로퍼티를 초기화해야 한다.  

클래스 인스턴스는 참조 타입이므로 참조할 필요가 없을 때 메모리에서 해제된다.  

이 과정을 `소멸`이라고 하는데 소멸되기 직전 `deinit`라는 메서드가 호출된다.  

```swift
class Person {
    var name: String = ""
    
    deinit {
        print("Person 클래스의 인스턴스가 소멸됩니다")
    }
}

var person: Person? = Person()
person = nil
// Person 클래스의 인스턴스가 소멸됩니다
```


<br><br><br>

## Struct

우리가 자주사용하는 Int, Double, String는 struct로 정의되어있다.

구조체는 struct 키워드로 정의한다.

```swift
public struct Int : SignedInteger, Comparable, Equatable

public struct Double

public struct String
```

이런 데이터 타입들은 구조체로 구현한다.   

구조체에서는 상속X, 프로토콜만 존재한다. →  `SignedInteger`, `Comparable`, `Equatable`  


<br><br>

### 구조체 생성하기
구조체(Struct)는 클래스와 달리 init메서드를 필수로 하지않는다.

```swift
struct Point {
    var x: Int
    var y: Int
}

let origin = Point(x: 0, y: 0)
```

물론 init메서드를 구현해도된다.

```swift

struct Point {
    var x: Int
    var y: Int
    
    init(x: Int, y: Int) {
        self.x = x
        self.y = y
    }
}
let origin = Point(x: 0, y: 0)
```

<br><br><br>

## 참조타입와 값 타입 : Reference Type and Value Type


### 참조타입 살펴보기
클래스는 참조타입이고 구조체는 값타입이다. 

참조란 "공유된 상태"라고 할 수 있다.

한번 생성한 변수나 상수가 참조되면 한곳에서의 변경이 다른 곳에도 영향을 미친다. 


```swift
class Person {
    var name: String
    
    init(name: String) {
        self.name = name
    }
}

var person1 = Person(name: "Alice")
var person2 = person1

person2.name = "Bob"

print(person1.name)  // Output: Bob
print(person2.name)  // Output: Bob
```

한번 생성한 person1을 perseon2에 선언했다.  

그러면 person2는 person1과 운명공동체가 되는 것이다.

물론 위의 경우에서 person1의 값을 바꿔도 동일하게 적용된다.

```swift
class Person {
    var name: String
    
    init(name: String) {
        self.name = name
    }
}

var person1 = Person(name: "Alice")
var person2 = person1

person1.name = "Bob"

print(person1.name)  // Output: Bob
print(person2.name)  // Output: Bob

```

<br><br>

다만 클래스가 참조타입이라고 아래처럼 헷갈리지말자. 
이 경우는 엄연히 다른 값이다. 

```
var person1 = Person(name: "Alice")
var person2 = Person(name: "Bob")

print(person1.name)  // Output: Alice
print(person2.name)  // Output: Bob
```


<br><br>

### Value타입 살펴보기

이번엔 구조체를 살펴보자  

```swift
struct Person {
    var name: String
    
    init(name: String) {
        self.name = name
    }
}
```

구조체는 클래스처럼 일심공동체가 아니다.  

값 그 자체만 복사해주는 개념이다.  

서로 남남이라는 걸 기억하자.  

```swift
struct Person {
    var name: String
    
    init(name: String) {
        self.name = name
    }
}

var person1 = Person(name: "Alice")
var person2 = person1

print(person2.name)  // Output: Alice

person2.name = "Bob"

print(person1.name)  // Output: Alice
print(person2.name)  // Output: Bob
```

<br><br><br>

## 장단점

웬만하면 대부분의 데이터는 클래스로도 구조체로도 생성할 수 있다.  

그러면 어떻게 구별해서 생성하는 것이 좋을까??

- 클래스는 공유해야 할 데이터, 다형성 및 상속이 필요한 경우에 적합하다. 또한 주로 대형 데이터 모델링, 뷰 컨트롤러, 네트워크 통신 객체 등에 사용된다.
- 구조체는 간단한 데이터 모델링이나 값의 전달, 데이터 복사가 필요한 경우에 유용하다. 또한 스레드 안전성을 필요로 하는 상황에서도 사용될 수 있다.


### 클래스의 장단점

- 장점
    - 참조타입이라는 점
        - 클래스는 참조 타입으로 동작하며, 메모리에서 객체의 실제 데이터가 저장되는 것이 아니라 객체의 참조가 저장된다. 이로써 여러 변수나 상수가 동일한 객체를 참조할 수 있어 메모리 효율성을 높일 수 있다.
    - 상속 및 다형성
        - 클래스는 상속을 통해 다른 클래스를 확장하고 재사용할 수 있으며, 다형성을 지원한다. 이는 코드 재사용성과 유연한 설계를 가능하게 한다.
    - 동적 타입
        - 클래스는 런타임에 동적으로 타입 정보를 조사하거나 변경할 수 있는 기능을 제공합니다.
- 단점
    - 참조 관리
        - 오히려 참조가 독이 되는 경우가 있다. 클래스는 참조 카운팅(reference counting)을 통해 메모리 관리가 이루어지므로, 순환 참조 등으로 인해 메모리 누수(memory leak)가 발생할 수 있다.
    - 복잡성
        - 상속과 다형성을 사용하면 코드가 복잡해질 수 있다. 클래스 간의 관계와 의존성을 이해하기 어려울 수 있다.



### 구조체의 장단점

- 장점
    - 값 타입이라는 점
        - 변수나 상수에 할당될 때 복사되어 전달된다. 이로써 값을 복사하여 전달하므로 참조 관리 문제가 없다.
    - 불변성 및 안정성
        - 구조체의 프로퍼티는 기본적으로 불변성을 가지며, mutating 키워드로 제한된 변경을 통해 안정성을 높일 수 있다.
    - 스레드 안전성
        - 값 타입인 구조체는 여러 스레드 간의 데이터 공유 시 별도의 동기화 없이 스레드 안전성을 보장한다.
    - 가볍고 단순한 모델링
        - 구조체는 주로 간단한 데이터 모델링이나 값의 전달을 위해 사용되며, 복잡성을 줄이고 코드를 더 예측 가능하게 만든다.
- 단점
    - 복사와 비교의 오버헤드
        - 구조체는 값 복사가 이루어지므로 큰 데이터 구조를 다룰 때 오버헤드가 발생할 수 있다.
    - 참조 불가능
        - 구조체는 상속을 지원하지 않고 참조 타입으로 동작하지 않기 때문에, 클래스의 다양한 기능을 활용할 수 없다.
