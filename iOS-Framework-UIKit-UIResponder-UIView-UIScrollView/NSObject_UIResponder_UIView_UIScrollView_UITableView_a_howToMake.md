# NSObject_UIResponder_UIView_UIScrollView_UITableView : 사용법

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
  ```swift
  addSubView(tableView)
  ```

### frame 혹은 제약조건 세팅
  ```swift
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
  ```swift
  class TableViewController: UIViewController, UITableViewDelegate, UITableViewDataSource { }
  ```

### TableView Protocol Delegate 선언
  ```swfit
    tableView.delegate = self
    tableView.dataSource = self
  ```

### TableView Delegate 함수 세팅
- 첫 UITableViewCell은 여기서 구현을 한 상황이다.
  ```swift
    /// 테이블뷰 섹션 내부의 Row의 갯수를 선언하는 부분
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
      return 10
    }
    
    /// cell이 어떻게 보여질지 세팅하는 부분
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
      // UITableViewCell 구현
      let cell = tableView.dequeueReusableCell(withIdentifier: "cell", for: indexPath)
    
      cell.textLabel?.text = "Hello world"
      return cell
    }

  ```


### 현재까지의 작업화면
- 시뮬레이터 다크모드전환 단축키: `Shift + Command + A`
<img width="356" alt="스크린샷 2023-01-28 오후 3 13 58" src="https://user-images.githubusercontent.com/76529148/215250704-86891e64-c094-4898-80ea-d76f41e6d14a.png">


### 현재까지의 전체코드

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
    tableView.frame = view.bounds

    tableView.delegate = self
    tableView.dataSource = self
  }
}

extension TableViewController: UITableViewDelegate, UITableViewDataSource {

  /// 테이블뷰 섹션 내부의 Row의 갯수를 선언하는 부분
  func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
    return 10
  }
  
  /// 테이블뷰의 cell이 어떻게 보여질지 선언하는 부분
  func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    // UITableViewCell 구현
    let cell = tableView.dequeueReusableCell(withIdentifier: "cell", for: indexPath)
  
    cell.textLabel?.text = "Hello world"
    return cell
  }
}

```

## Step2. 테이블뷰 내용을 보여주기위한 구조체 구현

### 구조체 구현
- `icon`처럼 항상 존재하지는 않을 정보라면 `?`을 통해 옵셔널 세팅해줄 것
  ```swift
  struct SettingsOptions {
    let title: String
    let icon: UIImage?
    let iconBackgroundColor: UIColor
    let handler: (() -> Void)
  }

  class TableViewController: UIViewController, UITableViewDelegate, UITableViewDataSource { }
  ```

### 구조체 init
- 변수선언
  ```swift
  var models = [SettingsOptions]()
  ```
- 변수값 세팅: 임의로 101개 세팅
  ```swift
  override func viewDidLoad() {
    super.viewDidLoad()
    configure()
  }

  func configure() {
    self.models = Array(0...100).compactMap({
      SettingsOptions(title: "Item \($0)", icon: UIImage(systemName: "house"), iconBackgroundColor: .systemPink) {
      }
    })
  } 
  ```
### TabelView에 반영하기
- numberOfRowsInSection에 모델변수의 갯수 선언
- cellForRowAt에 모델변수의 텍스트값 세팅
```swift

  func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
    return models.count
  }
  

  func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    let model = models[indexPath.row]
    let cell = tableView.dequeueReusableCell(withIdentifier: "cell", for: indexPath)
  
    cell.textLabel?.text = model.title
    return cell
  }
```


### 현재까지의 작업화면
<img width="358" alt="스크린샷 2023-01-28 오후 3 55 43" src="https://user-images.githubusercontent.com/76529148/215251949-32f24bc6-b9f7-4ec7-97eb-37c888c4cf87.png">

### 현재까지의 전체코드
```swift
import UIKit

struct SettingsOptions {
  let title: String
  let icon: UIImage?
  let iconBackgroundColor: UIColor
  let handler: (() -> Void)
}

class TableViewController: UIViewController {

  private let tableView: UITableView = {
    let table = UITableView(frame: .zero, style: .grouped)
    table.register(UITableViewCell.self, forCellReuseIdentifier: "cell")
    return table
  }()
  
  var models = [SettingsOptions]()
  
  override func viewDidLoad() {
    super.viewDidLoad()

    configure()
    title = "Settings"
    view.addSubview(tableView)
    tableView.frame = view.bounds

    tableView.delegate = self
    tableView.dataSource = self
  }

  func configure() {
    self.models = Array(0...100).compactMap({
      SettingsOptions(title: "Item \($0)", icon: UIImage(systemName: "house"), iconBackgroundColor: .systemPink) {

      }
    })
  }
}

extension TableViewController: UITableViewDelegate, UITableViewDataSource {

  func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
    return models.count
  }
  

  func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    let model = models[indexPath.row]
    let cell = tableView.dequeueReusableCell(withIdentifier: "cell", for: indexPath)
  
    cell.textLabel?.text = model.title
    return cell
  }
}

```

## Step3. UITableViewCell생성하기
- identifier 세팅하기
  ```swift
  static let identifier = "SettingTableViewCell"

  ```
- swift파일 세팅
  ```swift
  import UIKit

  class SettingTableViewCell: UITableViewCell {

    static let identifier = "SettingTableViewCell"
    
    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
      super.init(style: style, reuseIdentifier: reuseIdentifier)
    }
    
    required init?(coder: NSCoder) {
      fatalError()
    }
    
    override func layoutSubviews() {
      super.layoutSubviews()
    }
    
    override func prepareForReuse() {
      super.prepareForReuse()
    }
  }

  ```

- ViewController에서 해당 TableViewCell 등록하기
  ```swift
  // Property
  private let tableView: UITableView = {
    let table = UITableView(frame: .zero, style: .grouped)
    table.register(SettingTableViewCell.self, forCellReuseIdentifier: SettingTableViewCell.identifier)
    return table
  }()
  
  // TableViewDelegate - Cell for Row At 에도 셀정보 등록
  func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    let model = models[indexPath.row]
    guard let cell = tableView.dequeueReusableCell(
      withIdentifier: SettingTableViewCell.identifier,
      for: indexPath
    ) as? SettingTableViewCell else {
      return UITableViewCell()
    }
  
    cell.configure(with: model)
    return cell
  }
  ```

## 빠른 생성

```swift
import UIKit

class ViewController: UIViewController {
    
    lazy var listData = Array(0...10).map { "Item\($0)" }
    
    lazy var tableView: UITableView = {
       let tableView = UITableView()
        tableView.translatesAutoresizingMaskIntoConstraints = false
        tableView.delegate = self
        tableView.dataSource = self
        tableView.register(UITableViewCell.self, forCellReuseIdentifier: #function)
        return tableView
    }()

    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        view.addSubview(tableView)
        
        NSLayoutConstraint.activate([
            tableView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
            tableView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor),
            tableView.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor),
            tableView.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor),
        ])
    }
}


extension ViewController: UITableViewDelegate, UITableViewDataSource {
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return listData.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = UITableViewCell(style: .default, reuseIdentifier: #function)
        cell.textLabel?.text = listData[indexPath.row]
        return cell
    }
}


```
