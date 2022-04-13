# mutating 과 구조체

[Class && Struct && Enum 미완 enum추가](https://www.notion.so/Class-Struct-Enum-enum-326becc49f724b51bb0a13a9a9de1a25)

참고: [https://velog.io/@wook4506/iOS-Swift-Swift-문법을-알아보자-18편-mutating](https://velog.io/@wook4506/iOS-Swift-Swift-%EB%AC%B8%EB%B2%95%EC%9D%84-%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90-18%ED%8E%B8-mutating)

기존 글에서 클래스는 참조타입이고 구조체와 열거형은 값 타입이라고 정리를 했다.

그래서 값타입인 구조체에서는 인스턴스 메소드 내에서 프로퍼티들을 수정할 수 없게 되어있다.

때문에 이 프로퍼티들을 구조체 안에 있는 메소드에서 수정을 하려면 mutating이라는 키워드를 사용해야한다.

# mutating

특정 메소드 내에서 구조체 또는 열거형의 프로퍼티를 수정해야하는 경우, 해당 메소드의 동작을 변경하도록 하는 것

예시를 보면 Person이라는 구조체에서 init을 통해 초기화를 해주어서 완벽한 코드처럼 보이지만 에러가 발생한다.

```swift
struct Person {
    let name: String
    var age: Int

    init(name: String, age: Int) {
        self.name = name.uppercased()
        self.age = age
    }

    func changeAge() {
        age = 10       //에러! Cannot assign to property: 'self' is immutable
    }
}
```

위 에러는 바로 값타입인 구조체에서 메소드안의 값을 수정할 수 없기때문에 발생하는 것이다.

changeAge() 메소드 앞에 mutating을 붙여서 수정을 해보면

man 인스턴스를 처음 init할 때에는 24를 넣었지만 changeAge()메소드를 통해 age가 10으로 바뀌었다.

```swift
struct Person {
    let name: String
    var age: Int

    init(name: String, age: Int) {
        self.name = name.uppercased()
        self.age = age
    }

    mutating func changeAge() {
        age = 10
    }
}

var man = Person(name: "Song", age: 24)
man.changeAge()
print(man.age)
```
