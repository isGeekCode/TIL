# MessageUI - MFMailComposeVC : 문의메일 보내기

## MFMailComposeViewController

iOS에서 이메일을 작성하고 보내기 위한 시스템 뷰 컨트롤러.

이를 사용하여 사용자가 이메일 본문, 수신자 목록, 제목 및 첨부 파일을 포함한 이메일을 작성하고 전송할 수 있다.


## iOS 디바이스에서 Email을 보내는 방법
- 먼저 Email을 보내려면 MessageUI를 import해야한다. 
- 시뮬레이터에서는 실행되지 않는다.
- iOS 디바이스 내 Mail계정이 연동되어 있어야만 메일 발송이 가능하다.

```

import MessageUI

// MARK: Send Mail
class SettingViewController: MFMailComposeViewControllerDelegate {

  /// 메일보내기 기능
  private func sendMail() {
  
    // 이메일 사용가능한지 체크
    if MFMailComposeViewController.canSendMail() {
      let mailComposeVC = MFMailComposeViewController()
      mailComposeVC.mailComposeDelegate = self
      mailComposeVC.setToRecipients(["bang.hyeonseok.dev@gmail.com"])
      mailComposeVC.setSubject("<앱이름> 문의하기")
      mailComposeVC.setMessageBody(bodyString(), isHTML: false)
      present(mailComposeVC, animated: true)
    } else {
      failAlertVC()
    }
  }

  // 디바이스 내 Mail앱을 이용할 수 없는 경우
  private func failAlertVC() {
    let title = "메일을 보낼 수 없습니다."
    let message = "계정을 확인하고 다시 시도해주세요."
    let alert = UIAlertController(title: "확인", message: message, preferredStyle: .alert)

    let close = UIAlertAction(title: "취소", style: .cancel)
    let move = UIAlertAction(title: "App Store로 이동", style: .default) { [weak self] _ in
      self?.moveToAppStore()
    }

    [move, close].forEach { alert.addAction($0) }
    present(alert, animated: true)
  }

  // TODO: 앱스토어 링크 수정필요
  /// 앱스토어로 이동시키는 함수
  private func moveToAppStore() {
    if let url = URL(string: Configs.appStoreURL),
        UIApplication.shared.canOpenURL(url) {
      if #available(iOS 10.0, *) {
        UIApplication.shared.open(url, options: [:], completionHandler: nil)
      } else {
        UIApplication.shared.openURL(url)
      }
    }
  }

  /// mail default contents
  private func bodyString() -> String {
    return """
           이곳에 내용을 작성해주세요.

           -------------------

           Device Model : \(getDeviceIdentifier())
           Device OS    : \(UIDevice.current.systemVersion)
           App Version  : \(getCurrentVersion())

           -------------------
           """
  }

  /// 앱 버전을 가져오는 함수
  private func getCurrentVersion() -> String {
    guard let dictionary = Bundle.main.infoDictionary,
          let version = dictionary["CFBundleShortVersionString"] as? String else { return "" }

    return version
  }

  /// 기종을 가져오는 함수
  private func getDeviceIdentifier() -> String {
    var systemInfo = utsname()
    uname(&systemInfo)
    let machineMirror = Mirror(reflecting: systemInfo.machine)
    let identifier = machineMirror.children.reduce("") { identifier, element in
      guard let value = element.value as? Int8, value != 0 else { return identifier }
      return identifier + String(UnicodeScalar(UInt8(value)))
    }
    return identifier
  }

  private func getModel() -> String {
      var systemInfo = utsname()
      uname(&systemInfo)
      let machineMirror = Mirror(reflecting: systemInfo.machine)
      let model = machineMirror.children.reduce("") { identifier, element in
          guard let value = element.value as? Int8, value != 0 else { return identifier }
          return identifier + String(UnicodeScalar(UInt8(value)))
      }
      return model
  }

  /// after sending mail
  func mailComposeController(_ controller: MFMailComposeViewController, didFinishWith result: MFMailComposeResult, error: Error?) {
    dismiss(animated: true)
  }

  /// 시스템페이지로 이동처리
  func moveToSystemSetting() {
    guard let url = URL(string: UIApplication.openSettingsURLString) else { return }

    if UIApplication.shared.canOpenURL(url) {
        UIApplication.shared.open(url)
    }
  }
}
```
