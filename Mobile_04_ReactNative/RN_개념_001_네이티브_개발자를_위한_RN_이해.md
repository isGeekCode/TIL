# RN_개념_001_네이티브_개발자를_위한_RN_이해

## 🤔 이 문서를 읽기 전에
- **대상 독자**: iOS(Swift) 또는 Android(Kotlin) 경험자
- **예상 소요 시간**: 30분
- **난이도**: 🟢 입문 (네이티브 → RN 전환)

## 🎯 이 문서에서 배울 것
1. React Native는 왜 클래스가 없나?
2. useState는 전역 변수인가?
3. ViewController/Activity는 어디 갔나?
4. 생명주기는 어떻게 관리하나?
5. 네이티브 개념과 RN 개념 1:1 매핑

---

## 📖 본문

### 1. "클래스가 없다고?" - 함수형 vs 객체지향

#### iOS(Swift) 코드
```swift
// UIViewController - 클래스 기반
class WebViewController: UIViewController {
    // 프로퍼티 (상태)
    var isLoading: Bool = true
    var errorMessage: String? = nil
    var webView: WKWebView!

    // 생명주기
    override func viewDidLoad() {
        super.viewDidLoad()
        setupWebView()
        loadURL()
    }

    // 메서드
    func loadURL() {
        webView.load(URLRequest(url: URL(string: "https://example.com")!))
    }

    func handleError(message: String) {
        self.errorMessage = message
        showAlert()
    }
}
```

#### Android(Kotlin) 코드
```kotlin
// Activity - 클래스 기반
class WebActivity : AppCompatActivity() {
    // 프로퍼티 (상태)
    private var isLoading: Boolean = true
    private var errorMessage: String? = null
    private lateinit var webView: WebView

    // 생명주기
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_web)
        setupWebView()
        loadURL()
    }

    // 메서드
    private fun loadURL() {
        webView.loadUrl("https://example.com")
    }

    private fun handleError(message: String) {
        this.errorMessage = message
        showAlert()
    }
}
```

#### React Native 코드 (함수형)
```typescript
// 함수 컴포넌트 - 클래스 없음!
function WebShell() {
    // 상태 (클래스 프로퍼티 대신 Hooks)
    const [isLoading, setIsLoading] = useState(true);
    const [errorMessage, setErrorMessage] = useState<string | null>(null);
    const webViewRef = useRef<WebView>(null);

    // 생명주기 (useEffect)
    useEffect(() => {
        // viewDidLoad() / onCreate() 역할
        loadURL();
    }, []);

    // 함수
    const loadURL = () => {
        // WebView 로딩 로직
    };

    const handleError = (message: string) => {
        setErrorMessage(message);
        showAlert();
    };

    // UI 반환 (render 메서드 대신)
    return (
        <WebView
            ref={webViewRef}
            source={{ uri: 'https://example.com' }}
        />
    );
}
```

---

### 2. 핵심 개념 비교표

| 개념 | iOS (Swift) | Android (Kotlin) | React Native |
|------|-------------|------------------|--------------|
| **화면 단위** | `UIViewController` | `Activity` / `Fragment` | 함수 컴포넌트 (function) |
| **상태 저장** | 클래스 프로퍼티 (`var isLoading`) | 클래스 프로퍼티 (`private var isLoading`) | `useState(false)` |
| **참조 보관** | 프로퍼티 (`var webView: WKWebView!`) | 프로퍼티 (`lateinit var webView`) | `useRef<WebView>(null)` |
| **생명주기** | `viewDidLoad()`, `viewWillAppear()` | `onCreate()`, `onResume()` | `useEffect(() => {}, [])` |
| **UI 정의** | Storyboard 또는 코드 | XML 또는 Compose | JSX (return 문) |
| **비동기 처리** | `async/await` | `suspend fun` / Coroutines | `async/await` (동일) |

---

### 3. "useState는 전역인가?" - 상태 관리 이해

#### 오해: useState가 전역처럼 보이는 이유

```typescript
// ❓ 이게 전역 변수 같아 보임
const [count, setCount] = useState(0);

// Swift로 치면 이렇게 보임
var count: Int = 0  // 전역 변수?
```

**실제로는:**
```typescript
// React가 내부적으로 하는 일 (단순화)
const componentStates = new Map();  // React 내부 저장소

function useState(initialValue) {
    const componentId = getCurrentComponentId();  // 컴포넌트마다 고유 ID

    if (!componentStates.has(componentId)) {
        componentStates.set(componentId, initialValue);
    }

    const state = componentStates.get(componentId);
    const setState = (newValue) => {
        componentStates.set(componentId, newValue);
        reRenderComponent();  // 다시 렌더링
    };

    return [state, setState];
}
```

**네이티브 비유:**
```swift
// Swift - 클래스 프로퍼티
class MyViewController: UIViewController {
    var count: Int = 0  // 이 ViewController 인스턴스에만 속함
}

// React Native - useState
function MyComponent() {
    const [count, setCount] = useState(0);  // 이 컴포넌트 인스턴스에만 속함
}
```

**핵심:**
- ✅ useState는 **컴포넌트 인스턴스마다 독립적**
- ✅ 클래스 프로퍼티처럼 작동 (전역 아님!)
- ✅ React가 내부적으로 관리 (개발자는 몰라도 됨)

---

### 4. 생명주기 비교

#### iOS (UIViewController)

```swift
class MyViewController: UIViewController {
    override func viewDidLoad() {
        // 뷰가 메모리에 로드됨 (최초 1회)
        setupUI()
    }

    override func viewWillAppear(_ animated: Bool) {
        // 화면에 나타나기 직전 (매번)
        loadData()
    }

    override func viewDidAppear(_ animated: Bool) {
        // 화면에 완전히 나타남 (매번)
        startAnimation()
    }

    override func viewWillDisappear(_ animated: Bool) {
        // 화면에서 사라지기 직전
        pauseAnimation()
    }

    deinit {
        // 메모리에서 해제
        cleanup()
    }
}
```

#### Android (Activity)

```kotlin
class MyActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        // 액티비티 생성 (최초 1회)
        setupUI()
    }

    override fun onStart() {
        // 화면에 보이기 시작
        loadData()
    }

    override fun onResume() {
        // 사용자와 상호작용 시작
        startAnimation()
    }

    override fun onPause() {
        // 사용자와 상호작용 중지
        pauseAnimation()
    }

    override fun onDestroy() {
        // 액티비티 파괴
        cleanup()
    }
}
```

#### React Native (useEffect)

```typescript
function MyComponent() {
    // 1. 컴포넌트 마운트 (viewDidLoad / onCreate)
    useEffect(() => {
        console.log('컴포넌트 마운트됨');
        setupUI();

        // 5. 컴포넌트 언마운트 (deinit / onDestroy)
        return () => {
            console.log('컴포넌트 언마운트됨');
            cleanup();
        };
    }, []);  // 빈 배열 = 최초 1회만

    // 2. 특정 상태 변경 시 (매번)
    useEffect(() => {
        console.log('데이터 변경됨:', data);
        loadData();
    }, [data]);  // data 변경될 때마다

    // 3. 매 렌더링마다 (거의 안 씀)
    useEffect(() => {
        console.log('렌더링됨');
    });  // 의존성 배열 없음

    return <View>...</View>;
}
```

#### 생명주기 비교 도표

```
iOS/Android                React Native (useEffect)
──────────────────────────────────────────────────
viewDidLoad/onCreate  →    useEffect(() => {}, [])  // 마운트

viewWillAppear        →    useEffect(() => {}, [의존성])
onResume                   // 의존성 변경 시

viewWillDisappear     →    return () => {}  // 클린업
onPause

deinit/onDestroy      →    return () => {}  // 언마운트
```

---

### 5. 실제 코드 비교: WebView 구현

#### iOS (Swift)

```swift
class WebViewController: UIViewController, WKNavigationDelegate {
    // 1. 프로퍼티
    private var webView: WKWebView!
    private var isLoading: Bool = true
    private var currentURL: String = ""

    // 2. 생명주기
    override func viewDidLoad() {
        super.viewDidLoad()
        setupWebView()
        loadURL("https://example.com")
    }

    // 3. 메서드
    private func setupWebView() {
        let config = WKWebViewConfiguration()
        webView = WKWebView(frame: .zero, configuration: config)
        webView.navigationDelegate = self
        view.addSubview(webView)
    }

    private func loadURL(_ urlString: String) {
        guard let url = URL(string: urlString) else { return }
        webView.load(URLRequest(url: url))
    }

    // 4. 델리게이트
    func webView(_ webView: WKWebView, didStartProvisionalNavigation navigation: WKNavigation!) {
        isLoading = true
        showLoadingIndicator()
    }

    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        isLoading = false
        hideLoadingIndicator()
    }

    func webView(_ webView: WKWebView, didFail navigation: WKNavigation!, withError error: Error) {
        handleError(error.localizedDescription)
    }
}
```

#### React Native

```typescript
function WebShell() {
    // 1. 상태 (프로퍼티 대신)
    const webViewRef = useRef<WebView>(null);
    const [isLoading, setIsLoading] = useState(true);
    const [currentURL, setCurrentURL] = useState('');

    // 2. 생명주기 (viewDidLoad 대신)
    useEffect(() => {
        // 초기 설정
        console.log('WebShell 마운트됨');

        return () => {
            // 정리
            console.log('WebShell 언마운트됨');
        };
    }, []);

    // 3. 함수 (메서드 대신)
    const handleLoadStart = () => {
        setIsLoading(true);
        // showLoadingIndicator();
    };

    const handleLoadEnd = () => {
        setIsLoading(false);
        // hideLoadingIndicator();
    };

    const handleError = (error: any) => {
        console.error('WebView 에러:', error);
        // 에러 처리
    };

    // 4. UI 반환 (뷰 구성 대신)
    return (
        <View style={{ flex: 1 }}>
            <WebView
                ref={webViewRef}
                source={{ uri: 'https://example.com' }}
                onLoadStart={handleLoadStart}      // didStartProvisionalNavigation
                onLoadEnd={handleLoadEnd}          // didFinish
                onError={handleError}               // didFail
            />
            {isLoading && <ActivityIndicator />}
        </View>
    );
}
```

---

### 6. "이상한" 점들 해명

#### Q1. 왜 함수인데 상태를 유지하나?

```typescript
function MyComponent() {
    const [count, setCount] = useState(0);  // 함수가 끝나도 사라지지 않음!

    return <Text>{count}</Text>;
}
```

**답:**
- React가 함수 외부(Fiber 트리)에 상태 저장
- 함수는 "UI를 그리는 템플릿"일 뿐
- 실제 상태는 React 내부에 보관

**네이티브 비유:**
```swift
// Swift - 클래스 인스턴스가 상태 보관
let vc = MyViewController()  // 인스턴스 생성
vc.count = 5  // 인스턴스에 저장

// React - React 엔진이 상태 보관
<MyComponent />  // React가 내부적으로 인스턴스 생성
// React 내부: componentStates[componentId] = { count: 5 }
```

---

#### Q2. useEffect 의존성 배열이 뭔가?

```typescript
useEffect(() => {
    console.log('count 변경됨:', count);
}, [count]);  // ← 이게 뭐야?
```

**답:**
- `[]` 빈 배열 = 최초 1회만 실행 (viewDidLoad)
- `[count]` = count 변경될 때마다 실행
- 없음 = 매 렌더링마다 실행 (거의 안 씀)

**네이티브에는 없는 개념:**
```swift
// Swift에는 이런 게 없음
// 대신 명시적으로 호출
var count: Int = 0 {
    didSet {  // 프로퍼티 옵저버
        print("count 변경됨: \(count)")
        updateUI()
    }
}
```

---

#### Q3. JSX는 뭔가? XML인가?

```typescript
return (
    <View style={{ flex: 1 }}>
        <Text>Hello</Text>
    </View>
);
```

**답:**
- JSX = JavaScript + XML 스타일
- 실제로는 함수 호출로 변환됨

**변환 전 (JSX):**
```typescript
<View style={{ flex: 1 }}>
    <Text>Hello</Text>
</View>
```

**변환 후 (JavaScript):**
```typescript
React.createElement(
    View,
    { style: { flex: 1 } },
    React.createElement(Text, null, 'Hello')
);
```

**네이티브 비유:**
```swift
// Swift - 명령형 UI
let view = UIView()
view.backgroundColor = .white

let label = UILabel()
label.text = "Hello"
view.addSubview(label)

// React Native - 선언형 UI
<View style={{ backgroundColor: 'white' }}>
    <Text>Hello</Text>
</View>
```

---

### 7. 네이티브 개발자가 헷갈리는 용어

| 네이티브 용어 | React Native 용어 | 설명 |
|--------------|-------------------|------|
| ViewController / Activity | Component (함수) | 화면 단위 |
| var property | useState | 상태 변수 |
| weak var / lateinit var | useRef | 참조 보관 |
| viewDidLoad / onCreate | useEffect(() => {}, []) | 초기화 |
| deinit / onDestroy | useEffect return | 정리 |
| delegate | Props (함수) | 이벤트 콜백 |
| Storyboard / XML | JSX | UI 정의 |
| UIView / View | `<View>` | 컨테이너 |
| UILabel / TextView | `<Text>` | 텍스트 |
| UIButton / Button | `<Pressable>` 또는 라이브러리 | 버튼 |

---

### 8. 실전 팁: 네이티브 → RN 사고방식 전환

#### 네이티브 사고 (명령형)
```swift
// "이렇게 해라"
let label = UILabel()
label.text = "Hello"
label.textColor = .red

if isError {
    label.textColor = .red
} else {
    label.textColor = .black
}
```

#### React 사고 (선언형)
```typescript
// "이렇게 보여라"
<Text style={{ color: isError ? 'red' : 'black' }}>
    Hello
</Text>
```

**핵심 차이:**
- 네이티브: "상태가 바뀌면 **직접** UI 업데이트"
- React: "상태가 바뀌면 **자동으로** UI 재렌더링"

---

## 💡 직접 해보기

### 실습: 네이티브 코드를 RN으로 변환

#### iOS Swift 코드
```swift
class CounterViewController: UIViewController {
    var count: Int = 0
    var label: UILabel!

    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
    }

    func increment() {
        count += 1
        updateLabel()
    }

    func updateLabel() {
        label.text = "\(count)"
    }
}
```

#### React Native로 변환 (답)
```typescript
function Counter() {
    const [count, setCount] = useState(0);

    const increment = () => {
        setCount(count + 1);
        // updateLabel() 불필요! 자동 재렌더링
    };

    return (
        <View>
            <Text>{count}</Text>
            <Button title="+" onPress={increment} />
        </View>
    );
}
```

---

## 🐛 네이티브 개발자가 자주 하는 실수

### ❌ 실수 1: 직접 UI 업데이트 시도

```typescript
❌ 네이티브처럼 하려고 함
const textRef = useRef<Text>(null);
textRef.current.setText('Hello');  // ← 이런 거 없음!

✅ React 방식
const [text, setText] = useState('');
setText('Hello');  // 상태 변경 → 자동 재렌더링
```

### ❌ 실수 2: 생명주기 메서드 찾기

```typescript
❌ 이런 거 없음
componentDidLoad() { }
componentWillUnmount() { }

✅ useEffect 사용
useEffect(() => {
    // didLoad

    return () => {
        // willUnmount
    };
}, []);
```

### ❌ 실수 3: 클래스로 작성하려고 함

```typescript
❌ 옛날 방식 (Class Component)
class MyScreen extends React.Component {
    state = { count: 0 };
    ...
}

✅ 최신 방식 (Function Component + Hooks)
function MyScreen() {
    const [count, setCount] = useState(0);
    ...
}
```

---

## 🔗 참고 자료

### 공식 문서
- [React 공식 문서 - Thinking in React](https://react.dev/learn/thinking-in-react)
- [React Native 공식 문서](https://reactnative.dev/)

### 관련 문서
- 다음: `RN_시작_001_프로젝트_첫_만남.md`

---

## ✅ 체크리스트

- [ ] React Native는 함수형 프로그래밍을 사용함을 이해했다
- [ ] useState가 클래스 프로퍼티와 같은 역할임을 알겠다
- [ ] useEffect가 생명주기 메서드 역할을 함을 알겠다
- [ ] JSX가 UI를 선언적으로 정의하는 방식임을 이해했다
- [ ] 명령형(네이티브) vs 선언형(React) 차이를 알겠다

---

## 📌 핵심 요약

1. **클래스 없음:** 함수형 컴포넌트 사용
2. **useState = 클래스 프로퍼티:** 상태 저장
3. **useRef = weak var:** 참조 보관
4. **useEffect = 생명주기:** 초기화/정리
5. **JSX = 선언형 UI:** "어떻게"가 아닌 "무엇을"
6. **사고방식 전환:** 명령형 → 선언형

---

**작성일**: 2026-01-07
**난이도**: 🟢 입문 (네이티브 → RN 전환자용)
**중요도**: ⭐⭐⭐⭐⭐ (반드시 먼저 읽기!)
