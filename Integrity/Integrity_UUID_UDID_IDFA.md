# Integrity - UUID / UDID / IDFA

## UUID(Universally Unique Identifier)

`기기`에 대한 고유 식별자로, iOS 6 이후 버전에서는 UUID를 직접적으로 얻을 수 없다.
MAC 주소 등을 이용해 UUID를 생성할 수 있다. 하지만 이는 보안적으로 안전하지 않은 방법.

UUID는 생성할 때 마다 랜덤하게 변경 되며 기기별로 구분할 수 있는 유니크한(중복되지 않는) 값이다.

### 그럼에도 UUID를 얻는 방법
- 라이브러리 사용하기(TAKUUID) : Cocoapods, Carthage
[링크: TAKUUID](https://github.com/taka0125/TAKUUID)
```swift
import TAKUUID

class ViewController: UIViewController {

    @IBOutlet weak var uuidInTheKeychain: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        initUUID()
    }
    
    private func initUUID() {
        TAKUUIDStorage.sharedInstance().migrate()
        uuidInTheKeychain.text = TAKUUIDStorage.sharedInstance().findOrCreate()
    }
}
```

### 키체인 사용하기
- 키체인 세팅
    - Signing & Capabilities
    - `+ Capability` 클릭
    - Keychain Sharing
    - `+`클릭 후 Identifier 입력
    Keychain Group은 이 Team ID가 같은 앱들끼리 Keychain을 공유하게 해준다. 보안주의!!
    추가 보완 필요

보통 앱을 처음 실행할 경우 UUID를 생성해서 값을 앱 내부에 저장하고 서버에도 저장을 해서 서버와 통신하며 해당 기기를 구분하게 된다. 

그런데 UUID를 앱 내부에 파일이나 DB(sqlite, core data)... 형태로 저장할 경우 앱을 지웠다가 다시 설치 하면 없어지기 때문에 앱을 지우더라도 저장값을 유지하기 위해서 보통 키체인에 저장해서 불러온다. 
(재설치 하더라도 값을 그대로 가져온다.)

키체인은 보통 암호나 인증서들을 저장하는 용도로 쓰인다.
단, 공장초기화를 하면 키체인에 저장한 값은 지워진다.  
[UUID를 키체인에 저장하는 방법](http://webs.co.kr/index.php?mid=iphone&listStyle=gallery&document_srl=3319716)

## UDID(Universally Unique Device Identifier)

역시 iOS 기기의 고유한 식별자. 이전에는 iOS 개발자들이 앱을 테스트하거나 기기를 관리할 때 UDID를 사용해왔다.

UDID 역시 개인정보 보호 문제로 iOS 7부터는 제한적으로 사용할 수 있게 되었다. 이제는 UDID를 직접적으로 얻을 수 없으며, 대신에 UUID 또는 IDFA를 사용해야 한다.

### 그럼에도 UDID를 얻는 방법

- iTunes를 통한 UDID 얻기
    - iOS 기기를 컴퓨터에 연결한 후 iTunes를 실행하고, 해당 기기를 선택한다. 이후 요약(Summary) 탭을 클릭하면 기기 정보가 표시되며, 여기서 '시리얼 번호'를 클릭하면 UDID가 표시된다. 이 방법은 iOS 6 이전 버전에서 사용 가능.

- Xcode를 통한 UDID 얻기
    - Xcode를 실행하고, iOS 기기를 컴퓨터에 연결한다. 이후 'Window' 메뉴에서 'Devices and Simulators'를 선택하고, 연결된 기기를 선택한다. 이후 'Details' 탭을 클릭하면 UDID가 표시된다.

- UDID 앱을 이용한 UDID 얻기
    - App Store에서 다운로드 가능한 'UDID 앱'을 이용해 UDID를 얻을 수도 있다. 이 앱을 설치한 후 실행하면, UDID가 표시됩니다. 이 방법은 iOS 6 이후 버전에서도 사용 가능하다.


## UUID 와 UDID 의 차이점

UUID와 UDID(는 모두 iOS 기기의 고유한 식별자. 하지만 두 식별자는 다른 목적으로 사용한다.

UUID는 앱에서 사용자를 식별하기 위해 사용한다. iOS 6 이전 버전에서는 개발자가 UUID를 직접적으로 생성할 수 있었으며, 이를 이용해 사용자 기기를 식별하는 경우가 종종 있었다. iOS 6 이후 버전에서는 UUID를 직접적으로 생성할 수 없으며, 대신 MAC 주소 등을 이용해 UUID를 생성할 수 있다. 하지만 이는 안전하지 않은 방법.

UDID는 기기 자체를 식별하기 위해 사용한다. iOS 개발자가 기기를 관리하거나 앱을 테스트할 때 UDID를 사용하기도 한다. 그러나 UDID는 개인정보 보호 문제로 iOS 7부터는 제한적으로 사용할 수 있게 되었다.

- UUID는 앱 내에서 사용자를 식별하기 위해
- UDID는 기기 자체를 식별하기 위해



## IDFA(Identifier for Advertisers)

- iOS 6 이후 버전에서는 UUID를 대신해 안전하게 사용할 수 있는 IDFA(Identifier for Advertisers)를 사용하는 것이 권장된다. IDFA는 광고 추적을 위해 사용되며, 사용자가 동의한 경우에만 수집이 가능하다.
