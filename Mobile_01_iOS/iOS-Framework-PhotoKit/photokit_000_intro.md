# PhotoKit - Introduce
PhotoKit은 iOS와 macOS에서 사진과 비디오 라이브러리를 관리하고 조작하기 위한 프레임워크다.  

이를 통해 사용자는 디바이스에 저장된 사진과 비디오를 검색, 관리 및 편집할 수 있다. 


## 주요 클래스

- PHPhotoLibrary: 사진 라이브러리에 접근하고 변경 사항을 반영하는 클래스.
- PHAsset: 사진과 비디오의 메타데이터를 나타내는 클래스.
- PHFetchResult: 특정 조건에 따라 검색된 PHAsset 객체의 컬렉션을 나타내는 클래스.
- PHImageManager: 사진과 비디오의 이미지 및 비디오 데이터를 요청하고 제공하는 클래스.
- PHAssetCollection: 앨범이나 순간을 나타내는 클래스.


## 권한
사진 라이브러리에 접근하려면 사용자로부터 권한을 요청해야 한다. 이를 위해 Info.plist 파일에 다음과 같은 항목을 추가해야 한다.


```xml
<key>NSPhotoLibraryUsageDescription</key>
<string>사진 라이브러리에 접근하기 위한 설명</string>
```

### 권한요청

```swift
import UIKit
import Photos

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        PHPhotoLibrary.requestAuthorization { status in
            switch status {
            case .authorized:
                print("사용자가 사진 라이브러리 접근을 허용함")
                self.fetchPhotos()
                
            case .denied, .restricted:
                print("사용자가 사진 라이브러리 접근을 거부함")
            case .notDetermined:
                print("사용자가 아직 결정하지 않음")
            @unknown default:
                fatalError("알 수 없는 상태")
            }
        }
    }
    
    // 사진 정보 호출
    func fetchPhotos() { }
}
```




