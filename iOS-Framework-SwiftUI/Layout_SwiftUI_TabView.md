# Layout - SwiftUI: TabView

ContentView는 SwiftUI View 구조체를 나타낸다. body 속성은 TabView를 반환하며, TabView의 각 탭은 Text 뷰를 사용하여 표시한다. 
각 탭에는 Image(systemName:)과 Text() 함수를 사용하여 아이콘과 텍스트를 추가한다.

ContentView_Previews는 미리보기 기능을 위한 코드이다. SwiftUI 미리보기를 사용하면 코드를 빠르게 시각적으로 확인할 수 있다.

## tabItem을 이용하여 구현하기
```swift

import SwiftUI

struct ContentView: View {
    var body: some View {
        TabView {
            Text("First View")
                .tabItem {
                    Image(systemName: "1.circle")
                    Text("First")
                }
            Text("Second View")
                .tabItem {
                    Image(systemName: "2.circle")
                    Text("Second")
                }
            Text("Third View")
                .tabItem {
                    Image(systemName: "3.circle")
                    Text("Third")
                }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}

```


### 구현 화면
https://user-images.githubusercontent.com/76529148/226113592-33d7906c-4ecd-4ef1-b66f-7a388115c6b5.mov


## 탭별로 View를 각각 생성하기

```swift
struct ContentView: View {
    var body: some View {
        TabView {
            FirstView()
                .tabItem {
                    Image(systemName: "1.circle")
                    Text("First")
                }
            SecondView()
                .tabItem {
                    Image(systemName: "2.circle")
                    Text("Second")
                }
            ThirdView()
                .tabItem {
                    Image(systemName: "3.circle")
                    Text("Third")
                }
        }
    }
}

struct FirstView: View {
    var body: some View {
        Text("First View")
    }
}

struct SecondView: View {
    var body: some View {
        Text("First View")
    }
}

struct ThirdView: View {
    var body: some View {
        Text("First View")
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
```
