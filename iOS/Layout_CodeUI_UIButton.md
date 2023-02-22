# Layout - CodeUI, StoryboardUI: UIButton



UIButton 은 말그대로 버튼을 눌렀을 때, 특정 로직을 실행할 수 있도록 

하게 하는 객체다. 

이를 위해서 두단계를 거친다.

- step1 : UIButton UI작업
- step2: Action 세팅
- step3: UIButton과 Action 연결

UIButton을 사용하는 방법은 스토리보드의 사용 여부에 따라 달라진다.

## 스토리보드에서 UIButton을 생성하는 경우

- UI작업
    - 라이브러리에서 스토리보드로 UIButton 올려놓기
    - 오토레이아웃 세팅하기
    - IBOutlet 연결  - ViewController.swift로 드래그하기
- Action 세팅
    - IBAction 연결 - ViewController.swift로 드래그하기
    - IBAction 메서드 내부에 코드 구현
    

### 용어설명

- IB : Interface Builder의 약자
- IBOutlet : Interface Builder를 통해 받아온 정보로 변수선언
- Action **:** Event가 일어난 경우 호출되는 Action을 정의해둔 것! 하나의 함수!
- IBAction **:** Interface Builder를 통해 받아온 정보로 Action을 수행하겠다!
- sender **:** 이 메소드의 caller. 버튼에서는 어떤 버튼이 눌렸는지 구분해주는 역할

스토리보드 작업으로 간단한 연결을 하게 되면 아래와 같다.

```swift
class ViewController: UIViewController {

    // MARK: 변수 선언
    @IBOutlet weak var myButton: UIButton!
    
    // MARK: Action 구현
    @IBAction func buttonAction(_ sender: UIButton) {
          print("Hello GeekCode")
    }
    
    override func viewDidLoad() {
          super.viewDidLoad()
          // Do any additional setup after loading the view.

     }
}

```

## Code Programming으로 UIButton을 생성하는 경우

- UI작업
    - 변수선언
    - 오토레이아웃 세팅하기: setConstraints
    - 뷰에 추가 : addSubView
    - 상세옵션 세팅 : setDetail
- Action 세팅
    - @objc함수 생성
    - sender를 보내려면 파라미터 구현
- UIButton과 Action연결
    - addTarget함수로 UIButton에 연결
    

```swift
class ViewController: UIViewController {

    // MARK: 변수 선언
    var myButton: UIButton()

    
    override func viewDidLoad() {
          super.viewDidLoad()
    
    // MARK: UI작업

    // 계층에 추가
        self.view.addSubView(myButton)

    // Constraint 자동생성 비활성화
        myButton.translatesAutoresizingMaskIntoConstraints = false

    // Constraints 세팅 및 활성화
          // 방법1 : 배열에 Constraints를 담아 일괄 활성화 

        NSLayoutConstraint.activate([
            myButton.topAnchor.constraint(equalTo: self.view.safeAreaLayoutGuide.topAnchor, constant: 30),
            myButton.centerXAnchor.constraint(equalTo: self.view.centerXAnchor),
            myButton.widthAnchor.constraint(equalToConstant: 100),
            myButton.heightAnchor.constraint(equalToConstant: 100),
        ])

          // 방법2 : 각 Constraint를 활성화하기
        /*
          myButton.topAnchor.constraint(equalTo: self.view.safeAreaLayoutGuide.topAnchor, constant: 30).isActive = true
          myButton.centerXAnchor.constraint(equalTo: self.view.centerXAnchor).isActive = true
          myButton.widthAnchor.constraint(equalToConstant: 100).isActive = true
          myButton.heightAnchor.constraint(equalToConstant: 100).isActive = true
        */
        
    // MARK: setDetail
        myButton.backgroundColor = .systemTeal
        myButton.setTitle("myBytton", for: .normal)

    // MARK: UIButton과 Action연결
        myButton.addTarget(self, action: #selector(buttonAction(_:)), for: .touchUpInside)
   }

    // MARK: Action 구현
    @objc func buttonAction(_ sender: UIButton) {
          print("Hello GeekCode")
    }
}

```


## UIButton에 버튼이미지 세팅하기
### Step1: UIImage생성
버튼에 들어가는 이미지는 UIImage에 담아 사용한다. 
이때 UIImage는 아래와 같이 만든다. 
```swift
// 아이콘이미지를 사용하는 경우
let image = UIImage(systemName: "heart.fill")

// Assets에 넣은 커스텀 이미지를 사용하는 경우
let image = UIImage(named: "normal-image")
```
### Step2: 원하는 버튼의 상태에 세팅
기본적인 상태의 버튼 이미지를 선택할때는 아래와 같다.
```swift
myButton.setImage(normalImage, for: .normal)
```

버튼을 클릭하는 순간의 이미지를 선택할 경우 highlighted를 세팅한다.
```swift
myButton.setImage(normalImage, for: .highlighted)
```


### UIControl.State
버튼의 상태는 UIControl.State 구조체로 이루어져있다.

.normal: 기본 상태
.highlighted: 터치 다운 상태
.disabled: 비활성화 상태
.selected: 선택된 상태
.focused: 포커스된 상태
.application: 어플리케이션 정의 상태




각 상태는 해당하는 경우에 UIControl에서 발생하는 이벤트 및 동작을 다르게 처리하도록 도와준다. 예를 들어, .normal 상태에서는 버튼이 보통 상태이므로, 사용자가 버튼을 눌렀을 때의 동작을 정의할 수 있다. 반면에, .disabled 상태에서는 버튼이 비활성화되었으므로, 사용자가 버튼을 눌러도 아무런 동작이 수행되지 않도록 처리할 수 있다.

UIControl 클래스에서는 state 프로퍼티를 통해 현재 상태를 확인할 수 있으며, `setEnabled(_:animated:)`, `setSelected(_:animated:)`, `setHighlighted(_:animated:)` 등의 메서드를 사용하여 상태를 변경할 수 있다.


## 스토리보드에서 작업하면 생략되는 코드들

- addSubView : 라이브러리에서 스토리보드로 드래그로 선언하는 부분
- translatesAutoresizingMaskIntoConstraints = false
    - 코드로 UI작업을 하게 되면 Constraints를 직접 코드로 세팅해야하는데, 이때 위 부분을 false해주지 않으면 자동으로 오토리사이징마스크가 생성되게 된다.
    - 그러면 코드로 작성한 Constraint가 동작하지않는다.
- Constraint.isActive = true
    - Constraint를 만들고 활성화를 해주어야한다.
    - NSLayoutConstraint.activate(`[ Constraints ]`)  로 대체 할 수 있다.
- addTarget
    - ViewController내부에 IBOutlet과 IBAction이 연결되어있다.

## 스토리보드의 장단점

장점

- 간단한 작업은 스토리보드로 하는 것이 편하다.
- UI를 직접 확인하며 작업이 가능하다.
- View의 전환 또한 드래그로 해결이 된다.
- 세부옵션들을 한번에 보면서 세팅이 가능하다.

단점

- 스토리보드가 비대해질경우
    - 한눈에 파악하기 힘들 수 있다.
    - 스토리보드가 무거워져서 사용할때 로딩이 길어진다.
- 오토레이아웃에 대한 이해도가 낮으면 에러의 늪에 빠진다.
    
    

### 코드 프로그래밍의 장단점

장점

- 따로 여기저기 움직이지않고 한자리에서 구현이 가능하다.
- 프로젝트를 가볍게 유지할 수 있다.

단점

- 코드가 길어져 자칫 가독성이 떨어지기때문에 깔끔한 정리가 필요하다
- UI작업
    - 많은 노력이 필요하다. 많은부분을 일일히 지정해줘야하기때문이다.
    - 세부옵션의 경우, 익숙하지않으면 일일히 찾아야한다.

++ 추가필요
