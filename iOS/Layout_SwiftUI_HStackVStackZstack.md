# Layout - SwiftUI: UIText

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
```

## VStack

```swift
var body: some View {
    VStack {
        Text("1")
        Text("2")
        Text("3")
    }
}
```


## ZStack

```swift
var body: some View {
    ZStack {
        Text("1")
        Text("2")
        Text("3")
    }
}
```


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
