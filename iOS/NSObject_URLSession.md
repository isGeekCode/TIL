# NSObject - URLSession

Swift에서 데이터 통신을 하는 가장 기본적인 방법은 URLRequest, URL Session, and URLSessionDataTask 사용하는 방법이다.

- URLRequest: URLRequest는 웹 서버에 보낼 요청의 정보를 제공하는 객체.
- URLSession: URLSession은 웹 서버에 데이터를 전송하거나 데이터를 수신하는 네트워크 통신을 처리하는 객체.
- URLSessionDataTask: URLSessionDataTask는 URLSession 객체를 통해 웹 서버에 데이터를 요청하고 응답을 수신하는 객체.

이 세 객체를 사용하여 HTTP GET, POST, PUT, DELETE 등의 네트워크 요청을 처리할 수 있다.

HTTP 요청을 사용하여 RESTful API를 호출하는 것이 가장 기본적인 방법이다.

### GET 요청으로 웹 API에 접근하는 예제.

```swift
let url = URL(string: "https://api.example.com/data")!
let task = URLSession.shared.dataTask(with: url) { (data, response, error) in
    if let data = data {
        let result = String(data: data, encoding: .utf8)
        print(result)
    }
}
task.resume()
```

이 외에도 Alamofire, Moya 등의 라이브러리를 사용할 수도 있다. 이들 라이브러리는 더 편리하고 강력한 HTTP 통신 기능을 제공한다.

### POST 사용하기
```swift
let url = URL(string: "https://www.example.com/post")!
var request = URLRequest(url: url)
request.httpMethod = "POST"

let parameters = ["key": "value"]
let data = try! JSONSerialization.data(withJSONObject: parameters, options: [])
request.httpBody = data

let task = URLSession.shared.dataTask(with: request) { data, response, error in
    guard let data = data, error == nil else {
        print(error?.localizedDescription ?? "No data")
        return
    }

    let responseJSON = try? JSONSerialization.jsonObject(with: data, options: [])
    if let responseJSON = responseJSON as? [String: Any] {
        print(responseJSON)
    }
}

task.resume()

```


# Alamofire

Alamofire는 iOS에서 HTTP 네트워크 통신을 다루는 라이브러리다. 아래는 Alamofire를 사용하여 GET 요청을 보내는 예제이다.


## GET형식
```swift
import Alamofire

AF.request("https://api.example.com/data")
    .response { response in
        if let data = response.data {
            let result = String(data: data, encoding: .utf8)
            print(result)
        }
    }
```
또는
```
import Alamofire

AF.request("https://www.example.com/api/v1/data").responseJSON { response in
      if let data = response.data {
          print("Success: \(data)")
      } else {
          print("Error: \(String(describing: response.error))")
      }
  }
```


## POST형식

```swift
import Alamofire

let parameters: [String: Any] = ["key": "value"]

AF.request("https://www.example.com/post", method: .post, parameters: parameters, encoding: JSONEncoding.default)
    .validate()
    .responseJSON { response in
        switch response.result {
        case .success(let value):
            print(value)
        case .failure(let error):
            print(error)
        }
    }
```

## Alamofire의 6가지 response handler
- 1. response
```swift
AF.request("https://api.example.com/data").response { response in
        if let data = response.data {
            let result = String(data: data, encoding: .utf8)
            print(result)
        }
    }
```

- 2. reponseData
```swift
AF.request("https://www.example.com/api/v1/data").responseData { response in
    switch response.result {
        case .success(let data):
            print("Success: \(data)")
        case .failure(let error):
            print("Error: \(error)")
    }
}
```


- 3. responseString

```swift
```

- 4. responseJSON


- 5. responseDecodable



# Validation
유효성검사는 요청에 대한 response를 하기 전에 .validate()를 호출함으로써 유효하지 않은 상태 코드나 MIME타입이 있는 경우 response하지 않도록 한다.

일반적인 사용 방법은 아래와 같고

AF.request(url)
  .validate()
  .response { response in 
     print(response)
}
상태 코드나 MIME 타입 조건을 넣는 방법은 다음과 같다.

AF.request(url)
  .validate(200..<300) // 200~300 사이 상태코드만 허용
  .validate(contentType:["application/json"]) // JSON 포맷만 허용
  .response { response in 
      print(response)
}
주석처럼 위 코드는 해당 URL에 대한 응답 처리를 상태코드가 200~300이면서 JSON 포맷일 때 응답처리를 한다.

