# NSObject_UIResponder_UIViewController_UITableViewController : 테이블뷰 전용 ViewController


iOS에서 리스트를 구현하는 방법은 SwiftUI에서는 List()를 이용하고, UIKit에서는 UITableView를 사용하거나 UITableViewController를 사용한다.

여기선 특별히 UITableViewController를 알아보자.    
- [코드보기로 이동](#전체코드)

## 소개
UITableView는 위에서 말한것처럼 규칙적으로 반복되는 형태의 리스트를 보여주기위한 UIView 
객체이다. 이 UITableView를 보통 어떤 View위에 생성하여 사용하게 되는데,

특별히 UITableView를 쉽게 구현하고 관리하기 쉽게 만든 클래스가 UITableViewController객체이다. 

기본적으로 UITableViewController는 UIViewController를 상속하고 있기때문에, UIViewController로서의 역할을 수행한다. 그리고 UITableView를 자체적으로 갖고있기때문에 따로 UITableView를 사용하는데 있어서 필요한 여러가지 세팅들을 세팅할 수 있다. 

- UITableView 만드는 방법
    - [TIL : UITableView 사용법
](https://github.com/isGeekCode/TIL/blob/main/Mobile-IOS/NSObject_UIResponder_UIView_UIScrollView_UITableView_a_howToMake.md)  
  
## 생성과정
- 사용할 셀 등록하기
- 섹션 안의 Row 갯수 구현
- 셀의 표시 방식 구현
- 선택: 셀클릭시 동작 구현
  
### 사용할 셀 등록하기
```swift
tableView.register(UITableViewCell.self, forCellReuseIdentifier: "Cell")
```
  
### 섹션 안의 Row 갯수 구현
```swift
override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
    return 10
}
```
  
### 셀의 표시 방식 구현
```swift
override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath)
    cell.textLabel?.text = "Row \(indexPath.row + 1)"
    return cell
}
```
### 선택: 셀클릭시 동작 구현
```swift
override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
    print("didSelectRowAt: \(indexPath.row)")
}
```
  
## 전체코드
```swift
class MyTableViewController: UITableViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        tableView.register(UITableViewCell.self, forCellReuseIdentifier: "Cell")
    }

    // 필수 : 셀을 얼마나 보여줄 것인지 정의
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return 10
    }

    // 필수 : 셀을 어떻게 보여줄 것인지 정의
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath)
        cell.textLabel?.text = "Row \(indexPath.row + 1)"
        return cell
    }

    // 선택 : 셀 클릭시 동작을 정의
    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        print("didSelectRowAt: \(indexPath.row)")
    }
}
```

## UIViewController에서 UITableViewController를 추가하는 방법
특별히 UIViewController에서 UITableViewController를 관리하기 위해 `addChild`로 추가하고 `tableViewController.didMove(toParent: self)`로 추가해서 사용할 수 있다.

- 키워드
    - addChild()
    - didMove(toParent:)

### addChild()
아래 예시 처럼 부모 클래스 내부에서 addChild(자녀클래스)의 형태로 선언한다.
```swift
class ViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()

        addChild(tableViewController)
}
```
### didMove(toParent:)
아래 전체코드 예시처럼 부모 클래스 내부에서 원하는 객체를 만들어서 해당객체.didMove(toParent: self)의 형태로 선언한다.

### 전체코드
```swift
class ViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()

        addChild(tableViewController)
}
```

```swift
class MyTableViewController: UITableViewController {
    var selectedRowIndex: Int?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        tableView.delegate = self
    }
    
    // 선택
    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        print("didSelectRowAt: \(indexPath.row)")
    }
    
    // 필수 : 셀을 얼마나 보여줄 것인지 정의
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return 10
    }
    
    // 필수 : 셀을 어떻게 보여줄 것인지 정의
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath)
        cell.textLabel?.text = "Row \(indexPath.row + 1)"
        return cell
    }
}

class ViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        
        let tableViewController = MyTableViewController()
        tableViewController.tableView.register(UITableViewCell.self, forCellReuseIdentifier: "Cell")
        
        addChild(tableViewController)
        view.addSubview(tableViewController.tableView)
        tableViewController.tableView.translatesAutoresizingMaskIntoConstraints = false
        NSLayoutConstraint.activate([
            tableViewController.tableView.topAnchor.constraint(equalTo: view.topAnchor),
            tableViewController.tableView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            tableViewController.tableView.bottomAnchor.constraint(equalTo: view.bottomAnchor),
            tableViewController.tableView.trailingAnchor.constraint(equalTo: view.trailingAnchor)
        ])
        tableViewController.didMove(toParent: self)
    }
}

```
### 구동화면
  <img width="300" alt="IMG_0839" src="https://github.com/isGeekCode/TIL/assets/76529148/c550dd46-1970-4298-b5f5-883e2261ec92">  


### History
- 230601 : 생성