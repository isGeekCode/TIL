# Special Literal

소스코드를 보다보면 #file #line #function 같은 것들을 볼 수 있다.  

특히 fatalError나 assert 함수를 자세히 살펴보면 아래와 같은 구성요소를 볼수가 있다.

```swift
func fatalError(_ message: @autoclosure() -> String = String(), file: Stitic String = #file, line: UInt = #line) -> Never
```

Literal은 아래처럼 구성된다.

- 일반 리터럴: “Hello”같은 문자열이나 숫자
- Array 리터럴: [1,2,3]
- dictionary 리터럴 [”key”: 13]
- playground 리터럴
- Special 리터럴


## playground 리터럴
Xcode에서 색이나 파일, 이미지를 표현하기위해 사용한다.

- #colorLiteral(red, green:, blue: alpha:)
- #fileLiteral(resourceName:)
- #imageLiteral(resourceName:)

그중 자주 사용할 수 있는 imageLiteral과 colorLiteral을 살펴보자.

각각 위예시처럼 파라미터를 넣어줄 수 있지만, `#imageLiteral()`, `#colorLiteral()`의 형태로 넣어줄 수 있다.

> 기존에는 그냥 color 혹은 image 만 입력해도 나왔지만 Xcode13부터는 위처럼 입력해야한다.   

<br><br>

### Color 리터럴

`#colorLiteral()`을 입력하면 아래와 같이 나온다.   
<img width="300" alt="스크린샷 2024-01-03 오후 12 49 11" src="https://github.com/isGeekCode/TIL/assets/128775960/2c0cb10e-ac59-4474-9dd5-f74590dbc137">

새로생긴 그림을 클릭하면 색상을 선택할 수 있다.  

<img width="300" alt="스크린샷 2024-01-03 오후 12 49 42" src="https://github.com/isGeekCode/TIL/assets/128775960/7b17dcfd-a2e1-4ec7-b040-cc376e214f8c">

그리고 이 색상을 선택해서 변수에 부여하는 것이다.  

<img width="300" alt="스크린샷 2024-01-03 오후 12 57 01" src="https://github.com/isGeekCode/TIL/assets/128775960/9975df51-e839-4070-8c1a-eac8985d635f">

<br><br><br>

### image 리터럴
마찬가지로 image리터럴도 `#imageLiteral()`로 입력한다.  
<img width="300" alt="스크린샷 2024-01-03 오후 12 47 36" src="https://github.com/isGeekCode/TIL/assets/128775960/6b916b23-9d17-496b-9818-c05e2a7a1584">

<br><br>

그림을 클릭하면 Assets에 추가된 이미지들이 보인다.  여기서 원하는 이미지를 선택한다.  
<img width="300" alt="스크린샷 2024-01-03 오후 12 47 28"   src="https://github.com/isGeekCode/TIL/assets/128775960/ea99b5b8-1b21-4757-9e60-521fac02a95b">

<br><br>

아래처럼 배열에 넣을 수도 있고, 변수에 넣을 수도 있다.  

<img width="300" alt="스크린샷 2024-01-03 오후 12 54 01" src="https://github.com/isGeekCode/TIL/assets/128775960/bf351151-78ea-40f2-9046-a10766052a22">

<br><br>

## Special 리터럴

그리고 마지막으로 Special Literal이 있다.

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
