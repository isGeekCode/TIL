# TIL_220529_UILabel CodeProgramming

```swift

class MainViewController: UIViewController {

    let titleLabel: UILabel = {
       let label = UILabel()
        label.textColor = .black
        label.textAlignment = .center
        label.text = "메인화면"
        label.font = UIFont.boldSystemFont(ofSize: 70)
        return label
    }()

    // 뷰가 생성되었을때 
    override func viewDidLoad() {
        super.viewDidLoad()

        self.titleLabel.translatesAutoresizingMaskIntoConstraints = false
        self.titleLabel.centerXAnchor.constraint(equalTo: self.view.centerXAnchor).isActive = true
        self.titleLabel.centerYAnchor.constraint(equalTo: self.view.centerYAnchor).isActive = true

    }
}

```

## UILabel선언하기

### 선언과 함께 세팅까지 설정

```swift
let titleLabel: UILabel = {
   let label = UILabel()  //메모리에 올라가는 부분
    label.textColor = .black
    label.textAlignment = .center
    label.text = "메인화면"
    label.font = UIFont.boldSystemFont(ofSize: 70)
    return label
}()

//클로저 형태로 선언하기

let titleLabel = UILabel().then {
    $0.textColor = .black
    $0.textAlignment = .center
    $0.text = "메인화면"
    $0.font = UIFont.boldSystemFont(ofSize: 70)
    $0.sizeToFit()
  }

//변수 세팅먼저하고 함수로 구현하기
let nameLabel = UILabel()
let nameTextField = UITextField()
let changeButton = UIButton()

override func viewDidLoad() {
        super.viewDidLoad()
        setUpValue()
        setUpView()
    }

// 요소 내용 설정
func setLabel() {
				nameLabel.text = "Label"
        nameTextField.backgroundColor = .gray
}

// 뷰 구성요소 세팅
func setUpView() {
    view.addSubview(nameLabel)
    view.addSubview(nameTextField)
    view.addSubview(changeButton)
}

```