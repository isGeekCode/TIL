# sample App - 투두리스트

투두리스트의 요소는 아래와 같다.

- 최소기능
    - 리스트에 들어갈 객체
    - 리스트 추가
    - 리스트 제거
    
- 추가기능
    - 체크박스
    - 리스트 순서 변경
    - 악세서리 타입
    - 디테일 페이지

또한 투두리스트에서 가장 중요한 것은 두가지라고 할 수있다.  

1. 투두리스트 데이터를 어떻게 관리하느냐  
2. UI로 어떻게 바인딩 할 것인가  

데이터의 변경은 UI의 업데이트로 이어져야한다.  
<br><br><br>

## MVC
최소기능만 넣어서 가장 간단한 코드로 만들어봤다.  
  
- 최소기능  
    - 리스트에 들어갈 객체  
    - 리스트 추가 
    - 리스트 제거
<br><br>

### 전체 코드
```swift
import UIKit

// 할일 객체
class ToDoItem {
    let title: String

    init(title: String) {
        self.title = title
    }
}

///  투두리스트를 추가: 버튼클릭, 투두리스트 삭제: 테이블뷰의 칸 클릭
class ToDoListViewController: UIViewController {
    
    @IBOutlet weak var tableView: UITableView!
    
    var toDoItems: [ToDoItem] = []
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        tableView.register(UITableViewCell.self, forCellReuseIdentifier: "cell")
        tableView.dataSource = self
        tableView.delegate = self
        
        // 더미데이터
        toDoItems.append(ToDoItem(title: "할 일 1"))
        tableView.reloadData()
    }

    @IBAction func btnAction(_ sender: Any) {
        let alertController = UIAlertController(title: "Add ToDo", message: nil, preferredStyle: .alert)
        alertController.addTextField { textField in
            textField.placeholder = "Enter title"
        }

        let addAction = UIAlertAction(title: "Add", style: .default) { [weak self] _ in
            if let title = alertController.textFields?.first?.text {
                self?.toDoItems.append(ToDoItem(title: title))
                self?.tableView.reloadData()
            }
        }

        let cancelAction = UIAlertAction(title: "Cancel", style: .cancel, handler: nil)

        alertController.addAction(addAction)
        alertController.addAction(cancelAction)

        present(alertController, animated: true, completion: nil)
    }
}

extension ToDoListViewController: UITableViewDataSource, UITableViewDelegate {

    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return toDoItems.count
    }

    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "cell", for: indexPath)
        let toDoItem = toDoItems[indexPath.row]
        cell.textLabel?.text = toDoItem.title
        return cell
    }

    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        let alertController = UIAlertController(title: "Remove ToDo", message: "Do you want to remove this item?", preferredStyle: .alert)

        let removeAction = UIAlertAction(title: "Remove", style: .destructive) { [weak self] _ in
            self?.toDoItems.remove(at: indexPath.row)
            self?.tableView.reloadData()
        }

        let cancelAction = UIAlertAction(title: "Cancel", style: .cancel, handler: nil)

        alertController.addAction(removeAction)
        alertController.addAction(cancelAction)

        present(alertController, animated: true, completion: nil)
    }
}
```
<br><br>

[[top]](#-sample-app---투두리스트)

<br><br><br>


## History
- 230728: MVP정의, MVC구현

