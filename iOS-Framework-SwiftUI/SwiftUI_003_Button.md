# Layout - SwiftUI: Button

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

### 기본구조
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

<img width="337" alt="스크린샷 2023-02-28 오후 2 29 26" src="https://user-images.githubusercontent.com/76529148/221762506-e4b12745-d4d2-4bcc-8c61-44d05775842b.png">


객체를 만들때 이니셜라이저를 만들기 위해 소괄호를 열면 여러 가지 형태, 용도의 형태를 익힐 수 가 있다.

이때 Role이라는 걸 볼 수 있다.

### Role

- none
- destructive
- cancel

Role에서는 none, .destructive, .cancel의 enum을 세팅하면 버튼의 용도에 따른 색상을 만들수 있다.

### 선언형

버튼의 모양에 여러 가지 값들을 선언형으로 구현이 가능하다

아래모양은 먼저 동작을 정하고, Label의 UI를 지정하는 코드이다. 

```swift
  Button(role: .none) {
    print("Hitted")
  } label: {
    Text("Hit me")
      .padding()           // 안쪽 여백 만들기
      .frame(width: 150)   // 가로의 길이 지정하기
      .background(.purple) // 색상을 넣는 방법
      .cornerRadius(15)    // 가장자리를 둥글게
  }
```

<img width="346" alt="스크린샷 2023-02-28 오후 2 39 19" src="https://user-images.githubusercontent.com/76529148/221763956-3ad64fac-c5ac-433d-84aa-c347e169ac03.png">


