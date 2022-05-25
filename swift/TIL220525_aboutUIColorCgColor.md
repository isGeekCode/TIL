# 🍊 CGColor

색상(color)을 해석하는 방법이 명시되어있는 색상 공간(color space)이 있는,색상(color)을 정의하는 요소의 집합입니다

Color는 코어그래픽스(CoreGraphics)프레임워크와 연결되어있어 앞에 CG가 붙었어요.

이 밖에도 CGRect, CGSize, CGPoint 도 CG의 데이터타입이에요. ios 에서 그려주는 것은 모두 코어그래픽스 프레임워크가 담당합니다

- 코어그래픽스 프로그래밍 가이드
    
    [https://developer.apple.com/documentation/coregraphics](https://developer.apple.com/documentation/coregraphics)
    
- 코어그래픽스 개념, 메소드 등
    
    [https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html)
    

 

# 🍊 UIColor

색상 데이터 또는 추가로 알파값(투명도)를 저장하는 객체

앞에 붙어있는 UI를 보면 알다시피 NSObject를 상속받으면서 UIKit 프레임워크와 연결되어있어요

애플에 따르면 빨 주 노 같은 기본적인 색상에 대한 정의를 제공하고 있습니다.

일단 이것만봐서는 큰 차이가 없어보여요. 둘다 색상 데이터를 가지고 있다는 공통점은 알겠어요

# 🍊 차이점

- **UIColor**
    
    → 우리가 정말 많이 그동안 다루었던 UIKit 프레임워크의 하위 요소, 즉 User Interface를 다루는 곳에서 지정하는 색상
    
- **CGColor**
    
    → Core Graphics 프레임워크에서 사용하는 요소의 색상값을 사용할 때 CGColor로 지정
    

우리가 자주사용 하는 View는 UIView라는 UIKit프레임워크에 속한 요소라 BackGroundColor를 지정할 때 UIColor로 지정한것이고

뷰의 layer는 CG에서 다루는(그리는) 요소라 shadowColor, borderColor 등을 줄때에는 CGColor로 지정하는 것

# 🍊 ****예시

View의 테두리 색상을 지정하려면 layer.borderColor = UIColor.black.cgColor 

이렇게 접근을 해야합니다. UIColor로 색을 지정해주고 그 색상을 CGColor로 잡아주는 거에요.

borderColor는 CGColor를 상속받고 있거든요. 

→ 때문에 cgColor가 아니면 에러가 발생합니다. 

label, Button, View 모두 layer가 있기 때문에 Border를 줄 수가 있습니다.