# Layout - SwiftUI: UIButton

## UIButton Init
Button은 보여질 내용과 해야할 Action으로 나뉘어진다.

아래는 기본적인 형태이다. 
```swift
import SwiftUI

struct ContentView: View {
    var body: some View {
      Button("Hit me") {
        print("Hitted")
      }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}

```
객체를 만들때 이니셜라이저를 만들기 위해 소괄호를 열면 
여러 가지 형태, 용도의 형태를 익힐 수 가 있다.

```swift
Button {
  // Action
  print("Hitted")
} label: {
  // View
  Text("Hit me")
}
```

Role에서는 none, .destructive, .cancel의 enum을 세팅하면 버튼의 용도에 따른 색상을 만들수 있다.

```swift
Button(role: .destructive) {
  print("Hitted")
} label: {
  Text("Hit me")
}
```

버튼의 모양에 여러 가지 값들을 선언형으로 구현이 가능하다

```swift
  Button(role: .none) {
    print("Hitted")
  } label: {
    Text("Hit me")
      .padding()
      .frame(width: 150)
      .background(.purple)
      .cornerRadius(15)
  }
```


