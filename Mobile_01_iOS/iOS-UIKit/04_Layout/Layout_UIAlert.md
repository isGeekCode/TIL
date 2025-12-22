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


## Alert + DatePicker

```swift
@IBActionfuncCSPicker(_ sender:Any) {

//let dialog = UIAlertController(title: nil, message: nil, preferredStyle: .actionSheet)

let datePicker =UIDatePicker()
        datePicker.datePickerMode = .date
        datePicker.preferredDatePickerStyle = .wheels
        datePicker.locale =NSLocale(localeIdentifier: "ko_KO")asLocale// datePicker의 default 값이 영어이기 때문에 한글로 바꿔줘야한다. 그래서 이 방식으로 변경할 수 있다.

let dateChooserAlert =UIAlertController(title: nil, message: nil, preferredStyle: .actionSheet)
        dateChooserAlert.view.addSubview(datePicker)
        dateChooserAlert.addAction(UIAlertAction(title: "선택완료", style: .cancel, handler: nil))
//dialog.setValue(contentVC, forKey: "contentViewController") // private api

let height :NSLayoutConstraint =NSLayoutConstraint(item: dateChooserAlert.view, attribute: .height, relatedBy: .equal, toItem: nil, attribute: .notAnAttribute, multiplier: 1.1, constant: 300)
        dateChooserAlert.view.addConstraint(height)

        present(dateChooserAlert, animated: true, completion: nil)

    }
```
