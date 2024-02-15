# UITableView - 템플릿

## Content
- [lazy var MockData + CustomCell](#lazy-var-mockdata--customcell)
- [inset Grouped Style](#inset-grouped-style)


<br><br>

## lazy var MockData + CustomCell
```swift
import UIKit

class ViewController: UIViewController {

    lazy var listData = Array(0...10).map { "Item\($0)" }
    
    lazy var tableView = {
        let tableView = UITableView()
        tableView.delegate = self
        tableView.dataSource = self
        tableView.register(CustomTableViewCell.self, forCellReuseIdentifier: CustomTableViewCell.identifier)
        tableView.translatesAutoresizingMaskIntoConstraints = false
        return tableView
    }()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setLayout()
    }
    
    func setLayout() {
        view.backgroundColor = .white
        view.addSubview(tableView)
        NSLayoutConstraint.activate([
            tableView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
            tableView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor),
            tableView.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor),
            tableView.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor),
        ])
    }


}

extension ViewController : UITableViewDelegate, UITableViewDataSource {
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return listData.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell =  tableView.dequeueReusableCell(withIdentifier: CustomTableViewCell.identifier, for: indexPath) as! CustomTableViewCell
        cell.textLabel?.text = listData[indexPath.row]
        return cell
    }
}

class CustomTableViewCell: UITableViewCell {

    static let identifier = "test"
    
    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier )
        print(#function)
    }
    
    required init?(coder: NSCoder) {
        super.init(coder: coder)
    }
}
```

<br><br>

## inset Grouped Style

```swift
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

//        tableView.frame = view.bounds

        tableView.translatesAutoresizingMaskIntoConstraints = false
        NSLayoutConstraint.activate([
            tableView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
            tableView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor),
            tableView.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor),
            tableView.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor),
        ])
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
