# [Common Method] 로그 관련 함수

Category: isTutorial

Swift에서 콘솔창에 로그 쉽게 출력하는 방법이다.

보통 로그에 날짜, 파일명, 메소드명, 라인을 작성하려면 아래와 같이 작성한다.

```swift
print("\(Date()) \(#file.components(separatedBy: "/").last ?? "") \(#function) \(#line) 로그 내용")
```

## 함수설명

### Date() : → 날짜 출력

### #file :

파일 출력

→ #file만 사용하는 경우에는 파일이 있는 디렉터리가 모두 출력

**components(separateBy:)함수를 사용**

.last → 마지막 위치

### #fuction

현재 메소드명

### #line

현재 라인 출력

위와같이 작성하면 콘솔창에 이렇게 출력된다.

## 출력결과

### #file만 사용 하는 경우

```
2020-10-11 16:31:33 +0000 /Users/dev/Desktop/workspace/ios/Proj/Proj/MainVC.swift viewDidLoad() 32 로그 내용
```

### #file과 components(separateBy:).last 사용하는 경우

```
2020-10-11 16:31:33 +0000 MainVC.swift viewDidLoad() 31 로그 내용
```

## 별도의 로그 메서드 생성하기

```swift

/**
public func 으로 아래와 같이 정의하고 출력하는 형식은 원하는대로 변경하여 사용하면 된다.
#if DEBUG, #endif 를 사용하면 디버그 모드에만 로그가 출력되고 릴리즈시에는 로그가 출력되지 않는다.
*/

/**
- parameters :
	- #file : 현재의 파일 디렉토리
	- #line : 현재 줄의 위치
	- #function : 현재 사용한 함수의 위치
*/

public func Log<T>(_ object: T?, filename: String = #file, line: Int = #line, funcName: String = #function) {
    #if DEBUG
    if let obj = object {
        print("\(Date()) \(filename.components(separatedBy: "/").last ?? "")(\(line)) : \(funcName) : \(obj)")
    } else {
        print("\(Date()) \(filename.components(separatedBy: "/").last ?? "")(\(line)) : \(funcName) : nil")
    }
    #endif
}
```

실제로 사용하는 부분에서는 아래와 같이 호출해서 사용하면 된다.

```swift
Log("로그내용")
```

위와같이 작성하면 콘솔창에 이렇게 출력된다.

```
2020-10-11 16:31:33 +0000 MainVC.swift(33) : viewDidLoad() : 로그 내용
```

## 메소드 사용하여 float <-> String, 현재 클래스 이름 받기

### 타입캐스팅

### 선언

```swift
init<Subject>(describing instance: Subject)
```

String( )으로 특정 값을 감싸서 문자열(String)로 만든다.

Swift의 기본 타입들은 모두 이 변환이 가능하며, (사실 인터폴레이션이 가능한 타입들은 다 된다고 보면 된다.

그 외에 이를 통한 직변환이 불가능한 타입들은 String(describing:)을 이용해서 변환하면 된다.

**Float -> String**

```swift
let stringValue = String(describing: floatValue)
```

반대로 **String -> Float**

```swift
let floatValue = CGFloat(NSString(string: StringValue).floatValue)
```

---

### String(describing:) 메소드를 사용하여 현재 클래스 이름 받기

\*ClassName.Type할 경우 컴파일 에러 발생 -> 특정 클래스의 타입을 얻고 싶은 경우 ClassName.self로 접근

AViewController 파일에서 다음과 같이 코드를 작성해도 되지만,

```
print(String(describing: AViewController.self))
```

더 간편하게, 클래스이름을 입력하지 않아도 현재 클래스 이름을 출력 가능

```
print(String(describing: type(of: self)))
```

![title](Assets/스크린샷_2022-03-18_오전_10.58.15.png)
