오토레이아웃의 개념

레이아웃을 자동으로 계산


## Anchor
View를 액자라고 생각하고 전체 화면을 벽이라고 생각하자.

<img width="132" alt="스크린샷 2022-11-07 오전 11 14 25" src="https://user-images.githubusercontent.com/76529148/200213282-481e1bd7-5c5e-4ce9-a4be-b72199f47880.png">


액자는 걸지않으면 아래로 떨어지기때문에 Anchor(앙카)를 달아주어야한다. 자리를 잡으면 파란색 잡지못하면 빨간색으로 표시된다.

오토레이아웃의 성립조건

1. 너비와 높이 지정 : 스크린사이즈를 기반으로 뷰의 크기 설정
    - width
    - height
2. 위치 지정 : 앵커로 설정
    - 가로 → X축
    - 세로 → Y축

뷰를 기준으로 앵커를 양옆에 달아주면 Xcode자체에서는 기기의 화면을 알고있기 때문에 자동으로 크기를 잡아줄 수가 있다.

## Constraint

- First item: X를
- Second item: Y로부터
- Constraint 만큼

오토레이아웃을 잡을 뷰의 이름이 헷갈린다면 이름을 수정해서 확인해볼 수 있다.

First item: MainView.Leading

Second item: Safe Area Leading

Constraint : 100

이부분을 해석하면 아래와 같다

`MainView`의 Leading을 

`Safe Area Leading`으로부터 100 만큼 떨어지게 둔다.

## Align

앵커는 Top, Bottom, Leading, Ttrailing이 존재한다. 그외에도 

선택한 요소들을 특정 기준에 맞게 정렬하는 방법도 있다.

각 앵커의 TBLT에 맞게 맞출 수도 있고, Horizontal, Vertical의 중아에 맞게 설정또한 가능하다.


## IBDesignable & IBInspectable

### View의 외곽 라인 라운딩처리하기

TestView.layer.cornerRadius = 20

→ 그림자나 외곽선 같은 경우는 Layer에 접근한다.

```swift
// MARK: Step 1. 클래스 구현

@IBDesignable
class CustomView: UIView {

	@IBInspectable
	var cornerRadius: CGFloat = 0 {
		// 값이 설정될 때 알 수 있음
		didSet {
			self.layer.cornerRadius = cornerRadius
		}
	}
}

// MARK: Step 2. 스토리보드에서 원하는 뷰 클래스를 CustomView로 변경

// MARK: Step 3. 적용할 ViewController의 생명주기에 맞게 접근하여 값 부여
class MainViewController: UIViewController {

	IBOutlet var testVIew: CustomView!

	override func viewDidLoad() {
		super.viewDidLoad()

		testView.cornerRadius = 10

		// CustomView IBInspectable세팅을 안해둔 경우
		testView.layer.cornerRadius = 10
	}
}
```

아래와 같이 설정을 한다음, 스토리보드에서 클래스를 CustomView로 설정한다면   

ViewDidLoad 에서 layer를 생략하고 바로 접근이 가능하다.

### IBInspectable

@ 어노테이션으로 IBInspectable를 추가하면 새로 didSet세팅한 항복을 스토리보드의 인스펙터패널에서  GUI로 슬롯이 생성된다.

### IBDesignable

@ 어노테이션으로 IBDesignable를 추가하면 IBInspectable로 생성된 슬롯의 값을 바꿀때 바로바로 스토리보드에서 변화를 확인 할 수가 있다.