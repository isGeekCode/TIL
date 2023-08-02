# Network Programming - RESTful APIs (작성중)

RESTful API란,   

웹 서버와 클라이언트 사이에서 데이터를 주고받기 위한 규칙과 방법을 정의한 인터페이스다.  

주로 HTTP 프로토콜을 사용하여 대이털르 요청하고 응답하는 방식으로 동작한다.  

<br><br>

## 알아야할 키워드

- 엔드포인트
- HTTP메서드
- Request
- Response

<br><br>

### 엔드포인트
RESTful API는 웹과 클라이언트 사이에서 데이터를 주고받기위한 수단이라고 했다.  

이 수단은 정말 다양하게 존재하기 때문에, 각각의 API마다 고유한 URL을 가지게 된다.  
 
이 URL을 엔드포인트라고 한다.  

<br><br>

### HTTP메서드
RESTful API는 주로 HTTP메서드를 사용한다고 했다. 대표적인 메서드는 아래와 같다.

- GET : 서버로부터 데이터를 요청하는 메서드다.
- POST : 서버로 데이터를 전송하고, 새로운 리소스를 생성하는 메서드다.
- PUT : 서버로 데이터를 전송하여, 리소스를 업데이트하는 메서드다.
- DELETE : 서버로부터 리소스를 삭제하는 메서드다.

이렇게 네가지가 있지만 정말 자주 사용하는 것은 `GET`, `POST` 이 두가지 방법이다.

<br><br>

### Request 
클라이언트에서 서버로 무엇인가 원하는 것을 의미한다.   
 
사용하는 메서드에 따라 요청 방법이 살짝 달라진다.   

- GET 메서드
    - 데이터를 URL의 쿼리 파라미터로 보낸다.
    - 데이터가 URL에 노출되므로 보안적으로 취약할 수 있다.
    - 주로 서버로부터 데이터를 요청할 때 사용한다.

예를 들어, `https://api.example.com/posts?category=technology&page=1`와 같이 요청하면,  

서버는 `category`가 `technology`이고 `page`가 `1`인 게시물 데이터를 응답한다.

<br><br>

- POST 메서드
    - 데이터를 HTTP요청의 바디에 담아서 보 낸다.
    - 데이터가 URL에 노출되지 않아 GET에 비해 보안적으로 안전하다.
    - 주로 서버로 데이털르 전송하여 새로운 리소스를 생성하거나 업데이트시 사용한다.
    
예를 들어, 아래와 같이 POST메서드를 사용할 수 있다.

- URL: `https://api.example.com/users`
- Body(JSON형식):
    ```swift
    {
      "name": "John Doe",
      "email": "johndoe@example.com",
      "age": 30
    }
    ```
<br><br><br>   

### Response

클라이언트의 요청을 받고, 서버에서 리턴하는 것을 말한다.  

Header와 Body의 형태를 가지고 있다.  
 
- Header : 요청이나 응답에 포함된 메타데이터를 담고 있다.
- Body : 요청이나 응답에 대한 실제 데이터가 담겨 있다.
    - 주로 JSON, XML, HTML, 텍스트 등의 형식으로 포함된다.

<br><br><br> 
   
## iOS에서 사용하는 실제 코드

단계는 아래와 같다.  
- 요청 URL 생성
- URLSession 객체 생성
- 데이터 요청을 생성
- 요청 완료시, 클로저 구현
- 에러처리
- 응답처리
- 데이터 파싱
- 요청 전송 시작


### GET형식

```Swift
import Foundation

func fetchPosts() {
    // 1. 요청 URL 생성.
    guard let url = URL(string: "https://api.example.com/posts") else {
        print("Invalid URL")
        return
    }

    // 2. URLSession 객체를 생성.
    let session = URLSession.shared

    // 3. 데이터 요청을 생성.
    let task = session.dataTask(with: url) { (data, response, error) in
        // 4. 요청이 완료되었을 때 실행되는 클로저입니다.

        // 5. 에러 처리
        if let error = error {
            print("Error: \(error)")
            return
        }

        // 6. HTTP 응답 처리
        guard let httpResponse = response as? HTTPURLResponse,
              (200...299).contains(httpResponse.statusCode) else {
            print("Invalid response")
            return
        }

        // 7. 데이터 파싱 및 처리
        if let data = data {
            do {
                let jsonObject = try JSONSerialization.jsonObject(with: data, options: [])
                // jsonObject를 원하는 모델로 파싱하거나 데이터 처리를 진행합니다.
                print(jsonObject)
            } catch {
                print("Error parsing data: \(error)")
            }
        }
    }

    // 8. 요청 전송 시작
    task.resume()
}

```


<br><br>


### POST형식
GET과 달리 Requst바디에 넣을 데이터를 생성해야한다.

```swift
import Foundation

func createNewUser() {
    // 1. 요청 URL 생성.
    guard let url = URL(string: "https://api.example.com/users") else {
        print("Invalid URL")
        return
    }

    // 2. URLRequest 객체 생성.
    var request = URLRequest(url: url)
    request.httpMethod = "POST" // HTTP 메서드를 POST로 설정합니다.

    // 3. 요청 바디에 전송할 데이터를 생성. (JSON 형식으로 예시)
    let newUser = [
        "name": "John Doe",
        "email": "johndoe@example.com",
        "age": 30
    ]

    do {
        let jsonData = try JSONSerialization.data(withJSONObject: newUser, options: [])
        request.httpBody = jsonData // 요청 바디에 데이터를 추가합니다.
    } catch {
        print("Error creating request body: \(error)")
        return
    }

    // 4. URLSession 객체 생성.
    let session = URLSession.shared

    // 5. 데이터 요청 생성.
    let task = session.dataTask(with: request) { (data, response, error) in
        // 6. 요청이 완료되었을 때 실행되는 클로저입니다.

        // 7. 에러 처리
        if let error = error {
            print("Error: \(error)")
            return
        }

        // 8. HTTP 응답 처리
        guard let httpResponse = response as? HTTPURLResponse,
              (200...299).contains(httpResponse.statusCode) else {
            print("Invalid response")
            return
        }

        // 9. 데이터 파싱 및 처리
        if let data = data {
            do {
                let jsonObject = try JSONSerialization.jsonObject(with: data, options: [])
                // jsonObject를 원하는 모델로 파싱하거나 데이터 처리를 진행합니다.
                print(jsonObject)
            } catch {
                print("Error parsing data: \(error)")
            }
        }
    }

    // 10. 요청 전송 시작
    task.resume()
}

```

<br><br><br>

## API응답 처리하기
응답을 받게 되면 해당 결과 값을 보고 내가 사용할 방식에 맞게 데이터를 처리해줘야한다.  

iOS에서 사용하는 대표적인 처리방법으로는 JSONSerialization을 사용하는 방법, Codable프로토콜을 이용한 방법이 있다.    
한번 살펴보자.  


<br><br>

### JSONSerialization을 사용하는 방법
JSON파싱은 `JSONSerialization`클래스를 이용하여 JSON데이터를 파싱하는 방법이다.  
이 방법은 iOS에서도 기본적으로 제공되는 API이다.  


- [TIL: 직렬화(Serialization)란](https://github.com/isGeekCode/TIL/blob/main/ComputerScience/Serialization.md) 
- [TIL: JSONSerialization으로  직렬화하기](https://github.com/isGeekCode/TIL/blob/main/iOS-Foundation/Foundation_JSONSerialization.md)  
- [TIL: iOS에서의 직렬화(Serialization하기)](https://github.com/isGeekCode/TIL/blob/main/iOS-Development/iOS_JSONSerializationMethod.md)  
- [TIL: Codable로 직렬화하기](https://github.com/isGeekCode/TIL/blob/main/iOS-Swift/Codable.md)
  

- 장점
    - iOS에서 기본으로 제공하기에 추가 라이브러리가 필요하지않다.
    - 간단한 JSON파싱 작업에 적합하다.
- 단점
    - 직접 파싱하기 떄문에, 코드가 상대적으로 많고 복잡할 수 있다.
    - JSON데이터의 키와 모델 객체의 프로퍼티 이름을 일일히 매핑해야한다.
    
<br><br>



<br><br><br>

## History
- 230801: 초안작성
- 230802: JSONSerialization 사용법 작성
- 230802: Codable 프로토콜 사용법 작성

