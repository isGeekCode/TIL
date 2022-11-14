전통적인 MVC구조로 HTTP사용하기

- [참고 포스팅](https://medium.com/swift-coding/mvc-in-swift-a9b1121ab6f0) (원문)
- [참고 깃허브](https://github.com/stevencurtis/SwiftCoding/tree/master/MVCHTTPCodingExample)

컨트롤러는 일반적으로 공개적으로 사용 가능한 기능 모델을 통해 모델과 통신합니다.

모델은 KVO를 통해 컨트롤러와 통신할 수 있습니다.

M: 데이터 및 데이터를 조작하는 로직

- 모델 개체 혹은 네트워킹 코드

V: C가 제어해야하는 UI구성요소

- C에게 알리기위해 target-action 혹은 delegate패턴을 사용할 수 있다.
- 자기가 보여주고 있는 Model을 소유하고 있지않다 → 테이블뷰의 Delegate를 사용한다.

C: M과 V사이에 위치 - 일반적으로 Delegate패턴 사용

- 아웃렛을 통해 뷰와 소통할 수 있다.

하지만 우린 궁극적으로 모델에서 뷰로가는 소통을 멈춰야한다. 

예를 들어 계산기를 만들때

뷰는 UIButton의 특정 인스턴스이고, UIButton은 계산기의 로직을 전혀 몰라야하기 때문이다. 

MVC는 한화면으로 진행되는 경향이 있다.

여러 MVC와 통신할 때에는 각 View를 단일 MVC로 취급한다. 

downLoad버튼을 누르면 HTTP를 통해 다운로드 하는 로직을 가진 4가지 구현방법

**Method 1 — API call within the view controller**

**Method 2 — Delegate pattern**

**Method 3 — Closures**

**Method 4 — NSNotifications**

### Method1 :  **API call within the view controller**

가장 간단하게 구현할 수 있는 방법이지만 HTTP가 내부에 존재한다. 

```bash
class APIInViewController: UIViewController {
    @IBOutlet weak var dataDownloadedLabel: UILabel!
    
    var dataDownloaded = 0 {
        didSet {
            DispatchQueue.main.async(execute: {  [weak self] () -> Void in
                guard let self = self else {return}
                self.dataDownloadedLabel.text = "Data items downloaded : \(self.dataDownloaded)"
            }
            )
        }
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
    }
    
    @IBAction func apiAction(_ sender: UIButton) {
        makeAPICall()
    }
    
    func makeAPICall() {
        let config = URLSessionConfiguration.default
        let session = URLSession(configuration: config)
        let url = URL(string: baseUrl + breachesExtensionURL)
        let task = session.dataTask(with: url!) { [weak self] (data, response, error) in
            guard let self = self else {return}
            if let data = data{
                self.dataDownloaded += data.count
            }
        }
        task.resume()
    }
    
}
```

따라서 HTTPManager 클래스를 따로 생성해서 분리할 수 가 있다.

```bash
// HTTPOutSideVC.swift

import UIKit

class HTTPOutsideViewController: UIViewController {

    // By definition this approach CANNOT work
    
    @IBOutlet weak var dataDownloadedLabel: UILabel!
    var dataDownloaded = 0 {
        didSet {
            DispatchQueue.main.async(execute: {  [weak self] () -> Void in
                guard let self = self else {return}
                self.dataDownloadedLabel.text = "Array objects downloaded : \(self.dataDownloaded)"
                }
            )
        }
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
    }

    @IBAction func makeAPICall(_ sender: UIButton) {
        let httpManager = TightlyCoupledHTTPManager()
        httpManager.get(urlString: baseUrl + breachesExtensionURL)
        dataDownloaded += httpManager.data.count
    }

}

//  TightlyCoupledHTTPManager.swift

import Foundation

class TightlyCoupledHTTPManager {
    var data = Data()
    public func get(urlString: String) {
        let url = URL(string: urlString)
        if let usableUrl = url {
            let request = URLRequest(url: usableUrl)
            let task = URLSession.shared.dataTask(with: request, completionHandler: { (data, response, error) in
                self.data = data!
                print (data!)
            })
            task.resume()
        }
    }    
}
```

분리는 했으나 이 방법으로는 VC로 데이터를 가져올 방법이 없다. 

그래서 httpManager.data.count는 항상 0이다. API호출을 하는데 시간이 걸리고, 해당 로직으로 이동을 할때 데이터가 채워졌는지를 확인할 시간이 없기 때문이다. 

타이머를 사용하여 대기하는 등의 방법 또한 불안정하며 특정 시점에 데이터가 채워지는 것을 보장하지않는다. 

### **Method 2 — Delegate pattern**

델리게이트 패턴을 사용한다는 것는 해당 프로토콜만 준수하기만하면 모든 클래스에서 데이터를 수신할 수 있다는 것을 의미한다.

```swift
//  DelegationHTTPManager.swift

import Foundation

protocol DelegationHTTPDelegate: AnyObject {
    func didDownloadBreaches(_ data: Data) // called when the manager has completed downloading all the breaches
}
```

```swift
class DelegationHTTPManager {
    static let shared: DelegationHTTPManager = DelegationHTTPManager()
    var delegate : DelegationHTTPDelegate? = nil
    
    public func get (urlString: String) {
        let url = URL(string: urlString)
        if let usableUrl = url {
            let request = URLRequest(url: usableUrl)
            let task = URLSession.shared.dataTask(with: request, completionHandler: { (data, response, error) in
                self.delegate!.didDownloadBreaches(data!)
            })
            task.resume()
        }
    }
}
```

didDownloadBreaches 함수가 대리자에 의해 호출되려면 VC를 대리자 설정해야한다. 

```swift
//  HTTPDelegateViewController.swift
import UIKit

class HTTPDelegateViewController: UIViewController {
    
    var dataDownloaded = 0 {
        didSet {
            DispatchQueue.main.async(execute: {  [weak self] () -> Void in
                guard let self = self else {return}
                self.dataDownloadedLabel.text = "Array objects downloaded : \(self.dataDownloaded)"
                }
            )
        }
    }
    
    @IBOutlet weak var dataDownloadedLabel: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
    }
    
    @IBAction func downloadAPIAction(_ sender: UIButton) {
        DelegationHTTPManager.shared.delegate = self
        DelegationHTTPManager.shared.get(urlString: baseUrl + "/breaches")
    }
}

extension HTTPDelegateViewController : DelegationHTTPDelegate {
    func didDownloadBreaches(_ data: Data) {
        dataDownloaded += data.count
    }
}
```

### **Method 3 — Closures**

Swift 5에 도입된 새로운 Result 유형을 사용한다.

```swift
//  ClosureHTTPManager.swift
import Foundation

class ClosureHTTPManager {
    static let shared: ClosureHTTPManager = ClosureHTTPManager()

    enum HTTPError: Error {
        case invalidUR
        case invalidResponse(Data?, URLResponse?)
    }
    
    public func get(urlString: String, completionBlock: @escaping (Result<Data, Error>) -> Void) {
        guard let url = URL(string: urlString) else {
            completionBlock(.failure(HTTPError.invalidURL))
            return
        }
        
        let task = URLSession.shared.dataTask(with: url) { data, response, error in
            guard error == nil else {
                completionBlock(.failure(error!))
                return
            }

            guard
                let responseData = data,
                let httpResponse = response as? HTTPURLResponse,
                200 ..< 300 ~= httpResponse.statusCode else {
                    completionBlock(.failure(HTTPError.invalidResponse(data, response)))
                    return
            }

            completionBlock(.success(responseData))
        }
        task.resume()
    }
}
```

콜백은 클로저에서 사용할 수 있으며 UI를 업데이트하는 데 사용된다. 

API 호출을 사용한 후 메인 스레드에 있지 않을 수 있으므로 UI 작업이 적절한 스레드에 있는지 확인해야 한다

```swift
//  HTTPClosuresViewController.swift
import UIKit

class HTTPClosuresViewController: UIViewController {

    @IBOutlet weak var dataDownloadedLabel: UILabel!
    
    var dataDownloaded = 0 {
        didSet {
            DispatchQueue.main.async(execute: {  [weak self] () -> Void in
                guard let self = self else {return}
                self.dataDownloadedLabel.text = "Array objects downloaded : \(self.dataDownloaded)"
                }
            )
        }
    }
    
    @IBAction func APIButtonAction(_ sender: UIButton) {
        ClosureHTTPManager.shared.get(urlString: baseUrl + breachesExtensionURL, completionBlock: { [weak self] data in
            
            print ("thread", Thread.current)
            guard let self = self else { return }
            switch data {
            case .failure(let error):
                print(error)
                
            case .success(let dataret):
                self.dataDownloaded += dataret.count
            }
        })
    }

    override func viewDidLoad() {
        super.viewDidLoad()
    }
}
```

Delegate 패턴은 일대일 관계여야 한다. 따라서 프로토콜을 준수하는 다수의 뷰 컨트롤러를 갖고 싶다면 이것은 아마도 올바른 솔루션이 아닐 것이다.

### **방법 4 — NSNotifications**

알림은 데이터가 수신될 때 여러 보기가 알림을 수신할 수 있음을 의미합니다.

확장 내에서 알림의 이름을 지정할 수 있습니다.

```swift
extension Notification.Name {
    static let notificationHTTPDidUpdateNotification = Notification.Name("NotificationHTTPDidUpdateNotification")
}
```

알림에 대한 리스너를 설정합니다.

```swift
class HTTPNotificationViewController: UIViewController {

override func viewDidLoad() {
        super.viewDidLoad()
        NotificationCenter.default.addObserver(self, selector: #selector( notificationReceived(withNotification:) ), name: Notification.Name.notificationHTTPDidUpdateNotification, object: nil)
    }
    
    deinit {
        NotificationCenter.default.removeObserver(self)
    }

}
```

알림수신 준비

```swift
@objc func notificationReceived (withNotification notification: NSNotification) {
        if let userInfo = notification.userInfo {
            if let prog = userInfo["sent"] as? Int {
                dataDownloaded += prog
            }
        }
    }
```

전체코드

```swift
//  HTTPNotificationViewController.swift
import UIKit

class HTTPNotificationViewController: UIViewController {

    @IBOutlet weak var dataDownloadedLabel: UILabel!

    var dataDownloaded = 0 {
        didSet {
            DispatchQueue.main.async(execute: {  [weak self] () -> Void in
                guard let self = self else {return}
                self.dataDownloadedLabel.text = "Array objects downloaded : \(self.dataDownloaded)"
                }
            )
        }
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        NotificationCenter.default.addObserver(self, selector: #selector( notificationReceived(withNotification:) ), name: Notification.Name.notificationHTTPDidUpdateNotification, object: nil)
    }
    
    deinit {
        NotificationCenter.default.removeObserver(self)
    }
    
    @objc func notificationReceived (withNotification notification: NSNotification) {
        if let userInfo = notification.userInfo {
            if let prog = userInfo["sent"] as? Int {
                dataDownloaded += prog
            }
        }
    }
    
    @IBAction func downloadAPIAction(_ sender: UIButton) {
        NotificationHTTPManager.shared.get(urlString: baseUrl + "/breaches")
    }
    
}

extension Notification.Name {
    static let notificationHTTPDidUpdateNotification = Notification.Name("NotificationHTTPDidUpdateNotification")
}
```

이것은 NotificationHTTPManager에 의해 다루어진다.

```swift
class NotificationHTTPManager {
    static let shared: NotificationHTTPManager = NotificationHTTPManager()
    
    enum HTTPError: Error {
        case invalidURL
        case invalidResponse(Data?, URLResponse?)
    }
    
    public func get(urlString: String) {
        guard let url = URL(string: urlString) else {

            let dict = ["error": nil] as [String : Any?]
            NotificationCenter.default.post(name: Notification.Name.notificationHTTPDidUpdateNotification, object: self, userInfo: dict as [AnyHashable : Any])
            return
        }
        
        let task = URLSession.shared.dataTask(with: url) { data, response, error in
            guard error == nil else {
                //completionBlock(.failure(error!))
                let dict = ["error": nil] as [String : Any?]
                NotificationCenter.default.post(name: Notification.Name.notificationHTTPDidUpdateNotification, object: self, userInfo: dict as [AnyHashable : Any])
                return
            }
            guard
                let responseData = data,
                let httpResponse = response as? HTTPURLResponse,
                200 ..< 300 ~= httpResponse.statusCode else {
                    let dict = ["error": nil] as [String : Any?]
                    NotificationCenter.default.post(name: Notification.Name.notificationHTTPDidUpdateNotification, object: self, userInfo: dict as [AnyHashable : Any])

                    return
            }
            let dict = ["sent": responseData.count] as [String : Any?]
            NotificationCenter.default.post(name: Notification.Name.notificationHTTPDidUpdateNotification, object: self, userInfo: dict as [AnyHashable : Any])
        }
        task.resume()
    }
}
```

HTTPManager의 다양한 반복은 HTTP 호출을 수행하는 데 전적으로 책임이 있다.  만약 JSON도 디코딩하길 원한다면 더많은 작업을 해야한다.