# Swift - Initialization에 대해 알아보기


## 초기화에 대하여 
초기화(Initialization)는 클래스, 구조체 또는 열거형을 사용하기 위한 준비하는 과정. 각각의 저장 속성을 위해 초기화된 값을 설정하는 것과 사용하기 위한 새로운 인스턴스를 준비하기전에 필요한 그외 다른 설정 또는 초기화를 진행함.

특히! 클래스는 무조건 init을 해주어야한다. 구조체는 기본적으로 저장프로퍼티들을 파라미터로 가지는 이니셜라이저가 있다.

### 이니셜라이저(Initializers)

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

### 초기화의 종류

- Designated init
- Convinience init

### 초기화의 목적 

1. 모든 멤버 초기화
2. 상속받은 멤버들 customizing


<br><br><br>

## 클래스 초기화 예시

### class 초기화(1): 파라미터가 없는 경우

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

init에 아무 파라미터를 주지 않고, 직접 프로퍼티에 값을 줄 수 있다.  

이 방법은 모든 클래스 인스턴스가 같은 프로퍼티 값을 가질 때 유용하다.  

<br><br>

### class 초기화(2): 파라미터가 있는 경우

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

init에 파라미터를 넣어 초기화 하는 방법이다.  

이방법을 쓰면, 넘겨주는 String에 따라서 text 값이 달라지는 클래스 인스턴스가 생긴다.  

<br><br>

### class 초기화(3): 파라미터 변수명을 다르게 생성하는 경우

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

init 또한 메서드이기 때문에 파라미터명을 마음대로 설정할 수 있다.  

파라미터가 다르면 메서드 이름이 동일해도 다른 메서드 취급을 받는다.  

때문에 여러 종류의 init을 생성할 수 있다.  

<br><br>

### 클래스 초기화(4): 파라미터에 와일드카드 패턴을 사용하는 경우

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

init()안에 `_`라는 와일드카드 패턴을 사용하면 파라미터명을 생략할 수 있다.   

> 파라미터 이름을 넘겨주지 않아도 되는 init이 두개인경우, 에러가 발생한다.
> 타입이 다른경우에는 다른 init으로 인정하여 잘 작동한다.

<br><br>

## Init할때 옵셔널 타입 변수가 있는 경우

### 클래스 초기화(5): 옵셔널 타입 변수를 init의 파라미터로 포함하지 않는 경우

response라는 클래스 프로퍼티가 있다.  

원래 init메서드에는 모든 클래스 프로퍼티를 초기화 해야만 한다.  

하지만 response는 옵셔널 타입이기 때문에 오류가 나지 않는다.  

<br>

```swift
class SurveyQuestion {
    var text: String
    var response: String?
    
    init(text: String) {
        self.text = text
    }
}
var question = SurveyQuestion(text: "GeekCode")
print(question.text)// "GeekCode"
print(question.response) // nil
```

이렇게 옵셔널타입인 프로퍼티는 클래스 인스턴스가 만들어질 때, nil로 초기화된다.

그렇기 때문에 위와 같이 옵셔널 타입을 제외한 init이 가능하다.

<br>

### 클래스 초기화(6): 옵셔널 타입 변수를 init의 파라미터로 포함하는 경우

클래스 변수는 옵셔널로 되어있지만 init 메서드의 파라미터는 옵셔널로 되어있지않은 경우이다. 

```swift
class SurveyQuestion {
   var text: String
   var response: String?
   
   init(text: String, response: String) {
        self.text = text
        self.response = response
   }
}
```

아래 세가지 경우가 있다. 

- 첫번째: 이미 생성한 인스턴스의 옵셔널 변수에 nil 선언이 될까?
- 두번째: 인스턴스를 생성할 때 옵셔널 변수자리에 파라미터로 nil 선언이 될까?(1)
- 세번째: 인스턴스를 생성할 때 옵셔널 변수자리에 파라미터로 nil 선언이 될까?(2)


<br>

- 첫번째: 이미 생성한 인스턴스의 옵셔널 변수에 nil 선언이 될까?

> 된다 : response가 옵셔널 타입이기때문에 부여할 수 있다.


```swift

class SurveyQuestion {
   var text: String
   var response: String?
   
   init(text: String, response: String) {
        self.text = text
        self.response = response
   }
}

var a = SurveyQuestion(text: "hello", response: "Good day")

a.response = nil    // 가능하다!!

print(a.text)       // hello
print(a.response)   // nil
```


- 두번째: 인스턴스를 생성할 때 옵셔널 변수자리에 파라미터로 nil 선언이 될까?(1)

> 안된다 : init메서드는 String? 이 아니라 String로 구현되어있다.

```swift
class SurveyQuestion {
   var text: String
   var response: String?
   
   init(text: String, response: String) {
        self.text = text
        self.response = response
   }
}

var b = SurveyQuestion(text: "bye", response: nil)  // ERROR!!!!
```


- 세번째: 인스턴스를 생성할 때 옵셔널 변수자리에 파라미터로 nil 선언이 될까?(2)

이번엔 init메서드의 파라미터로 옵셔널이 들어가 있다.  

> 된다 : init메서드의 파라미터가 옵셔널일땐 init할때 nil을 넣어줄 수 있다.

```swift
class SurveyQuestion {
    var text: String
     var response: String?
     
    init(text: String, response: String?) {
        self.text = text
        self.response = response
    }
}

var a = SurveyQuestion(text: "hello", response: nil) // 가능
print(a.text)           // hello
print(a.response)       // nil

a.response = "GeekCode"
print(a.text)           // hello
print(a.response)       // Optional("GeekCode")
```

## Designated initializer → 지정 초기자

- init으로 표현
- 클래스의 모든 프로퍼티를 초기화 해야함
- 클래스 타입은 반드시 한개 이상의 지정 초기자가 필요

```swift
init(parameters) {
    statements
}
```

## Convenience initializer (편의 초기자)

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



## History
- 220316: 초안작성
- 230817: 케이스별 정리
