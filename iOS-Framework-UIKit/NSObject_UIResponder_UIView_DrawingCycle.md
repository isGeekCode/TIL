# UIView의 Drawing Cycle (Layout Cycle)

UIViewController에 생명주기가 있는 것과 관련하여,   
UIView에서도 이와 밀접하게 Drawing Cycle이라는 것이 맞물려서 실행된다.  

<br><br>

🟩 ViewController의 메서드
- loadView
- viewDidLoad
- viewWillAppear
- updateViewConstraints
- viewWilLayoutSubviews
- viewDidLayoutSubViews
- viewDidAppear

🟥 View의 메서드
- requiresConstraintBasedLayout
- updateConstraints
- intrinsicContentSize
- layoutSubviews
- drawRect

<br>

이제 이 ViewController와 View 메서드를 합치면? 아래와 같이 맞물린다.  

- 🟥 requiresConstraintBasedLayout
- 🟩 loadView
- 🟩 viewDidLoad
- 🟩 viewWillAppear
- Constraints : 오토레이아웃 (재조정)
    - 🟥 updateConstraints
    - 🟥 intrinsicContentSize
    - 🟩 updateViewConstraints
- Layout : 위치 / 크기 (재조정)
    - 🟩 viewWilLayoutSubviews
    - 🟥 layoutSubviews
    - 🟩 viewDidLayoutSubViews
- Draw : 실제 내부 컨텐츠를 (다시) 그리기
    - 🟥 drawRect
- 🟩 viewDidAppear

<br><br>

## RunLoop (Update Cycle)
아이폰은 1초에 60번 화면을 다시 그린다.    
UI를 담당하는 Main Thread가 1초에 60번 다시 그려야하는 역할을 가진다.  
> 항상은 아니고, 다시 그려야할 필요가 생기면

- 앱이 시작될 때,  앱을 담당하는 Main Run Loop (반복문)가 생긴다.  
- 이벤트처리를 담당하고,  어떤 함수를 실행시킬 건지 선택하고 실행한다.  
- 그에 따른 함수 등 실행의 결과를 화면에 보여줘야하기때문에, 화면을 다시 그린다.
- 항상 그리는 것은 아니고, 화면을 다시 그리는 일이 필요할 때, 뷰를 전체적으로 업데이트한다.  


<br><br>

다시 위에 있는 Cycle을 보자.  


- 🟥 requiresConstraintBasedLayout
- 🟩 loadView
- 🟩 viewDidLoad
- 🟩 viewWillAppear
- Constraints : 오토레이아웃 (재조정)
    - 🟥 updateConstraints
    - 🟥 intrinsicContentSize
    - 🟩 updateViewConstraints
- Layout : 위치 / 크기 (재조정)
    - 🟩 viewWilLayoutSubviews
    - 🟥 layoutSubviews
    - 🟩 viewDidLayoutSubViews
- Draw : 실제 내부 컨텐츠를 (다시) 그리기
    - 🟥 drawRect
- 🟩 viewDidAppear

<br><br>

실제 런루프로 뷰를 다시 그리는 것과 연관된 부분은  
viewWillAppear (화면에 뷰가 표시될 예정) 이후인  
🟥 updateConstraints 부터 
viewDidAppear (화면에 뷰가 표시됨) 이전인  
🟥 drawRect 까지이다.  


<br><br>

아까 언급한 것처럼 1초에 60번 매번 이메서드를 호출하는것이 아니라 
필요한 경우, 해당 메서드를 호출하는 것이다.  

이에 해당하는 메서드와 역할은 아래와 같다.  

- 🟥 updateConstraints : 제약 조건을 (재)업데이트하는 과정
- 🟥 layoutSubviews : 하위 뷰들의 위치 / 크기를 계산하고 (재)배치
- 🟥 drawRect : 실제 내부 컨텐츠 (다시) 그리기

1초에 60번마다 감지하여, 
(제약조건 / View들의 위치 크기 / 그리는 작업)이 변경되었다면  
메서드가 실행되는 것이다.  

그런데 위 메서드를 개발자가 실행하려고 하면,  경고창이 생긴다.  

Apple에서는 해당 메서드가 아닌 또다른 코드들을 제공한다. 

- 🟥 updateConstraints
    - setNeedsUpdateConstraints() : 다음 사이클에 오토레이아웃 조정 요청
    - updateConstraintsIfNeeded() : 지금 당장 오토레이아웃 조정 요청
- 🟥 layoutSubviews
    - setNeedsLayout() : 다음 사이클에 위치 / 크기 조정 요청
    - layoutIfNeeded() : 지금 당장 위치 / 크기 조정 요청
- 🟥 drawRect
    - setNeedsDisplay() : 다음 사이클에 draw 요청
    - displayIfNeeded() : 지금 당장 draw 요청

<br><br>

## 예제 : 버튼클릭시 UI변경

```swift

final class MyButton: UIButton {

    var onAndOff = false
    
    /*
    // Only override draw() if you perform custom drawing.
    // An empty implementation adversely affects performance during animation.
    override func draw(_ rect: CGRect) {
        // Drawing code
    }
    */
    
    func toggle() {
        self.onAndOff.toggle()
    }
    
    override func layoutSubviews() {
        super.layoutSubviews()
        print(#function)
    }
}

final class ViewController: UIViewController {
    
    // 제약조건을 저장하기 위한 변수 선언
    // (나중에 접근해서 변경하기 위함)
    private var btnHeightAnchor : NSLayoutConstraint!
    private var btnWidthAnchor: NSLayoutConstraint!
    
    // 버튼
    private lazy var testButton: MyButton = {
        let button = MyButton()
        button.layer.cornerRadius = 12
        button.backgroundColor = .yellow
        button.setTitle("Button", for: .normal)
        button.setTitleColor(.black, for: .normal)
        button.addTarget(self, action: #selector(handleAnimationEffect), for:.touchUpInside)
        button.onAndOff = false
        button.translatesAutoresizingMaskIntoConstraints = false
        return button
    }()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
        setupConstraints()
    }
    
    func setupUI() {
        view.addSubview(myButton)
    }
    
    func setupConstraints() {
        
        // 원칙적인 오토레이아웃 설정 (높이, 넓이)
        //testButton.heightAnchor.constraint(equalToConstant: 60).isActive = true
        //testButton.widthAnchor.constraint(equalToConstant: 100).isActive = true
        
        // 제약조건을 변수에 저장 : 차후 변경하기 위함
        btnHeightAnchor = testButton.heightAnchor.constraint(equalToConstant: 60)
        btnWidthAnchor = testButton.widthAnchor.constraint(equalToConstant: 100)
        
        btnHeightAnchor.isActive = true
        btnWidthAnchor.isActive = true
        
        // 원칙적인 오토레이아웃 설정 (가운데 정렬 - X, Y축)
        testButton.centerXAnchor.constraint(equalTo: view.centerXAnchor).isActive = true
        testButton.centerYAnchor.constraint(equalTo: view.centerYAnchor).isActive = true
    }
    
    @objc func handleAnimationEffect(){
        print(#function)
        
        // 높이/넓이 변경 관련 애니메이션 코드
        if !testButton.onAndOff {
            btnHeightAnchor.constant = 400
            btnWidthAnchor.constant = 200
        } else {
            btnHeightAnchor.constant = 60
            btnWidthAnchor.constant = 100
        }
        
        UIView.animate(withDuration: 2) {
            // 지금당장 layoutSubviews 실행 요청
            self.view.layoutIfNeeded()
        } completion: { success in
            print("애니메이션 처리 완료")
        }
        testButton.toggle()
    }
}



```
