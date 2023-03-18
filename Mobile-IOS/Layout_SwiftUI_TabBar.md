# Layout - SwiftUI: TabBar


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
