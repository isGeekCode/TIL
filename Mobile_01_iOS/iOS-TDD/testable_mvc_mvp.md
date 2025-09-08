# Testable한 코드 만들기1 - VC -> MVC -> MVP


## ViewController하나로 기본 예제 만들기

```swift
import UIKit

// MARK: Model
struct Task {
    let title: String
    var completed: Bool
}


protocol TaskViewProtocol: AnyObject {
    func displayTasks(_ tasks: [Task])
}

class ViewController: UIViewController, TaskViewProtocol {
    
    var tasks: [Task] = []
    
    let myLabel: UILabel = {
        let label = UILabel()
        label.translatesAutoresizingMaskIntoConstraints = false
        label.text = "초기값"
        return label
    }()
    
    lazy var myButton: UIButton = {
        let button = UIButton()
        button.translatesAutoresizingMaskIntoConstraints = false
        button.setTitle("버튼", for: .normal)
        button.addTarget(self, action: #selector(buttonTapped(_:)), for: .touchUpInside)
        button.setTitleColor(.systemBlue, for: .normal)
        return button
    }()

    override func viewDidLoad() {
        super.viewDidLoad()
        setLayout()
    }
    
    func setLayout() {
        view.backgroundColor = .systemYellow
        view.addSubview(myLabel)
        view.addSubview(myButton)
        NSLayoutConstraint.activate([
            myLabel.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            myLabel.centerYAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerYAnchor),
            myButton.topAnchor.constraint(equalTo: myLabel.bottomAnchor, constant: 30),
            myButton.centerXAnchor.constraint(equalTo: myLabel.centerXAnchor),
        ])
        
    }

    @objc func buttonTapped(_ sender: UIButton) {
        addTask(title: "1")
    }
    
    func addTask(title: String) {
        let newTask = Task(title: title, completed: false)
        tasks.append(newTask)
        displayTasks(tasks)
    }
    
    func displayTasks(_ tasks: [Task]) {
        // UI 업데이트 로직
        var value = ""
        
        for i in tasks {
            value += i.title
        }
        myLabel.text = "\(value)"
    }
    
}

```

<br><br>


## MVC패턴
1. 데이터는 모두 Model로 가져간다.
2. View와 Controller를 분리한다.
3. View는 View를 업데이트 시키기위한 메서드를 제공한다.
4. 데이터 포맷팅은 Controller에서 진행해준다. 
    - Model은 데이터 자체만을 다뤄야한다.
    - View에서는 데이터를 다루지 않는다
    - 그래서 Controller에서 진행해야한다.

```swift
import UIKit

protocol TaskViewProtocol: AnyObject {
    func displayTasks(_ tasks: [Task])
}


// MARK: Model
class TaskManager {
    
    private var tasks: [Task] = []

    init() {
        
    }
    
    func setInitTasks() {
        tasks = [Task(title: "초기값", completed: false)]
    }
    
    func getTasks() -> [Task] {
        return tasks
    }
    
    func addTask(title: String) {
        let newTask = Task(title: title, completed: false)
        tasks.append(newTask)
    }

}


// MARK: View
class MyView: UIView {
    
    private let myLabel: UILabel = {
        let label = UILabel()
        label.translatesAutoresizingMaskIntoConstraints = false
        return label
    }()
    
    var myButton: UIButton = {
        let button = UIButton()
        button.translatesAutoresizingMaskIntoConstraints = false
        button.setTitle("버튼", for: .normal)
        button.setTitleColor(.systemBlue, for: .normal)
        return button
    }()
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        translatesAutoresizingMaskIntoConstraints = false
        setUI()
    }
    
    private func setUI() {
        
        addSubview(myLabel)
        addSubview(myButton)
        
        NSLayoutConstraint.activate([
            myLabel.centerXAnchor.constraint(equalTo: centerXAnchor),
            myLabel.centerYAnchor.constraint(equalTo: centerYAnchor),
            
            myButton.topAnchor.constraint(equalTo: myLabel.bottomAnchor, constant: 20), // 조정된 간격
            myButton.centerXAnchor.constraint(equalTo: centerXAnchor),
            myButton.widthAnchor.constraint(equalToConstant: 100), // 버튼 너비
            myButton.heightAnchor.constraint(equalToConstant: 50)  // 버튼 높이
        ])
    }
    
    // 외부에서 myLabel에 접근해서 부여할 수 있도록 메서드 구현
    func display(value: String) {
        myLabel.text = value
    }
}

// MARK: Controller
class ViewController: UIViewController, TaskViewProtocol {
    
    let myTaskManager = TaskManager()
    var myView = MyView()

    override func viewDidLoad() {
        super.viewDidLoad()
        setLayout()
        setButtonAction()
        myTaskManager.setInitTasks()
    }
    
    func setLayout() {
        view.backgroundColor = .systemYellow
        view.addSubview(myView)
        
        let width = view.bounds.width * 0.8
        let height = view.bounds.height * 0.5

        NSLayoutConstraint.activate([
            myView.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            myView.centerYAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerYAnchor),
            myView.widthAnchor.constraint(equalToConstant: width),
            myView.heightAnchor.constraint(equalToConstant: height)
        ])
    }
    
    // 컨트롤러 역할
    func setButtonAction() {
        myView.myButton.addTarget(self, action: #selector(buttonTapped(_:)), for: .touchUpInside)
    }

    @objc func buttonTapped(_ sender: UIButton) {
        myTaskManager.addTask(title: "1")
        displayTasks(myTaskManager.getTasks())
    }
    
    
    /// UI 업데이트 로직
    func displayTasks(_ tasks: [Task]) {
        let tasks = myTaskManager.getTasks()
        let value = tasks.map { $0.title }.joined(separator: " ")
        myView.display(value: value)
    }
}


```

<br><br>

## MVP

```swift
import UIKit

protocol TaskViewProtocol: AnyObject {
    func display(value: String)
}


// MARK: Model
class TaskManager {
    
    private var tasks: [Task] = []

    init() {
        
    }
    
    func setInitTasks() {
        tasks = [Task(title: "초기값", completed: false)]
    }
    
    func getTasks() -> [Task] {
        return tasks
    }
    
    func addTask(title: String) {
        let newTask = Task(title: title, completed: false)
        tasks.append(newTask)
    }

}


// MARK: View
class MyView: UIView, TaskViewProtocol {
    
    private let myLabel: UILabel = {
        let label = UILabel()
        label.translatesAutoresizingMaskIntoConstraints = false
        return label
    }()
    
    var myButton: UIButton = {
        let button = UIButton()
        button.translatesAutoresizingMaskIntoConstraints = false
        button.setTitle("버튼", for: .normal)
        button.setTitleColor(.systemBlue, for: .normal)
        return button
    }()
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        translatesAutoresizingMaskIntoConstraints = false
        setUI()
    }
    
    private func setUI() {
        
        addSubview(myLabel)
        addSubview(myButton)
        
        NSLayoutConstraint.activate([
            myLabel.centerXAnchor.constraint(equalTo: centerXAnchor),
            myLabel.centerYAnchor.constraint(equalTo: centerYAnchor),
            
            myButton.topAnchor.constraint(equalTo: myLabel.bottomAnchor, constant: 20), // 조정된 간격
            myButton.centerXAnchor.constraint(equalTo: centerXAnchor),
            myButton.widthAnchor.constraint(equalToConstant: 100), // 버튼 너비
            myButton.heightAnchor.constraint(equalToConstant: 50)  // 버튼 높이
        ])
    }
    
    // 외부에서 myLabel에 접근해서 부여할 수 있도록 메서드 구현
    func display(value: String) {
        myLabel.text = value
    }
}


// MARK: Presenter
class TaskPresenter {
    weak var view: TaskViewProtocol?
    var myTaskManager = TaskManager()
    
    init(view: TaskViewProtocol) {
        self.view = view
        myTaskManager.setInitTasks()
    }
    
    func addButtonAction(button: UIButton) {
        button.addTarget(self, action: #selector(buttonTapped), for: .touchUpInside)
    }
    
    @objc func buttonTapped() {
        myTaskManager.addTask(title: "초기값 1")
        let tasks = myTaskManager.getTasks()
        let value = tasks.map { $0.title }.joined(separator: " ")
        print(value)
        view?.display(value: value)
    }
}

// MARK: Setup in ViewController
class ViewController: UIViewController {
    
    var presenter: TaskPresenter?
    var myView = MyView()

    override func viewDidLoad() {
        super.viewDidLoad()
        setLayout()
        setupPresenter()
    }
    
    private func setupPresenter() {
        presenter = TaskPresenter(view: myView)
        presenter?.addButtonAction(button: myView.myButton)
    }
    
    func setLayout() {
        view.backgroundColor = .systemYellow
        view.addSubview(myView)
        
        let width = view.bounds.width * 0.8
        let height = view.bounds.height * 0.5

        NSLayoutConstraint.activate([
            myView.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            myView.centerYAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerYAnchor),
            myView.widthAnchor.constraint(equalToConstant: width),
            myView.heightAnchor.constraint(equalToConstant: height)
        ])
    }
}



```

<br><br>

## Unit Test

```swift
import XCTest
@testable import Testable

class TaskPresenterTests: XCTestCase {
    
    var presenter: TaskPresenter!
    var mockView: MockView!
    var taskManager: TaskManager!
    
    
    override func setUp() {
        super.setUp()
        mockView = MockView()
        taskManager = TaskManager()
        presenter = TaskPresenter(view: mockView)
        presenter.myTaskManager = taskManager
    }
    
    func testAddTask() {
        print("테스트중")
        presenter.buttonTapped()
        XCTAssertEqual(mockView.displayedValue, "초기값 1")
    }
}


class MockView: TaskViewProtocol {
    
    var displayedValue: String?

    func display(value: String) {
        displayedValue = value
    }
}

```
