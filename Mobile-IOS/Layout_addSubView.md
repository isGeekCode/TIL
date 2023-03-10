# Layout - Hierarchy of UIView (feat. addSubView)


### 1. view의 계층구조는 superView, subView, siblingView 로 구성

- view의 계층구조는 superView, subView, siblingView 로 특정되며 이는 drawing순서를 결정짓는다.
- superView와 subView의 관계에서는 superView가 우선해서 그려진다.
- 동일한 superView 내부에 여러 siblingView가 있다면 먼저 addSubView가 된 순으로 drawing된다.
- siblingView가 겹쳐질 때는 , 먼저 drawing된 View가 가려진다.


### 2. superView와 subView의 계층 구조에 따른 몇가지 특징

- superView를 제거하면 subView도 함께 제거된다.
- superView의 투명도는 subView에도 적용된다.
- superView의 size가 변하면 subView에도 적용된다.
- superView는 subView를 array로 관리한다.

### 3. **subView 관리를 위한 methods**

```swift
// subView추가
superView.addSubView(_:)
// superView제거
removeFromSuperView()
// subView를 한번에 제거하는 함수는 없지만 아래 클로저를 통해 가능
superView.subviews.forEach {$0.removeFromSuperview()}

// view1을 추가
self.view.addSubview(self.view1)

// view1을 0번째에 삽입
self.view.insertSubview(view: self.view1, at: 0)

insertSubview(at:)
// 지정한 서브뷰 아래에 서브뷰를 추가
insertSubview(:belowSubview) 
// 지정한 서브뷰 위에 서브뷰를 추가
insertSubview(:aboveSubview)

// view1을 가장 앞으로
self.view.bringSubview(toFront: self.view1)

// view1을 가장 뒤로
self.view.sendSubview(toBack: self.view1)

// 0번째 view와 1번째 view의 위치를 변경한다.
self.view.exchangeSubview(at: 0, withSubviewAt: 1)

// subView에는 tag를 붙여 addSubView하기
subView.tag = 1
let assignSubView = superView.viewWithTag(1) 
//assignSubView는 subView를 가리킴

//특정 View를 superView인지 확인
let superView = UIView()
let subView = UIView()

superView.addSubview(subView)

let isSuperView: Bool = subView.isDescendant(of: superView)
print(isSuperView) // true
```

그외 다양한 함수로 View를 동적으로 관리가 가능

• willRemoveSubview(*:),* 

*didAddSubview(*:) 

willMove(toSuperview:), 

didMoveToSuperview willMove(toWindow:),

didMoveToWindow
