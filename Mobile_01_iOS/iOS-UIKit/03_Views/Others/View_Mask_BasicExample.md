# View - UIView 마스크 입문 (두 개의 UIView로 이해하기)

## 0. 마스크가 뭐지? (큰 네모 + 작은 네모 그림으로 이해하기)
- **큰 네모(원본 뷰)**: 화면에 보여줄 실제 콘텐츠다. 예로 사진, 단색 배경, 카메라 프리뷰가 온다.
- **작은 네모(마스크 뷰)**: 원본 뷰 위에 덮는 투명한 판(스텐실)이라 생각하면 된다. 이 판에서 **불투명한 부분만 원본을 통과**하고 투명한 부분은 잘린다.
- 즉 작은 네모가 어떤 모양이냐에 따라 큰 네모에서 보이거나 숨겨지는 영역이 결정된다.

```
원본 뷰 (전체 표시)        마스크 (불투명 영역만 통과)        결과
┏━━━━━━━━━━━━┓        ┏━━━━━━━━━━━━┓        ┏━━━━━━━━━━━━┓
┃████████████┃   +    ┃░░░░████░░░░┃   →    ┃░░░░████░░░░┃
┃████████████┃        ┃░░░░████░░░░┃        ┃░░░░████░░░░┃
┃████████████┃        ┃░░░░████░░░░┃        ┃░░░░████░░░░┃
┗━━━━━━━━━━━━┛        ┗━━━━━━━━━━━━┛        ┗━━━━━━━━━━━━┛
(모두 보임)              (가운데만 불투명)             (가운데만 보임)
```

- UIKit에서 이 "작은 네모"는 `UIView`나 `CALayer`가 담당한다. 마스크의 알파 값이 1일수록 잘 보이고 0이면 완전히 잘린다.
- 결국 마스크는 **"무엇을 보여 주고 무엇을 숨길지"**를 결정하는 투명도 필터라고 기억하면 된다.

---

아주 기초적인 마스크 동작을 눈으로 확인하려면 단 두 개의 `UIView`만 있어도 충분하다. 아래 예제는 **큰 사각형 뷰(`coloredView`) 위에 더 작은 뷰(`maskView`)를 마스크로 씌워 특정 영역만 보이도록** 만드는 과정이다.

## 1. 기본 구성 준비
```swift
final class MaskPlaygroundViewController: UIViewController {
    private let coloredView: UIView = {
        let view = UIView(frame: CGRect(x: 40, y: 120, width: 240, height: 240))
        view.backgroundColor = .systemTeal
        view.layer.cornerRadius = 24
        return view
    }()

    private let maskView: UIView = {
        // maskView 자체는 화면에 보이지 않지만, 알파(=불투명도) 정보로 coloredView를 잘라낸다.
        let view = UIView(frame: CGRect(x: 0, y: 0, width: 160, height: 160))
        view.backgroundColor = .black   // 알파가 1인 영역만 원본이 보인다.
        view.layer.cornerRadius = 80    // 모서리를 둥글게 만들어 원형 마스크를 만든다.
        view.layer.masksToBounds = true // 마스크 자신의 둥근 모서리 유지
        return view
    }()

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemBackground
        view.addSubview(coloredView)

        applyMask()
    }

    private func applyMask() {
        // 마스크는 원본 뷰의 좌표계를 기준으로 배치해야 한다.
        maskView.center = CGPoint(x: coloredView.bounds.midX, y: coloredView.bounds.midY)

        // 핵심: coloredView.mask에 UIView를 지정하면 maskView의 알파가 1인 부분만 그려진다.
        coloredView.mask = maskView
    }
}
```

### 실행 결과
- `coloredView`는 240×240 크기의 사각형이지만, 마스크가 160×160이므로 **원형 영역 안쪽만** 화면에 나타난다.
- `maskView`는 실제로 화면에 보이지 않는다. 대신 그 위치와 모양이 `coloredView`의 "보이는 영역"을 결정한다.

## 2. 마스크 이동/애니메이션으로 효과 확인하기
마스크 뷰 위치를 바꿔 보면 원본 뷰도 함께 움직이는 것이 아니라 **보이는 영역만 이동**한다는 사실을 이해하기 쉽다.

```swift
override func viewDidAppear(_ animated: Bool) {
    super.viewDidAppear(animated)

    // 2초 뒤 마스크를 오른쪽 아래로 이동시키는 예제
    UIView.animate(withDuration: 1.2,
                   delay: 2,
                   options: [.curveEaseInOut, .autoreverse, .repeat]) {
        self.maskView.center = CGPoint(x: self.coloredView.bounds.maxX - 20,
                                       y: self.coloredView.bounds.maxY - 20)
        self.coloredView.mask = self.maskView // center를 바꾼 뒤에도 다시 할당 필요 없음
    }
}
```

- 애니메이션 동안 `coloredView.mask`에 지정된 뷰의 위치가 바뀌면, 그 경로에 따라 보이는 영역이 움직이며 마스크 효과를 직관적으로 확인할 수 있다.

## 3. 핵심 포인트 정리
- `UIView.mask`는 그 뷰 전체에 적용된다. 서브뷰나 레이어도 모두 같은 마스크 영향을 받는다.
- 마스크 역할을 하는 뷰/레이어는 화면에 직접 표시되지 않으며, **알파 값이 1인 부분만 원본 뷰를 통과**시킨다.
- 마스크 크기가 원본보다 작으면 일부만 보이고, 크거나 같은 경우는 전체가 보인다.
- `maskView`에 `cornerRadius`나 `transform`, `path`(ShapeLayer를 덧씌우는 방식) 등을 적용하면 다양한 모양을 쉽게 만들 수 있다.
- 마스크 갱신 시에는 `maskView.frame`/`center`를 조정하거나 새로운 마스크 뷰를 다시 할당하면 된다.

## 4. `CAShapeLayer`를 이용한 자유로운 마스크 만들기
UIView를 그대로 마스크로 쓰면 직사각형·둥근 모서리 정도로 한정되지만, `CAShapeLayer`를 직접 만들어서 `layer.mask`에 붙이면 곡선·여러 개의 구멍 등 원하는 모양을 만들 수 있다.

```swift
private func applyShapeLayerMask() {
    // 1) 클리핑할 영역(예: 큰 사각형)과 투명하게 뚫을 영역(동그라미 두 개)을 경로로 정의
    let outerRect = UIBezierPath(rect: coloredView.bounds)
    let firstHole = UIBezierPath(ovalIn: CGRect(x: 40, y: 40, width: 80, height: 80))
    let secondHole = UIBezierPath(ovalIn: CGRect(x: 120, y: 120, width: 60, height: 60))
    outerRect.append(firstHole)
    outerRect.append(secondHole)

    // 2) CAShapeLayer 생성 후 path 지정, evenOdd로 안쪽 경로를 투명하게 처리
    let maskLayer = CAShapeLayer()
    maskLayer.frame = coloredView.bounds
    maskLayer.path = outerRect.cgPath
    maskLayer.fillRule = .evenOdd

    // 3) UIView의 layer.mask에 할당하면 지정한 경로가 그대로 마스크가 된다.
    coloredView.layer.mask = maskLayer
}
```

- `fillRule = .evenOdd`를 주면 첫 번째 경로는 불투명, 그 안에 append된 경로들은 투명 구멍으로 처리된다.
- 단일 경로나 곡선, 다각형도 `UIBezierPath`로 만들 수 있으니, ROI를 정교하게 자르거나 다중 구멍을 만들 때 유용하다.
- `CAShapeLayer`는 애니메이션과도 궁합이 좋아서 `CABasicAnimation(keyPath: "path")`로 마스크 모양을 부드럽게 변화시키는 것도 가능하다.

### 뷰컨트롤러에서 ShapeLayer 마스크 적용 예시

```swift
final class ShapeMaskViewController: UIViewController {
    private let previewView: UIView = {
        let view = UIView()
        view.backgroundColor = .systemIndigo
        view.translatesAutoresizingMaskIntoConstraints = false
        return view
    }()

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemBackground

        view.addSubview(previewView)
        NSLayoutConstraint.activate([
            previewView.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            previewView.centerYAnchor.constraint(equalTo: view.centerYAnchor),
            previewView.widthAnchor.constraint(equalToConstant: 240),
            previewView.heightAnchor.constraint(equalToConstant: 240)
        ])
    }

    override func viewDidLayoutSubviews() {
        super.viewDidLayoutSubviews()
        applyShapeMask()
    }

    private func applyShapeMask() {
        let outer = UIBezierPath(rect: previewView.bounds)
        outer.append(UIBezierPath(ovalIn: CGRect(x: 30, y: 30, width: 100, height: 100)))
        outer.append(UIBezierPath(ovalIn: CGRect(x: 120, y: 120, width: 80, height: 80)))

        let shapeMask = CAShapeLayer()
        shapeMask.frame = previewView.bounds
        shapeMask.path = outer.cgPath
        shapeMask.fillRule = .evenOdd

        previewView.layer.mask = shapeMask
    }
}
```

- 오토레이아웃으로 뷰 위치와 크기를 잡은 뒤 `viewDidLayoutSubviews()`에서 마스크를 갱신하면 로테이션이나 레이아웃 변경에도 대응할 수 있다.
- 필요하면 `viewDidLayoutSubviews()` 대신 뷰 크기가 확정되는 타이밍마다(예: `layoutSubviews` 커스텀) 마스크를 다시 계산하면 된다.

### `UIBezierPath`로 만들 수 있는 대표 모양들
마스크로 쓰는 경로는 원하는 모양을 직접 그리면 된다. 자주 쓰는 패턴을 정리해 두면 응용하기 쉽다.

```swift
// 1. 기본 도형
UIBezierPath(rect: CGRect(x: 20, y: 20, width: 120, height: 80))              // 사각형
UIBezierPath(roundedRect: rect, cornerRadius: 16)                             // 둥근 사각형
UIBezierPath(ovalIn: rect)                                                    // 원/타원

// 2. 호(arc)와 원형 슬라이스
UIBezierPath(arcCenter: center,
             radius: 60,
             startAngle: .pi * 0.1,
             endAngle: .pi * 1.4,
             clockwise: true)

// 3. 자유로운 궤적 (move → line → curve)
let star = UIBezierPath()
star.move(to: CGPoint(x: 120, y: 10))
star.addLine(to: CGPoint(x: 150, y: 90))
star.addQuadCurve(to: CGPoint(x: 60, y: 40), controlPoint: CGPoint(x: 100, y: 120))
star.close()   // 시작점과 끝점을 이어 폐곡선 완성

// 4. 여러 경로를 결합하거나 빼기
let donut = UIBezierPath(ovalIn: CGRect(x: 30, y: 30, width: 200, height: 200))
donut.append(UIBezierPath(ovalIn: CGRect(x: 90, y: 90, width: 80, height: 80)))
```

- `append`를 사용하면 하나의 `UIBezierPath`에 여러 도형을 겹칠 수 있다. `fillRule = .evenOdd`와 조합하면 반전이나 구멍 뚫기 같은 효과를 쉽게 만들 수 있다.
- `addQuadCurve`와 `addCurve`(베지어 2차·3차)는 자유 곡선을 만들 때 유용하다. 제어점을 어떻게 두느냐에 따라 자연스러운 곡선 마스크를 만들 수 있다.
- 필요한 경우 `CGMutablePath`를 직접 만들고 `UIBezierPath(cgPath:)`로 감싸서 사용할 수도 있다. 복잡한 SVG 경로나 그래픽 에셋을 마스크로 쓸 때 편리하다.

이렇게 단순한 실험을 통해 마스크가 "뷰를 잘라내는 개념"이라는 점을 감각적으로 이해한 뒤, 더 복잡한 ROI/경로 조합으로 확장해 나가면 자연스럽게 실전에 적용할 수 있다.

### 다양한 모양 적용

```swift
import UIKit

final class ViewController: UIViewController {
    private let previewView = UIView()
    private let stack = UIStackView()
    
    // 1) 경로 빌더 타입 통일
    private typealias PathBuilder = (CGRect) -> UIBezierPath
    private var currentBuilder: PathBuilder?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemBackground
        
        previewView.translatesAutoresizingMaskIntoConstraints = false
        previewView.backgroundColor = .systemBlue
        previewView.layer.cornerRadius = 16
        
        stack.axis = .horizontal
        stack.spacing = 12
        stack.distribution = .fillEqually
        stack.translatesAutoresizingMaskIntoConstraints = false
        
        // 2) bounds를 ‘나중에’ 받도록 빌더 정의 (self 캡처 X)
        let configurations: [(String, PathBuilder)] = [
            ("Rect", { bounds in
                UIBezierPath(rect: bounds)
            }),
            ("Rounded", { bounds in
                UIBezierPath(roundedRect: bounds, cornerRadius: 30)
            }),
            ("Ovals", { bounds in
                // 배경 전체를 먼저 그리고, 원을 append → evenOdd로 구멍 뚫기
                let path = UIBezierPath(rect: bounds)
                path.append(UIBezierPath(ovalIn: CGRect(x: bounds.minX + 30,
                                                        y: bounds.minY + 30,
                                                        width: 80, height: 80)))
                path.append(UIBezierPath(ovalIn: CGRect(x: bounds.minX + 140,
                                                        y: bounds.minY + 120,
                                                        width: 60, height: 60)))
                return path
            }),
            ("Star", { bounds in
                let path = UIBezierPath()
                
                // 중심 좌표 & 반지름 설정
                let center = CGPoint(x: bounds.midX, y: bounds.midY)
                let outerRadius = min(bounds.width, bounds.height) / 2.2
                let innerRadius = outerRadius * 0.45   // 안쪽 꼭짓점
                
                // 별은 총 10개의 점(바깥/안쪽 번갈아)으로 구성
                var angle: CGFloat = -CGFloat.pi / 2 // 위쪽부터 시작 (12시 방향)
                let angleIncrement = CGFloat.pi / 5  // 36도씩
                
                // 첫 점
                let firstPoint = CGPoint(
                    x: center.x + cos(angle) * outerRadius,
                    y: center.y + sin(angle) * outerRadius
                )
                path.move(to: firstPoint)
                
                // 나머지 점들
                for i in 1..<10 {
                    angle += angleIncrement
                    let radius = (i % 2 == 0) ? outerRadius : innerRadius
                    let point = CGPoint(
                        x: center.x + cos(angle) * radius,
                        y: center.y + sin(angle) * radius
                    )
                    path.addLine(to: point)
                }
                
                path.close()
                return path
            }),
            ("Donut", { bounds in
                let outer = UIBezierPath(ovalIn: bounds.insetBy(dx: 10, dy: 10))
                outer.append(UIBezierPath(ovalIn: bounds.insetBy(dx: 60, dy: 60)))
                return outer
            })
        ]
        
        configurations.forEach { title, builder in
            let button = UIButton(type: .system)
            button.setTitle(title, for: .normal)
            button.addAction(UIAction { [weak self] _ in
                self?.currentBuilder = builder
                self?.applyMask(builder)
            }, for: .touchUpInside)
            stack.addArrangedSubview(button)
        }
        
        view.addSubview(previewView)
        view.addSubview(stack)
        
        NSLayoutConstraint.activate([
            previewView.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            previewView.centerYAnchor.constraint(equalTo: view.centerYAnchor, constant: -60),
            previewView.widthAnchor.constraint(equalToConstant: 240),
            previewView.heightAnchor.constraint(equalToConstant: 240),
            
            stack.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 20),
            stack.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -20),
            stack.topAnchor.constraint(equalTo: previewView.bottomAnchor, constant: 20)
        ])
        
        // 3) 초기 선택
        currentBuilder = configurations.first?.1
    }
    
    override func viewDidLayoutSubviews() {
        super.viewDidLayoutSubviews()
        // 4) 레이아웃 이후 실제 bounds 확정 → 현재 선택 빌더 재적용
        if let builder = currentBuilder {
            applyMask(builder)
        }
    }
    
    private func applyMask(_ builder: PathBuilder) {
        let path = builder(previewView.bounds)
        let maskLayer = CAShapeLayer()
        maskLayer.frame = previewView.bounds
        maskLayer.path = path.cgPath
        // 구멍(도넛/오벌스)도 지원하려고 evenOdd 사용 (단일 경로에도 문제 없음)
        maskLayer.fillRule = .evenOdd
        previewView.layer.mask = maskLayer
    }
}

```

- 여러 버튼을 눌러가며 사각형·타원·별·도넛 형태의 마스크를 즉시 적용할 수 있는 뷰컨트롤러 예제다.
- `applyMask`에 넘기는 클로저가 `previewView`의 `bounds`를 받아 처리하면, 뷰 크기가 바뀌어도 동일한 로직을 재사용할 수 있다.
- `fillRule`을 `.nonZero`로 바꾸면 구멍 없이 전체를 채우는 마스크(예: 별 전체를 보여 주는 형태)를 만들 수 있다.

이렇게 단순한 실험을 통해 마스크가 "뷰를 잘라내는 개념"이라는 점을 감각적으로 이해한 뒤 더 복잡한 ROI/경로 조합으로 확장하면 자연스럽게 실전에 적용할 수 있다.
