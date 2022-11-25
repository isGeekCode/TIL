# 타입프로퍼티(static) - 프로퍼티(3)

- [[참고: 애플문서]](https://docs.swift.org/swift-book/LanguageGuide/Properties.html)
- [[참고: Zedd’s Blog]](https://zeddios.tistory.com/251)



**프로퍼티 시리즈**

- [저장프로퍼티(feat.클래스와 구조체) - 프로퍼티(1)](https://www.notion.so/feat-1-f7bdd1442cc6485d81743f181ad6f16e)
- [연산프로퍼티(Getter/Setter) - 프로퍼티(2)](https://www.notion.so/Getter-Setter-2-f89ddb3673d54156b9cca5d1bd2ec65c)
- **[프로퍼티 옵저버(willSet / didSet) - 프로퍼티(2.5)](https://www.notion.so/willSet-didSet-2-5-886d6a17a23a47669ae7b9adde0e65dc)**


- **🍊 타입프로퍼티(static) - 프로퍼티(3)**

**타입프로퍼티란 타입자체와 연결한 프로퍼티를 말한다.**

타입프로퍼티도 저장 타입 프로퍼티와 연산 타입 프로퍼티가 있다.

- 저장 타입 프로퍼티(Stored type Property) - 변수 혹은 상수
- 연산 타입 프로퍼티(Computed type Property) - 항상 변수

그리고 저장 타입 프로퍼티는 반드시 초기값이 있어야하며, 처음 액세스할때에는 lazy를 사용한 것처럼 늦게 초기화된다. 다수의 thread에 의해 동시에 액세스 되고 있어도, 한번만 초기화되는 것이 보증되어있어서 lazy라는 ㅋ워드를 사용할 필요가 없다. 



### 타입프로퍼티 정리

- 타입프로퍼티란 타입자체에 연결된 프로퍼티를 말한다.
- 저장 타입 프로퍼티 / 연산 타입 프로퍼티가 있다.
- 저장 타입프로퍼티
    - 상수 / 변수일 수 있다.
    - 반드시 기본값을 줘야한다.
    - 첫 액세스시 lazy init한다. (lazy는 안붙여도 된다)
- 연산 타입 프로퍼티는
    - 반드시 변수여야 한다.
    



## 타입프로퍼티 사용법

static 키워드를 이용하여 정의한다. 

Apple 예제

```swift
// 구조체
struct SomeStructure {
    static var storedTypeProperty = "Some value."
    static var computedTypeProperty: Int {
        return 1
    }
}

// 열거형
enum SomeEnumeration {
    static var storedTypeProperty = "Some value."
    static var computedTypeProperty: Int {
        return 6
    }
}

// 클래스
class SomeClass {
    static var storedTypeProperty = "Some value."
    static var computedTypeProperty: Int {
        return 27
    }
    class var overrideableComputedTypeProperty: Int {
        return 107
    }
}
```



### 구조체

- 구조체의 저장타입프로퍼티는 저장인스턴스프로퍼티와 다르게 기본값을 줘야한다.
- 연산 타입 프로퍼티는 항상 변수여야한다.

```swift

struct SomeStructure {

        // 구조체 저장 타입 프로퍼티 -> 기본값이 있음
    static var storedTypeProperty = "Some value."

    // 구조체 연산 타입 프로퍼티 -> 반드시 변수
    static var computedTypeProperty: Int {
        return 1
    }
}

// 구조체 저장 프로퍼티 -> 기본값이 없음
struct FixedLengthRange 
    var firstValue: Int
    let length: Int
}

var rangeOfThreeItems = FixedLengthRange(firstValue: 0, length: 3)

rangeOfThreeItems.firstValue = 6
rangeOfThreeItems.length = 10//error!
```



### 열거형

클래스와 구조체에서만 쓰였던 저장 (인스턴스)프로퍼티와 달리 열거형에서 사용가능하다. 

```swift

enum SomeEnumeration {

    // 열거형 저장 타입 프로퍼티 -> 기본값이 있음
    static var storedTypeProperty = "Some value."

        // 열거형 연산 프로퍼티 - 반드시 변수
    static var computedTypeProperty: Int {
        return 6
    }
}
```



### 클래스

클래스에서도 동일하게 저장 타입 프로퍼티와 연산 타입프로퍼티를 사용할 수있다.

- 특별하게 class 타입에 대한 연산 타입프로퍼티의 경우,
    - class키워드를 이용하여 서브클래스가 슈퍼클래스의 구현을 override할 수 있다.

```swift
class SomeClass {

    static var storedTypeProperty = "Some value."
    static var computedTypeProperty: Int {
        return 27
    }

    class var overrideableComputedTypeProperty: Int {
        return 10
    }
}
```

 overrideableComputedTypeProperty는 class키워드가 붙어있기 때문에 연산 타입 프로퍼티이다. 

현재 선언되어있는 SomeClass를 상속받은 클래스는 “class”키워드가 붙은 저 overrideableComputedTypeProperty라는 연산 타입 프로퍼티를 재정의 할 수 있다.

```swift
class ChildSomeClass : SomeClass{

    override static var overrideableComputedTypeProperty: Int{

       return 2222
    }

}
```

재정의를 하기 때문에 앞부분엔 override키워드가 붙어야한다. 



## 타입프로퍼티 접근방법

보통 인스턴스프로퍼티의 경우는 아래 코드처럼 구조체 / 열거형 / 클래스 인스턴스를 하나 생성하고 그 인스턴스들을 통해 프로퍼티에 접근을 했다.

```swift
struct FixedLengthRange {

    var firstValue: Int
    let length: Int
}

// 인스턴스 생성
var rangeOfThreeItems = FixedLengthRange(firstValue: 0, length: 3)

rangeOfThreeItems.firstValue = 6
```

하지만 타입프로퍼티의 경우는 인스턴스가 아닌 타입자체의 이름을 치고 접근한다.

```swift

class ChildSomeClass : SomeClass{

    static var storedTypeProperty = "Some value."
    static var computedTypeProperty: Int {
        return 27
    }
    override static var overrideableComputedTypeProperty: Int{

       return 2222
    }

}

SomeStructure.storedTypeProperty = "Another value."
print(SomeStructure.storedTypeProperty)
print(SomeEnumeration.computedTypeProperty
print(SomeClass.computedTypeProperty)              
```
