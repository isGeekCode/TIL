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



