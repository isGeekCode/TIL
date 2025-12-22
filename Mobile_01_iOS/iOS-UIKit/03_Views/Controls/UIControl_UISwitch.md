# UISwitch
UISwitch는 iOS 애플리케이션에서 사용자가 특정 설정을 켜고 끄는 데 사용되는 UI Control 객체이다.

스위치는 일반적으로 2진수의 옵션(On 또는 Off)을 나타내고, 사용자가 스위치를 터치하여 설정을 변경할 수 있다.
사용자에게 현재 설정 상태를 시각적으로 표시한다. 

그래서 일반적으로 애플리케이션의 설정 화면이나 사용자 기본 설정을 조정하는 기능에서 많이 사용된다.

## 주요 특징

- On/Off 상태 표시
    - UISwitch는 현재 설정 상태를 사용자에게 시각적으로 표시한다. 켜진 상태일 때는 스위치의 색상과 애니메이션으로 켜진 상태를 나타내고, 꺼진 상태일 때는 다른 색상과 모양으로 꺼진 상태를 나타낸다.

- 상태 변화 감지: 사용자가 스위치를 터치하여 설정을 변경할 때, UISwitch는 상태 변화를 감지하고 해당 정보를 애플리케이션에 알린다. 이를 통해 애플리케이션은 사용자의 설정에 따라 필요한 동작을 수행할 수 있다.

- 값 저장: UISwitch는 On 또는 Off와 같은 이진 값을 가지며, 이 값을 애플리케이션 내에서 저장하고 사용할 수 있다. 사용자의 설정을 나중에 검색하거나 변경된 설정을 지속적으로 유지할 수 있다.


## 간단한 사용법

### 선언

```swift
let mySwitch = UISwitch()
view.addSubview(mySwitch)


// 제약조건으로 위치 크기를 정하는 경우
mySwitch.translatesAutoresizingMaskIntoConstraints = false
NSLayoutConstraint.activate([
    mySwitch.centerXAnchor.constraint(equalTo: view.centerXAnchor),
    mySwitch.centerYAnchor.constraint(equalTo: view.centerYAnchor)
])


// Frame으로 위치 크기를 정하는 경우
mySwitch.frame = CGRect(x: 100, y: 100, width: 50, height: 30)

// 초기 상태 세팅 (default: false)
mySwitch.isOn = true

// 이벤트처리
mySwitch.addTarget(self, action: #selector(switchValueChanged(_:)), for: .valueChanged)

// 처리할 이벤트
@objc func switchValueChanged(_ sender: UISwitch) {
    if sender.isOn {
        // UISwitch가 켜진 상태로 변경되었을 때 수행할 작업
    } else {
        // UISwitch가 꺼진 상태로 변경되었을 때 수행할 작업
    }
```
### tag로 switch를 구분하는 경우
변수선언, 레이아웃, addSubView은 기본과 동일
```swift

// 세팅
firstSwitch.tag = 100
secondSwitch.tag = 101

// 처리할 이벤트 조건문 처리
@objc func setValueChanged(_ sender: UISwitch) {

    // switch문
    switch sender.tag {
    case 100:
        //tag 100 determine
    case 101:
        //tag 101 determine
    default:
        return
    }
    
    /* 
    // if문
    if sender.tag == 100 {
        //tag 100 determine
    } else if sender.tag == 101 {
        //tag 101 determine
    }
    
    */
}
```

### UISwitch 색상변경
들어가는 색상은 3종류가 있다.
- tintColor
- onTintColor
    - 스위치가 켜진 상태일 때의 배경 색상
    - 따로 지정하지않을 경우 nil로 나온다. 기본적으로 systemGreen 색상으로 나온다.
- thumbTintColor
    - 스위치의 Thumb(핸들러)부분의 색상


```swift
```

### UISwitch에 Image넣기

```swift
// 이미지 파일명으로부터 UIImage 인스턴스 생성
let onImage = UIImage(named: "onImageName")
let offImage = UIImage(named: "offImageName")

// UISwitch 인스턴스 생성
let mySwitch = UISwitch()

// 이미지 할당
mySwitch.onImage = onImage
mySwitch.offImage = offImage
```
