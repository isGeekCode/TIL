# [Gesture Recognizer] Long Press

## 서론

핸드폰에서 지원하는 제스쳐란 그냥 단순하게 화면을 터치할 수도 있고, 길게 누를수도 있고, 두손가락으로 확대할 수 도 있고, 화면도 넘길 수 있다.

## **Declaration**

```swift
@MainActor class UILongPressGestureRecognizer : [UIGestureRecognizer](https://developer.apple.com/documentation/uikit/uigesturerecognizer)
```

## **Overview**

`[UIGestureRecognizer](https://developer.apple.com/documentation/uikit/uigesturerecognizer)`의 하위 클래스이다.

사용자는 작업이 트리거되기전에 뷰에서 하나이상의 손가락을 누르고 최소시간동안 손가락을 누르고 있어야한다.

그 시간동안 사용자의 손가락이 지정된 거리 이상 움직일 수 없고 실패하게 된다.

사용자가 **minimumPressDuration으로 설정한 시간**동안 **numberOfTouchesRequired( )로 설정한 만큼의 손가락 갯수**로 누르고 **allowableMovement로 설정한 터치허용범위**를 벗어나지 않으면 제스처가 시작됩니다( ). 제스처 인식기는 손가락이 움직일 때마다 **변경 상태로 전환**되고 **사용자가 손가락을 떼면( ) 종료**됩니다

`UILongPressGestureRecognizer` is a concrete subclass of `[UIGestureRecognizer](https://developer.apple.com/documentation/uikit/uigesturerecognizer)`.

The user must press one or more fingers on a view and hold them there for a minimum period of time before the action triggers. While down, the userʼs fingers canʼt move more than a specified distance or the gesture fails.

Long-press gestures are continuous. The gesture begins (`[UIGestureRecognizer.State.began](https://developer.apple.com/documentation/uikit/uigesturerecognizer/state/began)`) when the user presses the number of allowable fingers (`[numberOfTouchesRequired](https://developer.apple.com/documentation/uikit/uilongpressgesturerecognizer/1616425-numberoftouchesrequired)`) for the specified period (`[minimumPressDuration](https://developer.apple.com/documentation/uikit/uilongpressgesturerecognizer/1616423-minimumpressduration)`) and the touches do not move beyond the allowable range of movement (`[allowableMovement](https://developer.apple.com/documentation/uikit/uilongpressgesturerecognizer/1616427-allowablemovement)`). The gesture recognizer transitions to the Change state whenever a finger moves, and it ends (`[UIGestureRecognizer.State.ended](https://developer.apple.com/documentation/uikit/uigesturerecognizer/state/ended)`) when the user lifts any of the fingers.

## 선행 지식

스토리보드 사용경험

## 초기세팅

UIGestureRecognizer

[https://developer.apple.com/documentation/uikit/touches_presses_and_gestures/handling_uikit_gestures](https://developer.apple.com/documentation/uikit/touches_presses_and_gestures/handling_uikit_gestures)

**스토리보드로 구현**

제스쳐를 사용할 ViewController 에 UILongPressGestureRecognizer를 추가한다.

**코드로 구현** → 스토리보드에서 추가 안해도된다.

[https://developer.apple.com/documentation/uikit/touches_presses_and_gestures/handling_uikit_gestures/handling_long-press_gestures](https://developer.apple.com/documentation/uikit/touches_presses_and_gestures/handling_uikit_gestures/handling_long-press_gestures)

```swift
// Long Press Gesture - 선언
let longTouchGesture = UILongPressGestureRecognizer(target: self, action: #selector(longTouchAction(_:)))

// Long Press Gesture - 적용
view.addGestureRecognizer(panGestrue)
```

### LongTouchAction 함수

@objc는 selector로 사용하려면 써야하고, recognizer에서 제스쳐에 대한 정보를 가지고 있다

```swift
@objc
func longTouchAction(_ recognizer: UILongPressGestureRecognizer) {
    print(recognizer.state.rawValue)
}
```

## UIGestureRecognizer.State

```swift
// Declaration
enum State: Int
```

UIGestureRecognizer는 enum의 형태이고 자료형은 Int이기 때문에 switch를 사용하기 용이하다

아래처럼 세분화 되어있는데 많이 사용하는 것은 아래 세가지이다.

- .began : 롱프레스 시작을 알려줌
- .ended : 롱프레스 종료를 알려줌
- .changed : 롱프레스 후 변화

```swift
case possible
//The gesture recognizer has not yet recognized its gesture, but may be evaluating touch events. This is the default state.
case began
//The gesture recognizer has received touch objects recognized as a continuous gesture. It sends its action message (or messages) at the next cycle of the run loop.
case changed
//The gesture recognizer has received touches recognized as a change to a continuous gesture. It sends its action message (or messages) at the next cycle of the run loop.
case ended
//The gesture recognizer has received touches recognized as the end of a continuous gesture. It sends its action message (or messages) at the next cycle of the run loop and resets its state to UIGestureRecognizer.State.possible.
case cancelled
//The gesture recognizer has received touches resulting in the cancellation of a continuous gesture. It sends its action message (or messages) at the next cycle of the run loop and resets its state to UIGestureRecognizer.State.possible.
case failed
//The gesture recognizer has received a multi-touch sequence that it cannot recognize as its gesture. No action message is sent and the gesture recognizer is reset to UIGestureRecognizer.State.possible.
```

## .changed에서 사용하는 함수들

드래그 애니메이션에 사용

### location(in:\_)

**Summary**

Returns the point computed as the location in a given view of the gesture represented by the receiver.

**Declaration**

func location(in view: UIView?) -> CGPoint

**Discussion**

The returned value is a generic single-point location for the gesture computed by the UIKit framework. It is usually the centroid of the touches involved in the gesture. For objects of the UISwipeGestureRecognizer and UITapGestureRecognizer classes, the location returned by this method has a significance special to the gesture. This significance is documented in the reference for those classes.

**Parameters**

view

A UIView object on which the gesture took place. Specify nil to indicate the window.

**Returns**

A point in the local coordinate system of view that identifies the location of the gesture. If nil is specified for view, the method returns the gesture location in the window’s base coordinate system

**터치한 위치정보의 좌표를 알려준다. 어느View를 기준으로 할지 정해야한다.**

전체 화면에서의 xy좌표를 알면 좋겠지만, 특정 View 위에서 x,y가 몇인지 계산하기 복잡하니 기준점을 정하면 거기서 부터 계산된 값을 알려준다.

```swift
@objc
func longTouchAction(_ recognizer: UILongPressGestureRecognizer) {
    switch recognizer.state {
    case .began:
        // 롱터치 시작
        break
    case .ended:
        // 롱터치 종료
        break
    case .changed:
        // 터치 후 변화
        // 1
        let point: CGPoint = recognizer.location(in: self.view)
        // 2
        let point2: CGPoint = recognizer.location(in: self.longTouchView)
    default:
        // 나머지 불필요
        break
    }
}
```

위에 주석 `1`은 `self.view`기준으로 x,y를 알려주는 값이고

위에 주석 `2`는 `self.panGetstureView` 기준으로 x,y를 알려주는 값이다.(마치 view의 frame과 bound 차이 처럼)

그럼 여기서 `point`와 `.changed`를 잘 생각해보자,`.began`과 `.ended`는 한번만 호출되지만 `.changed`는 바뀔때마다 호출이 된다.

한마디로 롱터치 시작 후 **변화**되는 **위치값**을 알 수 있다.이를 이용하면, 위에 GIF와 같이 롱터치후 변화 되는 값에 따라 `view`를 이동시켜줄 수 있다는 말이 된다!

(잘 이해가 안된다면 위 코드에서 `point`와 `point2`를 주석걸고 `print`해서 x, y값에 대해 보면 이해에 도움이 될 것 같다.)

드래그관련 추가적인 블로그

[https://jiseobkim.github.io/swift/ui/2020/03/25/swift-DragAnimation_Step2_Transform.html](https://jiseobkim.github.io/swift/ui/2020/03/25/swift-DragAnimation_Step2_Transform.html)

### 탭틱과 햅틱

탭틱 : 압력 센서를 통해 압력을 주는 경우 동작되는 원리이며 이를 탭틱 엔진으로 피드백 하는 방식

햅틱 : 압력을 통해 동작되는 원리가 아닌 Long press (S/W로 구현)를 통해 동작되는 원리이며 이를 진동으로 피드백 하는 방식

iPhone XR을 시작으로 새로운 모델들이 모두 3D Touch 없이 Haptic Touch만 가능하며 기존 3D Touch를 지원하는 모델도 HapticTouch로 전환됨

iPhone 6s에 3D Touch가 최초 적용 당시 압력 감도를 인식한다하여 삼차원 터치라고 불렸던 경우도 있었다.

햅틱 터치는 3D 터치가 작동하는 모든 곳에서 작동한다.

add

```swift
class ViewController: UIViewController {

    @IBOutlet weak var button: UIButton!

    override func viewDidLoad() {
        super.viewDidLoad()

        // add guesture recognizer
        let longPress = UILongPressGestureRecognizer(target: self, action: #selector(longPress(_:)))
        self.button.addGestureRecognizer(longPress)
				// 추가작업

    }

@objc func longPress(_ guesture: UILongPressGestureRecognizer) {
        if guesture.state == UIGestureRecognizerState.began {
            print("Long Press")
        }
    }

@IBAction func normalButtonTap(sender: UIButton) {
        print("Button tapped")
    }
}
```

\***\*Configuring the Gesture Recognizer\*\***

**minimumPressDuration: TimeInterval**

제스처가 인식되기 위해 사용자가 보기를 눌러야 하는 최소 시간입니다.

The minimum time that the user must press on the view for the gesture to be recognized.

**numberOfTouchesRequired: Int**

제스처 인식을 위해 뷰를 터치해야 하는 손가락의 수입니다.

The number of fingers that must touch the view for gesture recognition.

**numberOfTapsRequired: Int**

제스처 인식에 필요한 보기의 탭 수입니다.

The number of taps on the view necessary for gesture recognition.

**allowableMovement: CGFloat**

제스처가 실패하기 전에 보기에서 손가락의 최대 움직임입니다.

The maximum movement of the fingers on the view before the gesture fails.

다른 제스쳐

\***\*Standard Gestures\*\***

[Handling UIKit Gestures](https://developer.apple.com/documentation/uikit/touches_presses_and_gestures/handling_uikit_gestures)

Use gesture recognizers to simplify touch handling and create a consistent user experience.

[Coordinating Multiple Gesture Recognizers](https://developer.apple.com/documentation/uikit/touches_presses_and_gestures/coordinating_multiple_gesture_recognizers)

Discover how to use multiple gesture recognizers on the same view.

`[class UIHoverGestureRecognizer](https://developer.apple.com/documentation/uikit/uihovergesturerecognizer)`

A discrete gesture recognizer that interprets pointer movement over a view.

`[class UIPanGestureRecognizer](https://developer.apple.com/documentation/uikit/uipangesturerecognizer)`

A discrete gesture recognizer that interprets panning gestures.

`[class UIPinchGestureRecognizer](https://developer.apple.com/documentation/uikit/uipinchgesturerecognizer)`

A discrete gesture recognizer that interprets pinching gestures involving two touches.

`[class UIRotationGestureRecognizer](https://developer.apple.com/documentation/uikit/uirotationgesturerecognizer)`

A discrete gesture recognizer that interprets rotation gestures involving two touches.

`[class UIScreenEdgePanGestureRecognizer](https://developer.apple.com/documentation/uikit/uiscreenedgepangesturerecognizer)`

A discrete gesture recognizer that interprets panning gestures that start near an edge of the screen.

`[class UISwipeGestureRecognizer](https://developer.apple.com/documentation/uikit/uiswipegesturerecognizer)`

A discrete gesture recognizer that interprets swiping gestures in one or more directions.

`[class UITapGestureRecognizer](https://developer.apple.com/documentation/uikit/uitapgesturerecognizer)`

A discrete gesture recognizer that interprets single or multiple taps.

[Supporting Gesture Interaction in Your Apps](https://developer.apple.com/documentation/uikit/touches_presses_and_gestures/supporting_gesture_interaction_in_your_apps)

Enrich your app’s user experience by supporting standard and custom gesture interaction.

![스크린샷_2022-03-25_오전_8 36 59](https://user-images.githubusercontent.com/76529148/160081034-481eb1bf-2ca4-4b38-a43a-447216b1208d.png)
