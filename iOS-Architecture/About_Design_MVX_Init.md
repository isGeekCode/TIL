# 디자인패턴이란

**"디자인 패턴은 소프트웨어를 개발할 때 발생하는 다양한 문제에 대한 재사용 가능한 템플릿 해결방법!"**

 즉, 어떤 실질적인 코드가 아닌 아이디어라고 할 수 있다.

- 패턴 이름
    - 해결할 문제, 해결 방법, 결과를 설명, 해당 디자인을 설명하고 공유하기 편하기 때문
- 해결할 문제
    - 해당 패턴이 어떤 문제를 해결할 때 사용할 것인지
- 해결 방법
    - 디자인 패턴은 다양한 상황에 적용될 수 있는 템플릿과 같기 때문에 해결 방법은 특정 디자인이나 구현을 설명하지는 않고, 추상적인 설명과 요소를 제공하여 해결 방법을 제시
- 결과
    - 소프트웨어에서는 동일한 기능을 구현할 때 메모리, 속도 등을 비교하여 어느 코드가 더 나은 성능을 보이는지 비교할 수 있다. 또한 디자인 패턴을 사용하는 이유인 재사용성도 평가 항목에 포함된다.


## 디자인패턴의 종류

### 목적

패턴이 무엇을 하는지 정의하는 것으로 "생성", "구조", "행위" 중의 한 가지 목적을 갖는다.

1. **구조 디자인 패턴 (Structural Design Pattern)**
    
    → 클래스나 객체의 구성을 통해 더 큰 구조로 만들 수 있게 해주는 것과 관련된 패턴
    
    ex) MVC, MVVM
    
2. **행위 디자인 패턴 (Behavioral Design Pattern)** 
    
    → 패턴을 주로 클래스에 적용하는지 아니면 객체에 적용하는지에 따라 구분되는 패턴
    
    ex) Delegation, Observer
    
3. **생성 디자인 패턴 (Creational Design Pattern)** 
    
    → 객체의 생성과정에 관여하는 패턴
    
    ex) Singleton, Prototype

## 디자인패턴의 장단점

### 장점

- 개발자의 시간을 아껴주고 불필요한 작업방지
- 프로그램 시작시, 구체화하는데 최초 시작점이 된다.
- 디자인패턴은 개발자들의 언어 → 소통시 디자인패턴기반 의사소통
- 코드간의 반복성을 찾기 쉽도록 구현

### 단점

- 남용하면 프로젝트가 지나치게 복잡해질 수 있다. → 디자인패턴을 추가하기전에 문제를 정확히 정의해서 예방
- 디자인패턴을 많이 안다고 중요한 것이 아니다.

참고: [https://www.raywenderlich.com/books/design-patterns-by-tutorials/v3.0/chapters/1-what-are-design-patterns](https://www.raywenderlich.com/books/design-patterns-by-tutorials/v3.0/chapters/1-what-are-design-patterns)

### 여러 디자인 패턴들

- 싱글턴 패턴 (Singleton Pattern)목적 : 생성범위 : 객체객체의 생성에 관련된 패턴으로서 특정 클래스의 인스턴스가 오직 하나임을 보장하고 이 인스턴스에 접근할 방법을 제공합니다.
- 퍼사드 패턴 (Facade Pattern)목적 : 구조범위 : 객체건물의 정문에 있는 안내소처럼 개발자가 사용해야 하는 서브 시스템의 가장 앞쪽에 위치하면서 하위 시스템에 있는 객체들을 사용할 수 있도록 하는 역할을 합니다. 시스템의 복잡성을 줄이기 위해 서브 시스템을 구조화하고 서브 시스템으로의 접근을 하나의 퍼사드 객체로 제공하는 패턴입니다.
- 옵저버 패턴 (Observer Pattern)목적 : 행위범위 : 객체객체의 상태변화를 관찰하는 관찰자들, 즉 옵저버들의 목록을 객체에 등록하여 상태 변화가 있을 때마다 메서드 등을 통해 객체가 직접 목록의 각 옵저버에게 통지하도록 하는 패턴입니다.
- 스트래티지 패턴 (Strategy Pattern)목적 : 행위범위 : 객체알고리즘을 담당하는 각각의 클래스를 만들어 책임을 분산하기 위한 목적으로 만든 행위 패턴입니다.
- 팩토리 패턴 (Factory Pattern)목적 : 생성범위 : 클래스객체를 생성하기 위한 인터페이스를 정의하지만 어떤 클래스의 인스턴스를 생성할지에 대한 결정은 하위 클래스에서 이루어지도록 인스턴스 생성의 책임을 떠넘기는 패턴입니다.
- 어댑터 패턴 (Adapter Pattern)목적 : 구조범위 : 클래스, 객체클래스의 인터페이스를 사용자가 기대하는 다른 인터페이스로 변환하는 패턴으로, 호환성이 없는 인터페이스 때문에 함께 동작할 수 없는 클래스들이 함께 동작하도록 해줍니다.

## -**싱글턴 패턴 → iOS 애플리케이션의 다양한 곳에 사용되고 있다.**

- 앱 전체에 하나 존재하는 UIApplication 객체
- 파일 접근을 돕는 FileManager
- 알림 센터 NotificationCenter 객체
- 데이터 지속성이 필요한 정보(앱 내 설정) UserDefaults 객체
- 네트워크 통신을 위한 URLSession 객체

## MVC패턴

Model / View / Controller로 나누는 패턴.

iOS 에서는 ViewController가 있는데, 규모가 큰 프로젝트에서는 이 VC가 점점 커지고 무거워지면서

**Massive ViewController**라는 별명을 가지고 있기도한 패턴이다.

![MVCimage](https://www.notion.so/nylonguitarist/MVC-MVVM-18748ba883a8443d9affa4054bc0b24e#b981741212c04ab5a9f18619b3de6cea)
![AppleMVC](https://www.notion.so/nylonguitarist/MVC-MVVM-18748ba883a8443d9affa4054bc0b24e#c8ee15317ecf4ecb8170f489afa468f8)  
Model에서는 애플리케이션에서 사용할 데이터들을 관리, 

View는 유저 인터페이스를 표현 및 관리.  → 사용자에게 보여주고 , 사용자가 조작할 수 있게 함.

Controller는 View와 Model의 다리 역할을 해 View의 입력을 Model이 반영하고, Model의 변화를 View에 갱신하는 역할을 한다. 

하지만, 애플의 MVC 패턴은 기존 MVC 패턴과 다르다. View와 Controller가 강하게 연결되어 있어 View Controller가 거의 모든 일을 한다.

## MVVM 패턴

MVVM 패턴은 Model / View / ViewModel로 이루어져있는 패턴이다.

### **기능**

- Model은 데이터 구조체가 들어간다.
    
    → 데이터의 형상 그자체
    
- View는 MVC패턴에서 ViewController의 View에 해당하는 부분
    
    → 보여주는 것을 담당
    
- ViewModel은 MVC패턴에서 ViewController의 로직에 해당하는 부분이 들어간다.
    
    → 보여주기위한 데이터를 관리
    

MVC에서 Controller를 빼고 ViewModel을 추가한 패턴.  여기서 View Controller가 View가 되고, ViewModel이 중간 역할을 한다.  

View와 ViewModel 사이에 Binding(바인딩-연결고리)가 있다. ViewModel은 Model에 변화를 주고, 

ViewModel을 업데이트하는데 이 바인딩으로 인해 View도 업데이트를 한다. 

ViewModel은 View에 대해 아무것도 모르기 때문에 테스트가 쉽고 바인딩으로 인해 코드 양을 줄일 수 있다.  

![MVVM](https://www.notion.so/nylonguitarist/MVC-MVVM-18748ba883a8443d9affa4054bc0b24e#8f4b55cf53af48b5998075ad2c499e79)

### 과정

1. 사용자가 화면에서 Action을 취하면 Command Pattern으로 View → ViewModel로 전달됩니다.
2. ViewModel 이 Model에게 data를 요청합니다.
3. Model은 요청받은 data를 통해 update된 data를 ViewModel로 전달합니다.
4. ViewModel은 응답받은 데이터를 가공해서 저장합니다.
5. View는 ViewModel과의 Data Binding을 통해서 자동으로 갱신됩니다.

**여기서 Command Pattern 이란 ?**

"Command = 명령어"실행될 기능을 추상화, 캡슐화하여 한 클래스에서 여러 기능을 실행할 수 있도록 하는 패턴입니다.

**여기서 Data Binding 이란 ?**

view와 로직이 분리되어 있어도 한 쪽이 바뀌면 다른 쪽도 업데이트가 이루어 지는 것입니다.

iOS 에서 Data Binding을 하는 방법에는 이런 것들이 있습니다.

- KVO
- Delegation
- Functional Reactive Programming
- Property Observer

### -MVVM의 장점

1. 유지보수에 좋다.
2. 자동화된 테스팅에 적합한 모델이다 ( View Model과 View 간의 의존성이 없기 때문에 )
3. 새로운 개발자라도 빠르게 적응이 가능하고 개발이 가능한 수준의 난이도와 복잡성

### 단점 → 단순한 프로젝트를 개발하기에는 MVC에 비해서는 긴코드를 작성해야한다.

## 실무에서는!!

회사에서 사용하는 모든 코드들은 이후에 새로운 기능이 추가될 확률이 굉장히 높고, 유지보수 및 테스트가 용이해야하기 때문에 많은 회사들이 MVVM 패턴을 채택하는 경향이 있다.

그렇기 때문에 MVC가 어느정도 익숙해졌고, 새로운 패턴을 적용을 하기위해서는 MVVM은 필수로 익혀야할 것



---  

# **Initializer**

### 클래스의 정의

클래스는 class라는 키워드를 사용한다

```swift
class Person {
    var name: String = ""
}
```

클래스는 상속받을 수 있다

클래스 이름 뒤에 콜론(:)을 써주고 부모 클래스 이름을 쓰면 됩니다

```swift
var personVar: Person = Person()
personVar.name = "현석"

let personLet: Person = Person()
personVar.name = "현석"
```

구조체와 다르게 클래스의 인스턴스는 참조 타입이므로 클래스의 인스턴스 상수 let으로 선언해도 내부 프로퍼티 값을 변경할 수 있다

구조체는 프로퍼티에 맞는 이니셜라이저를 제공하지만

클래스는 그렇지 않아서 클래스 인스턴스의 저장 프로퍼티를 초기화해야 합니다

클래스 인스턴스는 참조 타입이므로 참조할 필요가 없을 때 메모리에서 해제된다

이 과정을 **소멸**이라고 하는데 소멸되기 직전 `deinit`라는 메서드가 호출된다

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


## 🌐 Struct 예시)

우리가 자주사용하는 Int, Double, String의 정의부분

구조체는 struct 키워드로 정의한다.

```swift
public struct Int : SignedInteger, Comparable, Equatable

public struct Double

public struct String
```

이런 데이터 타입들은 구조체로 구현

구조체에서는 상속X, 프로토콜이 존재 →  `SignedInteger`, `Comparable`, `Equatable`

```swift
struct User {
var id: String
var level: Int
}
```

User라는 구조체. 이 구조체는 String 타입의 id와 Int 타입의 level이라는 저장 프로퍼티가 있다.

그럼 이제 User라는 구조체의 인스턴스 생성 및 사용을 하자.

```swift
var userVar: User = User(id: "hyeon", level: 100)
userVar.id = "hyeon"  // 변경 가능
userVar.level = 201    // 변경 가능

let userLet: User = User(id: "hyeon", level: 100)
userLet.id = "hyeon"  // 변경 불가! 오류!
userLet.level = 202    // 변경 불가!
모든 구조체는 초기화 시 프로퍼티를 선언할 수 있는 이니셜라이저를 자동으로 생성해 제공합니다
```

**위에 만든 User처럼 id와 level 프로퍼티만 정의하면 자동으로 사용 가능**

인스턴스가 생성되고 초기화된 후 마침표(.)을 사용하여 프로퍼티 값에 접근할 수 있다

구조체를 상수 let으로 선언하면 인스턴스 내부의 프로퍼티 값을 변경할 수 없다.




# 초기화 Initialization

초기화는 클래스, 구조체 또는 열거형을 사용하기 위한 준비하는 과정. 각각의 저장 속성을 위해 초기화된 값을 설정하는 것과 사용하기 위한 새로운 인스턴스를 준비하기전에 필요한 그외 다른 설정 또는 초기화를 진행함.

특히! 클래스는 무조건 init을 해주어야한다. 구조체는 기본적으로 저장프로퍼티들을 파라미터로 가지는 이니셜라이저가 있다.

****이니셜라이저(Initializers)****

이니셜라이저는 특정 타입의 새로운 인스턴스를 만들기 위해 호출하며, 인자가 없는 인스턴스 메소드와 유사한 형식으로 `init` 키워드를 사용한다.

```swift
init() {
    // perform some initialization here
}
```

아래는 Fahrenheit라는 새로운 구조체로 화씨 크기를 표현하는 온도를 저장한다. Fahrenheit 구조체는 Double 타입의 temperature 저장 속성을 가진다.

```swift
struct Fahrenheit {
    var temperature: Double
    init() {
        temperature = 32.0
    }
}
var f = Fahrenheit()
println("The default temperature is \(f.temperature)° Fahrenheit")
// prints "The default temperature is 32.0° Fahrenheit"
```

이 구조체는 인자를 가지지 않는 단일 이니셜라이저 `init`으로 정의하며 32.0 값으로 이니셜라이저가 temperature에 저장한다.

초기화의 종류

- Designated init
- Convinience init

초기화의 목적 

1. 모든 멤버 초기화
2. 상속받은 멤버들 customizing

### 클래스 초기화 예시

### 1. class 초기화 -1

```swift
class SurveyQuestion{
    var text: String
    init(){
        self.text = "hello"
    }
}
var question = SurveyQuestion()
print(question.text)//"hello"
```

init에 아무 파라미터를 안주고 직접 프로퍼티에 값을 줄 수 있다. 이 방법은 모든 클래스 인스턴스가 같은 프로퍼티 값을 가질 때 유용함.

### **2. class 초기화 -2**

```swift
class SurveyQuestion {

    var text: String
    init(text: String) {
        self.text = text
    }
}
var question = SurveyQuestion(text: "hello")
print(question.text)//"hello"
```

init에 파라미터를 넣어 초기화 하는 방법. 이방법을 쓰면, 넘겨주는 String에 따라서 text프로퍼티의 값이 다른 클래스 인스턴스가 생긴다.

### **3. class 초기화 - 3 이름이 같아도 파라미터가 다르다면!!**

```swift
class SurveyQuestion {

    var text: String
    init(text: String) {
        self.text = text
    }
    init(questionText: String) {
        self.text = questionText
    }
}

var question = SurveyQuestion(text: "hello")
print(question.text)//"hello"

var cheeseQuestion = SurveyQuestion(questionText: "Do you like cheese?")
print(cheeseQuestion.text)//"Do you like cheese?"
```

파라미터의 이름이 다르다. 그럼 똑같은 init이지만 해당 파라미터 이름이 있는 곳으로 알아서 입력된다.

### 클래스 초기화-4. 파라미터에 와일드카드 패턴사용할 때

```swift
class SurveyQuestion{

    var text: String
    init(text: String) {
        self.text = text
    }

    init(questionText: String) {
        self.text = questionText
    }

    init(_ questionList: String) {
        self.text = questionList
    }
}

var question = SurveyQuestion(text: "hello")
print(question.text)//"hello"

var cheeseQuestion = SurveyQuestion(questionText: "Do you like cheese?")
print(cheeseQuestion.text)//"Do you like cheese?"

var questionList = SurveyQuestion("Health")
//init에 _ 이 있기 때문에 파라미터 이름을 안넣어도 된다. 또한, 자기에 맞는 init이 무엇인지 알아서 찾아간다. 
print(questionList.text)//"Health"

```

 init()안에 _ 를 해주고 파라미터 이름을 써줬죠? 이건 이 메소드를 부를 때, 파라미터 이름을 생략해도 된다는 것을 의미한다. 그래서 저렇게 바로 "Health"를 넣어줄 수 있다.

**하지만, 파라미터 이름을 넘겨주지 않아도 되는 init이 두개인경우, 에러가 발생**

→ 타입이 다른경우에는 다른 init으로 인정하여 잘 작동함.

### 옵셔널 타입은 init이 없어도된다.

```swift
class SurveyQuestion {
    var text: String
    var response: String?
    init(text: String) {
        self.text = text
    }
}
```

분명히 response라는 클래스 프로퍼티가 있지만, 모든 클래스 프로퍼티를 초기화 해야만 하는 init에 넣어주지 않아도  response는 옵셔널 타입이기 때문이죠. 오류가 나지 않는다.

```swift
class SurveyQuestion {
    var text: String
     var response: **String?**
    init(text: String) {
        self.text = text
    }
}
var question = SurveyQuestion(text: "zedd")
print(question.text)//"zedd"
**print(question.response)//nil**
```

이렇게 옵셔널타입인 프로퍼티는 클래스 인스턴스가 만들어질 때, nil로 초기화된다.

그렇기 때문에 아래와 같이 옵셔널 타입을 제외한 init이 가능하다.

```swift
class SurveyQuestion {
   var text: String
   var response: **String?**
   init(text: String, response: String) {
        self.text = text
        self.response = response
   }
}
```

Q. response는 옵셔널 타입인데, 왜 init할때는 String?을 넘겨주지 않고 String을 넘겨줄까?

```swift
// 1. 변수가 옵셔널인경우

class SurveyQuestion {
   var text: String
   var response: String?
   init(text: String, response: **String**) {
        self.text = text
        self.response = response
   }
}
// response에 nil 부여 //가능
var a = SurveyQuestion(text: "hello", response: "Good day")
a.response = nil //가능 -> response가 옵셔널 타입이기때문!

// init파라미터에 nil 부여 **//error!**
var b = SurveyQuestion(text: "bye", **response: nil)
// -> init은 String?이 아니라 String으로 받기때문.**

// 2.
class SurveyQuestion {
    var text: String
     var response: String?
    init(text: String, response: **String?**) {
        self.text = text
        self.response = response
    }
}
var a = SurveyQuestion(text: "hello", **response: nil) //가능**
a.response = nil //가능 response가 옵셔널 타입이기때문!
```

### Designated initializer → 지정 초기자

- init으로 표현
- 클래스의 모든 프로퍼티를 초기화 해야함
- 클래스 타입은 반드시 한개 이상의 지정 초기자가 필요

```swift
init(parameters) {
    statements
}
```

# #Convenience initializer (편의 초기자)

- 옵셔널
- Designated init의 파라미터 중 일부를 기본값으로해서 이 Convenience init안에서 Designated init을 호출하여 초기화를 진행 할 수 있다.
- Convenience init을 사용하려면 designated init이 먼저 선언되어야한다.
- ※ convenience가 아닌 init키워드는 블록안에 self.init과 같이 다른 초기화 메소드를 부를 수 없음

```swift
class Person {
    var name: String
    var age: Int
    var gender: String

    init(name: String, age: Int, gender: String) {
        self.name = name
        self.age = age
        self.gender = gender
    }

    convenience init(age: Int, gender: String) {
        self.init(name: "hyeon", age: age, gender: gender)
    }
}

```
