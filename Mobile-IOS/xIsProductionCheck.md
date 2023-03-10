# appStoreReceiptURL

앱스토어와 관련된 내용을 담고 있는 URL이다. 

이곳에서 아래 코드를 통해 앱스토어에서 다운로드했는지도 체크할 수 있다.

```swift
extension Bundle {
    var isProduction: Bool {
        #if DEBUG
            return false
        #else
            guard let path = self.appStoreReceiptURL?.path else {
                return true
            }
            return !path.contains("sandboxReceipt")
        #endif
    }
}

// 조금더 자세한 path가 필요한 경우
extension Bundle {

var appStoreReceiptURLPath: String {
        guard let path = self.appStoreReceiptURL?.path else { return "nil" }
        return path
    }
}

```

아래처럼 얼럿을 통해 체크가능

```swift
DispatchQueue.main.async {
        
            let msg = "현재 isProduction의 값은 \(Bundle.main.isProduction)입니다.\n\n path는 \(Bundle.main.appStoreReceiptURLPath)입니다"
            print("appStoreReceiptURLPath ::\n\(Bundle.main.appStoreReceiptURLPath)")
            let alert = UIAlertController(title: "", message: msg, preferredStyle: .alert)
            let confirm = UIAlertAction(title: "확인", style: .default)
            alert.addAction(confirm)
            self.present(alert, animated: true) { }
        }
```

appDelegate나 SceneDelegate에서 해당 얼럿을 띄울경우 ViewController가 뜨는 시간을 고려해 지연시킨후 띄우는 것이 좋다. 

전체코드

```swift
func alertIsProductionCheck() {
    DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
        if let topVC = UIApplication.topViewController() {
            let msg = "현재 isProduction의 값은 \(Bundle.main.isProduction)입니다.\n\n path는 \(Bundle.main.appStoreReceiptURLPath)입니다"
            print("appStoreReceiptURLPath ::\n\(Bundle.main.appStoreReceiptURLPath)")
            let alert = UIAlertController(title: "", message: msg, preferredStyle: .alert)
            let confirm = UIAlertAction(title: "확인", style: .default)
            alert.addAction(confirm)
            topVC.present(alert, animated: true) { }
        }

    }
}

extension UIApplication {
    class func topViewController(base: UIViewController? = UIWindow.keyWindow?.rootViewController) -> UIViewController? {
        
        if let nav = base as? UINavigationController {
            return topViewController(base: nav.visibleViewController)
        }
        
        if let presented = base?.presentedViewController {
            return topViewController(base: presented)
        }
        print("topViewController\(String(describing: base))")
        return base
    }
}

extension Bundle {
    var isProduction: Bool {
        #if DEBUG
            return false
        #else
            guard let path = self.appStoreReceiptURL?.path else {
                return true
            }
            return !path.contains("sandboxReceipt")
        #endif
    }

    var appStoreReceiptURLPath: String {
        guard let path = self.appStoreReceiptURL?.path else { return "nil" }
        return path
    }
}
```
