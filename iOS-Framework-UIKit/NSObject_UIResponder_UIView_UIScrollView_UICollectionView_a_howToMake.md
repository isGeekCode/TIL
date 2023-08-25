# NSObject_UIResponder_UIView_UIScrollView_UICollectionView : 사용법

CollectionView는 iOS에서 다양한 방식으로 데이터를 표시하는 컴포넌트로, TableView와 비슷한 역할을 한다. 하지만 TableView와는 몇 가지 중요한 차이점이 있다.

## 색인
- [CollectionView와 TableView의 차이점](#collectionview와-tableview의-차이점)
- [공통된 특징](#공통된-특징)
- [기본 사용법](#기본-사용법)
- [Cell 크기 세팅하기](#cell-크기-세팅하기)
    - [단일 셀 크기 - 상단 인스턴스 변수로 설정하는 경우](#단일-셀-크기---상단-인스턴스-변수로-설정하는-경우)
    - [단일 셀 크기 - collectionView 메서드로 설정하는 경우](#단일-셀-크기---collectionview-메서드로-설정하는-경우)
- [여러 셀 크기가 들어가는 경우](#여러-셀-크기가-들어가는-경우)
    - [item의 값에 따라 크기가 다른 경우](#item의-값에-따라-크기가-다른-경우)
    - [item 개수에 따라 셀의 크기가 다른 경우](#item-개수에-따라-셀의-크기가-다른-경우)
- [UICollectionViewCell 등록해서 재사용하기](#uicollectionviewcell-등록해서-재사용하기)
    - [여러개의 UICollectionViewCell을 사용하는 경우](#여러개의-uicollectionviewcell을-사용하는-경우)
- [UICollectionView Methods](#uicollectionview-methods)
    - [UICollectionViewDelegateFlowLayout](#uicollectionviewdelegateflowlayout)
        - [상단 인스턴스 속성으로 세팅하는 경우](#상단-인스턴스-속성으로-세팅하는-경우)
        - [Delegate 메서드로 세팅하는 경우](#delegate-메서드로-세팅하는-경우)
- [가로로 스크롤하는 콜렉션뷰 만들기](#가로로-스크롤하는-콜렉션뷰-만들기)
- [그리드 형태의 콜렉션뷰](#그리드-형태의-콜렉션뷰)
- [3 * 3 횡스크롤 그리드](#3--3-횡스크롤-그리드)
- [3 * n  종스크롤 그리드](#3--n--종스크롤-그리드)


<br><br>

- [[TOP]](#)

<br><br>

## CollectionView와 TableView의 차이점

- 다양한 레이아웃: TableView는 단일 열로 구성된 리스트를 표시하는 데 주로 사용된다. 하지만 CollectionView는 다양한 레이아웃을 가지고 있어 그리드, 스택, 플로우 레이아웃 등 다양한 형태로 데이터를 표현할 수 있다.

- 유연한 셀 디자인: TableView에서는 모든 셀이 동일한 모양을 가지지만, CollectionView는 다양한 셀 디자인을 지원한다. 각 셀은 고유한 디자인과 레이아웃을 가질 수 있으며, 데이터에 따라 동적으로 변경할 수 있다.

- 다중 열 및 섹션: TableView는 주로 단일 열을 가지는 리스트를 표시하는 데 사용되지만, CollectionView는 다중 열을 가질 수 있다. 또한, 섹션을 사용하여 데이터를 그룹화하고 여러 열로 표시할 수도 있다.

<br><br>

[[TOP]](#)

<br><br>

## 공통된 특징

- 뷰 재사용: TableView는 재사용 가능한 셀을 사용하여 효율적인 메모리 관리를 할 수 있다. CollectionView도 TableView와 동일한 방식으로 셀 재사용을 지원하여 대규모 데이터 세트의 표시와 성능을 향상시킬 수 있다.

- 커스텀 레이아웃: CollectionView는 커스텀 레이아웃을 구현할 수 있는 유연성을 제공한다. 원하는 방식으로 아이템의 위치와 크기를 지정하여 완전히 사용자 정의된 레이아웃을 만들 수 있다.

이러한 차이점들로 인해 CollectionView는 TableView보다 더 다양한 데이터 표현 방식과 유연성을 제공하며, 데이터를 시각적으로 풍부하게 표현할 수 있다. 

TableView는 단순한 리스트 표시에 적합하고, CollectionView는 더 복잡하고 다양한 데이터 표현에 유용하다.



<br><br>

[[TOP]](#)

<br><br>


# 기본 사용법

### 화면
<img width="300" alt="스크린샷 2023-08-25 오후 1 20 04" src="https://github.com/isGeekCode/TIL/assets/76529148/d2f7cd19-51b7-4d62-ad07-4452cdd7ca99">


<br><br>

[[TOP]](#)

<br><br>

### 전체코드


```swift
import UIKit

class ViewController: UIViewController {

    // 임의의 리스트 데이터
    let itemList = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7", "Item 8", "Item 9", "Item 10"]

    lazy var collectionView: UICollectionView = {
        let layout = UICollectionViewFlowLayout()
        let cv = UICollectionView(frame: .zero, collectionViewLayout: layout)
        // 콜렉션 뷰의 delegate와 dataSource 설정
        cv.delegate = self
        cv.dataSource = self
        // collectionView의 속성들 설정
        cv.backgroundColor = .lightGray
        cv.showsVerticalScrollIndicator = false
        cv.showsHorizontalScrollIndicator = false
        // 셀 등록
        cv.register(UICollectionViewCell.self, forCellWithReuseIdentifier: "Cell")
        return cv
    }()

    override func viewDidLoad() {
        super.viewDidLoad()
        setupCollectionView()
    }

    private func setupCollectionView() {

        // 콜렉션 뷰의 오토레이아웃 설정
        collectionView.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(collectionView)
        NSLayoutConstraint.activate([
            collectionView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
            collectionView.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor),
            collectionView.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor),
            collectionView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor)
        ])
    }
}

extension ViewController: UICollectionViewDelegate, UICollectionViewDataSource {
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return itemList.count
    }

    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "Cell", for: indexPath)

        // 셀의 배경색 설정
        cell.backgroundColor = .systemYellow

        // UILabel 추가하여 텍스트 설정
        let label = UILabel()
        label.text = "test"
        label.textColor = .white
        label.textAlignment = .center
        label.backgroundColor = .systemTeal
        cell.contentView.addSubview(label)

        return cell
    }
}

```



<br><br>

[[TOP]](#)

<br><br>


## Cell 크기 세팅하기

### 단일 셀 크기 - 상단 인스턴스 변수로 설정하는 경우

`UICollectionViewFlowLayout` 객체의 속성으로 설정할 수 있다. 

<br><br>

### 전체코드

```swift
class ViewController {

    lazy var collectionView: UICollectionView = {
        let layout = UICollectionViewFlowLayout()
        layout.itemSize = CGSize(width: 100, height: 100) // 셀 크기 설정
        layout.minimumInteritemSpacing = 10 // 셀 사이의 수평 간격 설정
        layout.minimumLineSpacing = 10 // 셀 사이의 수직 간격 설정
        
        let cv = UICollectionView(frame: .zero, collectionViewLayout: layout)
        // collectionView의 속성들 설정
        cv.backgroundColor = .white
        cv.showsVerticalScrollIndicator = false
        cv.showsHorizontalScrollIndicator = false
        // 셀 등록
        cv.register(UICollectionViewCell.self, forCellWithReuseIdentifier: "Cell")
        return cv
    }()
    
    
    override func viewDidLoad {
        super.viewDidLoad()
        
        // AutoLayout Codes..
    }
}

extension ViewController: UICollectionViewDelegate, UICollectionViewDataSource {
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return itemList.count
    }

    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "Cell", for: indexPath)

        // 셀의 배경색 설정
        cell.backgroundColor = .blue

        // UILabel 추가하여 텍스트 설정
        let label = UILabel()
        label.text = "test"
        label.textColor = .white
        label.textAlignment = .center
        label.backgroundColor = .blue // UILabel의 배경색 설정
        cell.contentView.addSubview(label)

        return cell
    }
}
```


<br><br>

[[TOP]](#)

<br><br>

### 단일 셀 크기 - collectionView 메서드로 설정하는 경우

UICollectionViewDelegateFlowLayout 프로토콜을 이용해 구현할 수 있다. 

<br><br>

### 전체코드

```swift
extension ViewController: UICollectionViewDelegateFlowLayout {
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
        // 단일한 셀 크기 설정
        return CGSize(width: 100, height: 100)
    }

    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, minimumInteritemSpacingForSectionAt section: Int) -> CGFloat {
        // 셀 사이의 수평 간격 설정
        return 10
    }

    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, minimumLineSpacingForSectionAt section: Int) -> CGFloat {
        // 셀 사이의 수직 간격 설정
        return 10
    }
}
```



<br><br>

[[TOP]](#)

<br><br>

## 여러 셀 크기가 들어가는 경우

### item의 값에 따라 크기가 다른 경우

  
```swift

extension ViewController: UICollectionViewDelegateFlowLayout {

    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
        // itemList의 각 항목에 따라 다른 셀 크기 설정
        let item = itemList[indexPath.item]
        if item == "Item 1" {
            return CGSize(width: 100, height: 100)
        } else if item == "Item 2" {
            return CGSize(width: 150, height: 50)
        } else {
            return CGSize(width: 100, height: 120)
        }
    }
}
```



<br><br>

[[TOP]](#)

<br><br>

### item 개수에 따라 셀의 크기가 다른 경우


```swift
extension ViewController: UICollectionViewDelegate, UICollectionViewDataSource {
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
    
        if itemList.isEmpty {
            return 1
        } else {
            return itemList.count
        }
    }
}

extension ViewController: UICollectionViewDelegateFlowLayout {
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
        if itemList.isEmpty {
            return CGSize(width: 100, height: 100)
        } else {
            return CGSize(width: 150, height: 200)
        }
    }
}
```

<br><br>

[[TOP]](#)

<br><br>

## UICollectionViewCell 등록해서 재사용하기

<br><br>

Cell을 객체화 해서 사용하는 방법이 조금더 일반적이다.  

셀은 좀더 커스텀하게 구현하기 때문이다. 

셀을 사용하기위해서는 identifier를 사용하는데 두 가지 과정을 진행해야한다. 

- 콜렉션 뷰자체에 해당 셀을 등록
- 재사용 셀에 해당 셀을 등록

<br><br>

```swift
class ViewController: UIViewController {
    var collectionView = UICollectionView()

    override func viewDidLoad() {
        super.viewDidLoad()
        // 콜렉션 뷰자체에 해당 셀을 등록
        collectionView.register(MyCell.self, forCellWithReuseIdentifier: "MyCell")
    }
}

// 재사용 셀에 해당 셀을 등록
extension ViewController: UICollectionViewDataSource {

    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
            let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "MyCell", for: indexPath) as! MyCell

}
```

<br><br>

위처럼 identifier를 하드코딩해도되지만 에러를 방지하기위해 아래처럼 UICollectionViewCell 내부에 identifier 변수를 하나 만들어서 사용하는 것이 좋다.  

<br><br>

```swift

class MyCell: UICollectionViewCell {
    static let reuseIdentifier = "MyCell"
}

class ViewController: UIViewController {
    var collectionView = UICollectionView()

    override func viewDidLoad() {
        super.viewDidLoad()
        // 콜렉션 뷰자체에 해당 셀을 등록
        collectionView.register(MyCell.self, forCellWithReuseIdentifier: MyCell.reuseIdentifier)
    }
}

// 재사용 셀에 해당 셀을 등록
extension ViewController: UICollectionViewDataSource {

    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
            let cell = collectionView.dequeueReusableCell(withReuseIdentifier: MyCell.reuseIdentifier, for: indexPath) as! MyCell

}
```

전체 코드로 보자.  

```swift
import UIKit

class MyCell: UICollectionViewCell {
    static let reuseIdentifier = "MyCell"
    
    var titleLabel: UILabel!
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        setupUI()
    }
    
    required init?(coder aDecoder: NSCoder) {
        super.init(coder: aDecoder)
        setupUI()
    }
    
    private func setupUI() {
        titleLabel = UILabel()
        titleLabel.textAlignment = .center
        titleLabel.textColor = .black
        titleLabel.translatesAutoresizingMaskIntoConstraints = false
        contentView.addSubview(titleLabel)
        
        NSLayoutConstraint.activate([
            titleLabel.centerXAnchor.constraint(equalTo: contentView.centerXAnchor),
            titleLabel.centerYAnchor.constraint(equalTo: contentView.centerYAnchor)
        ])
    }
}

class ViewController: UIViewController {
    lazy var collectionView: UICollectionView = {
        let layout = UICollectionViewFlowLayout()
        let cv = UICollectionView(frame: .zero, collectionViewLayout: layout)
        cv.backgroundColor = .white
        cv.translatesAutoresizingMaskIntoConstraints = false
        cv.register(MyCell.self, forCellWithReuseIdentifier: MyCell.reuseIdentifier)
        return cv
    }()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupCollectionView()
    }
    
    private func setupCollectionView() {
        view.addSubview(collectionView)
        
        NSLayoutConstraint.activate([
            collectionView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
            collectionView.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor),
            collectionView.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor),
            collectionView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor)
        ])
    }
}

// MARK: - UICollectionViewDataSource

extension ViewController: UICollectionViewDataSource {
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return 10
    }
    
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: MyCell.reuseIdentifier, for: indexPath) as! MyCell
        cell.titleLabel.text = "\(indexPath.item)"
        return cell
    }
}

// MARK: - UICollectionViewDelegate

extension ViewController: UICollectionViewDelegate {
    func collectionView(_ collectionView: UICollectionView, didSelectItemAt indexPath: IndexPath) {
        print("Selected item at index \(indexPath.item)")
    }
}

```


<br><br>

[[TOP]](#)

<br><br>

###  여러개의 UICollectionViewCell을 사용하는 경우

<br><br>


```swift
import UIKit


class ViewController: UIViewController, UICollectionViewDataSource, UICollectionViewDelegate {
    lazy var collectionView: UICollectionView = {
        let layout = UICollectionViewFlowLayout()
        let cv = UICollectionView(frame: .zero, collectionViewLayout: layout)
        cv.delegate = self
        cv.dataSource = self
        cv.backgroundColor = .white
        cv.translatesAutoresizingMaskIntoConstraints = false
        // 여러 개의 셀 등록
        cv.register(MyCell.self, forCellWithReuseIdentifier: MyCell.reuseIdentifier)
        cv.register(YourCell.self, forCellWithReuseIdentifier: YourCell.reuseIdentifier)
        return cv
    }()
    
    var itemList: [String] = [] // 예시 데이터
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupCollectionView()
        
        // itemList에 데이터를 추가하여 MyCell과 YourCell을 구분해보세요.
        itemList = ["Item 1", "Item 2", "Item 3"] // 아이템이 있는 경우
        // itemList = [] // 아이템이 없는 경우
    }
    
    private func setupCollectionView() {
        view.addSubview(collectionView)
        
        NSLayoutConstraint.activate([
            collectionView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
            collectionView.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor),
            collectionView.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor),
            collectionView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor)
        ])
    }
    
    // MARK: UICollectionViewDataSource
    
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return itemList.count > 0 ? itemList.count : 1
    }
    
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        if itemList.count == 0 {
            let cell = collectionView.dequeueReusableCell(withReuseIdentifier: MyCell.reuseIdentifier, for: indexPath) as! MyCell
            cell.titleLabel.text = "No Items"
            return cell
        } else {
            let cell = collectionView.dequeueReusableCell(withReuseIdentifier: YourCell.reuseIdentifier, for: indexPath) as! YourCell
            cell.titleLabel.text = itemList[indexPath.item]
            return cell
        }
    }
    
    // MARK: UICollectionViewDelegate
    
    func collectionView(_ collectionView: UICollectionView, didSelectItemAt indexPath: IndexPath) {
        if itemList.count > 0 {
            print("Selected item: \(itemList[indexPath.item])")
        }
    }
}

class MyCell: UICollectionViewCell {
    static let reuseIdentifier = "MyCell"
    
    var titleLabel: UILabel!
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        setupUI()
    }
    
    required init?(coder aDecoder: NSCoder) {
        super.init(coder: aDecoder)
        setupUI()
    }
    
    private func setupUI() {
        titleLabel = UILabel()
        titleLabel.textAlignment = .center
        titleLabel.textColor = .black
        titleLabel.translatesAutoresizingMaskIntoConstraints = false
        contentView.addSubview(titleLabel)
        
        NSLayoutConstraint.activate([
            titleLabel.centerXAnchor.constraint(equalTo: contentView.centerXAnchor),
            titleLabel.centerYAnchor.constraint(equalTo: contentView.centerYAnchor)
        ])
    }
}

class YourCell: UICollectionViewCell {
    static let reuseIdentifier = "YourCell"
    
    var titleLabel: UILabel!
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        setupUI()
    }
    
    required init?(coder aDecoder: NSCoder) {
        super.init(coder: aDecoder)
        setupUI()
    }
    
    private func setupUI() {
        titleLabel = UILabel()
        titleLabel.textAlignment = .center
        titleLabel.textColor = .blue
        titleLabel.translatesAutoresizingMaskIntoConstraints = false
        contentView.addSubview(titleLabel)
        
        NSLayoutConstraint.activate([
            titleLabel.centerXAnchor.constraint(equalTo: contentView.centerXAnchor),
            titleLabel.centerYAnchor.constraint(equalTo: contentView.centerYAnchor)
        ])
    }
}
```



<br><br>

[[TOP]](#)

<br><br>


### 전체코드 보기

<details>
  <summary><b>코드보기</b></summary>

```swift
import UIKit

class ViewController: UIViewController, UICollectionViewDataSource {
    lazy var collectionView: UICollectionView = {
        let layout = UICollectionViewFlowLayout()
        layout.scrollDirection = .horizontal
        layout.minimumLineSpacing = 20
        layout.sectionInset = UIEdgeInsets(top: 0, left: 20, bottom: 0, right: 20)
        let cv = UICollectionView(frame: .zero, collectionViewLayout: layout)
        cv.dataSource = self
        cv.backgroundColor = .white
        cv.translatesAutoresizingMaskIntoConstraints = false
        cv.register(MyCell.self, forCellWithReuseIdentifier: MyCell.reuseIdentifier)
        return cv
    }()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupCollectionView()
    }
    
    private func setupCollectionView() {
        view.addSubview(collectionView)
        
        NSLayoutConstraint.activate([
            collectionView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
            collectionView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            collectionView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
            collectionView.heightAnchor.constraint(equalToConstant: 100)
        ])
    }
    
    // MARK: UICollectionViewDataSource
    
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return 10
    }
    
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: MyCell.reuseIdentifier, for: indexPath) as! MyCell
        cell.titleLabel.text = "\(indexPath.item)"
        
        // 셀 배경색 설정
        cell.backgroundColor = indexPath.item % 2 == 0 ? .lightGray : .gray
        
        return cell
    }
}

class MyCell: UICollectionViewCell {
    static let reuseIdentifier = "MyCell"
    
    var titleLabel: UILabel!
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        setupUI()
    }
    
    required init?(coder aDecoder: NSCoder) {
        super.init(coder: aDecoder)
        setupUI()
    }
    
    private func setupUI() {
        titleLabel = UILabel()
        titleLabel.textAlignment = .center
        titleLabel.textColor = .black
        titleLabel.translatesAutoresizingMaskIntoConstraints = false
        contentView.addSubview(titleLabel)
        
        NSLayoutConstraint.activate([
            titleLabel.centerXAnchor.constraint(equalTo: contentView.centerXAnchor),
            titleLabel.centerYAnchor.constraint(equalTo: contentView.centerYAnchor)
        ])
    }
}
```

</details>



<br><br>

[[TOP]](#)

<br><br>

# UICollectionView Methods


## UICollectionViewDelegateFlowLayout
다양한 레이아웃 설정을 커스터마이즈할 수 있는 메서드를 제공한다. 

- collectionView(_:layout:sizeForItemAt:)
    - 각 셀의 크기를 설정한다.
- collectionView(_:layout:insetForSectionAt:)
    - 섹션의 inset을 설정한다.
- collectionView(_:layout:minimumLineSpacingForSectionAt:)
    - 셀 사이의 세로 간격을 설정한다.
- collectionView(_:layout:minimumInteritemSpacingForSectionAt:)
    - 셀 사이의 가로 간격을 설정한다.
- collectionView(_:layout:referenceSizeForHeaderInSection:)
    - 섹션 헤더의 크기를 설정한다.
- collectionView(_:layout:referenceSizeForFooterInSection:)
    - 섹션 푸터의 크기를 설정한다.

또한 이 메서드들을 사용하지않아도 상단 인스턴스 변수를 설정할 때,  
이런 형태로 세팅이 가능하다.   

<br><br>

### 상단 인스턴스 속성으로 세팅하는 경우


```swift
lazy var collectionView: UICollectionView = {
    let layout = UICollectionViewFlowLayout()
    layout.scrollDirection = .horizontal
    layout.minimumLineSpacing = 20 // 세로 간격
    layout.minimumInteritemSpacing = 10 // 가로 간격
    layout.itemSize = CGSize(width: 100, height: 100) // 셀 크기
    layout.sectionInset = UIEdgeInsets(top: 10, left: 20, bottom: 10, right: 20) // 섹션 inset
    layout.headerReferenceSize = CGSize(width: 0, height: 50) // 헤더 크기
    layout.footerReferenceSize = CGSize(width: 0, height: 30) // 푸터 크기
    
    let cv = UICollectionView(frame: .zero, collectionViewLayout: layout)
    cv.dataSource = self
    cv.delegate = self // UICollectionViewDelegateFlowLayout 설정
    cv.backgroundColor = .white
    cv.translatesAutoresizingMaskIntoConstraints = false
    cv.register(MyCell.self, forCellWithReuseIdentifier: MyCell.reuseIdentifier)
    return cv
}()

```



<br><br>

[[TOP]](#)

<br><br>



### Delegate 메서드로 세팅하는 경우


<br><br>

<details>
  <summary><b>코드보기</b></summary>

```swift
extension ViewController: UICollectionViewDelegateFlowLayout {
    // MARK: UICollectionViewDelegateFlowLayout

    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
        return CGSize(width: 100, height: 100) // 셀 크기 설정
    }

    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, insetForSectionAt section: Int) -> UIEdgeInsets {
        return UIEdgeInsets(top: 10, left: 20, bottom: 10, right: 20) // 섹션 inset 설정
    }

    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, minimumLineSpacingForSectionAt section: Int) -> CGFloat {
        return 20 // 세로 간격 설정
    }

    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, minimumInteritemSpacingForSectionAt section: Int) -> CGFloat {
        return 10 // 가로 간격 설정
    }

    // MARK: UICollectionViewDelegateFlowLayout - Header & Footer

    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, referenceSizeForHeaderInSection section: Int) -> CGSize {
        return CGSize(width: collectionView.bounds.width, height: 50) // 헤더 높이 설정
    }

    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, referenceSizeForFooterInSection section: Int) -> CGSize {
        return CGSize(width: collectionView.bounds.width, height: 30) // 푸터 높이 설정
    }

    // MARK: Supplementary Views - Header & Footer
    // 이건 선택 사항
    func collectionView(_ collectionView: UICollectionView, viewForSupplementaryElementOfKind kind: String, at indexPath: IndexPath) -> UICollectionReusableView {
        if kind == UICollectionView.elementKindSectionHeader {
            let headerView = collectionView.dequeueReusableSupplementaryView(ofKind: kind, withReuseIdentifier: "Header", for: indexPath)
            headerView.backgroundColor = .lightGray // 헤더 배경색 설정
            return headerView
        } else if kind == UICollectionView.elementKindSectionFooter {
            let footerView = collectionView.dequeueReusableSupplementaryView(ofKind: kind, withReuseIdentifier: "Footer", for: indexPath)
            footerView.backgroundColor = .darkGray // 푸터 배경색 설정
            return footerView
        }
        return UICollectionReusableView()
    }
}
```

</details>


<br><br>

[[TOP]](#)

<br><br>

# 가로로 스크롤하는 콜렉션뷰 만들기

UICollectionViewFlowLayout을 통해 설정할 수 있다. 
```swift
    lazy var collectionView: UICollectionView = {
        let layout = UICollectionViewFlowLayout()
        // 스크롤 방향설정
        layout.scrollDirection = .horizontal
        layout.minimumLineSpacing = 20
        layout.sectionInset = UIEdgeInsets(top: 0, left: 20, bottom: 0, right: 20)
        let cv = UICollectionView(frame: .zero, collectionViewLayout: layout)
        cv.dataSource = self
        cv.backgroundColor = .white
        cv.translatesAutoresizingMaskIntoConstraints = false
        cv.register(MyCell.self, forCellWithReuseIdentifier: MyCell.reuseIdentifier)
        return cv
    }()

```


<br><br>

[[TOP]](#)

<br><br>

# 그리드 형태의 콜렉션뷰

그리드 스타일을 만들 때에는 고려해야할 요소들이 있다.
- 콜렉션뷰 자체의 가로 세로 길이
- 셀 가로 세로길이

## 3 * 3 횡스크롤 그리드

### 동작화면
<img width="300" alt="ezgif-2-1df36bf8e6" src="https://github.com/isGeekCode/TIL/assets/76529148/a7b0c47e-336e-4ab7-aed6-8fde6cef4a22">


<br><br>

[[TOP]](#)

<br><br>

### 전체코드

<details>
  <summary><b>코드보기</b></summary>

```swift
import UIKit

class ViewController: UIViewController, UICollectionViewDataSource, UICollectionViewDelegateFlowLayout {
    
    let collectionView: UICollectionView = {
        let layout = UICollectionViewFlowLayout()
        layout.scrollDirection = .horizontal
        let collectionView = UICollectionView(frame: .zero, collectionViewLayout: layout)
        collectionView.translatesAutoresizingMaskIntoConstraints = false
        collectionView.backgroundColor = .systemYellow // 배경색을 systemYellow로 변경
        return collectionView
    }()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        collectionView.dataSource = self
        collectionView.delegate = self
        
        collectionView.register(Cell.self, forCellWithReuseIdentifier: "Cell")
        
        view.addSubview(collectionView)
        
        NSLayoutConstraint.activate([
            collectionView.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor),
            collectionView.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor),
            collectionView.heightAnchor.constraint(equalToConstant: 300),
            collectionView.centerYAnchor.constraint(equalTo: view.centerYAnchor)
        ])
    }
    
    func numberOfSections(in collectionView: UICollectionView) -> Int {
        return 1
    }
    
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return 21 // 전체 갯수를 21로 변경
    }
    
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "Cell", for: indexPath) as! Cell
        cell.configure(number: indexPath.item + 1)
        return cell
    }
    
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
        return CGSize(width: 90, height: 90) // 셀 크기를 가로 90, 세로 90으로 변경
    }
}

class Cell: UICollectionViewCell {
    let label: UILabel = {
        let label = UILabel()
        label.textAlignment = .center
        label.font = UIFont.systemFont(ofSize: 16)
        label.translatesAutoresizingMaskIntoConstraints = false
        return label
    }()
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        
        contentView.backgroundColor = .lightGray // 색상을 lightGray로 변경
        
        contentView.addSubview(label)
        
        NSLayoutConstraint.activate([
            label.topAnchor.constraint(equalTo: contentView.topAnchor),
            label.leadingAnchor.constraint(equalTo: contentView.leadingAnchor),
            label.trailingAnchor.constraint(equalTo: contentView.trailingAnchor),
            label.bottomAnchor.constraint(equalTo: contentView.bottomAnchor)
        ])
    }
    
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    func configure(number: Int) {
        label.text = "\(number)"
    }
}

```

</details>


<br><br>

[[TOP]](#)

<br><br>

## 3 * n  종스크롤 그리드

인스타그램처럼 아래로 내려간다고 생각하면 된다.  

셀의 크기를 가로로 3개씩 배치하고 세로로 n개가 되도록 설정하는 

`3 * n` 형태이다.  

 즉, 한 행에 3개의 셀이 있고 그 아래로 n행이 형성된다.  


### 동작화면

<img width="300" alt="ezgif-2-759074f266" src="https://github.com/isGeekCode/TIL/assets/76529148/388e40e0-274a-4892-8c4e-3c4b509bceee">



<br><br>

[[TOP]](#)

<br><br>

### 전체코드

<details>
  <summary><b>코드보기</b></summary>

```swift
import UIKit

class ViewController: UIViewController, UICollectionViewDataSource, UICollectionViewDelegateFlowLayout {
    
    let collectionView: UICollectionView = {
        let layout = UICollectionViewFlowLayout()
        layout.scrollDirection = .vertical
        let collectionView = UICollectionView(frame: .zero, collectionViewLayout: layout)
        collectionView.translatesAutoresizingMaskIntoConstraints = false
        collectionView.backgroundColor = .systemYellow // 배경색을 systemYellow로 변경
        return collectionView
    }()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        collectionView.dataSource = self
        collectionView.delegate = self
        
        collectionView.register(Cell.self, forCellWithReuseIdentifier: "Cell")
        
        view.addSubview(collectionView)
        
        NSLayoutConstraint.activate([
            collectionView.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor),
            collectionView.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor),
            collectionView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
            collectionView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor),
        ])
    }
    
    func numberOfSections(in collectionView: UICollectionView) -> Int {
        return 1
    }
    
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return 21 // 전체 갯수를 21로 변경
    }
    
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "Cell", for: indexPath) as! Cell
        cell.configure(number: indexPath.item + 1)
        return cell
    }
    
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
        let screenWidth = UIScreen.main.bounds.width
        let cellWidth = (screenWidth - 30) / 3
        return CGSize(width: cellWidth, height: cellWidth) // 가로 크기에서 30을 빼고 3으로 나눈 값으로 설정
    }
    
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, insetForSectionAt section: Int) -> UIEdgeInsets {
        return UIEdgeInsets(top: 0, left: 0, bottom: 0, right: 0)
    }
}

class Cell: UICollectionViewCell {
    let label: UILabel = {
        let label = UILabel()
        label.textAlignment = .center
        label.font = UIFont.systemFont(ofSize: 16)
        label.translatesAutoresizingMaskIntoConstraints = false
        return label
    }()
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        
        contentView.backgroundColor = .lightGray // 색상을 lightGray로 변경
        
        contentView.addSubview(label)
        
        NSLayoutConstraint.activate([
            label.topAnchor.constraint(equalTo: contentView.topAnchor),
            label.leadingAnchor.constraint(equalTo: contentView.leadingAnchor),
            label.trailingAnchor.constraint(equalTo: contentView.trailingAnchor),
            label.bottomAnchor.constraint(equalTo: contentView.bottomAnchor)
        ])
    }
    
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    func configure(number: Int) {
        label.text = "\(number)"
    }
}

```

</details>


<br><br>

[[TOP]](#)

<br><br>

## History
- 230701 : 초안작성
- 230825 : Cell 크기별 코드 작성
- 230825 : 세로형태 그리드 스타일 생성
- 230825 : 가로형태 그리드 스타일 생성
