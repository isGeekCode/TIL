# CLLocation - 비콘 조회하기
CLLocation은 현재 위치를 알기위해 사용하기도 하지만, 비콘이라는 장치를 조회하는 데도 사용할 수 있다.

비콘(Beacon)은 주변에 있는 장치들에게 신호를 발송하여 블루투스 기술을 이용해 위치 정보를 전송하는 작은 무선 송신 장치이다. 주로 Bluetooth Low Energy(BLE)를 이용하여 동작하며, 소형화되어 휴대성이 좋다.

비콘은 보통 UUID(Universally Unique Identifier)를 포함한 식별자와 추가적인 정보인 Major 값과 Minor 값으로 구성된다. 비콘은 주변 장치들이 해당 비콘의 신호를 수신하여 식별하고, 이를 통해 위치 정보를 파악할 수 있다.

비콘은 다양한 분야에서 활용될 수 있는데 주로 위치 기반 서비스에서 사용되며, 실내 네비게이션, 광고 및 마케팅, 출결 체크, 자동화 시스템 등에 적용될 수 있다. 예를 들어, 상점 내에서 고객에게 할인 정보를 제공하기 위해 비콘을 사용하거나, 박물관에서 전시물의 설명을 비콘을 통해 제공할 수 있다.

비콘은 주변 장치들이 비콘의 신호를 감지하고 이를 활용하여 다양한 서비스와 상호작용하는 데에 활용될 수 있다.



## 간단한 사용법

```swift
import UIKit
import CoreLocation

class ViewController: UIViewController, CLLocationManagerDelegate {
    let locationManager = CLLocationManager()
    let targetUUIDString = "YOUR_TARGET_UUID" // 여기에 타겟 UUID 문자열을 입력.

    override func viewDidLoad() {
        super.viewDidLoad()
        
        // CLLocationManager 설정
        locationManager.delegate = self
        locationManager.requestWhenInUseAuthorization()
        
        // 타겟 UUID 문자열을 올바른 UUID 형식으로 변환
        guard let targetUUID = UUID(uuidString: targetUUIDString) else {
            print("Invalid target UUID")
            return
        }
        
        // 비콘 탐색을 위한 CLBeaconIdentityConstraint 생성
        let constraint = CLBeaconIdentityConstraint(uuid: targetUUID)
        // 비콘 탐색 시작
        locationManager.startRangingBeacons(satisfying: constraint)
    }
    
    // 비콘 탐색 결과 처리
    func locationManager(_ manager: CLLocationManager, didRange beacons: [CLBeacon], satisfying constraint: CLBeaconIdentityConstraint) {
        for beacon in beacons {
            if beacon.uuid == UUID(uuidString: targetUUIDString) {
                // 타겟 UUID와 일치하는 비콘을 찾았을 때 동작할 코드 작성
                print("비콘을 찾았습니다!")
                // 추가로 원하는 작업을 수행하거나 UI 업데이트 등을 할 수 있다.
                print("일치한 비콘정보 : \(beacon)")
                // 탐색 정지
                print("비콘을 탐색종료!")
                locationManager.stopRangingBeacons(satisfying: constraint)
            }
        }
    }
}
```


주변의 비콘 정보를 탐색 시작하고 탐색 종료하기 위해서는 CLBeaconIdentityConstraint 객체를 생성해야한다.
CLBeaconIdentityConstraint는 탐색해야할 목표 정보를 담을 수 있다.
이 CLBeaconIdentityConstraint는 `startRangingBeacons(satisfying:)`의 파라미터 값으로 들어간다

- 탐색 시작 : locationManager.startRangingBeacons(satisfying:)
- 탐색 종료 : locationManager.stopRangingBeacons(satisfying:)

```swift

// MARK: 탐색 시작하기
// 타겟 UUID 문자열을 올바른 UUID 형식으로 변환

let targetUUIDString = "YOUR_TARGET_UUID" // 여기에 타겟 UUID 문자열을 입력.

guard let targetUUID = UUID(uuidString: targetUUIDString) else {
    print("Invalid target UUID")
    return
}
// 비콘 탐색을 위한 CLBeaconIdentityConstraint 생성
let constraint = CLBeaconIdentityConstraint(uuid: targetUUID)

// 비콘 탐색 시작
locationManager.startRangingBeacons(satisfying: constraint)


// MARK: 탐색 종료하기

// 탐색한 결과를 가져오는 Delegate함수
func locationManager(_ manager: CLLocationManager, didRange beacons: [CLBeacon], satisfying constraint: CLBeaconIdentityConstraint) {

    for beacon in beacons {

        // print("주변에 조회되는 비콘정보 : \(beacon)")

        // 조회되는 비콘 중 원하는 비콘을 찾은 경우
        if beacon.uuid == UUID(uuidString: targetUUIDString) {
            print("일치한 비콘정보 : \(beacon)")

            // 탐색 종료 처리
            locationManager.stopRangingBeacons(satisfying: constraint)
        }
    }
}

```


## History
- 230719: 초안작성
