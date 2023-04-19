# NSObject_UIBarItem

NSObject 의 UIBarItem은 iOS 애플리케이션에서 사용되는 클래스 중 하나로,

네비게이션 바, 툴바, 탭 바 등에 표시되는 아이템을 나타내는 추상 클래스이다.

UIBarItem 클래스는 구체적으로 구현된 것이 아니기 때문에, 이를 상속받는 구체적인 서브클래스를 사용해야 한다. 구체적인 서브클래스로는 UIBarButtonItem, UITabBarItem 등이 있으며, 이들은 각각 네비게이션 바/툴바 아이템, 탭 바 아이템을 나타낸다.

## UIBarButtonItem
UIBarItem 클래스는 텍스트, 이미지, 뷰 등의 속성을 가지며, 이를 설정하여 아이템의 모양을 변경할 수 있다. 또한 isEnabled 속성을 통해 아이템을 활성화/비활성화할 수 있다.

### 툴바 사용하기
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

### 결과화면
<img width="253" alt="스크린샷 2023-04-19 오후 9 38 28" src="https://user-images.githubusercontent.com/76529148/233077500-de820d0f-3581-4547-87fb-63c54a01f4d5.png">

### 네비게이션바 사용하기

```swift
class ViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
      view.backgroundColor = .systemYellow
        // 내비게이션 바에 버튼 추가
        let addButton = UIBarButtonItem(barButtonSystemItem: .add, target: self, action: #selector(addButtonTapped))
//        navigationItem.rightBarButtonItem = addButton
        navigationItem.leftBarButtonItem = addButton
    }
    
    @objc func addButtonTapped() {
        print("Button tapped!")
    }
}
```
<img width="254" alt="스크린샷 2023-04-19 오후 9 43 15" src="https://user-images.githubusercontent.com/76529148/233078188-07a5691f-7e65-4bd6-b286-1cffa986f9e2.png">

## UITabBarItem
NSObject_UIBarItem 클래스는 애플리케이션에서 매우 자주 사용되는 클래스이며, UI를 구성하는데 매우 중요한 역할을 합니다.



