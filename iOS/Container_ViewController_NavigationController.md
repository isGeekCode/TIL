# Container ViewController Type - Navigation Controller

네비게이션 컨트롤러는 ViewController의 타입 중 Container ViewController Type에 속한다.

이 컨테이너 뷰컨트롤러에는 TabBar ViewController또한 포함된다.

## ViewController Type

ViewController는 두가지 타입이 존재한다.

- Content ViewController Type:
- Container ViewController Type: NavigationViewController / TabBarViewController 처럼 여러개의 ViewController를 제어하는 ViewController

## 네비게이션 인터페이스

아래 그림은 iOS에서 정말 많이 사용하는 인터페이스이다. 주로 계층적 구조의 화면전환을 위해 사용되는 드릴다운 인터페이스이다.

![스크린샷 2022-03-22 오후 1.32.04.png](assets/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-03-22_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_1.32.04.png)

네비게이션 인터페이스를 구현하기위해서는 네비게이션 컨트롤러가 필요하다.

네비게이션 컨트롤러는 2개의 뷰를 나타낸다. 하나는 네비게이션 바( 혹은 툴바)이고 다른 하나는 **네비게이션 스택**에 쌓일 컨텐츠뷰이다.

![스크린샷 2022-03-22 오후 1.40.48.png](assets/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-03-22_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_1.40.48.png)

StoryBoard의 라이브러리에서 NavigationController를 선택하여 사용하고

기존의 ViewController를 사용하려면 editor - embed In 을 보면 Navigation / Tab Bar를 선택할 수 있다.

![스크린샷 2022-03-22 오후 1.41.33.png](assets/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-03-22_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_1.41.33.png)

Navigation컨트롤러를 이용하여 View를 이동하면 네이게이션 스택에 쌓이게된다.

여기서 스택의 각각의 위치에 있는 뷰를 컨트롤 할 수가 있다.

```swift
// AppDelegate에서 RootViewController 구현하기

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
        // Override point for customization after application launch.

        // 루트 뷰 컨트롤러가 될 뷰 컨트롤러를 생성합니다.
        let rootViewController = UIViewController()
        // 위에서 생성한 뷰 컨트롤러로 내비게이션 컨트롤러를 생성합니다.
        let navigationController = UINavigationController(rootViewController: rootViewController)

        self.window = UIWindow(frame: UIScreen.main.bounds)
        // 윈도우의 루트 뷰 컨트롤러로 내비게이션 컨트롤러를 설정합니다.
        self.window?.rootViewController = navigationController
        self.window?.makeKeyAndVisible()

        return true
    }

// 내비게이션 스택에 있는 최상위 뷰 컨트롤러에 접근하기 위한 프로퍼티입니다.
var topViewController: UIViewController?

// 현재 내비게이션 인터페이스에서 보이는 뷰와 관련된 뷰 컨트롤러에 접근하기 위한 프로퍼티입니다.
var visibleViewController: UIViewController?

// 내비게이션 스택에 특정 뷰 컨트롤러에 접근하기 위한 프로퍼티입니다.(루트 뷰 컨트롤러의 인덱스는 0 입니다.)
var viewController: [UIViewController]

// 내비게이션 스택에 뷰 컨트롤러를 푸시합니다.
// 푸시 된 뷰 컨트롤러는 최상위 뷰 컨트롤러로 화면에 표시됩니다.
func pushViewController(UIViewController, animated: Bool)

// 내비게이션 스택에 있는 최상위 뷰 컨트롤러를 팝합니다.
// 최상위 뷰 컨트롤러 아래에 있던 뷰 컨트롤러의 콘텐츠가 화면에 표시됩니다.
func popViewController(animated: Bool) -> UIViewController?

// 내비게이션 스택에서 루트 뷰 컨트롤러를 제외한 모든 뷰 컨트롤러를 팝합니다.
// 루트 뷰 컨트롤러가 최상위 뷰 컨트롤러가 됩니다.
// 삭제된 모든 뷰 컨트롤러의 배열이 반환됩니다.
func popToRootViewController(animated: Bool) -> [UIViewController]?

// 특정 뷰 컨트롤러가 내비게이션 스택에 최상위 뷰 컨트롤러가 되기 전까지 상위에 있는 뷰 컨트롤러들을 팝합니다.
func popToViewController(_ viewController: UIViewController,
        animated: Bool) -> [UIViewController]?
```

네비게이션 바에 관련된 애플 문서를 살펴보면

## **Navigation Bar Titles**

- **내비게이션 바에 현재 뷰의 제목을 보여주세요.**
  - 하지만 만약 내비게이션 바에 제목을 추가하는 것이 중복되는 행동이라면 제목은 비워두어도 좋습니다.
  - 예를 들어, Notes 앱은 컨텐츠에 첫 라인에 현재 뷰에 대한 정보를 제공하므로 내비게이션 바에 제목을 비워둡니다.
- **현재 뷰의 정보를 더 강조하고 싶다면 큰 크기의 제목을 사용하세요.**
  - 어떤 앱에서는 큰 볼드체의 텍스트로 작성된 제목이 사람들이 탐색을 하거나 검색을 할 때를 돕습니다.
  - 예를 들어, tabbed layout 에서는 큰 제목이 명료하게 탭이 활성화 되어있음을 알리고 사람들에게 가장 위로 스크롤 해야된다는 것을 알립니다. Phone 앱이 이런 접근을 사용합니다. Music 앱은 앨범, 아티스트, 플레이리스트, 라디오와 같은 컨텐츠 영역과 구분 짓는 용도로 큰 제목을 사용합니다.
  - iOS 13 이상에서는 큰 제목의 내비게이션 바는 배경 요소나 그림자효과를 기본값으로 가지지 않습니다. 또한, 사용자가 컨텐츠를 스크롤하기 시작하면 큰 제목에서의 일반 제목으로의 전환효과가 일어납니다.
  - 개발자 가이드: [prefersLargeTitles](https://developer.apple.com/documentation/uikit/uinavigationbar/2908999-preferslargetitles)
- **큰 제목의 네비게이션 바를 사용할 때는 테두리를 숨기세요.**
  - iOS 13 이상에서는 내비게이션 바의 하단 테두리의 그림자효과를 없애는 것으로 숨길 수 있습니다(테두리는 사용자가 컨텐츠 영역을 스크롤 하면 자동으로 다시 나타납니다).
  - 테두리가 없는 스타일은 기존의 표준 네비게이션 바와는 잘 어울리지 않습니다. 네비게이션바의 제목과 버튼이 명확하게 보이지 않을 수 있습니다.
  - iPad에서의 Split View는 예외적인 상황으로 나누어진 두 뷰의 일관성을 유지하기 위해 두 뷰에 모두 테두리가 없는 스타일을 적용할 수 있습니다.

## Navigation Bar Controls

- **네비게이션 바가 지나치게 많은 control로 복잡해지지 않도록 해야 합니다.**
  - 일반적으로 내비게이션 바는 현재 뷰의 제목, 뒤로가기 버튼과 하나의 control 외의 요소들을 포함하지 않습니다.
  - 내비게이션 바에 segmented control을 사용하고자 한다면, 그 내비게이션 바는 segmented control 외의 제목이나 다른 control등의 요소들을 포함해서는 안됩니다.
- **표준 뒤로 가기 버튼을 사용하세요.**
  - 만약 커스텀 버튼을 만든다고 하더라도 다른 인터페이스들과 일관성이 있도록 여전히 표준과 비슷한 모양을 유지해야 합니다.
- **여러 개의 Breadcrumb Path를 사용하면 안 됩니다.**
  - 뒤로 가기 버튼은 항상 이전 화면으로 돌아가는 하나의 동작만을 수행해야 합니다. 만약 당신이 사용자들이 페이지의 모든 경로를 알아야 한다고 생각한다면, 앱의 계층구조를 단순하게 하는 것을 고려해야 합니다.
- **텍스트 버튼에게는 충분한 공간을 확보해주세요.**
  - 만약 내비게이션 바에 여러 개의 텍스트 버튼을 추가한다면, 텍스트 버튼이 알아보기 힘들 수도 있습니다.
  - 버튼 사이에 고정된 공간을 부여해서 구분되도록 만들어주어야 합니다.
  - 개발자 가이드: [UIBarButtonSystemItemFixedSpace /](https://developer.apple.com/documentation/uikit/uibarbuttonsystemitem/uibarbuttonsystemitemfixedspace) [UIBarButtonItem](https://developer.apple.com/documentation/uikit/uibarbuttonitem)
- **앱의 정보 계층을 단순화하기 위해 Segmented Control의 사용을 고려해야 합니다.**
  - 만약 내비게이션 바에 Segmented Control을 사용한다면, 최상위 계층에서만 사용하세요.
  - 그리고 하위 계층에서는 적절한 뒤로 가기 버튼 제목을 선정해야 합니다.

우리눈에 보여지는 화면은 스택에 따라 바뀌는데 네비게이션바는 네비게이션 컨트롤러에 종속된 뷰 전체가 공유한다. 내비게이션바는 내비게이션 컨트롤러에 의해 생성되고, 최상위 뷰 컨트롤러가 변경될 때마다 내비게이션바가 업데이트 된다.

**가운데** : 네비게이션 바 타이틀

**양옆**: 네비게이션 아이템

![스크린샷 2022-03-22 오후 1.51.41.png](assets/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-03-22_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_1.51.41.png)

### **UINavigationController Class**

- init

```
// 내비게이션 컨트롤러의 인스턴스를 생성, 매개변수로 루트 뷰 컨트롤러를 넘겨줍니다.
init(rootViewController: UIViewController)
```

- property

```swift
// 내비게이션 스택의 최상위 뷰 컽트롤러에 접근하기 위한 property
var topViewController: UIViewController?
// 현재 내비게이션 인터페이스에서 보이는 뷰와 관련된 뷰 컨트롤러에 접근하기 위한 property
var visibleViewController: UIViewController?
// 내비게이션 스택에 특정 뷰 컽트롤러에 접근하기 위한 property
var viewController: [UIViewController]
```

- method

```swift
// 내비게이션 스택에 뷰 컨트롤러를 push
func pushViewController(UIViewContoller, animated: Bool)
// 내비게이션 스택 최상위 뷰 컨트롤러를 pop
func popViewController(animated: Bool) -> UIViewController?
// 내비게이션 스택에서 루트 뷰 컨트롤러를 제외한 모든 뷰 컨트롤러를 pop
func popToRootViewController(animated: Bool) -> [UIViewController]?
// 특정 뷰 컨트롤러가 내비게이션 스택의 최상위 뷰 컨트롤러가 되기 전까지 pop
func popToViewController(_ viewController: UIViewController, animated: Bool) -> [UIViewController]?
```

- code를 이용한 Navigation Interface

```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
        // Override point for customization after application launch.

        // 루트 뷰 컨트롤러가 될 뷰 컨트롤러를 생성합니다.
        let rootViewController = UIViewController()
        // 위에서 생성한 뷰 컨트롤러로 내비게이션 컨트롤러를 생성합니다.
        let navigationController = UINavigationController(rootViewController: rootViewController)

        self.window = UIWindow(frame: UIScreen.main.bounds)
        // 윈도우의 루트 뷰 컨트롤러로 내비게이션 컨트롤러를 설정합니다.
        self.window?.rootViewController = navigationController
        self.window?.makeKeyAndVisible()

        return true
    }
```

네비게이션 바 코드로 생성하기

```swift
//UIView를 생성해 frame으로 위치를 잡아줌
func setNC() {
    let view = UIView(frame: CGRect(x:0,y: 0, width: 200, height: 40))

    view.backgroundColor = .brown
    view.layer.borderWidth = 3

//네비게이션바의 Title부분은 View로 되어있다.
    self.navigationItem.titleView = View
```

내비게이션 바 버튼 아이템은 하나만 있는 게 양쪽에. leftButtonItem, 과. rightButtonItem으로 나눠져 있다.

1. barButtonSystemItem - 바 버튼의 타입을 지정합니다. 일부 특정 타입에 미리 준비된 아이콘을 제공하므로 제공하는 바버튼 타입을 지정해주면 됩니다.
2. target - 호출할 메서드가 있는 인스턴스입니다.
3. Action - 버튼을 클릭했을 때 호출하는 메서드입니다.

바 버튼 아이템은 UIBarButtonItem(customView: UIView)같이 초기화 메서드도 제공을 합니다. 이 초기화 메서드를 통해 뷰 객체에 바 버튼을 생성할 수 있습니다.

```swift

let v = UIView(frame:CGRect(x:0,y: 0, width: 200, height: 40))
let rbtn = UIBarButtonItem(customView: v)

self.navigationItem.rightBarButtonItem = rItems

let label = UILabel(frame:CGRect(~))

v.addSubView(label)
```

이런 식으로 코드를 보면은 UIView(frame:)을 통해서 UIView를 생성해주고 해당 뷰안에 UILabel을 넣어 위치를 잡아준 뷰를 생성해주었습니다.

또 해당 뷰를 UIBarButtonItem(customView:)를 통해서 뷰 객체를 넣은 바 버튼을 생성할 수 있고. rightBarButtonItem을 통해 오른쪽에 있는 barButtonItem에 넣어줬습니다

### 네비게이션 바 감추기

**스토리보드 이용하기**

1. 스토리보드의 네비게이션 컨트롤러 클릭
2. 우측 Attributes Inspector에서 Shows Navigation Bar 해제

![스크린샷 2022-03-22 오후 2.00.07.png](assets/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-03-22_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_2.00.07.png)

코드이용하기

```swift
// 네비게이션 컨트롤러로 연결되어있는 컨트롤러에 접근
self.navigationController?.isNavigationBarHidden = true
```

### **Navigation View Conversion**

UINavigationController 클래스의 method 또는 세그(segue)를 사용하여 스택의 뷰 컨트롤러를 추가(push) / 삭제(pop) 할 수 있습니다.
