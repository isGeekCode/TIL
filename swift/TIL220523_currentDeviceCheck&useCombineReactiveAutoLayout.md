## 현재기기의 화면크기 측정하기 + 콤바인을 이용한 반응형레이아웃 만들기

기기사이즈가 너무 작은 기기같은 경우 키보드를 올렸을 때 보이지 않는 경우가 있다.

먼저 기기사이즈를 가져오는 코드는 아래와 같다.

```swift
if (UIDevice.CurrentDevice.UserInterfaceIdiom == UIUserInterfaceIdiom.Phone) {
    if ((UIScreen.MainScreen.Bounds.Height * UIScreen.MainScreen.Scale) == 1136) {
        Console.WriteLine("iPhone 5 or 5S or 5C");
    } else if ((UIScreen.MainScreen.Bounds.Height * UIScreen.MainScreen.Scale) == 1334) {
        Console.WriteLine("iPhone 6/6S/7/8");
    } else if ((UIScreen.MainScreen.Bounds.Height * UIScreen.MainScreen.Scale) == 1920 || (UIScreen.MainScreen.Bounds.Height * UIScreen.MainScreen.Scale) == 2208) {
        Console.WriteLine("iPhone 6+/6S+/7+/8+");
    } else if ((UIScreen.MainScreen.Bounds.Height * UIScreen.MainScreen.Scale) == 2436) {
        Console.WriteLine("iPhone X, XS, 11 Pro");
    } else if ((UIScreen.MainScreen.Bounds.Height * UIScreen.MainScreen.Scale) == 2688) {
        Console.WriteLine("iPhone XS Max, 11 Pro Max");
    } else if ((UIScreen.MainScreen.Bounds.Height * UIScreen.MainScreen.Scale) == 1792) {
        Console.WriteLine("iPhone XR, 11");
    } else {
        Console.WriteLine("Unknown");
    }
}
```

먼저 기기사이즈를 가져오기 위해 ViewDidLoad에서 프린트 함수를 실행해본다.

```swift
print(UIScreen.main.bounds.height * UIScreen.main.scale)
// 1136 : iphoneSE
```

이렇게 화면이 작을 경우, 로그인화면같은 텍스트필드가 많은 페이지에서 키보드를 생성할 경우

하단부 텍스트필드는 가려져서 볼수가 없는 경우가 생긴다. 이때 해당 뷰 혹은 텍스트필드의 Constraint를 IBOutlet에 연결 해두면 화면의 사이즈를 조건으로 값을 바꿀 수가 있다.

콤바인을 사용해 키보드가 올라가는 순간을 캐치하고 키보드의 높이가 변하는 부분에서 내가 원하는 Constraint를 변화시킨다

```swift
import Foundation
import Combine
import UIKit

final class KeyboardMonitor : ObservableObject {

    enum Status {
        case show, hide
        var description : String {
            switch self {
            case .show: return "보임"
            case .hide: return "안보임"
            }
        }
    }

    @IBOutlet weak var idViewTopConstraint: NSLayoutConstraint!
		@IBOutlet weak var loginBtnBottomConstraint: NSLayoutConstraint!
    @IBOutlet weak var loginBtnLeadingConstraint: NSLayoutConstraint!
    @IBOutlet weak var loginBtnTrailingConstraint: NSLayoutConstraint!

    var subscriptions = Set<AnyCancellable>()

    @Published var updatedKeyboardStatusAction : Status = .hide
    @Published var keyboardHeight : CGFloat = 0.0


    init(){
        print("KeyboardMonitor - init() called")

        // 키보드가 올라올 때 이벤트가 들어옴
        NotificationCenter.Publisher(center: NotificationCenter.default, name: UIResponder.keyboardWillShowNotification) // 아래 값을 구독
            .sink{ (noti : Notification) in
                print("KeyboardMonitor - keyboardWillShowNotification: noti : ", noti)
                self.updatedKeyboardStatusAction = .show

            }.store(in: &subscriptions)

        // 키보드가 내려갈 때 이벤트가 들어옴
        NotificationCenter.Publisher(center: NotificationCenter.default, name: UIResponder.keyboardWillHideNotification)
            .sink{ (noti : Notification) in
                print("KeyboardMonitor - keyboardWillHideNotification: noti : ", noti)
                self.updatedKeyboardStatusAction = .hide
//                self.keyboardHeight = 0
            }.store(in: &subscriptions)

        // 키보드 크기가 변경될 때 이벤트가 들어옴
        NotificationCenter.Publisher(center: NotificationCenter.default, name: UIResponder.keyboardWillChangeFrameNotification)
            .sink{ (noti : Notification) in
                print("KeyboardMonitor - keyboardWillChangeFrameNotification: noti : ", noti)

                let keyboardFrame = noti.userInfo?[UIResponder.keyboardFrameEndUserInfoKey] as! CGRect

                print("KeyboardMonitor - keyboardWillChangeFrameNotification: keyboardFrame.height : ", keyboardFrame.height)
                self.keyboardHeight = keyboardFrame.height

            }.store(in: &subscriptions)

        /// 키보드 올라온 이벤트 처리 -> 키보드 높이
        NotificationCenter.Publisher(center: NotificationCenter.default, name: UIResponder.keyboardWillShowNotification)
            .merge(with: NotificationCenter.Publisher(center: NotificationCenter.default, name: UIResponder.keyboardWillChangeFrameNotification))
            .compactMap { (noti : Notification) -> CGRect in
                return noti.userInfo?[UIResponder.keyboardFrameEndUserInfoKey] as! CGRect
            }.map{ (keyboardFrame : CGRect) -> CGFloat in
                return keyboardFrame.height
            }.subscribe(Subscribers.Assign(object: self, keyPath: \.keyboardHeight))

        /// 키보드 내려갈때 이벤트 처리 -> 키보드 높이
        NotificationCenter.Publisher(center: NotificationCenter.default, name: UIResponder.keyboardWillHideNotification)
            .compactMap { (noti : Notification) -> CGFloat in
                return .zero
            }.subscribe(Subscribers.Assign(object: self, keyPath: \.keyboardHeight))


    } //init()
}
```

ViewController

```swift
//  LoginViewController.swift
//  Created by bang_hyeonseok on 2022/05/13.

import UIKit
import Combine

class LoginViewController: UIViewController{

	var keyboardMonitor : KeyboardMonitor?
	var subscriptions = Set<AnyCancellable>()

	override func viewDidLoad() {
        super.viewDidLoad()
        keyboardMonitor = KeyboardMonitor()
        observingKeyboardEvent()
}

//  화면을 터치하는 경우 키보드 dismiss
    let tap = UITapGestureRecognizer(target: self, action: #selector(hideKeyBoard)
		self.view.addGestureRecognizer(tap)

//MARK: - Functions
    @objc func hideKeyBoard() {
        print("화면Tap감지")
        self.view.endEditing(true)

    }
}

//MARK: - KeyboardMornitor
extension LoginViewController {//기기 사이즈가 너무 작으면 화면을 올려버리기

    /// 키보드 이벤트처리
    fileprivate func observingKeyboardEvent() { //키보드 height를 받아서 처리
        keyboardMonitor?.$keyboardHeight.sink{ height in
            print("LoginViewController-$keyboardHeight : ", height)
            self.loginBtnBottomConstraint.constant = height > 0 ? height : 50

            if UIDevice.current.userInterfaceIdiom == UIUserInterfaceIdiom.phone {
                print(UIScreen.main.bounds.height * UIScreen.main.scale)
                if UIScreen.main.bounds.height * UIScreen.main.scale <= 1136 {
                    self.idViewTopConstraint.constant = height > 0 ? 20 : 40
                }
            }
        }.store(in: &subscriptions)
    }

}

```

iphoneSE는 당연히 작아서 수정을해야하고

iphone 6,7,8 정도도 이렇게 반응형으로 제작을 해야 사용에 불편이 없다고 생각한다.

📌 키보드올라갈경우 변화시킨것

- 상단 회사 로고
- 패스워드를 알려주세요 라고 써있는 상태라벨의 Top Constraint
- 아이디와 패스워드 textfield 묶음을 가지고 있는 View의 Top Constraint
- 로그인버튼의 BottomConstraint, Leading / Trailling Constraint

```swift
//MARK: - KeyboardMornitor
extension LoginViewController {//기기 사이즈가 너무 작으면 화면을 올려버리기

    /// 키보드 이벤트처리
    fileprivate func observingKeyboardEvent() { //키보드 height를 받아서 처리
        keyboardMonitor?.$keyboardHeight.sink{ height in
            print("LoginViewController-$keyboardHeight : ", height)
            self.loginBtnBottomConstraint.constant = height > 0 ? height : 50
            self.loginBtnLeadingConstraint.constant = height > 0 ? 0 : 30
            self.loginBtnTrailingConstraint.constant = height > 0 ? 0 : 30
            self.loginBtn.layer.cornerRadius = height > 0 ? 0 : 15

            if UIDevice.current.userInterfaceIdiom == UIUserInterfaceIdiom.phone {
               // print(UIScreen.main.bounds.height * UIScreen.main.scale)
                if UIScreen.main.bounds.height * UIScreen.main.scale <= 1136 {
                    self.idViewTopConstraint.constant = height > 0 ? 20 : 40
                    self.statusLabelTopConstraint.constant = height > 0 ? -50 : 40
                    self.logoLabel.isHidden = height > 0 ? true : false
                }
            }
        }.store(in: &subscriptions)
    }

}
```

### 변경전

![IMG_0138](https://user-images.githubusercontent.com/76529148/169769945-93b3035c-05f6-4285-9d6d-8505e35d267e.PNG)

### 변경후

![IMG_0139](https://user-images.githubusercontent.com/76529148/169769930-3c2dd974-d5b9-4783-8c1f-4d916084da52.PNG)
