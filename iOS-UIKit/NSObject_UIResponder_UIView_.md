# NSObject_UIResponder_UIView : UIView 클래스

화면의 직사각형 영역에 대한 내용을 관리하는 개체.

```swift
@MainActor
class UIView : UIResponder
```

<br><br><br>
https://github.com/isGeekCode/TIL/tree/main#ios-swiftui
## Overview

뷰는 앱 UI의 기본 구성요소이고, UIView클래스는 모든 View들에 공통되는 동작을 정의한다.  
View객체는 직사각형 bounds 안에서의 내용을 렌더링하고 해당되는 content들과 생기는 상호작용들을 다룬다.  
UIView 클래스는 인스턴스화하여 고정된 배경색을 표시하는데 사용할 수 있는 [Concrete 클래스](https://github.com/isGeekCode/TIL/blob/main/About-IT/iOS_words.md#concrete-class)이다. 


### var subviews

### var intrinsicContentSize
UIView와 그 하위 클래스들에서 제공되는 프로퍼티로, 해당 뷰의 내용(content)에 기반하여 자동으로 계산된 적절한 크기를 나타낸다. 이 프로퍼티는 주로 뷰의 내용물의 크기가 알려져 있을 때 사용되며, Auto Layout과 같은 레이아웃 시스템에서 뷰의 크기를 결정하는 데 활용된다.  
  
예를 들어, UILabel이나 UIButton과 같은 뷰들은 내용물의 텍스트나 이미지에 따라 크기가 동적으로 변할 수 있습니다. 이런 경우 intrinsicContentSize를 사용하여 뷰의 내용물에 맞는 적절한 크기를 자동으로 계산할 수 있다.  
  
주로 사용되는 UIView의 서브클래스에서 intrinsicContentSize를 오버라이딩하여 내용물의 크기를 계산하도록 구현할 수 있다. 이렇게 하면 Auto Layout 시스템이 해당 뷰의 크기를 결정할 때 intrinsicContentSize 값을 참고하여 자동으로 크기를 조정할 수 있다.  


## History
- 230810 : 초안작성
