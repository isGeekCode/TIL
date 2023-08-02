# Foundation - JSONSerialization 직렬화하기

- 참고링크
    - [TIL: 직렬화(Serialization)](https://github.com/isGeekCode/TIL/blob/main/ComputerScience/Serialization.md)
    - [TIL: Codable 사용하기](#)

iOS의 Foundation 프레임워크에서 제공하는 클래스다.   
JSON 데이터를 파싱하고 JSON객체를 Swift에서 사용할 수 있는 형식으로 변환하는 기능을 제공한다.  

주로 아래와 같은 두가지 주요기능을 수행한다.


- Serialization : Dictionary or Array -> JSON Data
- Deserialization : JSON Data -> Dictionary or Array

간단하게 말해서, 직렬화와 역직렬화를 수행해주는 클래스이다.

일단 직렬화 방법은 아래처럼 세가지의 방법이 있다.
## 순서
- [직렬화하기](#직렬화하기)
    - [Dictionary 타입으로 JSONData만들기](#Dictionay로-JSONData만들기)
    - [Array 타입으로 JSONData만들기](#Array-타입으로-JSONData만들기)
    - [Dictionary / Array를 혼합하여 JSONData만들기](#Dictionary--Array-를-혼합하여-JSONData만들기)
- [역직렬화하기](#역직렬화하기)
    - [Dictionary구조의 JSONData를 역직렬화 하기](#Dictionary구조의-JSONData를-역직렬화하기)
    - [Array구조의 JSONData를 역직렬화 하기](#Array구조의-JSONData를-역직렬화하기)
    - [Dictionary/Array가 혼합된 JSONData를 역직렬화 하기](#DictionaryArray가-혼합된-JSONData를-역직렬화하기)
    - [Dictionary/Array가 혼합, 더 복잡한 JSONData를 역직렬화 하기](#DictionaryArray가-혼합-더-복잡한-JSONData를-역직렬화하기)
    - [Codable이용하여 역직렬화 하기](#-Codable이용하여-역직렬화하기)


<br><br>

## 직렬화하기 

### Dictionay로 JSONData 만들기
- Dictionary 생성
- Dictionary를 JSON데이터로 변환
- JSON데이터를 파싱하여 Foundation 객체로 변환


> Dictionay로 만드는 경우 결과물은 `{}`로 생성된다. 

```swift
func createJSONDataWithDictionary() -> Data? {
    let dictionary = [
        "name": "John Doe",
        "age": 30,
        "email": "johndoe@example.com"
    ]

    do {
        return try JSONSerialization.data(withJSONObject: dictionary, options: .prettyPrinted)
    } catch {
        print("Error during JSON serialization: \(error)")
        return nil
    }
}

// JSONData 완성
guard let jsonData = createJSONDataWithDictionary() else { return }
// 결과를 확인하기위해 JSON 데이터를 String으로 변환
guard let jsonString = String(data: jsonData, encoding: .utf8) else { return }
print("jsonString:\n\(jsonString)")

/*
jsonString:
{
  "email" : "johndoe@example.com",
  "age" : 30,
  "name" : "John Doe"
}
*/
```  
<br>
[[Top]](#순서)


<br><br>

### Array 타입으로 JSONData만들기
> 배열의 경우 결과물도 Array로 생성된다. 

```swift
func createJSONDataWithArray() -> Data? {
    let array = ["apple", "banana", "orange"]

    do {
        return try JSONSerialization.data(withJSONObject: array, options: .prettyPrinted)
    } catch {
        print("Error during JSON serialization: \(error)")
        return nil
    }
}

// JSONData 완성
guard let jsonData = createJSONDataWithArray() else { return }
// 결과를 확인하기위해 JSON 데이터를 String으로 변환
guard let jsonString = String(data: jsonData, encoding: .utf8) else { return }
print("jsonString:\n\(jsonString)")

/*
jsonString:
[
  "apple",
  "banana",
  "orange"
]
*/
```

<br>
[[Top]](#순서)

<br><br>

### Dictionary / Array 를 혼합하여 JSONData만들기

```swift
func createJSONDataWithDictionaryAndArray() -> Data? {
    let dictionary: [String : Any] = [
        "name": "John Doe",
        "age": 30,
        "email": "johndoe@example.com",
        "fruits": ["apple", "banana", "orange"]
    ]

    do {
        return try JSONSerialization.data(withJSONObject: dictionary, options: .prettyPrinted)
    } catch {
        print("Error during JSON serialization: \(error)")
        return nil
    }
}

// JSONData 완성
guard let jsonData = createJSONDataWithDictionaryAndArray() else { return }
// 결과를 확인하기위해 JSON 데이터를 String으로 변환
guard let jsonString = String(data: jsonData, encoding: .utf8) else { return }
print("jsonString:\n\(jsonString)")

/*
jsonString:
{
  "fruits" : [
    "apple",
    "banana",
    "orange"
  ],
  "age" : 30,
  "email" : "johndoe@example.com",
  "name" : "John Doe"
}

*/

```

<br>
[[Top]](#순서)

<br><br><br>
## 역직렬화하기
이것도 마찬가지로 3가지 사례를 보여주려고 한다.

- [Dictionary구조의 JSONData를 역직렬화 하기](#-Dictionary구조의-JSONData를-역직렬화하기)
- [Array구조의 JSONData를 역직렬화 하기](#-Array구조의-JSONData를-역직렬화하기)
- [Dictionary/Array가 혼합된 JSONData를 역직렬화 하기](#-DictionaryArray가-혼합된-JSONData를-역직렬화하기)
- [Dictionary/Array가 혼합, 더 복잡한 JSONData를 역직렬화 하기](#-DictionaryArray가-혼합-더-복잡한-JSONData를-역직렬화하기)
- [Codable이용하여 역직렬화 하기](#-Codable이용하여-역직렬화-하기)

각각의 예제에는 JSONData를 먼저 생성하고 있다.  

실질적으로 역직렬화하는 부분은 한두줄에 불과하다!  

모두 동일하게 아래함수를 사용한다. 
```swift
let jsonObject = try JSONSerialization.jsonObject(with: jsonData, options: [])
```

다만 예제에 JSON의 구조를 먼저 보여주는 이유는  

JSONSerialization을 이용하여 역직렬화(Deserialization)할 때에는 하나씩 일일히 키값을 잡아줘야하기 때문이다.  

그래서 역직렬화 이후, 값을 처리할때 코드가 아주 길어진다.

처음 JSONSerialization 가 나올당시엔 이게 최선이었지만!!!  

Codable을 이용하면 얘기가 다르다.  

그거부터 보고 싶다면 클릭해서 아래로 이동  
- [Codable이용하여 역직렬화 하기](#-Codable이용하여-역직렬화-하기)


<br>
[[Top]](#순서)
<br><br>
### Dictionary구조의 JSONData를 역직렬화 하기
```swift
// MARK: JSONData Deserialization(1) - Dictionary
func deserializationWithDictionary() {
    
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

}
/*
 Name: John Doe, Age: 30, Email: johndoe@example.com
 */

```

<br>
[[Top]](#순서)
<br><br>

### Array구조의 JSONData를 역직렬화 하기
name, age, email의 값을 가지고 있는 element가 두 개 들어있다.

```swift
// MARK: JSONData Deserialization(2) - Array
func deserializationWithArray() {
    
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

}

/*
 Name: John Doe, Age: 30, Email: johndoe@example.com
 Name: Jane Smith, Age: 28, Email: janesmith@example.com
 */
```
<br>
[[Top]](#순서)
<br><br>
### Dictionary/Array가 혼합된 JSONData를 역직렬화 하기
딕셔너리의 한 value 값으로 Array가 들어갔다.  

```swift

// MARK: JSONData Deserialization(3) - Dictionary and Array
func deserializationWithDictionaryAndArray() {
    
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

}

/*
 Name: John Doe, Age: 30, Email: johndoe@example.com
 Fruits: ["apple", "banana", "orange"]
 */

```
<br>
[[Top]](#순서)
<br><br>
### Dictionary/Array가 혼합, 더 복잡한 JSONData를 역직렬화 하기
이번 JSON형태를 보면, Dictionary형태에서 한 value값이  Array 형태를 갖고 있는데 그 내부에 또 Dictionary형태다.

이런 형태인거다.
- Dictionary
    - Array
        - Dictionary

<br>
이번엔 역직렬화를 마치고 struct에 담아보자.   
<br>
```swift

// MARK: JSONData Deserialization(4) - Dictionary and Array more Complex
func deserializationMoreComplex() {
    
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
    guard let jsonData = jsonString.data(using: .utf8) else { return }

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
    
    // Deserialization 시작
    do {
        // JSON 데이터를 파싱하여 Swift 객체로 변환
        if let jsonObject = try JSONSerialization.jsonObject(with: jsonData, options: []) as? [String: Any] {
            // JSON 데이터를 Dictionary 형태로 사용
            if let companyName = jsonObject["name"] as? String,
               let companyAddress = jsonObject["address"] as? String,
               let employeeArray = jsonObject["employees"] as? [[String: Any]] {

                var employees: [Employee] = []
                for employeeData in employeeArray {
                    if let employeeName = employeeData["name"] as? String,
                       let employeeAge = employeeData["age"] as? Int,
                       let employeeEmail = employeeData["email"] as? String {
                        let employee = Employee(name: employeeName, age: employeeAge, email: employeeEmail)
                        employees.append(employee)
                    }
                }

                // 생성한 employee 배열을 Company의 employees Value값으로 넣어준다.
                let company = Company(name: companyName, address: companyAddress, employees: employees)


                // JSON 데이터를 Swift 객체로 변환
                print("Company Name: \(company.name), Address: \(company.address)")
                
                // 요소별로 print하기
                print("Employees:")
                for employee in company.employees {
                    print("Name: \(employee.name), Age: \(employee.age), Email: \(employee.email)")
                }
            } else {
                print("Invalid JSON format")
            }
        } else {
            print("Invalid JSON format")
        }
    } catch {
        print("Error during JSON parsing: \(error)")
    }
}

/*
 Company Name: ABC Company, Address: 123 Main St
 
 Employees:
 Name: John Doe, Age: 30, Email: johndoe@example.com
 Name: Jane Smith, Age: 28, Email: janesmith@example.com
 */

```

<br>
[[Top]](#순서)
<br><br><br>

위에서는 역직렬화 이후 정보를 처리하는게 급격히 복잡해졌다.

원래 이글은 Foundation - JSONSerialization을 소개하는 글이지만,  

아래 내용을 소개해본다. 

### Codable이용하여 역직렬화 하기
위 방법에서는 역직렬화를 모두 한다음 구현한 객체를 만들어줬다.  

Codable은 Codable 프로토콜을 struct에 채택하고,  
아래와 같이 하면된다.  
```SWIFT
let decoder = JSONDecoder()
let company = try decoder.decode(Company.self, from: jsonData)
```
키값으로 일일히 풀지않아도된다. 알아서 미리 구현한 구조체를 따라 들어가서 객체화된다. 

좀더 전체적인 과정을 살펴보자.  

```swift

// MARK: JSONData Deserialization(5) - Dictionary and Array With Codable
func deserializationWithCodable() {
    
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
    guard let jsonData = jsonString.data(using: .utf8) else { return }


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
        // Use JSONDecoder to decode JSON data into Company object
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

<br>
[[Top]](#순서)
<br><br><br>


## History
- 230802 : 초안작성
- 230802 : Codable 사용법 추가
