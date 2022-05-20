# 배열안에 담긴 url 유효성 검사

ViewController로 넘어온 mapUrl의 유무를 체크하고 for문으로 유효성 체크

```swift
 for i in 0..<shareRecordDic.count {
              if self.mapUrl! == shareRecordDic[i]["mapUrl"]! {
                  alertPresentViewController(message: "이미 공유한 적이 있습니다", animated: true) { _ in
                      return
                  }
                  return
              }
          }
```

validationCheck()에서 

기존에 UserDefault에 저장된 [[String:String]] 를 담기위해

var dic: [String: AnyObject]를 먼저 생성하고 시작

```swift
class ViewController {

convenience init(isOverlayFooter: Bool, imageUrl: String, mapUrl: String, distance: String, time: String, speed: String) {
        self.init(isOverlayFooter: isOverlayFooter)
        
        self.imageUrl = imageUrl
        self.mapUrl = mapUrl
        self.distance = distance
        self.time = time
        self.speed = speed
    }

func ViewDidLoad {
	super.viewDidLoad()

	var snapFrame = self.photoView.frame //CGRect
  snapFrame.origin.y += self.contentView.frame.origin.y
	        
  if let image = self.view.snapshot(of: snapFrame) {
		var dic: [String: AnyObject]
            if self.mapUrl != nil {
                dic = [
                    "image": image,
                    "mapUrl": self.mapUrl! as AnyObject
                ]
                //기록 검증
                validationCheck()
            } else {
                dic = [
                    "image": image
                ]
            }
}

func validationCheck() {
        if let shareRecordDic = UserDefaults.standard.value(forKey: "UserDefaultKey") as? [[String:String]] {
            
            for i in 0..<shareRecordDic.count {
                if self.mapUrl! == shareRecordDic[i]["mapUrl"]! {
                    alertPresentViewController(message: "메세지", animated: true) { _ in
                        return
                    }
                    return
                }
            }
        }
    }

func alertPresentViewController(message alertMessage: String?, animated flag: Bool, handler: ((UIAlertAction) -> Void)?) -> Void {
        // message은 옵셔널. 메세지 내용에 따른 분기를 여기서 처리하기 위함 (실제 사용하는 부분에서는 메시지 유무를 체크할 필요가 없음)
        guard let message = alertMessage , alertMessage != nil && alertMessage != "" else { return }
        
        DispatchQueue.main.async(execute: {
            let alert = UIAlertController(title: Message.title, message:message, preferredStyle: UIAlertController.Style.alert)
            
            alert.addAction(UIAlertAction(title: Message.buttonTrue, style: UIAlertAction.Style.default, handler: handler))
            
            if let topController = UIApplication.topViewController() {
                topController.present(alert, animated: flag, completion: nil)
            }
        })
    }
```