# Layout - SwiftUI: State와 바인딩

SwiftUI에서는 `@State`프로퍼티를 사용하면 해당 `View`와 `@State`프로퍼티가 바인딩 된다.

바인딩이란 객체가 무언가에 묶여서 값이 변화하거나 상태가 변화할때 자동으로 동작할 수 있도록 연결된 것을 말한다.
쉽게 말해 View와 데이터를 연결하는 것이다.

그래서 여기에 @State가 달린 프로퍼티가 있다면 해당 변수에 변화가 생길 때, 해당View를 자동으로 다시 그려지도록 해주는 유용한 기능이다.

  
## TextField를 이용한 예제
@State를 이용하여 View에 텍스트필드와 해당 텍스트필드의 값을 연결하는 내용이다.

```swift
struct ContentView: View {
    @State private var name: String = ""
    
    var body: some View {
        VStack {
            TextField("Enter your name", text: $name)
            Text("Hello, \(name)!")
        }
    }
}
```

## Toggle을 이용한 예제
```swift
struct ContentView: View {
    @State private var isOn: Bool = false
    
    var body: some View {
        VStack {
            Toggle("Toggle", isOn: $isOn)
            if isOn {
                Text("The toggle is on")
            } else {
                Text("The toggle is off")
            }
        }
    }
}

```

## Button을 누르면 Text가 바뀌는 예제
```swift
struct ContentView: View {
    @State private var count = 0
    
    var body: some View {
        VStack {
            Text("Count: \(count)")
            Button("Increment") {
                count += 1
            }
        }
    }
}
```

## Slider을 변경하면 Text가 바뀌는 예제
```swift
struct ContentView: View {
    @State private var value: Double = 0.5
    
    var body: some View {
        VStack {
            Slider(value: $value)
            Text("\(value)")
        }
    }
}
```

## Stepper를 이용하여 Text가 바뀌는 예제
```swift
struct ContentView: View {
    @State private var value = 0
    
    var body: some View {
        VStack {
            Stepper(value: $value, in: 0...10) {
                Text("Value: \(value)")
            }.padding(30).background(.yellow)
        }
    }
}
```

# State는 Combine과 연관이 있나? 
@State는 직접적으로 Combine과 연관이 없다. Combine은 iOS에서 자체적으로 동작의 흐름을 비동기적으로 파이프처럼 연결할 수 있도록 만든 프레임워크이다. 오히려 UIKit의 PropertyObserver 중 didSet과 비슷한 기능을 한다.

# State와 PropertyObserver 중 didSet
둘다 공통점은 값이 변화하게 되면 무언가에 영향을 줄 수 있다는 것이다.

확연한 차이점은 State같은 경우는 View의 LifeCycle 동안에만 유지가 되고, View가 소멸되면 값이 초기화가 된다.
PropertyObserver의 경우는 그에 반해 값이 변경 될때마다 지정한 동작을 호출할 수가 있다.

# 그렇다면 State를 잘 사용하려면 SwiftUI의 View의 생명주기를 잘 이해해야하는가?
맞다. 일반적인 UIKit의 View의 생명주기와 SwiftUI의 View의 생명주기는 다르다.
아래는 SwiftUI의 View 생명주기 동안 호출하는 함수들이다.

- init(): 뷰(View)가 생성될 때 호출된다. 이 메서드에서는 뷰(View)가 사용할 초기 상태(State)를 설정한다.
- body: 뷰(View)가 나타내는 콘텐츠를 정의한다.
- onAppear(): 뷰(View)가 나타날 때 호출된다. 이 메서드에서는 뷰(View)가 나타나기 전에 수행해야 할 작업을 구현할 수 있다.
- onDisappear(): 뷰(View)가 사라질 때 호출된다. 이 메서드에서는 뷰(View)가 사라지기 전에 수행해야 할 작업을 구현할 수 있다.
