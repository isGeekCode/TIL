# MessageUI란
MessageUI는 iOS에서 문자 메시지와 이메일과 같은 메시징 기능을 구현하는 데 사용되는 프레임워크이단. 이를 사용하여 사용자가 애플리케이션에서 직접 이메일 또는 SMS 메시지를 작성하는 등 다양한 메세징 기능을 사용할 수 있다.


## MessageUI에 속한 ViewController
MessageUI에 속한 ViewController는 모두 사용자가 데이터를 입력하고 다른 사용자에게 전송하는 것을 지원한다.
각각의 ViewController는 대부분 델리게이트 프로토콜을 구현하고 사용자가 작업을 완료하거나 취소할 때 알림을 받을 수 있다. 이를 통해 애플리케이션은 작업의 성공 여부를 파악하고 적절한 조치를 취할 수 있다.


## 비슷한 기능을 하는 ViewController
각각의 프레임워크는 다르지만 공유를 하는 점에서 비슷한 기능을 한다.

### MessageUI
- **MFMailComposeViewController**
  - 이메일을 작성하고 보내는 시스템 뷰 컨트롤러.
  - [관련 TIL:MessageUI - MFMailComposeVC : 문의메일 보내기](https://github.com/isGeekCode/TIL/blob/main/Mobile-IOS/MessageUI_sendMail.md)

- **MFMessageComposeViewController**
  - SMS 및 MMS 메시지를 작성하고 보내기 위한 뷰 컨트롤러.
  - [관련 TIL:MessageUI - MFMessageComposeVC : 문자메세지 보내기
](https://github.com/isGeekCode/TIL/blob/main/Mobile-IOS/MessageUI_sendSMS.md)


### UIKit
- **UIDocumentPickerViewController**
  - 사용자가 파일을 선택하고 공유하기 위한 뷰 컨트롤러.
- **UIActivityViewController**
  - 애플리케이션에서 지원하는 모든 활동을 사용자에게 제공하여 공유할 수 있도록하는 뷰 컨트롤러.
- **UIImagePickerController**
  - 사진 또는 비디오를 선택하고 공유하기 위한 뷰 컨트롤러.


### Social
- **SLComposeViewController**
  - Twitter, Facebook 등의 소셜 미디어 서비스에 게시하기 위한 뷰 컨트롤러.
