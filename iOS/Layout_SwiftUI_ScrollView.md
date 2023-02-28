# Layout - SwiftUI: ScrollView

화면에서 스크롤 가능한 컨텐츠를 표시하기 위해 사용된다. 
ScrollView는 사용자가 스크롤할 수 있는  영역을 제공하고, 그 안에 다양한 뷰를 배치할 수 있다


### Init

ScrollView는 아래와 같이 사용할 수 있다.

```swift
ScrollView {
    // 스크롤 가능한 컨텐츠 뷰
}
```

기존에 사용했던 HStack, VStack, ZStack같은 경우는 아래와 같이 만들었을때

공간적인 한계성을 가지고 있다.

```swift
VStack {
          Text("1")
            .frame(width: 300, height: 500)
            .background(.teal)
          Text("2")
            .frame(width: 300, height: 500)
            .background(.orange)
          Text("3")
            .frame(width: 300, height: 500)
            .background(.yellow)
        }
```


<img src="https://user-images.githubusercontent.com/76529148/221868073-7b9d9f9b-c5cc-4162-8099-bf9769ded5de.png  width="200" height="400"/>


그래서 기존 Stack을 ScrollView로 수정하게 되면 아래와 같이 스크롤이 가능한 객체로 된다.  ScrollView의 인자로는 스크롤 가능한 컨텐츠를 포함하는 뷰가 전달된다. 이 컨텐츠 뷰는 ScrollView에 배치된 다양한 SwiftUI 뷰와 레이아웃 방식이 동일하다.

```swift
ScrollView {
          Text("1")
            .frame(width: 300, height: 500)
            .background(.teal)
          Text("2")
            .frame(width: 300, height: 500)
            .background(.orange)
          Text("3")
            .frame(width: 300, height: 500)
            .background(.yellow)
}
```

[https://user-images.githubusercontent.com/76529148/221869147-903188ee-1b29-4cba-9728-444ea0f93b88.mov](https://user-images.githubusercontent.com/76529148/221869147-903188ee-1b29-4cba-9728-444ea0f93b88.mov)

### 스크롤영역

기본적으로 스크롤영역을 확인하기 위해 색상을 넣어보면 생각과 달리 한정된 부분만 색상이 들어간다. 

```swift
var body: some View {
        ScrollView {
          Text("1")
            .frame(width: 300, height: 500)
            .background(.teal)
            .opacity(0.7)
          Text("2")
            .frame(width: 300, height: 500)
            .background(.orange)
            .opacity(0.7)
          Text("3")
            .frame(width: 300, height: 500)
            .background(.blue)
            .opacity(0.7)
        }
        .background(.red)
}
```

[https://user-images.githubusercontent.com/76529148/221871213-11609f31-1ce0-46c0-b63e-96d740cbea99.mov](https://user-images.githubusercontent.com/76529148/221871213-11609f31-1ce0-46c0-b63e-96d740cbea99.mov)

### 스크롤방향

ScrollView에는 다양한 스크롤 방향이 있다. ScrollView에서 스크롤 방향을 설정하려면 axis 매개 변수를 사용한다. 예를 들어, ScrollView를 수평 방향으로 스크롤하려면 다음과 같이 작성할 수 있다.

```swift
ScrollView(.horizontal) {
    // 수평 방향으로 스크롤 가능한 컨텐츠 뷰
}
```

### 메모리 효율성

ScrollView는 표시되는 모든 뷰를 미리 메모리에 로드하지 않아 효율적으로 사용할 수 있다.  또한 사용자가 스크롤할 때마다 새로운 뷰를 요청하며, 사용자가 스크롤을 멈출 때 로드된 뷰는 메모리에서 제거된다. 

이를 통해 큰 데이터 세트를 처리하는 데 유용하다.

### 다양한 속성들

ScrollView는 다양한 속성을 가지고 있으며, 이를 사용하여 스크롤 뷰의 동작 및 외관을 커스터마이즈할 수 있다. 

예를 들어, ScrollView에는 스크롤 indicator를 표시하는 showIndicators 매개 변수가 있다.

```swift
ScrollView(showIndicators: true) {
    // 스크롤 가능한 컨텐츠 뷰
}
```

이 외에도 `contentInset`, `contentOffset`, `contentHorizontalAlignment`, `contentVerticalAlignment` 등 다양한 속성을 제공한다. 이러한 속성을 사용하여 ScrollView의 외관 및 동작을 제어할 수 있다.
