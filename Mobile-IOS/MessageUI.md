# MessageUI - MFMessageComposeVC : 문자메세지 보내기

## MFMessageComposeViewController

MFMessageComposeViewController는 iOS에서 SMS 및 MMS 메시지를 작성하고 보내기 위한 시스템 뷰 컨트롤러다. 

이 뷰 컨트롤러를 사용하면 사용자는 이미 친숙한 UI를 사용하여 메시지를 작성하고 전송할 수 있다.

또한, `MFMessageComposeViewController`는 사용자가 전송한 메시지의 상태를 추적하는 델리게이트 메서드를 제공한다.

이를 사용하여 애플리케이션은 메시지가 성공적으로 전송되었는지, 실패했는지 또는 사용자가 전송을 취소했는지 등을 확인할 수 있다.


## 간단한 사용법
```swift
import UIKit
import MessageUI

class ViewController: UIViewController, MFMessageComposeViewControllerDelegate {

  @IBAction func touchUpBtn(_ sender: Any) {
    print("btn Touch!!")
    
    let messageComposer = MFMessageComposeViewController()
    messageComposer.messageComposeDelegate = self
    if MFMessageComposeViewController.canSendText(){
        messageComposer.recipients = ["01012345678"]
        messageComposer.body = "text message"
        self.present(messageComposer, animated: true, completion: nil)
    }
  }
  
  func messageComposeViewController(_ controller: MFMessageComposeViewController, didFinishWith result: MessageComposeResult) {
      switch result {
      case MessageComposeResult.sent:
          print("전송 완료")
          break
      case MessageComposeResult.cancelled:
          print("취소")
          break
      case MessageComposeResult.failed:
          print("전송 실패")
          break
      default:
          break
      }
      controller.dismiss(animated: true, completion: nil)
  }
}
```

## MFMessageComposeViewController Delegate

델리게이트 함수들은 다음과 같다.

- messageComposeViewController:didFinishWithResult:
  - 이 메서드는 사용자가 메시지 작성 및 전송 작업을 완료하거나 취소할 때 호출된다.
  - 이 메서드는 MFMessageComposeViewController에서 메시지 작성 및 전송 작업의 결과를 전달한다.

- messageComposeViewController:shouldSendMessage:toRecipients:completion:
  - 이 메서드는 메시지를 보내기 전에 호출된다.
  - 이 메서드는 메시지 컴포즈 뷰 컨트롤러에서 작성한 `메시지의 본문`과 `수신자 목록`을 포함하는 두 개의 매개변수와 함께 호출된다.
  - 이 메서드를 구현하여 사용자가 메시지를 보내기 전에 메시지의 유효성을 검사하고 필요한 경우 메시지를 수정할 수 있다.

- messageComposeViewController:didSendMessage:
  - 이 메서드는 메시지가 성공적으로 전송된 후 호출된다.
  - 이 메서드에는 사용자가 보낸 메시지의 전체 내용이 포함된다.

- messageComposeViewController:didFailWithError:
  - 이 메서드는 메시지 작성 또는 전송 작업이 실패한 경우 호출된다.
  - 이 메서드에는 오류 객체가 포함된다.

