# present - UIKit to SwiftUI

## 참고링크
- [TIL : UIKit으로 구현된 화면에 SwiftUI View를 추가하기 : UIHostingController](https://github.com/isGeekCode/TIL/blob/main/iOS-SwiftUI_UIKit/PreviewProvider_UIHostingController.md)


UIHostingController를 사용하면 UIKit내부에서 SwiftUI를 ViewController처럼 취급해서 처리할 수 있다.


이 글에서 다룰 내용은 아래와 같다.

## 순서
- [1. UIKit에서 SwiftUI를 present하기](#UIKit에서-SwiftUI를-present하기)
- [2. SwiftUI dismiss하기](#SwiftUI-dismiss하기)
    - [2.1. 클로저로 dismiss하기](#클로저로-dismiss하기)
    - [2.2. delegate함수를 이용해 dismiss하기](#delegate함수를-이용해-dismiss하기)
    - [2.3. SwiftUI presentationMode를 이용해 dismiss하기](#SwiftUI-presentationMode를-이용해-dismiss하기)

### 적용한 화면
모두 동일한 결과 화면을 보인다.  

<img width="300" alt="ezgif-5-a9cfe89f2d" src="https://github.com/isGeekCode/TIL/assets/76529148/5916aa41-6746-4bb4-b94f-542898e63460">

<br>

- [[TOP]](#순서)

<br><br><br>


## UIKit에서 SwiftUI를 present하기

상단의 참고링크를 보면 더 자세한 내용을 확인 가능하다.

```SWIFT
import UIKit
import SwiftUI

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        view.backgroundColor = .systemPink
        
        let button = UIButton()
        // .. 제약조건
        
        button.addTarget(self, action: #selector(buttonTapped), for: .touchUpInside)
    }
    
    // 버튼 액션 구현
    @objc func buttonTapped() {
        let swiftUIView = SwiftUIView(textValue: "This is in SwiftUI", dismissHandler: {
        
            // SwiftUI에서 버튼을 누르면 모달을 닫기
            self.dismiss(animated: true, completion: nil) 
        })

        let hostingController = UIHostingController(rootView: swiftUIView)
        present(hostingController, animated: true, completion: nil)
    }
}

struct SwiftUIView: View {
    
    @State var textValue: String

     // 모달 닫기용 closure
    var dismissHandler: (() -> Void)?

    var body: some View {
        GeometryReader { geometry in
            
            Button(action: {
                // 버튼을 누르면 모달을 닫기 위해 dismissHandler 호출
                self.dismissHandler?() 
            }, label: {
                Text(textValue)
                    .foregroundColor(.black)
            })
            .frame(width: 150, height: 150)
            .background(.green)
            
            // 현재 화면에 크기 부여
            .frame(width: geometry.size.width, height: geometry.size.height)
            .background(.yellow)
        }
    }
}


struct MyViewControllerWrapper: UIViewControllerRepresentable {
    func makeUIViewController(context: Context) -> ViewController {
        return ViewController()
    }

    func updateUIViewController(_ uiViewController: ViewController, context: Context) {
        // UIViewController가 업데이트되었을 때 필요한 로직이 있다면 여기에 작성
    }
}

struct MyViewControllerWrapper_Previews: PreviewProvider {
    static var previews: some View {
        MyViewControllerWrapper()
    }
}

```
    
<br>

- [[TOP]](#순서)

<br><br><br>


## SwiftUI dismiss하기


### 클로저로 dismiss하기

- 1. SwiftUI의 변수로 클로저를 세팅한다. 
- 2. SwiftUI의 dismiss를 원하는 시점에 해당 클로저를 세팅한다. 
- 3. 이 SwiftUI를 감싼 UIHostingController를 init하는 시점에 클로저 변수에 hostingController.dismiss 함수를 세팅한다.


```SWIFT
import UIKit
import SwiftUI

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        view.backgroundColor = .systemPink
        
        let button = UIButton()
        // .. 제약조건
        
        button.addTarget(self, action: #selector(buttonTapped), for: .touchUpInside)
    }
    
    // 버튼 액션 구현
    @objc func buttonTapped() {
        let swiftUIView = SwiftUIView(textValue: "This is in SwiftUI", dismissHandler: {
        
            // SwiftUI에서 버튼을 누르면 모달을 닫기
            self.dismiss(animated: true, completion: nil) 
        })

        let hostingController = UIHostingController(rootView: swiftUIView)
        present(hostingController, animated: true, completion: nil)
    }
}

struct SwiftUIView: View {
    
    @State var textValue: String

     // 모달 닫기용 closure
    var dismissHandler: (() -> Void)?

    var body: some View {
        GeometryReader { geometry in
            
            Button(action: {
                // 버튼을 누르면 모달을 닫기 위해 dismissHandler 호출
                self.dismissHandler?() 
            }, label: {
                Text(textValue)
                    .foregroundColor(.black)
            })
            .frame(width: 150, height: 150)
            .background(.green)
            
            // 현재 화면에 크기 부여
            .frame(width: geometry.size.width, height: geometry.size.height)
            .background(.yellow)
        }
    }
}


struct MyViewControllerWrapper: UIViewControllerRepresentable {
    func makeUIViewController(context: Context) -> ViewController {
        return ViewController()
    }

    func updateUIViewController(_ uiViewController: ViewController, context: Context) {
        // UIViewController가 업데이트되었을 때 필요한 로직이 있다면 여기에 작성
    }
}

struct MyViewControllerWrapper_Previews: PreviewProvider {
    static var previews: some View {
        MyViewControllerWrapper()
    }
}

```

<br>

- [[TOP]](#순서)

<br><br><br>

### delegate함수를 이용해 dismiss하기

이방법은 가장 무난한 방법이 아닐까 생각한다.  

  

```swift
// 프로토콜 생성
protocol SwiftUIViewDelegate: AnyObject {
    // 생성한 SwiftUI View를 닫기위한 방법
    func swiftUIViewDidDismiss()
}

// 프로토콜 채택
class ViewController: UIViewController, SwiftUIViewDelegate {

    override func viewDidLoad() {
        super.viewDidLoad()

        view.backgroundColor = .systemPink
        
        let button = UIButton()
        // 버튼 생성관련 코드 생략
        button.addTarget(self, action: #selector(buttonTapped), for: .touchUpInside)
    }
    
    @objc func buttonTapped() {
        var swiftUIView = SwiftUIView(textValue: "This is in SwiftUI")

        // delegate 선언
        swiftUIView.delegate = self
        
        let hostingController = UIHostingController(rootView: swiftUIView)
        present(hostingController, animated: true, completion: nil)
    }

    // Delegate method to handle dismissal
    func swiftUIViewDidDismiss() {
        dismiss(animated: true, completion: nil)
    }

}

struct SwiftUIView: View {
    
    // delegate 변수생성
    weak var delegate: SwiftUIViewDelegate?

    @State var textValue: String

    var body: some View {
        GeometryReader { geometry in
            
            Button(action: {
            
            
                // 버튼을 누르면 모달을 닫기 위해 dismiss 호출
                delegate?.swiftUIViewDidDismiss()
                
            }, label: {
                Text(textValue)
                    .foregroundColor(.black)
            })
            .frame(width: 150, height: 150) // 버튼의 크기를 200x200으로 설정
            .background(.green) // 배경색을 시스템 그린으로 설정
            
            // 현재 화면에 크기 부여
            .frame(width: geometry.size.width, height: geometry.size.height)
            .background(.yellow)
        }
    }
}

```

<br>

- [[TOP]](#순서)

<br><br><br>

### SwiftUI presentationMode를 이용해 dismiss하기

이 방법은 좀더 SwiftUI스러운 방법이다. 

띄울때는 상단과 비슷하지만 클로저 변수가 이제 사라졌다.


```SWIFT
//UIKit 부분

    @objc func buttonTapped() {
        let swiftUIView = SwiftUIView(textValue: "This is in SwiftUI")
        let hostingController = UIHostingController(rootView: swiftUIView)
        present(hostingController, animated: true, completion: nil)
    }


//SwiftUI부분

struct SwiftUIView: View {
    
    @State var textValue: String
    
    
    @Environment(\.presentationMode) var presentationMode

    var body: some View {
        GeometryReader { geometry in
            
            Button(action: {
                // 버튼을 누르면 모달을 닫기 위해 dismiss 호출
                self.presentationMode.wrappedValue.dismiss()

            }, label: {
                Text(textValue)
                    .foregroundColor(.black)
            })
            .frame(width: 150, height: 150) // 버튼의 크기를 200x200으로 설정
            .background(.green) // 배경색을 시스템 그린으로 설정
            
            // 현재 화면에 크기 부여
            .frame(width: geometry.size.width, height: geometry.size.height)
            .background(.yellow)
        }
    }
}


```

여기서 `@Environment(\.presentationMode)`은  

SwiftUIView가 present된 상태에서 모달을 닫기 위해 사용되는 환경 속성이다.

presentationMode 속성을 사용하여 모달을 닫기 위해 `self.presentationMode.wrappedValue.dismiss()`를 호출한다.  

<br>

- [[TOP]](#순서)

<br><br><br>

## History
- 230804: 초안작성
