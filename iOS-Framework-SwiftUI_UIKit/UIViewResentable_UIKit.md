# SwiftUI에서 UIKit 사용하기 : UIViewRepresentable

## UIViewRepresentable

UIViewRepresentable 프로토콜을 구현하면 SwiftUI에서 UIView객체를 사용가능하다.

```SWIFT
@available(iOS 13.0, tvOS 13.0, *)
@available(macOS, unavailable)
@available(watchOS, unavailable)

public protocol UIViewRepresentable : View where Self.Body == Never {

  associatedtype UIViewType : UIView
  
  func makeUIView(context: Self.Context) -> Self.UIViewType
  
  func updateUIView(_ uiView: Self.UIViewType, context: Self.Context)
  
  static func dismantleUIView(_ uiView: Self.UIViewType, coordinator: Self.Coordinator)
  
  associatedtype Coordinator = Void
  
  func makeCoordinator() -> Self.Coordinator
  
  typealias Context = UIViewRepresentableContext<Self>
}
```


<BR><BR>

UIViewRepresentable의 3가지를 필수로 정의해야한다.
- `makeUIView(context:)` -> `Self.UIViewType`
    - `makeUIView(content:)` : UIView를 생성하고 초기화하는 메서드
    - `Self.UIViewType`: 위 메서드에서 리턴되는 UIView객체의 타입
    - `updateUIView(_:,context:)` : UIView의 업데이트가 필요할 때 호출하는 메서드

<BR><BR>

## UIViewRepresentable를 이용하여 SwiftUI에서 UILabel 사용방법
- UIViewRepresentable 프로토콜을 구현
- makeUIView메소드와 updateUIView를 구현

```SWIFT
struct MyUILabel: UIViewRepresentable {
    
    @Binding var text: String
    
    func makeUIView(context: Context) -> UILabel {
        let label = UILabel()
        label.textColor = .black
        label.textAlignment = .center
        label.backgroundColor = .systemTeal
        return label
    }
    
    
    func updateUIView(_ myLabel: UILabel, context: Context) {
        myLabel.text = text
        
    }
}

struct ContentView_Previews: PreviewProvider {
  static var previews: some View {
      ContentView(text: "Hello world")
  }
}
```

<BR><BR>

사용할 때에는 일반적으로 SwiftUI를 사용하는 방법으로 선언한다.


```swift
struct ContentView: View {
    @State var text: String
    var body: some View {
        VStack {
            MyUILabel(text: $text)
            
            Spacer(minLength: 100)
                .foregroundStyle(.red)
        
            Text("Today's Weather")
                .font(.title)
                .border(.gray)
            HStack {
                Text("🌧")
                Text("Rain & Thunderstorms")
                Text("⛈")
            }
            .alignmentGuide(HorizontalAlignment.center) { _ in  50 }
            .border(.gray)
        }
        .border(.gray)
        
    }
}

```

<BR><BR>

### 결과 이미지

<img width="300" alt="스크린샷 2023-11-16 오전 9 36 03" src="https://github.com/isGeekCode/TIL/assets/76529148/79d48696-92a3-493a-810c-89164b9b78be">


- 참고링크 : [김종권 : 튜토리얼 - 13. SwiftUI에서 UIKit 사용 방법 (UIViewRepresentable, UIViewControllerRepresentable)](https://ios-development.tistory.com/1043)



### History
- 231116: 초안작성
