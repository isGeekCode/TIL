# 화면전환 - UITabBarController 이해하기

탭 바 컨트롤러(Tab Bar Controller)는 네비게이션 컨트롤러와 비슷한 방식으로 동작하지만, 하단에 여러 탭으로 구성되어 있는 인터페이스를 제공하는 컨트롤러다. 각 탭은 하나의 뷰 컨트롤러를 대응시키며, 사용자는 하단 탭 바를 터치하여 다른 뷰 컨트롤러로 전환할 수 있다.

### 적용화면
  
<img width="500" alt="ezgif-4-05ae2c1872" src="https://github.com/isGeekCode/TIL/assets/76529148/3cafd1c0-8cd7-4268-9341-d7f6a9ee5bff">    
  
## TabBar Controller의 구조

<img width="600" alt="img1 daumcdn-13" src="https://github.com/isGeekCode/TIL/assets/76529148/b069b799-1345-4b90-b500-8c22dfdfed7b">    

  
  
<img width="600" alt="img1 daumcdn-14" src="https://github.com/isGeekCode/TIL/assets/76529148/27719c83-0c21-4d23-9016-d2b99e2fb329">    
  
  

  
탭 바 컨트롤러의 구조는 네비게이션 컨트롤러와 유사하게 스택(stack) 자료 구조를 사용한다.

탭 바 컨트롤러의 탭들은 일종의 스택으로 생각할 수 있다.

사용자가 하단의 탭 바를 터치하면 해당 탭에 대응되는 뷰 컨트롤러가 화면에 보여진다.

탭 바 컨트롤러는 다른 뷰 컨트롤러를 'push' 하지 않고, 하단 탭 바를 선택하는 것만으로 뷰 컨트롤러를 전환한다.


## TabBar Controller의 용도

일반적으로 탭 바 컨트롤러는 앱의 주요 기능이나 다양한 섹션들을 탭 형태로 나누어 제공하는데 사용된다.

예를 들어, 앱의 메인 화면, 설정 화면, 알림 화면 등이 각각 탭으로 나눠져 있을 수 있다.



## TabBar Controller의 초기화와 활용


탭 바 컨트롤러의 초기화와 활용은 SceneDelegate에서 설정한다. 아래는 탭 바 컨트롤러를 생성하고 탭에 대응되는 뷰 컨트롤러들을 설정하는 예시 코드다.


### SceneDelegate에서 직접 TabBarController를 생성하고 ViewController들을 구성하는 경우
```swift
class SceneDelegate: UIResponder, UIWindowSceneDelegate {

    var window: UIWindow?

    func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
        // 초기값
        // guard let _ = (scene as? UIWindowScene) else { return }
        guard let windowScene = (scene as? UIWindowScene) else { return }

        // 각각의 뷰 컨트롤러를 인스턴스화합니다.
        let viewControllerA = ViewControllerA()
        let viewControllerB = ViewControllerB()
        let viewControllerC = ViewControllerC()
        let viewControllerD = ViewControllerD()


        // 각 뷰 컨트롤러에 대응되는 아이콘을 설정합니다.
        viewControllerA.tabBarItem = UITabBarItem(title: "A", image: UIImage(systemName: "house"), selectedImage: nil)
        viewControllerB.tabBarItem = UITabBarItem(title: "B", image: UIImage(systemName: "heart"), selectedImage: nil)
        viewControllerC.tabBarItem = UITabBarItem(title: "C", image: UIImage(systemName: "star"), selectedImage: nil)
        viewControllerD.tabBarItem = UITabBarItem(title: "D", image: UIImage(systemName: "gear"), selectedImage: nil)

        // 탭 바 컨트롤러를 생성하고 탭에 대응되는 뷰 컨트롤러들을 설정합니다.
        let tabBarController = UITabBarController()
        tabBarController.viewControllers = [viewControllerA, viewControllerB, viewControllerC, viewControllerD]
        // TabBar의 background 색상
        tabBarController.tabBar.backgroundColor = .lightGray

        // 탭 바 컨트롤러를 루트 뷰 컨트롤러로 설정합니다.
        window = UIWindow(windowScene: windowScene)
        window?.rootViewController = tabBarController
        window?.makeKeyAndVisible()
    }
}
```
### 별도의 UITabBarController 클래스를 구현하고, SceneDelegate에서는 호출만 하는 경우

```swift

import UIKit

class MainTabBarController: UITabBarController {

    override func viewDidLoad() {
        super.viewDidLoad()

        let viewControllerA = ViewControllerA()
        let viewControllerB = ViewControllerB()
        let viewControllerC = ViewControllerC()
        let viewControllerD = ViewControllerD()

        // 탭 바에 대응되는 아이콘과 타이틀을 설정하고 뷰 컨트롤러들을 탭으로 설정합니다.
        viewControllerA.tabBarItem = UITabBarItem(title: "A", image: UIImage(systemName: "house"), selectedImage: nil)
        viewControllerB.tabBarItem = UITabBarItem(title: "B", image: UIImage(systemName: "heart"), selectedImage: nil)
        viewControllerC.tabBarItem = UITabBarItem(title: "C", image: UIImage(systemName: "star"), selectedImage: nil)
        viewControllerD.tabBarItem = UITabBarItem(title: "D", image: UIImage(systemName: "gear"), selectedImage: nil)

        self.viewControllers = [viewControllerA, viewControllerB, viewControllerC, viewControllerD]
    }
}


class SceneDelegate: UIResponder, UIWindowSceneDelegate {

    var window: UIWindow?

    func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
        // 초기값
        // guard let _ = (scene as? UIWindowScene) else { return }
        guard let windowScene = (scene as? UIWindowScene) else { return }

        // MainTabBarController를 루트 뷰 컨트롤러로 설정한다.
        let mainTabBarController = MainTabBarController()

        window = UIWindow(windowScene: windowScene)
        window?.rootViewController = mainTabBarController
        window?.makeKeyAndVisible()
    }
}
```

## 전체코드

### 1. 탭바를 따로 구현

```swift
class SceneDelegate: UIResponder, UIWindowSceneDelegate {

    var window: UIWindow?

    func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
        // 초기값
        // guard let _ = (scene as? UIWindowScene) else { return }
        guard let windowScene = (scene as? UIWindowScene) else { return }

        // MainTabBarController를 루트 뷰 컨트롤러로 설정한다.
        let mainTabBarController = MainTabBarController()

        window = UIWindow(windowScene: windowScene)
        window?.rootViewController = mainTabBarController
        window?.makeKeyAndVisible()
    }
}

class MainTabBarController: UITabBarController {

    override func viewDidLoad() {
        super.viewDidLoad()

        let viewControllerA = ViewControllerA()
        let viewControllerB = ViewControllerB()
        let viewControllerC = ViewControllerC()
        let viewControllerD = ViewControllerD()

        // 탭 바에 대응되는 아이콘과 타이틀을 설정하고 뷰 컨트롤러들을 탭으로 설정합니다.
        viewControllerA.tabBarItem = UITabBarItem(title: "A", image: UIImage(systemName: "house"), selectedImage: nil)
        viewControllerB.tabBarItem = UITabBarItem(title: "B", image: UIImage(systemName: "heart"), selectedImage: nil)
        viewControllerC.tabBarItem = UITabBarItem(title: "C", image: UIImage(systemName: "star"), selectedImage: nil)
        viewControllerD.tabBarItem = UITabBarItem(title: "D", image: UIImage(systemName: "gear"), selectedImage: nil)

        self.viewControllers = [viewControllerA, viewControllerB, viewControllerC, viewControllerD]
        self.tabBar.backgroundColor = .lightGray
    }
}

class ViewControllerA: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemTeal
    }
}

class ViewControllerB: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .lightGray
    }
}

class ViewControllerC: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .white

    }
}

class ViewControllerD: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemRed
        navigationItem.title = "D"
    }
}

```


### 2. 탭바를 SceneDelegate에서 탭바를 직접 구현
```swift
class SceneDelegate: UIResponder, UIWindowSceneDelegate {

    var window: UIWindow?

    func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
        guard let windowScene = (scene as? UIWindowScene) else { return }

        // 각각의 뷰 컨트롤러를 인스턴스화합니다.
        let viewControllerA = ViewControllerA()
        let viewControllerB = ViewControllerB()
        let viewControllerC = ViewControllerC()
        let viewControllerD = ViewControllerD()


        // 각 뷰 컨트롤러에 대응되는 아이콘을 설정합니다.
        viewControllerA.tabBarItem = UITabBarItem(title: "A", image: UIImage(systemName: "house"), selectedImage: nil)
        viewControllerB.tabBarItem = UITabBarItem(title: "B", image: UIImage(systemName: "heart"), selectedImage: nil)
        viewControllerC.tabBarItem = UITabBarItem(title: "C", image: UIImage(systemName: "star"), selectedImage: nil)
        viewControllerD.tabBarItem = UITabBarItem(title: "D", image: UIImage(systemName: "gear"), selectedImage: nil)

        // 탭 바 컨트롤러를 생성하고 탭에 대응되는 뷰 컨트롤러들을 설정합니다.
        let tabBarController = UITabBarController()
        tabBarController.viewControllers = [viewControllerA, viewControllerB, viewControllerC, viewControllerD]
        // TabBar의 background 색상
        tabBarController.tabBar.backgroundColor = .lightGray

        // 탭 바 컨트롤러를 루트 뷰 컨트롤러로 설정합니다.
        window = UIWindow(windowScene: windowScene)
        window?.rootViewController = tabBarController
        window?.makeKeyAndVisible()
    }
}
class ViewControllerA: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemTeal
    }
}

class ViewControllerB: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .lightGray
    }
}

class ViewControllerC: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .white

    }
}

class ViewControllerD: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemRed
        navigationItem.title = "D"
    }
}

```

## History
- 230721 : 초안작성
