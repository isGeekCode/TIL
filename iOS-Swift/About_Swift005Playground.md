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


## History
- 230830 : 초안작성
