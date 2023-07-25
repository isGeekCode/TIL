# Segue를 이용한 화면이동

iOS를 하게 되면 가장 처음엔 하나의 화면으로만 앱을 만들지만 상황에 따라 여러 개의 화면이 필요해진다. 

이 때, 화면을 전환하기 위해 여러가지 방법을 사용할 수 있는데, 아래와 같다.





Segue는 한 뷰 컨트롤러에서 다른 뷰 컨트롤러로 전환을 수행하는 메커니이다. 

이를 이용해 사용자가 앱 내에서 다른 화면으로 이동할 수 있도록 할 수 있다.

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
