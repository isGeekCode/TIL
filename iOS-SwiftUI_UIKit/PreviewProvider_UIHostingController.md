# UIKit으로 구현된 화면에 SwiftUI View를 추가하기 : UIHostingController

> 이 글은 SwiftUI의 UIHostingController 사용법을 설명한 글이다. 

viewController가 있다고 가정하자.

```swift
class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        view.backgroundColor = .systemGreen
    }
}
```

여기에 아래와 같은 SwiftUI를 추가하고 싶다.

```swift
struct SwiftUIView: View {
    
    var body: some View {
        GeometryReader { geometry in
            
            VStack {
                Text("This is in SwiftUI")
            }
            
            // VStack을 GeometryReader의 크기와 일치시키기
            .frame(width: geometry.size.width, height: geometry.size.height)
            .background(Color.yellow) // 배경색을 노란색으로 설정
        }
    }
}
```

하지만 UIKit에서는 UIView를 addSubView할 수는 있어도, SwiftUI의 View타입을 추가할 수는 없다. 

이때 필요한 것이 UIHostingController이다. 

> UIHostingController는 파라미터로 SwiftUI의 View를 받아서,
> UIKit의 UIViewController처럼 동작하게 해준다. 

그래서 아래와 같이 사용한다.

```SWIFT
import UIKit
import SwiftUI  // UIHostingController는 여기 포함된다.

class viewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        view.backgroundColor = .systemGreen

        // SwiftUI의 View INIT
        let swiftUIView = SwiftUIView()
        let hostingController = UIHostingController(rootView: swiftUIView)

        addChild(hostingController)
        view.addSubview(hostingController.view)
        
        // 제약조건 세팅
        hostingController.view.translatesAutoresizingMaskIntoConstraints = false
        NSLayoutConstraint.activate([
            hostingController.view.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            hostingController.view.centerYAnchor.constraint(equalTo: view.centerYAnchor),
            hostingController.view.widthAnchor.constraint(equalTo: view.widthAnchor, multiplier: 0.7),
            hostingController.view.heightAnchor.constraint(equalTo: view.heightAnchor, multiplier: 0.7)
        ])

        // 추가한다음 부모에게 이 객체가 추가되었음을 알리는 메서드
        hostingController.didMove(toParent: self)
    }
}
```


이렇게 하면 추가가 가능하다.  다만 이렇게만 하면 SwiftUI를 쓰는 이유중 하나인 Preview가 사라지니 아래 내용을 추가한다.  


```SWIFT
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

### 전체코드 : UIHostingController

```swift
import UIKit
import SwiftUI  // UIHostingController는 여기 포함된다.

class viewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        view.backgroundColor = .systemGreen

        // SwiftUI의 View INIT
        let swiftUIView = SwiftUIView()
        let hostingController = UIHostingController(rootView: swiftUIView)

        addChild(hostingController)
        view.addSubview(hostingController.view)
        
        // 제약조건 세팅
        hostingController.view.translatesAutoresizingMaskIntoConstraints = false
        NSLayoutConstraint.activate([
            hostingController.view.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            hostingController.view.centerYAnchor.constraint(equalTo: view.centerYAnchor),
            hostingController.view.widthAnchor.constraint(equalTo: view.widthAnchor, multiplier: 0.7),
            hostingController.view.heightAnchor.constraint(equalTo: view.heightAnchor, multiplier: 0.7)
        ])

        // 추가한다음 부모에게 이 객체가 추가되었음을 알리는 메서드
        hostingController.didMove(toParent: self)
    }
}

// MARK: 추가할 View
struct SwiftUIView: View {
    
    var body: some View {
        GeometryReader { geometry in
            
            VStack {
                Text("This is in SwiftUI")
            }
            
            // VStack을 GeometryReader의 크기와 일치시키기
            .frame(width: geometry.size.width, height: geometry.size.height)
            .background(Color.yellow) // 배경색을 노란색으로 설정
        }
    }
}

// MARK: Preview 활성화
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


### 제약조건을 더 추가한 예제
이건 위 사례에 hostingController를 앵커로 잡아서 UILabel을 추가한 사례이다. 

```swift
import UIKit
import SwiftUI

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        view.backgroundColor = .systemGreen
        let swiftUIView = SwiftUIView()
        let hostingController = UIHostingController(rootView: swiftUIView)

        addChild(hostingController)
        view.addSubview(hostingController.view)

        hostingController.view.translatesAutoresizingMaskIntoConstraints = false
        NSLayoutConstraint.activate([
            hostingController.view.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            hostingController.view.centerYAnchor.constraint(equalTo: view.centerYAnchor),
            hostingController.view.widthAnchor.constraint(equalTo: view.widthAnchor, multiplier: 0.7),
            hostingController.view.heightAnchor.constraint(equalTo: view.heightAnchor, multiplier: 0.7)
        ])

        hostingController.didMove(toParent: self)

        let topLabel = UILabel()
        topLabel.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(topLabel)

        NSLayoutConstraint.activate([

            topLabel.widthAnchor.constraint(equalToConstant: 300),
            topLabel.heightAnchor.constraint(equalToConstant: 50),
            topLabel.bottomAnchor.constraint(equalTo: hostingController.view.topAnchor, constant: -30), // 이 부분 수정
            topLabel.centerXAnchor.constraint(equalTo: hostingController.view.centerXAnchor)
        ])

        topLabel.backgroundColor = .systemBlue
        topLabel.text = "This is in UIKit"
        topLabel.textAlignment = .center
    }
}

struct SwiftUIView: View {
    
    var body: some View {
        GeometryReader { geometry in
            
            VStack {
                Text("This is in SwiftUI")
            }
            
            // VStack을 GeometryReader의 크기와 일치시키기
            .frame(width: geometry.size.width, height: geometry.size.height)
            .background(Color.yellow) // 배경색을 노란색으로 설정
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
  
  
### 실행화면

<img width="500" alt="스크린샷 2023-08-04 오후 2 21 25" src="https://github.com/isGeekCode/TIL/assets/76529148/cd9307c5-371d-49a4-a69a-c8a4c732e41d">


## HostingController로 데이터 넘기기

위에서 HostingController는 SwiftUI로 구현된 View를 UIViewController처럼 사용할 수 있다고 했다.  


그렇다면 INIT할 때 데이터도 넘어갈까?????  

그래서 SwiftUI view객체에 변수를 추가했다.

이 예제엔 초기값이 없다.

```SWIFT

struct SwiftUIView: View {
    
    // 변수 추가
    @State var textValue: String

    
    var body: some View {
        GeometryReader { geometry in
            
            VStack {
                Text(textValue) // 변수 부여
            }
            
            // VStack을 GeometryReader의 크기와 일치시키기
            .frame(width: geometry.size.width, height: geometry.size.height)
            .background(Color.yellow) // 배경색을 노란색으로 설정
        }
    }
}

```

그러면 hostingController로 연결하기위해 SwiftUI View를 초기화하면서 인자를 넣어주어야한다.  

```SWIFT

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        view.backgroundColor = .systemPink
        
        // 변수에 텍스트 선언
        let swiftUIView = SwiftUIView(textValue: "This is in SwiftUI")
        let hostingController = UIHostingController(rootView: swiftUIView)

        .. 이하 생략
```

SwiftUI에는 text가 없지만 UIHostingController를 통해 View를 init하면서 넣어줬기 때문에,   

최종화면에는 text가 들어간 모습을 볼 수 있다.

### 실행화면

<img width="500" alt="스크린샷 2023-08-04 오후 2 32 31" src="https://github.com/isGeekCode/TIL/assets/76529148/6a9ab50a-99aa-4149-86d6-b0bdc766125a">


### 전체코드

```SWIFT
import UIKit
import SwiftUI

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        view.backgroundColor = .systemPink
        let swiftUIView = SwiftUIView(textValue: "This is in SwiftUI")
        let hostingController = UIHostingController(rootView: swiftUIView)

        addChild(hostingController)
        view.addSubview(hostingController.view)

        hostingController.view.translatesAutoresizingMaskIntoConstraints = false
        NSLayoutConstraint.activate([
            hostingController.view.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            hostingController.view.centerYAnchor.constraint(equalTo: view.centerYAnchor),
            hostingController.view.widthAnchor.constraint(equalTo: view.widthAnchor, multiplier: 0.7),
            hostingController.view.heightAnchor.constraint(equalTo: view.heightAnchor, multiplier: 0.7)
        ])

        hostingController.didMove(toParent: self)

        let topLabel = UILabel()
        topLabel.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(topLabel)

        NSLayoutConstraint.activate([

            topLabel.widthAnchor.constraint(equalToConstant: 300),
            topLabel.heightAnchor.constraint(equalToConstant: 50),
            topLabel.bottomAnchor.constraint(equalTo: hostingController.view.topAnchor, constant: -30), // 이 부분 수정
            topLabel.centerXAnchor.constraint(equalTo: hostingController.view.centerXAnchor)
        ])

        topLabel.backgroundColor = .systemBlue
        topLabel.text = "This is in UIKit"
        topLabel.textAlignment = .center
    }
}

struct SwiftUIView: View {
    
    @State var textValue: String
    
    var body: some View {
        GeometryReader { geometry in
            
            VStack {
                Text(textValue)
            }
            
            // VStack을 GeometryReader의 크기와 일치시키기
            .frame(width: geometry.size.width, height: geometry.size.height)
            .background(Color.yellow) // 배경색을 노란색으로 설정
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


## History
- 230804: 초안작성
