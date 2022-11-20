# UIView

## View & Window

View란 앱의 사용자 인터페이스를 구성한다.

- View는 UIView의 인스턴스거나 UIView 하위 클래스의 인스턴스이다.
- 자신을 어떻게 그리는지 알고 있다.
- 터치와 같은 이벤트들을 처리할 수 있다.
- 뷰 계층 구조상에 존재한다. 뷰 계층 구조의 루트는 앱의 윈도우 이다.

iOS 앱은 모든 View 들의 컨테이너 역할을 하는 **UIWindow 인스턴스**
를 가지는데 이는 AppDelegate에 정의되어 있으며`(SceneDelegate를 사용하는 경우는 SceneDelegate에 정의)`

UIWindow 는 UIView 의 하위 클래스 이므로 *Window 는 그 자체가 View*라고 할 수 있다.

최초의 window는 스토리보드를 사용할 때는 자동으로 생성이 되지만 코드로 구현할 때는

1. 먼저 Main 으로 되어 있던**Info.plist** 의 항목을 지워야 한다. 프로젝트를 생성할 때 자동으로 Xcode는 Main.storyboard를 통해 메인 window 객체를 만들고 **_rootViewController_**를 설정하게 되어 있다.

- rootViewController : 현재 앱의 가장 밑 부분에 있는 Controller, 즉 앱을 켰을때 처음 실행되는 뷰 컨트롤러라고 생각하면 됩니다
  아래 부분을 삭제
  ![스크린샷 2022-03-15 오후 2.56.34.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/143c1f60-827a-43da-a102-b85fe5cbefbf/스크린샷_2022-03-15_오후_2.56.34.png)

1. AppDelegate.swift 파일에 Window 객체를 생성하고 넣어주도록 한다.

   ```swift
   var window: UIWindow?
   window = UIWindow.init(frame: UIScreen.main.bounds)
   ```

2. window 객체는 그저 뷰를 보여주는 컨테이너 역할이기 때문에 rootViewController를 만들고 설정해야만 뷰가 제대로 나오는 것을 확인할 수 있다
3. rootViewController 를 만들고도 시뮬레이터에 검은 화면만 나온다면 이것은 window가 keyWindow가 아니기 때문

   ```
   window.makeKeyAndVisible()
   ```

## **뷰의 계층구조(View hierarchy)**

![스크린샷 2022-03-15 오후 3.00.27.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e9133792-0e0a-4b1f-994c-6e5a191b88da/스크린샷_2022-03-15_오후_3.00.27.png)

- 앱이 시작되면 윈도우가 생성되고 그 윈도우에 다른 뷰들을 추가하는게 가능해진다.
- Window에 추가한 View들을 Window의 하위뷰 (subView)라고 한다.
- Window의 SubView들은 자신의 SubView를 가질 수 있는데 그것들이 Window를 root로 한 뷰객체들의 계층구조라고 할 수 있다.

# ViewController

- MVC(Model-View-Controller) 디자인 패턴에서, View Controller는 스크린에 나타나는 정보를 보여주는 View 객체와 앱의 콘텐츠를 저장하는 data 객체를  관리한다.
- 이 중 ViewController는 뷰 계층과 해당 뷰들을 최신 상태로 유지하는데 필요한 정보를 관리하는 역할을 하게 된다.
- 모든 UIKit은 앱의 콘텐츠를 표시하기 위해 View Controller에 크게 의존하며 뷰와 UI 관련 로직을 관련하기 위해 Custom View Controller를 자주 정의하게 된다. (UIKIt이란 UI를 담당하는 프레임워크를 말한다!)
- 우리가 생성한 Custom View Controller의 대부분은 View Controller가 모든 뷰를 소유하고 다른 뷰들과의 상호 작용을 관리하는 **_Content View Controller_** 다. 이때 자신의 모든 View들을 ViewController가 스스로 관리한다.
  ![스크린샷 2022-03-15 오후 3.05.46.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/953ea1cb-9b2e-4887-afe3-048ee5c83703/스크린샷_2022-03-15_오후_3.05.46.png)

## ViewController에 View추가

- UIViewController는 뷰 계층 구조에서 root view 역할을 하고 view property를 통해 접근할 수 있는 content view를 포함하고 있다.
- 이 root view에서는 인터페이스에 보여줘야 할 필요한 custom view를 추가하는 것이 가능하다
- 스토리보드에서 추가하기 위해서는 View Controller에 드래그 함으로써 뷰를 추가할 수 있다
- UIButton이나 UIImageView 등 모든 View들이 들어가는 View를 rootView라고 한다.
- 스토리보드에서 구현하는 경우는 AutoLayout을 통해 사이즈와 위치를 지정해 주어야 빌드했을 때 보여진다.

## **Store References to Important Views**

앱을 실행할 때 ViewController의 코드에서 View에 접근하게 된다.

- View계층에서 View를 참조하기위해서는 ViewController의 Property인 outlet을 사용해 접근한다.
- outlet키워드를 통해 스토리보드에서 해당 프로퍼티를 인지한다.
- 모든 View요소들을 추가하지 않아도되고 앱실행중 업데이트가 필요한 요소들만 참조해도 된다.
- 몇 몇 View요소는 Protocol을 준수해야하는 경우도 있다.

## Handle Event Occuring in Views ans Controls

- ViewController가 이벤트의 발생을 알기 위해서는 View와의 상호작용을 알 수 있는 방법을 사용해야한다.
  - ViewController에 Action Method 혹은 Delegate를 구현한다.
  - ViewControlle의 extension을 이용하여 Action Method 혹은 Delegate를 구현한다.
    → 이벤트처리하는 코드로 분리하면서 해당코드의 유효성 테스트가 용이
  - 전용 객체를 만들어 Delegate와 ActionMethod를 분리하여 관련 정보를 ViewController로 전달하는 방법
    → 유연성과 재사용성에 좋음

## Prepare Your Views to Appear Onscreen

UIKit은 화면에 View를 표시할 때, 다음과 같은 순서로 해당 View를 로드하고 구성한다.

1. 해당뷰의 init(coder:) 메서드를 사용하여 객체 생성
2. ViewController에서 해당하는 action 및 outlet을 View에 연결한다.
3. 각 View와 ViewController의 awakeFromNib() 메서드를 호출한다.

   `* awakeFromNib() 메소드의 경우는 View가 호출되고 해당하는 subview가 할당되고 초기화 됐을때 호출.`

4. ViewController의 View property에 View 계층을 할당한다.
5. View의 생명주기에 따른 메서드를 호출한다.

## ViewController Type

ViewController는 두가지 타입이 존재한다.

- Content ViewController Type:
- Container ViewController Type: NavigationViewController / TabBarViewController 처럼 여러개의 ViewController를 제어하는 ViewController

- Content ViewController Type

  - 일반적인 interface요소로 사용하는 ViewController
  - 앱의 contents의 일부분을 관리 혹은 자신의 모든 View는 스스로 관리한다. (Design Pattern에 따라다름)

- Container ViewController Type
  - NavigationViewController / TabBarViewController 처럼 여러개의 ViewController를 제어하는 ViewController
  - 다른 ViewController들로부터 정보를 모은다.
  - 자신의 View들과 자식ViewController들의 rootView들을 관리한다.
  - 직접 자식ViewController의 Contents를 관리하지는 않고 rootView의 크기조저로가 위치조절에 대해서만 관리

## ViewController 간의 연동

- ViewController에는 생명주기가 존재한다.
- ViewController사이에서는 전환이 가능하고 이전 ViewController의 View가 유지가 될수도 , 안될 수도 있다.
- 그 해당시점을 이벤트화하여 생명주기에 따른 메서드를 지정할 수 있다.

## LifeCycle Method

- ViewDidLoad()
- viewWillAppear()
- viewDidAppear()
- viewWillDisAppear()
- viewDidDisappear()

- ViewDidLoad()
  1.  뷰컨트롤러의 `var view: UIView!`프로퍼티는 지연로딩된다. view가 필요로 될 때 view가 nil이면 `loadView()` 메소드를 호출하여 view를 로드
  2.  **`loadView()`직후**에 호출되는 콜백메소드
- viewWillAppear()
  뷰컨트롤러의 root view 가 로드된 이후에 **window 의 뷰 계층으로 더해지기 직전** 호출되는 메소드이다.
- viewDidAppear()
  window 의 root view가 **뷰 계층으로 더해진 직 후** 호출되는 메소드이다.
- viewWillDisAppear()
  window 의 root view가 **뷰 계층에서 제거되기 직 전** 호출되는 메소드이다.
- viewDidDisappear()
  window 의 root view가 **뷰 계층에서 제거된 직 후** 호출되는 메소드이다.

![스크린샷 2022-03-15 오후 4.06.36.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/aa2b4970-3545-421d-9a86-89c677f9d9a2/스크린샷_2022-03-15_오후_4.06.36.png)

정리

- **뷰 컨트롤러**는 **데이터 객체와 뷰 사이의 중개자**이다.
- 뷰 컨트롤러와 모델(데이터 오브젝트)의 책임을 깔끔하게 분리하는 걸 유지 해야한다.
- **뷰 컨트롤러는** **Responder객체**이고 Responder Chain 에 연결된다. 따라서 view controller 도 **이벤트 헨들링**을 할 수있다.

# 화면전환 Presentation Style

View의 전환방식은 present, navigation, segue 방식으로 할수 있는데 다시 이 화면을 전환하는 방식들은 크게 두가지 → Present, Show(push) 의 형식으로 나뉜다.

UIViewController 클래스에 두가지 메서드 presentViewController 와 showViewController 가 있다.

presentViewController는 새로운 뷰를 모달 방식으로 보여준다. 이와 비슷하게 showViewController를 이용하면 기본적으로는 모달 방식으로 새로운 뷰를 나타낸다. 그러나 여러가지 유연한 방법을 제공하기 때문에 서브뷰로 보여주는 등의 넓은 선택지를 제공한다.

## Modal이란?

- 다른 화면을 띄워서 시선을 끌게 만드는 방식
- 딱 눈에 들어와야 하는 컨텐츠를 담는데 사용
- 사용: ViewController객체.present(객체)

**present**

- 잠깐 나타났다가 다시 원래대로 돌아오는 로직에 사용한다.
- present로 띄우고, Dismiss로 제거한다.
- present시 View가 disappear가 호출되지않으며 Dismiss할때, 다시 appear가 호출되지않는다.
- present방식은 뒤로가기가 따로 생기지 않아 개발할 때, 직접 구현해줘야한다.

**show (push)**

stack방식으로 쌓아가는 방식이다.

- show(push)로 띄우고, pop으로 제거한다.

### 1-2. Style

앱에 가장 잘 어울리는 스타일을 골라서 modalPressentationStyle 프로퍼티에 상수값을 넣어준다.

- UIModalPresentationFullScreen - 전체 화면을 완전히 덮어 **화면 전체에 새로운 뷰를 보여주는 방식**의 프레젠테이션 스타일. 흔하게 사용한다.
- UIModalPresentationCurrentContext
  - FullScreen 스타일이 전체 화면을 덮는 방식이라면 ( 장치 스크린의 크기에 대응된다 ), CurrentContext 스타일은 **현재 뷰에 대응해 새로운 뷰를 보여주는 방식**이다. 만약에 화면의 뷰를 작게 만들었다면, CurrentContext로 올려준 뷰도 작은 크기로 나오게 됩니다. 스플릿 뷰 등을 통해 화면을 분할한 상태여서 뷰가 스크린 크기보다 작을 때 사용하는 스타일.
- UIModalPresentationOverFullScreen / OverCurrentContext
  - 새로 생성하는 뷰의 투명도(알파값)를 정해 기존의 뷰를 볼 수 있는 스타일.
  - 위의 프레젠테이션 스타일들은 아래에 깔리는 뷰를 context에서 삭제해버리고 위에 새로운 뷰로 덮어버리지만, 이 두 스타일들은 **기존 뷰를 그대로 남겨두고 위에 뷰를 덮기 때문에 투명도를 조절해 반투명 상태로 만들어주면 새로운 뷰 아래에 기존 뷰를 볼 수 있다.**
- UIModalPresentationPageSheet
  - 뷰의 가로를 늘이지 않고 그대로 보여주는 프레젠테이션 스타일.
- UIModalPresentationFormSheet
  - 화면 가장자리에서 상하좌우 모두 여백을 가지고 섬처럼 떠있는 방식의 프레젠테이션 스타일.
- UIModalPresentationPopover
  - 팝오버뷰로 새로운 뷰를 나타내는 방식.
  - 주로 **추가 정보, 선택한 것에 대한 추가 옵션** 등을 나타내는데 사용. `iPad 기기에서만 지원.`

**FullScreen 스타일 3종류**

뒤 2개가 전체를 덮지 않는데도 FullScreen 인 이유는 뒷배경은 어둡거나 흐리게 처리되기 때문

![img1.daumcdn.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a8f809a4-fd31-415e-bf99-4ea6068e0fe1/img1.daumcdn.png)

**Popover 스타일.**

이것도 배경이 어두워지기에 FullScreen 스타일이다.

![img1.daumcdn-2.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cb3d3c0f-897b-4c7c-a7aa-1a6c5b2fc396/img1.daumcdn-2.png)

### 1-3 Transition Style

전환 스타일은 새로운 뷰를 골라준 스타일로 present 할 때, 어떤 애니메이션을 사용할 지를 결정하는 스타일이다. 표시할 뷰 컨트롤러의 modalTransitionStyle 프로퍼티에 원하는 전환 스타일을 지정해 변경 가능하다.

- Cover Vertical - 화면 하단에서부터 **새로운 뷰가 수직으로 올라오는** 트랜지션 스타일.
- Flip Horizontal - 화면의 가운데 수직선을 기준으로 **뷰를 뒤집는 듯한** 트랜지션 스타일.
- Cross Dissolve - 화면 전체가 흐려지며 **빠르게 전체화면이 새로운 뷰로 바뀌는** 트랜지션 스타일.
- Partial Curl - 세로로 제본된 책의 한 **페이지를 위로 넘기는 듯한** 트랜지션 스타일.

[https://ios-development.tistory.com/206](https://ios-development.tistory.com/206)

## 2. Presenting && Showing

### 2-1. Present 방식

인터페이스 빌더(스토리보드를 이용하는 걸 말하는 것 같네요)에서 세그웨이를 보면, 정보를 사용하여 뷰 컨트롤러를 인스턴스화해서 표시해줍니다. 또는, 뷰 컨트롤러 스크립트에서 showViewController, showDetailViewController메서드를 이용해서 뷰를 보여줄 수 있습니다. presentViewController를 이용하면 모달 방식으로 보여줄 수도 있습니다.

### Present - Move

```swift
// 스토리보드
import UIKit

class ViewController: UIViewController {

    @IBAction func moveNext(_ sender: Any) {

        // 스토리 보드 객체 가져오기 (인자 : 이름, 읽어들일 위치)
        let storyboard: UIStoryboard? = UIStoryboard(name: "Main", bundle: Bundle.main)

        // 뷰 객체 얻어오기 (storyboard ID로 ViewController구분)
        guard let uvc = storyboard?.instantiateViewController(identifier: "SecondVC") else {
            return
        }

        // 화면 전환 애니메이션 설정
        uvc.modalTransitionStyle = UIModalTransitionStyle.coverVertical

        self.present(uvc, animated: true)
    }
}

// programming

```

### Dismiss - Back

```swift
//스토리보드
import UIKit
class ScondViewController : UIViewController {
    @IBAction func back(_ sender: Any) {
        self.presentingViewController?.dismiss(animated: true)
    }
}

//programming
self.presentingViewController?.dismiss(animated: true)
```

참고

[https://o-o-wl.tistory.com/43](https://o-o-wl.tistory.com/43)

### 2-2 Show 방식

show, showDetailViewController 메서드를 사용합니다. 나타낼 뷰 컨트롤러 인스턴스(object)를 만들고, modalPresentationStyle 프로퍼티, modalTransitionStyle 프로퍼티를 원하는 스타일로 골라준다. 그 다음 현재 뷰 컨트롤러에서 showViewController 또는showDetailViewController 를 이용해 인스턴스를 호출해 뷰를 화면에 나타내주면 된다.

[https://h1guitar.tistory.com/16](https://h1guitar.tistory.com/164)

### NavigationController를 이용한 화면전환

[https://0urtrees.tistory.com/43](https://0urtrees.tistory.com/43)

### Segue를 연결하는 3가지 방법

스토리보드에서 segue를 지정하는 화면

![https://blog.kakaocdn.net/dn/bxS8b9/btqxcNpkJtC/JJeckcoUNgnjw8xORkkoSk/img.png](https://blog.kakaocdn.net/dn/bxS8b9/btqxcNpkJtC/JJeckcoUNgnjw8xORkkoSk/img.png)

[https://h1guitar.tistory.com/163](https://h1guitar.tistory.com/163)

참고

[https://zeddios.tistory.com/828](https://zeddios.tistory.com/828)

[https://zeddios.tistory.com/831](https://zeddios.tistory.com/831)

[https://ios-development.tistory.com/19](https://ios-development.tistory.com/19)

[https://etst.tistory.com/87](https://etst.tistory.com/87)

[https://0urtrees.tistory.com/43](https://0urtrees.tistory.com/43)

[https://h1guitar.tistory.com/164](https://h1guitar.tistory.com/164)

[https://h1guitar.tistory.com/163](https://h1guitar.tistory.com/163)
