# NSObject_UIResponder_UIView_UIScrollView

UIScrollView는 iOS 앱에서 스크롤 가능한 컨텐츠를 제공하기 위해 사용되는 뷰. 

또한 사용자가 화면을 스크롤하여 보이지 않는 부분의 컨텐츠를 볼 수 있게 한다. 

주로 이미지 뷰어, 웹 브라우저, 맵 뷰 등에서 사용된다.

특히!! 우리에게 익숙한 UITableView, UITextView의 상위 클래스다. 그래서 스크롤이 된다!!

<br><br>

## 포함된 주요 구성 요소

- Scroll Indicators: 사용자가 스크롤할 수 있는지를 나타내는 인디케이터. 수평 및 수직 스크롤 인디케이터를 모두 제공할 수 있다.
- contentOffset : 스크롤 뷰 내용의 현재 오프셋을 나타내는 CGPoint. 스크롤 위치를 나타내며, 이 값을 변경하여 스크롤 위치를 제어할 수 있다.
- contentSize: 스크롤 뷰의 컨텐츠 크기를 나타내는 CGSize. 컨텐츠의 실제 크기를 설정하여 스크롤 영역을 결정할 수 있다.

- isTracking : 현재 스크롤 뷰가 사용자의 터치를 추적하고 있는지 여부를 나타내는 불리언 값. 터치가 추적 중인지 확인할 때 사용된다.

<br><br>

## 스크롤뷰에서 이해해야하는 것
(Content Layout 영역 >= Frame Layout 영역)
- Content Layout
    - 실제로 스크롤해서 보여질 전체 뷰를 담는 Layout
    - 1~3번중 한 방식으로 스크롤 영역을 지정해야한다. 
        - 1. Costraints 설정: 내부에 필요한 만큼 컨텐츠를 추가하고, 마지막에 scrollView 스크롤 영역 끝을 지정해야한다. 
        - 2. ContentSize 설정 : `scrollView.contentSize = CGSize(width:height:)`로 크기를 지정해준다.  
        - 3. 스토리보드로 지정하는 경우, SizeInspector 에서 변경
            - Simulated Size: Freeform으로 변경
            - Height: 원하는 사이즈만큼 변경 (이 때, ViewController가 늘어나 보이니 놀라지 말자.)
- Frame Layout
    - 스크린에 보이는 만큼의 Layout
    - 우리가 AutoLayout Constraints를 설정하는 영역

<br><br>

## UIScrollViewDelegate
UIKit에서 많은 객체들이 Delegate를 갖고있는 것처럼, UIScrollView도 고유한 기능을 가지고 있다.  


- scrollViewDidScroll(_:)
    - 이 메서드는 스크롤 뷰가 스크롤되는 동안 호출된다. 스크롤의 변화를 감지하고 해당 정보를 사용하여 UI를 업데이트하거나 다른 동작을 수행할 수 있다.
- scrollViewWillBeginDragging(_:)
    - 사용자가 스크롤을 시작할 때 호출된다. 스크롤이 시작되기 전에 필요한 작업을 수행할 수 있다.
- scrollViewDidEndDragging(_:willDecelerate:)
    - 사용자가 스크롤 동작을 끝낸 후에 호출된다. 두 번째 매개변수 willDecelerate는 스크롤이 감속될 것인지 여부를 나타낸다.
- scrollViewWillBeginDecelerating(_:)
    - 스크롤이 감속되기 시작할 때 호출된다. 스크롤이 감속되기 전에 필요한 작업을 수행할 수 있다.
- scrollViewDidEndDecelerating(_:)
    - 스크롤이 감속을 마친 후 호출된다. 스크롤 감속이 완료된 후에 필요한 작업을 수행할 수 있다.

<br><br>

응용방법은 아래와 같이 사용할 수 있다. 

```swift
func scrollViewDidScroll(_ scrollView: UIScrollView) {
    // 스크롤 동작 감지 및 처리
        
    // 응용 1. 패럴랙스(Parallax) 효과 추가하기
    // 이미지나 뷰를 스크롤과 함께 이동시켜 패럴랙스 효과를 만들 수 있다.
    let offsetY = scrollView.contentOffset.y
    imageView.frame.origin.y = -offsetY * 0.5 // 스크롤 속도에 따라 이미지 이동
    
    // 응용 2. 네비게이션 바(또는 다른 UI 요소)의 투명도 조절하기
    // 스크롤 위치에 따라 네비게이션 바의 투명도를 조절하여 스크롤이 일어날 때 UI를 조절할 수 있다.
    let offsetY = scrollView.contentOffset.y
    let threshold: CGFloat = 100.0 // 스크롤 내리는 거리 임계값
    
    if offsetY > threshold {
        let alpha = min(1.0, (offsetY - threshold) / threshold)
        navigationController?.navigationBar.alpha = alpha
    } else {
        navigationController?.navigationBar.alpha = 0.0
    }
    
    // 응용 3. 무한 스크롤 (Infinite Scrolling) 구현하기
    // 스크롤이 특정 위치에 도달하면 새로운 데이터를 로드하여 무한 스크롤을 구현할 수 있다.
    let offsetY = scrollView.contentOffset.y
    let contentHeight = scrollView.contentSize.height
    let scrollViewHeight = scrollView.bounds.height
    
    if offsetY > contentHeight - scrollViewHeight {
        // 끝에 다가왔을 때 추가 데이터 로드
        loadMoreData()
    }
    
    // 응용 4. 스크롤 위치에 따라 UI 업데이트하기:
    // 스크롤 위치에 따라 UI 엘리먼트의 속성을 변경하여 동적인 효과를 추가할 수 있다.
    let offsetY = scrollView.contentOffset.y
    
    if offsetY > 200 {
        titleLabel.textColor = .white
    } else {
        titleLabel.textColor = .black
    }
}

func scrollViewWillBeginDragging(_ scrollView: UIScrollView) {
    // 스크롤 시작 전 작업 처리
    
    // 응용 1. 스크롤 시작 시 UI 요소 숨기기
    // 사용자가 스크롤을 시작하면 추가적인 정보를 보여주는 UI 요소를 숨기는 것이 좋을 때 사용할 수 있다.
    UIView.animate(withDuration: 0.3) {
        self.additionalInfoView.alpha = 0.0 // 추가 정보 뷰 숨기기
    }

    // 응용 2. 키보드 숨기기:
    // 사용자가 스크롤을 시작할 때 키보드가 열려있을 경우, 스크롤을 시작하면 키보드를 자동으로 숨기는 작업을 수행할 수 있다.
    view.endEditing(true) // 키보드 숨기기

    // 응용 3. 스크롤 시작 시 애니메이션 추가:
    // 스크롤을 시작하면 UI 요소에 애니메이션을 추가하여 부드러운 전환 효과를 제공할 수 있다.
    UIView.animate(withDuration: 0.3) {
        self.titleLabel.transform = CGAffineTransform(scaleX: 1.2, y: 1.2) // 제목 라벨 확대
    }

}

func scrollViewDidEndDragging(_ scrollView: UIScrollView, willDecelerate decelerate: Bool) {
    if !decelerate {
        // 원하는 로직 추가
    }

    // 응용 1. 스크롤 정지 시 추가 데이터 로드하기:
    // 사용자가 스크롤을 끝내면 스크롤이 정지된 상태에서 추가 데이터를 로드하여 무한 스크롤을 구현할 수 있다.
    if !decelerate {
        loadMoreData() 
    }

}

func scrollViewWillBeginDecelerating(_ scrollView: UIScrollView) {
    // 스크롤 감속 시작 전 작업 처리
}

func scrollViewDidEndDecelerating(_ scrollView: UIScrollView) {
    // 스크롤 감속 완료 후 작업 처리
}
```

<br><br>

## 자주 하는 실수
- Bottom의 존재
    - 한 화면에 UIScrollView를 구현하고, 내부적으로 컨텐츠를 넣는 경우가 있다.  이 때, 스크롤 끝을 지정하지 않으면 내부에 있는 objc 메서드들이 동작하지 않는다.  
<br>
<br><br>

## History
- 230508 : 초안작성
- 230901 : ContentView삭제 (ScrollView -> Cell 영역으로 이동)
- 230901 : UIScrollViewDelegate 추가
