# 저장프로퍼티 - 프로퍼티(1)

- [[참고: 애플문서]](https://docs.swift.org/swift-book/LanguageGuide/Properties.html)
- [[참고: Zedd’s Blog]](https://zeddios.tistory.com/243)

**프로퍼티 시리즈**

- **🍊  저장프로퍼티(feat.클래스와 구조체) - 프로퍼티(1)**
- [연산프로퍼티(Getter/Setter) - 프로퍼티(2)](https://www.notion.so/Getter-Setter-2-f89ddb3673d54156b9cca5d1bd2ec65c)
- **[프로퍼티 옵저버(willSet / didSet) - 프로퍼티(2.5)](https://www.notion.so/willSet-didSet-2-5-886d6a17a23a47669ae7b9adde0e65dc)**
- [타입프로퍼티(static) - 프로퍼티(3)](https://www.notion.so/static-3-d0f7852984df40029ba6994dec0eb5a1)

Property는 저장프로퍼티와 연산프로퍼티, 타입프로퍼티 가 있다.

클래스나 구조체는 이 저장프로퍼티, 연산프로퍼티로 이루어지는 것이다.

연산프로퍼티는 열거형에서도 사용된다. 

이제 설명할 내용은 그중 저장프로퍼티다.

# Stored Property

저장프로퍼티는 클래스와 구조체에서만 사용된다.

저장프로퍼티를 선언할 때는 저장할 기본값을 줄 수 있고, 이후 수정할 수 있다.

이때 사용되는 것이 변수와 상수이다. 

 `var`로 선언하면 변수가 저장되고, `let`으로 선언하면 상수가 저장된다. 

## 구조체

Apple 예제

```swift
struct FixedLengthRange {
    var firstValue: Int    // 변수 저장 프로퍼티
    let length: Int        // 상수 저장 프로퍼티
}
var rangeOfThreeItems = FixedLengthRange(firstValue: 0, length: 3)
rangeOfThreeItems.firstValue = 6   // 6
rangeOfThreeItems.length = 8       // ERROR!!!!
```

위 코드는 구조체이다.

FixedLengthRange안에 있는  `firstValue`와  `length`가  **저장프로퍼티** 다.  

초기값은 주지 않은 상태이다. 

### 인스턴스 생성

아래코드를 통해 `**var**`로 `FixedLengthRange`의 인스턴스를 하나 만들었다.

`var rangeOfThreeItems = FixedLengthRange(firstValue: 0, length: 3)`

### 구조체는 간편하게 이니셜이 가능하다.

구조체는 클래스와 달리 기본적으로 저장프로퍼티들을 파라미터로 가지는 이니셜라이저가 있다. 

때문에 **초깃값이 있는 경우**에는 `**FixedLengthRange()**` 로 선언해도 무방하다. 

위처럼 firstValue를 0, length3 으로 선언했기때문에

생성한 rangeOfThreeItems.firstValue 로 접근이 가능하다. 

하지만 var로 선언한 firstValue는 새롭게 값을 할당가능하지만, length는 let으로 선언했기때문에 length에 접근하여 값을 할당하면 에러가 발생한다. 

```swift
rangeOfThreeItems.firstValue = 6   // 6
rangeOfThreeItems.length = 8       // ERROR!!!!
```

위의 경우는 `FixedLengthRange`를 var로 생성했기때문에 가능했다. 만약 아래경우라면  firstValue도 length도 수정할 수 없다. 

```swift
struct FixedLengthRange {
    var firstValue: Int    // 변수 저장 프로퍼티
    let length: Int        // 상수 저장 프로퍼티
}
let rangeOfThreeItems = FixedLengthRange(firstValue: 0, length: 3)

rangeOfThreeItems.firstValue = 6  // ERROR!!!!
rangeOfThreeItems.length = 8      // ERROR!!!!
```

rangeOfThreeItems 자체가 상수이기 떄문에 length가 변수였어도 에러가 발생한다. 

## 클래스

위 Apple 예제를 다시 클래스로 수정하면 아래와 같다. 

```swift
class FixedLengthRange {
    var firstValue: Int    // 변수 저장 프로퍼티
    let length: Int        // 상수 저장 프로퍼티

    init(firstValue: Int, length: Int) {
        self.firstValue = firstValue
        self.length = length
    {
}
var rangeOfThreeItems = FixedLengthRange(firstValue: 0, length: 3)
rangeOfThreeItems.firstValue = 6

rangeOfThreeItems.firstValue = 6   // 6
rangeOfThreeItems.length = 8       // ERROR!!!!
```

위 코드는 클래스다.

저장프로퍼티에 초기값이 없는 경우 클래스는 **반드시 init(이니셜라이저)이 필요하다.**

구조체와 마찬가지로 `**rangeOfThreeItems**`를 `**var**`로 생성했을때 , firstValue는 변경가능하고 length는 변경할 수 없다.

그런데 rangOfThreeItems를 let을 생성했을 때, 

firstValue를 변경하는데 에러가 발생하지않는다.

```swift
let rangeOfThreeItems = FixedLengthRange(firstValue: 0, length: 3)
rangeOfThreeItems.firstValue = 6

rangeOfThreeItems.firstValue = 6   // 6
rangeOfThreeItems.length = 8       // ERROR!!!!
```

### 클래스의 특징: 참조 (Reference)

구조체를 생성하면 별개의 복사본이 생성되지만 클래스는 원본에 접근을 한다. 즉, 클래스로 생성한 모든 것이 원본이다. 

그렇기 때문에 위의 경우에서 rangeOfThreeItems를 let으로 생성했지만 firstValue를 변경가능하다. 

하지만 length는 애초에 let으로 생성된 저장프로퍼티라 변경할 수 없다. 

# Lazy

Lazy는 말 그대로 게으르다는 것을 뜻한다. 아래와 같이 사용할 수 있는데, Lazy가 붙게 되면

이 프로퍼티를 사용하는 순간이 되서야 생성을 하게 된다. 쓸데없는 데이터 낭비를 줄이기 때문에 성능도 올라가고, 공간도 절약이 가능하다. 반드시 var에만 사용할 수 있다. let으로 선언하게 되면 초기화를 함과 동시에 값을 가져오기 떄문에, 값이 필요할 때 사용하는 lazy를 사용할 수 없다. 

```swift
// MARK: 1. 간단하게 생성
lazy var titleLabel = UILabel()

// MARK: 2. 설정을 추가하여 생성
lazy var titleLabel: UILabel = {
        let label = UILabel()
        label.font = .systemFont(ofSize: 16, weight: .bold)
        return label
    }()
```

위와 같이 사용한다.  (1)처럼 간단하게 사용도 가능하고 (2)처럼 세팅을 미리해주어도 가능하다.

iOS에서는 특히 필요한 순간에 생성하고 싶은 객체나 UIView요소들을 그릴때 많이 사용한다.
