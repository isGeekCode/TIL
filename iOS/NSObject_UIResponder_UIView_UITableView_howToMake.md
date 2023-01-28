# NSObject_UIResponder_UIView_UITableView_만들기

## Step1. TableView 선언

### Property 
- `.grouped` 이 필요한 경우에 아래와 같이 하지만 필요 없을 경우에는 `UITableView()`로 생성
- cell도 등록해준다. 
  ```swift
    private let tableView: UITableView = {
      let table = UITableView(frame: .zero, style: .grouped)
      table.register(UITableViewCell.self, forCellReuseIdentifier: "cell")
      return table
    }()

  ```

### View에 추가
  ```
  addSubView(tableView)
  ```

### frame 혹은 제약조건 세팅
  ```
  // frame으로 설정할 경우
  tableView.frame = view.bounds

  // Constraint로 설정할 경우
  tableView.translatesAutoresizingMaskIntoConstraints = false  
  NSLayoutConstraint.activate([
      table.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
      table.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor),
      table.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor),
      table.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor),
  ])
  ```
  
### TableView Protocol 선언 
  ```
  class TableViewController: UIViewController, UITableViewDelegate, UITableViewDataSource { }
  ```

### TableView Protocol Delegate 선언
  ```swfit
      tableView.delegate = self
      tableView.dataSource = self
  ```

### TableView Delegate 함수 세팅

  ```
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
      return 10
    }
    

    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
      let cell = tableView.dequeueReusableCell(withIdentifier: "cell", for: indexPath)
    
      cell.textLabel?.text = "Hello world"
      return cell
    }

  ```


### 작업화면
- 시뮬레이터 다크모드전환 단축키: `Shift + Command + A`
<img width="356" alt="스크린샷 2023-01-28 오후 3 13 58" src="https://user-images.githubusercontent.com/76529148/215250704-86891e64-c094-4898-80ea-d76f41e6d14a.png">


### 현재까지 전체 코드

```swift
import UIKit

class TableViewController: UIViewController {

  private let tableView: UITableView = {
    let table = UITableView(frame: .zero, style: .grouped)
    table.register(UITableViewCell.self, forCellReuseIdentifier: "cell")
    
    return table
  }()
  
    override func viewDidLoad() {
        super.viewDidLoad()
      title = "Settings"
      view.addSubview(tableView)
      tableView.delegate = self
      tableView.dataSource = self
      tableView.frame = view.bounds
    }

extension TableViewController: UITableViewDelegate, UITableViewDataSource {

  func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
    return 10
  }
  

  func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {

    let cell = tableView.dequeueReusableCell(withIdentifier: "cell", for: indexPath)
  
    cell.textLabel?.text = "Hello world"
    return cell
  }
}

```


