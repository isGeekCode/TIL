# 연산프로퍼티 - 프로퍼티(2)

- [[참고: 애플문서]](https://docs.swift.org/swift-book/LanguageGuide/Properties.html)
- [[참고: Zedd’s Blog]](https://zeddios.tistory.com/245)

**프로퍼티 시리즈**

- [저장프로퍼티(feat.클래스와 구조체) - 프로퍼티(1)](https://github.com/isGeekCode/TIL/blob/main/iOS-Framework-Swift/aboutProperty1.md)
- **🍊 연산프로퍼티(Getter/Setter) - 프로퍼티(2)**
- [프로퍼티 옵저버(willSet / didSet) - 프로퍼티(2.5)](https://github.com/isGeekCode/TIL/blob/main/iOS-Framework-Swift/aboutProperty205.md)
- [타입프로퍼티(static) - 프로퍼티(3)](https://github.com/isGeekCode/TIL/blob/main/iOS-Framework-Swift/aboutProperty3.md)

Property는 저장프로퍼티와 연산프로퍼티, 타입프로퍼티 가 있다.

이제 설명할 내용은 그중 연산프로퍼티다.

저장프로퍼티는 상수와 변수값을 인스턴스의 일부에 저장한다. 클래스와 구조체에서만 사용된다.

반면 연산프로퍼티는 값을 저장하기보다는 특정연산을 수행하여 값을 반환한다. 클래스와 구조체, 열거형에서 사용된다.

클래스, 구조체, 열거형 (Class, Struct, Enum)에서 연산프로퍼티를 정의할 때는 Getter와 Setter를 통해 다른 프로퍼티의 값을 검색하고 세팅한다.

이 때, Getter와 Setter가 연산프로퍼티다.

# Getter / Setter

### 사용법

이렇게 선언하는 경우 전혀 문제가 생기지 않는다

```swift
var myProperty: Int

myProperty = 3
print(myProperty)
/// 3
```

아래와 같이 선언하면 무한 재귀가 생긴다.

무한재귀란 자신의 로직안에 자신을 호출하게 되면 끝없이 자신을 호출하는 일이 생기는 것을 말한다.

- get: 해당 변수에 접근할 때, 사용한다.
- set: 해당 변수에 값을 할당할 때, 사용한다.
  **단, 자기 자신을 부여하게 되면 무한재귀가 생겨나기 때문에 자신을 부여하면 안된다.**

```swift
var myProperty: Int{

    get {
				print("get에서 접근")
        return myProperty
    }

    set(newValue) {
				print("set에서 접근")
        myProperty = newValue      /// ( 15392 times )
    }
}

myProperty = 3
print(myProperty)
// get에서 접근
// 3
```

### Getter와 Setter를 사용하려면 저장프로퍼티가 필요하다.

위와 같은 이유로 무한재귀가 생기지 않도록 따로 저장공간을 만들어야한다. `**_myProperty**`

그리고 myProperty는 자신을 사용하는 것이 아니라, 새로만든 저장공간에 get, set하는 동작을 해야한다.

myProperty는 일종의 인터페이스 역할을 하는 것이다. 또한 연산프로퍼티는 반드시 변수로 생성해야한다.

- 저장프로퍼티를 생성해야한다.
- 연산프로퍼티는 변수로 생성해야한다.

```swift
var _myProperty: Int = 5      // 저장공간
var myProperty: Int {
    get {
        return _myProperty
    }

    set(newValue) {
        _myProperty = newValue
        print(_myProperty)
    }
}

myProperty = 2
print(myProperty)        /// 3
```

### newValue

Setter는 파라미터를 받아서 리턴을 하게 되어있다. set(newValue)이 기본값인데, 파라미터명을 변경하여 사용할 수도 있다.

```swift
set(newValue) {
	_myProperty = newValue
}

set(newNumber) {
	_myProperty = newNumber
}
```

괄호대신 set만 사용할 수 있는데, 이때는 반드시 newValue라는 파라미터명을 사용해야한다.

```swift
var _myProperty: Int = 5      // 저장공간
var myProperty: Int {
    get {
        return _myProperty
    }

    set {
        _myProperty = newValue
        print(_myProperty)
    }
}
```

### 유효성 검사

아래와 같이 set안에 if를 이용해서 유효성을 검사한다음 값을 부여할 수도 있다.

```swift
var _myProperty: Int = 5
var myProperty: Int {
    get {
        print("get에서 접근")
        return _myProperty
    }

    set {
        print("set에서 접근")

        if newValue < 3 {
            print("3보다 작을 수 없다")
        } else {
            _myProperty = newValue
        }
        print(_myProperty)
    }
}

myProperty = 2       // 3보다 작을 수 없다
print(myProperty)    // 5

myProperty = 4       // 3보다 작을 수 없다
print(myProperty)    // 4

```

### 의존적인 프로퍼티

외부에서는 apple로만 접근을 하게된다. 그리고 totalCost는 apple에 할당한 (정확히는 저장소인 appleCount)**********************************\*\***********************************에**********************************\*\*********************************** 할당된 갯수에 1000을 곱한 값을 가져온다. totalCost는 appleCount에 의존적인 프로퍼티다.

```swift
import UIKit

class FruitShop {
    var appleCount: Int = 3
    var apple: Int {
        get {
            print("get에서 접근")
            return appleCount
        }

        set {
            print("set에서 접근")

            if newValue < 3 {
                print("3보다 작을 수 없다")
            } else {

                appleCount = newValue
            }
            print(appleCount)
        }
    }

    var totalCost: Int {
        get {
            return appleCount * 1000
        }
    }
}

class ViewController: UIViewController {

    var someFruitShop = FruitShop()

    override func viewDidLoad() {
        super.viewDidLoad()

        someFruitShop.apple = 5
        print(someFruitShop.apple)             // 5
        print("\(someFruitShop.totalCost)원")   // 5000원

        someFruitShop.apple = 2           // 3보다 작을 수 없다
        print(someFruitShop.apple)        // 3
    }
}
```

이 경우에 아래와 같이 `**get**`만 구현된 `**someFruitShop.totalCost**`를 직접 부여하면 에러가 발생하기 때문에 사용할 수 없다.

```swift
// MARK: ERROR!!
someFruitShop.totalCost = 400
/// Cannot assign to property: 'totalCost' is a get-only property
```
