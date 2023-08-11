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

또한 더 정교한 컨텐츠를 그리기 위하여 subclass를 구성할 수 있다.  

앱에서 볼수 있는 라벨, 이미지, 버튼 등의 인터페이스 요소들을 표시하려면 커스텀하기보다는 UIKit 프레임워크에서 제공하는 View의 하위클래스들을 사용하자.  

View 객체는 앱과 사용자가 상호 작용할 수 이는 주요 수단이기 때문에, View는 아래와 같이 몇가지 책임성을 갖고 있다.  


- Drawing and animation
    - View객체는 UIkit이나 CoreGraphic를 사용하여 내부의 직사각형 영역에 Content를 그려낸다.    
    - 일부 View의 프로퍼티를 새로운 값으로 변경하여 애니메이션처리할 수 있다.  
- Layout and subview management : 레이아웃과 subview 관리  
    - View는 subView들을 포함할 수있고, 없을 수도 있다.  
    - View는 subview들의 크기와 위치를 조절할 수 있다.  
    - AutoLayout을 이용하여 View계층상 변경사항에 따른 View의 resizing, repositioning 규칙을 정의한다.  
- Event handling
    - View는 UIResponder클래스를 상속받아, 터치 등의 이벤트들에 응답할 수 있다.
    - View들은 gesture recognizer를 통하여 일반적인 제스쳐를 다룰 수 있다.

<br><br>
    
View는 다른 View의 내부에 중첩시킴으로서 View 계층구조를 생성할 수 있으며, 이런 중첩을통해 Content들을 편리하게 구성할 수 있다.  

View를 중첩하면 중첩된 하위View와 상위 View 사이에 부모-자식관계(상하위 관계)가 형성된다.  

부모뷰(상위뷰)는 여러개의 하위View를 포함할 수 있지만, 각각의 하위뷰는 하나의 상위뷰가 있다.  

기본적으로, 서브뷰의 내용이 부모뷰의 경계를 벗어날 때, 서브뷰의 내용에 대한 클리핑(잘라내기)는 발생하지 않는다.   
> 서브뷰의 내용이 부모 뷰의 경계를 벗어날 때에도 자동으로 잘려나가지 않고 보여준다는 의미
 
`clipsToBounds`프로퍼티를 사용해 해당 동작을 변경할 수 있다.  

Frame과 Bounds 프로퍼티는 각 View의 모양을 정의한다. 

`Frame`프로퍼티는 해당 View의 superview의 좌표시스템([Coordinate System](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/CoordinateSystem.html))에 따른 View의 원점과 크기를 정의한다.  

`Bounds`프로퍼티는 View가 그자체로 보았을 때의 View 내부 크기를 정의하고, 오직 Code를 통해 View를 구현할 때에만 사용한다.  

> Frame은 View가 부모뷰의 좌표시스템 내에서 어떤 위치에 있고, 얼마나 큰지를 나타낸다. 
> Bounds는 자신의 좌표 시스템에서의 위치와 크기를 가리킨다.  

`center` 프로퍼티를 통해 Frame이나 Bounds를 직접 변경하지않고 View의 위치를 쉽게 조정할 수 있다.  

UIView 클래스의 사용 방법에 대한 자세한 내용은 [iOS용 프로그래밍 가이드](https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/ViewPG_iPhoneOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009503) 를 참고하자.  


<br><br><br>


## Create a View

일반적으로는 Storyboard에 View생성하려면 storyboard의 라이브러리에서 캔버스로 드래그를 한다.  

또한 Code Programming을 통해서도 View를 생성할 수 있다. 

일반적으로는 View를 생성할 때, 생성하려는 View의 크기와 Superview 위치상의 위치를 지정한다.  

예를 들어, 아래 예제에서는 View를 생성하고 superview의 좌표계에 있는 점(10,10)에 생성하려는 View의 왼쪽 상단 모서리를 배치한다.  

<br>

```swift
let rect = CGRect(x: 10, y: 10, width: 100, height: 100)
let myView = UIView(frame: rect)
```

<br>

다른 View에 subview를 추가하려면, superview에서 [addSubview(_:)](https://developer.apple.com/documentation/uikit/uiview/1622616-addsubview)메서드를 호출하면된다.  

View에 subviews는 원하는 만큼 추가할 수 있고, iOS에서는 문제없이 형제뷰(sibling view)가 서로 겹칠 수 있다.  

`addSubview(_:)`메서드를 호출 할 때마다 새로운 View는 다른 형제View들의 상단에 배치된다.  

[insertSubview(_:aboveSubview:)](https://developer.apple.com/documentation/uikit/uiview/1622570-insertsubview)메서드와  [subview(_:belowSubview:)](https://developer.apple.com/documentation/uikit/uiview/1622598-insertsubview)메서드를 통하여 subview간의 z축상 순서를 지정 수 있다.   

또한 [exchangeSubview(at:withSubviewAt:)](https://developer.apple.com/documentation/uikit/uiview/1622448-exchangesubview)메서드를 사용하여 이미 추가된 subview들간의 위치를 서로 교환할 수 있다.  

뷰를 생성하고나면, 나머지 뷰 계층의 변경에 대응하여 뷰의 크기와 위치가 어떻게 변화하는지를 제어하기 위해 Auto Layout 규칙을 만든다.

자세한 내용은 [Auto Layout 가이드](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/index.html#//apple_ref/doc/uid/TP40010853)를 참고하자. 


## Draw views

View 생성은 필요에 따라 발생한다.  

View가 처음 보여질때, 혹은 레이아웃의 변경으로 전체 또는 일부가 보여질 때에 System에서는 View의 Content를 그리길 요청한다.  

UIKit이나 Core Graphics를 사용하는 Custom 컨텐츠가 포함된 View의 경우는, 시스템에서 해당 View의 [draw(_:)](https://developer.apple.com/documentation/uikit/uiview/1622529-draw)메서드를 호출한다.  


이 메서드의 구현은 뷰의 내용을 현재의 그래픽 컨텍스트에 그리는 역할을 맡는다. 이 그래픽 컨텍스트는 시스템에 의해 이 메서드를 호출하기 전에 자동으로 설정된다. 

> 개발자가 미리 `draw(_:) 메서드`를 구현하면, 시스템이 해당 메서드를 호출하고 화면에 표시된다. 






### var subviews

### var intrinsicContentSize
UIView와 그 하위 클래스들에서 제공되는 프로퍼티로, 해당 뷰의 내용(content)에 기반하여 자동으로 계산된 적절한 크기를 나타낸다. 이 프로퍼티는 주로 뷰의 내용물의 크기가 알려져 있을 때 사용되며, Auto Layout과 같은 레이아웃 시스템에서 뷰의 크기를 결정하는 데 활용된다.  
  
예를 들어, UILabel이나 UIButton과 같은 뷰들은 내용물의 텍스트나 이미지에 따라 크기가 동적으로 변할 수 있습니다. 이런 경우 intrinsicContentSize를 사용하여 뷰의 내용물에 맞는 적절한 크기를 자동으로 계산할 수 있다.  
  
주로 사용되는 UIView의 서브클래스에서 intrinsicContentSize를 오버라이딩하여 내용물의 크기를 계산하도록 구현할 수 있다. 이렇게 하면 Auto Layout 시스템이 해당 뷰의 크기를 결정할 때 intrinsicContentSize 값을 참고하여 자동으로 크기를 조정할 수 있다.  

> `draw(_:)` 메서드를 구현할 때에는 성능에 주의해야 하며, 가능하면 최소한의 그림 그리기만 수행하는 것이 좋다.
> 이유는 이 메서드가 호출될 때마다 해당 View 전체를 다시 그리기 때문에 불필요한 그리기 작업이 많으면 성능 저하가 발생할 수 있기 때문이다.


## History
- 230810 : 초안작성
