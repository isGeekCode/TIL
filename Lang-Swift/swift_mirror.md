# Swift - Mirror 사용하기

Mirror 클래스는 Swift에서 리플렉션(Reflection)을 지원하기 위해 사용되는 클래스이다. 리플렉션은 프로그램이 자기 자신을 "반사"하여 타입, 속성, 메서드 등의 정보를 확인하고 조작할 수 있는 기능을 의미한다.

즉 Mirror 클래스를 사용하면 객체의 내부 구조를 검사하고 해당 정보를 다룰 수 있다. 

예를 들어, 객체의 속성을 동적으로 확인하거나 타입의 이름을 얻을 수 있다. 


### Mirror를 사용하면 할 수 있는 것

- 객체의 속성을 순회하고 속성의 이름과 값을 얻을 수 있다.
- 객체의 타입을 확인하고 해당 타입에 정의된 속성, 메서드, 프로토콜 등의 정보를 알아낼 수 있다.
- 객체의 부모 클래스나 프로토콜을 확인할 수 있다.
- 객체의 상위 계층 구조를 확인하고 탐색할 수 있다.

Mirror는 주로 디버깅, 테스팅, 시리얼라이제이션 등의 상황에서 유용하게 사용된다. 

객체의 내부 정보를 동적으로 검사하거나 자동화된 작업을 수행해야 할 때 유용하게 활용할 수 있다.

## 간단한 예제

### 예제1: 객체의 속성 순회하기
```swift
class Person {
    var name: String
    var age: Int
    
    init(name: String, age: Int) {
        self.name = name
        self.age = age
    }
}

let person = Person(name: "John", age: 30)

let mirror = Mirror(reflecting: person)
for (propertyName, value) in mirror.children {
    if let propertyName = propertyName {
        print("Property: \(propertyName), Value: \(value)")
    }
}

/*
Property: name, Value: John
Property: age, Value: 30
*/

```

### 예제2. 객체의 타입 확인하기
```swift
class Car {
    var make: String
    var model: String
    
    init(make: String, model: String) {
        self.make = make
        self.model = model
    }
}

let car = Car(make: "Tesla", model: "Model S")

let mirror = Mirror(reflecting: car)
if let objectType = mirror.subjectType as? Car.Type {
    print("Object is of type: \(objectType)")
}
/*
Object is of type: Car
*/
```


### 예제3. 객체의 부모 클래스 확인하기

```swift
class Animal {
    // ...
}

class Dog: Animal {
    // ...
}

let dog = Dog()

let mirror = Mirror(reflecting: dog)
if let superclass = mirror.superclassMirror {
    print("Superclass: \(superclass.subjectType)")
}

/*
Superclass: Animal
*/
```


## 심화된 리플렉션 작업
좀더 복잡한 리플렉션 작업을 수행하려면 아래와 같은 속성들을 사용한다.

- children
- displayStyle
- subjectType
- superclassMirror()
- descendant(_: Mirror.Path)
- dump(_: inout TargetStream, name: String?, indent: Int, maxDepth: Int, maxItems: Int):

### children
객체의 속성을 나타내는 튜플의 시퀀스를 반환합니다. 각 튜플은 속성의 이름과 값을 포함한다.

### displayStyle
객체의 표시 스타일을 나타내는 Mirror.DisplayStyle 열거형 값을 반환한다. 이는 객체가 구조체인지, 클래스인지, 열거형인지 등을 알려준다.

예시는 subjectType참조

### subjectType
객체의 타입을 나타내는 Any.Type 값을 반환한다.

```swift
class Person {
    var name: String
    var age: Int
    
    init(name: String, age: Int) {
        self.name = name
        self.age = age
    }
}

let person = Person(name: "John", age: 30)

let mirror = Mirror(reflecting: person)
print("Object Type: \(mirror.subjectType)")
print("Display Style: \(mirror.displayStyle)")

for (propertyName, value) in mirror.children {
    if let propertyName = propertyName {
        print("Property: \(propertyName), Value: \(value)")
    }
}

```


### superclassMirror()
객체의 부모 클래스에 대한 Mirror 인스턴스를 반환한다.

상단 예제 3 참조

### descendant()
`descendant(_: Mirror.Path)`를 사용하면

주어진 경로로부터 하위 객체에 대한 Mirror 인스턴스를 반환한다.



### dump():
`dump(_: inout TargetStream, name: String?, indent: Int, maxDepth: Int, maxItems: Int)`를 이용하여
객체를 디버깅 용도로 출력한다. 

```swift
let model = Model(name: "Tom", age:2)
dump(model)
/*
  __lldb_expr_86.Model
  - name: "Tom"
  - age: 2
*/

```




### 심화 예1. 중첩된 구조 탐색하기


```swift
struct Address {
    var city: String
    var zipCode: String
}

class Person {
    var name: String
    var age: Int
    var address: Address
    
    init(name: String, age: Int, address: Address) {
        self.name = name
        self.age = age
        self.address = address
    }
}

let address = Address(city: "New York", zipCode: "12345")
let person = Person(name: "John", age: 30, address: address)

let mirror = Mirror(reflecting: person)
print("Object Type: \(mirror.subjectType)")
print("Display Style: \(mirror.displayStyle)")

for (propertyName, value) in mirror.children {
    if let propertyName = propertyName {
        print("Property: \(propertyName), Value: \(value)")

        if let nestedMirror = Mirror(reflecting: value) {
            for (nestedPropertyName, nestedValue) in nestedMirror.children {
                if let nestedPropertyName = nestedPropertyName {
                    print("Nested Property: \(nestedPropertyName), Value: \(nestedValue)")
                }
            }
        }
    }
}

/*
Object Type: Person
Display Style: Optional(Swift.Mirror.DisplayStyle.class)
Property: name, Value: John
Property: age, Value: 30
Property: address, Value: Address(city: "New York", zipCode: "12345")
Nested Property: city, Value: New York
Nested Property: zipCode, Value: 12345

*/
```
### 심화 예3. 특정 타입의 속성 필터링

아래 예시에서는 Person 클래스의 객체를 생성하고, Mirror를 사용하여 객체의 속성 중 이름이 "is"로 시작하는 속성만 필터링하여 출력한다. 속성 이름이 "is"로 시작하는 경우에 대한 속성 이름과 값이 출력된다.

```swift
class Person {
    var name: String
    var age: Int
    var isEmployed: Bool
    
    init(name: String, age: Int, isEmployed: Bool) {
        self.name = name
        self.age = age
        self.isEmployed = isEmployed
    }
}

let person = Person(name: "John", age: 30, isEmployed: true)

let mirror = Mirror(reflecting: person)
for (propertyName, value) in mirror.children {
    if let propertyName = propertyName, propertyName.starts(with: "is") {
        print("Property: \(propertyName), Value: \(value)")
    }
}

/*
Property: isEmployed, Value: true

*/

```
### 심화 예4. 특정 타입의 속성 필터링2
Mirror는 실제로 Dictionary타입은 아니지만 유사한 구조를 띈 구조를 이루고 있기 때문에 딕셔너리처럼 사용이 가능하다. 

```swift
class Person {
    var name: String
    var age: Int
    var isActive: Bool
    
    init(name: String, age: Int, isActive: Bool) {
        self.name = name
        self.age = age
        self.isActive = isActive
    }
}

let person = Person(name: "John", age: 30, isActive: true)

let mirror = Mirror(reflecting: person)
for (propertyName, value) in mirror.children {
    if let propertyName = propertyName {
        switch propertyName {
        case "name":
            if let name = value as? String {
                print("Name: \(name)")
            }
        case "age":
            if let age = value as? Int {
                print("Age: \(age)")
            }
        case "isActive":
            if let isActive = value as? Bool {
                print("Active: \(isActive)")
            }
        default:
            break
        }
    }
}

```



## 실제사용 예

### MyNB 스탬프API

일단 코드를 보면 downloadImageIfNeeded()메서드가 반복되고 있다. 
차이는 imageType의 속성이다. 이 속성값에 따라 이후 로직이 달라져서 리팩토링이 필요하다.  
 
```swift
// Download normal image
downloadImageIfNeeded(from: imageType.normal.detailPath) { image in
    listImages.append(image)
    checkAllDownloadsComplete()
}

// Download on image
downloadImageIfNeeded(from: imageType.on.detailPath) { image in
    listImages.append(image)
    checkAllDownloadsComplete()
}

// Download off image
downloadImageIfNeeded(from: imageType.off.detailPath) { image in
    listImages.append(image)
    checkAllDownloadsComplete()
}

// Download screenOn image
downloadImageIfNeeded(from: imageType.screenOn.detailPath) { image in
    images.append(image)
    checkAllDownloadsComplete()
}

// Download screenOff image
downloadImageIfNeeded(from: imageType.screenOff.detailPath) { image in
    images.append(image)
    checkAllDownloadsComplete()
}

func downloadImageIfNeeded(from url: String, completion: @escaping (UIImage?) -> Void) {
    guard let imageUrl = URL(string: url) else {
        completion(nil)
        return
    }
    
    KingfisherManager.shared.retrieveImage(with: imageUrl) { result in
        switch result {
        case .success(let imageResult):
            completion(imageResult.image)
        case .failure(let error):
            print("KingfisherManager ::: Failed to download image: \(error)")
            completion(nil)
        }
    }
}

/*
 
// 예시 데이터
let stampImage1 = StampImagePathModel(
    imageName: "logo1",
    imageType: ImageTypes(
        normal: ScalePath(detailPath: "logo1_normal_1x.png"),
        on: ScalePath(detailPath: "logo1_on_1x.png"),
        off: ScalePath(detailPath: "logo1_off_1x.png")
        screenOn: ScalePath(detailPath: "logo1_screenOn_1x.png"),
        screenOff: ScalePath(detailPath: "logo1_screenOff_1x.png")
    )
)

let stampImage2 = StampImagePathModel(
    imageName: "logo2",
    imageType: ImageTypes(
        normal: ScalePath(detailPath: "logo2_normal_1x.png"),
        on: ScalePath(detailPath: "logo2_on_1x.png"),
        off: ScalePath(detailPath: "logo2_off_1x.png"),
        screenOn: ScalePath(detailPath: "logo2_screenOn_1x.png"),
        screenOff: ScalePath(detailPath: "logo2_screenOff_1x.png")
    )
)

// StampImagePathModel 배열
let stampImages: [StampImagePathModel] = [stampImage1, stampImage2]

*/
```

이 imageType의 속성들은 mirror를 사용해 Dictionary형태로 바꿔보자.

- mirror.children을 이용해 5가지 타입의 이미지 경로를 가진 Dictionary타입을 생성한다.
- 생성한 imagePathDic를 가지고 이미지를 다운로드한다음 uiImageDic에 다시 동일한 key값으로 추가


```swift 

let imageType = stampImagePathModel.imageType
var imagePathDic: [String: String] = [:] // 다운로드할 image의 경로 Dic

// imageType변수를 리플렉션
let mirror = Mirror(reflecting: imageType)

for (propertyName, value) in mirror.children {
    if let propertyName = propertyName,
       let path = value as? ScalePath {
        imagePathDic[propertyName] = path.detailPath
    }
}


var uiImageDic: [String: UIImage] = [:]  // 최종적으로 들어갈 UIImage Dic

for (propertyName, imagePath) in imagePathDic {
    print("final Property: \(propertyName), ImagePath: \(imagePath)")
    
    downloadImageIfNeeded(from: imagePath) { image in
        uiImageDic[propertyName] = image
        totalCount += 1
        checkAllDownloadsComplete()
    }
}

/// 이미지를 다운로드하고 성공시 completion에 UIImage를 반환
func downloadImageIfNeeded(from url: String, completion: @escaping (UIImage?) -> Void) {
    guard let imageUrl = URL(string: url) else {
        completion(nil)
        return
    }
    
    KingfisherManager.shared.retrieveImage(with: imageUrl) { result in
        switch result {
        case .success(let imageResult):
            completion(imageResult.image)
        case .failure(let error):
            print("KingfisherManager ::: Failed to download image: \(error)")
            completion(nil)
        }
    }
}

func checkAllDownloadsComplete() {
    if totalCount == 5 {
        // 모든 다운로드 완료
    } else {
        // 다운로드 완료되지 않음
    }
}
```
