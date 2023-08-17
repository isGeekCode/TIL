# case let : for case let 익숙해지기

case let 이란 특정한 값을 패턴매칭을 통해 상수로 바인딩 하는 것이다.
이때 for문과 함께 사용하는 경우에는 in 뒤에 위치한 특정범위 안에 있는것들이 패턴매칭이 된다.
```swift
for case let specialElement in array {
    // specialElement를 처리
} 
```

### 일반적인 for case let
```swift
let numbers: [Any] = [1, 2, nil, 4, 5, nil, 7]

for case let number? in numbers {
    print(number) // 옵셔널 정수가 아닌 정수만 출력됨
}
```
패턴매칭이 된다고 했는데 예2를 보면 `for case let number?`라고 되어있다. 
`numbers`안에있는 요소를 number?라는 옵셔널 변수로 삼는다는 말이다. 
그래서 이 안에서는 옵셔널이 아닌 정수만 추출되어 number에 바인딩이 된다.
nil이 포함된 요소는 애초에 for문 안으로 못들어오게 되는 것이다. 

### as를 통해 형변환하는 for case let
```swift
class Shape { }
class Circle: Shape { }
class Square: Shape { }
class Triangle: Shape { }

let shapes: [Shape] = [Circle(), Square(), Circle(), Triangle(), Circle()]

for case let circle as Circle in shapes {
    circle.draw() // Circle 타입인 경우에만 draw() 메서드 호출
}
```
as 키워드를 사용하면 원하는 타입의 객체만 추출할 수 있다.

### Enum을 이용하는 for case let

case를 사용하는 열거형을 사용할때도 아래처럼 사용할 수 있다.
```swift
enum Fruit {
    case apple
    case orange
    case banana
    case strawberry
}

let fruits: [Fruit] = [.apple, .orange, .banana, .strawberry, .apple, .orange]

for case .apple in fruits {
    print("I found an apple!")
}
```

### enum을 사용하면서 as또한 사용하는 for case let
```swift
enum Vehicle {
    case car(speed: Int)
    case bicycle
    case motorcycle
    case truck
}

let vehicles: [Vehicle] = [.car(speed: 100), .bicycle, .car(speed: 60), .truck, .car(speed: 80)]

for case let .car(speed) as Vehicle in vehicles {
    print("Car with speed: \(speed)")
    // 추가로 수행할 작업
}
```
위의 코드에서는 배열에서 .car case에 해당하는 값을 추출하고, speed와 같은 연관 값을 바인딩하여 사용한다. 그리고 해당 값과 관련된 추가 작업을 수행할 수 있다. .car case에 대해서만 추가 작업을 수행하며, 다른 열거형 case는 패턴과 일치하지 않으므로 건너뛴다.



## 유용한 코드
### 네비게이션뷰컨트롤러 내부의 특정 뷰컨트롤러 캐치하기
이 함수는 네비게이션 컨트롤러에 속한 UIViewController들 중 특정 ViewController를 찾아 함수를 실행시키는 함수이다. 


```swift
if let navigationController = self.navigationController {
    for case let subVC as SubViewController in navigationController.viewControllers where subVC != self {
        subVC.reloadWebView()
    }
}
```
위코드를 사용하면 아래 내용을 가시적으로 만들 수 있다.
- navigationController 여부체크
- navigationController에 속한 viewControllers 배열 안에 SubVC만 체크하여 for문 실행시키는 것
- for문을 실행할때 where로 자신을 제외하는 조건

위 코드에서 where부분만 따로 떼어 아래와 같이 나눌수 있다.
```swift
if let navigationController = self.navigationController {
    for case let subViewController as SubViewController in navigationController.viewControllers {
        if subViewController != self {
            subViewController.reloadWebView()
        }
    }
}
```
하지만 네스팅이 심해져서 가독성을 떨어뜨릴 수가 있다.
그래서 `navigationController`를 옵셔널 체크하는 부분을 생략하면 아래와 같이 만들 수 있다.

```swift
self.navigationController?.viewControllers.forEach { viewController in
    if let subViewController = viewController as? SubViewController, subViewController != self {
        subViewController.reloadWebView()
    }
}
```
마지막으로 if let에서 위와 같이 길어지는 경우에 가독성이 떨어진다면, 정말 직관적으로 고차함수를 이용해 아래와 같이 리팩토링할 수 있다.

```swift
self.navigationController?.viewControllers
    .filter { $0 is SubViewController && $0 != self }
    .forEach { ($0 as! SubViewController).reloadWebView() }
```
결국은 case let은 결국 해당 값을 패턴매칭을 통해 상수로 바인딩하는 것이다. 그걸 for문과 함께 사용하는 것이 for case let이기 때문에 위와 같이 filter를 사용하는 것이 가능한 것이다.


## History
- 230609 : 초안작성
