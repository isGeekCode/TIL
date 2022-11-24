# Date로 두 개의 시간차 구하기


테스트를 하다보면  특정부분까지의 시간이 얼마나 걸리는지 알고 싶을 때가 있다.

이때 간단하게 Date함수를 이용해 시작시간과 현재시간을 가지고 시간을 구할 수 있다.

시간차는 Timer를 이용할 수도 있고 아래와 같이 Date를 이용할 수도 있다.

하지만 Date가 간단하게 구현이 가능하니 오늘은 이 방법을 알아보자



### 타이머 구현

```swift
class MainViewController: UIViewController {

        var startTime: Date?

        // 시작시간을 저장하는 함수
        func startTimer() {
            let startTime = Date()
            self.startTime = startTime
            print("작업시작\(String(describing: self.startTime))")
        }
        
        /// 타이머를 멈추고 시간차를 리턴한다.
        func stopTimer() -> Int {
        
                let endTime = Date()
                if let startTime = self.startTime {
            let interval = Int(endTime.timeIntervalSince(startTime)*1000)
                
                print("loginTimeCount : \(interval)/ms")
                return interval
        }
                return 0    
        }
}

```



### 얼럿세팅


시간을 시각적으로 보여줄 얼럿창을 생성하는 함수와 

얼럿을 띄워줄 현재 최상단에 위치한 ViewController 를 구하는 함수

```swift

extension UIApplication {
        
            // 얼럿을 띄워줄 최상단에 위치한 UIViewController를 찾는 함수
     func topViewController(base: UIViewController? = UIApplication.shared.keyWindow?.rootViewController) -> UIViewController? {

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



/// 기본 알럿 뷰 컨트롤러
    /// - Parameters:
    ///   - titl: 알럿 뷰 타이틀
    ///   - msg: 알럿 뷰 메세지
    ///   - cancel: 취소 버튼 유무
    ///   - vc: 알럿 뷰 보여질 뷰 컨트롤러
    ///   - complete: 버튼 클릭 값 escaping (Bool)
   func basicAlertControllerShow(WithTitle titl: String, message msg: String, isNeedCancel cancel: Bool, viewController vc: UIViewController, completeHandler complete: ((_ isCheck: Bool) -> Void)? = nil) -> Void {
        
        let alertController = UIAlertController.init(title: titl, message: msg, preferredStyle: .alert)
        if cancel {
            let cancelAction = UIAlertAction.init(title: RDMessage.buttonFalse, style: .cancel) { (cancelAct) in
                complete?(false)
            }
            alertController.addAction(cancelAction)
        }
        
        let btnAction = UIAlertAction.init(title: RDMessage.buttonTrue, style: .default) { (alertAct) in
            complete?(true)
        }
        
        alertController.addAction(btnAction)
        DispatchQueue.main.async {
            vc.present(alertController, animated: true, completion: nil)
        }
    }
```



## 사용

```swift
class MainViewController {

        // 타이머 시작
        startTime()
        
        DispatchQueue.main.async {
                  guard let topVC = UIApplication.topViewController() else { return  }
                            // 타이머 종료, 시간차 
                  let LoginTime = self.stopTimer()
                            
                  basicAlertControllerShow(WithTitle: "", message: "성공  \(LoginTime)/ms 소요", isNeedCancel: false, viewController: topVC) { isSuccess in
                      if isSuccess {
                
                          }
              }
        
        }
        

}

```
