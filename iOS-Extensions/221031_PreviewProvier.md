# UIKit에서 SwiftUI의 Preview를 사용하는 방법

앱개발을 하는 중 UI작업을 할 때, 시각적으로 확인을 해야하는 경우가 생긴다. 물론 소규모의 앱이나 작업에서는 매번 빌드하는 것이 나쁘지않지만,

해당 페이지가 세부적인 항목이라 여러번 클릭하고 대기하고 심지어는 빌드시간이 오래걸린다면.. 우리는 많은 스트레스를 받게된다.
실제로 회사에서 빌드하는데 정말 많은 시간을 보내고, 그때마다 흐름이 끊기는 것을 경험한다.

이를 해결하기위해 여러 방면을 찾아보았다.

첫번째 방법은 SwiftUI의 Preview를 사용하는 방법이다. 하지만 단점은 SwiftUI를 사용해야 해당 기능을 킬수 있다는 것이었다. 아직 나의 작업환경이 구버전이기 때문에 대부분 UIKit 혹은 Objc라 엄두를 못내고 있었다.

두번째 방법은 최근 Let us Swift 2022 여름 세미나에서 Inject를 사용하는 방법을 상세히 알려주셔서 사용하고 있었다. 다만 Inject는 몇가지 세팅을 해야한다는 단점이 있었다. 그래서 세팅하는 데 굉장히 많은 삽질을 했다.

그러던 중 첫번째 방법인 SwiftUI의 Provider를 UIKit에서 사용할 수 있다는 방법을 알게돼 여기에 소개해보려고 한다.
UIView 여러개를 다중으로 사용하는 것도 가능하지만 몇 가지 더 써넣어야하고, 어차피 나는 대부분 UIViewController만 확인하면 되기때문에 비교적 간단한 UIViewController에 적용하는 것만 소개하려고 한다. 다중사용에 대한 링크는 참고링크를 확인.

![img](https://user-images.githubusercontent.com/76529148/198916009-892d1701-944e-4fcd-b5a6-0321256476f7.gif)
<p align="center">
    <a href="https://ios-development.tistory.com/488" style="text-align: center;">이미지 출처 : 김종권의 iOS 앱 개발 알아가기</a>
</p>

### 📌 참고링크

- 애플문서: [https://developer.apple.com/documentation/swiftui/previewprovider](https://developer.apple.com/documentation/swiftui/previewprovider)
- 다중사용: [https://ios-development.tistory.com/488](https://ios-development.tistory.com/488)
### 📌 지원

- iOS 13.0+

## 📌 적용방법

### 🍊 Step1. 별도의 Extension 구현

```swift
import UIKit
import SwiftUI

#if DEBUG
extension UIViewController {
    private struct Preview: UIViewControllerRepresentable {
        let viewController: UIViewController

        func makeUIViewController(context: Context) -> UIViewController {
            return viewController
        }

        func updateUIViewController(_ uiViewController: UIViewController, context: Context) {
        }
    }

    func toPreview() -> some View {
        Preview(viewController: self)
    }
}

extension UIView {
    private struct Preview: UIViewRepresentable {
        typealias UIViewType = UIView
        let view: UIView

        func makeUIView(context: Context) -> UIView {
            return view
        }

        func updateUIView(_ uiView: UIView, context: Context) {
        }
    }

    func toPreview() -> some View {
        Preview(view: self)
    }
}
#endif
```

### 🍊 Step2. 사용할 UIView 혹은 UIViewController하단에 구조체 구현

```swift
#if canImport(SwiftUI) && DEBUG
import SwiftUI

// 이 부분은 아무 이름이나 넣어도 상관없다.
struct <#ViewController#>Preview: PreviewProvider {

    // 이 부분은 내가 사용하려는 ViewController / View 객체를 생성한다.
    static var previews: some View {
        <#ViewController#>().toPreview()
    }
}
#endif
```

### 🍊 Step **3. Resume버튼 클릭하여 실시간 업데이트 활성화**

‼️ preview가 안나오는 경우 Canvas를 눌러서 빌드

![img1 daumcdn-6](https://user-images.githubusercontent.com/76529148/198916117-109d460e-9b22-475b-8d7c-60263d868421.png)


## 👍  Tip: 다중 기기 확인하기
기존에는 여러 기기를 세로로 동시에 볼 수 있었지만 업데이트 된 이후, 기기마다 클릭해서 확인 할 수 있다.
다만, 이것도 최초 클릭시에는 약간의 시간이 걸린다.


```swift
#if DEBUG
import SwiftUI

@available(iOS 13.0, *)
struct <#ViewController#>Preview: PreviewProvider {
        // Device 배열로 여러 개의 디바이스에 적용된 모습을 같이 확인할 수 있다.
    static var devices = ["iPhone 14 Pro Max", "iPhone 14 Pro", "iPhone SE (2nd generation)"]

    static var previews: some View {

        ForEach(devices, id: \.self) { deviceName in
            MainViewController()  // 스토리보드 대신 ViewController의 인스턴스를 직접 생성합니다.
//            UIStoryboard(name: "Main", bundle: nil).instantiateViewController(identifier: "ViewController")
                .toPreview()
                .previewDevice(PreviewDevice(rawValue: deviceName))
                .previewDisplayName(deviceName)
        }
    }
}
#endif
```

### 적용 이미지
<img width="400" alt="스크린샷 2023-07-17 오후 3 08 34" src="https://github.com/isGeekCode/TIL/assets/76529148/cba74268-c446-43b1-915f-453c780b4e27">




## 👍  Tip: Snippet에 넣어서 사용하기

<img width="848" alt="스크린샷 2022-10-13 오후 12 56 51" src="https://user-images.githubusercontent.com/76529148/198915921-4b07d3b8-197e-4371-beea-4cd8fd169582.png">




## History
- 221031 : 초안작성
- 230717 : 다중 기기 적용화면 세팅방법 추가
