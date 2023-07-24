# 화면전환 - UINavigationController 이해하기

아래 예시 코드를 통해 iOS 네비게이션 컨트롤러(Navigation Controller)의 작동 방식과 주요 메서드들에 대해 알아보자.

## Navigation Controller의 구조
네비게이션 컨트롤러는 스택(stack) 자료 구조를 사용하여 뷰 컨트롤러를 관리합니다. 처음에는 스택에 'A' 뷰 컨트롤러가 있고, 다른 뷰 컨트롤러들은 'push' 연산으로 스택에 추가됩니다. 사용자는 'pop' 연산을 통해 이전 뷰 컨트롤러로 돌아갈 수 있습니다. 여기서 'push'는 뷰 컨트롤러를 네비게이션 스택에 추가하며, 'pop'은 네비게이션 스택의 맨 위에 있는 뷰 컨트롤러를 제거합니다.

## Navigation Controller의 초기화와 활용
SceneDelegate에서 네비게이션 컨트롤러는 ViewControllerA 인스턴스를 루트 뷰 컨트롤러로 갖는 UINavigationController 인스턴스로 초기화된다. 이렇게 설정하면 앱이 시작할 때 사용자에게 보여지는 첫 화면이 ViewControllerA가 된다.


```swift
    func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
//        초기값
//        guard let _ = (scene as? UIWindowScene) else { return }
        guard let windowScene = (scene as? UIWindowScene) else { return }

        window = UIWindow(windowScene: windowScene)
        let navigationController = UINavigationController(rootViewController: ViewControllerA())
        window?.rootViewController = navigationController
        window?.makeKeyAndVisible()
    }

```

### 적용화면
  
<img width="500" alt="ezgif-3-acab1a77c5" src="https://github.com/isGeekCode/TIL/assets/76529148/a7294acc-ae8a-48c6-bfab-244083181301">    

## Navigation Bar
네비게이션 컨트롤러는 각 뷰 컨트롤러의 상단에 네비게이션 바(Navigation Bar)를 표시한다. 이 네비게이션 바에는 현재 뷰 컨트롤러의 제목이 표시되며, 이는 각 뷰 컨트롤러의 'navigationItem.title' 속성으로 설정된다.

## Navigation Flow
앱의 사용자는 각 뷰 컨트롤러에서 버튼을 눌러 다음 뷰 컨트롤러로 'push'하거나 이전 뷰 컨트롤러로 'pop'하여 앱 내에서 이동할 수 있다.

### pushViewController(UIViewController:animated:)
pushViewController(UIViewController:animated:)함수는 아래와 같이 사용된다.
해당 viewController에 navigationController에 있을지 없을지 모르기 떄문에 옵셔널 체이닝을 사용한다.
파라미터로는 새롭게 띄워줄 ViewController를 넣어준다.

```swift
let viewControllerB = ViewControllerB()
navigationController?.pushViewController(viewControllerB, animated: true)
```


### popViewController(animated:)
네비게이션 컨트롤러는 Stack구조로 ViewControllers라는 배열안에 ViewController를 차례로 넣어준다. 
이 배열에서 뒤쪽에 있을수록 상단에 있는 화면이다.
이때 이 함수가 호출되면 마지막에 위치한 ViewController를 사라지게 한다.

```swift
navigationController?.popViewController(animated: true)
```



```swift

class SceneDelegate: UIResponder, UIWindowSceneDelegate {

    var window: UIWindow?

    func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
//        guard let _ = (scene as? UIWindowScene) else { return }
        guard let windowScene = (scene as? UIWindowScene) else { return }

        window = UIWindow(windowScene: windowScene)
        let navigationController = UINavigationController(rootViewController: ViewControllerA())
        window?.rootViewController = navigationController
        window?.makeKeyAndVisible()
    }
}

import UIKit

class ViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
    }
    
    func createButton(title: String, action: Selector, yPos: CGFloat) {
        let screenWidth = UIScreen.main.bounds.width
        let buttonWidth: CGFloat = 200
        let xPos = (screenWidth - buttonWidth) / 2

        let button = UIButton(frame: CGRect(x: xPos, y: yPos, width: buttonWidth, height: 50))
        button.setTitle(title, for: .normal)
        button.setTitleColor(.white, for: .normal)
        button.backgroundColor = .darkGray
        button.addTarget(self, action: action, for: .touchUpInside)
        view.addSubview(button)
    }
}

class ViewControllerA: ViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        
        view.backgroundColor = .systemTeal
        navigationItem.title = "A"
        createButton(title: "push B", action: #selector(pushToViewControllerB), yPos: 100)
    }
    
    @objc func pushToViewControllerB() {
        let viewControllerB = ViewControllerB()
        navigationController?.pushViewController(viewControllerB, animated: true)
    }

}

class ViewControllerB: ViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .lightGray
        navigationItem.title = "B"

        createButton(title: "push C", action: #selector(pushToViewControllerC), yPos: 100)
        createButton(title: "Pop", action: #selector(popViewController), yPos: 200)
        createButton(title: "Pop To Root", action: #selector(popToRootViewController), yPos: 300)
    }
    
    @objc func pushToViewControllerC() {
        let viewControllerC = ViewControllerC()
        navigationController?.pushViewController(viewControllerC, animated: true)
    }

    @objc func popViewController() {
        navigationController?.popViewController(animated: true)
    }

    @objc func popToRootViewController() {
        navigationController?.popToRootViewController(animated: true)
    }
}

// ViewControllerC, ViewControllerD도 위와 같은 패턴으로 작성해주세요.


class ViewControllerC: ViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemYellow
        navigationItem.title = "C"

        createButton(title: "push D", action: #selector(pushToViewControllerC), yPos: 100)
        createButton(title: "Pop", action: #selector(popViewController), yPos: 200)
        createButton(title: "Pop To Root", action: #selector(popToRootViewController), yPos: 300)
    }
    
    @objc func pushToViewControllerC() {
        let viewControllerD = ViewControllerD()
        navigationController?.pushViewController(viewControllerD, animated: true)
    }

    @objc func popViewController() {
        navigationController?.popViewController(animated: true)
    }

    @objc func popToRootViewController() {
        navigationController?.popToRootViewController(animated: true)
    }
}

class ViewControllerD: ViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemRed
        navigationItem.title = "D"

        createButton(title: "Pop", action: #selector(popViewController), yPos: 100)
        createButton(title: "Pop To Root", action: #selector(popToRootViewController), yPos: 200)
    }
    
    @objc func popViewController() {
        navigationController?.popViewController(animated: true)
    }

    @objc func popToRootViewController() {
        navigationController?.popToRootViewController(animated: true)
    }
}
```

## History
- 230720 : 초안작성
