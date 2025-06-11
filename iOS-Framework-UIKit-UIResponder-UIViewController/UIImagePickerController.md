# UIImagePickerController 사용법 정리

## 📌 오늘의 주제
**UIImagePickerController**를 이용한 기본적인 사진 선택 기능 구현



---

## 🔍 핵심

- `UIImagePickerController`는 **사진첩**이나 **카메라**에서 이미지를 가져오는 UIKit 기본 컴포넌트이다.
- `delegate` 프로토콜로 사용자의 선택 결과를 수신하며, 이미지 선택 후 `didFinishPickingMediaWithInfo`에서 이미지 데이터를 처리한다.
- 간단한 이미지 선택 기능에는 충분하지만, **개인정보 보호 및 다중 선택** 이슈로 인해 점점 `PHPickerViewController`로의 전환이 요구된다.  

---

## 적용 순서

1. **UIImagePickerController 생성 및 설정**
```swift
let picker = UIImagePickerController()
picker.sourceType = .photoLibrary // 또는 .camera
picker.delegate = self
```

2. **사진 선택 화면 띄우기**
```swift
present(picker, animated: true)
```

3. **선택한 이미지 처리**
```swift
extension ViewController: UIImagePickerControllerDelegate, UINavigationControllerDelegate {
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey: Any]) {
        if let image = info[.originalImage] as? UIImage {
            imageView.image = image
        }
        picker.dismiss(animated: true)
    }

    func imagePickerControllerDidCancel(_ picker: UIImagePickerController) {
        picker.dismiss(animated: true)
    }
}
```

4. **Info.plist 설정 (사진 접근 권한 요청)**
```xml
<key>NSPhotoLibraryUsageDescription</key>
<string>사진 접근을 허용해주세요.</string>
```

---

## 💡 주의할 점

- `delegate`는 두 가지 프로토콜을 모두 채택해야 한다:  
  `UIImagePickerControllerDelegate`, `UINavigationControllerDelegate`
- 실제 디바이스에서는 `.camera` 사용 시 카메라 권한 설정도 필요
- `iOS 14` 이후에는 `PHPickerViewController` 사용이 권장됨

---

## 📎 실전 적용 예시

`@objc private func selectImage()` 메서드에서 다음처럼 작성:
```swift
let picker = UIImagePickerController()
picker.sourceType = .photoLibrary
picker.delegate = self
present(picker, animated: true)
```

---

## HISTORY
- 250611: 초안 작성


