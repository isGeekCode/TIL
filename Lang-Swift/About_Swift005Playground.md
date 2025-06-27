# Playground에서 UIView를 그려보자

이 글은 사실 별게 없다.  

단지 playground에서 swift언어를 테스트할 때처럼  

UIKit클래스도 사용가능하다는 것을 소개하고 싶다.  

## UIKit을 돌린다?

우리가 처음에 Swift를 배울 때, playground를 사용해 간단하게 동작을 확인 할 수 있다.

UIKit에서 사용하는 UIView클래스들은 `(UIViewController같은 것들..)` 역시 클래스일 뿐이다.  

때문에 swift 구문 테스트와 동일하게 빠르게 테스트가 가능하다. 

## PlaygroundSupport

Swift Playgrounds와 같은 인터랙티브한 Swift 개발 환경에서 다양한 UI 요소 및 라이브 뷰를 통합하고 관리하는 데 도움을 주는 프레임워크다.  

Swift Playgrounds는 주로 학습 및 실험을 위한 환경이지만,  

PlaygroundSupport를 사용하면 Playgrounds에서 실제 앱에 가까운 UI와 기능을 개발하고 테스트할 수 있다.  

### 사용법
- import `PlaygroundSupport` , `UIKit`
- 코드 작성
- PlaygroundPage.current.liveView 에 확인하고 싶은 View를 지정한다.  


### 예제: View그려보기
```swift
import UIKit
import PlaygroundSupport

class MyView: UIView {
    override init(frame: CGRect) {
        super.init(frame: frame)
        setupUI()
    }
    
    required init?(coder aDecoder: NSCoder) {
        super.init(coder: aDecoder)
        setupUI()
    }
    
    private func setupUI() {
        backgroundColor = UIColor.systemYellow
        
        let label = UILabel()
        label.text = "Hello, Playground!"
        label.textAlignment = .center
        label.translatesAutoresizingMaskIntoConstraints = false
        
        addSubview(label)
        
        // Auto Layout 설정
        NSLayoutConstraint.activate([
            label.centerXAnchor.constraint(equalTo: centerXAnchor),
            label.centerYAnchor.constraint(equalTo: centerYAnchor)
        ])
    }
}

let viewController = UIViewController()
let customView = MyView(frame: CGRect(x: 0, y: 0, width: 200, height: 200))
viewController.view.addSubview(customView)
PlaygroundPage.current.liveView = viewController

```

<img width="600" alt="스크린샷 2023-08-30 오전 9 19 39" src="https://github.com/isGeekCode/TIL/assets/76529148/70078ed5-59b3-4031-9892-809e38d3ab79">


## 다양한 뷰를 보여줄 수 있다.
조금더 다양한 코드도 구현해서 viewControler자체를 동일하게 빌드할 수 있다.

심지어는 CollectionView 셀을 클릭했을 때, View가 변화하는 것도 볼 수 있다. 

다만, 살짝 버벅거리는 것을 보니.. 너무 큰 작업은 무리가 아닐까 싶지만.. 이렇게도 가능하다는 것

- [예시 코드](https://github.com/isGeekCode/TIL/blob/main/iOS-Architecture/Architecture_301_MVC_CollectionView.md)
<img width="600" alt="스크린샷 2023-08-30 오전 9 27 15" src="https://github.com/isGeekCode/TIL/assets/76529148/8070b382-8e60-4329-b18c-1d500178f89c">



## 선 그리기

UIBezierPath를 이용하면 선을 그려볼 수도 있다.  

아래는 간단한 그래프를 그려본 예제이다.  


```swift

import UIKit
import PlaygroundSupport

class GraphView: UIView {
    override func draw(_ rect: CGRect) {
        super.draw(rect)
        
        // 배경색 설정
        UIColor.lightGray.setFill()
        UIRectFill(rect)
        
        let path = UIBezierPath()
        path.lineWidth = 2
        
        // x축 그리기
        UIColor.black.setStroke()
        path.move(to: CGPoint(x: 0, y: bounds.height / 2))
        path.addLine(to: CGPoint(x: bounds.width, y: bounds.height / 2))
        path.stroke()
        
        // y축 그리기
        path.move(to: CGPoint(x: bounds.width / 2, y: 0))
        path.addLine(to: CGPoint(x: bounds.width / 2, y: bounds.height))
        path.stroke()
        
        // y = x 그래프 그리기 (빨간색)
        let graphPath = UIBezierPath()
        graphPath.lineWidth = 2
        UIColor.red.setStroke()
        
        for x in 0...Int(bounds.width) {
            let y = bounds.height - CGFloat(x)  // y = x 그래프의 식
            if x == 0 {
                graphPath.move(to: CGPoint(x: CGFloat(x), y: y))
            } else {
                graphPath.addLine(to: CGPoint(x: CGFloat(x), y: y))
            }
        }
        
        graphPath.stroke()
    }
}

let viewController = UIViewController()
let graphView = GraphView(frame: CGRect(x: 0, y: 0, width: 300, height: 300))
viewController.view.addSubview(graphView)
PlaygroundPage.current.liveView = viewController

```

- 빌드화면

<img width="400" alt="스크린샷 2023-08-30 오전 9 42 50" src="https://github.com/isGeekCode/TIL/assets/76529148/5b4ee062-a811-4450-ae69-e74bf9702850">





## History
- 230830 : 초안작성
