
# Special Literal

소스코드를 보다보면 #file #line #function 같은 것들을 보게되는데요

특히  fatalError나 assert 함수를 자세히 살펴보면  아래와 같은 구성요소를 볼수가 있어요.

```swift
func fatalError(_ message: @autoclosure() -> String = String(), file: Stitic String = #file, line: UInt = #line) -> Never
```

Literal은 아래처럼 구성돼요 

- 일반 리터럴: “Hello”같은 문자열이나 숫자
- Array 리터럴: [1,2,3]
- dictionary 리터럴 [”key”: 13]
- playground 리터럴
- Special 리터럴

playground 리터럴은 Xcode에서 색이나 파일, 이미지를 표현하기위해사용합니다.

- #colorLiteral(red, green:, blue: alpha:)
- #fileLiteral(resourceName:)
- #imageLiteral(resourceName:)

그리고 마지막으로 Special Literal입니다.

- #file: String
- #fileID: String
- #filePath: String
- #line: Int
- #column: Int
- #function: String
- #dsohandle: UnsafeRawPointer

### #file

- 표현식이 등장하는 파일의 경로

### #filePath

- 표현식이 등장하는 파일의 경로

### #fileID: String

- 모듈 및 파일의 이름
- `Sample/ViewController.swift`

### #line: Int

- 표현식이 등장하는 line 의 번호

### #column: Int

- 표현식이 시작하는 column 번호

### #function: String

- 표현식이 나타나는 선언부(declaration)의 이름