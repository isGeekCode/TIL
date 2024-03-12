# iOS에서 JSON다루기(1): Encode JSONData

- 참고링크
    - [TIL: 직렬화(Serialization)](https://github.com/isGeekCode/TIL/blob/main/ComputerScience/Serialization.md)
    - [TIL: Foundation - JSONSerialization 직렬화하기](https://github.com/isGeekCode/TIL/blob/main/iOS-Foundation/Foundation_JSONSerialization.md)
    - [TIL: iOS에서 JSON다루기(2): Decode JSONData](https://github.com/isGeekCode/TIL/blob/main/iOS-Foundation/Foundation_JSONSerialization_Decode.md)
    - [TIL: Swift - Codable 다루기](https://github.com/isGeekCode/TIL/blob/main/iOS-Lang-Swift/Codable.md)


iOS에서 직렬화를 하는 방법은 아래 세가지가 있다.
- [문자열로 JSONData만들기](#문자열로-JSONData만들기)
- [JSONSerialization을 이용해 JSONData만들기](#JSONSerialization을-이용해-JSONData만들기)
- [Codable을 이용해 JSONData만들기](#Codable을-ㄴ이용해-JSONData만들기)

+++  
  
여기에 추가로   

- [복잡한 구조를 3가지 방법으로 비교해보기](#복잡한-구조를-3가지-방법으로-비교해보기)

위 내용을 좀더 세부적으로 나눠보면 아래와 같다.

- String protocol을 이용해 JSONData만들기
- JSONSerialization을 이용해 JSONData만들기
    - Dictionary 타입으로 JSONData만들기
    - Array 타입으로 JSONData만들기
    - Dictionary / Array 를 혼합하여 JSONData만들기
- Codable protocol을 이용해 JSONData만들기
    - 객체를 Codable을 이용해서 JSONData만들기
    - 복잡한 데이터 구조를 가진 객체를 Codable을 이용해서 JSONData만들기


<br><br>

## 직렬화하기 

### 문자열로 JSONData만들기
`$0.data(using: .utf8)`메서드에 대한 자세한 설명은 상단 참고링크 참고

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

<br><br>

- [[TOP]](#iOS에서-JSON다루기)

<br><br>

### JSONSerialization을 이용해 JSONData만들기
`JSONSerialization.data(withJSONObject:options:)`메서드에 대한 자세한 설명은 상단 참고링크 참고

```swift
let param = param

JSONSerialization.data(withJSONObject: param, options: .prettyPrinted
```

** 자세한 코드 **

```swift
// MARK: Create JSONData(1) Dictionary
let dictionary: [String : Any] = [
    "name": "John Doe",
    "age": 30,
    "email": "johndoe@example.com"
]

do {
    try JSONSerialization.data(withJSONObject: dictionary, options: .prettyPrinted)
} catch {
    print("Error during JSON serialization: \(error)")
}

// MARK: Create JSONData(2) Array
let array = ["apple", "banana", "orange"]

do {
    try JSONSerialization.data(withJSONObject: array, options: .prettyPrinted)
} catch {
    print("Error during JSON serialization: \(error)")
}


// MARK: Create JSONData(3) Dictionary and Array

let dictionary: [String : Any] = [
    "name": "John Doe",
    "age": 30,
    "email": "johndoe@example.com",
    "fruits": ["apple", "banana", "orange"]
]

do {
    try JSONSerialization.data(withJSONObject: dictionary, options: .prettyPrinted)
} catch {
    print("Error during JSON serialization: \(error)")
}

```
아주 복잡한 구조는 하단 참고

<br><br>

- [[TOP]](#iOS에서-JSON다루기)

<br><br>

### Codable을 이용해 JSONData만들기

`JSONEncoder().encode()`메서드에 대한 자세한 설명은 상단 참고링크 참고  

```swift
//코더블할 객체 구현
struct User: Codable {
    let currentPage: String
    let pageSize: String
    let searchOpt: String
    let searchText: String
}

// 
let user = User(
    currentPage: "1",
    pageSize: "2",
    searchOpt: "1",
    searchText: ""
)
let encodableData = try JSONEncoder().encode(user)

```

- [[TOP]](#iOS에서-JSON다루기)

<br><br>

## 복잡한 구조를 3가지 방법으로 비교해보기

만들고 싶은 결과값은 이거다.
```swift
{
    "name": "ABC Company",
    "address": "123 Main St",
    "employees": [
        {
            "name": "John Doe",
            "age": 30,
            "email": "johndoe@example.com"
        },
        {
            "name": "Jane Smith",
            "age": 28,
            "email": "janesmith@example.com"
        }
    ]
}

```
위에서 소개한 3가지 방법으로 모두 살펴보자

### create JSON Data Using String Protocol

```swift
// 예제 JSON 데이터
let jsonString = """
    {
        "name": "ABC Company",
        "address": "123 Main St",
        "employees": [
            {
                "name": "John Doe",
                "age": 30,
                "email": "johndoe@example.com"
            },
            {
                "name": "Jane Smith",
                "age": 28,
                "email": "janesmith@example.com"
            }
        ]
    }
"""

// 예제용 JSON 데이터 생성완료
let jsonData = jsonString.data(using: .utf8)
```

<br>
<br>

### create JSON Data Using JSONSerialization

```swift

struct Company {
    let name: String
    let address: String
    let employees: [Employee]
}

struct Employee {
    let name: String
    let age: Int
    let email: String
}

// 예제 데이터 생성
let company = Company(
    name: "ABC Company",
    address: "123 Main St",
    employees: [
        Employee(name: "John Doe", age: 30, email: "johndoe@example.com"),
        Employee(name: "Jane Smith", age: 28, email: "janesmith@example.com")
    ]
)

// 구조체를 딕셔너리로 변환
let companyDict: [String: Any] = [
    "name": company.name,
    "address": company.address,
    "employees": company.employees.map { [
        "name": $0.name,
        "age": $0.age,
        "email": $0.email
    ]}
]

// JSONSerialization을 사용하여 Data로 변환
do {
    let jsonData = try JSONSerialization.data(withJSONObject: companyDict, options: [])
    
    
    // 여기에 jsonData를 사용할 수 있습니다. 예를 들어, 인코딩된 JSON 문자열을 출력하려면:
    if let jsonString = String(data: jsonData, encoding: .utf8) {
        print(jsonString)
    }
} catch {
    print("Serialization failed with error: \(error)")
}

```

<br>
<br>

### create JSON Data Using Codable Protocol

```swift

struct Company: Codable {
    let name: String
    let address: String
    let employees: [Employee]
}

struct Employee: Codable {
    let name: String
    let age: Int
    let email: String
}

// 예제 데이터 생성
let company = Company(
    name: "ABC Company",
    address: "123 Main St",
    employees: [
        Employee(name: "John Doe", age: 30, email: "johndoe@example.com"),
        Employee(name: "Jane Smith", age: 28, email: "janesmith@example.com")
    ]
)

// JSONEncoder를 사용하여 Encodable 구조체를 Data로 인코딩
let encoder = JSONEncoder()
do {
    let encodableData = try encoder.encode(company)
    
    // 여기에 encodableData를 사용할 수 있습니다. 예를 들어, 인코딩된 JSON 문자열을 출력하려면:
    if let jsonString = String(data: encodableData, encoding: .utf8) {
        print(jsonString)
    }
} catch {
    print("Encoding failed with error: \(error)")
}

```

<br><br><br>

## History
- 230802 : 초안작성
- 230803 : JSONSerialization 링크 연결
- 230803 : Codable 링크 연결
