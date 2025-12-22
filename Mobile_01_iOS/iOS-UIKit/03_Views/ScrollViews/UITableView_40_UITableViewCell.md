# [Apple Document] UITableViewCell

UITableViewCell객체는 단일 테이블의 콘텐츠를 관리하는 UIView다. 
테이블뷰셀을 구현할 때는 주로 커스텀 콘텐츠를 구성하겠지만, 아래와 같은 테이블뷰 관련 동작을 지원하고 있다.

- 셀 선택시 또는 하이라이트 컬러를 적용할 수 있다.
- 세부정보 혹은 disclosure control같은 악세서리 뷰를 지원한다.
- editing mode 즉, 편집모드로 전환시킬 수 있다.
- 셀의 시각적 계층구조를 구성하기 위해서 컨텐츠에 들여쓰기할 수 있다.

보통 앱의 컨텐츠는 셀이 갖고있는 bounds를 가득 차지하지만, 다른 컨텐츠를 위한 공간을 만들기 위해 해당 공간을 조절할 수가 있다.

셀에서 편집모드로 전환될 때, 컨텐츠 영역의 leading부분에 delete control을 추가한다.
또한 테이블뷰 셀 간의 순서를 재정렬 할 수 있는 reorder control을 선택적으로 Accessory View / Reordered control 영역에 배치할 수 있다.


모든 테이블 뷰는 컨텐츠를 표시하기위한 셀 타입이 하나라도 있어야한다. 한 테이블뷰에는 다양한 유형의 컨텐츠를 표시하기 위한 여러 셀 타입이 있을 수 있다. tableview의 dataSource 개체는 셀이 화면에 보여지기 직전에 셀 생성 및 구성을 처리한다. 

<br><br>

## 셀의 컨텐츠 구성

스토리보드 파일에서 (혹은 코드로) cell의 컨텐츠(내용)와 레이아웃을 구현한다.
테이블은 기본적으로 하나의 셀 타입을 갖고 있지만, 필요에 따라 테이블의  프로토타입 셀 속성값을 변화시켜 추가할 수 있다.  
셀의 컨텐츠를 구성하는 것 말고도 아래 속성들을 구현해야한다.

- Identifier : 이 ID를 사용해서 셀을 만든다.
- Style : 미리 구현되어있는 표준 타입 말고도 커스텀 셀을 정의할 수 있다.
- Class : UITableViewCell 클래스를 상속하여 커스텀 동작을 구현할 수 있다.

<br><br>

## Cell의 구조

<img width="500" alt="content-only_dark@2x" src="https://github.com/isGeekCode/TIL/assets/76529148/961db50d-9bee-428f-b58c-7ce976aa5e27">

셀의 구조는 아래와 같은 경우로 나뉘어진다. 
- Content만 있는경우
- Accessory view가 함께 있는 경우
- Edit mode(편집모드)


<br><br>

또한 content에는 세 가지 프로퍼티가 정의되어있다.

<img width="700" alt="63b0c95b-bf2f-4798-9cca-8a5e77631679" src="https://github.com/isGeekCode/TIL/assets/76529148/09486e78-011e-4029-9a8e-55fa6b74c6ee">

<br>


- textLabel: UILabel 타입으로 주제목이 들어가는 레이블
- detailTextLabel: UILabel 타입으로 추가적인 세부사항이 들어가는 부제목 레이블
- imageView: UIImageView 타입의 이미지를 표시하기 위한 이미지뷰

아래 여러가지 사례를 보며 살펴보자.  

<img width="300" alt="스크린샷 2023-11-17 오전 9 49 14" src="https://github.com/isGeekCode/TIL/assets/76529148/7f142b9c-9686-46ea-8096-56acc8df9276">

위 그림은 content안에 textLabel에만 값이 선언된 경우이다. 

이제 imageView 에 이미지가 세팅되면 아래와 같이 표시된다.

<img width="300" alt="스크린샷 2023-11-17 오전 9 53 39" src="https://github.com/isGeekCode/TIL/assets/76529148/0344332f-3531-4d7c-8be8-81ac4526c006">

이렇게 textLabel이 우측으로 밀려난다. 

여기에 AccessoryType을 추가해보자.

`cell.accessoryType = .disclosureIndicator`로 선언하면 아래와 같이 표시할 수 있다.

<img width="300" alt="스크린샷 2023-11-17 오전 10 31 25" src="https://github.com/isGeekCode/TIL/assets/76529148/842d4ef8-c0d8-4e72-9fa0-6d5405d66de5">

UITableViewCell의 Style이 default 인 경우, 위 경우들을 표시할 수 있다.

<br><br>

  
이제 textLabel아래에 subtitle을 표시하려면 cell의 style을 .subtitle 로 세팅해야 선언이 가능하다.

subtitle이 적용된 화면을 보자.

마찬가지로 disclosure는 설정을 해두었다.  

<img width="300" alt="스크린샷 2023-11-17 오전 10 27 43" src="https://github.com/isGeekCode/TIL/assets/76529148/053569dd-ccce-4406-b75c-2bf6563c5b4d">

<img width="300" alt="스크린샷 2023-11-17 오전 10 27 04" src="https://github.com/isGeekCode/TIL/assets/76529148/3179be94-45a7-494d-9995-279d4861adbf">


<br><br>

아이폰의 설정앱을 살펴보면 다양한 형태의 셀을 살펴보자. 

<img width="300" alt="스크린샷 2023-11-17 오전 9 59 56" src="https://github.com/isGeekCode/TIL/assets/76529148/0acf74a3-5f5e-4e78-87f0-9910a7c58507">
  
<img width="300" alt="스크린샷 2023-11-17 오전 9 58 36" src="https://github.com/isGeekCode/TIL/assets/76529148/58b073f9-4d1d-4f93-b8cc-bbae06e3b81b">
  
<img width="300" alt="스크린샷 2023-11-17 오전 9 56 47" src="https://github.com/isGeekCode/TIL/assets/76529148/461e037f-4800-4f20-ba22-213cc79857dd">


<br><br>

또 편집모드로 진입하는 모습은 언어 설정에서 볼 수 있다.  

<img width="300" alt="스크린샷 2023-11-17 오전 9 56 47" src="https://github.com/isGeekCode/TIL/assets/76529148/ac05ed1e-1d8c-4cb8-b4fc-756e40ca3699">

<br><br>

### style을 설정하는 것에 대하여
style을 설정하는 것은 설정페이지처럼 유동적인 데이터가 아닌 고정된 값을 영구적으로 보여주는 화면에서만 사용하는 것이 바람직하다고 생각한다.  

여러개의 row에 여러 데이터를 표시하려면 스크롤을 해야하는데 많은 데이터를 표시하기위해 테이블뷰에서는 UITableViewCell객체를 계속 생성해야만한다.  
그러면 과도한 비용을 지출해야하기 때문에 이때에는 style을 사용하지않고 커스텀셀의 ID값을 등록하여 재사용하는 방식으로 사용해야한다.  


<br><br>

## 셀 초기화

UITableViewCell의 init메서드는 아래와 같다.  

```swift
// 외부에서 UITableViewCell init
let cell = UITableViewCell(style: .default, reuseIdentifier: "Cell") 

// UITableViewCell 내부 init메서드
override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) { }
```

여기에 인자로들어가는 style은 UITableViewCell.CellStyle  enum 타입으로 아래와 같이 선언되어있다.

```swift
extension UITableViewCell {
    
    public enum CellStyle : Int, @unchecked Sendable {
        case default = 0
        case value1 = 1
        case value2 = 2
        case subtitle = 3
    }
```

이 스타일에 따른  UI는 앞선 설명과 아래 이미지를 참고하자.

<img width="500" alt="ios_uitable_cell_styles" src="https://github.com/isGeekCode/TIL/assets/76529148/88807f76-b39b-406b-b548-ff2e23bc14cc">

거듭 강조하지만 이 style을 지정하는 메서드는 고정된 데이터를 보여줄때 사용하자.  
유동적인 데이터는 아래 셀 재사용을 참고하자.  

<br><br>

## 셀 재사용

tableView는 UIScrollView를 상속받고 있기 때문에 많은 양의 데이터를 스크롤을 통해 보여줄 수 있다.  
하지만 각 셀을 끊임없이 생성하여 메모리를 낭비하면 앱의 메모리가 쌓여서 죽지않을까? 이를 방지하기위해  이미 생성한 셀을 재사용 할 수 가 있다. 그러면 앱의 메모리에 대한 비용을 줄일 수가 있다.  

셀을 재사용하기 위해선 아래와 같은 과정이 필요하다.

- 생성한 tableView에 cell의 identifier를 등록
- tableView의 delegate메서드인 cellForRowAt에서 tableView의 dequeueReusableCell 메서드로 재사용할 cell의 identifier를 등록


### 1. 셀 등록


```swift
// 기본 클래스
tableView.register(UITableViewCell.self, forCellReuseIdentifier: "Cell")

// 커스텀 클래스
tableView.register(MyTableViewCell.self, forCellReuseIdentifier: "Cell")

// nib파일을 사용하는 경우 
tableView.register(UINib(nibName: "CustomTableViewCell", bundle: nil), forCellReuseIdentifier: "Cell")
```

<br><br>



만약 커스텀 셀 내부에 ID값을 변수로 생성했다면 아래와 같이 사용도 가능하다.

```swift
tableView.register(MyTableViewCell.self, forCellReuseIdentifier: MyTableViewCell.reuseIdentifier)
tableView.register(UINib(nibName: "CustomTableViewCell", bundle: nil), forCellReuseIdentifier: MyTableViewCell.reuseIdentifier)

class MyTableViewCell : UITableViewCell { 

    static let reuseIdentifier = "MyTableViewCell"
}
```

<br><br>

### 2. 셀 재사용 선언

재사용을 위해서는 tableView의 `dequeueReusableCell(withIdentifier:for:)`메서드를 사용한다.  
이때 메서드명을 보면 dequeue / reusable Cell 을 볼 수 있다. dequeue란 큐로부터 가져오는 것을 말한다.  
Identifier에는 ID가 들어가고 for에는 IndexPath가 들어간다.  

tableView는 Queue 형식으로 셀을 관리한다. 즉, 선입선출 형식으로 셀을 생성하고 그걸 dequeue하여( 큐에서 가져와서) 다시 재사용 하는 것이다.  

그래서 특정 ID의 셀을 IndexPath에 재사용하는 것을 의미한다.   


```swift
func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {

        // 기본 클래스
        let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath)
        
        // 커스텀 클래스의 ID값을 사용하는 경우
        let cell = tableView.dequeueReusableCell(withIdentifier: MyTableViewCell.reuseIdentifier, for: indexPath)
        
}
```


## UI 구현부 메서드

### Nib을 사용하는 경우

`awakeFromNib()`에서드에서 로직을 추가할 수 있다.    
없어도 문제는 되지않는다.  


```swift
class CustomTableViewCell: UITableViewCell {

    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
    }
}
```

<br><br>


### 코드로만 구현하는 경우

`awakeFromNib()`에서드가 있어도 실행되지않는다. 

```swift
class CustomTableViewCell: UITableViewCell {

    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        // Initialization code
    }
    
    required init?(coder: NSCoder) {
        super.init(coder: coder)
    }
}
```

<br><br><br>



###  전체코드


```swift
import UIKit

class ViewController: UIViewController {

    let data = ["Sam", "John", "Kim", "Bang"]
    
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
        return data.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell =  tableView.dequeueReusableCell(withIdentifier: CustomTableViewCell.identifier, for: indexPath) as! CustomTableViewCell

        cell.textLabel?.text = data[indexPath.row]
        return cell
    }
}

class CustomTableViewCell: UITableViewCell {

    static let identifier = "test"
    
    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        print(#function)
    }
    
    required init?(coder: NSCoder) {
        super.init(coder: coder)
    }
}

```


<br><br><br>


## 재사용으로 인한 사이드이펙트


일반적으로 UI가 변경되지않는 앱들은 문제가 생기지않겠지만,

셀을 클릭할 때마다, 레이아웃이 변경되는 UI를 가진 테이블뷰라면 재사용에 대해 추가 작업을 진행해야한다.  


<br><br>


### Cell 내부에서 재사용 초기화하기

왜냐하면 이미 UI에 의해 레이아웃이 변경된 셀임에도, 스크롤을 하면 아직 변경되지 않아야할 셀이 변경되어있기도, 혹은 반대의 경우가 생기기 떄문이다.  짧게 말하면 이상하다.  

이런 경우, 해당 셀의 변수 등은  초기화 되어있지만 UI만 재사용 되어있다는 것을 기억하자. 셀의 state는 초기화 되어있다. 

다만 UI를 초기화 시켜주어야하기 때문에 아래와 같이 선언하다. 


```swift

class MyTableViewCell: UITableViewCell {

    /// 셀 재사용시 호출되는 메서드
    override func prepareForReuse() {
        super.prepareForReuse()
        // 재사용시 초기화
        updateUIForSelection(isActive: false) 
    }
}
```

위 처럼 셀이 재사용될 때에는 prepareForeReuse라는 메서드가 실행된다.  이 때, UI를 어떻게 초기화할 건지 메서드를 구현하여 원하는 UI를 유지시킬 수 있다. 사실 유지시킨다기보단 갱신이라고 보는게 맞다.  

 
<br><br>


### cellForRowAt에서 재사용 초기화하기
위 방법보다 더 자주 사용가능한 방법으로, 조건문으로 분기처리하여 초기화메서드를 넣어주는 것이다.

```swift

  func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "cell", for: indexPath)
      
        cell.thumbnailImageView?.image = UIImage(systemName: "heart.fill")
            
        if indexPath.row == 3 {
            cell.thumbnailImageView.backgroundColor = .red
        } else {
            cell.thumbnailImageView.backgroundColor = .clear
        }
        
        return cell
  }

```

특별한 로직이 없는 경우, 이렇게만 넣어줘도 재사용으로 인한 사이드이펙트 처리가 가능하다.

<br><br>

## History
- 230125: contentView에 대해서만 다루어서 최초생성
- 231117: contentView에서 내용 수정
- 231121: cellForRowAt에서 재사용 초기화하기 추가
