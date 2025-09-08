# NSObject_UIResponder_UIView : UIView 클래스

화면의 직사각형 영역에 대한 내용을 관리하는 개체.

```swift
@MainActor
class UIView : UIResponder
```

<br><br><br>


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


<br><br><br>

## Draw views

View 생성은 필요에 따라 발생한다.  

View가 처음 보여질때, 혹은 레이아웃의 변경으로 전체 또는 일부가 보여질 때에 System에서는 View의 Content를 그리길 요청한다.  

UIKit이나 Core Graphics를 사용하는 Custom 컨텐츠가 포함된 View의 경우는, 시스템에서 해당 View의 [draw(_:)](https://developer.apple.com/documentation/uikit/uiview/1622529-draw)메서드를 호출한다.  


이 메서드를 구현하면 뷰의 내용을 현재 graphic context에 그릴 수 있고. 이 그래픽 컨텍스트는 시스템에 의해 이 메서드를 호출하기 전에 자동으로 설정된다.

이로써 뷰의 내용의 정적 시각적 표현이 생성되며, 이것은 화면에 표시될 수 있다.

> 개발자가 미리 `draw(_:) 메서드`를 구현하면, 시스템이 해당 메서드를 호출하고 화면에 표시된다. 
> `draw(_:)` 메서드를 구현할 때에는 성능에 주의해야 하며, 가능하면 최소한의 그림 그리기만 수행하는 것이 좋다.
> 이유는 이 메서드가 호출될 때마다 해당 View 전체를 다시 그리기 때문에 불필요한 그리기 작업이 많으면 성능 저하가 발생할 수 있기 때문이다.

뷰의 실제 내용이 변경되면, 해당 뷰를 다시 그려야 함을 시스템에게 알려야 한다.  

이를 위해 뷰의 [setNeedsDisplay()](https://developer.apple.com/documentation/uikit/uiview/1622437-setneedsdisplay) 또는 [setNeedsDisplay(_:)](https://developer.apple.com/documentation/uikit/uiview/1622587-setneedsdisplay) 메서드를 호출해야 한다.  

이러한 메서드는 시스템에게 다음 Drawing Cycle동안 뷰를 업데이트해야 함을 알려준다.  

다음 Drawing Cycle까지 업데이트를 기다리기 때문에, 이러한 메서드를 여러 뷰에 동시에 호출하여 동시에 업데이트할 수 있다.  


> 이 메소드를 호출하는 즉시 view의 컨텐츠를 업데이트 하는 것이 아니다.  
> 다음 드로잉 사이클이 올때까지 기다렸다가 변화된 내용들을 한번에 업데이트 한다.  
> 따라서 호출하는 시점과 변경되는 시점의 차이가 생긴다.  


<br><br><br>

## Animate views

View의 여러 property(속성값)들을 변경하여 애니메이션화할 수 있다.   

즉, 프로퍼티를 변경하면 현재 값에서 시작해 새로 지정한 값에 끝나는 애니메이션을 생성한다. 

아래 UIView 클래스의 프로퍼티들을 통해 애니메이션화할 수 있다.  

- frame
- bounds
- center
- transform
- alpha
- backgroundColor 

변경된 내용을 애니메이션 처리하려면,  

[UIViewPropertyAnimator](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator)객체를 만들고, 이 메서드의 handler block을 통해 변경할 View의 프로퍼티를 변경한다.  

`UIViewPropertyAnimator`클래스를 사용하면 애니메이션의 지속시간과 타이밍을 지정할 수 있도록 해준다.  

하지만 실제 애니메이션을 수행하는 것은 이 클래스가 담당한다.  

현재 실행 중인 프로퍼티 기반의 애니메이터를 일시중지해서 애니메이션을 중단하고 상호작용하돌고 제어할 수도 있다.  
 

<br><br><br>

## Threading considerations(Threading 고려사항)

앱의 UI(User Interface) 조작은 주 스레드(Main thread)에서 이루어져야 한다.  

따라서 UIView 클래스의 메서드를 호출할 때는 항상 앱의 메인 스레드에서 실행 중인 코드에 호출을 해야한다.  

유일하게 View 객체를 생성하는 경우에만 메인 스레딩을 하지않아도 된다. 


<br><br><br>


## Subclassing notes(Subclassing 주의 사항)

UIView클래스는 시각적 컨텐츠와 사용자 상호작용이 모두 필요한 상속지점이다.  

UIView를 상속받는 이유는 여러가지가 있지만, 따라서 기본 UIView가 제공하지 않는 것이 있을 때만  UIView를 상속받아 구현하는 것이 좋다. 


<br><br><br>

## Methods to Override(Override하는 메서드)
UIView를 서브클래싱할 때, Override(재정의)해야하는 매서드가 몇개 있고,  
필요한 경우에만 Override해도 되는 메서드가 있다.  

UIView는 정말 다양하게 설정 가능한 클래스이기 때문에 커스텀 메서드를 재정의하지 않고도, 정교하게 View 동작을 구현하는 다양한 방법이 있다. 

이에 대한 설명은 [Altanatives to subclassing](https://developer.apple.com/documentation/uikit/uiview#1652896) 섹션에서 살펴보자.  


아래 목록에는 UIView 하위클래스에서 고려해볼 수 있는 메서드 목록이 포함되어 있다  

<br><br>

### Initializaion(초기화)
- `init(frame:)`
    - 초기화를 할때는 이 메서드를 구현하는 것이 좋다. 
    - 또한 이 메소드를 커스텀하여 초기화 메소드를 구현할 수 있다.
- `init(coder:)`
    - 스토리보드나 Nib파일을 통해 View를 로드하고, View에 커스텀 init이 필요한 경우 사용하자.
- `layerClass`
    - View의 뒤에 다른 Core Animation Layer를 사용하여 배경 공간을 생성할 때 사용한다.
    - 예를 들어, 스크롤 가능한 넓은 영역을 표시하기 위해 타일링을 사용하는 경우, 이속성을 CATiledLayer클래스로 설정할 수 있다.  
    - 자세한 내용은 [TIL : Layer에 대하여](https://github.com/isGeekCode/TIL/blob/main/iOS-Framework-UIKit/NSObject_UIResponder_UIView_layer.md) 참고 

<br><br>

### Drawing and Printing


- `draw(_:)`
    - 이 메서드를 구현하여 뷰가 custom 콘텐츠를 그릴 수 있다.
    - 만약 커스텀으로 그릴 것이 없다면, 이 메서드를 재정의하지 말자.

- `draw(_:for:)`
    - 이 메서드는 뷰의 콘텐츠를 printing 중에 다르게 그릴 경우에만 구현한다.

<br><br>

### Layout and Constraints

- `requiresConstraintBasedLayout`
    - view클래스가 제대로 작동하기 위해 제약조건이 필요한 경우, 이 속성을 사용한다.

- `updateConstraints()` 
    - 뷰와 하위 뷰 간의 커스텀 제약조건 생성이 필요한 경우, 이 메소드를 사용한다.

- `alignmentRect(forFrame:)`, `frame(forAlignmentRect:)` 
    - 여러 뷰에 대한 정렬 방식을 재정의할 수 있다.

- `didAddSubview(:)`, `willRemoveSubview(:)` 
    - 하위뷰 추가 및 제거를 추적하려면 이 메서드를 구현한다.

- `willMove(toSuperview:)`, `didMoveToSuperview()`
    - 현재 뷰의 계층 구조에서 뷰의 이동을 추적하기 위해 필요한 경우 이 메서드를 구현한다.


<br><br>

### Event Handling(이벤트 처리)

- `gestureRecognizerShouldBegin(_:)`
    - 이 메서드를 구현하여 뷰가 터치 이벤트를 직접 처리하고, 연결된 gesture recognizer가 추가 동작을 트리거하는 것을 방지하려는 경우에 구현한다.

- `touchesBegan(:with:)`, `touchesMoved(:with:)`, `touchesEnded(:with:)`, `touchesCancelled(:with:)` 
    - 터치 이벤트를 직접 처리해야 하는 경우에 사용한다. (제스처 기반 입력의 경우 gesture recognizer를 사용한다.)



<br><br>

### Alternatives to Subclassing(이벤트 처리)

많은 뷰 동작들은 서브클래싱 없이도 설정할 수 있다.  

메서드를 override하기 전에 아래 내용을 수정하면 필요한 동작들을 제공할 수 있는지 고려해보자.




- `addConstraint(_:)` 
    - 뷰와 그 하위 뷰에 대한 Autolayout 동작을 정의한다.

- `autoresizingMask`
    - 슈퍼뷰의 프레임이 변경될 때 Autolayout 동작을 제공한다.
    - 이러한 동작은 constraints들과 결합하여 사용할 수 있다.

- `contentMode` 
    - 뷰의 프레임이 아닌 뷰의 콘텐츠에 대한 레이아웃 동작을 제공한다.
    - 이 속성은 또한 콘텐츠가 뷰에 맞도록 축소/확대되거나 캐시되거나 다시 그려지는 방식에 영향을 미친다.

- `isHidden` 또는 `alpha `
    - 뷰 전체의 투명도를 변경한다.
    
- `backgroundColor` 
    - 해당 뷰의 색상을 설정한다.

- `Subviews` 
    - `draw(_:)`메서드를 사용하여 콘텐츠를 그리는 대신 이미지 및 레이블 서브뷰를 삽입하여 표시하려는 내용을 포함한 image나  albel의 하위 뷰를 포함한다.

- `Gesture recognizers` 
    - 들어오는 터치 이벤트를 직접 가로채고 처리하기 위해 gesture recognizer를 사용하여 액션을 타겟 객체로 보낼 수 있다.

- `Animations` 
    - 변경 사항을 직접 애니메이션처리하지 않고 내장된 애니메이션 support를 사용한다. `Core Animation`이 제공하는 애니메이션 지원은 빠르고 쉽게 사용할 수 있다.

- `Image-based backgrounds`
    - 정적인 콘텐츠를 표시하는 뷰의 경우, 이미지를 직접 그리는 대신 gesture recognizer와 함께 UIImageView 객체를 사용하는 것이 더 좋다.
    - 또는 일반적인 UIView 객체를 사용하고 이미지를 뷰의 CALayer 객체의 콘텐츠로 할당할 수도 있다.




<br><br><br>

# TOPIC
필요한 경우에만 내용 추가중


### var intrinsicContentSize

UIView와 그 하위 클래스들에서 제공되는 프로퍼티로, 해당 뷰의 내용(content)에 기반하여 자동으로 계산된 적절한 크기를 나타낸다. 이 프로퍼티는 주로 뷰의 내용물의 크기가 알려져 있을 때 사용되며, Auto Layout과 같은 레이아웃 시스템에서 뷰의 크기를 결정하는 데 활용된다.  
  
예를 들어, UILabel이나 UIButton과 같은 뷰들은 내용물의 텍스트나 이미지에 따라 크기가 동적으로 변할 수 있습니다. 이런 경우 intrinsicContentSize를 사용하여 뷰의 내용물에 맞는 적절한 크기를 자동으로 계산할 수 있다.  
  
주로 사용되는 UIView의 서브클래스에서 intrinsicContentSize를 오버라이딩하여 내용물의 크기를 계산하도록 구현할 수 있다. 이렇게 하면 Auto Layout 시스템이 해당 뷰의 크기를 결정할 때 intrinsicContentSize 값을 참고하여 자동으로 크기를 조정할 수 있다.  


## History
- 230810 : 초안작성
