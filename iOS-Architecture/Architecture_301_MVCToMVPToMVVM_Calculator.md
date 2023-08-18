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

<br><br>

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

<br><br>

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

<br><br>

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

<br><br>

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

<br><br><br>

## MVC - Model은 어디에????

이렇게 구현을 해보면, 보통 우리가 우려하는 Massive ViewController가 되어간다.  

ViewController가 비대해진다는 거다.  

잘 살펴보면 현재 Model이 구현되어있지 않다.  
우리가 구현한건 아래 그림과 같다.  


<br>

<img width="600" alt="스크린샷 2023-08-17 오후 1 57 54" src="https://github.com/isGeekCode/TIL/assets/76529148/44b31f21-be12-4637-ba60-5689b92121d2">

<br><br>

그럼에도 간단하게 만들다보면

- View를 ViewController안에서 만드는 경우
- Model도 안나눈 경우

이제 모델을 나눠보자..

<br><br>

### Model구현하기

따로 Model을 구현할 파일을 하나 만들자.

struct로 구현을 하고 기존에 ViewController에서 갖고 있던 데이터를 Model로 옮긴다. 


```swift

// MARK: - Controller

class ViewController: UIViewController {

    // MARK: Controller는 View와 Model을 소유
    private let calculatorView: CalculatorView = CalculatorView(frame: .zero)
    private let model: Calculator = Calculator()
    // private var token: String = ""
}

extension ViewController : CalculatorViewDelegate {
    // 유저 input을 받으면 호출되는 delegate 메서드
    func didChangeTokenText(_ calculatorView: CalculatorView, token: String) {
        
        // MARK: Model update : Controller -> Model
        model.token = token
//        self.token = token
    }
}


// MARK: - Model

class Calculator {
    // MARK: 변하는 Value자체를 Model에서 소유
    var token: String = ""
}


```

그리고 Controller에서 갖고있던 비즌이스로직들도 옮긴다. 

```swift
// MARK: - Model

class Calculator {

    var token: String = ""
    
    // MARK: Model에 접근하여 Business Logic을 처리할 수 있도록 메서드 구현
    func calculate(with input: String) -> Int {
        input.components(separatedBy:CharacterSet(charactersIn: token))
            .compactMap { Int($0) }
            .reduce(0, +)
    }
}



// MARK: - Controller
extension ViewController : CalculatorViewDelegate {

    // 유저 input을 받으면 호출되는 delegate 메서드
    func didChangeInputText(_ calculatorView: CalculatorView, input: String) {
        
        // MARK: Model update & return : Controller -> Model -> Controller
        let sum: Int = model.calculate(with: input)
//        let sum: Int = input.components(separatedBy:CharacterSet(charactersIn: token))
//            .compactMap { Int($0) }
//            .reduce(0, +)
        
        // model의 비즈니스 로직 결과를 받아서 view로 전달
        calculatorView.setResultText(String(describing: sum))
    }
}

```

자 이제 이동한 전체코드를 다시 살펴보자.  
이렇게 비즈니스로직을 Model로 충실하게 옮겨두면 MVC에서 ViewController가 비대해질 가능성이 월등히 낮아진다.  

```swift
// MARK: - MODEL

class Calculator {
    // MARK: 변하는 Value자체를 Model에서 소유
    var token: String = ""
    
    // MARK: Model에 접근하여 Business Logic을 처리할 수 있도록 메서드 구현
    func calculate(with input: String) -> Int {
        input.components(separatedBy:CharacterSet(charactersIn: token))
            .compactMap { Int($0) }
            .reduce(0, +)
    }
}

// MARK: - CONTROLLER

class ViewController: UIViewController {
    
    // MARK: Controller는 View와 Model을 소유
    private let calculatorView: CalculatorView = CalculatorView(frame: .zero)
    private let model: Calculator = Calculator()
    
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
        
        // MARK: Model update : Controller -> Model
        model.token = token
    }
    
    // MARK: 유저 Input : View -> Controller
    func didChangeInputText(_ calculatorView: CalculatorView, input: String) {
        
        // MARK: Model update & notify : Controller -> Model -> Controller
        let sum: Int = model.calculate(with: input)

        // MARK: - View Update : Controller -> View
        calculatorView.setResultText(String(describing: sum))
    }
}

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
```

<br><br><br>

MVC로 확실하게 분리하지 않은 상태에서 맹목적으로 Massive ViewController가 되니까 MVVM으로 가야한다는 생각으로 흘러가면 안된다. 


그렇다면 MVVM은 뭘까???

Model - View - ViewModel 로 나뉘어 진것은 알 수 있다.

그럼 우리가 궁금해야할 것은 이것이다. 
- Model과 ViewModel은 어떤 점이 다를까, 어떻게 나눌까
- Massive ViewModel은 왜 생길까?
- Massive ViewModel이 되는 현상이 일어나면 어떻게 해야하나

<br><br>

위키피디아에서 MVC 디자인패턴을 검색해보면 아래와 같은 내용을 볼 수 있다.  

<img width="600" alt="_mvvm_in_practice _010" src="https://github.com/isGeekCode/TIL/assets/76529148/77db82a6-3613-4450-b2e9-89531e79d513">

<br><br>

사실상 현업에서 경험하지않은 이상 비즈니스 로직이 비대해지는 것을 경험하기란 힘들다.  

몰랐던 것 뿐이기 때문에 앞으로는 Model에 비즈니스 로직을 분리하는 연습을 하도록 하자.  

그래서 위 그림에서 나온 것처럼 서로 영향없이 쉽게 고칠 수 있는 어플리케이션을 만들려면, 

모델을 제대로 분리했을 때 가능해진다.  

MVC를 제대로 만드는 경험을 해보자.  

원래 MVC 디자인패턴은 웹 프레임워크에서 처음으로 사용하기 시작했던 패턴이다. 아래 그림은 애플에서 제공하는 그림과 조금 다르게 생겼다.  

<img width="600" alt="_mvvm_in_practice _011" src="https://github.com/isGeekCode/TIL/assets/76529148/575215e2-6f48-471c-9cf8-94844b3bab3d">

다시 애플에서 제공한 Cocoa Framework를 출시하면서 소개한 MVC구조를 보자.  

위의 그림과 다르다. 그래서 이 구조를 `Cocoa MVC` 라고도 부른다.  

이 그림을 살펴보면 Mediator, Strategy, Observer, Command, Composite 패턴 등을 볼 수 있다. 

<img width="600" alt="스크린샷 2023-08-17 오후 3 00 38" src="https://github.com/isGeekCode/TIL/assets/76529148/50673476-cabc-448b-8f62-9aebc640e60f">

최근에는 위 이미지가 아래처럼 변경되었다.  

<img width="600" alt="스크린샷 2023-08-17 오후 1 57 54" src="https://github.com/isGeekCode/TIL/assets/76529148/44b31f21-be12-4637-ba60-5689b92121d2">

이와 관련해서 스탠퍼드 강좌에서 정말 잘 표현한 그림이 있다.  

<img width="600" alt="스크린샷 2023-08-17 오후 4 00 06" src="https://github.com/isGeekCode/TIL/assets/76529148/38130ea2-8911-4c39-a6a0-d812ee132e40">

위 그림에서 살펴보면 Controller는 중간 다리역할만 한다.  

- View와 Model사이에는 노란색의 중앙선이 있다.
    - View와 Model은 서로 알 수 없다. 
- Model과 Controller 사이에 Controlelr쪽만 점선이다.
    - Model은 Controller를 모른다.
- View와 Controller 사이에 Controlelr쪽만 점선이다.
    - View는 Controller를 모른다.


## MVP
MVC가 너무 Massive해진다고 해서 시도한 패턴은 MVP패턴이다.
 
> Model - View - Presenter

<img width="600" alt="_mvvm_in_practice _017" src="https://github.com/isGeekCode/TIL/assets/76529148/2870e4e2-0261-49f1-b9bd-5df8569e6ece">

MVP는 MVC에서 파생된 패턴이다.  

MVC와 다른점은 Presenter가 로직을 다 가져간다는 것이다.  

아래 도표를 보자.  

<img width="600" alt="[_mvvm_in_practice _018" src="https://github.com/isGeekCode/TIL/assets/76529148/2870e4e2-0261-49f1-b9bd-5df8569e6ece](https://github.com/isGeekCode/TIL/assets/76529148/01efbbc7-3420-467c-b788-6039c842fcb0">

View는 보이는 것처럼 수동적(Passive)이다.  

근데 가만히 보면 Apple이 소개한 cocoa MVC와 비슷하다는 느낌을 받는다.  

하지만 MVC와 MVP의 큰 차이가 있다.  

MVP는 View와 Presenter가 1:1의 관계가 있다. 

Presenter는 View마다 존재하게 되어있다.  

서로를 알고 있다. 손을 맞잡고 있는 형태이다.  

다만 이럴경우, BoilerPlate 코드가 굉장히 많아진다. 

그럼 MVP로 한번 작업해보자. 

Presenter를 생성해보자. 

### Presenter 생성

- 이제 MVC의 Controller 역할을 하던 ViewController는 View취급을 한다. 
- Model은 Presenter로 이동한다. 
- Presenter View 1:1 매칭하기
    - Presenter에는 View가 self로 선언할 옵셔널 변수를 만들고 init 메서드를 구현한다. 
    - View에서 Presenter를 init 하여 view를 자신으로 선언한다.  
- 이 때, presenter와 View는 `약한 참조`를 위해 weak 으로 선언한다. 
 
```swift

// MARK: - PRESENTER
class Presenter {
    // Controller역할을 하던 ViewControlelr에서 가져왔다.
    private let model: Calculator = Calculator()
    
    // View가 self로 선언할 변수
    private weak var view: ViewController?
    
    // MARK: Presenter와 View 매칭
    init(view: ViewController?) {
        self.view = view
    }
}


// MARK: - VIEW
class ViewController: UIViewController {
    
    // MARK: Presenter와 View 매칭
    private lazy var presenter: Presenter = Presenter(view: self)
    // MODEL은 Presenter로 이동
//    private let model: Calculator = Calculator()

}

```


### 프로토콜도 Presenter가 수행한다. 

```swift
// MARK: - PRESENTER

class Presenter {

    private let model: Calculator = Calculator()
    let view: ViewController?
    
    init(view: ViewController?) {
        self.view = view
    }
}

extension Presenter : CalculatorViewDelegate {

    // MARK: 유저 Input : View -> Presenter
    func didChangeTokenText(_ calculatorView: CalculatorView, token: String) {
        // MARK: updates Model : Presenter -> Model
        model.token = token
    }
    
    // MARK: 유저 Input : View -> Presenter
    func didChangeInputText(_ calculatorView: CalculatorView, input: String) {
        
        // MARK: updates Model & state change events : Presenter -> Model -> Presenter
        let sum: Int = model.calculate(with: input)
        // MARK: - updates View : Presenter -> View
        calculatorView.setResultText(String(describing: sum))
    }
}

// MARK: - VIEW
class ViewController: UIViewController {
    
    lazy var presenter: Presenter = Presenter(view: self)

    override func viewDidLoad() {
        super.viewDidLoad()

        // MARK: 유저 Input : View -> Presenter
        calculatorView.delegate = presenter
}
```

이렇게 하면 정상 작동한다.  

- 기존의 Model이 갖고있던 비즈니스로직은 그대로 가져간다. 
- Presenter가 View의 Delegate패턴을 가져간다. 
    - 변경 전 MVC 동작 : View ~> `Delegate패턴` ~> Controller -> Model 동작
    - 변경 후 MVP 동작 : View(ViewController) ~> `Delegate패턴` ~> Presenter -> Model


### 전체코드
```
// MARK: - MODEL

class Calculator {
    // MARK: 변하는 Value자체를 Model에서 소유
    var token: String = ""
    
    // MARK: Model에 접근하여 Business Logic을 처리할 수 있도록 메서드 구현
    func calculate(with input: String) -> Int {
        input.components(separatedBy:CharacterSet(charactersIn: token))
            .compactMap { Int($0) }
            .reduce(0, +)
    }
}

// MARK: - PRESENTER

class Presenter {
    
    private let model: Calculator = Calculator()
    private weak var view: ViewController?
    
    // MARK: Presenter와 View 매칭
    init(view: ViewController?) {
        self.view = view
    }
}

extension Presenter : CalculatorViewDelegate {

    // MARK: 유저 Input : View -> Presenter
    func didChangeTokenText(_ calculatorView: CalculatorView, token: String) {
        // MARK: updates Model : Presenter -> Model
        model.token = token
    }
    
    // MARK: 유저 Input : View -> Presenter
    func didChangeInputText(_ calculatorView: CalculatorView, input: String) {
        
        // MARK: updates Model & state change events : Presenter -> Model -> Presenter
        let sum: Int = model.calculate(with: input)
        // MARK: - updates View : Presenter -> View
        calculatorView.setResultText(String(describing: sum))
    }
}

// MARK: - VIEW

class ViewController: UIViewController {
    
    // MARK: Presenter와 View 매칭
    private lazy var presenter: Presenter = Presenter(view: self)
    private let calculatorView: CalculatorView = CalculatorView(frame: .zero)
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // MARK: 유저 Input : View -> Presenter
        calculatorView.delegate = presenter

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

// MARK: 유저 Input : View -> Presenter
protocol CalculatorViewDelegate: AnyObject {
    func didChangeTokenText(_ calculatorView: CalculatorView, token: String)
    func didChangeInputText(_ calculatorView: CalculatorView, input: String)
}

class CalculatorView: UIView {
    
    // MARK: 유저 Input : View -> Presenter
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
    
    // MARK: 유저 Input : View -> Presenter
    @objc private func didChangeTokenText(_ field: UITextField) {
        delegate?.didChangeTokenText(self,
                                     token: field.text ?? " ")
    }
    // MARK: 유저 Input : View -> Presenter
    @objc private func didChangeInputText(_ field: UITextField) {
        delegate?.didChangeInputText(self,
                                     input: field.text ?? "")
    }
    
    // MARK: View에 접근하여 update할 수 있도록 메서드 구현
    func setResultText(_ result: String) {
        resultLabel.text = result
    }
}
```

## TEST환경

MVC자체가 단점이 없는것은 아니다. 

다만 MVC패턴을 이용할때,  

Model은 테스트하기 어렵지않은데  

Controller를 테스트하기가 정말 어렵다.  

특히 그냥 Controller 말고 ViewController객체에 있어서는 테스트하기가 정말 불리하다.   

MVP의 경우 Presenter는 테스트하기가 정말 용이해지기때문에 TEST환경을 구축할 수 있다.  

그래서 MVP를 선호하는 경향이 있다.  

다만 문제는 View마다 Presenter가 생성되기 때문에 BolierPlate 코드가 많아지게 된다. 
> 보일러플레이트 코드는 애플리케이션의 핵심 로직과는 직접적인 연관이 없지만 필요한 설정, 초기화, 기본 구조 등을 구현하는 코드를 말한다. 

그래서 이제 MVVM을 언급하기 시작했다.  

## MVVM

<img width="600" alt="_mvvm_in_practice _020" src="https://github.com/isGeekCode/TIL/assets/76529148/922a4845-180f-4010-9b9a-bb467e8facbe">


그렇다면 Model과 ViewModel은 어떻게 구분할 것인가??

- View 로직 : 디스플레이 로직
- 데이터 로직 : 백엔드 로직

로직이 들어가는 걸 보니까 Model이다.  

아래 그림을 보자.  

<img width="600" alt="_mvvm_in_practice _022" src="https://github.com/isGeekCode/TIL/assets/76529148/11293228-a643-41d5-bc0f-d6631d1434ae">

여기에서 가장 중요한 것은 Binding이다.  

- Model과 ViewModel은 서로 Notification을 주고 받고 있다.
- View와 ViewModel은 서로 Binding이 되어있다. 

<img width="600" alt="_mvvm_in_practice _023" src="https://github.com/isGeekCode/TIL/assets/76529148/d59dbe22-7167-4185-a2d2-c99f23cd747e">

그래서 MVVM에서 핵심은 아래와 같다.  

- View로직, 비즈니스 로직의 분리
- 데이터 바인딩


### Data Binding 을 하는 방법
데이터를 서로 동기화를 성취하기만 하면된다.  
먼저 라이브러리보다는 iOS의 기본 방법들을 익히는 게 좋다.
- Property Observers
- KVO : Key - Value Observing
- Notification Center
- Delegation
- (RxSwift)
- (Combine)


## 예제 MVVM으로 변경하기

- 먼저 ViewModel 클래스를 생성한다. 
- Presenter가 갖고 있던 로직들을 ViewModel이 가져간다. 


```swift

// MARK: - VIEW
class ViewController: UIViewController {
    
    // Presenter를 없애고 ViewModel 생성
    private let viewModel: ViewModel = ViewModel()
//    private lazy var presenter: Presenter = Presenter(view: self)

    override func viewDidLoad() {
        super.viewDidLoad()

        // MARK: 유저 Input : View -> ViewModel
        calculatorView.delegate = viewModel
    }
}

```

- presenter가 맡았던 View의 input을 옮기기 위해 delegate을 ViewModel에서 처리한다. 

```swift


class ViewModel {

    private let model: Calculator = Calculator()

}

extension ViewModel : CalculatorViewDelegate {

    // MARK: 유저 Input : View -> ViewModel
    func didChangeTokenText(_ calculatorView: CalculatorView, token: String) {
        // MARK: updates Model : ViewModel -> Model
        model.token = token
    }
    
    // MARK: 유저 Input : View -> ViewModel
    func didChangeInputText(_ calculatorView: CalculatorView, input: String) {
        
        // MARK: updates Model & state change events : ViewModel -> Model -> ViewModel
        let sum: Int = model.calculate(with: input)
        // MARK: - updates View : ViewModel -> View
        calculatorView.setResultText(String(describing: sum))
    }
}


```


ViewModel은 View에 필요한 정보를 담고 있다. 
- inputText
- token
- result


```swift
class ViewModel {
    
    private let model: Calculator = Calculator()
    var inputText: String = ""
    var token: String = " "
    var result: Int = 0
}

```
그리고  ViewModel의 result가 바뀔때마다 View에 동기화가 되야한다. 

여기서는 KVO를 사용해보자.  


- ViewModel에 NSObject 상속
- ViewModel에서 추적할 result에 키워드를 붙인다. 
- View에 변수 NSKeyValueObservation 선언
- "result" keypath를 이용해서 calculatorView에 업데이트 처리
    - NSKeyValueObservation객체에 `viewModel.observe`메서드를 선언

```swift
class ViewModel: NSObject {
    
    private let model: Calculator = Calculator()
    var inputText: String = ""
    var token: String = " "
    @objc dynamic var result: Int = 0
}


class ViewController: UIViewController {

    private let viewModel: ViewModel = ViewModel()
    
    private var observation: NSKeyValueObservation?
    
    override func viewDidLoad() {
    super.viewDidLoad()

    // "result" keypath를 이용해서 calculatorView에 업데이트 처리
    observation = viewModel.observe(\.result) { ViewModel, changes in
        self.calculatorView.setResultText(String(describing: changes.newValue))
    }

}
```

### 전체코드

```swift

// MARK: MODEL

class Calculator {
    // MARK: 변하는 Value자체를 Model에서 소유
    var token: String = ""
    
    // MARK: Model에 접근하여 Business Logic을 처리할 수 있도록 메서드 구현
    func calculate(with input: String) -> Int {
        input.components(separatedBy:CharacterSet(charactersIn: token))
            .compactMap { Int($0) }
            .reduce(0, +)
    }
}



//MARK: - VIEW MODEL
class ViewModel: NSObject {
    
    private let model: Calculator = Calculator()

    var inputText: String = ""
    var token: String = " "
    @objc dynamic var result: Int = 0
}


extension ViewModel : CalculatorViewDelegate {

    // MARK: 유저 Input : View -> ViewModel
    func didChangeTokenText(_ calculatorView: CalculatorView, token: String) {
        // MARK: updates Model : ViewModel -> Model
        model.token = token
    }
    
    // MARK: 유저 Input : View -> ViewModel
    func didChangeInputText(_ calculatorView: CalculatorView, input: String) {
        
        // MARK: updates Model & state change events : ViewModel -> Model -> ViewModel
        let sum: Int = model.calculate(with: input)
        // MARK: - updates View : ViewModel -> View
        calculatorView.setResultText(String(describing: sum))
    }
}


// MARK: - VIEW
class ViewController: UIViewController {
    
    private let calculatorView: CalculatorView = CalculatorView(frame: .zero)

    private let viewModel: ViewModel = ViewModel()
    
    private var observation: NSKeyValueObservation?
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // "result" keypath를 이용해서 calculatorView에 업데이트 처리
        observation = viewModel.observe(\.result) { ViewModel, changes in
            self.calculatorView.setResultText(String(describing: changes.newValue))
        }
        
        // MARK: 유저 Input : View -> ViewModel
        calculatorView.delegate = viewModel

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


// MARK: 유저 Input : View -> ViewModel
protocol CalculatorViewDelegate: AnyObject {
    func didChangeTokenText(_ calculatorView: CalculatorView, token: String)
    func didChangeInputText(_ calculatorView: CalculatorView, input: String)
}

class CalculatorView: UIView {
    
    // MARK: 유저 Input : View -> ViewModel
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
    
    // MARK: 유저 Input : View -> ViewModel
    @objc private func didChangeTokenText(_ field: UITextField) {
        delegate?.didChangeTokenText(self,
                                     token: field.text ?? " ")
    }
    // MARK: 유저 Input : View -> ViewModel
    @objc private func didChangeInputText(_ field: UITextField) {
        delegate?.didChangeInputText(self,
                                     input: field.text ?? "")
    }
    
    // MARK: View에 접근하여 update할 수 있도록 메서드 구현
    func setResultText(_ result: String) {
        resultLabel.text = result
    }
}

```





```swift
```
```swift
```
```swift
```
```swift
```

![_mvvm_in_practice _026](https://github.com/isGeekCode/TIL/assets/76529148/5ecd01b8-097b-44f4-98d9-47afc7b24c9f)
![_mvvm_in_practice _030](https://github.com/isGeekCode/TIL/assets/76529148/f0ee5332-2b85-4b81-8ed4-1c893aaf5e18)


## History
- 230816: MVC 패턴 작성
- 230817: MVP 패턴 작성

