# ReactorKit - 예제: CountApp

![6aa05998-26da-11e7-9b85-e48bec938a6e](https://user-images.githubusercontent.com/76529148/218311926-51a9828d-b484-49e7-a090-ec6614222a8e.png)


RxSwift에 대한 자세한 개념은 다른 글에서 소개하려고 한다.
일단 MVVM에 대해 설명을 해야할 것 같다.
기존 MVC에서 MVVM으로 확장하면서 **데이터바인딩**이라는 개념이 등장하게 된다. 

Model과 View, ViewModel을 사용하는 MVVM구조는
특정 View의 속성과 ViewModel의 속성을 연결한 뒤 ViewModel 속성이 변경되면 자동으로 View를 업데이트하게 하는 구조이다. 이때 연결한다는 것이 데이터 바인딩이다. ViewModel에 선언된 값이 변할 때를 `didSet`이나 `willSet`같은 **PropertyObserver**를 통해 다음 동작을 선언해주는 것이다.

이걸 RxSwfit를 사용하면 **어떤 동작이 시작되고 끝나는 것**을 하나의 Stream(흐름)으로 만들어 작업을 하는 것이다. 그리고 이 흐름들이 여러 방향으로 중구난방 흩어질 수 있는데  Reactor라는 객체를 만들어서 각각 `Action`, `Reduce`, `State`, `Mutate`라는 함수를 만들어서 View와 Reactor사이를 보다 짧고 명쾌하게 만드는 시스템이다. 무엇보다 RxSwift로 만든 비동기적 Stream을 단방향 Stream으로 만든 다는 것에 큰 장점이 있다.  

아래는 View와 Reactor의 관계를 나타낸 그림이다. 
![img1 daumcdn-1](https://user-images.githubusercontent.com/76529148/218311867-7f4ad21c-ba35-4df0-877d-8f6b4a3dfe6c.png)

1. View는 Action(사용자 입력 등의 동작)을 Reactor에게 전달한다
2. Reactor는 전달받은 동작(Action)에 따라 비즈니스 로직을 수행한다. 
3. 그 후 Reactor는 상태값을 변경하여 그 값을 통해 View에 변화를 일으킨다.
이것이 기본적인 ReactorKit의 단방향 Stream이다. 

```swift
View -> Action -> Reactor -> State -> View
```



조금더 Reactor에서 일어나는 동작을 자세히 알아보면 아래와 같다.
![img1 daumcdn-2](https://user-images.githubusercontent.com/76529148/218311872-535b7c09-4f0e-4033-b2ea-fba320d22ab6.png)





Reactor는 Action이 들어오면 두 단계에 거쳐서 State를 변경하는 것을 볼 수 있습니다

 
1. mutate() 함수 

- Action 스트림을 Mutation 스트림으로 반환하는 역할

- 이곳에서 네트워킹이나 비동기 로직 등의 사이드 이펙트를 처리한다.
  그 결과로 Mutation을 방출하는데, 그 값이 reduce() 함수로 전달된다. 


2. reduce() 함수
- 이전 상태와 Mutation을 받아서 다음 상태를 반환한다. 




```
class CounterViewReactor: Reactor {
    enum Action {
        case increase
        case decrease
    }
    
    enum Mutation {
        case increaseValue
        case decreaseValue
        case setLoading(Bool)
    }
    
    struct State {
        var value: Int = 0
        var isLoading: Bool = false
    }

    let initialState = State()
}
```



# Reactor Kit 예제
## 최초상태
최초상태는 아래와 같다. 
- increaseButton과 decreaseButton, valueLabel이 있다.
- 두 버튼을 누르면 valueLabel에 있는 숫자가 늘어나고 줄어든다. 

```swift
import RxSwift
import RxCocoa
import ReactorKit
import UIKit

class CounterViewController: UIViewController {

    @IBOutlet var increaseButton: UIButton!
    @IBOutlet var decreaseButton: UIButton!
    @IBOutlet var valueLabel: UILabel!
    
```


# Reactor 만들기
CounterViewController는 ReactorKit에서 'View'에 해당하는데, 이 View에 대응되는 Reactor를 만들어주는 과정이다.  

Reactor는 View의 상태를 관찰한다. View로부터 Action을 전달받아 비즈니스 로직을 수행한 후 상태를 변경하여 다시 View에 전달한다.

Reactor 프로토콜
- 사용자와의 상호작용을 표현하는 Action
- 상태를 변경하는 Mutation
- View의 상태를 표현하는 State
- 최초의 상태를 나타내는 initialState

이렇게 Reactor프로토콜을 따르는 CounterViewReactor를 만들어보자
아래는 Reactor프로토콜을 충족시키는 기본구조이다. 
```swift
class CounterViewReactor: Reactor {
    enum Action { }
    
    enum Mutation { }
    
    struct State { }
    
    let initialState = State()
}
```

### 1. Action

- 사용자 액션은 increase(플러스버튼누르기)와 decrease(마이너스 버튼 누르기)가 있는데, 이것을 정의한다. 
  (사용자가 위의 액션을 하면 Reactor에 increase 또는 decrease가 전달될 것이다.)


### 2. State
- 현재 값을 정의하는 value라는 것을 만든다. 


### 3. Mutation 
- Action과 State을 이어주는 부분이다.

아래 두가지를 정의한다.
- increase라는 Action이 들어왔을 때는 value를 1 증가처리 -> increaseValue 
- decraese라는 Action이 들어왔을 때는 value를 1 감소처리 -> decreaseValue 

 ```swift
class CounterViewReactor: Reactor {
    enum Action {
        case increase
        case decrease
    }
    
    enum Mutation {
        case increaseValue
        case decreaseValue
    }
    
    struct State {
        var value: Int = 0
    }
    
    let initialState = State()
}
```

### mutate() 구현하기
action을 받아서 mutation의 Observable을 리턴해주는 함수이다.
- Action 스트림을 Mutation 스트림으로 변환하고, 네트워킹 또는 비동기 로직등의 Side Effect를 처리한다.
그 결과로 Observable<Mutation>이 반환되고 reduce() 메소드로 전달된다.

`increase`라는 action이 들어오면 `increaseValue`라는 mutation의 Observable을 
`decrease`라는 action이 들어오면 `decreaseValue`라는 mutation의 Observable을 리턴하도록 구현한다.

enum타입의 action에 구현한 내용들은 switch에 모두 작성해야한다. 여기서 Observable을 리턴하기때문에 스트림이 시작된다. 

```swift
    func mutate(action: CounterViewReactor.Action) -> Observable<CounterViewReactor.Mutation> {
        switch action {
        case .increase:
                Observable.just(Mutation.increaseValue)
        case .decrease:
                Observable.just(Mutation.decreaseValue)
        }
    }
```

###  reduce() 구현하기
이제 reduce 함수를 구현한다. 이 함수는 이전 상태와 mutaion을 받아서 다음 상태를 반환하는 함수이다.
enum타입의 mutate에 구현한 내용들은 switch에 모두 작성해야한다.

```swift

    func reduce(state: CounterViewReactor.State, mutation: CounterViewReactor.Mutation) -> CounterViewReactor.State {
        var newState = state
        switch mutation {
        case .increaseValue:
            newState.value += 1
        case .decreaseValue:
            newState.value -= 1
        }
        return newState
    }
```
- mutation이 increaeValue이면 이전상태에서 1을 증가시킨 새로운 상태를 리턴해주고
- mutation이 decreaseValue이면 이전 상태에서 1을 감소시킨 새로운 상태를 리턴해준다.

이렇게 하면 Reactor의 구현이 끝난다.


# View 채택하기
ReactorKit의 View로 만들려면 View라는 프로토콜을 따르게 해줘야한다.
만약 storyboard로 구현을 했다면 StoryboardView를 채택하고, 그게 아니라면 View를 채택한다. 
## 채택 예시
```swift
class CounterViewController: UIViewController, StoryboardView { }

class CounterViewController: UIViewController, View { }
```
View는 아래와 같이 구성되어있다.

## View의 기본구조
스토리보드를 사용하니까 StoryboardView 프로토콜을 따르게 해준다.
disposeBag을 구현해주고
bind라는 함수의 구현한다. (reactor 타입을 아까 만든 CounterViewReactor로 한다.)

```swift
class CounterViewController: UIViewController, View { 

    var disposeBag: DisposeBag = DisposeBag()

    @IBOutlet var increaseButton: UIButton!
    @IBOutlet var decreaseButton: UIButton!
    @IBOutlet var valueLabel: UILabel!

    func bind(reactor: CounterViewReactor) { }
```

## View의 bind구현하기
### Action 바인딩
이제 bind함수에서 사용자 액션을 reactor의 action으로 바인딩한다.

```swift

    func bind(reactor: CounterViewReactor) {
        // Action 바인딩
        increaseButton.rx.tap
            .map { Reactor.Action.increase }
            .bind(to: reactor.action)
            .disposed(by: disposeBag)
        
        decreaseButton.rx.tap
            .map { Reactor.Action.decrease }
            .bind(to: reactor.action)
            .disposed(by: disposeBag)
    }
```
increaseButton이 탭되면 increase 액션으로 변환하여 reactor의 action에 바인딩해주겠다
decreaseButton이 탭되면 decrease 액션으로 변환하여 reactor의 action에 바인딩해주겠다

라는 의미의 코드이다.
### State 바인딩

이제 reactor가 새로운 state를 주면, state안에 있는 value로 valueLabel을 업데이트 시키도록 한다.  
(다만 value가 이전 값이랑 다르다면)

```swift

    func bind(reactor: CounterViewReactor) {
        // Action 바인딩
        increaseButton.rx.tap
            .map { Reactor.Action.increase }
            .bind(to: reactor.action)
            .disposed(by: disposeBag)
        
        decreaseButton.rx.tap
            .map { Reactor.Action.decrease }
            .bind(to: reactor.action)
            .disposed(by: disposeBag)
        
        // State 바인딩
        reactor.state
            .map { $0.value }
            .distinctUntilChanged()
            .map { "\($0)" }
            .bind(to: valueLabel.rx.text)
            .disposed(by: disposeBag)
    }
```
이제 view의 구현도 완료되었다.


## View에 Reactor 넣어주기
이렇게 View내부에 바인딩을 한다고 동작하지않는다. bind메서드는 *해당 View의 reactor*에 새로운 값이 들어와야만 반응하기 때문이다. 

## AppDelegate / SceneDelegate
버전마다 다른 경우 인데, 현재 View를 init하는 부분에 이 View의 reactor를 넣어준다. 그러면 bind함수가 실행 가능해진다. 

```swift
class SceneDelegate: UIResponder, UIWindowSceneDelegate {

    var window: UIWindow?

    func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
        guard let _ = (scene as? UIWindowScene) else { return }
        let counterVC = window?.rootViewController as? CounterViewController
        let counterViewReactor = CounterViewReactor()
        counterVC?.reactor = counterViewReactor
    }
}
```
여기까지가 기본 기능이다. 

그러면 한가지더 로직을 추가해서 다채롭게 만들어보자
# IndicatorView 추가하기
비동기 같은 상황을 만들고 IndicatorView를 추가하고자 한다. 

## 조건
- 비동기에서 처럼 1초후 값이 증가, 감소하게 만들어줄 것
- 1초 동안 떠있을 인디케이터를 만들 것

## IndicatorView 변수 선언
```swift
    // 인디케이터 뷰를 추가
    @IBOutlet var activityIndicatorView: UIActivityIndicatorView!
```
## Reactor 구현


```swift
    struct State {
        var value: Int = 0
        // 새로 구현
        var isLoading: Bool = false
    }
```
```swift
```
```swift
```
```swift
```

```swift
```


### 참고
- https://h1guitar.tistory.com/302
- https://velog.io/@tmdckd232/Swift-Reactor-Kit
