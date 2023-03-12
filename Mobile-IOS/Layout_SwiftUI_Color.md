# Layout - SwiftUI: Color

Color는 Background나 Foreground에 들어갔던 색상과 살짝 다르게, Color가 들어간 View 느낌으로 인식하면 좋을 것같다.

선언방법은 아래와 같다.

```swift
Color(.red)
// RGB로 넣을 수도 있다.
Color(red: 0.5, green: 0.2, blue: 0.7)
```

그런데 이렇게 선언할경우 기본적으로는 상단 하단의 safeArea라고 불리우는 부분에는 색상이 들어가지않는다.

만약 이부분까지 색상을 넣어주고 싶은경우에는 아래와 같이  edgesIgnoringSafeArea()를 사용한다.

```swift
Color(.red)
Color(.systemPink).edgesIgnoringSafeArea(.all)
Color(.systemYellow).edgesIgnoringSafeArea(.top)
Color(.systemBlue).edgesIgnoringSafeArea(.bottom)
// 여러개의 옵션을 원할경우 배열안에 넣어준다.
Color(.systemGreen).edgesIgnoringSafeArea([.top,.bottom])

```

<img width="400" alt="스크린샷 2023-03-12 오전 11 46 40" src="https://user-images.githubusercontent.com/76529148/224521388-c4162529-1e3d-4ca9-a5d2-cc7da8cac8e7.png">



또 아래와 같이 도형을 만들 수도 있다. Color객체를 만들어 clipShape로 해당 모양을 지정한다.

이때는 width와 height를 지정해줄 수 있다.

→ 원 같은 경우는 width height중 큰 값을 기준으로 지름이 형성된다.

```swift
// 원
Color(.systemTeal)
  .frame(width: 300, height: 200)
  .clipShape(Circle())

// 사각형
Color(.systemYellow)
  .frame(width: 200, height: 100)
  .clipShape(Rectangle())

// 사각형에 둥근 모서리
Color(.systemOrange)
  .frame(width: 200, height: 100)
  .clipShape(RoundedRectangle(cornerRadius: 30))

```

<img width="219" alt="스크린샷 2023-03-12 오전 11 38 39" src="https://user-images.githubusercontent.com/76529148/224521463-25aaea4a-a343-40d3-a21a-c0ddd378786c.png">
