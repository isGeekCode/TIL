# UITableView : 편집스타일 설정하기 - editingStyle

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

이 영상은 아래 예시코드처럼 0번셀에는 insert, 1번셀에는 delete, 3번셀에는  none으로 처리를 하였다. 

세팅한 editButtonItem 을 이용해 활성상태를 토글해보자. 

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

<br><br><br>

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


<br><br><br>

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

여기서 해당 셀에 editing Style에 delete가 적용되어있다면 삭제가 가능한 셀에서는 swipe로도 삭제가 가능하다

<br><br>

## 동작화면
<img width="300" alt="editingStyle예시" src="https://github.com/isGeekCode/TIL/assets/76529148/90d175ad-2ddd-4a21-a5cc-68895654793c">

## 소스코드
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


<br><br><br>

# Swipe Action

> `tableView(_:editingStyle:indexPath:)`메서드는 어떤 셀에 어떤 editingStyle로 할지 구현하는 곳이다.  
> `tableView(_:commit:forRowAt:)`메서드는 어떤 editingStyle에서 어떤 동작을 할지 구현하는 곳이다.  

여기에 delete만 잘 구현이 되어있다면, swipe 액션을 따로 구현하지않아도 자동으로 swipe 액션을 지원한다.  

이 때, 동작하는 스와이프 동작은 `tableView(_:commit:forRowAt:)` 메서드에 구현한 동작이 실행된다.  

‼️‼️‼️‼️
단, 스와이프 액션으로 delete 이외의 동작을 구현해야한다면, 반드시 delete는 스와이프로 구현하고 다른 액션을 추가해야한다.  만약 구현하지않는 경우, editing Mode에서 삭제 버튼을 눌러도 동작하지않는다.  

## 정의하기

스와이프 동작은 셀의 좌측, 우측으로 정의할 수 있다. 

```swift
// 좌측
func tableView(_ tableView: UITableView, leadingSwipeActionsConfigurationForRowAt indexPath: IndexPath) -> UISwipeActionsConfiguration? { }

// 우측
func tableView(_ tableView: UITableView, trailingSwipeActionsConfigurationForRowAt indexPath: IndexPath) -> UISwipeActionsConfiguration? { } 
```

여기에 리턴할 UISwipeActionsConfiguration 타입을 구현한다.  
UISwipeActionsConfiguration은 파라미터로 `[UIContextualAction]` 배열을 받는다.  

위에서 커스텀 액션을 추가하는 경우, 반드시 delete를 구현해 주어야한다고 했다.   
먼저 삭제 로직을 구현해보자.  

```swift
func tableView(_ tableView: UITableView, trailingSwipeActionsConfigurationForRowAt indexPath: IndexPath) -> UISwipeActionsConfiguration? {

        let deleteAction = UIContextualAction(style: .destructive , title: "Delete") { (_, _, completionHandler) in
        // 삭제 로직 수행
        self.memos.remove(at: indexPath.row)
        tableView.deleteRows(at: [indexPath], with: .fade)

        completionHandler(true)
    }
    // 텍스트대신 아이콘을 표시 하고 싶은 경우
    // myAction.image = UIImage(systemName: "trash") 

    return UISwipeActionsConfiguration(actions: [deleteAction])
}
```

UIContextualAction은 이니셜라이저로 UIUIContextualAction.Style과 보여질 문자열을 옵셔널로 받는다.

```swift
convenience init(
    style: UIContextualAction.Style, // destructive, normal이 있다.  
    title: String?, // nil로 넣을 경우, 아무런 표시가 되지않는다.  
    handler: @escaping UIContextualAction.Handler
)
```
- UIContextualAction.Style
    - destructive : 기본 빨강 배경으로 표시된다. 마지막에 UIContextualAction.backgroundColor로 바꾸면 적용된다.  
    - normal : 기본 회색배경으로 표시된다.
- title? : 보여질 문자열이다. nil로 넣는 경우 아무런 표시가 나오지않는다.  
    - 만약 타이틀 대신 이미지를 보여주고 싶다면 UIContextualAction.image 를 통해 지정가능하다.
- handler : 해당 스와이프 액션시 실행할 completionHandler 이다.  
    - 만약 조건에 따라 동작 여부를 하도록 하고 싶다면 handler(:Bool)로 처리할 수 있다.  

<br><br>

## handler로 동작제어하기
조작이 익숙치 않아 실수로 delete를 하게 되면 곤란할 수 있다. 혹은 내가 미리 지정해둔 액션을 정말로 실행할 건지 조건절 처리함으로 로직 실행여부를 결정할 수 있다. 

주의해야할 점은 handler(false)로 선언을 하여도 이전에 선언해둔 코드는 실행되니 주의하자.  

아래는 얼럿을 통해 delete동작을 제어하는 예시이다.  
### 동작화면
<img width="300" alt="editingStyle예시" src="https://github.com/isGeekCode/TIL/assets/76529148/4174b658-6150-4236-9e50-10de133a7ef6">


### 소스코드
```swift
func tableView(_ tableView: UITableView, trailingSwipeActionsConfigurationForRowAt indexPath: IndexPath) -> UISwipeActionsConfiguration? {
        
    let deleteAction = UIContextualAction(style: .destructive , title: "Delete") { (_, _, completionHandler) in
        // 사용자 확인을 위한 얼럿 표시
        let alert = UIAlertController(title: "삭제 확인", message: "정말로 삭제하시겠습니까?", preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "취소", style: .cancel, handler: { _ in
            completionHandler(false)  // 사용자가 취소를 선택하면, 액션을 완료하지 않고 UI를 유지
        }))
        alert.addAction(UIAlertAction(title: "삭제", style: .destructive, handler: { _ in
            self.memos.remove(at: indexPath.row)
            tableView.deleteRows(at: [indexPath], with: .fade)
            completionHandler(true)  // 사용자가 삭제를 확정하면, 액션을 완료하고 UI를 사라지게 함
        }))
        self.present(alert, animated: true)
    }
    // 텍스트대신 아이콘을 표시 하고 싶은 경우
    // deleteAction.image = UIImage(systemName: "trash") 

    return UISwipeActionsConfiguration(actions: [deleteAction])
}
```

<br><br>

## 여러 액션 넣기
`UISwipeActionsConfiguration`의 파라미터로 `[UIContextualAction]` 배열을 받는다.
배열에 여러개의 Action을 넣게되면, 스와이프를 할 때 여러 동작을 넣을 수 있다.  
먼저 넣는 동작일 수록 가장자리에서 중심쪽으로 추가된다. 
스와이프를 끝까지 하게 되면 가장 첫번째 액션이 실행된다. 

이걸 각각 leading, trailing swipe로 구현해보자.  

## 소스코드
```swift
func tableView(_ tableView: UITableView, leadingSwipeActionsConfigurationForRowAt indexPath: IndexPath) -> UISwipeActionsConfiguration? {

        let editAction = UIContextualAction(style: .normal, title: "Edit") { (_, _, completionHandler) in
            // 편집 액션 수행
            self.editItem(at: indexPath)
            completionHandler(true)
        }
        editAction.backgroundColor = .systemTeal

        let deleteAction = UIContextualAction(style: .destructive , title: "Delete") { (_, _, completionHandler) in
            // 사용자 확인을 위한 얼럿 표시
            let alert = UIAlertController(title: "삭제 확인", message: "정말로 삭제하시겠습니까?", preferredStyle: .alert)
            alert.addAction(UIAlertAction(title: "취소", style: .cancel, handler: { _ in
                completionHandler(false)  // 사용자가 취소를 선택하면, 액션을 완료하지 않고 UI를 유지
            }))
            alert.addAction(UIAlertAction(title: "삭제", style: .destructive, handler: { _ in
                self.memos.remove(at: indexPath.row)
                tableView.deleteRows(at: [indexPath], with: .fade)
                completionHandler(true)  // 사용자가 삭제를 확정하면, 액션을 완료하고 UI를 사라지게 함
            }))
            self.present(alert, animated: true)
        }
        // 텍스트대신 아이콘을 표시 하고 싶은 경우
        deleteAction.image = UIImage(systemName: "trash") 

        return UISwipeActionsConfiguration(actions: [deleteAction, editAction])
    }

func tableView(_ tableView: UITableView, trailingSwipeActionsConfigurationForRowAt indexPath: IndexPath) -> UISwipeActionsConfiguration? {

    // 편집 액션
    let editAction = UIContextualAction(style: .normal, title: "Edit") { (_, _, completionHandler) in
        // 편집 액션 수행
        self.editItem(at: indexPath)
        completionHandler(true)
    }
    editAction.backgroundColor = .systemTeal

    // 삭제 액션
    let deleteAction = UIContextualAction(style: .destructive , title: "Delete") { (_, _, completionHandler) in
        // 사용자 확인을 위한 얼럿 표시
        let alert = UIAlertController(title: "삭제 확인", message: "정말로 삭제하시겠습니까?", preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "취소", style: .cancel, handler: { _ in
            completionHandler(false)  // 사용자가 취소를 선택하면, 액션을 완료하지 않고 UI를 유지
        }))
        alert.addAction(UIAlertAction(title: "삭제", style: .destructive, handler: { _ in
            self.memos.remove(at: indexPath.row)
            tableView.deleteRows(at: [indexPath], with: .fade)
            completionHandler(true)  // 사용자가 삭제를 확정하면, 액션을 완료하고 UI를 사라지게 함
        }))
        self.present(alert, animated: true)
    }
    // 텍스트대신 아이콘을 표시 하고 싶은 경우
    deleteAction.image = UIImage(systemName: "trash") 

    return UISwipeActionsConfiguration(actions: [deleteAction, editAction])
}

```

## 동작화면
<img width="300" alt="스와이프 여러 동작" src="https://github.com/isGeekCode/TIL/assets/76529148/53bab6b5-651b-4234-9690-7b52d0b017d6">

여기서 얼럿을 사용하고 얼럿 후 동작까지 구현해야한다면 함수로 쪼개서 아래와 같이 사용할 수 있겠다. 
편의상 trailing에 구현해보자. 어차피 얼럿으로 분기처리할 예정이기 때문에 completionHandler(true)만 사용해도 상관없다.  

```swift
func tableView(_ tableView: UITableView, trailingSwipeActionsConfigurationForRowAt indexPath: IndexPath) -> UISwipeActionsConfiguration? {

    let editAction = UIContextualAction(style: .normal, title: "Edit") { (_, _, completionHandler) in
        // 편집 액션 수행
        self.editItem(at: indexPath)
        completionHandler(true)
    }
    editAction.backgroundColor = .systemTeal


    let deleteAction = UIContextualAction(style: .destructive , title: "Delete") { (_, _, completionHandler) in
        // 사용자 확인을 위한 얼럿 표시
        self.deleteItem(at: indexPath)
        completionHandler(true)
    }
    // 텍스트대신 아이콘을 표시 하고 싶은 경우
    deleteAction.image = UIImage(systemName: "trash") 

    return UISwipeActionsConfiguration(actions: [deleteAction, editAction])
}

func deleteItem(at indexPath: IndexPath) {
    
    let alertController = UIAlertController(title: "삭제 확인", message: "정말로 삭제하시겠습니까?", preferredStyle: .alert)
    let cancelAction = UIAlertAction(title: "취소", style: .cancel, handler: nil)
    let deleteAction = UIAlertAction(title: "삭제", style: .destructive, handler: { _ in
        self.deleteMemo(at: indexPath)
    })
    alertController.addAction(cancelAction)
    alertController.addAction(deleteAction)

    present(alertController, animated: true, completion: nil)
}


// 데이터 모델 및 뷰 업데이트
func deleteMemo(at indexPath: IndexPath) {
    // 데이터 모델 업데이트
    self.memos.remove(at: indexPath.row)
    // 테이블 뷰의 해당 셀 업데이트
    tableView.deleteRows(at: [indexPath], with: .fade)
}


// 항목 수정 얼럿 생성
func editItem(at indexPath: IndexPath) {
    let alertController = UIAlertController(title: "Edit Item", message: nil, preferredStyle: .alert)
    alertController.addTextField { (textField) in
        textField.text = self.memos[indexPath.row]
    }

    let cancelAction = UIAlertAction(title: "취소", style: .cancel, handler: nil)
    let saveAction = UIAlertAction(title: "저장", style: .default) { (_) in
        if let editedText = alertController.textFields?.first?.text {
            self.updateMemo(at: indexPath, with: editedText)
        }
    }

    alertController.addAction(cancelAction)
    alertController.addAction(saveAction)
    present(alertController, animated: true, completion: nil)
    
    
}

// 데이터 모델 및 뷰 업데이트
func updateMemo(at indexPath: IndexPath, with newText: String) {
    // 데이터 모델 업데이트
    self.memos[indexPath.row] = newText
    // 테이블 뷰의 해당 셀 업데이트
    self.tableView.reloadRows(at: [indexPath], with: .automatic)
}
```

<br><br><br>


## History
- 230915: 초안작성
- 240208: 스와이프 추가, editingStyle 추가
