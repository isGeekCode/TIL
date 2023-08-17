# Caculator : MVC -> MVP -> MVVM


MVC의 개념을 잘 다져보자.  

원하는 앱의 동작을 보자.

### 실행화면

<img width="300" alt="ezgif-3-2f25342fcf" src="https://github.com/isGeekCode/TIL/assets/76529148/028d57af-2711-489c-bd4f-1467f9e0ab38">

### 동작설명

- 첫번째 텍스트필드에 입력한 특수문자를 입력한다.
- 두번째 텍스트필드에는 숫자특수문자... 조합으로 입력한다.
- 두번째 텍스트필드에 들어온 값에서 첫번째 텍스트필드에서 입력받은 특수문자로 쪼갠다.
- 쪼갠 모든 숫자를 더한 값을 하단 라벨에 반영한다.  

아래는 단순하게 UI만 구현한 코드이다.   

ViewController에 커스텀뷰를 구현하였다.  

```swift
// MARK: View부분
class CalculatorView: UIView {

    private lazy var tokenTextField: UITextField = {
        let field = UITextField()
        field.font = .preferredFont(forTextStyle: .body)
        field.borderStyle = .roundedRect
        field.backgroundColor = .secondarySystemBackground
        field.addTarget(self, action: #selector(didChangeTokenText), for: .editingChanged)
        field.setContentHuggingPriority(.defaultHigh, for: .vertical)
        return field
    }()
    
    private lazy var inputTextField: UITextField = {
        let field = UITextField()
        field.font = .preferredFont(forTextStyle: .headline)
        field.borderStyle = .roundedRect
        field.backgroundColor = .secondarySystemBackground
        field.addTarget(self, action: #selector(didChangeInputText), for: .editingChanged)
        field.setContentHuggingPriority(.required, for: .vertical)
        return field
    }()
    
    private lazy var resultLabel: UILabel = {
        let label = UILabel()
        label.textAlignment = .center
        label.font = .preferredFont(forTextStyle: .largeTitle)
        return label
    }()
    
    private lazy var stackView: UIStackView = {
        let vStack = UIStackView(arrangedSubviews: [tokenTextField, inputTextField, resultLabel])
        vStack.translatesAutoresizingMaskIntoConstraints = false
        vStack.axis = .vertical
        vStack.spacing = 16
        vStack.alignment = .fill
        vStack.distribution = .fill
        return vStack
    }()
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        
        addSubview(stackView)
        NSLayoutConstraint.activate([
            stackView.topAnchor.constraint(equalTo: safeAreaLayoutGuide.topAnchor),
            stackView.bottomAnchor.constraint(equalTo: safeAreaLayoutGuide.bottomAnchor),
            stackView.leadingAnchor.constraint(equalTo: safeAreaLayoutGuide.leadingAnchor),
            stackView.trailingAnchor.constraint(equalTo: safeAreaLayoutGuide.trailingAnchor),
        ])
    }
    
    required init?(coder: NSCoder) {
        super.init(coder: coder)
    }
}

extension CalculatorView {
    @objc private func didChangeTokenText(_ field: UITextField) { }
    
    @objc private func didChangeInputText(_ field: UITextField) { }
}

// MARK: ViewController부분
class ViewController: UIViewController {
    
    let calculatorView: CalculatorView = CalculatorView(frame: .zero)
    
    override func viewDidLoad() {
        super.viewDidLoad()

        calculatorView.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(calculatorView)

        NSLayoutConstraint.activate([
            calculatorView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
            calculatorView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor),
            calculatorView.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor),
            calculatorView.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor),
        ])
    }
}
```

MVC 패턴을 구현하기 위해서 MVC에 대해 생각해보자.  

<br><br>

## MVC

Model, View, Controller로 구현하는 것이다.  

이 세가지 중 중심에는 Controller가 있다.  

Controller가 사이에서 이들을 중재한다.  

<br><br>

## MVC - 사용자 인터랙션 : View -> Controller

사용자가 앱으로 input한다면 그 동작은 Controller로 연결된다. 

그래서 이제 textfield가 입력되면 반영되도록 처리해보자.

### Delegate패턴

View에서 Controller(ViewController)로 사용자 인풋을 알려주기위해 Delegate패턴을 사용해보자.

- CalculatorViewDelegate 
    - 프로토콜 생성
    - CalculatorView의 delegate를 ViewController가 self로 선언
    - 이제 ViewController는 delegate로 취급된다.
    - ViewController는 대리자가 되기 위해 프로토콜을 충족시켰다.
        - didChangeTokenText(_:token:)
        - didChangeInputText(_:input:)
    - CalculatorView에서 원하는 시점에 delegate의 프로토콜메서드르 실행가능해졌다.

```swift
// MARK: - View
// 프로토콜 생성
protocol CalculatorViewDelegate: AnyObject {
    func didChangeTokenText(_ calculatorView: CalculatorView, token: String)
    func didChangeInputText(_ calculatorView: CalculatorView, input: String)
}

class CalculatorView: UIView {
    // 대리자 변수 선언
    weak var delegate: CalculatorViewDelegate?
    
    // Other UIComponents...
}

extension CalculatorView {
    // 원하는 시점에 delegate의 프로토콜 메서드 호출
    @objc private func didChangeTokenText(_ field: UITextField) {
        delegate?.didChangeTokenText(self,
                                     token: field.text ?? " ")
    }
    
    // 원하는 시점에 delegate의 프로토콜 메서드 호출
    @objc private func didChangeInputText(_ field: UITextField) {
        delegate?.didChangeInputText(self,
                                     input: field.text ?? "")
    }
}


// MARK: - Controller
class ViewController: UIViewController {
    
    let calculatorView: CalculatorView = CalculatorView(frame: .zero)
    private var token: String = ""
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // View's AutoLayout Logic... 
        
        // CalculatorViewDelegate 프로토콜의 대리자를 자신으로 선언
        calculatorView.delegate = self
    }
}

// CalculatorViewDelegate 프로토콜 채택
extension ViewController : CalculatorViewDelegate {

    // 프로토콜 메서드를 구현 : 원하는 동작을 구현한다
    func didChangeTokenText(_ calculatorView: CalculatorView, token: String) { 
        self.token = token
    }

    // 프로토콜 메서드를 구현 : 원하는 동작을 구현한다
    func didChangeInputText(_ calculatorView: CalculatorView, input: String) { }
}
```

이제 ViewController의 프로토콜 메서드에서는 View로부터 전달받은 String을 받을 수 있게 됐다.

받은 정보는 Controller자체의 변수에 저장했다.

### 비즈니스 로직

바로 다시 View로 UI를 업데이트 하는 경우도 있지만,  

여기서는 비즈니스 로직이 필요하다. 

delegate 메서드에 비즈니스 로직을 구현하자. 

```swift
extension ViewController : CalculatorViewDelegate {

    // 프로토콜 메서드를 구현 : 원하는 동작을 구현한다
    func didChangeTokenText(_ calculatorView: CalculatorView, token: String) {
        self.token = token
    }
    
    // 프로토콜 메서드를 구현 : 원하는 동작을 구현한다
    func didChangeInputText(_ calculatorView: CalculatorView, input: String) {
    
        // MARK: - 비즈니스 로직
        let sum: Int = input.components(separatedBy:CharacterSet(charactersIn: token))
            .compactMap { Int($0) }
            .reduce(0, +)
    }
}

```


## MVC - UI Update : Controller -> View

이제 Controller는 다시 View에 반영시켜야한다.   
혹은 처리한 값을 View에 반영시킨다.  

Controller는 View를 알고 있다.
> ViewController내부에 calculatorView를 생성했다.

때문에 View의 메서드를 실행시킬 수 있다.

- View내부에 메서드를 생성하여 프로퍼티를 변경시킬수 있도록 만든다.
```
// MARK: View에 반영시키는 메서드
func setResultText(_ result: String) {
    resultLabel.text = result
}
```

이제 Controller에서 원하는 순간에 View에 접근해서 View를 update하는 메서드를 호출한다. 


```swift

// MARK: - View

class CalculatorView: UIView {
    weak var delegate: CalculatorViewDelegate?
    // Other Properties...
}

extension CalculatorView {

    // MARK: 유저 Input : View -> Controller
    @objc private func didChangeTokenText(_ field: UITextField) {
        delegate?.didChangeTokenText(self,
                                     token: field.text ?? " ")
    }
    // MARK: 유저 Input : View -> Controller
    @objc private func didChangeInputText(_ field: UITextField) {
        delegate?.didChangeInputText(self,
                                     input: field.text ?? "")
    }
    
    // MARK: View에 접근하여 update할 수 있도록 메서드 구현
    func setResultText(_ result: String) {
        resultLabel.text = result
    }
}


// MARK: - Controller
class ViewController: UIViewController {
    
    let calculatorView: CalculatorView = CalculatorView(frame: .zero)
    private var token: String = ""
}

extension ViewController : CalculatorViewDelegate {
    
    // MARK: 유저 Input : View -> Controller
    func didChangeTokenText(_ calculatorView: CalculatorView, token: String) {
        self.token = token
    }
    // MARK: 유저 Input : View -> Controller
    func didChangeInputText(_ calculatorView: CalculatorView, input: String) {
        
        // MARK: - 비즈니스 로직
        let sum: Int = input.components(separatedBy:CharacterSet(charactersIn: token))
            .compactMap { Int($0) }
            .reduce(0, +)
        
        // MARK: - View Update : Controller -> View
        calculatorView.setResultText(String(describing: sum))
    }
}

```

여기까지 하면 ViewController와 CalculatorView 만으로 완성할 수 있다. 

### 전체코드
```swift
// MARK: - VIEW

// MARK: 유저 Input : View -> Controller
protocol CalculatorViewDelegate: AnyObject {
    func didChangeTokenText(_ calculatorView: CalculatorView, token: String)
    func didChangeInputText(_ calculatorView: CalculatorView, input: String)
}

class CalculatorView: UIView {
    
    // MARK: 유저 Input : View -> Controller
    weak var delegate: CalculatorViewDelegate?
    
    private lazy var tokenTextField: UITextField = {
        let field = UITextField()
        field.font = .preferredFont(forTextStyle: .body)
        field.borderStyle = .roundedRect
        field.backgroundColor = .secondarySystemBackground
        field.addTarget(self, action: #selector(didChangeTokenText), for: .editingChanged)
        field.setContentHuggingPriority(.defaultHigh, for: .vertical)
        return field
    }()
    
    private lazy var inputTextField: UITextField = {
        let field = UITextField()
        field.font = .preferredFont(forTextStyle: .headline)
        field.borderStyle = .roundedRect
        field.backgroundColor = .secondarySystemBackground
        field.addTarget(self, action: #selector(didChangeInputText), for: .editingChanged)
        field.setContentHuggingPriority(.required, for: .vertical)
        return field
    }()
    
    private lazy var resultLabel: UILabel = {
        let label = UILabel()
        label.textAlignment = .center
        label.font = .preferredFont(forTextStyle: .largeTitle)
        return label
    }()
    
    private lazy var stackView: UIStackView = {
        let vStack = UIStackView(arrangedSubviews: [tokenTextField, inputTextField, resultLabel])
        vStack.translatesAutoresizingMaskIntoConstraints = false
        vStack.axis = .vertical
        vStack.spacing = 16
        vStack.alignment = .fill
        vStack.distribution = .fill
        return vStack
    }()
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        
        addSubview(stackView)
        NSLayoutConstraint.activate([
            stackView.topAnchor.constraint(equalTo: safeAreaLayoutGuide.topAnchor),
            stackView.bottomAnchor.constraint(equalTo: safeAreaLayoutGuide.bottomAnchor),
            stackView.leadingAnchor.constraint(equalTo: safeAreaLayoutGuide.leadingAnchor),
            stackView.trailingAnchor.constraint(equalTo: safeAreaLayoutGuide.trailingAnchor),
        ])
    }
    
    required init?(coder: NSCoder) {
        super.init(coder: coder)
    }
}

extension CalculatorView {

    // MARK: 유저 Input : View -> Controller
    @objc private func didChangeTokenText(_ field: UITextField) {
        delegate?.didChangeTokenText(self,
                                     token: field.text ?? " ")
    }
    // MARK: 유저 Input : View -> Controller
    @objc private func didChangeInputText(_ field: UITextField) {
        delegate?.didChangeInputText(self,
                                     input: field.text ?? "")
    }
    
    // MARK: View에 접근하여 update할 수 있도록 메서드 구현
    func setResultText(_ result: String) {
        resultLabel.text = result
    }
}


// MARK: - CONTROLLER

class ViewController: UIViewController {
    
    let calculatorView: CalculatorView = CalculatorView(frame: .zero)
    // MARK: 유저 Input : View -> Controller
    private var token: String = ""
    
    override func viewDidLoad() {
        super.viewDidLoad()

        calculatorView.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(calculatorView)

        NSLayoutConstraint.activate([
            calculatorView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
            calculatorView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor),
            calculatorView.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor),
            calculatorView.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor),
        ])
        
        // MARK: 유저 Input : View -> Controller
        calculatorView.delegate = self
    }
}

// MARK: - Controller
extension ViewController : CalculatorViewDelegate {

    // MARK: 유저 Input : View -> Controller
    func didChangeTokenText(_ calculatorView: CalculatorView, token: String) {
        self.token = token
    }
    // MARK: 유저 Input : View -> Controller
    func didChangeInputText(_ calculatorView: CalculatorView, input: String) {
        
        // MARK: - 비즈니스 로직
        let sum: Int = input.components(separatedBy:CharacterSet(charactersIn: token))
            .compactMap { Int($0) }
            .reduce(0, +)
        
        // MARK: - View Update : Controller -> View
        calculatorView.setResultText(String(describing: sum))
    }
}

```

## MVC - Model은 어디에????

이렇게 구현을 해보면, 보통 우리가 우려하는 Massive ViewController가 되어간다.  

ViewController가 비대해진다는 거다.  

잘 살펴보면 현재 Model이 구현되어있지 않다. 


