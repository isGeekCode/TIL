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




그래서 결국 MVVM


```swift
```
```swift
```
