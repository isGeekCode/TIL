# enum 사용법

```swift
// 두가지 방법 모두 가능하다. 
enum School {
    case elementary
    case middle
    case high
}

enum School {
    case elementary, middle, high
}

let mySchool = School.elementary
print("mySchool: \(mySchool)")
// mySchool: elementary
```

## enum에 자료형 선언

```swift
enum Grade: Int {
    case first
    case second
}
let myGrade = Grade.first
let yourGrade = Grade.second

print("myGrade: \(myGrade.rawValue)")
// 0
print("yourGrade: \(yourGrade.rawValue)")
// 1
```

1. Int로 임의의 rawValue를 넣으면, 그 뒤엔 순차적으로 값이 들어간다

```swift
// Int로 임의의 rawValue를 넣으면, 순차적으로 값이 들어간다
enum Fruit: Int {
    case apple = 2
    case pineappple
}
let myFruit = Fruit.apple
let yourFruit = Fruit.pineappple

print("myFruit: \(myFruit.rawValue)")
//myFruit: 2
print("yourFruit: \(yourFruit.rawValue)")
//yourFruit: 3
```

1. 첫번째 enum: Int에 rawValue를 부여하지않으면 무조건 0이 들어간다. 

```swift
// 2번째 enum에 100을 넣어서 blue는 값이 없지만 101이 부여된다.
enum Color: Int {
    case red
    case green = 100
    case blue

}
let myColor = Color.red
let yourColor = Color.green
let herColor = Color.blue

print("myColor: \(myColor.rawValue)")
//myFruit: 0
print("yourColor: \(yourColor.rawValue)")
//yourFruit: 100
print("herColor: \(herColor.rawValue)")
//yourFruit: 101
```

String이 들어있는 Enum

```swift
// String타입의 enum의 rawValue는 개인 그대로이다.
enum Vehicle: String {
    case train
    case bus
    case airplane
}
let myVehicle = Vehicle.train
print("myVehicle: \(myVehicle.rawValue)")
// myVehicle: train

enum Foods: String {
    case pasta = "chicken"
    case steak
    case ramen
}

let myDinner = Foods.pasta
print("myDinner: \(myDinner)")
// myDinner: pasta
print("myDinner: \(myDinner.rawValue)")
// myDinner: chicken
```

```swift

enum SchoolDetail {
    case elementary(name: String)
    case middle(name: String)
    case high(name: String)
}

let myMiddleSchoolName = SchoolDetail.high(name: "긱코드중학교")
print("myMiddleSchoolName: \(myMiddleSchoolName)")
// myMiddleSchoolName: high(name: "긱코드중학교")

enum Department {
    case food(name: String)
    case fashion(name: String)
    case sports(name: String)
    
    // 전부 동일하게 동작
    func getName() -> String {
        switch self{
        case .food(let name):
            return name
        case let .fashion(name):
            return name
        case .sports(let name):
            return name
        }
    }
}

let myShoppingList = Department.fashion(name: "Top10")
print("myShoppingList: \(myShoppingList)")
// myShoppingList: Fashion(name: "Top10")
print("myShoppingList: \(myShoppingList.getName())")
// myShoppingList: Top10
```
