# Swift - Codable 다루기

Serialize / Deserialize

이 두가지 과정을 간단하게 할수 있도록 만드는 방법이 Codable이다.

Codable은 Serialize / Deserialize 과 대응하는 Encodable / Decodable을 가지고 있는 프로토콜이다.


# 모델링

## 단일계층

아래와 같은 구조의 JSON을 만들기 위해서는 구조체 혹은 클래스로 형성된 모델이 필요하다.

```swift
{   "name" : "Park",   "age" : "100"}
```

### Struct일 경우

```swift
// MARK: - Person
struct Person : Codable {
    var name, age : String
}

```

### Class일 경우

`클래스는 이니셜라이저가 있어야한다.`

```swift
// MARK: - Person
 class Person {
     var name, age, employed: String

     init(name: String, age: String, employed: String) {
         self.name = name
         self.age = age
         self.employed = employed
     }
 }
```

이렇게 클래스 혹은 구조체를 뼈대로 삼아 여러개의 객체를 만들수가 있다.

이것을 모델링이라고 한다.

그리고 이 모델들을 이용해 JSON으로 Serialize를 할수있다.

## 상위계층

만약 여러개의 모델을 한꺼번에 사용한다면 상위계층이 만들어야 할때가 있다. 각각 Person객체가 들어간 구조를 추가한다면 아래와 같다.

### struct일경우

```swift
// MARK: - PersonModel
struct PersonModel : Codable {
    var person: [Person]
}

// MARK: - Person
struct Person : Codable {
    var name, age : String
}
```

### class일경우

```swift
// MARK: - PersonModel
 class PersonModel {
     var person: [Person]

     init(person: [Person]) {
         self.person = person
     }
 }

 // MARK: - Person
 class Person {
     var name, age, employed: String

     init(name: String, age: String, employed: String) {
         self.name = name
         self.age = age
         self.employed = employed
     }
 }
```

# Encodable (Serialize)

### 1. JSONEncoder 이니셜

```swift
let encoder = JSONEncoder()
```

### 2. JSON으로 만들 객체 생성

```swift
let park = Person(name: "Park", age: "100")
```

### 3. (선택) outputFormatting설정

```swift
// 하나만 적용하고 싶을 경우
   encoder.outputFormatting = .prettyPrinted
   encoder.outputFormatting = .sortedKeys

// 여러개를 동시에 적용하고 싶을 경우
   encoder.outputFormatting = [.sortedKeys, .prettyPrinted]
```

### 4. JSON Data로 인코딩

```swift
let jsonData = try? encoder.encode(personModel)
```

### 5. 생성된 JSONData와 그 Data를 읽을 수 있도록 String으로 변환하고 옵셔널 캐스팅을 해준다.

옵셔널캐스팅을 하는 이유는 4번 스텝에서 try?로 작업을 해주었기 때문이다. 또한 jsonData를 String으로 바꿔줄때,옵셔널로 리턴된다.

```swift
if let jsonData = jsonData, let jsonString = String(data: jsonData, encoding: .utf8) {

    print(jsonString)
}

/**

 {
   "name" : "Park",
   "age" : "100"
 }

*/

```

### 상위계층을 사용하는 경우

만약 모델을 여러개 배열에 넣어서 보낸다면 상위계층을 이용해 encode해야한다. 위 방법과 동일하다.

```swift
let encoder = JSONEncoder()
let park = Person(name: "Park", age: "100")
let kim = Person(name: "Kim", age: "26")

var personModel = PersonModel(person: [])
personModel.person.append(kim)
personModel.person.append(park)
// var personModel = PersonModel(person: [kim, park])

encoder.outputFormatting = [.sortedKeys, .prettyPrinted]

if let jsonData = jsonData, let jsonString = String(data: jsonData, encoding: .utf8) {

    print(jsonString)
}

/**

{
  "person" : [
    {
      "age" : "26",
      "name" : "Kim"
    },
    {
      "age" : "100",
      "name" : "Park"
    }
  ]
}
*/
```

Decodable에 동일한 json을 사용하기위해 VIewController에 String을 하나 이니셜해서 받았다.

```swift
var exampleJSON: String = ""

/// 중간 생략
if let jsonData = jsonData, let jsonString = String(data: jsonData, encoding: .utf8) {
        self.exampleJSON = jsonString
}

```

# Decodable (Deserialize)

- decode는 encode과정과 동일하다. 오히려 더 단순할 수 있다.
- 모바일 업무상 Decode를 하는 경우가 많다. 또한 JSON을 단순하게 받기보단 API를 통해 받기 때문에 API를 수신하고 property들을 정제하여 사용하기위해서는 API 명세서를 받거나 최소한 jsonResponse값정도는 받는 것이 좋다.
- 아래 사이트를 이용하면 빠르게 모델링을 할수가 있다.
    - [https://app.quicktype.io/](https://app.quicktype.io/)

모델링은 Encode과정에서 구현했기때문에 생략

### 1. JSONDecoder 이니셜

```swift
let decoder = JSONDecoder()

```

### 2. (선택) String을 Data로 변환

API로 받는 경우, 이 과정은 생략한다.

```swift
var data = exampleJSON.data(using: .utf8)

```

### 4. data를 decode처리

### 4.1 상위계층을 그대로 가져온 경우

```swift
if let data = data, let myPerson = try? decoder.decode(PersonModel.self, from: data) {

    print("myPerson: \(myPerson)")
    print("myPerson.person: \(myPerson.person)")

/**

myPerson:
PersonModel(person: [jsonDecode.Person(name: "Kim", age: "26"), jsonDecode.Person(name: "Park", age: "100")])

myPerson.person:
[jsonDecode.Person(name: "Kim", age: "26"), jsonDecode.Person(name: "Park", age: "100")]

*/

}
```

### 4.2 단일계층을 가져오는 경우

```swift
if let data = data, let myPerson = try? decoder.decode(Person.self, from: data) {

    print("myPerson: \(myPerson)")
    print("myPerson.age: \(myPerson.age)")
    print("myPerson.name: \(myPerson.name)")

// myPerson: Person(name: "Kim", age: "26")
// myPerson.age: 26
// myPerson.name: Kim
}
```

# 통신사용

Decoding 이후 새로운 객체에 넣어준다.

```swift
if let data = data, let myPerson = try? decoder.decode(Person.self, from: data) {

let newPerson = Person(name: myPerson.age, age: myPerson.name)
 print("newPerson: \(newPerson)")
 newPerson: Person(name: "100", age: "Park")
}
```

URL세션을 이용하는 코드

```swift

// MARK: Result용 enum
enum NetworkError: Error {
    case noConnection
    case noResult
    case someError
}

/// Person URLSession
    /// - Parameters:
    ///   - urlString: url String
    ///   - completionHandler: 결과값 리턴
    static func getPersonAPI(with urlString:String, completionHandler: @escaping(Result<Person?, NetworkError>, _ message: String?) -> Void ) {

        guard let url = URL(string:urlString) else { return }

        URLSession.shared.dataTask(with: url) { data, response, error in

            if error != nil {
                completionHandler(.failure(.someError), nil)
                return
            }

            guard let safeData = data else {
                completionHandler(.failure(.noResult), nil)
                return
            }

            if let personParse = self.parseJSON(safeData) {
                completionHandler(.success(personParse), nil)
            } else {
                completionHandler(.failure(.noResult), nil)
            }

        }.resume()
    }

    static func parseJSON(_ personData: Data) -> Person? {
        let decoder = JSONDecoder()

        do {
            let decodedData = try decoder.decode(Person.self, from: personData)

            let newPerson = Person(name: decodedData.name, age: decodedData.age)

            return newPerson
        } catch {
            print("파싱 실패")
            return nil
        }

    }

    // MARK: 사용

    let urlParse = "http://www.naver.com"

    URLSession.getParseAPI(with: urlParse) { [weak self] result, message  in

        guard let self = self else { return }

        // 네트워크 연결 안되면 앱종료하는 얼럿
        self.actionSheetPresentViewController(message: message, animated: true, handler: {
            exit(0)
        })

        switch result {
        case .failure(let falseData):
            if falseData != .noConnection {
            }
        case .success(let data):
            // 필요에 따라 가공해서 사용
            if let personData = data {
                if personData.resultCode == 0 {

                }
            }
        }
    }
```
