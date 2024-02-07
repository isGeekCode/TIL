# NSObject_UIResponder_UIView_UIScrollView_UITableView : 편집스타일 설정하기 - editingStyle

일반적으로 우리가 앱을 경험하게 되면 UX상 테이블에서 셀을 스와이프 하여 앱을 편집 / 삭제 하는 경우가 있다. 

또, 아예 버튼이 있어서 편집모드를 켜고 끌 수 있는 경우도 있다.  

이때, tableView를 편집할 수 있는 상태를 Editing mode라고 부른다. 

그리고 Editing mode일때나 스와이프로 사용할 수 있는 편집 스타일을 editingStyle이라고 한다.  

editingStyle은 테이블 뷰의 각 셀에 대한 편집 스타일을 정의할 수 있게 해주는데, 

여기서 나오는 editingStyle은 아래와 같다.
- 수정모드
- 삭제모드
- None



## 편집모드
테이블뷰에는 Editing 모드가 있어서 이걸 켜고 끌 수가 있다.  

활성화가 되면 editingStyle이 활성화가 되는 것이다.  

아래 예제를 보고 모드에 대해 알아보자.   

UIViewController에서 제공하는 기본 편집 버튼은 UIBarButtonItem으로 존재하기 때문에, 네비게이션바를 세팅하고 사용한다.

```swift
extension UIViewController {

    open var isEditing: Bool

    open func setEditing(_ editing: Bool, animated: Bool)

    open var editButtonItem: UIBarButtonItem { get }
}
```

이걸 세팅해보자. 

<img width="300" alt="editingStyle예시" src="https://github.com/isGeekCode/TIL/assets/76529148/308df10e-ba6d-412a-8610-4cc572d697f9">


```swift

class MemoViewController: UIViewController, UITableViewDataSource, UITableViewDelegate {

    var memos: [String] = ["A", "B", "C"]

    // 중간 생략
    override func viewDidLoad() {
        super.viewDidLoad()
        tableView.dataSource = self
        tableView.delegate = self
        self.navigationItem.rightBarButtonItem = self.editButtonItem // 편집버튼
    }
    
    // isEditing을 추적하여 처리되는 메서드
    override func setEditing(_ editing: Bool, animated: Bool) {
            super.setEditing(editing, animated: animated)
    }

    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return memos.count
    }

    // editing mode에 표시할 스타일 세팅
    func tableView(_ tableView: UITableView, editingStyleForRowAt indexPath: IndexPath) -> UITableViewCell.EditingStyle {
        
        if indexPath.row == 0 {
            return .insert
        } else if indexPath.row == 1 {
            return .delete 
        } else {
            return .none
        }
    }

}
```

### 커스텀 편집 버튼
만약 uiviewController에서 제공하는 UIBarButtonItem을 사용하지않는다면, 새롭게 buttonAction을 구현할 수 있다.  

다만 커스텀 편집 버튼을 사용하는 경우,

```
override func setEditing(_ editing: Bool, animated: Bool) {
    super.setEditing(editing, animated: animated)
}
```

위 메서드의 animated값이 false로 들어오게 되니 유의하자.  커스텀으로 만드는 경우 구태여 이 메서드는 만들지 않아도된다.  

```swift

class MemoViewController: UIViewController {

    var memos: [String] = ["A", "B", "C"]
    var editButton: UIButton!

    @IBOutlet weak var tableView: UITableView!
    @IBOutlet weak var memoTextField: UITextField!

    override func viewDidLoad() {
        super.viewDidLoad()
        tableView.dataSource = self
        tableView.delegate = self
        
        // Edit 버튼 초기화 및 설정
        editButton = UIButton(type: .system)
        editButton.setTitle("Edit", for: .normal)
        editButton.addTarget(self, action: #selector(toggleEditMode), for: .touchUpInside)
        navigationItem.rightBarButtonItem = UIBarButtonItem(customView: editButton)
    }
        
    @objc func toggleEditMode() {
        self.isEditing = !isEditing
        self.tableView.setEditing(self.isEditing, animated: true)

        let buttonTitle = self.isEditing ? "Done" : "Edit"
        
        DispatchQueue.main.async {
            self.editButton.setTitle(buttonTitle, for: .normal)
            self.editButton.sizeToFit() // 필요한 경우만 사용
        }
    }
    // tableview 메서드 생략
}
```


## 네비게이션 바 + 버튼으로 Insert 동작시키기
네비게이션바에 추가하기 때문에  NavigationController에 현재 ViewControleller가 추가되어있어야한다. 
이 경우에는  
```swift

var memos: [String] = ["A","B"]

override func viewDidLoad() {
    super.viewDidLoad()

    // 기존 코드...
    // 네비게이션 바에 "+" 버튼 추가
    let addButton = UIBarButtonItem(barButtonSystemItem: .add, target: self, action: #selector(addNewMemo))
    self.navigationItem.leftBarButtonItem = addButton
}

@objc func addNewMemo() {
    // 새로운 메모 추가 로직
    memos.append("새 메모")
    
    // 테이블 뷰에 새 행 추가
    let newIndexPath = IndexPath(row: memos.count - 1, section: 0)
    tableView.insertRows(at: [newIndexPath], with: .automatic)
    
    // tableView.reloadData() 를 하게 되면 애니메이션이 생기지 않는다. 
}

```

# Editing Style 구현하기
위에서 소개한 내용은 네비게이션 바에 있는 기능을 통해 변화를 주는 기능이었다면, 

이제 소개할 내용은 테이블뷰에 사용할 편집모드를 미리 설정하는 작업이다. 
 
editingStyle은 위에서 살펴본것 처럼 3가지이다.
- insert : 삽입하기
- delete : 삭제하기
- none : 아무 동작 없음

```swift
    // editing mode에 표시할 스타일 세팅
    func tableView(_ tableView: UITableView, editingStyleForRowAt indexPath: IndexPath) -> UITableViewCell.EditingStyle {
        
        if indexPath.row == 0 {
            return .insert
        } else if indexPath.row == 1 {
            return .delete 
        } else {
            return .none
        }
    }
    
    // 사용할 편집모드 구현
    func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCell.EditingStyle, forRowAt indexPath: IndexPath) {
        if editingStyle == .insert {
            // 현재 셀의 IndexPath에 추가 : 현재 셀 상단에 추가되는 효과

            // 데이터 모델에서 해당 항목 추가
            memos.insert("새 메모", at: indexPath.row)
            // 테이블 뷰에서 해당 셀 추가 
            tableView.insertRows(at: [indexPath], with: .automatic)
            
            /*
            // 현재 셀의 다음 IndexPath에 추가 : 현재 셀 하단에 추가되는 효과
            memos.insert("새 메모", at: indexPath.row + 1)
            let nextIndexPathRow = IndexPath(row: indexPath.row + 1,
                                             section: indexPath.section)

            tableView.insertRows(at: [nextIndexPathRow], with: .automatic)
            */
            
        }
        
        if editingStyle == .delete {
            // 데이터 모델에서 해당 항목 삭제
            memos.remove(at: indexPath.row)
            // 테이블 뷰에서 해당 셀 삭제
            tableView.deleteRows(at: [indexPath], with: .automatic)
        }
    }
```


# Swipe Action
스와이프 기능은 Editing Mode와 달리 row에 적용되어 셀의 왼쪽 오른쪽에 구현을 할 수 있다.  









## 동작화면

<img width="300" alt="스크린샷 2023-07-21 오후 4 25 33" src="https://github.com/isGeekCode/TIL/assets/76529148/21072645-4b44-4d3f-ace9-871bf95f6e5f">


## 

```swift
import UIKit

class MyTableViewController: UITableViewController {

    var items: [String] = ["Item 1", "Item 2", "Item 3"]

    override func viewDidLoad() {
        super.viewDidLoad()
        navigationItem.rightBarButtonItem = editButtonItem
    }

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return items.count
    }

    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath)
        cell.textLabel?.text = items[indexPath.row]
        return cell
    }

    override func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCell.EditingStyle, forRowAt indexPath: IndexPath) {
        if editingStyle == .delete {
            // 삭제 버튼을 누를 때 항목을 삭제
            items.remove(at: indexPath.row)
            tableView.deleteRows(at: [indexPath], with: .fade)
        } else if editingStyle == .insert {
            // 삽입 버튼을 누를 때 항목을 추가 (여기서는 사용하지 않음)
        }
    }

    // 편집 스타일 지원
    override func tableView(_ tableView: UITableView, editingStyleForRowAt indexPath: IndexPath) -> UITableViewCell.EditingStyle {
        if isEditing {
            // 편집 모드일 때는 삭제 스타일을 사용하고, 그렇지 않을 때는 삽입 스타일을 사용
            return .delete
        }
        return .insert
    }

    // 스와이프해서 편집 모드로 전환
    override func tableView(_ tableView: UITableView, leadingSwipeActionsConfigurationForRowAt indexPath: IndexPath) -> UISwipeActionsConfiguration? {
        let editAction = UIContextualAction(style: .normal, title: "Edit") { (_, _, completionHandler) in
            // 편집 액션 수행
            self.editItem(at: indexPath)
            completionHandler(true)
        }
        editAction.backgroundColor = .blue
        return UISwipeActionsConfiguration(actions: [editAction])
    }

    // 스와이프해서 삭제
    override func tableView(_ tableView: UITableView, trailingSwipeActionsConfigurationForRowAt indexPath: IndexPath) -> UISwipeActionsConfiguration? {
        let deleteAction = UIContextualAction(style: .destructive, title: "Delete") { (_, _, completionHandler) in
            // 삭제 액션 수행
            self.deleteItem(at: indexPath)
            completionHandler(true)
        }
        return UISwipeActionsConfiguration(actions: [deleteAction])
    }

    // 항목 추가
    @IBAction func addItem(_ sender: Any) {
        let newItem = "New Item"
        items.append(newItem)
        let indexPath = IndexPath(row: items.count - 1, section: 0)
        tableView.insertRows(at: [indexPath], with: .automatic)
    }

    // 항목 수정
    func editItem(at indexPath: IndexPath) {
        let alertController = UIAlertController(title: "Edit Item", message: nil, preferredStyle: .alert)
        alertController.addTextField { (textField) in
            textField.text = self.items[indexPath.row]
        }

        let cancelAction = UIAlertAction(title: "Cancel", style: .cancel, handler: nil)
        let saveAction = UIAlertAction(title: "Save", style: .default) { (_) in
            if let editedText = alertController.textFields?.first?.text {
                self.items[indexPath.row] = editedText
                self.tableView.reloadRows(at: [indexPath], with: .automatic)
            }
        }

        alertController.addAction(cancelAction)
        alertController.addAction(saveAction)
        present(alertController, animated: true, completion: nil)
    }

    // 항목 삭제
    func deleteItem(at indexPath: IndexPath) {
        items.remove(at: indexPath.row)
        tableView.deleteRows(at: [indexPath], with: .fade)
    }
}

```




## History
- 230915: 초안작성
