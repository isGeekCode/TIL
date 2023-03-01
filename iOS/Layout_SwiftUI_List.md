# Layout - SwiftUI: List

SwiftUI에서의 List는 UIKit에서 사용하는 UITableView와 거의 흡사하지만 선언하는 방식이 완전이 다르다.

일단 다른 객체와 마찬가지로 아래와 같이 선언할 수 있다

```swift
List {
  // 리스트에 들어갈 내용
  Text("1")
  Text("2")
  Text("3")
}
```

<img width="245" alt="스크린샷 2023-03-01 오후 3 15 36" src="https://user-images.githubusercontent.com/76529148/222059867-3cd2ed71-ef09-41cb-be68-750195df72da.png">

### List 안에 HStack 넣기

```swift
List {
          
    HStack {
        Image(systemName: "sun.min.fill")
        Text("GeekCode")
    }
    HStack {
        Image(systemName: "cloud.fill")
        Text("HamSik")
    }
    
    HStack {
        Image(systemName: "bolt")
        Text("Sonak")
    }
}
```

<img width="243" alt="스크린샷 2023-03-01 오후 3 23 58" src="https://user-images.githubusercontent.com/76529148/222061102-257379b5-4260-417f-ae97-99aa550fef2a.png">

### 동적인 List를 만들기

기존에는 List에 들어갈 반복된 내용이 있다면 동일하게 반복적으로 선언했다.

위에서 나온 예문에서는 HStack안에 Image와 Text만 다르고 동일한 구조가 존재했다.

그러면 내용이 많아질수록 수정해야하는 부분이 많아지기 때문에 효율성이 떨어진다. 

이럴때는 바뀔 내용들만 따로 모아서 보관하면 body에는 간단한 구조만 만들어 사용할 수 있다.

**→ names만 수정하면 바로 반영시킬 수 있다.**

‼️ 콜렉션타입에서 값을 가져오는 경우, 이 값을 구분하기위해 id (identifier)를 선언해야만 한다.

아래 코드는  `List(names, id: \.self)`로 각자 자기 자신을 id로 선언한 것이다. 

```swift
let names: [String] = ["GeekCode", "HamSik", "DRu"]
    
var body: some View {
  
    List(names, id: \.self) { name in
        Text(name)
    }

}
```

<img width="258" alt="스크린샷 2023-03-01 오후 3 46 16" src="https://user-images.githubusercontent.com/76529148/222064646-ddd200c6-23d0-4cc3-bcc7-48870e46d32c.png">

### 동적인 List에 Model 구현하기

위 예제에서는 name을 모아 만든 배열을 가지고 만들었다.

이걸 하나의  구조체나 클래스로 만들어서 보관할 수 있다.

```swift
// 기존 코드
let names: [String] = ["GeekCode", "HamSik", "DRu"]

// 구조체 구현
struct Person {
    let name: String
}

let people: [Person] = [Person(name: "GeekCode"),
                        Person(name: "HamSik"),
                        Person(name: "DRu")]
```

위와 같이 수정하면 이제 배열의 요소에서`Person.name`의 형태로 접근이 가능하다.

하지만 이 구조체도 List에 넣어주려면 id가 필요하다. 구분할 수 있는 방법이 필요하다는 것이다.

그래서 `Identifiable프로토콜`을 아래처럼 채택하다. 클래스 혹은 구조체 이름 옆에 `클래스이름: 프로토콜이름` 이런 형태로 넣어준다. 

id는 UUID()를 선언해준다. 상황에 따라 UUID()를 하는 것 자체가 불필요한 상황도 있다.

예를 들어 회원정보가 있는 경우, 이미 구분할 수 있는 정보가 있기 때문에 불필요하다.

아래 코드도 위 코드와 동일한 결과를 만들 수 있다.

```swift
struct Person: Identifiable {
    var id = UUID()
    let name: String
}

struct ContentView: View {
      
  let people: [Person] = [Person(name: "GeekCode"),
                          Person(name: "HamSik"),
                          Person(name: "DRu")]
  var body: some View {
    List(people) { person in
      Text(person.name)
    }
  }
}
```

### List { HStack { Image() Text() } }

이제 처음에 구현했던 HStack 여러개를 구현했던 것 처럼 만들기위해 Person `Struct`에 imageName을 추가했다.

```swift
struct Person: Identifiable {
    var id = UUID()
    let name: String
    let imageName: String
}

struct ContentView: View {
  
  let people: [Person] = [Person(name: "GeekCode", imageName: "sun.min.fill"),
                          Person(name: "HamSik", imageName: "cloud.fill"),
                          Person(name: "DRu", imageName: "bolt")]
  var body: some View { 
    List(people) { person in
      HStack {
        Image(systemName: person.imageName)
        Text(person.name)
      }
    }
  }
}
```

처음에 구현한 코드

```swift
struct ContentView: View {

    var body: some View {
  
    List {
              
        HStack {
            Image(systemName: "sun.min.fill")
            Text("GeekCode")
        }

        HStack {
            Image(systemName: "cloud.fill")
            Text("HamSik")
        }
        
        HStack {
            Image(systemName: "bolt")
            Text("Sonak")
        }
    }
}
```

결론적으로 뭔가 더 길어진것 처럼 보이지만 Person을 구현하면 한 부분에서 관리하기 쉬워진다는 장점이 있다.


# Section

List를 사용하다보면 너무 복잡해져서 카테고리별로 나눠야할 때가 있다.

아이폰에서 설정페이지를 진입하면 분류에 따라 칸이 나뉘어져 있다는 걸 알 수 있다.

이렇게 묶어서 표현하는 것을 Section이라고 한다. 

<img width="223" alt="스크린샷 2023-03-01 오후 6 57 14" src="https://user-images.githubusercontent.com/76529148/222105825-17b125d6-01f0-4e4d-bc3d-6b8a4f96d08c.png">

## Section 만들기

가장 간단한 구조는 `Section { 들어갈 컨텐츠 }` 의 구조로 생성할 수 있다.

```swift
List {
  Section {
    HStack {
      Image(systemName: "sun.min.fill")
      Text("GeekCode")
    }
    HStack {
      Image(systemName: "cloud.fill")
      Text("HamSik")
    }
    HStack {
      Image(systemName: "bolt")
      Text("DRu")
    }
  }

  Section {
    HStack {
      Image(systemName: "sun.min.fill")
      Text("GeekCode")
    }
    HStack {
      Image(systemName: "cloud.fill")
      Text("HamSik")
    }
    HStack {
      Image(systemName: "bolt")
      Text("DRu")
    }
  }
}
```

<img width="223" alt="스크린샷 2023-03-01 오후 6 49 50" src="https://user-images.githubusercontent.com/76529148/222103990-6422a66e-e94a-40fe-931c-94d6067f4f57.png">

### Section의 Header, Footer

UIKit에서 TableView와 마찬가지로 Section에도 Header와 Footer를 만들 수 있다.

이 부분에는 Section의 컨텐츠 부분과 마찬가지로 HStack에 넣어사용하면 되고 , 심지어 VStack도 들어간다. 

`Text`는 대문자로 들어간다. 

기본구조는 아래와 같다. 

```swift
List {
  Section {

  // 컨텐츠

  } header: {

  // 헤더

  } footer: {

  // 푸터

  }
}
```

아래와 같이 Header와 Footer를 각 Section에 만들 수 있다.

```swift
List {
    Section {
          // 컨텐츠
          HStack {
            Image(systemName: "sun.min.fill")
            Text("GeekCode")
          }
          HStack {
            Image(systemName: "cloud.fill")
            Text("HamSik")
          }
          HStack {
            Image(systemName: "bolt")
            Text("DRu")
          }

      } header: {
        // 헤더
        HStack {
          Image(systemName: "sun.min.fill")
          Text("Header")
        }

      } footer: {
        // 푸터
        HStack {
          Image(systemName: "sun.min.fill")
          Text("Footer")
        }
    } // Section1
      
    Section {
        HStack {
          Image(systemName: "sun.min.fill")
          Text("GeekCode")
        }
        HStack {
          Image(systemName: "cloud.fill")
          Text("HamSik")
        }
        HStack {
          Image(systemName: "bolt")
          Text("DRu")
        }
    } // Section2
}
```

<img width="214" alt="스크린샷 2023-03-01 오후 7 08 48" src="https://user-images.githubusercontent.com/76529148/222108719-835d3ba4-7a66-4eaa-95f7-f67d80ecf29b.png">
