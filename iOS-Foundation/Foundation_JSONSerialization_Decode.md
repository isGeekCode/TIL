# iOS에서 JSON다루기(2): Decode JSONData

- 참고링크
    - [TIL: 직렬화(Serialization)란](https://github.com/isGeekCode/TIL/blob/main/ComputerScience/Serialization.md)
    - [TIL: JSONSerialization으로  직렬화하기](https://github.com/isGeekCode/TIL/blob/main/iOS-Foundation/Foundation_JSONSerialization.md)
    - [TIL: Swift - Codable 다루기](https://github.com/isGeekCode/TIL/blob/main/iOS-Lang-Swift/Codable.md)

## 순서
iOS에서 역직렬화를 하는 방법은 아래 세가지가 있다.
- [Data를 문자열로 만들기](#Data를-문자열로-만들기)
- [JSONSerialization로 역직렬화하기](#JSONSerialization로-역직렬화하기)
- [Codable을 이용해 역직렬화하기](#Codable을-이용해-역직렬화하기)

+++  
  
여기에 추가로   

- [복잡한 구조를 3가지 방법으로 비교해보기](#복잡한-구조를-3가지-방법으로-비교해보기)

위 내용을 좀더 세부적으로 나눠보면 아래와 같다.

- String protocol을 이용해 문자열로 만들기
- JSONSerialization로 역직렬화하기
    - Dictionary 타입으로 역직렬화하기
    - Array 타입으로 역직렬화하기
    - Dictionary / Array 혼합타입으로 역직렬화하기
- Codable을 protocol 이용해 역직렬화하기
    - 객체를 Codable을 이용해서 역직렬화하기


<br><br>

## 역직렬화하기 

### Data를 문자열로 만들기
`String(data:encoding:)`메서드에 대한 자세한 설명은 상단 참고링크 참고

```swift
let jsonString = """
    {
        "name": "John Doe",
        "age": 30,
        "email": "johndoe@example.com"
    }
"""
// 예제 Data생성
let stringData = jsonString.data(using: .utf8)

// Data를 다시 String으로 변환
if let convertedString = String(data: stringData!, encoding: .utf8) {
    print(convertedString)
} else {
    print("Failed to convert Data to String.")
}

```

<br><br>

- [[TOP]](#순서)

<br><br>

### JSONSerialization로 역직렬화하기
아래 함수를 통해 역직렬화할 수 있다.
`JSONSerialization.jsonObject(with:options:)`메서드에 대한 자세한 설명은 상단 참고링크 참고

```swift
let jsonData = data

let jsonObject = try JSONSerialization.jsonObject(with: jsonData, options: [])
```

** 자세한 코드 **

Dictionary

```swift
// MARK: Deserialization(1) : Dictionary
// 예제 JSON 데이터
let jsonString = """
    {
        "name": "John Doe",
        "age": 30,
        "email": "johndoe@example.com"
    }
"""
// 예제용 JSON 데이터 생성완료
guard let jsonData = jsonString.data(using: .utf8) else { return }


// Deserialization 시작
do {
    // JSON 데이터를 파싱하여 Swift 객체로 변환
    let jsonObject = try JSONSerialization.jsonObject(with: jsonData, options: [])
    
    // JSON 데이터를 Dictionary 형태로 사용
    if let jsonDictionary = jsonObject as? [String: Any] {
    
        // 데이터 가공 시작
        if let name = jsonDictionary["name"] as? String,
           let age = jsonDictionary["age"] as? Int,
           let email = jsonDictionary["email"] as? String {
            // JSON 데이터를 Swift에서 사용할 수 있는 형태로 변환
            print("Name: \(name), Age: \(age), Email: \(email)")
        }
    }
} catch {
    print("Error during JSON parsing: \(error)")
}

    /*
     Name: John Doe, Age: 30, Email: johndoe@example.com
     */

```

<br><br>

Array  

```swift
// MARK: Deserialization(2) : Array
// 예제 JSON 데이터
let jsonString = """
    [
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
"""
// 예제용 JSON 데이터 생성완료
guard let jsonData = jsonString.data(using: .utf8) else { return }


// Deserialization 시작
do {
    // JSON 데이터를 파싱하여 Swift 객체로 변환
    let jsonObject = try JSONSerialization.jsonObject(with: jsonData, options: [])
    
    // 데이터 가공 시작
    if let jsonArray = jsonObject as? [Any] {
    
    
        // JSON 데이터를 Array 형태로 사용
        for item in jsonArray {
            if let dictionaryItem = item as? [String: Any] {
                if let name = dictionaryItem["name"] as? String,
                   let age = dictionaryItem["age"] as? Int,
                   let email = dictionaryItem["email"] as? String {
                   
                   
                    // JSON 데이터를 Swift에서 사용할 수 있는 형태로 변환
                    print("Name: \(name), Age: \(age), Email: \(email)")
                }
            }
        }
    } else {
        print("Invalid JSON format for Array")
    }

    
} catch {
    print("Error during JSON parsing: \(error)")
}

/*
Name: John Doe, Age: 30, Email: johndoe@example.com
Name: Jane Smith, Age: 28, Email: janesmith@example.com
*/
    

```

<br><br>
Dictionary and Array

```SWIFT
// MARK: JSONData Deserialization(3) - Dictionary and Array
    
// 예제 JSON 데이터
let jsonString = """
    {
        "name": "John Doe",
        "age": 30,
        "email": "johndoe@example.com",
        "fruits": ["apple", "banana", "orange"]
    }
"""

// 예제용 JSON 데이터 생성완료
guard let jsonData = jsonString.data(using: .utf8) else { return }


// Deserialization 시작
do {
    // JSON 데이터를 파싱하여 Swift 객체로 변환
    let jsonObject = try JSONSerialization.jsonObject(with: jsonData, options: [])
    
    if let jsonDictionary = jsonObject as? [String: Any] {
        // JSON 데이터를 Dictionary 형태로 사용
        if let name = jsonDictionary["name"] as? String,
           let age = jsonDictionary["age"] as? Int,
           let email = jsonDictionary["email"] as? String,
           let fruits = jsonDictionary["fruits"] as? [String] {
            // JSON 데이터를 Swift에서 사용할 수 있는 형태로 변환
            print("Name: \(name), Age: \(age), Email: \(email)")
            print("Fruits: \(fruits)")
        }
    } else {
        print("Invalid JSON format")
    }
    
} catch {
    print("Error during JSON parsing: \(error)")
}



/*
 Name: John Doe, Age: 30, Email: johndoe@example.com
 Fruits: ["apple", "banana", "orange"]
 */

```


아주 복잡한 구조는 하단 참고

<br><br>

- [[TOP]](#순서)

<br><br>

### Codable을 이용해 역직렬화하기

`JSONDecoder().decode(_from:)`메서드에 대한 자세한 설명은 상단 참고링크 참고  


```swift
//코더블할 객체 구현
struct Person: Codable {
    let name: String
    let age: Int
    let email: String
}

let decoder = JSONDecoder()
let decodedPerson = try decoder.decode(Person.self, from: jsonData)

/*
Person(name: "John Doe", age: 30, email: "johndoe@example.com")
*/

```

<br><br>

- [[TOP]](#순서)

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

### Using String Protocol

```SWIFT
if let jsonData = jsonString.data(using: .utf8),
   let parsedString = String(data: jsonData, encoding: .utf8) {
    print(parsedString)
} else {
    print("Failed to parse JSON data to String.")
}

/*
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

*/
```


<br><br>

- [[TOP]](#순서)

<br>
<br>

### Using JSONSerialization

```swift
// 저장할 객체 
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


// JSON 데이터 파싱
if let jsonData = jsonString.data(using: .utf8) {
    do {
        if let json = try JSONSerialization.jsonObject(with: jsonData, options: []) as? [String: Any] {
        
        
            
            // Company 객체 생성
            guard let companyName = json["name"] as? String,
                  let address = json["address"] as? String,
                  let employees = json["employees"] as? [[String: Any]] else {
                print("Failed to parse JSON data.")
                return
            }

            // Company 객체에 값 넣어주기
            var companyEmployees: [Employee] = []
            for employeeJSON in employees {
                guard let name = employeeJSON["name"] as? String,
                      let age = employeeJSON["age"] as? Int,
                      let email = employeeJSON["email"] as? String else {
                    print("Failed to parse employee JSON.")
                    continue
                }
                let employee = Employee(name: name, age: age, email: email)
                companyEmployees.append(employee)
            }
            
            let company = Company(name: companyName, address: address, employees: companyEmployees)
            
            // Company 객체와 그 안의 Employee 객체들 출력
            print("Company Name:", company.name)
            print("Address:", company.address)
            
            print("\nEmployees:")
            for employee in company.employees {
                print("Name:", employee.name)
                print("Age:", employee.age)
                print("Email:", employee.email)
                print("---")
            }
        }
    } catch {
        print("Error while parsing JSON: \(error)")
    }
}
```

<br><br>

- [[TOP]](#순서)

<br>
<br>

### Using Codable Protocol

```swift

// 저장할 객체 구현
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

// Deserialization 시작
do {
    let decoder = JSONDecoder()
    let company = try decoder.decode(Company.self, from: jsonData)

    // 객체를 한꺼번에 보여주기
    print("\(company)")
    
    print("Company Name: \(company.name), Address: \(company.address)")
    print("Employees:")
    for employee in company.employees {
        print("Name: \(employee.name), Age: \(employee.age), Email: \(employee.email)")
    }
} catch {
    print("Error during JSON parsing: \(error)")
}

    /*
     company:
     Company(name: "ABC Company", address: "123 Main St", employees: [UIKitApp.ViewController.(unknown context at $107178c8c).(unknown context at $107178d78).Employee(name: "John Doe", age: 30, email: "johndoe@example.com"), UIKitApp.ViewController.(unknown context at $107178c8c).(unknown context at $107178d78).Employee(name: "Jane Smith", age: 28, email: "janesmith@example.com")])

     
     Company Name: ABC Company, Address: 123 Main St
     Employees:
     Name: John Doe, Age: 30, Email: johndoe@example.com
     Name: Jane Smith, Age: 28, Email: janesmith@example.com
     */

```

<br><br>

- [[TOP]](#순서)


<br><br><br>

## History
- 230803 : 초안작성
