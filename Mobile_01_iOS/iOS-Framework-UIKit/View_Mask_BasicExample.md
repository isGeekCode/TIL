# View - UIView 마스크 입문 (두 개의 UIView로 이해하기)

## 0. 마스크가 뭐지? (큰 네모 + 작은 네모 그림으로 이해하기)
- **큰 네모(원본 뷰)**: 화면에 보여줄 실제 콘텐츠입니다. 예를 들면 사진, 단색 배경, 카메라 프리뷰 등이 이 자리에 옵니다.
- **작은 네모(마스크 뷰)**: 원본 뷰 위에 덮는 투명한 판(스텐실)이라고 생각하면 됩니다. 이 판에서 **불투명한 부분만 원본을 통과**하고, 투명한 부분은 잘립니다.
- 즉, 작은 네모가 어떤 모양이냐에 따라 큰 네모에서 보이거나 숨겨지는 영역이 결정됩니다.

```
원본 뷰 (전체 표시)        마스크 (불투명 영역만 통과)        결과
┏━━━━━━━━━━━━┓        ┏━━━━━━━━━━━━┓        ┏━━━━━━━━━━━━┓
┃████████████┃   +    ┃░░░░████░░░░┃   →    ┃░░░░████░░░░┃
┃████████████┃        ┃░░░░████░░░░┃        ┃░░░░████░░░░┃
┃████████████┃        ┃░░░░████░░░░┃        ┃░░░░████░░░░┃
┗━━━━━━━━━━━━┛        ┗━━━━━━━━━━━━┛        ┗━━━━━━━━━━━━┛
(모두 보임)              (가운데만 불투명)             (가운데만 보임)
```

- UIKit에서 이 "작은 네모"는 `UIView`나 `CALayer`가 담당합니다. 마스크의 알파 값이 1일수록 잘 보이고, 0이면 완전히 잘립니다.
- 결국 마스크는 **"무엇을 보여 주고, 무엇을 숨길지"**를 결정하는 투명도 필터이라고 기억하면 됩니다.

---

아주 기초적인 마스크 동작을 눈으로 확인하려면, 단 두 개의 `UIView`만으로도 충분합니다. 아래 예제는 **큰 사각형 뷰(`coloredView`)가 있고, 더 작은 뷰(`maskView`)를 마스크로 씌워 특정 영역만 보이도록** 만드는 과정입니다.

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
        // maskView 자체는 화면에 보이지 않지만, 알파(=불투명도) 정보로 coloredView를 잘라냅니다.
        let view = UIView(frame: CGRect(x: 0, y: 0, width: 160, height: 160))
        view.backgroundColor = .black   // 알파가 1인 영역만 원본이 보입니다.
        view.layer.cornerRadius = 80    // 모서리를 둥글게 만들어 원형 마스크를 만듭니다.
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
        // 마스크는 원본 뷰의 좌표계를 기준으로 배치해야 합니다.
        maskView.center = CGPoint(x: coloredView.bounds.midX, y: coloredView.bounds.midY)

        // 핵심: coloredView.mask에 UIView를 지정하면 maskView의 알파가 1인 부분만 그려집니다.
        coloredView.mask = maskView
    }
}
```

### 실행 결과
- `coloredView`는 240×240 크기의 사각형이지만, 마스크가 160×160이므로 **원형 영역 안쪽만** 화면에 나타납니다.
- `maskView`는 실제로 화면에 보이지 않습니다. 대신 그 위치와 모양이 `coloredView`의 "보이는 영역"을 결정합니다.

## 2. 마스크 이동/애니메이션으로 효과 확인하기
마스크 뷰 위치를 바꿔 보면, 원본 뷰도 함께 움직이는 것이 아니라 **보이는 영역만 이동**한다는 사실을 이해하기 쉽습니다.

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

- 애니메이션 동안 `coloredView.mask`에 지정된 뷰의 위치가 바뀌면, 그 경로에 따라 보이는 영역이 움직이며 마스크 효과를 직관적으로 확인할 수 있습니다.

## 3. 핵심 포인트 정리
- `UIView.mask`는 그 뷰 전체에 적용됩니다. 서브뷰나 레이어도 모두 같은 마스크 영향을 받습니다.
- 마스크 역할을 하는 뷰/레이어는 화면에 직접 표시되지 않으며, **알파 값이 1인 부분만 원본 뷰를 통과**시킵니다.
- 마스크 크기가 원본보다 작으면 일부만 보이고, 크거나 같은 경우는 전체가 보입니다.
- `maskView`에 `cornerRadius`나 `transform`, `path`(ShapeLayer를 덧씌우는 방식) 등을 적용하면 다양한 모양을 쉽게 만들 수 있습니다.
- 마스크 갱신 시에는 `maskView.frame`/`center`를 조정하거나 새로운 마스크 뷰를 다시 할당하면 됩니다.

이렇게 단순한 실험을 통해 마스크가 "뷰를 잘라내는 개념"이라는 점을 감각적으로 이해한 뒤, 더 복잡한 ROI/경로 조합으로 확장해 나가면 자연스럽게 실전에 적용할 수 있습니다.
