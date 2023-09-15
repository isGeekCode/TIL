# NSObject_UIResponder_UIView_UIScrollView_UITableView : 편집스타일 설정하기 - editingStyle

테이블뷰에서 셀을 드래그하면 편집을 할 수 있는 기능이 있다.

editingStyle은 테이블 뷰의 각 셀에 대한 편집 스타일을 정의할 수 있게 해주는데, 

편집 스타일은 셀을 스와이프하거나 편집 모드로 들어갈 때 표시가 된다.

여기서 나오는 모드는 아래와 같다.

- 수정모드
- 삭제모드

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
