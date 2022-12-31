# UIAlert 어디서든 띄우기

함수세팅

```swift
extension
/// 1초의 딜레이와 함께 알럿뷰 보여주는 함수
  /// - Parameters:
  ///   - titl: 알럿뷰 타이틀
  ///   - msg: 알럿뷰 메시지
  ///   - cancel: 취소 버튼 유무
  ///   - vc: 알럿 뷰 보여질 뷰 컨트롤러
  ///   - complete: 버튼 클릭 값 escaping (Bool)
static public func alertControllerShow(WithTitle titl: String, message msg: String, isNeedCancel cancel: Bool, viewController vc: UIViewController, completeHandler complete: ((_ isCheck: Bool) -> Void)? = nil) -> Void {
    
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
    
    DispatchQueue.main.asyncAfter(deadline: .now() + 0.5) {
        vc.present(alertController, animated: true, completion: nil)
    }
```
