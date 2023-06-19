# MVC to MVVM : 02. TableVC 클릭시 텍스트 변경

## 기존 MVC 구조

### Model
```swift
// MARK: - MODEL
struct Task {
    let id: Int
    let title: String
    let completed: Bool
}
```
  
  
### View
```swift
// MARK: - VIEW
private let tableView = UITableView()

private func setupUI() {
    tableView.translatesAutoresizingMaskIntoConstraints = false
    tableView.delegate = self
    tableView.dataSource = self
    view.addSubview(tableView)
    
    NSLayoutConstraint.activate([
        tableView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
        tableView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
        tableView.topAnchor.constraint(equalTo: view.topAnchor),
        tableView.bottomAnchor.constraint(equalTo: view.bottomAnchor)
    ])
}

func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
    print("didSelectRowAt::: \(indexPath.row)")
    changeTask(index: indexPath.row)
}

```
  
  
### Controller
```swift
// MARK: CONTROLLER
override func viewDidLoad() {
    super.viewDidLoad()
    setupUI()
    setTasks()
}

func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
    return tasks.count
}

func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    let cell = UITableViewCell(style: .subtitle, reuseIdentifier: "TaskCell")
    let task = tasks[indexPath.row]
    cell.textLabel?.text = task.title
    cell.detailTextLabel?.text = task.completed ? "Completed" : "Not Completed"
    return cell
}

private var tasks: [Task] = []

private func setTasks() {
    
    let tasks = [
        Task(id: 1, title: "Task 1", completed: false),
        Task(id: 2, title: "Task 2", completed: true),
        Task(id: 3, title: "Task 3", completed: true)
    ]
    
    self.tasks = tasks
    self.tableView.reloadData()
}

private func changeTask(index: Int) {
    var currentTask = self.tasks
    
    let willSetBool = currentTask[index].completed == true ? false : true
    currentTask[index] = Task(id: index + 1, title: "Task \(index + 1)", completed: willSetBool)
    self.tasks = currentTask
    self.tableView.reloadData()
}

```
  
  
## MVC 전체코드
```swift
//
//  TaskViewController.swift
//  UTCTime
//
//  Created by bang_hyeonseok on 2023/06/16.
//

import UIKit

class TaskViewController: UIViewController, UITableViewDelegate, UITableViewDataSource {
    
    // MARK: - VIEW
    private let tableView = UITableView()

    private func setupUI() {
        tableView.translatesAutoresizingMaskIntoConstraints = false
        tableView.delegate = self
        tableView.dataSource = self
        view.addSubview(tableView)
        
        NSLayoutConstraint.activate([
            tableView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            tableView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
            tableView.topAnchor.constraint(equalTo: view.topAnchor),
            tableView.bottomAnchor.constraint(equalTo: view.bottomAnchor)
        ])
    }
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        print("didSelectRowAt::: \(indexPath.row)")
        changeTask(index: indexPath.row)
    }
    

    // MARK: CONTROLLER
    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
        setTasks()
    }

    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return tasks.count
    }

    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = UITableViewCell(style: .subtitle, reuseIdentifier: "TaskCell")
        let task = tasks[indexPath.row]
        cell.textLabel?.text = task.title
        cell.detailTextLabel?.text = task.completed ? "Completed" : "Not Completed"
        return cell
    }

    private var tasks: [Task] = []

    private func setTasks() {
        
        let tasks = [
            Task(id: 1, title: "Task 1", completed: false),
            Task(id: 2, title: "Task 2", completed: true),
            Task(id: 3, title: "Task 3", completed: true)
        ]
        
        self.tasks = tasks
        self.tableView.reloadData()
    }
    
    private func changeTask(index: Int) {
        var currentTask = self.tasks
        
        let willSetBool = currentTask[index].completed == true ? false : true
        currentTask[index] = Task(id: index + 1, title: "Task \(index + 1)", completed: willSetBool)
        self.tasks = currentTask
        self.tableView.reloadData()
    }

    // MARK: - MODEL
    struct Task {
        let id: Int
        let title: String
        let completed: Bool
    }
}

```


## History
- 230619 : 예제 생성
