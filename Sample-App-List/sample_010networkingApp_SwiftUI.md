# Sample App : 네트워킹과정 앱 - SwiftUI [Data parse, URLSession, completion, Singleton, Error, Result, Generic]

<br>

네트워킹앱의 기능은 아래와 같다.

- 최소기능
    - 리스트표시
    - 하단 버튼 누를경우, 네트워킹
    - 네트워킹 결과를 리스트에 추가

<br>

- 네트워킹 구현과정
    - 서버에 데이터 요청
    - 데이터를 받아온다
    - 데이터를 파싱한다.
    - 파싱한 데이터로 화면을 그린다. 



<br><br>

## Contents
- [기본구조 구현](#기본구조-구현)
- [API 소개](#API-소개)
- [Response 더미데이터 생성](#Response-더미데이터-생성)
    - [CodingKey](#CodingKey)
    - [더미데이터로부터 데이터가져오기](#더미데이터로부터-데이터가져오기)
- [URLSession을 이용한 Request](#URLSession을-이용한-Request)
- [escaping closure](#escaping-closure)
    - [Escaping을 이용한 Response 호출](#Escaping을-이용한-Response-호출)
- [Error 타입 사용하기](#Error-타입-사용하기)
- [커스텀 Result 만들어 사용하기](#커스텀-Result-만들어-사용하기)
- [Generic으로 유동적인 메서드 만들기](#Generic으로-유동적인-메서드-만들기)

    
<br><br>

## 기본구조 구현
- 기본앱 구현
- 버튼구현


```swift
import SwiftUI

struct ContentView: View {
    
    @State var data: [String] = ["A", "B"]
    
    var body: some View {
        VStack {
            List { 
                // 컨텐츠 추가
                ForEach(data, id: \.self) { item in
                    Text(item)
                }
            }
        }
        
        Button {
            requestData()
        } label: {
            Text("Append")
        }
    }
    
    /// 버튼클릭시 동작
    func requestData() {
        data.append("etc")
    }
}

#Preview {
    ContentView()
}
```


<br><br>

### 동작

  <img width="300" alt="img1 daumcdn-4" src="https://github.com/isGeekCode/TIL/assets/76529148/8f58ee12-46dd-473e-8b2f-d13fb3bf5b6b">  

<br><br>

[[Top]](#contents)

<br><br><br>


## API 소개

[koreanjson API 경로](https://koreanjson.com/)

- Resources
    - Users: 유저 10명
    - Posts: 포스트 200개
    - Todos: 할 일 200개
    - Comments: 댓글 200개

<br>

- Routes
    - /users : GET 유저 목록
        - /users/:id : GET 유저 조회
        - 예시 : https://koreanjson.com/users/1
    - /posts : GET 포스트 목록
        - /posts/:id : GET 포스트 조회
        - 예시 : https://koreanjson.com/posts/1

    - /todos : GET 할 일 목록
        - /todos/:id : GET 할 일 조회
        - 예시 : https://koreanjson.com/todos/1

<br>

- Response
```swift
// 유저 목록 : https://koreanjson.com/users/1

{
    "id": 1,
    "name": "이정도",
    "username": "jd1386",
    "email": "lee.jungdo@gmail.com",
    "phone": "010-3192-2910",
    "website": "https://leejungdo.com",
    "province": "경기도",
    "city": "성남시",
    "district": "분당구",
    "street": "대왕판교로 160",
    "zipcode": "13525",
    "createdAt": "2019-02-24T16:17:47.000Z",
    "updatedAt": "2019-02-24T16:17:47.000Z"
}
```

<br><br>

[[Top]](#contents)

<br><br><br>

## Response 더미데이터 생성

일반적으로 앱개발을 하고 있을 때,  
서버가 작업이 되어있지 않은 경우가 많다. 

그래서 약속된 데이터를 미리 모델링하여 작업을 진행할 수 있다.  
위 과정에서 수신한 Response를 문자열로 저장한다.  

<br>

```swift
let dummyData = """
{
    "id": 1,
    "title": "정당의 목적이나 활동이 민주적 기본질서에 위배될 때에는 정부는 헌법재판소에 그 해산을 제소할 수 있고, 정당은 헌법재판소의 심판에 의하여 해산된다.",
    "content": "모든 국민은 인간으로서의 존엄과 가치를 가지며, 행복을 추구할 권리를 가진다. 모든 국민은 종교의 자유를 가진다. 국가는 농·어민과 중소기업의 자조조직을 육성하여야 하며, 그 자율적 활동과 발전을 보장한다. 모든 국민은 양심의 자유를 가진다. 누구든지 체포 또는 구속을 당한 때에는 즉시 변호인의 조력을 받을 권리를 가진다.",
    "createdAt": "2019-02-24T16:17:47.000Z",
    "updatedAt": "2019-02-24T16:17:47.000Z",
    "UserId": 1
}
"""

```

<br>

이제 이 문자열을 앱에서 사용해야할 형태로 만들어주어야야한다.  

이 더미 데이터 문자열을 Data로 변경하고,  사용할 구조체를 정의해서 변경할 것이다. 

이 때, 키값들을 모두 사용할 필요는 없고,  사용할 정보만 정의해서 가져올 수 있다.  

<br>

```swift
struct Article {
    let id: Int
    let title, content, createdAt, updatedAt: String
    let userID: Int
    
    enum CodingKeys: String, CodingKey {
        case id, title, content, createdAt, updatedAt
        case userID = "UserId"
    }
}

let dummyData = """
{
    "id": 1,
    "title": "정당의 목적이나 활동이 민주적 기본질서에 위배될 때에는 정부는 헌법재판소에 그 해산을 제소할 수 있고, 정당은 헌법재판소의 심판에 의하여 해산된다.",
    "content": "모든 국민은 인간으로서의 존엄과 가치를 가지며, 행복을 추구할 권리를 가진다. 모든 국민은 종교의 자유를 가진다. 국가는 농·어민과 중소기업의 자조조직을 육성하여야 하며, 그 자율적 활동과 발전을 보장한다. 모든 국민은 양심의 자유를 가진다. 누구든지 체포 또는 구속을 당한 때에는 즉시 변호인의 조력을 받을 권리를 가진다.",
    "createdAt": "2019-02-24T16:17:47.000Z",
    "updatedAt": "2019-02-24T16:17:47.000Z",
    "UserId": 1
}
"""
```


<br><br>

[[Top]](#contents)

<br><br><br>


### CodingKey
API를 통해 수신한 값을 구조체로 받기위해서는 키값들을 일치시켜야한다.   

그런데 웹에서 정의한 키값들은 Swift의 컨벤션에 맞지 않는 경우도 많다.  

이럴 땐, CodingKey 를 이용하면 내가 원하는 변수명으로 변경을 할 수가 있다.  

구조체를 모두 원하는 형태로 구현하고 enum CodingKeys를 구현하여 아래와 같은 형태로 구현한다.  

`case 변경후 사용할 키값 = "변경 전 키값"`

이형태로 아래와 같이 매칭하여 구조체를 구현한다.  

키값이 다르게 작성되면 변환시 에러가 발생한다.  
`error: The data couldn’t be read because it is missing.`


<br>

```swift
struct Article {
    let id: Int
    let title, content, createdAt, updatedAt: String
    let userID: Int // 변경 후 사용할 변수명
    
    enum CodingKeys: String, CodingKey {
        case id, title, content, createdAt, updatedAt
        case userID = "UserId"  // 새로운 변수명에 변경 전 키값인 UserId을 매칭한다는 뜻 
    }
}
```

<br><br>

[[Top]](#contents)

<br><br><br>


## 더미데이터로부터 데이터가져오기
위에서 생성한 dummyData는 문자열 일 뿐이고, 우리가 사용할 데이터는 Struct로 변환해서 사용하려고 한다.  

바로 문자열에서 Struct로 변환은 안되고,  Data 에서 Struct로 변환이 가능하다.  
그렇기 때문에 String 타입 dummyData를 아래와 같이 Data로 변환한다.   

> data(using:)메서드는 String이라는 구조체에 String protocol에 들어있는 메서드이다.  
> API에서 사용하는 데이터 변환 방식은 주로 utf8형식을 사용한다.  

```swift
guard let convertedData =  dummyData.data(using: .utf8) else { return }
```

<br><br>

[[Top]](#contents)

<br><br><br>

## Codable을 사용하여 변환된 데이터를 구조체로 변환하기
기존의 만들어둔 더미데이터(데이터형태로 변환됨)를  
앱에서 사용할 수 있도록 구조체로 가공하는 과정이다.   

```swift
let title = dict["title"]
let address = dict["address"]
```

<br>


과거에는 JSON 내부에 존재하는 키값들을 일일히 코드로 키값을 선언해서 꺼내 사용했지만,  
Codable을 사용하면 훨씬 보수성이 좋고 가독성 좋게 작업이 가능하다.  

기존의 구현한 모델 구조체에 Codable 프로토콜을 채택한다.  
Codable 프로토콜을 살펴보면 Encodable & Decodable 을 캡슐화한 것을 알 수 있다.  

<br>


```

struct Article: Codable {
    let id: Int
    let title, content, createdAt, updatedAt: String
    let userID: Int
    
    enum CodingKeys: String, CodingKey {
        case id, title, content, createdAt, updatedAt
        case userID = "UserId"
    }
}
```

<br>

JSONDecoder()의 decode 메서드를 이용해 집어넣을 그릇인 `구조체.self`와 `가공할 대상 data`를 넣어준다.  

이 때, 이 작업은 실패할 수 있기 때문에  swift 자체에서 do catch, try 를 사용하라고 안내한다. 

<br>


```
// 원본 데이터
guard let convertedData =  dummyData.data(using: .utf8) else { return }

do {
    let decodedResponse = try JSONDecoder().decode(Article.self, from: convertedData)
    data.append(decodedResponse.title)
} catch {
    print("error: \(error.localizedDescription)")
}

```

<br><br>

[[Top]](#contents)

<br><br><br>


### 전체코드

```

struct Article: Codable {
    let id: Int
    let title, content, createdAt, updatedAt: String
    let userID: Int
    
    enum CodingKeys: String, CodingKey {
        case id, title, content, createdAt, updatedAt
        case userID = "UserId"
    }
}


struct ContentView: View {
    
    @State var data: [String] = ["A", "B"]
    
    var body: some View {
        VStack {
            List { 
                ForEach(data, id: \.self) { item in
                    Text(item)
                }
            }
        }
        
        Button {
            // 버튼 액션
            requestData()
        } label: {
            Text("Append")
        }
    }
    
    func requestData() {
        // String -> Data 변환
        guard let convertedData =  dummyData.data(using: .utf8) else { return }
        
        do {
            // codable을 이용하여 Article 구조체로 변환
            let decodedResponse = try JSONDecoder().decode(Article.self, from: convertedData)
            // 변환된 데이터 추가
            data.append(decodedResponse.title)
        } catch {
            print("error: \(error.localizedDescription)")
        }
    }
}
```

<br><br>

### 동작

  <img width="300" alt="img1 daumcdn-4" src="https://github.com/isGeekCode/TIL/assets/76529148/e95c28e7-6c33-4b8f-ab72-14dc3a311c64">  

<br><br>

[[Top]](#contents)

<br><br><br>

## URLSession을 이용한 Request
앞에서는 더미데이터를 이용해 Response를 처리하였다.  

이제 서버로 보낼 Request를 구현하자.  

- 구조체 경로 생성
- 세션 구현
    - task 작성
    - task 실행

<br>

Apple에서 미리 구현해둔 URLSession 싱글톤을 가져온다.  

이 싱글톤이 가진 `dataTask(with:)` 라는 메서드를 이용한다.  

파라미터로는 `URL`이 들어갈 수도 있고, `URLRequest`가 들어가는 경우도 있다.  

GET방식이라면 두가지 방식 모두 사용가능하지만,  
POST방식이라면 반드시 URLRequest를 사용해야한다.  

여기선 GET방식이기 떄문에 URL을 생성해서 파라미터로 사용한다.  

<br>

```
    let endPoint = "https://koreanjson.com/posts/1"
    
    // 문자열 그대로의 경로를 사용하도록 구조체 URL로 변환
    guard let url = URL(string: endPoint) else { return }
    
    // 싱글톤 URLSession 가져오기
    let session = URLSession.shared
    
    // 업무 정의
    let task = session.dataTask(with: url) { data, response, error in
        // 수신한 Data, URLResponse, Error 체크 후 업무 정의
    }
    
    // 업무 실행
    task.resume()
```

<br>

dataTask(with:) 메서드는 Data?, URLResponse?, Error? 세가지 타입으로 반환한다.  

이것들이 각각 존재할지 모르기 때문이다.  

비동기적으로 통신한 결과를 옵셔널 타입으로 가져온다.  

그래서 일반적으로는 1. 에러체크 2. response 체크 3. 데이터 체크 4. 데이터 가공
순으로 작업을 정의한다.  
<br>

```
// 업무 정의
let task = session.dataTask(with: url) { data, response, error in

    // 에러 여부 체크
    if let _ = error { return }
    
    // 응답 성공 체크
    guard let response = response as? HTTPURLResponse, response.statusCode == 200 else { return }
    
    // 데이터 여부 체크
    guard let data = data else { return }
    
    
    // 더미데이터 대신 실제 data로 Codable처리
    do {
        let decodedResponse = try JSONDecoder().decode(Article.self, from: data)
        print("decodedResponse:\(decodedResponse)")
    } catch {
        print("error: \(error.localizedDescription)")
    }
}

// 정의한 업무 실행
task.resume()
```


<br><br>


### 전체코드

```swift
func requestArticle() {
    let endPoint = "https://koreanjson.com/posts/1"
    
    // 문자열 그대로의 경로를 사용하도록 구조체 URL로 변환
    guard let url = URL(string: endPoint) else { return }
    
    // 싱글톤 URLSession 가져오기
    let session = URLSession.shared
    
    // 업무 정의
    let task = session.dataTask(with: url) { data, response, error in
    
        if let _ = error { return }
        
        guard let response = response as? HTTPURLResponse, response.statusCode == 200 else { return }
        
        guard let data = data else { return  }
        
        
        // 더미데이터 대신 실제 data로 Codable처리
        do {
            let decodedResponse = try JSONDecoder().decode(Article.self, from: data)
            print("decodedResponse:\(decodedResponse)")
        } catch {
            print("error: \(error.localizedDescription)")
        }
    }
    
    // 정의한 업무 실행
    task.resume()
}
```
<br><br>

[[Top]](#contents)

<br><br><br>


## escaping closure
네트워킹 작업은 클라이언트(내 컴퓨터 혹은 핸드폰)만 하는 작업이 아닌,  서버 컴퓨터 뿐 아니라 네트워크 환경에 따라 얼마든지 속도에 영향을 받을 수 있다.  

그렇기 때문에 탑다운 방식으로 코드를 읽어나가는 내 앱의 속도에 맞춰서  결과를 보장하지 못한다.  
그래서 사용하는 것이 @escaping 이다.  탈출 클로저라고도 부른다.  

swift에서는 함수의 파라미터로 () -> () 이렇게 클로저를 넣을 수 가 있다.  

먼저 가볍게 클로저를 살펴보자.  

<br>


```swift

var closure: () -> () = {
    print("Test")
}

closure() // Test

closure = { 
    print("test2")
}

closure() //test2

```

<br>


위와 같은 것을 클로저 라고 부른다.  
그리고 우리가 흔하게 사용하는 func 또한 클로저의 일종이다.  
클로저는 이름이 없는 클로저와 이름이 있는 클로저(일반적인 함수)로 나뉘는 것이다.  

swift에서는 함수의 파라미터로 () -> () 이렇게 클로저를 넣을 수 가 있다.  

<br>


```swift
// 기본적인 형태
func someMethod() { }

// 기본적인 형태
func someMethod(num: Int) { }

// 파라미터로 클로저를 넣는 형태
func someClosure(completion: () -> ()) {
    completion()
}

```

<br>


좀더 클로저를 살펴보자. 

파라미터로 클로저를 넣는 경우에는,  
함수 내부에서 해당 클로저를 구현해줘야한다.  여기서는 completion이라는 파라미터 명으로 사용하였다.  

선언부에서는 completion() 까지 넣어주어야 클로저까지 동작한다.  

<br>


```swift
// 파라미터로 String을 받는 클로저를 넣는 형태
func someClosure(num: Int, completion: (String) -> ()) {
    completion()
}
```
 
 <br>

 
클로저의 파라미터가 있다면 in 키워드 앞에 파라미터가 들어온다.  

파라미터의 갯수에 따라 `a, b in` 이런식으로 표현할 수 있고, in 키워드를 지우고 `$0` 처럼 사용도 가능하다. 키워드 갯수에 따라 `$0, $1` 처럼 사용 가능하다. 


<br>


```swift
// 파라미터로 String을 받는 클로저를 넣는 형태
func someClosure(num: Int, completion: (String) -> ()) {
    
    let numString = num as? String
    completion(numString)
}

// 위의 경우 사용할 때, 아래와 두 경우와 같이 사용할 수 있다.  
// 1. 파라미터 내부에 클로저 구현
someClosure(num: 4, completion: { str in
    print("str의 값은: \(str)")
})
// 동일
someClosure(num: 4, completion: { 
    print("str의 값은: \($0)")
})


// 2. 가장 마지막 파라미터로 클로저가 오는 경우, 
someClosure(num: 3) { str in
    print("str의 값은: \(str)")
}
// 동일
someClosure(num: 3) { 
    print("str의 값은: \($0)")
}


func someClosure(num: Int, completion: @escaping() -> ()) {
    // 파라미터로 탈출클로저를 넣는 형태
}

```

<br>


위와 같이 다양한 방법으로 함수를 구현할 수 있다.  

@escaping를 사용하면 해당 함수의 클로저가 함수범위를 벗어나도,  

해당 값을 붙잡고 있게 된다.  
비동기 작업이 완료되면 외부에서 해당 값을 처리할 수 있게 되는 것이다. 


<br><br>

### Escaping을 이용한 Response 호출
이제 네트워킹이 완료되는 데로 결과를 가져올 함수를 구현해 보자.  

메서드에 `completion: @Escaping (Article?) -> ()`파라미터를 추가하고

통신 결과 처리후 completion에 Article을 넣어주면 된다.  

가령 여러가지 에러들로 인해 Article이 들어가지 못하는 상황도 있다.  

그렇기 떄문에 옵셔널로 처리해준다.    

<br>

```swift

// 성공하는 부분
let decodedResponse = try JSONDecoder().decode(Article.self, from: data)
completion(decodedResponse)

// 실패하는 부분
completion(nil)
```

<br>

성공 여부에 따라 위와 같이 처리하면 되는 것이다.  

<br>

```swift
func requestArticle(completion: @escaping (Article?) -> ()) {
    let endPoint = "https://koreanjson.com/post2s/1"
    
    // 문자열 그대로의 경로를 사용하도록 구조체 URL로 변환
    guard let url = URL(string: endPoint) else { return }
    
    // 싱글톤 URLSession 가져오기
    let session = URLSession.shared
    
    // 업무 정의
    let task = session.dataTask(with: url) { data, response, error in
    
        if let _ = error { return }
        
        guard let response = response as? HTTPURLResponse, response.statusCode == 200 else { return }
        
        guard let data = data else { return  }
        
        
        do {
            let decodedResponse = try JSONDecoder().decode(Article.self, from: data)
            completion(decodedResponse)
        } catch {
            completion(nil)
        }
    }
    
    // 정의한 업무 실행
    task.resume()
}

```

<br>

이제 정의한 requestArticle을 사용해보자.  

requestArticle에서는 Article? 타입으로 파라미터를 가져오고 있다.  

<br>

```swift

func requestData() {

    // requestArticle의 결과값인 article 을 체크
    requestArticle { article in
        if let article = article {
            // 데이터가 있는 경우 로직
            data.append(article.title)
        } else {
            // 데이터가 없는 경우
            print("data is nil")
        }
    }
}

```


<br>

### 전체코드

```swift
// 선언하는 부분
func requestArticle(completion: @escaping (Article?) -> ()) {
    let endPoint = "https://koreanjson.com/post2s/1"
    
    // 문자열 그대로의 경로를 사용하도록 구조체 URL로 변환
    guard let url = URL(string: endPoint) else { return }
    
    // 싱글톤 URLSession 가져오기
    let session = URLSession.shared
    
    // 업무 정의
    let task = session.dataTask(with: url) { data, response, error in
    
        if let _ = error { return }
        
        guard let response = response as? HTTPURLResponse, response.statusCode == 200 else { return }
        
        guard let data = data else { return  }
        
        
        do {
            let decodedResponse = try JSONDecoder().decode(Article.self, from: data)
            completion(decodedResponse)
        } catch {
            completion(nil)
        }
    }
    
    // 정의한 업무 실행
    task.resume()
}

// 사용하는 부분
func requestData() {

    // requestArticle의 결과값인 article 을 체크
    requestArticle { article in
        if let article = article {
            data.append(article.title)
        } else {
            print("data is nil")
        }
    }
}
```


<br><br>

[[Top]](#contents)

<br><br><br>


## Error 타입 사용하기
기존의 completion 타입을 Article뿐아니라 에러에 대한 메세지를 넣기도 한다. 
어디서 에러가 났는지 모르기에 각각 에러가 나는 부분에 대한 문자열을 정의해서 사용할 수 있다. 

<br>

```swift
    func requestData() {
        requestArticle { article, error in
            if let error = error {
                print(error)
            }
            
            if let article = article {
                data.append(article.title)
            }
        }
    }
    
    func requestArticle(completion: @escaping (Article?, String?) -> ()) {
        let endPoint = "https://koreanjson.com/posts/1"
        
        // 문자열 그대로의 경로를 사용하도록 구조체 URL로 변환
        guard let url = URL(string: endPoint) else {
            completion(nil, "This is not correct url")
            return }
        
        // 싱글톤 URLSession 가져오기
        let session = URLSession.shared
        
        // 업무 정의
        let task = session.dataTask(with: url) { data, response, error in
        
            if let _ = error {
                completion(nil, "We got some errror. check the internet")
                return 
            }
            
            guard let response = response as? HTTPURLResponse, response.statusCode == 200 else {
                completion(nil, "Invalid response")
                return 
            }
            
            guard let data = data else {
                completion(nil, "the data received is wrong")
                return 
            }
            
            
            do {
                let decodedResponse = try JSONDecoder().decode(Article.self, from: data)
                completion(decodedResponse, nil)
                
            } catch {
                print("error: \(error.localizedDescription)")
            }
        }
        
        // 정의한 업무 실행
        task.resume()
    }

```

<br>

그런데 에러는 여러 곳에서 발생할 수도 있기 때문에 발생 위치마다 문자열로 넣어준다면,  
어떤 에러들이 있는지 파악이 어려울 수 있고, 관리도 어렵고, 가독성도 떨어질 수 있다.  

이를 위해 Error 타입을 사용할 수 있다.  기본적인 Error 타입을 사용할 수도 있고, 커스텀 enum을 만들어서 사용할 수 도 있다.  

사용한 error 메세지를 모아보자.  

- This is not correct url
- We got some errror. check the internet
- Invalid response
- the data received is wrong


이제 이 에러들을 enum으로 정리해보자.  

```swift
enum NetworkError: Error {
    case invalidURL
    case badConnection
    case invalidResponse
    case invalidData
    
    var errorMessage: String {
        switch self {
        case .invalidURL:
            return "This is not correct url"
        case .badConnection:
            return "We got some errror. check the internet"
        case .invalidResponse:
            return "Invalid response"
        case .invalidData:
            return "the data received is wrong"
        }
    }
}

```

<br>


이렇게 만든 커스텀 에러타입을 Completion에 정의하고,  담아준다.  
NetworkError 타입은 Error타입이기 때문에 Error타입으로 정의해줘도 상관없다.  

```swift
//    String? ->  NetworkError? 
//    func requestPost(completion: @escaping (Posts?, String?) -> ()) {

    func requestPost(completion: @escaping (Posts?, NetworkError?) -> ()) {
        let endPoint = "https://koreanjson.com/posts/1"
        
        // 문자열 그대로의 경로를 사용하도록 구조체 URL로 변환
        guard let url = URL(string: endPoint) else {
            completion(nil, .invalidURL)
            return
        }
        
        // 싱글톤 URLSession 가져오기
        let session = URLSession.shared
        
        // 업무 정의
        let task = session.dataTask(with: url) { data, response, error in
        
            if let _ = error {
                completion(nil, .badConnection)
                return 
            }
            
            guard let response = response as? HTTPURLResponse, response.statusCode == 200 else {
                completion(nil, .invalidResponse)
                return 
            }
            
            guard let data = data else {
                completion(nil, .invalidData )
                return 
            }
            
            
            do {
                let decodedResponse = try JSONDecoder().decode(Posts.self, from: data)
                completion(decodedResponse, nil)
                
            } catch {
                print("error: \(error.localizedDescription)")
            }
        }
        
        // 정의한 업무 실행
        task.resume()
    }
    
    func requestPostData() {
        requestPost { post, error in
            if let error = error {
                print(error.errorMessage)
            }
            if let post = post {
                data.append(post.title)
            }
        }
    }
}

```

<br>

이제 Error관리가 손쉬워졌다.  


<br><br>

[[Top]](#contents)

<br><br><br>


## 커스텀 Result 만들어 사용하기

Completion을 통해 여러 파라미터를 내보낼 수 있다는 걸 알게됐다.  

하지만 앞서 선언한 completion들을 보면
`func requestPost(completion: @escaping (Posts?, NetworkError?) -> ())`
이런식으로 Completion이 작성되어있다.  

- completion(nil, .badConnection)
- completion(nil, .invalidResponse)
- completion(decodedResponse, nil)

이런 식으로 Completion 을 넣어주려면 어떤건 nil을 넣고, 어떤 건 값을 넣어주며 복잡해질 수 있다.  

이런 가독성을 위해 사용하는 것이 Result 타입이다.  

```swift
enum MyResult {
    case success(data: Posts)
    case failure(error: NetworkError)
}
```

어차피 결과에는 성공하면 특정 데이터, 실패하면 NetworkError 타입이 들어오기 때문에  
위와 같이 정의할 수 있다.  

그러면 성공인지 실패인지에 따라 enum에서 정한 타입을 넣어줄 수 있다.  

```swift
// 코드 사용
func requestPostData() {
    requestPost { result in
        switch result {
        case .success(data: let post):
            data.append(post.title)
        case .failure(error: let error):
            switch error {
            case .invalidURL:
                print("URL이 유효하지 않은 얼럿 띄우기")
            case .badConnection:
                print("badConnection 얼럿 띄우기")
            default: 
                print("알 수 없는 에러처리")
            }
        }
    }
}


// 코드 정의
func requestPost(completion: @escaping (MyResult) -> ()) {
    let endPoint = "https://koreanjson.com/posts/1"
    
    // 문자열 그대로의 경로를 사용하도록 구조체 URL로 변환
    guard let url = URL(string: endPoint) else {
        completion(.failure(error: .invalidURL))
        return
    }
    
    // 싱글톤 URLSession 가져오기
    let session = URLSession.shared
    
    // 업무 정의
    let task = session.dataTask(with: url) { data, response, error in
    
        if let _ = error {
            completion(.failure(error: .badConnection))
            return 
        }
        
        guard let response = response as? HTTPURLResponse, response.statusCode == 200 else {
            completion(.failure(error: .invalidResponse))
            return 
        }
        
        guard let data = data else {
                completion(.failure(error: .invalidData))
            return 
        }
        
        
        do {
            let decodedResponse = try JSONDecoder().decode(Posts.self, from: data)
                completion(.success(data: decodedResponse))
            
        } catch {
            print("error: \(error.localizedDescription)")
        }
    }
    
    // 정의한 업무 실행
    task.resume()
}
```

<br><br>

[[Top]](#contents)

<br><br><br>

## Generic으로 유동적인 메서드 만들기

사실 위에서 만든 MyResult는 Result 타입을 모방한 형태일 뿐이다.  
실제 

### 새로운 request
    requestArticle 메서드는 https://koreanjson.com/posts/1 경로를 이용해 get형식으로 받아오는 메서드였다.  
    
        여기에 https://koreanjson.com/users/1 경로를 이용하여 비슷한 메서드를 만들어보자.  
    
    버튼은 새로운 버튼을 생성해보자.  

### Users Codable모델 구현
기존의 모델은 Posts로 바꾸고, Users도 구현해보자. 



```swift
struct Users: Codable {
    let id: Int
    let name, userName, email, phone, website, province, city, district, street, createdAt, updatedAt: String
    
    enum CodingKeys: String, CodingKey {
        case id, name, email, phone, website, province, city, district, street, createdAt, updatedAt
        case userName = "username"
    }
}

```


```swift

// https://koreanjson.com/users/1

func requestUserData() {
    requestUser { result in
        switch result {
        case .success(data: let user):
            data.append(user.city)
        case .failure(error: let error):
            switch error {
            case .invalidURL:
                print("URL이 유효하지 않은 얼럿 띄우기")
            case .badConnection:
                print("badConnection 얼럿 띄우기")
            default: 
                print("알 수 없는 에러처리")
            }
        }

func requestUser(completion: @escaping (UserResult) -> ()) {
    let endPoint = "https://koreanjson.com/users/1"
    
    // 문자열 그대로의 경로를 사용하도록 구조체 URL로 변환
    guard let url = URL(string: endPoint) else {
        completion(.failure(error: .invalidURL))
        return
    }
    
    // 싱글톤 URLSession 가져오기
    let session = URLSession.shared
    
    // 업무 정의
    let task = session.dataTask(with: url) { data, response, error in
    
        if let _ = error {
            completion(.failure(error: .badConnection))
            return 
        }
        
        guard let response = response as? HTTPURLResponse, response.statusCode == 200 else {
            completion(.failure(error: .invalidResponse))
            return 
        }
        
        guard let data = data else {
            completion(.failure(error: .invalidData))
            return 
        }
        
        
        do {
            let decodedResponse = try JSONDecoder().decode(Users.self, from: data)
            completion(.success(data: decodedResponse))
        } catch {
            print("error: \(error.localizedDescription)")
        }
    }
    
    // 정의한 업무 실행
    task.resume()
}

enum UserResult {
    case success(data: Users)
    case failure(error: NetworkError)
}


```




<br><br>

[[Top]](#contents)

<br><br><br>


[ ](https://www.youtube.com/watch?v=u2sSdwxu2R0&t=302s)


## History
- 240313 : 기본 앱 추가, 더미데이터, Response Model구현, CodingKey구현
- 240314 : Codable, URLSession, escaping, error타입
