# CLLocation - 위치정보 사용하기

iOS에서 현재 위치의 위도와 경도를 가져오려면 Core Location 프레임워크를 사용할 수 있다. 

Core Location은 위치 관련 서비스를 제공하는 프레임워크로, GPS, Wi-Fi, 셀룰러 네트워크 등을 사용하여 사용자의 현재 위치를 결정할 수 있다.


`CLLocationManager.location` 의 값을 통해 최초에 호출한 위치값을 가져올 수 가 있다.
만약 지속적으로 업데이트를 해서 정보를 가져오고 싶다면 아래와 같이 구현하여 가져올 수 있다.


놀랍게도 CLLocationManagerDelegate 프로토콜은 모든 함수가 옵셔널로 처리되어있어서 자동으로 생성되지않는다.

아마 어떤 기능을 사용할 지 자율성을 보장하기 위해서가 아닐까?

CLLocation을 사용하면서 중요한 것은 위치접근 권한을 설정해야한다는 것이다.

반드시 Info.plist에 내용을 추가하자

## 간단한 사용법

- 1. CLLocationManager init
- 2. CLLocationManagerDelegate 를 누가 처리할지 선언
- 3. CLLocationManagerDelegate 프로톸콜 구현 
  - 3-1.(선택) didUpdateLocations(:) 구현
  - 3-2.(선택) didChangeAuthorization(:) 구현
- 4. startUpdatingLocation : 위치 업데이트 시작
- 5. (필수) Info.plist 구현

```
// info.plist 
// Key: 
// Privacy - Location When In Use Usage Description
// Value: 일단 아무내용이나 써보자
// This app needs access to your location to provide location-based services

```

```swift
    private let locationManager = CLLocationManager() // 1.

    locationManager.delegate = self // 2.

    locationManager.requestWhenInUseAuthorization() // 3. 위치 권한 요청
    locationManager.startUpdatingLocation() // 4. 위치 업데이트 시작


    // 3-1. 위치 업데이트 시 호출되는 메서드
    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        if let location = locations.last {
            let latitude = location.coordinate.latitude
            let longitude = location.coordinate.longitude
            
            // 위도와 경도 사용
            print("Latitude: \(latitude), Longitude: \(longitude)")
            
            locationManager.stopUpdatingLocation()
        }
    }
    
    // 3-2. 위치 권한 변경 시 호출되는 메서드
    func locationManager(_ manager: CLLocationManager, didChangeAuthorization status: CLAuthorizationStatus) {
        if status == .authorizedWhenInUse {
            locationManager.startUpdatiocation()
        }
    }
```



## ViewController에서 사용하기

잊지 말아야할 위치접근권한
```
// info.plist 
// Key: 
// Privacy - Location When In Use Usage Description
// Value: 일단 아무내용이나 써보자
// This app needs access to your location to provide location-based services

```


```

import UIKit
import CoreLocation

class ViewController: UIViewController, CLLocationManagerDelegate {
    private let locationManager = CLLocationManager()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        locationManager.delegate = self

        locationManager.requestWhenInUseAuthorization() // 위치 권한 요청
        locationManager.startUpdatingLocation() // 위치 업데이트 시작

    }
    
    // 위치 업데이트 시 호출되는 메서드
    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        if let location = locations.last {
            let latitude = location.coordinate.latitude
            let longitude = location.coordinate.longitude
            
            // 위도와 경도 사용
            print("Latitude: \(latitude), Longitude: \(longitude)")
            
            locationManager.stopUpdatingLocation()
        }
    }
    
//     위치 권한 변경 시 호출되는 메서드
//    func locationManager(_ manager: CLLocationManager, didChangeAuthorization status: CLAuthorizationStatus) {
//        if status == .authorizedWhenInUse {
//            locationManager.startUpdatiocation()
//        }
//    }

    // 위치 권한 변경 시 호출되는 메서드
    func locationManager(_ manager: CLLocationManager, didChangeAuthorization status: CLAuthorizationStatus) {
        switch status {
        case .authorizedAlways, .authorizedWhenInUse:
            print("GPS 권한 설정됨")
            self.locationManager.startUpdatingLocation()
        case .restricted, .notDetermined:
            print("GPS 권한 설정되지 않음")
            self.locationManager.requestWhenInUseAuthorization()
        case .denied:
            print("GPS 권한 요청 거부됨")
            self.locationManager.requestWhenInUseAuthorization()
        default:
            print("GPS: Default")
        }
    }

}
```

### 적용화면
<img width="400" alt="IMG_4259 2" src="https://github.com/isGeekCode/TIL/assets/76529148/6fbfb555-fee6-41ed-a6f9-701be095dc0c">  


## 싱글톤을 따로 구현해서 사용하는 방법

- 싱글톤 구현
```swift
import CoreLocation

class LocationManager: NSObject, CLLocationManagerDelegate {
    static let shared = LocationManager()
    
    private let locationManager = CLLocationManager()
    
    private override init() {
        super.init()
        
        locationManager.delegate = self
        locationManager.requestWhenInUseAuthorization()
        locationManager.startUpdatingLocation()
    }
    
    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        if let location = locations.last {
            let latitude = location.coordinate.latitude
            let longitude = location.coordinate.longitude
            
            // 위도와 경도 사용
            print("Latitude: \(latitude), Longitude: \(longitude)")
            
            locationManager.stopUpdatingLocation()
        }
    }
    
    func locationManager(_ manager: CLLocationManager, didChangeAuthorization status: CLAuthorizationStatus) {
        switch status {
        case .authorizedAlways, .authorizedWhenInUse:
            print("GPS 권한 설정됨")
            locationManager.startUpdatingLocation()
        case .restricted, .notDetermined:
            print("GPS 권한 설정되지 않음")
            locationManager.requestWhenInUseAuthorization()
        case .denied:
            print("GPS 권한 요청 거부됨")
            locationManager.requestWhenInUseAuthorization()
        default:
            print("GPS: Default")
        }
    }
}
```

- 외부에서 사용하기
```swift
import UIKit
import CoreLocation

class ViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        
        LocationManager.shared.delegate = self
        LocationManager.shared.startUpdatingLocation()
    }
}

extension ViewController: CLLocationManagerDelegate {
    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        if let location = locations.last {
            let latitude = location.coordinate.latitude
            let longitude = location.coordinate.longitude
            
            // 위도와 경도 사용
            print("Latitude: \(latitude), Longitude: \(longitude)")
            
            LocationManager.shared.stopUpdatingLocation()
        }
    }
}

```


## History
- 230717 : 초안작성
