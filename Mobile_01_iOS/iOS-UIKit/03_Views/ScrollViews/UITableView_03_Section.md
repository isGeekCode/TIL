# UITableView - Section 구현하기

이번엔 여러 섹션을 가진 테이블뷰를 구현해보고, 각 섹션에 다른 종류의 셀도 사용해보자.  


## 섹션 나누기


### 섹션을 구별할 구조체 생성
섹션을 구분할 구조체를 구현한다.  

```swift
import UIKit

struct SectionModel {
    let title: String
    let itemList: [String]
}
```

<br><br>

### 구현할 내용 추가
```swift
var sectionList: [SectionModel] = [
    SectionModel(title: "Section 1",
                 itemList: ["Item 1","Item 2","Item 3"]),
    
    SectionModel(title: "Section 2",
                 itemList: ["Item 4","Item 5"]),
    
    SectionModel(title: "Section 3",
                 itemList: ["Item 6","Item 7","Item 8"]),
    ]

```

<br><br>

### 델리게이트 메서드 구현
이제 데이터가 단순 Array가 아니기때문에, section과 row를 혼동하면 안된다.  

IndexPath프로퍼티는 Section과 Row를 가지고 있다.  



```swift
extension ViewController: UITableViewDelegate, UITableViewDataSource {
    
    // Section의 수
    func numberOfSections(in tableView: UITableView) -> Int {
        return sectionList.count
    }
    
    // Section당 Row의 수
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return sectionList[section].itemList.count
    }
    
    // 각 셀에만 해당하는 데이터 모델을 추출해 바인딩처리
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        
        let cell = UITableViewCell()
        let item = sectionList[indexPath.section].itemList[indexPath.row]

        cell.textLabel?.text = item
        return cell
    }
    
    func tableView(_ tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
        return sectionList[section].title
    }
}

```


<br><br>


### 작업화면
<img width="356" alt="스크린샷 2023-01-28 오후 3 13 58" src="https://github.com/isGeekCode/TIL/assets/76529148/d1255f3a-cc61-4b4e-b209-a8811f2e8417">

<br><br>

### 전체코드

```swift
import UIKit

struct SectionModel {
    let title: String
    let itemList: [String]
}


class ViewController: UIViewController {
    
    var sectionList: [SectionModel] = [
        SectionModel(title: "Section 1",
                     itemList: ["Item 1","Item 2","Item 3"]),
        
        SectionModel(title: "Section 2",
                     itemList: ["Item 4","Item 5"]),
        
        SectionModel(title: "Section 3",
                     itemList: ["Item 6","Item 7","Item 8"]),
        ]
    
    var tableView = UITableView(frame: .zero, style: .insetGrouped)
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setUI()
        setDetail()
    }

    
    func setDetail() {
        tableView.dataSource = self
        tableView.delegate = self
    }
    
    func setUI() {
        view.addSubview(tableView)
        tableView.frame = view.bounds

    }
}

extension ViewController: UITableViewDelegate, UITableViewDataSource {
    
    func numberOfSections(in tableView: UITableView) -> Int {
        return sectionList.count
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return sectionList[section].itemList.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        
        let cell = UITableViewCell()
        let item = sectionList[indexPath.section].itemList[indexPath.row]

        cell.textLabel?.text = item
        return cell
    }
    
    func tableView(_ tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
        return sectionList[section].title
    }
}
```

<br><br>

## 섹션별로 다르게 구현하기
이번엔 여러 셀을 등록하고, 내가 원하는 섹션에 배치를 해보자. 


### 원하는 정보 배치
원하는 순서에 맞게 배치해보자.  

```swift
var sectionList: [SectionModel] = [
    SectionModel(title: "개발자 정보",
                 itemList: ["John Doe"]),
    
    SectionModel(title: "앱 정보",
                 itemList: ["생활 편의", "다운로드 수", "v1.3.2"]),
]

```

<br><br>

### 섹션에 사용할 셀 등록

```swift
// BusinessCardTableViewCell 등록
tableView.register(BusinessCardTableViewCell.self, forCellReuseIdentifier: "BusinessCardTableViewCell")
// 기본 UITableViewCell 등록
tableView.register(UITableViewCell.self, forCellReuseIdentifier: "cell")
```

<br><br>


### 섹션에 따른 표시방식 변경
```swift
func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    // 첫 번째 섹션에 BusinessCardTableViewCell 사용
    if indexPath.section == 0 {
        guard let cell = tableView.dequeueReusableCell(withIdentifier: "BusinessCardTableViewCell", for: indexPath) as? BusinessCardTableViewCell else {
            fatalError("Unable to dequeue BusinessCardTableViewCell")
        }
        let item = sectionList[indexPath.section].itemList[indexPath.row]
        // 예시 데이터 - 실제 앱에서는 모델에 맞는 데이터를 사용해야 함
        cell.configure(name: item, title: "Software Engineer", contact: "john.doe@example.com")
        return cell
    } else {
        // 나머지 섹션에는 기본 UITableViewCell 사용
        let cell = tableView.dequeueReusableCell(withIdentifier: "cell", for: indexPath)
        let item = sectionList[indexPath.section].itemList[indexPath.row]
        cell.textLabel?.text = item
        return cell
    }
}

```

<br><br>

### 섹션에 따른 셀 높이 변경
이제 특별히 높이를 제어하게 됐다. 이경우에는 아래 메서드를 이용한다.  

```swift
func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
    
    if indexPath.section == 0 {
        return 150
    } else {
        return 50
    }
}
```

<br><br>

### 작업화면
<img width="356" alt="스크린샷 2023-01-28 오후 3 13 58" src="https://github.com/isGeekCode/TIL/assets/76529148/cc5a7575-f171-4d46-9425-eb544ba2fb8f">

<br><br>

### 전체코드

```swift
import UIKit

struct SectionModel {
    let title: String
    let itemList: [String]
}


class ViewController: UIViewController {
    
    var sectionList: [SectionModel] = [
        SectionModel(title: "개발자 정보",
                     itemList: ["John Doe"]),
        
        SectionModel(title: "앱 정보",
                     itemList: ["생활 편의", "다운로드 수", "v1.3.2"]),
    ]
    
    var tableView = UITableView(frame: .zero, style: .insetGrouped)
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setUI()
        setDetail()
    }
    
    
    func setDetail() {
        tableView.dataSource = self
        tableView.delegate = self
        
        // BusinessCardTableViewCell 등록
        tableView.register(BusinessCardTableViewCell.self, forCellReuseIdentifier: "BusinessCardTableViewCell")
        // 기본 UITableViewCell 등록
        tableView.register(UITableViewCell.self, forCellReuseIdentifier: "cell")
        
    }
    
    func setUI() {
        view.addSubview(tableView)
        tableView.frame = view.bounds
    }
}

extension ViewController: UITableViewDelegate, UITableViewDataSource {
    
    func numberOfSections(in tableView: UITableView) -> Int {
        return sectionList.count
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return sectionList[section].itemList.count
    }    
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        // 첫 번째 섹션에 BusinessCardTableViewCell 사용
        if indexPath.section == 0 {
            guard let cell = tableView.dequeueReusableCell(withIdentifier: "BusinessCardTableViewCell", for: indexPath) as? BusinessCardTableViewCell else {
                fatalError("Unable to dequeue BusinessCardTableViewCell")
            }
            let item = sectionList[indexPath.section].itemList[indexPath.row]
            // 예시 데이터 - 실제 앱에서는 모델에 맞는 데이터를 사용해야 함
            cell.configure(name: item, title: "Software Engineer", contact: "john.doe@example.com")
            return cell
        } else {
            // 나머지 섹션에는 기본 UITableViewCell 사용
            let cell = tableView.dequeueReusableCell(withIdentifier: "cell", for: indexPath)
            let item = sectionList[indexPath.section].itemList[indexPath.row]
            cell.textLabel?.text = item
            return cell
        }
    }
    
    func tableView(_ tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
        return sectionList[section].title
    }
    
    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
        
        if indexPath.section == 0 {
            return 150
        } else {
            return 50
        }
    }
}


class BusinessCardTableViewCell: UITableViewCell {
    
    let nameLabel: UILabel = {
        let label = UILabel()
        label.translatesAutoresizingMaskIntoConstraints = false
        label.font = UIFont.boldSystemFont(ofSize: 20)
        label.textColor = .black
        return label
    }()
    
    let titleLabel: UILabel = {
        let label = UILabel()
        label.translatesAutoresizingMaskIntoConstraints = false
        label.font = UIFont.systemFont(ofSize: 16)
        label.textColor = .black
        return label
    }()
    
    let contactLabel: UILabel = {
        let label = UILabel()
        label.translatesAutoresizingMaskIntoConstraints = false
        label.font = UIFont.systemFont(ofSize: 14)
        label.textColor = .black
        return label
    }()
    
    let logoImageView: UIImageView = {
        let imageView = UIImageView()
        imageView.translatesAutoresizingMaskIntoConstraints = false
        imageView.image = UIImage(systemName: "person.fill")
        return imageView
    }()
    
    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        //        contentView.backgroundColor = .systemYellow.withAlphaComponent(0.3)
        contentView.addSubview(nameLabel)
        contentView.addSubview(titleLabel)
        contentView.addSubview(contactLabel)
        contentView.addSubview(logoImageView)
        applyConstraints()
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    private func applyConstraints() {
        NSLayoutConstraint.activate([
            nameLabel.topAnchor.constraint(equalTo: contentView.topAnchor, constant: 20),
            nameLabel.leadingAnchor.constraint(equalTo: contentView.leadingAnchor, constant: 20),
            
            titleLabel.topAnchor.constraint(equalTo: nameLabel.bottomAnchor, constant: 30),
            titleLabel.leadingAnchor.constraint(equalTo: nameLabel.leadingAnchor),
            
            contactLabel.topAnchor.constraint(equalTo: titleLabel.bottomAnchor, constant: 10),
            contactLabel.leadingAnchor.constraint(equalTo: nameLabel.leadingAnchor),
            
            logoImageView.topAnchor.constraint(equalTo: contentView.topAnchor, constant: 10),
            logoImageView.trailingAnchor.constraint(equalTo: contentView.trailingAnchor, constant: -20),
            logoImageView.widthAnchor.constraint(equalToConstant: 50),
            logoImageView.heightAnchor.constraint(equalToConstant: 50),
        ])
    }
    
    func configure(name: String, title: String, contact: String) {
        nameLabel.text = name
        titleLabel.text = title
        contactLabel.text = contact
    }
}


```


<br><br>


## enum을 이용한 셀 타입 설정
이전에는 필요한 정보를 아래처럼 순서에 맞게 표시했기 때문에 직관적이지 않았다. 
```swift
var sectionList: [SectionModel] = [
    SectionModel(title: "개발자 정보",
                 itemList: ["John Doe"]),
    
    SectionModel(title: "앱 정보",
                 itemList: ["생활 편의", "다운로드 수", "v1.3.2"]),
]

```

이제 좀더 명확하게 표시해보자.  


<br><br>


### 셀타입 enum 정의

```swift
enum CellType {
    case businessCard
    case plain
}

```


<br><br>


### 구조체 수정
이제 모델 자체에서도 타입 캐치가 가능하도록 구현한 타입을 넣어준다.  

```swift
struct SectionModel {
    let title: String
    let itemList: [String]
    let cellType: CellType // 각 섹션의 셀 타입을 나타내는 속성 추가
}

var sectionList: [SectionModel] = [
    SectionModel(title: "개발자 정보",
                 itemList: ["John Doe"],
                 cellType: .businessCard),
    
    SectionModel(title: "앱 정보",
                 itemList: ["생활 편의", "다운로드 수", "v1.3.2"],
                 cellType: .plain),
]
```

<br><br>


### `tableView(_:cellForRowAt:)` 메서드 수정

메서드를 수정하여 각 섹션의 cellType에 따라 적절한 셀을 반환한다.

```swift
func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    let sectionModel = sectionList[indexPath.section]
    
    switch sectionModel.cellType {
    case .businessCard:
        guard let cell = tableView.dequeueReusableCell(withIdentifier: "BusinessCardTableViewCell", for: indexPath) as? BusinessCardTableViewCell else {
            fatalError("Unable to dequeue BusinessCardTableViewCell")
        }
        let item = sectionModel.itemList[indexPath.row]
        // 데이터 바인딩
        cell.configure(name: item, title: "Software Engineer", contact: "john.doe@example.com")
        return cell
        
    case .plain:
        let cell = tableView.dequeueReusableCell(withIdentifier: "cell", for: indexPath)
        let item = sectionModel.itemList[indexPath.row]
        cell.textLabel?.text = item
        return cell
    }
}
```

<br><br>


### 높이 메서드 수정
메서드를 수정하여 각 섹션의 cellType에 따라 적절한 셀을 반환한다.

```swift
    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
        
        let sectionModel = sectionList[indexPath.section]
        
        switch sectionModel.cellType {
        case .businessCard:
            return 150
        case .plain:
            return 50
        }
    }
```


## 전체코드

```swift
import UIKit

enum CellType {
    case businessCard
    case plain
}


struct SectionModel {
    let title: String
    let itemList: [String]
    let cellType: CellType // 각 섹션의 셀 타입을 나타내는 속성 추가
}

class ViewController: UIViewController {
    
    var sectionList: [SectionModel] = [
        SectionModel(title: "개발자 정보",
                     itemList: ["John Doe"],
                     cellType: .businessCard),
        
        SectionModel(title: "앱 정보",
                     itemList: ["생활 편의", "다운로드 수", "v1.3.2"],
                     cellType: .plain),
    ]

    
    var tableView = UITableView(frame: .zero, style: .insetGrouped)
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setUI()
        setDetail()
    }
    
    
    func setDetail() {
        tableView.dataSource = self
        tableView.delegate = self
        
        // BusinessCardTableViewCell 등록
        tableView.register(BusinessCardTableViewCell.self, forCellReuseIdentifier: "BusinessCardTableViewCell")
        // 기본 UITableViewCell 등록
        tableView.register(UITableViewCell.self, forCellReuseIdentifier: "cell")
        
    }
    
    func setUI() {
        view.addSubview(tableView)
        tableView.frame = view.bounds
    }
}

extension ViewController: UITableViewDelegate, UITableViewDataSource {
    
    func numberOfSections(in tableView: UITableView) -> Int {
        return sectionList.count
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return sectionList[section].itemList.count
    }    
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let sectionModel = sectionList[indexPath.section]
        
        switch sectionModel.cellType {
        case .businessCard:
            guard let cell = tableView.dequeueReusableCell(withIdentifier: "BusinessCardTableViewCell", for: indexPath) as? BusinessCardTableViewCell else {
                fatalError("Unable to dequeue BusinessCardTableViewCell")
            }
            let item = sectionModel.itemList[indexPath.row]
            // 데이터 바인딩
            cell.configure(name: item, title: "Software Engineer", contact: "john.doe@example.com")
            return cell
            
        case .plain:
            let cell = tableView.dequeueReusableCell(withIdentifier: "cell", for: indexPath)
            let item = sectionModel.itemList[indexPath.row]
            cell.textLabel?.text = item
            return cell
        }
    }
    
    func tableView(_ tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
        return sectionList[section].title
    }
    
    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
        
        let sectionModel = sectionList[indexPath.section]
        
        switch sectionModel.cellType {
        case .businessCard:
            return 150
        case .plain:
            return 50
        }
    }
}


class BusinessCardTableViewCell: UITableViewCell {
    
    let nameLabel: UILabel = {
        let label = UILabel()
        label.translatesAutoresizingMaskIntoConstraints = false
        label.font = UIFont.boldSystemFont(ofSize: 20)
        label.textColor = .black
        return label
    }()
    
    let titleLabel: UILabel = {
        let label = UILabel()
        label.translatesAutoresizingMaskIntoConstraints = false
        label.font = UIFont.systemFont(ofSize: 16)
        label.textColor = .black
        return label
    }()
    
    let contactLabel: UILabel = {
        let label = UILabel()
        label.translatesAutoresizingMaskIntoConstraints = false
        label.font = UIFont.systemFont(ofSize: 14)
        label.textColor = .black
        return label
    }()
    
    let logoImageView: UIImageView = {
        let imageView = UIImageView()
        imageView.translatesAutoresizingMaskIntoConstraints = false
        imageView.image = UIImage(systemName: "person.fill")
        return imageView
    }()
    
    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        contentView.addSubview(nameLabel)
        contentView.addSubview(titleLabel)
        contentView.addSubview(contactLabel)
        contentView.addSubview(logoImageView)
        applyConstraints()
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    private func applyConstraints() {
        NSLayoutConstraint.activate([
            nameLabel.topAnchor.constraint(equalTo: contentView.topAnchor, constant: 20),
            nameLabel.leadingAnchor.constraint(equalTo: contentView.leadingAnchor, constant: 20),
            
            titleLabel.topAnchor.constraint(equalTo: nameLabel.bottomAnchor, constant: 30),
            titleLabel.leadingAnchor.constraint(equalTo: nameLabel.leadingAnchor),
            
            contactLabel.topAnchor.constraint(equalTo: titleLabel.bottomAnchor, constant: 10),
            contactLabel.leadingAnchor.constraint(equalTo: nameLabel.leadingAnchor),
            
            logoImageView.topAnchor.constraint(equalTo: contentView.topAnchor, constant: 10),
            logoImageView.trailingAnchor.constraint(equalTo: contentView.trailingAnchor, constant: -20),
            logoImageView.widthAnchor.constraint(equalToConstant: 50),
            logoImageView.heightAnchor.constraint(equalToConstant: 50),
        ])
    }
    
    func configure(name: String, title: String, contact: String) {
        nameLabel.text = name
        titleLabel.text = title
        contactLabel.text = contact
    }
}

```
