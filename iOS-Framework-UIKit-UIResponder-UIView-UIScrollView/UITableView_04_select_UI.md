# UITableView - 셀 선택, 삭제 및 상호작용

<br><br>

## 선택 액션 추가하기

셀을 선택하는 데에 있어서 

```
// UITableViewDelegate 메서드 - 셀 선택
func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
    
    // 현재 선택한 ROW값을 통해 데이터를 추출
    let selectedItem = itemList[indexPath.row]
    // 선택완료 이후에 다시 비활성화 처리
    tableView.deselectRow(at: indexPath, animated: true)
} 
```

<br><br>

## 셀 삭제 액션 추가하기
테이블뷰에는 다양한 스와이프 액션이 있지만 삭제기능만 추가하는 경우, 아주 간단하게 세팅이 가능하다. 
삭제 이외의 스와이프액션을 추가하려면 살짝 과정이 추가되니 참고하자.

```swift
// UITableViewDelegate 메서드 - 셀 삭제
func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCell.EditingStyle, forRowAt indexPath: IndexPath) {
    if editingStyle == .delete {
        // 데이터도 같이 삭제처리
        itemList.remove(at: indexPath.row)
        // 테이블뷰 UI상 삭제처리
        tableView.deleteRows(at: [indexPath], with: .automatic)
    }
}

```

<br><br>

편집스타일 및 스와이프 액션에 대해 더 자세한 내용은 아래 링크를 참고하자. 
[UITableView : 편집스타일 설정하기 - editingStyle](https://github.com/isGeekCode/TIL/blob/main/iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_10_editingStyle.md)


<br><br>

## 얼럿 추가하기
사용자 상호작용에 있어서 바로 동작을 실행하는 것 보다는 사용자에게 확인을 하는 단계를 거칠 수 있다. 
바로 얼럿을 사용하는 것이다.  


```swift
    // 간단한 알림 표시 메서드
func showAlert(message: String, completion: @escaping () -> ()) {
    let alert = UIAlertController(title: nil, message: message, preferredStyle: .alert)
    alert.addAction(UIAlertAction(title: "취소", style: .destructive))
    alert.addAction(UIAlertAction(title: "확인", style: .default) { _ in
        completion()
    })
    present(alert, animated: true)
}

```

<br>

탈출클로저를 이용하여 얼럿 확인을 누르면 동작하도록 세팅하자.  


```swift
// UITableViewDelegate 메서드 - 셀 선택
func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
    
    let selectedItem = itemList[indexPath.row]
    showAlert(message: "\(selectedItem) 선택됨") { 
        tableView.deselectRow(at: indexPath, animated: true)
    }
}

// UITableViewDelegate 메서드 - 셀 삭제
func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCell.EditingStyle, forRowAt indexPath: IndexPath) {
    if editingStyle == .delete {
        showAlert(message: "\(indexPath.row)를 삭제하시겠습니까") { 
            self.itemList.remove(at: indexPath.row)
            tableView.deleteRows(at: [indexPath], with: .automatic)
        }
    }
}

```

<br><br>


### 전체코드
```swift
class ViewController: UIViewController {
    
    var itemList: [String] = ["Item 1", "Item 2", "Item 3"]
    var tableView = UITableView()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setUI()
        setDetail()
    }
    
    
    func setDetail() {
        tableView.dataSource = self
        tableView.delegate = self
        tableView.register(UITableViewCell.self, forCellReuseIdentifier: "cell")
    }
    
    func setUI() {
        view.addSubview(tableView)
        tableView.frame = view.bounds
    }
}

extension ViewController: UITableViewDelegate, UITableViewDataSource {
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return itemList.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        
        let cell = tableView.dequeueReusableCell(withIdentifier: "cell", for: indexPath)
        cell.textLabel?.text = itemList[indexPath.row]
        return cell
    }
        
    // UITableViewDelegate 메서드 - 셀 선택
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        
        let selectedItem = itemList[indexPath.row]
        showAlert(message: "\(selectedItem) 선택됨") { 
            tableView.deselectRow(at: indexPath, animated: true)
        }
    }
    
    // UITableViewDelegate 메서드 - 셀 삭제
    func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCell.EditingStyle, forRowAt indexPath: IndexPath) {
        if editingStyle == .delete {
            showAlert(message: "\(indexPath.row)를 삭제하시겠습니까") { 
                self.itemList.remove(at: indexPath.row)
                tableView.deleteRows(at: [indexPath], with: .automatic)
            }
        }
    }
    
    // 간단한 알림 표시 메서드
    func showAlert(message: String, completion: @escaping () -> ()) {
        let alert = UIAlertController(title: nil, message: message, preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "취소", style: .destructive))
        alert.addAction(UIAlertAction(title: "확인", style: .default) { _ in
            completion()
        })
        present(alert, animated: true)
    }
}
```

