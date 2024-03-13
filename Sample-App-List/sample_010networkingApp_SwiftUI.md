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
- [API 소개](#API-소개)
- [Response 더미데이터 생성](#Response-더미데이터-생성)
    - [CodingKey](#CodingKey)
    
    
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

```swift
struct Article {
    let id: Int
    let title, content, createdAt, updatedAt: String
    let UserID: Int
    
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

<br>

```swift
struct Article {
    let id: Int
    let title, content, createdAt, updatedAt: String
    let UserID: Int // 변경 후 사용할 변수명
    
    enum CodingKeys: String, CodingKey {
        case id, title, content, createdAt, updatedAt
        case userID = "UserId"  // 새로운 변수명에 변경 전 키값인 UserId을 매칭한다는 뜻 
    }
}
```

<br><br>

[[Top]](#contents)

<br><br><br>

[ ](https://www.youtube.com/watch?v=u2sSdwxu2R0&t=302s)

## History
- 240313 : 기본 앱 추가, 더미데이터, Response Model구현, CodingKey구현
