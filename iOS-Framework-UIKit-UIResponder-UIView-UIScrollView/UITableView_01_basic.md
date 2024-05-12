# UITableView - 기본 UITableView 생성

- 참고자료 : [Apple Document](https://developer.apple.com/documentation/uikit/uitableview)

테이블뷰는 데이터를 앱에 표시할 수 있는 가장 기본적인 방법으로서, iOS개발에 중요한 요소중 하나이다.  

## 이해하면 좋은 것
- 기본 생성방법
- delegation 이란

<br><br>


##  두 개의  Delegation
UITableView에는 DataSource, Delegate 라는 대리자가 옵셔널로 생성되어 있다.   
각각의 용도는 아래와 같다.  

- DataSource : 테이븗뷰의 구성을 어떻게 할지 위임
- Delegate : 테이블뷰의 동작을 결정하는 걸 위임




## Step1. TableView 선언하기

### Property 
- 아이폰 설정앱처럼 그룹화된 셀을 보여주고 싶다면 style에서 .grouped / insetGrouped 를 선택한다.
    - 이 내용은 Section 구현에서 추가언급예정
- 셀을 스크롤하며 재활용해야한다면 cell도 등록해준다. 
```swift
let tableView: UITableView = UITableView()
// let table = UITableView(frame: .zero, style: .plain)
// let table = UITableView(frame: .zero, style: .grouped)
// let table = UITableView(frame: .zero, style: .insetGrouped)
```

<br><br>

### View에 추가
```swift
addSubView(tableView)
```

<br><br>

### frame 혹은 제약조건 세팅
```swift
// frame으로 설정할 경우
tableView.frame = view.bounds
```
<br><br>

```swift
// Constraint로 설정할 경우
tableView.translatesAutoresizingMaskIntoConstraints = false  
NSLayoutConstraint.activate([
  table.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
  table.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor),
  table.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor),
  table.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor),
])
```
  
<br><br>
  
### TableView Protocol 채택 
프로토콜을 채택하면 해당 프로토콜에서 미리 설정한 것들을 필수로 구현해야만 한다.
  
```swift
class ViewController: UIViewController, UITableViewDelegate, UITableViewDataSource { }

```

혹은 아래와 같이 나눠서 구현하기도 한다.   

```swift
class ViewController: UIViewController { }

extension ViewController: UITableViewDelegate, UITableViewDataSource { }

```


<br><br>

### TableView Delegate 선언
delegation이란 원래 해당 역할을 수행할 주체를 위임한다는 것이다.  
그래서 ViewController 내부에서 tableView의 delegate를 self로 선언한다는 것은  
해당 tableView의 여러 메서드들을 ViewController에 구현해서 처리하겠다는 말이다.  

tableView의 위임자는 delegate와 dataSource가 있다.  
```swift
tableView.delegate = self
tableView.dataSource = self
```

<br><br>

만약 delegate 선언을 상단 프로퍼티의 클로저에 구현하고 싶다면 이렇게 선언한다.    

```swift
lazy var tableView: UITableView = {
    let tableView = UITableView()
    tableView.delegate = self
    tableView.dataSource = self
    return tableView
}()
```

<br><br>

### TableView Delegate 메서드 세팅
- 여기선 10개의 셀에 "Hello world"를 보여주는 것으로 하드코딩
```swift
/// 테이블뷰 섹션 내부의 Row의 갯수를 선언하는 부분
func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
  return 10
}

/// cell이 어떻게 보여질지 세팅하는 부분
func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {

  // UITableViewCell 구현
  let cell = UITableViewCell()
  cell.textLabel?.text = "Row \(indexPath.row)"
  return cell
}

```

<br><br>

### 현재까지의 작업화면
- 시뮬레이터 다크모드전환 단축키: `Shift + Command + A`
<img width="356" alt="스크린샷 2023-01-28 오후 3 13 58" src="https://github.com/isGeekCode/TIL/assets/76529148/49a56b76-94d6-419a-b2d4-4fc81cbd7c31">


<br><br>

### 현재까지의 전체코드

```swift
import UIKit

class ViewController: UIViewController {

  let tableView: UITableView = UITableView()
  
  override func viewDidLoad() {
    super.viewDidLoad()
    view.addSubview(tableView)
    tableView.frame = view.bounds

    tableView.delegate = self
    tableView.dataSource = self
  }
}

extension ViewController: UITableViewDelegate, UITableViewDataSource {

  /// 테이블뷰 섹션 내부의 Row의 갯수를 선언하는 부분
  func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
    return 10
  }
  
  /// 테이블뷰의 cell이 어떻게 보여질지 선언하는 부분
  func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    // UITableViewCell 구현
    let cell = UITableViewCell()
    cell.textLabel?.text = "Row \(indexPath.row)"
    return cell
  }
}

```

<br><br>

## TableViewCell을 재사용하기
테이블뷰에서 가장 중요한 요소 중 하나이다.  
테이블뷰는 스크롤할 정도로 여러개의 셀을 가지고 있을 때,  
추가적으로 화면에 표시할 셀을 생성하게 되어있다.  

그런데 매번 새로 생성하게 되면 자원을 낭비하게 된다.  

그렇기 때문에 사용하는 개념이 재사용이다.  

tableView에 셀을 관리할 Queue를 두고, 
미리 그 Queue에 넣을 셀을 등록한다. 
또 Queue에서 뺄 셀도 등록을 하게 된다.  

<br><br>

### 셀 등록하기
- UINib : 내가 사용할 테이블뷰셀 클래스
    - 만약 커스텀 클래스를 사용한다면 해당 클래스를 넣어준다.  
- forCellReuseIdentifier : 구분에 필요한 ID
```swift
// 재사용할 셀을 등록하는 메서드
func register(UINib?, forCellReuseIdentifier: String)

// 사용예
tableView.register(UITableViewCell.self, forCellReuseIdentifier: "cell")
```

<br><br>

### dequeue하여 재사용할 셀 선언하기
UITableView는 reusableCell 큐에서 지정된 식별자(identifier)를 가진 셀을 "빼내어(dequeue)" 재사용하는 방식으로 작동한다. 
이때 사용하는 메서드는 두가지가 있는데, 아래 메서드가 indexPath를 넣어서 명시적으로 설정하는 메서드기 때문에 이걸 이용하는 것을 선호한다.  

- withIdentifier : 구분에 필요한 ID
- for : indexPath 
```swift
func dequeueReusableCell(withIdentifier: String, for: IndexPath) -> UITableViewCell

// tableView의 DataSource 메서드
func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {

  let cell = tableView.dequeueReusableCell(withIdentifier: "cell", for: indexPath)
  cell.textLabel?.text = "Row \(indexPath.row)"
  
  return cell
}
```

<br><br>

### 현재까지의 작업화면
<img width="356" alt="스크린샷 2023-01-28 오후 3 13 58" src="https://github.com/isGeekCode/TIL/assets/76529148/30a77816-185b-4fa3-bb5b-5659dd4d5c4e">

<br><br>

### 전체코드
```swift
import UIKit

class ViewController: UIViewController {
    
    let tableView: UITableView = UITableView()
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        view.addSubview(tableView)
        tableView.frame = view.bounds
        
        tableView.delegate = self
        tableView.dataSource = self
        
        tableView.register(UITableViewCell.self, forCellReuseIdentifier: "cell")
    }
}

extension ViewController: UITableViewDelegate, UITableViewDataSource {
    
    /// 테이블뷰 섹션 내부의 Row의 갯수를 선언하는 부분
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return 50
    }
    
    /// 테이블뷰의 cell이 어떻게 보여질지 선언하는 부분
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        // UITableViewCell 구현
        let cell = tableView.dequeueReusableCell(withIdentifier: "cell", for: indexPath)
        cell.textLabel?.text = "Row \(indexPath.row)"
        
        return cell
    }
}

```
