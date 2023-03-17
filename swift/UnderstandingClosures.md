# Understanding Closures in Swift : 클로저 톺아보기


### Categories
- [클로저란](#클로저란)
- [클로저 표현식](#클로저 표현식)
- [클로저의 사용하기](#클로저의 사용하기)

### [클로저란](#클로저란)
클로저는 Named Closure와 Unnamed Closure로 나뉜다.

우리가 흔하게 사용하는 함수는 Named Closure다.

둘다 클로저에 포함되지만 우리가 통상적으로 부르는 클로저는 Unnamed Closure를 말한다. 

```swift
// 1. Named Closure
func doSomthing() {
    print("do something!!!")
}

// 2. UnnamedClosure
let doSomething = { print("do something!!!") }
```

결국 클로저와 함수는 그게 그것이기 때문에 1급객체의 성질을 가지고 있다.

즉 클로저도 아래의 성질을 갖고있다.

1. 변수나 상수에 대입할 수 있다.
2. 함수의 인자값으로 클로저를 전달할 수 있다.
3. 함수의 반환값으로 클로저를 사용할 수 있다.

### [클로저 표현식](#클로저 표현식)

unnamed Closure , 익명함수 (이하 클로저로 설명) 는 헤드 부분과 바디부분으로 나누어진다. 

이걸 구분하는게 in이라는 키워드이다. 

![스크린샷 2022-11-25 오전 9.00.59.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/daec0b09-5c42-4bad-be40-be0db4dc9978/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-11-25_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_9.00.59.png)


### [클로저의 사용하기](#클로저의 사용하기)

### 함수의 사용법

```swift

// 기본형
func doSomething(firstParam: String, secondParam: String) -> Void {
}

// 위 함수에서 Void 생략
func doSomething(firstParam: String, secondParam: String) {
}

// 파라미터가 없다면?
func doSomething() {
}
```

### 클로저의 사용법

파라미터와 리턴타입의 유무에 따라 조금씩 다르다. 

```swift
// ParamX, ReturnTypeX
let doSomething = { () -> () in
        print("someThing")
}
// 사용
domething()

// ParamO, ReturnTypeO
let doSomething = { (firstParam: String ) -> String in
    return "Something is\(firstParam)"    
}
// 사용
doSomething("work") // doSomething( firstParam: "work")   //ERROR!!!!
// Something is work
```

## 1급객체의 특징

### 1. 변수나 상수에 대입할 수 있다.

클로저 자체를 변수에 대입하며 동시에 작성이 가능하다.

```swift
let closure = { () -> () in
    print("Closure")
}

let closure2 = closure
```

### 2. 함수의 파라미터 값으로 클로저를 전달할 수 있다.

클로저의 타입이 () **->** () 와 같을 때

파라미터의 타입을 명시하는 부분에 명시한다.

```swift
func doSomething(closure: () -> ()) {
    closure()
}
```

위 경우처럼 함수를 파라미터로 받는 함수가 있다.

이걸 아래처럼 파라미터 안에 클로저를 넣어줘도 된다.

![스크린샷 2022-11-25 오후 12.34.53.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/488994d8-0e8b-4c68-8bad-fde118a035ee/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-11-25_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_12.34.53.png)

표시된 부분이 파라미터 안에 들어간 클로저다.

### 3. 함수의 반환값으로 클로저를 사용할 수 있다.

클로저의 타입이 () **->** () 와 같을 때, 

1. 함수의 반환타입에 명시해 준다.
2. return 에 클로저를 넣는다.

```swift
func doSomething() -> () -> () {

        return { () -> () in
                print("Hello world!")
    }
}
```

## 클로저 실행하기

1. 대입된 변수나 상수로 호출하기

```swift
let closure = { () -> String in
    return "Hello world!"
}

closure()
```

1. 클로저를 직접 호출하기
    
    클로저 자체를 ()로 감싸고, 호출구문()를 한번더 추가한다. 
    

```swift
( { () -> () in
    print("Hello world!")
} )()
```

## 1. 후행클로저 Trailing Closure

- 함수의 마지막 파라미터가 클로저일 때, 이 클로저를  파라미터 값 형식이 아니라  함수 뒤에 붙여서 작성할 수 있다.
- Argument Label은 생략한다.

### 파라미터가 클로저 하나인 함수

```swift
func doSomething(closure: () -> ()) {
    closure()
}
```

위 함수를 호출하려면 `함수의 호출구문 ()안에` 아래와 같이 해야했다.

위 함수를 호출할 때 아래와 같이 작성한다. 이렇게 파라미터 의 값형식으로 쓰인 클로저를 `Inline Closure`라고 부른다.

```swift
// 함수의 파라미터 값안에 있는 클로저 Inline Closure
doSomething(closure: { () -> () in
    print("Hello!")
})
```

각 괄호들 `})` 때문에 가독성이 떨어져서 해석이 쉽지않다.

이럴때, 클로저를 파라미터 값형식이 아니라 함수의 마지막에 꼬리처럼 덧붙여서 아래처럼 사용할 수 있다.

```swift
// 함수호출구문 안에 파라미터값으로 있던 클로저가 꼬리처럼 붙었다.
doSomething () { () -> () in
    print("Hello!")
}
```

1. 파라미터가 클로저 하나여서 후행클로저가 가능하다
2. closure라는 Argument Label이 생략됐다.

여기서 파라미터가 클로저 하나일경우엔 호출구문도 생략가능하다

```swift
doSomething { () -> () in
    print("Hello!")
}
```

### 파라미터가 여러개인 함수

아래와 같이 첫 번째 파라미터로 success라는 클로저를 받고,

두 번째 파라미터로 fail이라는 클로저를 받는 함수가 있다.

```swift
func fetchData(success: () -> (), fail: () -> ()) {
    //do something...
}
```

위 함수를 Inline Closure로 호출하면 아래와 같다. 

```swift
fetchData(success: { () -> () in
    print("Success!")
}, fail: { () -> () in
    print("Fail!")
})
```

역시 가독성이 훌륭하진않다.  이것을 탈출클로저로 작성한다면 마지막 클로저는 함수뒤로 옮길 수 있다.

```swift
fetchData(success:  { () -> () in
            print("Success!")
        }) { () -> () in
            print("Fail!")
        }
```

그러면 success의 파라미터 값은 inlineClosure, fail의 파라미터 값은 후행클로저로 호출이 가능하다.

fetchData(success:  { () -> () **in**

print("Success!")

}) { () -> () **in**

print("Fail!")

}

하지만 이렇게 파라미터가 여러개일 경우에는 파라미터를 넘겨줘야하기 때문에 함수 호출 구문()을 생략할 수 없다.

## 클로저 경량화

클로저는 헤드부분  `() → () in` 여러종류의 괄호때문에 살짝 가독성이 떨어진다.  그래서 어려워보인다. 그래서 문법을 최적화해서 클로저를 단순하게 쓸 때 사용하는 것이 경량화 문법이다.

```swift
func doSomething(closure: (Int, Int, Int) -> Int) {
    closure(1, 2, 3)
}
```

위 함수는 파라미터값으로 클로저를 갖고 있다.  이걸 호출할 때, Inline Closure로 호출하면 아래처럼 작성할 수 있다.

```swift
doSomething(closure: { (a: Int, b: Int, c: Int) -> Int in
    return a + b + c
})
```

이걸 경량문법으로 바꿔보자

### 1. 파라미터의 타입과 리턴타입을 생략할 수 있다.

위에서 파라미터에 쓰인 `: Int`와  in  좌측에 있던 `→ Int` 처럼 기입된 타입들을 아래와 같이 생략하여 작성가능하다. 

```swift
doSomething(closure: { (a, b, c) in
    return a + b + c
})
```

 

### 2. Parameter Name은 Shortand Argument Name으로 대체하고, 동시에 in키워드를 삭제한다.

`Shortand Argument Name`이란 클로저 내에서 파라미터 이름대신 $를 사용해서 첫번째일경우 `$0`, 두번째 파라미터일경우 `$1`를 사용하는 것을 말한다. 

위 1번 예제의 함수를 아래와 같이 바꿀 수 있다.

```swift
doSomething(closure: {
    return $0 + $1 + $2
})
```

### 3. 단일 리턴문일 경우, return도 생략한다.

클로저 내부에 코드가 return 구문 하나뿐이라면 아래와 같이 생략가능하다. 

```swift
doSomething(closure: {
    $0 + $1 + $2
})
```

### 4. 마지막 파라미터 값이 클로저라면 후행클로저로 작성한다.

위의 예시는 단일 파라미터지만 마지막 파라미터의 값이 클로저라면 파라미터안에 있는 클로저를 뒤로 뺄 수 있다.

```swift
doSomething() {  
     $0 + $1 + $2
}
```

또한 이미 후행클로저는 함수의 파라미터가 클로저 하나라면 함수 호출구문() 도 생략가능하다.

```swift
doSomething {  
     $0 + $1 + $2
}
```

## 2. @autoClosure

파라미터로 전달된 일반구문 과 함수를 클로저로  래핑(wrapping)하는 것을 말한다. 

@autoClosure 어노테이션은 파라미터의 함수타입정의 바로앞에 붙인다. 

```swift
func doSomething(closure: @autoclosure () -> ()) {
}
```

위와 같이 작성하면 이제 closure라는 파라미터는 실제로 클로저를 전달받진 않지만 클로저처럼 사용할 수 있게된다. 

클로저와 다른 점은 실제 클로저를 전달하는 것이 아니기 때문에 파라미터로 값을 넘기는 것처럼 ()를 통해 구문을 넘겨줄 수가 있다.

```swift
doSomething(closure: 1 > 2)

func doSomething(closure: @autoclosure () -> ()) {
    closure()
}
```

이 때 주의할 점은 파라미터가 없어야만한다. 리턴타입은 상관없다. 

### autoClosure는 지연된 실행을 할 수 있다.

일반구문은 작성되자마자 실행된다. 하지만 autoClosure로 작성하면 함수 내에서 클로저를 실행할 때까지 구문이 실행되지않는다. 함수가 실행되는 시점에 구문을 클로저로 만들기 때문이다. 

autoClosure는 아직 공부가 더필요하다. 

다음에 보강할 것!!

## 3. 탈출클로저 @escaping

지금까지 사용한 클로저들은 대부분 함수내부에서 직접실행할 때 사용하는 클로저 들이었다. 

중첩함수를 리턴할 수 없고 어쩌고 저쩌고 하는 이유들이 있지만. 가장 중요한것은

내가 원하는 시점에 원하는 로직을 사용할 수 있도록 조절할 수 있다는 것이다. 

이것 만으로도 엄청난 매력을 가진 클로저다.

### 사용방법

클로저의 파라미터 타입 앞에 @escaping 을 달아준다. 

```swift
// 구현
func doSomething(closure: @escaping () -> ()) {
}

// 사용
doSomething {
        closure()
}
```

사용할 땐 내가 원하는 상황, 시점에 후행 클로저 안에서 @escaping을 붙인 파라미터를 호출하면된다. 

### iOS에서 흔하게 사용하는 클로저

### 후행클로저

Alert을 구현하다보면 마주치는 후행클로저이다. 

confirmAction에 담긴 버튼을 클릭했을 때, 이후에 실행되는 클로저 이다. 

```swift
let alert = UIAlertController(title: "", message: "종료하시겠습니까.", preferredStyle: .alert)
let confirmAction = UIAlertAction(title: "확인", style: .default) { _ in
    self.dismiss(animated: true)
}
              
alert.addAction(confirmAction)
self.present(alert, animated: false, completion: nil)
```

### completion / Completion handler

위와 똑같은 방법인데 특별한 시점을 위해 자주 사용하는 탈출클로저이다. 

함수를 구현할 때, 파라미터명을 completion 이나 completion handler로 자주 작성한다. 

주로 저녁함수를 빼서 사용하거나, API통신할 때  특정시점을 위해 사용한다. 

아래와 같이 이미지를 다운로드 성공, 실패할 때 UIImage를 전달할 때도 사용한다.

```swift
public struct FileDownloader {

        /// 이미지 다운로드 함수
    /// - Parameters:
    ///   - url: 이미지 URL
    ///   - completionHandler: true : 이미지 다운로드 성공, false : 이미지 다운로드 실패(with UIImage())
    static public func downloadImage(fromUrl url: String, completionHandler: @escaping (Bool, UIImage) -> Void) {
        guard let imageUrl = URL(string: url),
              let imageData = try? Data(contentsOf: imageUrl),
              let image = UIImage(data: imageData) else {
            ErrLog("Convert url to Data OR data to Image FAIL")
            completionHandler(false, UIImage())
            return
        }
        completionHandler(true, image)
    }

}

```

아래와 같이 사용한다.

![스크린샷 2022-11-25 오후 3.03.19.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8abf0b3e-b316-42b9-96c5-1235c7c7a069/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-11-25_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_3.03.19.png)

API를 이용할 때도 많이 사용한다. 

성공이나 실패를 탈출클로저에 담아 사용가능하다.

```swift
func getDataReturnData(url: String, successHandler: @escaping (_ resultData: Data?)-> Void, errorHandler: @escaping (_ error: Error)-> Void) -> Void {

        let session = URLSession.shared
      if let reqUrl = URL(string: url) {
      session.dataTask(with: reqUrl) { (data, response, error) in
                if error != nil {
                            errorHandler(error!)
                } else {
                        guard let resultdata = data else { 
                                    successHandler(nil)
                         return 
                        }
                        successHandler(resultData)
                }
        }.resume()
```

정말 다양하게 사용이 가능하다. 

작성하다보니 생각보다 별거 아니라는 생각이 들었는데 

어렵다 ㅋㅋㅋ… 특히 autoClosure는… 저만 못 봤나요.. 언제쓰지….
