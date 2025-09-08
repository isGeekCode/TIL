# UITableView - 동적 셀 높이

<br><br>

## 텍스트 양에 따른 동적 셀 높이

```swift
// 샘플 데이터
let items = [
    "짧은 텍스트",
    "매우 긴 텍스트 예시입니다. 이 텍스트는 셀의 높이가 동적으로 조정되어야 온전히 표시될 수 있습니다. Auto Layout을 사용하여 셀의 높이가 콘텐츠에 따라 자동으로 변하도록 구현할 수 있습니다.",
    "또 다른 짧은 텍스트"
]

// 동적 셀 높이 설정
tableView.rowHeight = UITableView.automaticDimension
tableView.estimatedRowHeight = 44 // 기본값으로 사용할 높이



func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    let cell = UITableViewCell(style: .default, reuseIdentifier: "cell")
    cell.textLabel?.text = items[indexPath.row]
    cell.textLabel?.numberOfLines = 0 // 무제한 라인 수 설정
    return cell 
}

```



### 작업화면

<img width="300" alt="editingStyle예시" src="https://github.com/isGeekCode/TIL/assets/76529148/75668bf4-bf12-4d08-b6df-359dbef36fda">



<br><br>

### 전체코드

```swift
import UIKit

class ViewController: UIViewController, UITableViewDelegate, UITableViewDataSource {
    
    var tableView: UITableView!
    
    // 샘플 데이터
    let items = [
        "짧은 텍스트",
        "매우 긴 텍스트 예시입니다. 이 텍스트는 셀의 높이가 동적으로 조정되어야 온전히 표시될 수 있습니다. Auto Layout을 사용하여 셀의 높이가 콘텐츠에 따라 자동으로 변하도록 구현할 수 있습니다.",
        "또 다른 짧은 텍스트"
    ]
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        tableView = UITableView(frame: view.bounds, style: .plain)
        tableView.delegate = self
        tableView.dataSource = self
        
        // 동적 셀 높이 설정
        tableView.rowHeight = UITableView.automaticDimension
        tableView.estimatedRowHeight = 44 // 기본값으로 사용할 높이
        
        view.addSubview(tableView)
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return items.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = UITableViewCell(style: .default, reuseIdentifier: "cell")
        cell.textLabel?.text = items[indexPath.row]
        cell.textLabel?.numberOfLines = 0 // 무제한 라인 수 설정
        return cell
    }
}

```


## 클릭시 글씨 접기


```swift
// 샘플 데이터
let items = [
    "첫 번째 아이템의 긴 텍스트 예시입니다. 이 텍스트는 셀의 높이가 콘텐츠의 양에 따라 동적으로 조정되어야 합니다. Auto Layout과 UITableView의 automaticDimension 기능을 사용하여 이를 구현할 수 있습니다.",
    "두 번째 아이템에도 마찬가지로 긴 텍스트를 사용합니다. 셀의 높이가 콘텐츠의 양에 따라 자동으로 조정되는 것을 확인할 수 있습니다. 이를 통해 사용자에게 더 나은 읽기 경험을 제공할 수 있습니다.",
    "세 번째 아이템에도 긴 텍스트를 적용합니다. 긴 텍스트는 사용자가 셀을 탭할 때 전체 내용을 볼 수 있도록 확장되어야 합니다. 이러한 동적 셀 높이 조정은 사용자 인터페이스의 유연성을 크게 향상시킵니다."
]
```

이번엔 모든 글이 길다고 가정해보자.  

<img width="300" alt="editingStyle예시" src="https://github.com/isGeekCode/TIL/assets/76529148/4e46509b-3d3e-4c37-9d43-dee2df6272a9">


위 이미지 처럼 모든 글의 길이가 들쭉 날쭉 하게 되면, 일관성있는 모습을 보여줄 수 가 없다.  
기본적으로 모두 1줄만 표시하고, 클릭시 길게 보여줄 수 있도록 처리해보자.  


### 각 셀의 선택 여부 저장

```swift
var expandedIndexPaths: Set<IndexPath> = [] // 확장된 셀의 IndexPath를 추적하는 세트
```

그리고 셀 클릭시 선택된 셀 값들을 Set에 추가 삭제 한다.  

```swift
func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
    tableView.deselectRow(at: indexPath, animated: true)

    if expandedIndexPaths.contains(indexPath) {
        expandedIndexPaths.remove(indexPath) // 셀이 이미 확장되었다면 축소
    } else {
        expandedIndexPaths.insert(indexPath) // 셀이 축소되었다면 확장
    }
    
    tableView.reloadRows(at: [indexPath], with: .automatic) // 해당 셀만 리로드하여 높이 변경 적용
    
    print("expandedIndexPaths:: \(expandedIndexPaths)")
}

```

### 선택된 값들을 어떻게 보여줄 것인가

    expandedIndexPaths값에 따라 textLabel의 줄 수를 1줄로 

```swift
func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    let cell = UITableViewCell(style: .default, reuseIdentifier: "cell")
    cell.textLabel?.text = items[indexPath.row]
    // 확장된 셀에 대해서는 무제한 라인 수 설정
    cell.textLabel?.numberOfLines = expandedIndexPaths.contains(indexPath) ? 0 : 1 
    return cell
}
```
