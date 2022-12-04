# TableViewCell - accessoryType

애플문서

[https://developer.apple.com/documentation/uikit/uitableviewcell/accessorytype/](https://developer.apple.com/documentation/uikit/uitableviewcell/accessorytype/)

테이블뷰를 사용할때, 테이블뷰 셀의 옵션중에 accessoryType이라는 것이 있다.

enum으로 선택되어있고, default는 none으로 되어있다.

AccessoryType

- none
- disclosureIndicator
- detailDisclosureButton
- checkmark
- detailButton

간단히 설명해보자면 아래와 같다.

- case none
  - 액세서리가 따로 없는 기본값
- case disclosureIndicator
  - 새 콘텐츠를 표시하기 위한 셰브론 모양의 컨트롤입니다.
- case detailDisclosureButton
  - 정보 버튼 및 공개(쉐브론) 컨트롤.
- case checkmark
  - 체크마크 이미지.
- case detailButton
  - 정보 버튼
  - enum값을 각각 테이블뷰에 설정해보면 아래와 같이 나타난다.


<img width="251" alt="스크린샷 2022-12-04 오전 9 36 23" src="https://user-images.githubusercontent.com/76529148/205469300-0b4eb7f8-c55a-4378-a2f8-06f2c46386cb.png">


### DisclouserIndicator

새로운 컨텐츠를 표시하기위한 셰브론 모양의 컨트롤러다.

새롭게 보여줄 Accessory View자체를 push segue로 보여준다.

문서에 따르면 

Accessory View 안에서의 터치 이벤트에 대한 응답으로 델리게이트 함수인`tableView(_:accessoryButtonTappedForRowWith)`  을 호출하지 않는다. 

 
라고 써있는데 이 말은 나머지는 저기서 조작하라는 말인가..

### Detail Disclousure Button

information 아이콘과 DisclouserIndicator를 같이 두고 싶을 때 사용한다.

DisclouserIndicator는 마찬가지로 push segue를 할 수있다. 

detail 버튼에 대한 응답을 구현하려면 `tableView(_:accessoryButtonTappedForRowWith:)` 함수를 사용한다.

### CheckMark

이 케이스는 따로 터치를 추적하지않는다고 한다. 

체크마크를 숨기려면 none과 checkMark사이에 왔다갔다할 수 있도록

tableView(didSelectRowAt)` 함수에 구현하면 된다.

### Detail Button

information 버튼을 생성한다. 이 버튼을 눌렀을 때, 상세정보를 보여주고 싶을 때 사용한다.

detail 버튼에 대한 응답을 구현하려면 `tableView(_:accessoryButtonTappedForRowWith:)` 함수를 사용한다.
