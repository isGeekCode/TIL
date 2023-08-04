# UIKit에서 SwiftUI의 Preview 사용하기

ViewController의 UI를 생성하다보면 빌드하는데 정말 많은 시간이 소요된다.  

SwiftUI의 장점은 빠르게 UI를 확인하면서 구현하는게 가능한데, 이걸 가능하게 하는 Provider를   

사용가능하게 하는 방법이다.

## 주요 키워드
- UIViewControllerRepresentable
- PreviewProvider

## 흐름

- UIViewController준비
- UIViewControllerRepresentable를 통해 SwiftUI 의 View로 리턴
- 리턴받은 View를 Preview로 표시

## 염두해야할 점

구현된 UI중 색상과 같은 건 바로바로 Preview를 통해 변하는데,  

Constraint의 값이 바뀌는 것은 바로 반영이 안되어서 Preview를 refresh해줘야 한다.  

단축키는 `option + command + p`이다.  

익숙해지는데 아주 조금의 시간이 걸렸다.  

## 사용법

```SWIFT

import UIKit
import SwiftUI

class ViewController: UIViewController { 

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemYellow
    }
}

// 프로토콜을 통해 UIViewController를 SwiftUI의 View로 리턴하는 구조체
struct MyViewControllerWrapper: UIViewControllerRepresentable {
    func makeUIViewController(context: Context) -> ViewController {
        return ViewController()
    }

    func updateUIViewController(_ uiViewController: ViewController, context: Context) {
        // UIViewController가 업데이트되었을 때 필요한 로직이 있다면 여기에 작성
    }
}

// SwiftUI의 View를 Preview로 보여주는 구조체
struct MyViewControllerWrapper_Previews: PreviewProvider {
    static var previews: some View {
        MyViewControllerWrapper()
    }
}
```

<br><br>

## 기기별 보기

만약 기기별로 보고 싶다면 PreviewProvider 구현부에 Group으로 구현한다.  

그러면 Preview부분에 기기별 탭이 생성된다.  

> 최초로 누를때는 렌더링에 시간이 걸리는것을 참고!!

```SWIFT

struct MyViewControllerWrapper_Previews: PreviewProvider {
    static var previews: some View {
        Group {
            MyViewControllerWrapper()
                .previewDevice(PreviewDevice(rawValue: "iPhone SE (2nd generation)"))
                .previewDisplayName("iPhone SE (2nd generation)")

            MyViewControllerWrapper()
                .previewDevice(PreviewDevice(rawValue: "iPhone 13 Pro"))
                .previewDisplayName("iPhone 13 Pro")
        }
    }
}


```




## History
- 230804 : 초안작성
