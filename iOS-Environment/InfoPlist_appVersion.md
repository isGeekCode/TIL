# Info.plist - App Version 가져오기

앱의 버전을 가져와야하는 경우가 있다.

아래 코드로 가져올 수 있다.

```swift
let appVersion = Bundle.main.infoDictionary?["CFBundleShortVersionString"] as? String
```

이 값은 옵셔널로 들어오기 때문에 필요한 경우 옵셔널 캐스팅을 해주고 사용한다.

필요한경우 옵셔널 캐스팅을 해서 사용할 수 있다.

```swift
  /// 현재 앱의 버전정보를 알려주는 함수
  /// - Returns: VersionInfo String
  func versionInfo() -> String {

    guard let appVersion = Bundle.main.infoDictionary?["CFBundleShortVersionString"] as? String else { return ""}
    return appVersion
  }

// 방법 1.
testLabel.text = "v \(versionInfo())"

// 방법 2.
let versionInfo = versionInfo()
testLabel.text = versionInfo
```
