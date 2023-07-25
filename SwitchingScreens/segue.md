# Segue를 이용한 화면이동

iOS를 하게 되면 가장 처음엔 하나의 화면으로만 앱을 만들지만 상황에 따라 여러 개의 화면이 필요해진다. 

이 때, 화면을 전환하기 위해 여러가지 방법이 있는데, 전체적인 소개는 아래 링크를 참고하자.

이 글에서는 Segue를 통하여 화면 이동을 하는 방법을 소개하고자 한다.
- [TIL : iOS에서의 화면관리 및 전환](https://github.com/isGeekCode/TIL/blob/main/SwitchingScreens/A_Various_switchingScene.md)

## Segue

Segue는 한 뷰 컨트롤러에서 다른 뷰 컨트롤러로 전환을 수행하기위한 수단이다. 

이를 이용해 사용자가 앱 내에서 다른 화면으로 이동할 수 있도록 할 수 있다.

좀더 자세히 알아보자면

Segue는 `UIStoryboardSegue` 클래스다.

ViewController간의 이동을 관리하기 위해 추상화하고 전환의 세부사항을 캡슐화를 하는 클래스이다. 

이전 ViewController에서 새로운 ViewController로 전환할 때, segue의 인스턴스를 사용한다. 

Segue에서 특별한 점을 소개하자면 아래와 같다.

- 출발지 / 도착지
- identifier
- (modal일 경우)
    - modalPresentationStyle
    - modalTransitionStyle

### 출발지와 도착지
Segue는 전 화면과 후 화면을 부드럽게 전환을 해야하기 때문에, 당연하게도 출발지와 목적지가 필요하다.
Segue는 스토리보드와 함께 사용하기 때문에 스토리보드에서 출발지와 도착지를 링크하면 된다.

### identifier
한 화면에서 여러 개의 Segue가 존재할 수도 있고, 각 Segue에 따른 데이터가 필요할 수 있다.
이를 구별하기위해 사용하는 것이 identifier다.

### Modal방식

modal방식이란, 현재의 화면을 보존하면서 사용자의 주의를 새로운 작업에 집중시키기위해 전체 화면을 차지하는 방식을 말한다. 

예를 들어, 사용자가 사진을 선택하거나, 이메일을 작성할 때 사용할 수 있다.

이런 경우에 새로운 뷰가 현재 뷰를 완전히 가릴 수 있다.

## Segue 만들기

스토리보드에서 이동 전 화면에서 이동 후 화면으로 Segue를 만들어보자.

일단 필요한 것은 trigger가 될 요소를 만들어주는 것이다.

A 화면에서 버튼을 누르면 B 화면으로 이동하는 것이다.

- 시나리오
    - ViewControllerA(노랑)
    - 버튼 클릭
    - ViewController(파랑)으로 전환

1. segue 시작점, 끝점 선언
ViewControllerA의 트리거(버튼)을 클릭하고 Control버튼을 누른 상태에서 B로 드래그
<img width="500" alt="스크린샷 2023-07-25 오후 4 24 23" src="https://github.com/isGeekCode/TIL/assets/76529148/f0b8b2e1-4b46-4ef6-ade4-4af67fb074ca">

2. 어떤 방식으로 전환할 지 선택
그러면 아래와 같이 선택을 위한 창이 생겨난다. 
가장 일반적으로 사용하는 것은 `Present Modally`. 이걸 선택해준다.
<img width="200" alt="스크린샷 2023-07-25 오후 4 23 46" src="https://github.com/isGeekCode/TIL/assets/76529148/67c7fed0-0f1d-4e07-81b8-42f82d21e03a">

3. 연결된 화면
<img width="500" alt="스크린샷 2023-07-25 오후 4 21 46" src="https://github.com/isGeekCode/TIL/assets/76529148/47c9b7e0-2df1-48c8-8db1-46b4ee2e4b97">
  
4. 동작 화면
<img width="300" alt="ezgif-3-d5a07d300a" src="https://github.com/isGeekCode/TIL/assets/76529148/b8cdcbb0-f14b-457f-b870-ea5c7352c7fc">







```swift
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

//    @IBAction func unwindToA(_ segue: UIStoryboardSegue) {
//        print("unwind")
//    }

    override func viewDidLoad() {
        super.viewDidLoad()
    }
}

class ViewControllerB: ViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        createButton(title: "Dismiss", action: #selector(dismissViewController), yPos: 100)
    }
    
    @objc func dismissViewController() {
        self.dismiss(animated: true)
    }

    @objc func popViewController() {
        self.dismiss(animated: true)
    }
}

extension UIApplication {
    class func topViewController() -> UIViewController? {
        if #available(iOS 13.0, *) {
            return shared.windows.first { $0.isKeyWindow }?.rootViewController?.topViewController
        } else {
            return shared.keyWindow?.rootViewController?.topViewController
        }
    }
}

extension UIViewController {
    var topViewController: UIViewController? {
        if let presentedViewController = presentedViewController {
            return presentedViewController.topViewController
        }
        if let navigationController = self as? UINavigationController {
            return navigationController.visibleViewController?.topViewController
        }
        if let tabBarController = self as? UITabBarController {
            return tabBarController.selectedViewController?.topViewController
        }
        return self
    }
}

class ViewControllerC: ViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        
        createButton(title: "Dismiss", action: #selector(dismissViewController), yPos: 100)
        createButton(title: "DismissToBlue", action: #selector(DismissToBlue), yPos: 200)
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        let destVC = segue.destination as? ViewControllerA
    }
    
    
    @objc func dismissViewController() {
        self.dismiss(animated: true)
    }
    
    @objc func DismissToBlue() {
        self.dismiss(animated: true) {
            if let topViewController = UIApplication.topViewController() {
                topViewController.dismiss(animated: true)
            }
        }
    }
}

```
