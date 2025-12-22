# UIView의 Drawing Cycle (Layout Cycle)

> **💡 이 문서를 읽기 전에**
> - UIViewController의 생명주기를 먼저 이해하면 더 쉽게 이해할 수 있습니다
> - Drawing Cycle은 화면에 뷰가 어떻게 그려지는지를 설명하는 개념입니다

## 📌 개요

UIViewController에 생명주기가 있는 것처럼,
UIView에도 **Drawing Cycle(레이아웃 사이클)** 이라는 것이 있습니다.

이 두 가지는 서로 밀접하게 맞물려서 실행되며, 화면에 UI가 그려지는 전체 과정을 이루게 됩니다.

**왜 중요한가?**
- UI 버그를 디버깅할 때 어느 시점에서 문제가 발생하는지 파악 가능
- 애니메이션을 구현할 때 정확한 타이밍 제어 가능
- 성능 최적화를 위해 불필요한 레이아웃 계산 방지 가능

<br><br>

## 🔍 주요 메서드 구분

화면이 그려지는 과정에는 **ViewController 메서드**와 **View 메서드**가 함께 동작합니다.

### 🟩 ViewController의 메서드 (뷰 컨트롤러가 호출)
- `loadView` - 뷰 계층 구조 로드
- `viewDidLoad` - 뷰가 메모리에 로드된 직후
- `viewWillAppear` - 화면에 나타나기 직전
- `updateViewConstraints` - 제약 조건 업데이트 시점
- `viewWilLayoutSubviews` - 레이아웃 시작 직전
- `viewDidLayoutSubViews` - 레이아웃 완료 직후
- `viewDidAppear` - 화면에 완전히 나타난 후

### 🟥 View의 메서드 (개별 뷰가 호출)
- `requiresConstraintBasedLayout` - 오토레이아웃 사용 여부 결정
- `updateConstraints` - 실제 제약 조건 업데이트
- `intrinsicContentSize` - 뷰 고유의 콘텐츠 크기
- `layoutSubviews` - 하위 뷰들의 위치/크기 계산
- `drawRect` - 실제 화면 그리기 (Custom Drawing)

<br>

## 🔄 전체 실행 흐름

이제 ViewController와 View 메서드가 **어떤 순서로 맞물려 실행되는지** 살펴보겠습니다.

> **💡 핵심 포인트**
> - 🟩 표시는 ViewController가 제어하는 시점
> - 🟥 표시는 각 View가 직접 제어하는 시점
> - 실제로는 이 과정이 계층적으로 반복됩니다 (루트뷰 → 하위뷰 → 하위뷰의 하위뷰...)

### 1️⃣ 초기화 단계
- 🟥 `requiresConstraintBasedLayout` - 오토레이아웃 필요 여부 확인
- 🟩 `loadView` - 뷰 계층 구조 생성
- 🟩 `viewDidLoad` - 뷰 로드 완료, 초기 설정 수행

### 2️⃣ 화면 표시 준비
- 🟩 `viewWillAppear` - 화면에 나타나기 직전

### 3️⃣ Constraints (제약 조건 단계)

> **이 단계에서는**: 오토레이아웃 제약 조건을 계산하고 설정합니다

- 🟥 `updateConstraints` - 뷰 자신의 제약 조건 업데이트 (하위 → 상위 순)
- 🟥 `intrinsicContentSize` - 뷰가 가져야 할 고유 크기 계산 (예: UILabel의 텍스트 크기)
- 🟩 `updateViewConstraints` - 뷰 컨트롤러 레벨에서 제약 조건 업데이트

### 4️⃣ Layout (위치/크기 배치 단계)
> **이 단계에서는**: 실제 위치(x, y)와 크기(width, height)를 계산합니다

- 🟩 `viewWillLayoutSubviews` - 레이아웃 시작 직전 (상위 → 하위 순)
- 🟥 `layoutSubviews` - 실제 하위 뷰들의 frame 계산 및 배치
- 🟩 `viewDidLayoutSubViews` - 레이아웃 완료 직후

### 5️⃣ Draw (화면 그리기 단계)
> **이 단계에서는**: 실제로 픽셀을 그립니다 (Custom Drawing이 필요한 경우만)

- 🟥 `drawRect` - 뷰의 내부 콘텐츠를 직접 그림 (예: 그래프, 도형 등)

### 6️⃣ 완료 단계
- 🟩 `viewDidAppear` - 화면에 완전히 표시됨

<br><br>

> **⚠️ 주의사항**
> - `drawRect`는 일반적인 UILabel, UIButton 등에서는 사용하지 않습니다
> - 커스텀 드로잉(예: 차트, 그래프, 특수한 도형)이 필요할 때만 오버라이드합니다
> - 대부분의 경우 `layoutSubviews`까지만 신경 쓰면 됩니다

<br><br>

## ⏱️ RunLoop (Update Cycle)

> **💡 핵심 개념**
> - iOS는 초당 60프레임(60 FPS)으로 화면을 갱신합니다
> - 최신 기기는 120Hz ProMotion을 지원하기도 합니다
> - 하지만 매번 화면을 다시 그리는 것은 아닙니다!

### RunLoop의 동작 방식

**RunLoop란?**
- 앱이 시작될 때 생성되는 **Main Run Loop(메인 반복문)**
- 사용자 입력, 타이머, 네트워크 응답 등 이벤트를 계속 감시합니다
- UI 업데이트는 반드시 이 Main Thread(메인 스레드)에서만 가능합니다

**동작 순서:**
1. **이벤트 감지** - 사용자가 버튼을 누르거나, 데이터가 변경되거나, 타이머가 동작
2. **함수 실행** - 해당 이벤트에 맞는 코드 실행
3. **UI 업데이트 필요 판단** - 화면을 다시 그려야 하는가?
4. **Update Cycle 실행** - 필요한 경우에만 Drawing Cycle 진행

> **⚠️ 중요한 점**
> - 항상 화면을 다시 그리는 것이 아닙니다
> - "변경이 필요한 뷰"만 선택적으로 업데이트합니다
> - 이것이 iOS가 부드럽고 빠른 이유입니다!

<br><br>

### 🔄 Update Cycle의 핵심 영역

위에서 본 전체 Drawing Cycle 중에서, **실제로 RunLoop에서 반복적으로 실행되는 부분**은 다음과 같습니다:

```
🟩 viewWillAppear    ← 이후부터
    ↓
🟥 updateConstraints
🟥 intrinsicContentSize
🟩 updateViewConstraints
    ↓
🟩 viewWillLayoutSubviews
🟥 layoutSubviews        ← 이 부분들이 반복 실행됨
🟩 viewDidLayoutSubViews
    ↓
🟥 drawRect
    ↓
🟩 viewDidAppear     ← 이전까지
```

> **즉, 화면이 표시된 후에도 `updateConstraints` → `layoutSubviews` → `drawRect` 부분은 필요에 따라 반복 실행됩니다!**

<br><br>

## 🎯 실제 Update Cycle에서 반복되는 3가지 핵심 메서드

RunLoop는 1초에 60번(60 FPS) 이 세 가지를 확인하고, **변경이 필요한 경우에만** 실행합니다:

### 1️⃣ 🟥 `updateConstraints`
**역할**: 오토레이아웃 제약 조건을 (재)계산
**실행 시점**: 제약 조건이 변경되었을 때
**예시**: UILabel의 텍스트가 변경되어 크기가 달라져야 할 때

### 2️⃣ 🟥 `layoutSubviews`
**역할**: 하위 뷰들의 실제 위치(x, y)와 크기(width, height)를 (재)계산
**실행 시점**: 뷰의 frame이 변경되어야 할 때
**예시**: 화면 회전, 애니메이션, 제약 조건 변경 등

### 3️⃣ 🟥 `drawRect`
**역할**: 뷰의 내부 콘텐츠를 픽셀 단위로 (재)그리기
**실행 시점**: 커스텀 드로잉이 필요할 때
**예시**: 차트 그리기, 그라데이션 배경 등

<br>

> **⚠️ 중요! 이 메서드들을 직접 호출하면 안 됩니다!**
>
> Xcode에서 `layoutSubviews()`, `updateConstraints()` 등을 직접 호출하면 경고가 나타납니다.
>
> **왜 그럴까요?**
> - 이 메서드들은 시스템이 최적의 타이밍에 자동으로 호출합니다
> - 개발자가 직접 호출하면 성능 문제와 예측 불가능한 동작이 발생할 수 있습니다
>
> **대신, Apple이 제공하는 안전한 방법을 사용해야 합니다!** 

<br><br>

## 🛠️ 개발자가 사용해야 하는 안전한 메서드들

시스템 메서드를 직접 호출하는 대신, Apple이 제공하는 **요청(Request) 메서드**를 사용합니다.

### 1️⃣ Constraints 업데이트 요청

| 메서드 | 실행 시점 | 사용 예시 |
|--------|----------|-----------|
| `setNeedsUpdateConstraints()` | 다음 Update Cycle에 | 여러 제약 조건을 한 번에 변경할 때 |
| `updateConstraintsIfNeeded()` | 지금 즉시 | 제약 조건 변경 후 바로 계산이 필요할 때 |

```swift
// 예시
label.text = "새로운 텍스트"
view.setNeedsUpdateConstraints()  // 다음 사이클에 제약 조건 재계산 요청
```

### 2️⃣ Layout 업데이트 요청 (가장 자주 사용!)

| 메서드 | 실행 시점 | 사용 예시 |
|--------|----------|-----------|
| `setNeedsLayout()` | 다음 Update Cycle에 | 부드러운 애니메이션 없이 레이아웃 변경 |
| `layoutIfNeeded()` | 지금 즉시 | 애니메이션 블록 내에서 사용 |

```swift
// 예시 1: 단순 레이아웃 변경
heightConstraint.constant = 200
view.setNeedsLayout()  // 다음 사이클에 레이아웃 재계산

// 예시 2: 애니메이션과 함께 (가장 많이 사용!)
UIView.animate(withDuration: 0.3) {
    heightConstraint.constant = 200
    view.layoutIfNeeded()  // 즉시 레이아웃 재계산 → 애니메이션 효과
}
```

### 3️⃣ Drawing 업데이트 요청

| 메서드 | 실행 시점 | 사용 예시 |
|--------|----------|-----------|
| `setNeedsDisplay()` | 다음 Update Cycle에 | 커스텀 뷰를 다시 그려야 할 때 |
| `displayIfNeeded()` | 지금 즉시 (거의 사용 안 함) | 즉각적인 렌더링이 필요할 때 |

```swift
// 예시: 커스텀 차트 뷰의 데이터가 변경됨
chartView.data = newData
chartView.setNeedsDisplay()  // 다음 사이클에 다시 그리기 요청
```

<br>

> **💡 실무 팁**
>
> **가장 많이 사용하는 조합:**
> ```swift
> // 애니메이션과 함께 레이아웃 변경
> UIView.animate(withDuration: 0.3) {
>     // 1. 제약 조건 변경
>     self.heightConstraint.constant = 200
>
>     // 2. 즉시 레이아웃 재계산 요청
>     self.view.layoutIfNeeded()
> }
> ```
>
> **왜 이 조합을 사용할까?**
> - `layoutIfNeeded()`가 애니메이션 블록 안에서 호출되면
> - 레이아웃 변경이 부드럽게 애니메이션 됩니다!
> - 이것이 iOS 애니메이션의 핵심 패턴입니다

<br><br>

## 💻 실전 예제: 버튼 클릭 시 애니메이션으로 크기 변경하기

> **이 예제에서 배울 내용:**
> - `layoutSubviews()` 메서드가 언제 호출되는지 확인
> - `layoutIfNeeded()`를 사용한 부드러운 애니메이션 구현
> - 제약 조건 변경과 레이아웃 업데이트의 관계

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

<br>

### 📝 코드 설명

**1. MyButton 클래스 (커스텀 버튼)**
```swift
override func layoutSubviews() {
    super.layoutSubviews()
    print(#function)  // "layoutSubviews" 출력
}
```
- `layoutSubviews()`가 언제 호출되는지 확인하기 위한 print 문
- 버튼을 클릭할 때마다 콘솔에 "layoutSubviews" 출력됨을 확인할 수 있습니다

**2. ViewController의 핵심 로직**
```swift
@objc func handleAnimationEffect() {
    // 1️⃣ 제약 조건 변경 (아직 화면에는 반영 안 됨)
    if !testButton.onAndOff {
        btnHeightAnchor.constant = 400  // 커지기
        btnWidthAnchor.constant = 200
    } else {
        btnHeightAnchor.constant = 60   // 작아지기
        btnWidthAnchor.constant = 100
    }
    
    // 2️⃣ 애니메이션 블록 안에서 layoutIfNeeded() 호출
    UIView.animate(withDuration: 2) {
        self.view.layoutIfNeeded()  // ← 여기가 핵심!
    } completion: { success in
        print("애니메이션 처리 완료")
    }
    
    testButton.toggle()
}
```

**핵심 포인트:**
- `constant` 값을 변경해도 즉시 화면에 반영되지 않습니다
- `layoutIfNeeded()`를 호출해야 실제 레이아웃이 재계산됩니다
- 이것이 `UIView.animate` 블록 안에 있으면 → **부드러운 애니메이션 효과!**

### 🎬 실행 결과

버튼을 클릭하면:
1. 콘솔에 "handleAnimationEffect" 출력
2. 콘솔에 "layoutSubviews" 출력 (레이아웃이 다시 계산됨을 확인)
3. 버튼이 2초 동안 부드럽게 크기 변경
4. "애니메이션 처리 완료" 출력

### 🤔 만약 `layoutIfNeeded()`를 빼면?

```swift
// ❌ 잘못된 예
btnHeightAnchor.constant = 400
// layoutIfNeeded() 없음
```
→ 제약 조건만 변경되고 화면에 즉시 반영되지 않습니다!  
→ 다음 Update Cycle에서 자동으로 반영되지만, 애니메이션 효과가 없습니다

### 🤔 만약 애니메이션 블록 밖에서 호출하면?

```swift
// ⚠️ 애니메이션 없이 즉시 변경
btnHeightAnchor.constant = 400
view.layoutIfNeeded()  // 애니메이션 블록 밖
```
→ 즉시 변경되지만 애니메이션 효과가 없습니다!

<br><br>

## 📚 요약

### Drawing Cycle의 전체 흐름
1. **초기화** → `loadView`, `viewDidLoad`
2. **제약 조건 계산** → `updateConstraints`
3. **레이아웃 계산** → `layoutSubviews` (가장 중요!)
4. **화면 그리기** → `drawRect` (커스텀 뷰만)

### 실무에서 기억할 핵심 3가지

1️⃣ **절대 직접 호출하지 말 것**
- ❌ `layoutSubviews()` 직접 호출
- ✅ `setNeedsLayout()` 또는 `layoutIfNeeded()` 사용

2️⃣ **애니메이션 패턴**
```swift
UIView.animate(withDuration: 0.3) {
    // 제약 조건 변경
    view.layoutIfNeeded()  // ← 이것만 기억하면 됨!
}
```

3️⃣ **디버깅할 때**
- `layoutSubviews()`에 print 문 추가하여 언제 호출되는지 확인
- 레이아웃 버그의 90%는 제약 조건 문제

### 다음 학습 추천
- UIViewController Life-cycle과 함께 보기
- 오토레이아웃(Auto Layout) 심화 학습
- UIView 애니메이션 고급 기법

<br><br>

## History
- 251222 : 주석추가
