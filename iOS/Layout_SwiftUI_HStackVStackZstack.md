# Layout - SwiftUI: HStack, VStack, ZStack

## UIStackView
UIKit에서 StackView라는 것이 있다.  Auto Layout을 이용해 열 또는 행에 View들의 묶음을 배치할 수 있는 간소화된 객체이다. 그래서 Flexible하게 내부 요소들을 채울 수 있다.

### 내부요소 관리
StackView는 "Arranged Subviews" 프로퍼티에 들어있는 모든 뷰의 레이아웃을 관리한다.
이 뷰들은 StackView의 arrangedSubviews 배열의 순서에 따라 StackView의 축(axis)을 따라 배치된다.
더 정확히 하면, 레이아웃은 StackView의 축(axis), distribution(분배), alignment(정렬방식), spacing(여백)에 따라 배치된다.

1. axis(축) 
2. distribution(분배) 
3. alignment(정렬) 
4. spacing(여백)

이 프로퍼티들을 이용해 스택뷰의 arrangeSubviews 배열에 들어있는 View들의 Layout을 관리할 수 있다.

자세한 내용은 아래 링크를 참고하자
https://hyunndyblog.tistory.com/148/

# HStack, VStack, ZStack
UIKit에서 UIStackView가 선택적이었다면 SwiftUI에서는 필수적인 요소라고 생각하면된다.
UIStackView에서느느 Axis(방향)을 정해줬지만 이것들은 각각 이미 Axis가 정해져있다.

각각 Horizontal, Vertical, Z축 방향으로 Axis가 정해져있다.
아래는 기본적인 형태이다. body를 제외한 코드는 생략하겠다

## HStack
```swift
var body: some View {
    HStack {
        Text("1")
        Text("2")
        Text("3")
    }
}

var body: some View {
  HStack{
    Rectangle()
        .fill(Color.teal)
        .frame(width: 150, height: 150)
    
    Rectangle()
        .fill(Color.orange)
        .frame(width: 150, height: 150)
  }
}
```

### 그림1
파랑색 사각형과 오렌지 사각형이 횡방향으로 배치된다.
<img width="297" alt="스크린샷 2023-02-18 오후 6 24 57" src="https://user-images.githubusercontent.com/76529148/219950794-eb3261df-e89c-41bd-a1d7-28510bccb425.png">


## VStack

```swift
var body: some View {
    VStack {
        Text("1")
        Text("2")
        Text("3")
    }
}

var body: some View {
  VStack{
    Rectangle()
        .fill(Color.teal)
        .frame(width: 150, height: 150)
    
    Rectangle()
        .fill(Color.orange)
        .frame(width: 150, height: 150)
  }
}
```

### 그림2
파랑색 사각형과 오렌지 사각형이 종방향으로 배치된다.
<img width="296" alt="스크린샷 2023-02-18 오후 6 25 04" src="https://user-images.githubusercontent.com/76529148/219950800-f713d114-24d9-4ff3-87e0-bdc7554762d9.png">


## ZStack

```swift
var body: some View {
    ZStack {
        Text("1")
        Text("2")
        Text("3")
    }
}


var body: some View {
  ZStack{
    Rectangle()
        .fill(Color.teal)
        .frame(width: 150, height: 150)
    
    Rectangle()
        .fill(Color.orange)
        .frame(width: 150, height: 150)
  }
} 
```
### 그림3-1
파랑색 사각형과 오렌지 사각형이 Z축으로 배치된다. 이때 Z축이 큰 요소가 바깥쪽에 있기때문에 주황색이 더 가까이 있다. 주황색만 보이게 된다. 
<img width="295" alt="스크린샷 2023-02-18 오후 6 25 11" src="https://user-images.githubusercontent.com/76529148/219950817-fb5e84ff-56fa-42a5-8920-677c0a019628.png">

### 그림3-2
Z축을 이해하기 위해 Xcode의 Hierachy를 찍은 사진이다. 이런식으로 쌓여있다.
<img width="482" alt="스크린샷 2023-02-18 오후 6 33 26" src="https://user-images.githubusercontent.com/76529148/219950833-b566f329-5295-4364-96c3-5c75fd4bafbb.png">

### 배경색 채우기

```swift
    var body: some View {
      VStack {
        Spacer()
        HStack {
          Spacer()
          Text("Test")
          Spacer()
        }
        Spacer()
      }.background(Color.yellow)
    }
```
