# Layout - SwiftUI: Padding

패딩은 뷰의 가장자리와 콘텐츠 사이에 공간을 추가하는 데 사용할 수 있는 modifier(수정자)이다. 이 공간은 View의 위, 아래, 왼쪽, 오른쪽 한 면 이상에 추가할 수 있으며 추가하려는 공간의 양을 지정할 수 있다.

패딩을 사용하려면 모든 보기에서 `padding()` 메서드를 호출하고 원하는 양을 파라미터로 넣는다. 

아래 코드에서는 padding이 컬러값 보다 전에 넣었는지 혹은 후에 넣었는 지에 따라 모양이 달라진다.

- 1번이미지: 컬러아래에 100
- 2번이미지: 컬러전에 leading 100
- 3번이미지: 컬러다음에 leading 100

만약 한번에 여러개를 주고 싶은경우 `.padding([.leading, .bottom])`처럼 배열에 넣고 사용하면 된다.

```swift
VStack{
      Image(systemName: "bolt")
        .resizable()
        .aspectRatio(contentMode: .fit)
        .frame(width: 100)
        .background(.yellow)
        .foregroundColor(.orange)
        .padding(.bottom, 100)

      Image(systemName: "bolt")
        .resizable()
        .aspectRatio(contentMode: .fit)
        .frame(width: 100)
        .padding(.leading, 100)
        .background(.yellow)
        .foregroundColor(.orange)
      
      Image(systemName: "bolt")
        .resizable()
        .aspectRatio(contentMode: .fit)
        .frame(width: 100)
        .background(.yellow)
        .foregroundColor(.orange)
        .padding(.leading, 100)
    }
  }
```
<img width="228" alt="스크린샷 2023-03-09 오후 11 20 05" src="https://user-images.githubusercontent.com/76529148/224053937-6de6eade-4bba-438a-9504-71d9bf2e9732.png">
