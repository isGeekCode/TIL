# 1. 로컬라이징

현지화, 그 나라의 실정에 맞추어서 수정하는 것을 로컬라이징 이라고한다. 

let us: Go! 세미나 내용 중

앱 내 디자인에 있어, 탭바의 레이블이 사라질 경우 장점은 무엇일까 에 대하여

![스크린샷 2022-03-17 오전 10.04.48.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/01c2335e-5bc3-44bb-b79d-3720b005c940/스크린샷_2022-03-17_오전_10.04.48.png)

→ 네이버 웹툰 앱

탭바 하단에 레이블을 생성해두면 해당 나라에서만 사용하는 것은 상관없지만

여러 나라를 타겟으로 출시하는 경우, 각 나라에 맞게 번역을 해야하는 상황 발생

- 페이스북 같은 경우는 레이블을 없앤 상태

탭바 하단의 레이블이 사라질 경우, 로컬라이징이 쉬움

본격적인 로컬라이징은 나중에 정리

[https://zeddios.tistory.com/368](https://zeddios.tistory.com/368)

# 2. 써드파티(Third party)

써드파티의 위키백과 설명은 아래와 같다.

"**기본적으로 '제 3자'를 뜻하는 단어. 이 제 3자가 어떤 분야의 제 3자를 의미하는지에 따라 의미가 나뉜다. 대체로는 제조자와 사용자 이외 외부의 생산자를 가리키는 뜻으로 쓰인다**."

→

서드파티는 해당 분야에 그 분야를 처음 개척했거나 원천기술을 확보하고 있는 등의 주요기업이 아니라

해당 분야에 호환되는 상품을 출시하거나 타 기업의 주 기술을 이용한 **파생상품** 등을 생산하는 회사들을 가르키는 용어.

스마트폰의 ios를 예로 들면

앱스토어에 들어가있는 앱들은 아이폰의 써드파티이다.(필터링 앱, 사진보정  등)

아이폰 내 번들 앱(캘린더, 메세지 등)은 퍼스트파티 (First party)라고 한다.


# UIDevice

현재 장치를 나타낸다.

A representation of the current device.

## **Declaration(선언)**

`@MainActor class UIDevice : NSObject`

## **Overview (개요)**

할당된 이름, 장치모델, 운영체제 이름 및 버전과 같은 장치에 대한 정보를 가져오기 위하여 정보를 얻기 위하여  사용한다.  또한 물리적방향과 같은 장치특성의 변동사항을 감지한다.  orientation property를 이용하여 orientation을 감지하거나,  `orientationDidChangeNotification` 기능을 등록해 변경알림을 받을 수 있다. orientation data 등을 사용하려면 `beginGeneratingDeviceOrientationNotifications()` 메서드를 사용해 데이터 전달을 활성화 해야한다. 더이상 device orientation이 필요하지 않을 때에는  `endGeneratingDeviceOrientationNotifications()` 메서드를 활용하여 데이터전달을 비활성화한다.

마찬가지로, `UIDevice` instance를 활용하여  배터리충전상태(→`batteryState` property) 및 충전수준(→`batteryLevel` property) 에 대한 알림을 받을 수 있다.

또한 근접센서 상태(`proximityState` property)를 제공한다. 근접센서는 사용자의 얼굴이 기기에 가까이 다가갔는지를 감지한다. 배터리 모니터링 혹은 근접센서 기능은 필요할 때만 활성화하길 바람. 커스텀 입력 및 키보드 보기 메뉴에서 playInputClick()메서드를 활용해여 키보드 입력 클릭을 실행 할 수 있다.

### (원문)

Use a `UIDevice` object to get information about the device such as assigned name, device model, and operating-system name and version. You also use the `UIDevice` instance to detect changes in the device’s characteristics, such as physical orientation. You get the current orientation using the `orientation` property or receive change notifications by registering for the `orientationDidChangeNotification` notification. Before using either of these techniques to get orientation data, you must enable data delivery using the `beginGeneratingDeviceOrientationNotifications()` method. When you no longer need to track the device orientation, call the `endGeneratingDeviceOrientationNotifications()` method to disable the delivery of notifications.

Similarly, you can use the `UIDevice` instance to obtain information and notifications about changes to the battery’s charge state (described by the `batteryState` property) and charge level (described by the `batteryLevel` property). The `UIDevice` instance also provides access to the proximity sensor state (described by the `proximityState` property). The proximity sensor detects whether the user is holding the device close to their face. Enable battery monitoring or proximity sensing only when you need it.

You can also use the `playInputClick()` instance method to play keyboard input clicks in custom input and keyboard accessory views.

## **Topics(주제)**

### - 공유된 장치 인스턴스 가져오기

Getting the Shared Device Instance

`class var current: UIDevice`

현재 장치를 나타내는 객체

### 사용가능한 기능 확인

- 현재장치가 멀티태스킹을 지원하는지 여부를 나타내는 Bool 값
    
    `var isMultitaskingSupported: Bool`
    

### 장치 및 운영체제 식별

- 장치 이름
    
    `var name: String`
    
- 장치에서 사용중인 운영체제 이름
    
    `var systemName: String`
    
- 운영체제의 현재 버전
    
    `var systemVersion: String`
    
- 장치의 모델
    
    `var model: String`
    
- 지역화(현지화)된 문자열로서의 장치 모델.
    
    `var localizedModel: String`
    
- **현재 장치에서 사용할 인터페이스 스타일**
    
    `var userInterfaceIdiom: UIUserInterfaceIdiom`
    
    - .phone
    - .pad
    - .tv
    - .carPlay
    - .mac
- 앱 공급업체에서 기기를 고유하게 식별하는 UUID (영숫자 문자열)
    
    `var identifierForVendor: UUID?`
    

### 기기 방향 추적

****Tracking the Device Orientation****

- 장치의 물리적 방향

`var orientation: UIDeviceOrientation`

- 장치의 물리적 방향을 설명하는 상수

`enum UIDeviceOrientation`

- 장치가 방향 알림을 생성하는지 여부를 나타내는 부울 값

`var isGeneratingDeviceOrientationNotifications: Bool`

- 장치 방향 변경 알림 생성을 시작

`func beginGeneratingDeviceOrientationNotifications()`

- 장치 방향 변경 알림 생성을 종료

`func endGeneratingDeviceOrientationNotifications()`

### 현재 방향 결정

장치가 세로 방향인지 여부를 나타내는 부울 값

`var isPortrait: Bool`

장치가 가로 방향인지 여부를 나타내는 부울 값

`var isLandscape: Bool`

지정된 방향이 위인지 아래인지를 나타내는 부울 값

`var isFlat: Bool`

지정된 방향이 세로 방향인지 가로 방향인지 여부를 나타내는 부울 값

`var isValidInterfaceOrientation: Bool`

### 장치 배터리상태 가져오기

장치의 배터리 충전 수준

`var batteryLevel: Float`

배터리 모니터링이 활성화되었는지 여부를 나타내는 부울 값입니다.

`var isBatteryMonitoringEnabled: Bool`

기기의 배터리 상태입니다.

`var batteryState: UIDevice.BatteryState`

장치의 배터리 전원 상태를 설명하는 상수입니다.

`enum UIDevice.BatteryState`

### 근접 센서 사용

근접 모니터링이 활성화되었는지 여부를 나타내는 부울 값입니다.

`var isProximityMonitoringEnabled: Bool`

근접 센서가 사용자에게 가까이 있는지 여부를 나타내는 부울 값입니다.

`var proximityState: Bool`

### ****Input Clicks 실행****

활성화된 입력 보기에서 입력 클릭을 실행

`func playInputClick()`

### ****현재 Idiom 얻기****

View, ViewController 같은 특성 환경이 있는 장치 또는 개체의 인터페이스 유형을 나타내는 상수

`enum UIUserInterfaceIdiom`

Deprecated

`~~func UI_USER_INTERFACE_IDIOM() -> UIUserInterfaceIdiom~~`

~~Returns the interface idiom supported by the current device (recommended for apps that run in versions of iOS earlier than 3.2).~~

 ****Notifications 관리****

모든 `UIDevice`notification은 에서 반환된 싱글톤 장치 인스턴스에 의해 게시된다.

- 배터리 잔량이 변경되면 게시되는 알림
    
    `class let batteryLevelDidChangeNotification: NSNotification.Name`
    
- 배터리 상태가 변경되면 게시되는 알림
    
    `class let batteryStateDidChangeNotification: NSNotification.Name`
    
- 기기의 방향이 변경될 때 게시되는 알림
    
    `class let orientationDidChangeNotification: NSNotification.Name`
    
- 근접 센서의 상태가 변경되면 게시되는 알림
    
    `class let proximityStateDidChangeNotification: NSNotification.Name`
    

# **UIScreen**

하드웨어 기반 디스플레이와 관련된 속성을 정의하는 개체

## **선언**

`@MainActor class UIScreen : [NSObject](https://developer.apple.com/documentation/objectivec/nsobject)`

## Topic

### ****사용 가능한 화면 가져오기****

`[class var main: UIScreen](https://developer.apple.com/documentation/uikit/uiscreen/1617815-main)`

장치의 화면을 나타내는 화면 개체를 반환

`[class var screens: [UIScreen]](https://developer.apple.com/documentation/uikit/uiscreen/1617812-screens)`

장치에 연결된 모든 화면을 포함하는 배열을 반환

`[var mirrored: UIScreen?](https://developer.apple.com/documentation/uikit/uiscreen/1617829-mirrored)`

외부 디스플레이에 의해 미러링되는 화면.

### ****화면 좌표 공간 얻기****

`[var coordinateSpace: UICoordinateSpace](https://developer.apple.com/documentation/uikit/uiscreen/1617833-coordinatespace)`

화면의 현재 좌표 공간

`[var fixedCoordinateSpace: UICoordinateSpace](https://developer.apple.com/documentation/uikit/uiscreen/1617819-fixedcoordinatespace)`

화면의 고정 좌표 공간

### ****경계 정보 얻기****

포인트로 측정된 화면의 사각형 경계 

`[var bounds: CGRect](https://developer.apple.com/documentation/uikit/uiscreen/1617838-bounds)`

포인트로 측정된 앱 창의 사각형 frame  **더 이상 사용되지 않음**

`~~[var applicationFrame: CGRect](https://developer.apple.com/documentation/uikit/uiscreen/1617835-applicationframe)~~`

픽셀 단위로 측정한 실제 화면의 경계 사각형

`[var nativeBounds: CGRect](https://developer.apple.com/documentation/uikit/uiscreen/1617810-nativebounds)`

기본 배율

`[var nativeScale: CGFloat](https://developer.apple.com/documentation/uikit/uiscreen/1617825-nativescale)`

화면과 관련된 자연 스케일 요소

`[var scale: CGFloat](https://developer.apple.com/documentation/uikit/uiscreen/1617836-scale)`

## 디바이스 사이즈 활용

```swift
// 뷰 전체 폭 길이
let screenWidth = UIScreen.main.bounds.size.width
    
// 뷰 전체 높이 길이
let screenHeight = UIScreen.main.bounds.size.height
```

## 기기별 사이즈 최적화시키기

```swift
    func setAutolayout() {
        if screenHeight == 896 {
            print("iPhone 11, 11proMax, iPhone XR")
        }
        else if screenHeight == 926 {
            print("iPhone 12proMax")
        }
        else if screenHeight == 844 {
            print("iPhone 12, 12pro")
        }
        else if screenHeight == 736 {
            print("iPhone 8plus")
        }
        else if screenHeight == 667 {
            print("iPhone 8")
        }
        else {
            print("iPhone 12 mini, iPhone XS")
        }
    }

// 다른 방법
switch UIScreen.main.nativeBounds.height {
    case 1136:
      print("iPhone 5 or 5S or 5C")
      break
    case 1334:
      print("iPhone 6/6S/7/8")
      break
    case 1920,2208:
      print("iPhone 6+/6S+/7+/8+")
      break
    case 2436:
      print("iPhone X")
      break
    case 1792:
        print("iPhone Xr, 11")
      break
    case 2688:
        print("iPhone 11pro max, Xs Max")
      break
    default:
      print("unknown")
}
```

### ****화면 모드 액세스****

`[var currentMode: UIScreenMode?](https://developer.apple.com/documentation/uikit/uiscreen/1617817-currentmode)`

화면과 연결된 현재 화면 모드

`[var preferredMode: UIScreenMode?](https://developer.apple.com/documentation/uikit/uiscreen/1617823-preferredmode)`

화면의 기본 표시 모드

`[var availableModes: [UIScreenMode]](https://developer.apple.com/documentation/uikit/uiscreen/1617839-availablemodes)`

화면과 연관될 수 있는 디스플레이 모드.

### ****디스플레이 링크 얻기****

`[func displayLink(withTarget: Any, selector: Selector) -> CADisplayLink?](https://developer.apple.com/documentation/uikit/uiscreen/1617820-displaylink)`

현재 화면에 대한 표시 링크 개체를 반환

`[var maximumFramesPerSecond: Int](https://developer.apple.com/documentation/uikit/uiscreen/2806814-maximumframespersecond)`

화면이 렌더링할 수 있는 초당 최대 프레임 

### ****디스플레이 밝기 설정****

`[var brightness: CGFloat](https://developer.apple.com/documentation/uikit/uiscreen/1617830-brightness)`

화면의 밝기 수준

`[var wantsSoftwareDimming: Bool](https://developer.apple.com/documentation/uikit/uiscreen/1617821-wantssoftwaredimming)`

화면이 소프트웨어에서 에뮬레이트하여 하드웨어가 일반적으로 할 수 있는 것보다 낮게 흐리게 표시될 수 있는지 여부를 나타내는 부울 값

### ****디스플레이의 오버스캔 보정 설정****

`[var overscanCompensationInsets: UIEdgeInsets](https://developer.apple.com/documentation/uikit/uiscreen/1617824-overscancompensationinsets)`

직사각형 자르기를 방지하는 데 필요한 가장자리 삽입 값

`[var overscanCompensation: UIScreen.OverscanCompensation](https://developer.apple.com/documentation/uikit/uiscreen/1617818-overscancompensation)`

외부 화면의 경우 이 속성은 오버스캔을 보상하기 위해 원하는 기술을 설정

`[enum UIScreen.OverscanCompensation](https://developer.apple.com/documentation/uikit/uiscreen/overscancompensation)`

화면 가장자리의 픽셀 손실을 보정하기 위한 다양한 기술을 설명

### ****화면 스크린샷 캡처****

`[func snapshotView(afterScreenUpdates: Bool) -> UIView](https://developer.apple.com/documentation/uikit/uiscreen/1617814-snapshotview)`

현재 화면 내용을 기반으로 스냅샷 보기를 반환

### ****화면 녹화 감지****

`[var isCaptured: Bool](https://developer.apple.com/documentation/uikit/uiscreen/2921651-iscaptured)`

시스템이 화면을 다른 대상에 적극적으로 복제하는지 여부를 나타내는 부울 값

### ****화면에서 초점 변경 처리****

`~~[var focusedItem: UIFocusItem?](https://developer.apple.com/documentation/uikit/uiscreen/1649175-focuseditem)~~`

현재 집중하고 있는 항목입니다. **더 이상 사용되지 않음**

`~~[var focusedView: UIView?](https://developer.apple.com/documentation/uikit/uiscreen/1617831-focusedview)~~`

현재 초점이 맞춰져 있는 보기입니다. **더 이상 사용되지 않음**

`~~[var supportsFocus: Bool](https://developer.apple.com/documentation/uikit/uiscreen/1617816-supportsfocus)~~`

화면이 포커스 기반 입력을 지원하는지 여부를 나타내는 부울 값. **더 이상 사용되지 않음**

### ****화면 대기 시간 얻기****

`[var calibratedLatency: CFTimeInterval](https://developer.apple.com/documentation/uikit/uiscreen/3368162-calibratedlatency)`

현재 화면에 대해 사용자가 보정한 대기 시간입니다.

### ****알림****

`[class let didConnectNotification: NSNotification.Name](https://developer.apple.com/documentation/uikit/uiscreen/1617826-didconnectnotification)`

이 알림은 새 화면이 장치에 연결될 때 게시

`[class let didDisconnectNotification: NSNotification.Name](https://developer.apple.com/documentation/uikit/uiscreen/1617837-diddisconnectnotification)`

이 알림은 화면이 장치에서 연결 해제될 때 게시

`[class let modeDidChangeNotification: NSNotification.Name](https://developer.apple.com/documentation/uikit/uiscreen/1617840-modedidchangenotification)`

이 알림은 화면의 현재 모드가 변경될 때 게시

`[class let brightnessDidChangeNotification: NSNotification.Name](https://developer.apple.com/documentation/uikit/uiscreen/1617832-brightnessdidchangenotification)`

이 알림은 화면의 밝기가 변경될 때 게시

`[class let capturedDidChangeNotification: NSNotification.Name](https://developer.apple.com/documentation/uikit/uiscreen/2921652-captureddidchangenotification)`

캡처된 화면 상태가 변경될 때 전송되는 알림

