# TDD - 테스트 주도 개발 (iOS)

> Test-Driven Development for iOS

## TDD란?

간단정리: **테스트를 먼저 작성**하고, 그 테스트를 통과하는 코드를 작성하는 개발 방법론.

TDD는 코드를 작성하기 전에 실패하는 테스트를 먼저 작성하고, 그 테스트를 통과시키는 최소한의 코드를 작성한 후, 리팩토링하는 사이클을 반복합니다.

## TDD 학습 로드맵

**중요**: TDD를 시작하기 전에 **Unit Test 작성법**을 먼저 익혀야 합니다.

### 학습 순서
```
1. Unit Test 기초
   ↓
   - XCTest 프레임워크 사용법
   - Assertion 메서드 익히기
   - Given-When-Then 패턴
   ↓
2. Test Double
   ↓
   - Mock, Stub, Spy 개념
   - 의존성 주입 (Dependency Injection)
   ↓
3. TDD 사이클 연습
   ↓
   - Red-Green-Refactor 반복
   - 작은 단위로 시작
   ↓
4. 실무 적용
   ↓
   - MVVM/MVP 패턴과 결합
   - CI/CD 통합
```

## 간단 구현 접근방법

### TDD 환경 구성 (iOS)
- 1. **XCTest 프레임워크** - iOS 기본 테스트 프레임워크
- 2. **테스트 타겟** - Xcode 프로젝트에 Test Target 추가
- 3. **테스트 파일** - `Tests` 폴더에 `*Tests.swift` 파일 생성
- 4. **import** - `@testable import YourApp` 으로 앱 모듈 접근

### 필요한 구성 요소
- **SUT (System Under Test)**: 테스트할 대상 객체
- **Test Double**: Mock, Stub, Spy 등 테스트용 객체
- **Assertion**: 기대값과 실제값 비교

### TDD 사이클
1. **Red**: 실패하는 테스트 작성
2. **Green**: 테스트를 통과하는 최소한의 코드 작성
3. **Refactor**: 코드 개선 (테스트는 그대로 유지)

<br><br>

## TDD 구동 원리

**핵심 개념:**
- **테스트 먼저 (Test First)** - 코드보다 테스트를 먼저 작성
- **작은 단계 (Baby Steps)** - 한 번에 하나의 기능만 테스트
- **빠른 피드백 (Fast Feedback)** - 테스트는 빠르게 실행되어야 함

### Red-Green-Refactor 사이클

```
📕 Red (실패)
   ↓
   테스트 작성 (실패하는 테스트)
   ↓
📗 Green (성공)
   ↓
   최소 코드 작성 (테스트 통과)
   ↓
🔵 Refactor (개선)
   ↓
   코드 개선 (테스트 유지)
   ↓
   (반복)
```

### 동작 방식 (iOS 예시)

**1. Red - 실패하는 테스트 작성**
```swift
func testLoginButtonTitle() {
    // Given
    let viewController = LoginViewController()

    // When
    viewController.loadViewIfNeeded()

    // Then
    XCTAssertEqual(viewController.loginButton.title, "로그인")
    // ❌ 실패! loginButton이 아직 없음
}
```

**2. Green - 테스트 통과하는 최소 코드**
```swift
class LoginViewController: UIViewController {
    let loginButton: UIButton = {
        let button = UIButton()
        button.setTitle("로그인", for: .normal)
        return button
    }()
}
// ✅ 성공! 테스트 통과
```

**3. Refactor - 코드 개선**
```swift
class LoginViewController: UIViewController {
    private lazy var loginButton: UIButton = {
        let button = UIButton(type: .system)
        button.setTitle("로그인", for: .normal)
        button.titleLabel?.font = .systemFont(ofSize: 16, weight: .bold)
        return button
    }()
}
// ✅ 여전히 성공! 테스트 유지
```

<br><br>

## XCTest 기본 구조

### 테스트 클래스 작성

```swift
import XCTest
@testable import MyApp  // 앱 모듈 접근

class LoginViewModelTests: XCTestCase {

    // 각 테스트 전에 실행
    override func setUp() {
        super.setUp()
        // 초기화 코드
    }

    // 각 테스트 후에 실행
    override func tearDown() {
        // 정리 코드
        super.tearDown()
    }

    // 테스트 메서드 (test로 시작)
    func testExample() {
        // 테스트 코드
    }
}
```

### Given-When-Then 패턴

테스트를 명확하게 구조화하는 패턴:

```swift
func testUserLogin_WithValidCredentials_ReturnsSuccess() {
    // Given (준비): 테스트 조건 설정
    let viewModel = LoginViewModel()
    let email = "test@example.com"
    let password = "password123"

    // When (실행): 테스트할 동작 수행
    let result = viewModel.login(email: email, password: password)

    // Then (검증): 결과 확인
    XCTAssertTrue(result.isSuccess)
    XCTAssertEqual(result.user?.email, email)
}
```

## XCTest Assertion 메서드

### 기본 Assertion
```swift
// 값 비교
XCTAssertEqual(actual, expected)           // 같은지
XCTAssertNotEqual(actual, expected)        // 다른지

// Boolean
XCTAssertTrue(expression)                  // true인지
XCTAssertFalse(expression)                 // false인지

// Nil 체크
XCTAssertNil(expression)                   // nil인지
XCTAssertNotNil(expression)                // nil이 아닌지

// 에러 체크
XCTAssertThrowsError(expression)           // 에러 발생하는지
XCTAssertNoThrow(expression)               // 에러 없는지
```

## iOS TDD 실전 예제

### 예제: 할 일 목록 앱 (Todo App)

#### 1. Model 테스트

```swift
// TodoTests.swift
import XCTest
@testable import TodoApp

class TodoTests: XCTestCase {

    func testTodoCreation() {
        // Given
        let title = "TDD 공부하기"

        // When
        let todo = Todo(title: title)

        // Then
        XCTAssertEqual(todo.title, title)
        XCTAssertFalse(todo.isCompleted)
    }

    func testTodoCompletion() {
        // Given
        var todo = Todo(title: "테스트 작성")

        // When
        todo.complete()

        // Then
        XCTAssertTrue(todo.isCompleted)
    }
}
```

```swift
// Todo.swift (구현)
struct Todo {
    let title: String
    private(set) var isCompleted: Bool = false

    mutating func complete() {
        isCompleted = true
    }
}
```

#### 2. ViewModel 테스트

```swift
// TodoViewModelTests.swift
class TodoViewModelTests: XCTestCase {

    var sut: TodoViewModel!  // SUT: System Under Test

    override func setUp() {
        super.setUp()
        sut = TodoViewModel()
    }

    override func tearDown() {
        sut = nil
        super.tearDown()
    }

    func testAddTodo() {
        // Given
        let title = "새로운 할 일"

        // When
        sut.addTodo(title: title)

        // Then
        XCTAssertEqual(sut.todos.count, 1)
        XCTAssertEqual(sut.todos.first?.title, title)
    }

    func testCompleteTodo() {
        // Given
        sut.addTodo(title: "할 일")
        let index = 0

        // When
        sut.completeTodo(at: index)

        // Then
        XCTAssertTrue(sut.todos[index].isCompleted)
    }

    func testDeleteTodo() {
        // Given
        sut.addTodo(title: "할 일 1")
        sut.addTodo(title: "할 일 2")

        // When
        sut.deleteTodo(at: 0)

        // Then
        XCTAssertEqual(sut.todos.count, 1)
        XCTAssertEqual(sut.todos.first?.title, "할 일 2")
    }
}
```

```swift
// TodoViewModel.swift (구현)
class TodoViewModel {
    private(set) var todos: [Todo] = []

    func addTodo(title: String) {
        let todo = Todo(title: title)
        todos.append(todo)
    }

    func completeTodo(at index: Int) {
        todos[index].complete()
    }

    func deleteTodo(at index: Int) {
        todos.remove(at: index)
    }
}
```

## Test Double (테스트 더블)

Test Double은 테스트를 위해 **실제 객체를 대신하는 가짜 객체**를 말합니다. 영화 촬영에서 위험한 장면을 대신하는 "스턴트 더블"에서 유래한 용어입니다.

### 왜 Test Double이 필요한가?

실제 객체를 사용하면 테스트가 어려운 경우:
- **네트워크 호출**: 실제 API 서버에 의존
- **데이터베이스**: 실제 DB 연결 필요
- **시간/날짜**: 현재 시간에 의존
- **외부 서비스**: 결제, 메일 발송 등

Test Double을 사용하면:
- ✅ 빠른 테스트 (네트워크 없이 즉시 실행)
- ✅ 독립적인 테스트 (외부 환경에 영향 안 받음)
- ✅ 예측 가능한 테스트 (항상 동일한 결과)

### Test Double의 5가지 유형

#### 1. Dummy (더미)
**용도**: 파라미터를 채우기 위해서만 사용. 실제로 사용되지 않음.

```swift
// 테스트에서 파라미터가 필요하지만 실제로는 안 쓰이는 경우
func testUserCreation() {
    let dummyEmail = "dummy@test.com"  // 실제로 검증 안 함
    let user = User(name: "Test", email: dummyEmail)
    XCTAssertEqual(user.name, "Test")
}
```

**특징:**
- 가장 단순한 형태
- 메서드가 호출되어도 아무것도 하지 않음
- 파라미터 자리 채우기용

#### 2. Stub (스텁)
**용도**: **미리 준비된 답변을 제공**. 특정 입력에 대해 고정된 값을 반환.

```swift
// Stub: 항상 같은 데이터 반환
class StubTodoService: TodoServiceProtocol {
    var todosToReturn: [Todo] = []  // 미리 설정한 데이터

    func fetchTodos(completion: @escaping ([Todo]) -> Void) {
        completion(todosToReturn)  // 고정된 값 반환
    }
}

// 사용 예
func testViewModel_LoadsStubData() {
    let stub = StubTodoService()
    stub.todosToReturn = [Todo(title: "테스트")]  // 반환값 미리 설정

    let viewModel = TodoViewModel(service: stub)
    viewModel.fetchTodos()

    XCTAssertEqual(viewModel.todos.count, 1)
}
```

**특징:**
- 질문(Query)에 대한 답변 제공
- 호출 여부는 검증하지 않음
- "이 메서드 호출하면 이 값 돌려줘" 역할

#### 3. Spy (스파이)
**용도**: **메서드 호출을 기록**. 어떤 메서드가 몇 번, 어떤 인자로 호출되었는지 추적.

```swift
// Spy: 호출 정보를 기록
class SpyTodoService: TodoServiceProtocol {
    var fetchTodosCallCount = 0  // 호출 횟수 기록
    var lastCompletionHandler: (([Todo]) -> Void)?  // 마지막 호출 파라미터 기록

    func fetchTodos(completion: @escaping ([Todo]) -> Void) {
        fetchTodosCallCount += 1  // 호출 기록
        lastCompletionHandler = completion
        completion([])
    }
}

// 사용 예
func testViewModel_CallsFetchTodosOnce() {
    let spy = SpyTodoService()
    let viewModel = TodoViewModel(service: spy)

    viewModel.refreshData()

    XCTAssertEqual(spy.fetchTodosCallCount, 1)  // 1번 호출되었는지 검증
}
```

**특징:**
- 호출 여부, 횟수, 파라미터를 기록
- Stub 기능 + 검증 기능
- "이 메서드가 실제로 불렸나?" 확인용

#### 4. Mock (목)
**용도**: **예상되는 호출을 검증**. 특정 메서드가 특정 방식으로 호출되었는지 확인.

```swift
// Mock: 기대값 설정 + 검증
class MockTodoService: TodoServiceProtocol {
    var expectedFetchCount = 0
    var actualFetchCount = 0

    func fetchTodos(completion: @escaping ([Todo]) -> Void) {
        actualFetchCount += 1
        completion([])
    }

    func verify() {
        assert(actualFetchCount == expectedFetchCount,
               "Expected \(expectedFetchCount) calls, but got \(actualFetchCount)")
    }
}

// 사용 예
func testViewModel_FetchesExactlyOnce() {
    let mock = MockTodoService()
    mock.expectedFetchCount = 1  // 기대값 설정

    let viewModel = TodoViewModel(service: mock)
    viewModel.loadData()

    mock.verify()  // Mock이 스스로 검증
}
```

**특징:**
- 기대값(expectation)을 미리 설정
- 자체적으로 검증(verify) 기능 포함
- Spy보다 더 엄격한 검증
- "이 메서드가 정확히 N번, 이런 인자로 불려야 해" 검증

#### 5. Fake (페이크)
**용도**: **실제로 동작하는 구현체**. 단, 프로덕션에는 부적합한 간단한 구현.

```swift
// Fake: 실제 동작하지만 간소화된 버전
class FakeTodoRepository: TodoRepositoryProtocol {
    private var todos: [Todo] = []  // 실제 DB 대신 메모리 사용

    func save(_ todo: Todo) {
        todos.append(todo)  // 실제로 저장 동작
    }

    func findAll() -> [Todo] {
        return todos  // 실제로 조회 동작
    }

    func delete(_ id: String) {
        todos.removeAll { $0.id == id }  // 실제로 삭제 동작
    }
}

// 사용 예
func testRepository_SaveAndRetrieve() {
    let fake = FakeTodoRepository()  // 실제 DB 대신 메모리 DB

    fake.save(Todo(title: "할 일"))
    let todos = fake.findAll()

    XCTAssertEqual(todos.count, 1)
}
```

**특징:**
- 실제 동작하는 구현 (In-Memory DB 등)
- 프로덕션용보다 단순함
- 복잡한 설정 없이 빠르게 테스트

### Test Double 비교표

| 유형 | 답변 제공 | 호출 기록 | 검증 기능 | 실제 동작 | 주 용도 |
|------|----------|----------|----------|----------|---------|
| **Dummy** | ❌ | ❌ | ❌ | ❌ | 파라미터 채우기 |
| **Stub** | ✅ | ❌ | ❌ | ❌ | 고정 데이터 반환 |
| **Spy** | ✅ | ✅ | ❌ | ❌ | 호출 여부 추적 |
| **Mock** | ✅ | ✅ | ✅ | ❌ | 엄격한 검증 |
| **Fake** | ✅ | ❌ | ❌ | ✅ | 간소화된 실제 구현 |

### 언제 무엇을 사용할까?

```swift
// Stub 사용: "이 API 호출하면 성공 데이터 주세요"
let stub = StubNetworkService()
stub.responseData = successData
viewModel.fetchData()

// Spy 사용: "이 메서드가 호출되었나요?"
let spy = SpyAnalytics()
button.tap()
XCTAssertTrue(spy.trackEventCalled)

// Mock 사용: "이 메서드가 정확히 1번, 이 파라미터로 불려야 해"
let mock = MockPaymentService()
mock.expect(method: "processPayment", times: 1, with: 10000)
checkout.pay()
mock.verify()

// Fake 사용: "실제 DB 대신 메모리 DB로 테스트"
let fake = FakeUserRepository()
fake.save(user)
let found = fake.findById(user.id)
```

**실무 팁:**
- 대부분의 경우 **Stub + Spy 조합**이면 충분
- Mock은 너무 엄격해서 테스트가 깨지기 쉬움
- Fake는 초기 설정 비용이 있지만 재사용 가치 높음

### iOS에서 자주 사용하는 예시

```swift
// 1. 네트워크: Stub 사용
class StubAPIClient: APIClientProtocol {
    var jsonToReturn: String = "{}"
    func request(url: URL) async -> Data {
        return jsonToReturn.data(using: .utf8)!
    }
}

// 2. Analytics: Spy 사용
class SpyAnalyticsTracker: AnalyticsProtocol {
    var trackedEvents: [String] = []
    func track(event: String) {
        trackedEvents.append(event)
    }
}

// 3. UserDefaults: Fake 사용
class FakeUserDefaults: UserDefaultsProtocol {
    private var storage: [String: Any] = [:]
    func set(_ value: Any, forKey key: String) {
        storage[key] = value
    }
    func object(forKey key: String) -> Any? {
        return storage[key]
    }
}
```

### Mock, Stub, Spy 활용 예제

#### Stub 예제: 네트워크 요청 테스트

```swift
// 프로토콜 정의
protocol TodoServiceProtocol {
    func fetchTodos(completion: @escaping ([Todo]) -> Void)
}

// Mock 객체
class MockTodoService: TodoServiceProtocol {
    var fetchTodosCalled = false
    var todosToReturn: [Todo] = []

    func fetchTodos(completion: @escaping ([Todo]) -> Void) {
        fetchTodosCalled = true
        completion(todosToReturn)
    }
}

// 테스트
class TodoViewModelNetworkTests: XCTestCase {

    func testFetchTodos() {
        // Given
        let mockService = MockTodoService()
        mockService.todosToReturn = [
            Todo(title: "테스트 1"),
            Todo(title: "테스트 2")
        ]
        let viewModel = TodoViewModel(service: mockService)

        // When
        viewModel.fetchTodos()

        // Then
        XCTAssertTrue(mockService.fetchTodosCalled)
        XCTAssertEqual(viewModel.todos.count, 2)
    }
}
```

#### Spy: 델리게이트 테스트

```swift
// Spy 객체
class SpyTodoViewDelegate: TodoViewDelegate {
    var didUpdateTodosCalled = false
    var receivedTodos: [Todo] = []

    func didUpdateTodos(_ todos: [Todo]) {
        didUpdateTodosCalled = true
        receivedTodos = todos
    }
}

// 테스트
func testViewModelNotifiesDelegate() {
    // Given
    let viewModel = TodoViewModel()
    let spy = SpyTodoViewDelegate()
    viewModel.delegate = spy

    // When
    viewModel.addTodo(title: "새 할 일")

    // Then
    XCTAssertTrue(spy.didUpdateTodosCalled)
    XCTAssertEqual(spy.receivedTodos.count, 1)
}
```

## 비동기 테스트

### XCTestExpectation 사용

```swift
func testAsyncFetchTodos() {
    // Given
    let expectation = expectation(description: "Fetch todos")
    let viewModel = TodoViewModel()

    // When
    viewModel.fetchTodos { todos in
        // Then
        XCTAssertEqual(todos.count, 3)
        expectation.fulfill()
    }

    // Wait for async operation
    wait(for: [expectation], timeout: 5.0)
}
```

### Async/Await 테스트 (iOS 15+)

```swift
func testAsyncAwaitFetch() async throws {
    // Given
    let viewModel = TodoViewModel()

    // When
    let todos = try await viewModel.fetchTodos()

    // Then
    XCTAssertEqual(todos.count, 3)
}
```

## TDD의 장점

1. **버그 감소**
   - 코드 작성 전 테스트로 요구사항 명확화
   - 리팩토링 시 기존 기능 보호

2. **설계 개선**
   - 테스트 가능한 코드 = 좋은 설계
   - 의존성 주입, 단일 책임 원칙 자연스럽게 적용

3. **문서화 효과**
   - 테스트 코드가 사용 예제이자 문서
   - 코드의 의도와 동작 명확히 전달

4. **리팩토링 안정성**
   - 테스트가 안전망 역할
   - 자신감 있게 코드 개선 가능

5. **빠른 피드백**
   - 문제를 즉시 발견
   - 디버깅 시간 절약

## TDD의 단점

1. **초기 시간 투자**
   - 테스트 작성 시간 필요
   - 학습 곡선 존재

2. **UI 테스트 어려움**
   - UIViewController 테스트 복잡
   - → MVVM, MVP 패턴으로 해결

3. **과도한 테스트**
   - 사소한 것까지 테스트하면 유지보수 부담

## TDD 베스트 프랙티스 (iOS)

### 1. MVVM/MVP 패턴 사용
```swift
// ViewModel을 테스트하기 쉽게 분리
class LoginViewModel {
    func login(email: String, password: String) -> Bool {
        // 비즈니스 로직 (테스트 쉬움)
    }
}

// ViewController는 UI만 담당
class LoginViewController: UIViewController {
    private let viewModel = LoginViewModel()

    @IBAction func loginButtonTapped() {
        let result = viewModel.login(
            email: emailTextField.text ?? "",
            password: passwordTextField.text ?? ""
        )
        // UI 업데이트
    }
}
```

### 2. 의존성 주입 (Dependency Injection)
```swift
// Bad: 직접 생성 (테스트 어려움)
class TodoViewModel {
    let service = TodoService()  // 고정됨
}

// Good: 주입 (테스트 쉬움)
class TodoViewModel {
    let service: TodoServiceProtocol

    init(service: TodoServiceProtocol = TodoService()) {
        self.service = service
    }
}

// 테스트에서 Mock 주입 가능
let viewModel = TodoViewModel(service: MockTodoService())
```

### 3. 테스트 이름 규칙
```swift
// 패턴: test[테스트대상]_[조건]_[예상결과]
func testLogin_WithValidCredentials_ReturnsSuccess() { }
func testLogin_WithInvalidPassword_ReturnsError() { }
func testAddTodo_WithEmptyTitle_DoesNotAddTodo() { }
```

### 4. 한 테스트는 한 가지만 검증
```swift
// Bad: 여러 가지 검증
func testTodoOperations() {
    sut.addTodo(title: "할 일")
    XCTAssertEqual(sut.todos.count, 1)  // 추가 검증

    sut.completeTodo(at: 0)
    XCTAssertTrue(sut.todos[0].isCompleted)  // 완료 검증
}

// Good: 분리
func testAddTodo_IncreasesTodosCount() {
    sut.addTodo(title: "할 일")
    XCTAssertEqual(sut.todos.count, 1)
}

func testCompleteTodo_SetsIsCompletedToTrue() {
    sut.addTodo(title: "할 일")
    sut.completeTodo(at: 0)
    XCTAssertTrue(sut.todos[0].isCompleted)
}
```

## iOS TDD 핵심 원칙

### 1. Unit Test부터 연습하고 TDD를 숙련한다

TDD는 테스트 작성 능력이 전제되어야 합니다. 먼저 기존 코드에 Unit Test를 작성하는 연습을 하세요.

```swift
// 1단계: 기존 함수에 테스트 작성 연습
class Calculator {
    func add(_ a: Int, _ b: Int) -> Int {
        return a + b
    }
}

// 테스트 작성 연습
func testAdd() {
    let calculator = Calculator()
    XCTAssertEqual(calculator.add(2, 3), 5)
}

// 2단계: 익숙해지면 TDD로 전환 (테스트 먼저 작성)
```

### 2. 외부 세계와의 접점에는 Mock을 활용한다

네트워크, 데이터베이스, UserDefaults 등 외부 의존성은 Mock으로 대체합니다.

```swift
// 외부 의존성: 네트워크
protocol NetworkService {
    func fetchData() async throws -> Data
}

// Mock으로 대체
class MockNetworkService: NetworkService {
    var dataToReturn: Data = Data()
    func fetchData() async throws -> Data {
        return dataToReturn
    }
}

// 테스트에서 Mock 사용
func testViewModel() async throws {
    let mock = MockNetworkService()
    mock.dataToReturn = "test".data(using: .utf8)!
    let viewModel = MyViewModel(networkService: mock)

    await viewModel.loadData()
    XCTAssertEqual(viewModel.items.count, 1)
}
```

### 3. Internal 구현체도 테스트에 활용할 수 있다

`@testable import`를 사용하면 `internal` 접근 제어자도 테스트에서 접근 가능합니다.

```swift
// MyApp 모듈
class InternalHelper {
    func processData(_ input: String) -> String {  // internal (기본)
        return input.uppercased()
    }
}

// 테스트
@testable import MyApp

func testInternalHelper() {
    let helper = InternalHelper()
    XCTAssertEqual(helper.processData("hello"), "HELLO")
}
```

### 4. 뷰 테스트는 상태에 따라 변하는 값을 테스트한다

UI 레이아웃은 테스트하지 않고, **상태 변화에 따른 UI 업데이트**를 테스트합니다.

```swift
class ProfileViewController: UIViewController {
    @IBOutlet weak var nameLabel: UILabel!
    @IBOutlet weak var logoutButton: UIButton!

    var isLoggedIn: Bool = false {
        didSet { updateUI() }
    }

    private func updateUI() {
        logoutButton.isHidden = !isLoggedIn
        nameLabel.text = isLoggedIn ? "사용자" : "로그인 필요"
    }
}

// 테스트: 상태에 따른 UI 변화
func testLoginState_UpdatesUI() {
    let vc = ProfileViewController()
    vc.loadViewIfNeeded()

    // 로그아웃 상태
    vc.isLoggedIn = false
    XCTAssertTrue(vc.logoutButton.isHidden)
    XCTAssertEqual(vc.nameLabel.text, "로그인 필요")

    // 로그인 상태
    vc.isLoggedIn = true
    XCTAssertFalse(vc.logoutButton.isHidden)
    XCTAssertEqual(vc.nameLabel.text, "사용자")
}
```

### 5. private 메서드는 만들기 전에 테스트되고 있어야 한다

`private` 메서드는 직접 테스트할 수 없습니다. 따라서 **public 메서드를 통해 간접적으로 테스트**되어야 합니다.

```swift
class UserValidator {
    // public 메서드 (테스트 대상)
    func isValid(email: String, password: String) -> Bool {
        return isValidEmail(email) && isValidPassword(password)
    }

    // private 메서드 (직접 테스트 불가)
    private func isValidEmail(_ email: String) -> Bool {
        return email.contains("@")
    }

    private func isValidPassword(_ password: String) -> Bool {
        return password.count >= 8
    }
}

// 테스트: public 메서드를 통해 private 메서드도 검증
func testIsValid_WithValidCredentials_ReturnsTrue() {
    let validator = UserValidator()
    XCTAssertTrue(validator.isValid(email: "test@test.com", password: "12345678"))
    // private 메서드도 함께 테스트됨
}

func testIsValid_WithInvalidEmail_ReturnsFalse() {
    let validator = UserValidator()
    XCTAssertFalse(validator.isValid(email: "invalid", password: "12345678"))
    // isValidEmail이 간접적으로 테스트됨
}
```

### 6. TDD로만 모든 코드를 작성하지는 않는다

TDD는 도구입니다. 상황에 맞게 선택적으로 사용하세요.

**TDD가 유용한 경우:**
- 비즈니스 로직이 복잡한 경우
- 요구사항이 명확한 경우
- 리팩토링이 잦은 핵심 기능

**TDD를 건너뛰어도 되는 경우:**
- UI 프로토타입 단계
- 간단한 화면 전환
- 일회성 스크립트
- 빠른 검증이 필요한 실험적 기능

```swift
// TDD 적용 ✅: 복잡한 비즈니스 로직
class PaymentCalculator {
    func calculateTotal(items: [Item], discount: Discount?) -> Int {
        // 테스트 먼저 작성 후 구현
    }
}

// TDD 건너뛰기 ⏭️: 간단한 화면 전환
func navigateToDetail() {
    let vc = DetailViewController()
    navigationController?.pushViewController(vc, animated: true)
}
```

### 7. Cocoa Framework의 작동 방식을 다양하게 알아둔다

iOS 테스트를 위해서는 Cocoa Framework의 생명주기와 동작을 이해해야 합니다.

**알아두면 좋은 것들:**

```swift
// 1. ViewController 생명주기
func testViewController() {
    let vc = MyViewController()
    vc.loadViewIfNeeded()  // viewDidLoad() 호출
    // ⚠️ loadView() 없이 바로 vc.view 접근하면 무한 루프 가능

    vc.viewWillAppear(false)
    vc.viewDidAppear(false)
}

// 2. Notification 테스트
func testNotificationObserver() {
    let expectation = expectation(description: "Notification")

    NotificationCenter.default.addObserver(
        forName: .myNotification,
        object: nil,
        queue: .main
    ) { _ in
        expectation.fulfill()
    }

    NotificationCenter.default.post(name: .myNotification, object: nil)
    wait(for: [expectation], timeout: 1.0)
}

// 3. UserDefaults 테스트 (별도 suite 사용)
func testUserDefaults() {
    let defaults = UserDefaults(suiteName: "TestSuite")!
    defaults.set("test", forKey: "key")
    XCTAssertEqual(defaults.string(forKey: "key"), "test")
    defaults.removePersistentDomain(forName: "TestSuite")  // 정리
}

// 4. Main Thread 검증
func testMainThread() {
    sut.updateUI()
    XCTAssertTrue(Thread.isMainThread)
}
```

### 8. AppDelegate도 테스트할 수 있다

AppDelegate의 로직도 분리하여 테스트할 수 있습니다.

```swift
// AppDelegate 로직 분리
class AppCoordinator {
    func configureInitialSettings() {
        // 초기 설정 로직
        UserDefaults.standard.register(defaults: ["theme": "light"])
    }

    func handleRemoteNotification(_ userInfo: [AnyHashable: Any]) -> Bool {
        // 푸시 알림 처리 로직
        guard let type = userInfo["type"] as? String else { return false }
        return type == "message"
    }
}

@main
class AppDelegate: UIResponder, UIApplicationDelegate {
    let coordinator = AppCoordinator()

    func application(_ application: UIApplication,
                     didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        coordinator.configureInitialSettings()
        return true
    }
}

// AppCoordinator 테스트
class AppCoordinatorTests: XCTestCase {
    var sut: AppCoordinator!

    override func setUp() {
        super.setUp()
        sut = AppCoordinator()
    }

    func testConfigureInitialSettings() {
        sut.configureInitialSettings()
        XCTAssertEqual(UserDefaults.standard.string(forKey: "theme"), "light")
    }

    func testHandleRemoteNotification_WithValidType_ReturnsTrue() {
        let userInfo: [AnyHashable: Any] = ["type": "message"]
        XCTAssertTrue(sut.handleRemoteNotification(userInfo))
    }

    func testHandleRemoteNotification_WithInvalidType_ReturnsFalse() {
        let userInfo: [AnyHashable: Any] = ["type": "unknown"]
        XCTAssertFalse(sut.handleRemoteNotification(userInfo))
    }
}
```

## 레거시 코드를 TDD로 전환하기

기존 프로젝트에 TDD를 도입할 때는 점진적 접근이 필요합니다.

### 1. Deprecated를 활용한 점진적 마이그레이션

기존 코드를 한번에 바꾸지 말고, 새 인터페이스를 만들고 기존 코드를 deprecated 처리합니다.

```swift
// 기존 코드 (테스트 불가능한 static 메서드)
class GitHubService {
    @available(*, deprecated, message: "Use init(sessionManager:) instead")
    static func search(keyword: String, completion: @escaping ([Repository]) -> Void) {
        // SessionManager.default에 강하게 결합됨
        SessionManager.default.request(...)
    }
}

// 새 코드 (테스트 가능한 인스턴스 메서드)
class GitHubService {
    private let sessionManager: SessionManagerProtocol

    init(sessionManager: SessionManagerProtocol = SessionManager.default) {
        self.sessionManager = sessionManager
    }

    func search(keyword: String, completion: @escaping ([Repository]) -> Void) {
        sessionManager.request(...)
    }
}
```

**마이그레이션 단계:**
1. 테스트 가능한 새 인터페이스 작성
2. 기존 메서드에 `@available(*, deprecated)` 추가
3. 새 코드부터 테스트 작성
4. 점진적으로 호출부 변경
5. 모두 전환 후 deprecated 코드 삭제

### 2. 작은 단위부터 시작

레거시 프로젝트에서는 한번에 모든 것을 테스트하려 하지 말고:

```swift
// ❌ 처음부터 전체 ViewController 테스트 시도
func testEntireViewController() { ... }

// ✅ 작은 유틸리티 함수부터 시작
func testDateFormatter() {
    let formatter = DateFormatter.iso8601
    XCTAssertEqual(formatter.string(from: date), "2024-01-01")
}

// ✅ 점진적으로 확장
func testViewModel_FetchData() { ... }
func testViewController_UpdateUI() { ... }
```

## TDD의 팀 협업 가치

### 1. 주니어 개발자 실수 방지

테스트가 있으면 경험이 적은 개발자도 안전하게 코드를 수정할 수 있습니다.

```swift
// 테스트가 API 호출 실수를 방지
func testSearchService_SendsCorrectAPIRequest() {
    // Given
    let stub = SessionManagerStub()
    let service = GitHubService(sessionManager: stub)

    // When
    service.search(keyword: "swift")

    // Then
    XCTAssertEqual(stub.requestedURL, "https://api.github.com/search/repositories")
    XCTAssertEqual(stub.requestedParams["q"], "swift")
    // ⚠️ 주니어가 잘못된 URL을 넣으면 테스트 실패!
}
```

**실무 사례:**
- 잘못된 API 엔드포인트 사용 → 테스트가 바로 감지
- 파라미터 오타 → 테스트 실패로 즉시 발견
- 인증 토큰 누락 → 테스트에서 검증

### 2. 코드 리뷰 효율 향상

```swift
// PR에 테스트가 함께 제출되면:
// 1. 리뷰어가 의도를 명확히 이해
// 2. 엣지 케이스 확인 가능
// 3. 리뷰 시간 단축

func testPayment_WithZeroAmount_ThrowsError() {
    // 리뷰어: "아, 0원 결제는 에러 처리하는구나"
    XCTAssertThrowsError(try payment.process(amount: 0))
}
```

### 3. 리팩토링 안전성

```swift
// 팀원이 성능 개선을 위해 코드를 대폭 수정
// 기존 테스트가 모두 통과하면 → 안전하게 머지 가능

// Before: O(n²) 알고리즘
func findDuplicates(in array: [Int]) -> [Int] { ... }

// After: O(n) 알고리즘으로 개선
func findDuplicates(in array: [Int]) -> [Int] { ... }

// 테스트는 동일 - 결과만 검증
func testFindDuplicates() {
    XCTAssertEqual(findDuplicates(in: [1,2,2,3]), [2])
    // ✅ 구현이 바뀌어도 테스트 통과
}
```

## TDD 실무 적용 팁

### 1. 모든 코드를 테스트하지 마라
- **테스트할 것**: 비즈니스 로직, 계산, 데이터 변환
- **테스트 안 해도 됨**: UI 레이아웃, 애니메이션, 단순 getter/setter

### 2. 테스트하기 쉬운 구조로 설계
```swift
// View와 로직 분리
// ✅ ViewModel (테스트 쉬움)
// ❌ ViewController (테스트 어려움)
```

### 3. 빠른 테스트 유지
- 네트워크 요청은 Mock
- 데이터베이스는 In-Memory
- 테스트는 1초 이내

### 4. 테스트 실패 시 즉시 수정
```swift
// ❌ 나중에 고치려고 주석 처리
// func testFeatureX() { ... }

// ✅ 실패 원인 파악 후 즉시 수정
func testFeatureX() {
    // 실패하면 바로 고치거나 구현 변경
}
```

### 5. CI/CD에서 자동 실행
```bash
# Xcode 명령어로 테스트 자동화
xcodebuild test -scheme MyApp -destination 'platform=iOS Simulator,name=iPhone 15'

# GitHub Actions 예시
# - PR 생성 시 자동 테스트
# - 테스트 실패하면 머지 차단
```

### 6. 코드 커버리지 활용 (단, 맹신하지 말 것)

```
코드 커버리지 80% = 좋은 테스트? ❌
커버리지는 참고만 하고, 의미 있는 테스트 작성이 우선

✅ 좋은 테스트: 엣지 케이스, 에러 처리 검증
❌ 나쁜 테스트: 커버리지만 채우려고 작성한 테스트
```

## 참고 자료

### 도서
- Test Driven Development (Kent Beck)
- Growing Object-Oriented Software, Guided by Tests

### iOS 관련
- [Apple: Testing Documentation](https://developer.apple.com/documentation/xctest)
- [WWDC: Testing in Xcode](https://developer.apple.com/videos/play/wwdc2019/413/)

### 한국어 자료
- [Let's TDD - 전수열 (Let's Swift 2018)](https://www.youtube.com/watch?v=meTnd09Pf_M)
  - iOS TDD 실전 워크샵 강연
  - Git Search 앱 라이브 코딩
- [Let's TDD 정리 블로그](https://velog.io/@alwaysblu/Lets-TDD-%EC%A0%84%EC%88%98%EC%97%B4-%EB%8B%98)

### 관련 문서
- [Testable한 코드 만들기 (MVC → MVP)](../../Mobile_01_iOS/iOS-TDD/testable_mvc_mvp.md)
- [Clean Code](../../CodeQuality/clean_code.md)
- [SOLID 원칙](../../CodeQuality/solid_principles.md)

## 핵심 요약

1. **Red-Green-Refactor** 사이클 지키기
2. **Given-When-Then** 패턴으로 명확한 테스트 작성
3. **작은 단계로** 진행하기
4. **MVVM/MVP** 패턴으로 테스트 가능한 구조 만들기
5. **의존성 주입**으로 Mock 객체 활용
6. **빠른 피드백**이 핵심

**TDD는 완벽한 테스트가 아니라, 더 나은 설계와 안정적인 코드를 위한 도구입니다!**
