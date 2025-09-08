# PHPickerViewController 사용법

## 📌 오늘의 주제
iOS 14 이상에서 권장되는 이미지 선택 방식인 **PHPickerViewController** 사용법 정리

---

## 🔍 핵심 개념

- `PHPickerViewController`는 사진 접근 권한 최소화 및 다중 선택을 지원하는 **Privacy-Friendly Picker**.
- `UIImagePickerController`의 대체제로 권장되며, 사진첩 접근 및 선택을 더 안전하게 처리 가능.

---

## ✅ 적용 순서

1. **PhotosUI 임포트**
```swift
import PhotosUI
```

2. **PHPickerConfiguration 설정**
```swift
var config = PHPickerConfiguration()
config.selectionLimit = 1 // 또는 0으로 무제한
config.filter = .images
```

3. **Picker 생성 및 delegate 설정**
```swift
let picker = PHPickerViewController(configuration: config)
picker.delegate = self
present(picker, animated: true)
```

4. **Delegate 메서드 구현**
```swift
extension ViewController: PHPickerViewControllerDelegate {
    func picker(_ picker: PHPickerViewController, didFinishPicking results: [PHPickerResult]) {
        picker.dismiss(animated: true)

        guard !results.isEmpty else {
            print("사진 선택 취소됨")
            return
        }

        guard let itemProvider = results.first?.itemProvider,
              itemProvider.canLoadObject(ofClass: UIImage.self) else { return }

        itemProvider.loadObject(ofClass: UIImage.self) { [weak self] image, error in
            guard let self, let image = image as? UIImage else { return }
            DispatchQueue.main.async {
                self.imageView.image = image
            }
        }
    }
}
```

---

## 💡 주의할 점

- `.delegate`는 `present()` 전에 반드시 지정
- 선택 취소도 `didFinishPicking`은 무조건 호출되며, `results.isEmpty`로 판단
- `.camera` 사용은 불가 → 사진 라이브러리에서만 선택 가능

---

## 📎 실전 적용 예시

`@objc private func selectImage()` 메서드
```swift
@objc private func selectImage() {
    var config = PHPickerConfiguration()
    config.selectionLimit = 1
    config.filter = .images

    let picker = PHPickerViewController(configuration: config)
    picker.delegate = self
    present(picker, animated: true)
}
```

---

## COMMENT

기존의 `UIImagePickerController`보다 안전하고 유연한 방식으로,
**취소, 다중 선택, 권한 대응** 모두 현대적 흐름에 맞춰 개선됨.  
향후 모든 이미지 선택 로직은 `PHPicker`를 기본으로 가져가는 것이 좋음.

## HISTORY
- 250611: 초안작성
