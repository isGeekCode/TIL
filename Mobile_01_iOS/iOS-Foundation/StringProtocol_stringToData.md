# String Protocol - String to Data

String을 Data로 만드는 상황은 아래와 같이 정말 다양하다.  


## 사용법

아주 간단하게 아래와 같이 사용할 수 있다.
```swift

let jsonString = """
    {
        "name": "John Doe",
        "age": 30,
        "email": "johndoe@example.com"
    }
"""
        
let stringData = jsonString.data(using: .utf8)

```


Apple Document를 보면 아래와 같이 나온다.   

```swift
extension String : StringProtocol { }

extension StringProtocol {
    /// Returns a `Data` containing a representation of
    /// the `String` encoded using a given encoding.
    public func data(using encoding: String.Encoding, allowLossyConversion: Bool = false) -> Data?
}
```

주어진 encoding 방법을 이용하여  데이터화 한다는 말이다.   
이렇게 만든 데이터를 아래와 같은 여러 곳에서 사용 가능하다.  

- 네트워크 통신: 웹 서비스나 RESTful API와 통신할 때, 문자열로 된 JSON 데이터를 Data 객체로 변환해 서버에 전송해야 할 수 있다.
- 파일 저장: 로컬 파일 시스템에 문자열을 저장하고자 할 때, 문자열을 Data 객체로 변환한 후 파일로 쓰기를 수행할 수 있다.
- 데이터 암호화: 보안이 필요한 문자열을 암호화하려면, 먼저 문자열을 바이트 배열인 Data 객체로 변환해야 할 수 있다.
- 텍스트 인코딩 변환: 다른 문자 인코딩으로 문자열을 변환하려면, 먼저 문자열을 해당 인코딩의 Data 객체로 변환해야 할 수 있다.
- 이미지 또는 바이너리 데이터 처리: Base64 인코딩과 같은 방법으로 이미지나 바이너리 데이터를 문자열로 받았을 경우, 이를 다시 Data 객체로 변환하여 처리해야 할 수 있다.
- 데이터베이스 저장: 일부 데이터베이스 시스템은 문자열 대신 Data 객체를 사용하여 데이터를 저장하고 검색할 수 있으므로 변환 작업이 필요할 수 있다.
- 다국어 지원: 다양한 언어와 로케일을 지원하려면, 문자열을 특정 인코딩의 Data 객체로 변환해야 할 수 있다.


## History
- 230803 : 초안작성
