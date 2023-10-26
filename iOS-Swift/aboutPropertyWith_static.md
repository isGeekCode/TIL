# 타입메서드, 클래스메서드, 인스턴스 메서드

다른 글에서 타입 프로퍼티에 대해 알아봤는데

메서드도 마찬가지로 타입메서드라는 게 있다.

그래서 그와 비교할 수 있는 세가지를 소개하려고 한다. 


<br><br>

스위프트의 함수는 세 가지 종류가 있다.

앞에 뭐가 붙느냐에 따라 `instance` / `class` / `static` 로 나뉜다.


```swift

class SwiftMethod {

    // 1. Instance 함수
    func myInstanceFunc() {}
    // 2. class 함수
    class func myClassFunc() {}
    // 3. static 함수
    static func myStaticFunc() {}

}
```

우리가 Swift로 코딩을 처음할 때, 사용하던 일반적인 함수 1번이 바로 instance 메서드이다. 

## class func 와 static func

### 공통점
이 둘은 공통적으로 타입 메서드 라고 부른다. 

이들은 객체를 생성자`()`를 사용하지 않아도 바로 접근이 가능하다.


```swift
SwiftMethod.myClassFunc()
SwiftMethod.myStaticFunc()
```

### 차이점

이 둘의 차이는 이 클래스를 상속받은 subClass에서 차이를 느낄 수 있다.

class 메서드는 override가 가능하고
static 메서드는 override가 불가능하다.


```swift
class SubclassSwiftMethod: SwiftMethod {
    
    override class func myClassFunc() {
        print("myClassFunc()")
    }
    
    /// Cannot override static method!!!!
    override static func myStaticFunc() {
        print("myStaticFunc()")
    }
    
}

```

더불어 반대로 상속이 불가능한 struct, enum에 class func를 정의해도 에러가 난다.  

## final class func 와 static func

static func 는 상속을 못받기 때문에,

더이상의 상속을 막아주는 final 키워드를 이용하여 class func에 사용하면 동일한 결과를 가져온다. 

class SwiftMethod {
    class func myClassFunc() {}
    static func myStaticFunc() {}
}

//style 1 : final class
class SubSwiftMethod1 : Sample {
    override final class func myClassFunc() {}
}

//style 2 : static
class SubSwiftMethod2 : Sample {
    override static func myClassFunc() {}
}



## History

- 231026: 초안작성
