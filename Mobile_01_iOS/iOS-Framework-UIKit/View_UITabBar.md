# UITabBar

## UITabBar
- 일반적으로 하단 모서리에 위치한다.
- `radio-style`을 가졌다. 이 말은 하나가 선택되고 다중선택을 불가능하다는 말이다.
- 앱의 모드를 결정한다. 
- UITabBarItem을 하나 이상 가진다.
- backGround 이미지를 설정할 수 있다.
- tintColor 를 설정할 수있다
- TabBar를 직접 생성하게 되면 TabBar 내의 TabItem 을 직접 추가 삭제 변경, 선택에 대한 응답을 제어하기 위해서는 delegate 가 필요합니다.


## TabBarItem
탭 표시줄의 항목을 설명하는 객체.
```swift
viewConstrollerA.tabBarItem = UITabBarItem(title: "A", image: UIImage(systemName: "star"), selectedImage: nil)

```

### Attribute(속성값)

- Background
    - backgrouondImage : TabBar에 표시할 배경이미지
- shadow
    - shadowImage : 사용자 지정 그림자 이미지
- selection
    - selectionIndicatorImage : 선택한 탭에 사용할 이미지
- imageTint
    - tintColor : 선택한 항목에 적용할 tintColor
- style
    - barStyle : 막대에 적용할 기본 스타일
    - isTranslucent : 막대의 불투명도 조절
- barTint
    - barTintColor : 막다에 들어갈 tintColor
- itemPositioning
    - itemPositioning : 위치 지정

- var delegate: UITabBarDelegate?


### Configuring tab bar items : 표시줄 항목 구성
- var items: [UITabBarItem]?

- func setItems([UITabBarItem]?, animated: Bool)

- var selectedItem: UITabBarItem?


### 탭바와 툴바의 차이

<img width="588" alt="스크린샷 2023-07-21 오후 4 25 33" src="https://github.com/isGeekCode/TIL/assets/76529148/cf13fd8f-2c6a-4687-8222-cd80644ed61b">

## History
- 230721 : 초안작성
