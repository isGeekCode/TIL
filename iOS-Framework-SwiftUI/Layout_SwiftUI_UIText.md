# Layout - SwiftUI: Text

## UIText Init

아래는 기본적인 형태이다. 
```swift
import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack {
            Text("GeekCode")
                .bold()
                .underline()
                .italic()
                .strikethrough()
            Text("GeekCode")
                .font(.body)
            Text("GeekCode")                
                .font(.headline)
            Text("GeekCode")
                .font(.system(.title))
            Text("GeekCode")
                .font(.system(size: 50))
            Text("GeekCode")
                .underline(true, color:.orange)
            Text("GeekCode")
                .foregroundColor(.red)
            Text("GeekCode")
                .background(.purple)
            Text("GeekCode")
                .foregroundColor(.green)
                .font(.system(size: 39,
                              weight: .bold,
                              design: .rounded))
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
```

아래처럼 여러 옵션을 선택할 수 있다. 
- bold
- underline
- italic
- strikethrough
색상관련 옵션
- foregroundColor 
- background

<img width="368" alt="스크린샷 2023-02-15 오후 7 18 26" src="https://user-images.githubusercontent.com/76529148/219061864-f28b2dfd-de2d-4ed7-ab14-0f0764f7a010.png">
