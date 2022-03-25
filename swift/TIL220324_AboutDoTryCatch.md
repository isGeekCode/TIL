# TIL220324_DoTryCatch

Category: isGrammer
Langu: Swift
Tag: API, JSON
isGrammer: No
isOK: No
isPosted: No
isRad: No
isRead: No
isSecret: No
공부날짜: 2022년 3월 24일
생성일시: 2022년 2월 25일 오후 3:59
선행지식: Codable, EscapeClosure, HTTP, OptionalBinding, URLSession
최종편집: 2022년 3월 24일 오후 4:59
추가개념?: No
환경: Xcode

## 서론

## 선행 지식

## 오류처리의 과정

오류 처리에는 다음 세 가지 과정이 필요합니다.

1. **오류의 종류 정의하기**
2. **발생한 오류 던지기**
3. **던진 오류 처리하기**

# **1. 오류의 종류 정의하기 (선택사항)**

먼저 오류의 종류를 정의해줍니다.

```
enum 오류종류이름 : Error {
     case 종류1
     case 종류2
       .
       .
       .
}
```

오류의 종류는 아래와 같이 enum으로 정의합니다.

```swift
enum TestError : Error {
	case outOfRange                          // 1
	case invalidInputNum(testNum : Int)      // 2
}

// alamofire에 정의된 AFError 에러 정의
public enum AFError: Error {
    /// The underlying reason the `.multipartEncodingFailed` error occurred.
    public enum MultipartEncodingFailureReason {
        case bodyPartURLInvalid(url: URL)
        case bodyPartFilenameInvalid(in: URL)
				...
		}
}
```

1번은 기본적인 enum 케이스이고 2번은 parameter를 받는 케이스입니다.

예외상황이 많아질수록 케이스가 늘어날 수 있습니다.

여기서 1**. 오류의 종류를 정의 하는 부분**은 선택사항입니다.

그 이유는 궂이 케이스별로 오류처리하지 않을 때도 있기 때문입니다.

그냥 간단하게 에러 출력하실거면 건너뛰도 됩니다.

# **2. 발생한 오류 던지기**

오류는 **throws** 를 이용해 던집니다. “**오류를 처리해 주는 곳으로 전달해준다 “**라는 것을 의미 합니다.

```swift
func printNumber(_ number: Int) -> Int {
    var text = ""                    // 변수생성
	  guard number > 0 else { return } // 오류가 발생할 수 있는 부분

		return text
}
```

자, 위에 printNumber()라는 메소드가 있습니다.

중간에 guard문을 썼는데 이부분에서 오류가 발생할 수도 있기 때문에 사용했습니다.

오류를 던지기 위해 **throw를 총 두 군데에 써줍니다.**

```swift
func printNumber(_ number: Int)throws -> Int {    // 1   throws
	var text = ""

  guard number > 0 else {
		throw TestError.outOfRange                // 2 throw
	}
	return text
}
```

1. 첫번째 **throws는 오류가 발생할 가능성이 있는 메소드 제목 옆**에 써줍니다.
2. 두번째 **throw ( ‘s’ 없음)은 오류가 발생할 구간에**서 써줍니다.

   → 처음에 오류를 정의 했다면 이곳에 추가합니다.

```swift
enum TestError : Error {
	case outOfRange                          // 1
	case invalidInputNum(testNum : Int)      // 2
}
```

여기서 2번처럼 변수가 있는 경우, 아래와 같이 구현합니다.

```swift
func printNumber(_ number: Int) throws -> Int {
	var text = ""
	guard number > 0 else {
		throw TestError.invalidInputNum(testNum: number)
	}
  return text
}
```

꼭 number가 아니어도 넘겨주고 싶은 값을 넘겨줄 수 있다.

# **3. 던진 오류 처리하기**

오류 처리는 **try**와 **do-catch**로 합니다.

다시 printNumber 함수로 돌아가볼게요

```swift
func printNumber(_ number: Int) throws -> Int {
    var text = ""
		guard number > 0 else {
		   throw TestError.outOfRange
    }
		return text
}
```

해당 경우, throw로 예외를 던져줬습니다.

예외를 받는 곳은 그럼 어디냐.

printNumber() 메소드를 사용하는 곳입니다.

예를들어, printNumber() 메소드가 클래스 Object 안에 있었다고 가정

```swift
class Object {
    func printNumber(_ number: Int) throws -> Int {
           .......
    }
}
```

우선 Object 인스턴스를 만들어주고 printNumber() 메소드를 호출해줍니다.

```swift
let object = Object()

let resultNumber = object.printNumber(-20)
```

근데 printNumber에 변수로 -20이라는 음수값을 넣어줬습니다.

이러면 에러가 발생하게 되는데

이때 오류가 발생하는 메소드는 **try**를 써줘야합니다.

따라서 위의 방식이 아니라

```swift
let resultNumber = try object.printNumber(-20)
```

이렇게 try를 넣어줍니다! 오류 발생하는 메소드 앞에 말이죠.

```swift
func printNumber(_ number: Int)throws -> Int {
```

위에서 printNumber 뒤에 throws를 써줬다는건

이 함수에서 오류를 던진다는 의미였죠?

**try**의 의미는 이렇습니다.

```
‘이 함수가 오류가 발생할 수도 있는데, 한번 시도해볼게요.’
```

말 그대로 ‘시도해보겠다'는 선언이죠.

하지만 여기서 끝이 아니라 do-catch로 감싸줘야 처리를 할 수 있습니다.

```swift
do {

	let resultNumber = try object.printNumber(-20)

} catch {                  // 생략이 가능

   print(error)

}
```

위의 do-catch 문은 오류를 처리하는 가장 간단한 방법입니다.

1번에서 오류 종류 정의하는 건 선택사항이라고 했죠?

오류를 정의하지 않아도 기본적으로 이렇게 에러를 출력할 수 있습니다.

심지어는 catch를 생략해도 무방합니다.

```swift
do {

	let resultNumber = try object.printNumber(-20)

}
```

이렇게요

하지만 모처럼 오류 케이스를 나누어줬으니,

활용방법을 알아봅시다.

```swift
do {

	let resultNumber = try object.printNumber(-20)

} catch TestError.outOfRange {
	// 오류처리
} catch TestError.invalidInput(let testNumber) {
   // 오류처리
}
```

위에서 정의한 케이스별로 처리해줍니다

오류처리까지 채우면 이렇습니다

```swift
do {

	let resultNumber = try object.printNumber(-20)

	} catch TestError.outOfRange {
	   print("양수가 아닙니다!")

	} catch TestError.invalidInput(let testNumber) {
	  print("부적절한 숫자 \(testNumber)")
	}
```

케이스별로 처리하기 때문에 switch문으로도 쓸 수 있습니다

```swift
do {

	let resultNumber = try object.printNumber(-20)

} catch {switch error {

	   case TestError.outOfRange:
	       // 오류처리
	   case TestError.invalidInput(let number):
	       // 오류처리
	}
}
```

# **추가 설명 : try?와 try!**

try는 try?나 try!로 쓸 수 있습니다.

## **try?**

```swift
let resultNumber =try? object.printNumber(20)
print("\(resultNumber)")   // Optional("20") 또는 nil
```

printNumber에서 오류가 발생할 수도 있다는 걸 인정하는 겁니다.

Swift에서 물음표는 옵셔널을 의미하죠.

따라서 resultNumber가 리턴값을 옵셔널 타입 또는 nil로 받을 수 있게 됩니다.

옵셔널 타입의 리턴값이 있을 경우 try? 를 쓰게되면 이중 Wrapping 됩니다. 그래서 **옵셔널 바인딩 할때 주의**

## **try!**

```swift
let resultNumber =try! object.printNumber(-20)
print("\(resultNumber)")   // "20"
```

printNumber 메소드에서 오류가 절!대! 발생하지 않을 자신이 있으면 씁니다.

오류발생 시 Runtime Error가 발생하고 강제종료됩니다.
