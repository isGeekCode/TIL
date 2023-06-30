# 요즘 핫한 GPT로 앱만들어보기


## 질문 간단한 앱만들어보기
swift로 앱을 만들어줘. viewcontroller안에 두개의 UITextfield가 있어. 위에있는 첫번째 uitextfield에는 이메일이 들어가고, 아래에 있는 두번째 Uitextfield에는 8글자의 비밀번호가 들어가게해줘. 만약 두 개의 uitextfield의 값에 따라 각각의
Bool타입 변수가 true일때, 하단에  있는 UIButton을 활성화처리해줘.  snapkit라이브러리와 then라이브러리를 이용해서 만들어줘

```swift
import UIKit
import SnapKit
import Then

class ViewController: UIViewController {
    
    let emailTextField = UITextField().then {
        $0.placeholder = "Email"
    }
    
    let passwordTextField = UITextField().then {
        $0.placeholder = "Password (8 characters)"
    }
    
    let submitButton = UIButton().then {
        $0.setTitle("Submit", for: .normal)
        $0.isEnabled = false
    }
    
    var isEmailValid = false
    var isPasswordValid = false {
        didSet {
            submitButton.isEnabled = isEmailValid && isPasswordValid
        }
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        view.addSubview(emailTextField)
        view.addSubview(passwordTextField)
        view.addSubview(submitButton)
        
        emailTextField.snp.makeConstraints { make in
            make.top.equalTo(view.safeAreaLayoutGuide).offset(20)
            make.left.equalTo(view.safeAreaLayoutGuide).offset(20)
            make.right.equalTo(view.safeAreaLayoutGuide).offset(-20)
        }
        
        passwordTextField.snp.makeConstraints { make in
            make.top.equalTo(emailTextField.snp.bottom).offset(20)
            make.left.equalTo(view.safeAreaLayoutGuide).offset(20)
            make.right.equalTo(view.safeAreaLayoutGuide).offset(-20)
        }
        
        submitButton.snp.makeConstraints { make in
            make.top.equalTo(passwordTextField.snp.bottom).offset(20)
            make.left.equalTo(view.safeAreaLayoutGuide).offset(20)
            make.right.equalTo(view.safeAreaLayoutGuide).offset(-20)
        }
        
        emailTextField.addTarget(self, action: #selector(validateEmail), for: .editingChanged)
        passwordTextField.addTarget(self, action: #selector(validatePassword), for: .editingChanged)
    }
    
    @objc func validateEmail() {
        isEmailValid = emailTextField.text?.contains("@") == true
    }
    
    @objc func validatePassword() {
        isPasswordValid = passwordTextField.text?.count == 8
    }
}


```

# rxswift추가하기
위 코드에  rxswift라이브러리를 적용해줘


```swift
import UIKit
import SnapKit
import Then
import RxSwift
import RxCocoa

class ViewController: UIViewController {
    
    let emailTextField = UITextField().then {
        $0.placeholder = "Email"
    }
    
    let passwordTextField = UITextField().then {
        $0.placeholder = "Password (8 characters)"
    }
    
    let submitButton = UIButton().then {
        $0.setTitle("Submit", for: .normal)
        $0.isEnabled = false
    }
    
    let disposeBag = DisposeBag()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        view.addSubview(emailTextField)
        view.addSubview(passwordTextField)
        view.addSubview(submitButton)
        
        emailTextField.snp.makeConstraints { make in
            make.top.equalTo(view.safeAreaLayoutGuide).offset(20)
            make.left.equalTo(view.safeAreaLayoutGuide).offset(20)
            make.right.equalTo(view.safeAreaLayoutGuide).offset(-20)
        }
        
        passwordTextField.snp.makeConstraints { make in
            make.top.equalTo(emailTextField.snp.bottom).offset(20)
            make.left.equalTo(view.safeAreaLayoutGuide).offset(20)
            make.right.equalTo(view.safeAreaLayoutGuide).offset(-20)
        }
        
        submitButton.snp.makeConstraints { make in
            make.top.equalTo(passwordTextField.snp.bottom).offset(20)
            make.left.equalTo(view.safeAreaLayoutGuide).offset(20)
            make.right.equalTo(view.safeAreaLayoutGuide).offset(-20)
        }
        
        let emailValid = emailTextField.rx.text.orEmpty
            .map { $0.contains("@") }
            .share(replay: 1)
        
        let passwordValid = passwordTextField.rx.text.orEmpty
            .map { $0.count == 8 }
            .share(replay: 1)
        
        Observable.combineLatest(emailValid, passwordValid)
            .map { $0 && $1 }
            .bind(to: submitButton.rx.isEnabled)
            .disposed(by: disposeBag)
    }
}

```

## MVVM추가하기
위 코드를 mvvm형식으로 만들어줘


```swift
import UIKit
import SnapKit
import Then
import RxSwift
import RxCocoa

class ViewModel {
    let emailValid: Observable<Bool>
    let passwordValid: Observable<Bool>
    let submitEnabled: Observable<Bool>
    
    init(emailText: Observable<String>, passwordText: Observable<String>) {
        emailValid = emailText
            .map { $0.contains("@") }
            .share(replay: 1)
        
        passwordValid = passwordText
            .map { $0.count == 8 }
            .share(replay: 1)
        
        submitEnabled = Observable.combineLatest(emailValid, passwordValid)
            .map { $0 && $1 }
    }
}

class ViewController: UIViewController {
    
    let emailTextField = UITextField().then {
        $0.placeholder = "Email"
    }
    
    let passwordTextField = UITextField().then {
        $0.placeholder = "Password (8 characters)"
    }
    
    let submitButton = UIButton().then {
        $0.setTitle("Submit", for: .normal)
        $0.isEnabled = false
    }
    
    let disposeBag = DisposeBag()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        view.addSubview(emailTextField)
        view.addSubview(passwordTextField)
        view.addSubview(submitButton)
        
        emailTextField.snp.makeConstraints { make in
            make.top.equalTo(view.safeAreaLayoutGuide).offset(20)
            make.left.equalTo(view.safeAreaLayoutGuide).offset(20)
            make.right.equalTo(view.safeAreaLayoutGuide).offset(-20)
        }
        
        passwordTextField.snp.makeConstraints { make in
            make.top.equalTo(emailTextField.snp.bottom).offset(20)
            make.left.equalTo(view.safeAreaLayoutGuide).offset(20)
            make.right.equalTo(view.safeAreaLayoutGuide).offset(-20)
        }
        
        submitButton.snp.makeConstraints { make in
            make.top.equalTo(passwordTextField.snp.bottom).offset(20)
            make.left.equalTo(view.safeAreaLayoutGuide).offset(20)
            make.right.equalTo(view.safeAreaLayoutGuide).offset(-20)
        }
        
        let emailText = emailTextField.rx.text.orEmpty
        let passwordText = passwordTextField.rx.text.orEmpty
        let viewModel = ViewModel(emailText: emailText, passwordText: passwordText)
        
        viewModel.submitEnabled
            .bind(to: submitButton.rx.isEnabled)
            .disposed(by: disposeBag)
    }
}

```
왠지 만들다 포기했네요 죽었나? 
하지만 테스트결과 지난 값은 이어갈 수 있는 것 같습니다.

## reactor kit 추가하기
위 코드에 reactor kit라이브러리를 적용해줘
```swift
import UIKit
import ReactorKit
import SnapKit

class LoginViewController: UIViewController, View {
    typealias Reactor = LoginReactor

    let emailTextField = UITextField()
    let passwordTextField = UITextField()
    let loginButton = UIButton()

    init(reactor: Reactor) {
        super.init(nibName: nil, bundle: nil)
        self.reactor = reactor
    }

    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    func bind(reactor: Reactor) {
        // Actions
        emailTextField.rx.text.map { Reactor.Action.updateEmail($0) }
            .bind(to: reactor.action)
            .disposed(by: disposeBag)

        passwordTextField.rx.text.map { Reactor.Action.updatePassword($0) }
            .bind(to: reactor.action)
            .disposed(by: disposeBag)

        loginButton.rx.tap.map { Reactor.Action.submit }
            .bind(to: reactor.action)
            .disposed(by: disposeBag)

        // States
        reactor.state.map { $0.isValid }
            .distinctUntilChanged()
            .bind(to: loginButton.rx.isEnabled)
            .disposed(by: disposeBag)
    }

    override func viewDidLoad() {
        super.viewDidLoad()

        emailTextField.placeholder = "Email"
        view.addSubview(emailTextField)

        passwordTextField.placeholder = "Password"
        passwordTextField.isSecureTextEntry = true
        view.addSubview(passwordTextField)

        loginButton.setTitle("Login", for: .normal)
        loginButton.isEnabled = false
        view.addSubview(loginButton)

        emailTextField.snp.makeConstraints { make in
            make.top.equalToSuperview().offset(20)
            make.left.equalToSuperview().offset(20)
            make.right.equalToSuperview().offset(-20)
        }

        passwordTextField.snp.makeConstraints { make in
            make.top.equalTo(emailTextField.snp.bottom).offset(20)
            make.left.equalToSuperview().offset(20)
            make.right.equalToSuperview().offset(-20)
        }

        loginButton.snp.makeConstraints { make in
            make.top.equalTo(passwordTextField.snp.bottom).offset(20)
            make.left.equalToSuperview().offset(20)
            make.right.equalToSuperview().offset(-20)
        }
    }
}

final class LoginReactor: Reactor {
    enum Action {
        case updateEmail(String?)
        case updatePassword(String?)
        case submit
    }

    enum Mutation {
        case setEmail(String?)
        case setPassword(String?)
    }

    struct State {
        var email: String?
        var password: String?
        var isValid: Bool {
           
```

## 화면이동 연결하기

위 코드에서 uibutton이 활성화됐을때, 버튼을 누르면 settingviewcontroller라는 이름의 viewcontroller가 push형식으로 이동할 수 있도록 적용해줘

```swift
import ReactorKit
import UIKit

class ViewController: UIViewController, StoryboardView {
    @IBOutlet weak var emailTextField: UITextField!
    @IBOutlet weak var passwordTextField: UITextField!
    @IBOutlet weak var submitButton: UIButton!
    
    var disposeBag = DisposeBag()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Reactor Kit
        reactor = ViewReactor()
        
        emailTextField.rx.text
            .orEmpty
            .bind(to: reactor!.action.map(Reactor.Action.updateEmail))
            .disposed(by: disposeBag)
        
        passwordTextField.rx.text
            .orEmpty
            .bind(to: reactor!.action.map(Reactor.Action.updatePassword))
            .disposed(by: disposeBag)
        
        reactor!.state.map { $0.isValid }
            .bind(to: submitButton.rx.isEnabled)
            .disposed(by: disposeBag)
        
        submitButton.rx.tap
            .subscribe(onNext: { [weak self] _ in
                guard let self = self else { return }
                let vc = SettingViewController.instantiate()
                self.navigationController?.pushViewController(vc, animated: true)
            })
            .disposed(by: disposeBag)
    }
}

final class ViewReactor: Reactor {
    enum Action {
        case updateEmail(String)
        case updatePassword(String)
    }
    
    enum Mutation {
        case setEmail(String)
        case setPassword(String)
    }
    
    struct State {
        var email: String
        var password: String
        var isValid: Bool {
            return email.contains("@") && password.count >= 8
        }
    }
    
    var initialState: State
    
    init() {
        initialState = State(email: "", password: "")
    }
    
    func mutate(action: Action) -> Observable<Mutation> {
        switch action {
        case .updateEmail(let email):
            return .just(.setEmail(email))
        case .updatePassword(let password):
            return .just(.setPassword(password))
        }
    }
    
    func reduce(state: State, mutation: Mutation) -> State {
        var state = state
        switch mutation {
        case .setEmail(let email):
            state.email = email
        case .setPassword(let password):
            state.password = password
        }
        return state
    }
}

```

## 두번째 화면 설정하기
위 코드에서 settingviewcontroller에는 위에는 navigationController 의 title은 large로 해줘. 아래에는 uitableview를 만들어줘

```swift
class ViewController: UIViewController {

    private let emailTextField = UITextField()
    private let passwordTextField = UITextField()
    private let loginButton = UIButton()

    private let viewModel: LoginViewModel
    
    init(viewModel: LoginViewModel) {
        self.viewModel = viewModel
        super.init(nibName: nil, bundle: nil)
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
        bindViewModel()
    }
    
    private func setupUI() {
        // Setup emailTextField
        emailTextField.placeholder = "Email"
        view.addSubview(emailTextField)
        
        // Setup passwordTextField
        passwordTextField.placeholder = "Password (8 characters)"
        passwordTextField.isSecureTextEntry = true
        view.addSubview(passwordTextField)
        
        // Setup loginButton
        loginButton.setTitle("Login", for: .normal)
        loginButton.isEnabled = false
        view.addSubview(loginButton)
        
        // Setup Constraints
        emailTextField.snp.makeConstraints { make in
            make.top.equalTo(view.safeAreaLayoutGuide).offset(20)
            make.leading.trailing.equalTo(view.safeAreaLayoutGuide).inset(20)
        }
        
        passwordTextField.snp.makeConstraints { make in
            make.top.equalTo(emailTextField.snp.bottom).offset(20)
            make.leading.trailing.equalTo(view.safeAreaLayoutGuide).inset(20)
        }
        
        loginButton.snp.makeConstraints { make in
            make.top.equalTo(passwordTextField.snp.bottom).offset(20)
            make.leading.trailing.equalTo(view.safeAreaLayoutGuide).inset(20)
        }
    }
    
    private func bindViewModel() {
        let input = LoginViewModel.Input(email: emailTextField.rx.text.orEmpty.asObservable(),
                                         password: passwordTextField.rx.text.orEmpty.asObservable(),
                                         loginTap: loginButton.rx.tap.asObservable())
        let output = viewModel.transform(input: input)
        
        output.isValid
            .drive(loginButton.rx.isEnabled)
            .disposed(by: rx.disposeBag)
        
        output.login
            .subscribe(onNext: { [weak self] in
                guard let self = self else { return }
                let settingVC = SettingViewController()
                self.navigationController?.pushViewController(settingVC, animated: true)
            })
            .disposed(by: rx.disposeBag)
    }
}

class SettingViewController: UIViewController {

    private let tableView = UITableView()
    
    override func viewDidLoad() {
        super.viewDidLoad

```
역시나 길어지니 뻗어버렸다

## Coordinator패턴 적용시키기
위 코드에 coordinator패턴을 적용시켜줘


```swift
import UIKit

class LoginViewController: UIViewController {
    let emailTextField = UITextField()
    let passwordTextField = UITextField()
    let loginButton = UIButton()

    let viewModel = LoginViewModel()
    let coordinator: LoginCoordinator

    init(coordinator: LoginCoordinator) {
        self.coordinator = coordinator
        super.init(nibName: nil, bundle: nil)
    }

    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    override func viewDidLoad() {
        super.viewDidLoad()

        view.backgroundColor = .white

        emailTextField.placeholder = "Email"
        passwordTextField.placeholder = "Password"
        passwordTextField.isSecureTextEntry = true

        loginButton.setTitle("Login", for: .normal)
        loginButton.setTitleColor(.black, for: .normal)
        loginButton.isEnabled = false

        view.addSubview(emailTextField)
        view.addSubview(passwordTextField)
        view.addSubview(loginButton)

        emailTextField.snp.makeConstraints { (make) in
            make.top.equalToSuperview().offset(100)
            make.left.equalToSuperview().offset(16)
            make.right.equalToSuperview().offset(-16)
            make.height.equalTo(44)
        }

        passwordTextField.snp.makeConstraints { (make) in
            make.top.equalTo(emailTextField.snp.bottom).offset(16)
            make.left.right.height.equalTo(emailTextField)
        }

        loginButton.snp.makeConstraints { (make) in
            make.top.equalTo(passwordTextField.snp.bottom).offset(16)
            make.left.right.height.equalTo(emailTextField)
        }

        loginButton.rx.tap.subscribe(onNext: { [weak self] in
            guard let self = self else { return }
            self.coordinator.goToSettings()
        }).disposed(by: viewModel.disposeBag)

        viewModel.emailValid.bind(to: emailTextField.rx.valid).disposed(by: viewModel.disposeBag)
        viewModel.passwordValid.bind(to: passwordTextField.rx.valid).disposed(by: viewModel.disposeBag)
        viewModel.allValid.bind(to: loginButton.rx.enabled).disposed(by: viewModel.disposeBag)

        emailTextField.rx.text.orEmpty.bind(to: viewModel.email).disposed(by: viewModel.disposeBag)
        passwordTextField.rx.text.orEmpty.bind(to: viewModel.password).disposed(by: viewModel.disposeBag)
    }
}

class SettingsViewController: UITableViewController {
    override func viewDidLoad() {
        super.viewDidLoad()

        title = "Settings"
        tableView.register(UITableViewCell.self, forCellReuseIdent
```
오...UITableViewController라는 클래스를 하나 생성하려 했나보다.


## rxswift, mvvm, coordinator, reactorkit 모두 적용시키기

위코드에 rxswift, mvvm, coordinator, reactorkit 을 적용시켜줘

```
Sorry, it's not possible to apply all the architectures and libraries in the same code. Each architecture and library has its own way of implementing and solving a problem. It is recommended to choose one architecture and library that best fits your project needs and requirements.

```
요건 안된단다.


