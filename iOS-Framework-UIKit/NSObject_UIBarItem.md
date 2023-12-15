# NSObject_UIBarItem_UIBarButtonItem & UITabBarItem : 네비게이션바 / 툴바 / 탭바를 표시하는 아이템

NSObject 의 UIBarItem은 iOS 애플리케이션에서 사용되는 클래스 중 하나로,

네비게이션 바, 툴바, 탭 바 등에 표시되는 아이템을 나타내는 추상 클래스이다.

UIBarItem 클래스는 구체적으로 구현된 것이 아니기 때문에, 이를 상속받는 구체적인 서브클래스를 사용해야 한다. 구체적인 서브클래스로는 UIBarButtonItem, UITabBarItem 등이 있으며, 이들은 각각 네비게이션 바/툴바 아이템, 탭 바 아이템을 나타낸다.

<br><br>

## UIBarButtonItem
UIBarButtonItem은 UIToolBar와 UINavigationBar에 세팅할 수 있는 Item 이다.   
  
UIBarItem 클래스는 텍스트, 이미지, 뷰 등의 속성을 가지며, 이를 설정하여 아이템의 모양을 변경할 수 있다.  
또한 isEnabled 속성을 통해 아이템을 활성화/비활성화할 수 있다.  

<br><br>

### UIBarButtonItem의 속성

- title: UIBarButtonItem에 표시되는 문자열 제목.
- image: UIBarButtonItem에 표시되는 이미지. 일반적으로 25x25 또는 50x50 크기의 이미지를 사용.
- style: UIBarButtonItem의 스타일. 버튼 또는 바 버튼 스타일 중 하나일 수 있습니다. 바 버튼 스타일은 텍스트 레이블과 함께 표시되며, 일반적으로 네비게이션 바에서 사용.
- target: UIBarButtonItem의 이벤트를 처리하는 객체. 일반적으로 뷰 컨트롤러 또는 그에 대한 델리게이트가 된다.
- action: UIBarButtonItem을 탭할 때 실행되는 메서드 또는 셀렉터.
- enabled: UIBarButtonItem이 사용 가능한지 여부를 나타내는 부울 값. false로 설정하면 UIBarButtonItem이 회색조로 변경.
- tintColor: UIBarButtonItem의 색상. 기본 색상은 시스템 색상이며, 다른 색상으로 변경할 수 있다.

<br><br>


### 이니셜라이저
두가지 방법으로 생성이 가능하다.  
```swift
// MARK: 1. iOS13부터 추가된 UIAction
lazy var plusButton: UIBarButtonItem = {
    let action = UIAction { [weak self] _ in
        // 버튼이 탭될 때 실행할 코드
        self?.plusAction()
    }
    return UIBarButtonItem(systemItem: .add, primaryAction: action)
}()

// UIAction에 사용할 메서드
func plusAction() { }

// MARK: 2. selector를 이용한 전통적인 action
lazy var editButton: UIBarButtonItem = {
    let button = UIBarButtonItem(title: "Edit",
                                 style: .plain,
                                 target: self,
                                 action: #selector(editAction))
    return button
}()

// selector에 사용할 메서드
@objc func editAction() { }

```


### 툴바 사용하기
- 네비게이션바를 임베드 먼저 해야 동작한다.

```swift
class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        
      navigationController?.isToolbarHidden = false
      toolbarItems = makeToolbarItems()
  }

  private func makeToolbarItems() -> [UIBarButtonItem] {
      
    let space = UIBarButtonItem(barButtonSystemItem: .flexibleSpace, target: self, action: nil)
    let edgeSpace = UIBarButtonItem(barButtonSystemItem: .fixedSpace, target: self, action: nil)
      
    let buttonItem1 = UIBarButtonItem(barButtonSystemItem: .action, target: nil, action: nil)
    let buttonItem2 = UIBarButtonItem(barButtonSystemItem: .bookmarks, target: nil, action: nil)
    let buttonItem3 = UIBarButtonItem(barButtonSystemItem: .camera, target: nil, action: nil)
    let buttonItem4 = UIBarButtonItem(barButtonSystemItem: .search, target: nil, action: nil)
    let buttonItem5 = UIBarButtonItem(barButtonSystemItem: .refresh, target: nil, action: nil)
      
      return [edgeSpace, buttonItem1, space, buttonItem2, space, buttonItem3, space, buttonItem4, space, buttonItem5, edgeSpace]
  }
}


```

<br><br>

### 결과화면
<img width="300" alt="스크린샷 2023-04-19 오후 9 38 28" src="https://user-images.githubusercontent.com/76529148/233077500-de820d0f-3581-4547-87fb-63c54a01f4d5.png">


<br><br>

### 네비게이션바 사용하기

```swift
class ViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
      view.backgroundColor = .systemYellow
        // 내비게이션 바에 버튼 추가
        let addButton = UIBarButtonItem(barButtonSystemItem: .add,
                                        target: self,
                                        action: #selector(addButtonTapped))
        
//        navigationItem.rightBarButtonItem = addButton
        navigationItem.leftBarButtonItem = addButton
    }
    
    @objc func addButtonTapped() {
        print("Button tapped!")
    }
}
```

<br><br>

<img width="300" alt="스크린샷 2023-04-19 오후 9 43 15" src="https://user-images.githubusercontent.com/76529148/233078188-07a5691f-7e65-4bd6-b286-1cffa986f9e2.png">

<br><br>

### 네비게이션바에 여러개를 추가하기
한쪽에 여러개의 버튼을 추가할때는 leftBarButtonItem, rightBarButtonItem 를 사용하는 대신   
leftBarButtonItems, rightBarButtonItems로 세팅한다.  
        
```swift

class ViewController: UIViewController {
    
    let editButton: UIBarButtonItem
    let plusButton: UIBarButtonItem

    override func viewDidLoad() {
        super.viewDidLoad()
        
        navigationItem.rightBarButtonItems = [editButton, plusButton]

    }
}
```



## UITabBarItem
NSObject_UIBarItem 클래스는 애플리케이션에서 매우 자주 사용되는 클래스이며, UI를 구성하는데 매우 중요한 역할을 합니다.

탭 바 인터페이스는 일반적으로 화면 아래에 위치하며, 여러 화면(뷰 컨트롤러) 간에 전환할 수 있는 간단한 방법을 제공한다.

### UITabBarItem의 속성

- title: 탭 바 항목에 표시되는 문자열 제목.
- image: 탭 바 항목에 표시되는 이미지. 일반적으로 25x25 또는 50x50 크기의 이미지를 사용한다.
- selectedImage: 탭 바 항목이 선택되었을 때 표시되는 이미지. 이 속성을 사용하지 않으면 이미지가 회색조로 변경된다.
- badgeValue: 탭 바 항목 오른쪽 상단 모서리에 표시되는 배지 값. 일반적으로 읽지 않은 알림 수 또는 작업 수를 나타내는 데 사용된다.



### 탭바 사용하기

- 탭바를 임베드 먼저 해야 동작한다.
```swift
class ViewController: UIViewController {
  
  override func viewDidLoad() {
    super.viewDidLoad()
    
    // Create two view controllers
    let firstVC = UIViewController()
    firstVC.view.backgroundColor = .systemYellow
    let secondVC = UIViewController()
    secondVC.view.backgroundColor = .systemTeal
    
    // Create two UITabBarItem instances
    let firstTabBarItem = UITabBarItem(title: "First", image: UIImage(named: "first"), selectedImage: UIImage(named: "first_selected"))
    let secondTabBarItem = UITabBarItem(title: "Second", image: UIImage(named: "second"), selectedImage: UIImage(named: "second_selected"))
    
    // Set the tab bar item for each view controller
    firstVC.tabBarItem = firstTabBarItem
    secondVC.tabBarItem = secondTabBarItem
    
    // Create a UITabBarController and set the view controllers
    let tabBarController = UITabBarController()
    tabBarController.viewControllers = [firstVC, secondVC]
    
    // Set the UITabBarController as the root view controller
    self.view.addSubview(tabBarController.view)
    self.addChild(tabBarController)
    tabBarController.didMove(toParent: self)
  }
}
```

### 결과화면

https://user-images.githubusercontent.com/76529148/233790777-2d4235ff-8764-4031-9408-fad7e1bf77a4.mov

## History
- 230420 : UIBarButtonItem 추가
- 230422 : UITabBarItem 추가
