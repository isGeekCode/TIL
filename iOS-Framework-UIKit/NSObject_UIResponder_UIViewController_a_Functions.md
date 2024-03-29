# NSObject_UIResponder_UIViewController : 소개

UIViewController는 iOS 앱에서 사용자 인터페이스를 관리하고 화면을 제어하는 객체이다. 앱의 화면을 구성하는 뷰들과 함께 작동하여 사용자 인터페이스를 구성하고 제어하는 역할을 수행한다.

특별히 `storyboards`나 `xibs` 또는 코드로 UI를 구현한다고 해도 View 계층을 관리하기 위해서는 필수적인 클래스이다.

## UIViewController의 주요 특징과 역할

- 뷰 컨트롤러 생명주기 관리
    - UIViewController는 뷰 컨트롤러의 생명주기를 관리한다. 앱의 라이프사이클 이벤트에 따라 뷰 컨트롤러의 메서드가 호출되어 초기화, 뷰 로딩, 뷰가 나타남/사라짐, 메모리 경고 등의 상태를 처리한다.
- 사용자 인터페이스 관리
    - 앱의 화면을 구성하는 뷰들을 관리하고, View 계층 구조를 조작하여 사용자 인터페이스를 구성한다. ViewController는 뷰의 생성, 배치, 크기 조정, 레이아웃, 애니메이션 등을 다루는 역할을 수행한다.
- 사용자 이벤트 처리
    - 사용자의 입력 및 이벤트에 응답하여 적절한 동작을 수행한다. 터치, 제스처, 버튼 탭 등의 이벤트를 처리하고, 필요에 따라 액션 메서드를 호출하거나 화면 전환 등의 작업을 수행한다.
- 데이터 관리
    - 데이터를 관리하고, 필요에 따라 데이터를 가져오거나 업데이트하는 역할을 수행한다. 데이터 모델과의 상호작용을 통해 뷰 컨트롤러의 상태를 변경하고, 데이터를 뷰에 표시하거나 사용자 입력을 처리하는 등의 작업을 수행한다.
- 화면 전환 및 내비게이션 관리
    - 화면 전환과 내비게이션 스택 관리를 처리한다. 다른 뷰 컨트롤러로의 화면 전환, 내비게이션 바, 탭 바, 페이지 컨트롤 등을 이용한 앱 내비게이션을 구성하고 제어한다.
    
UIViewController는 iOS 앱의 핵심 구성 요소 중 하나로, 사용자 인터페이스의 구성과 제어, 데이터 관리, 이벤트 처리, 화면 전환 및 내비게이션 등을 담당한다.


## 주요 함수
워낙 iOS앱의 핵심 구성 요소이기 때문에 많은 함수가 존재한다.

### 생성자 함수
- [TIL : UIViewController의 생성자 함수](https://github.com/isGeekCode/TIL/blob/main/Mobile-IOS/NSObject_UIResponder_UIViewController_a_howToMake.md)



### 생명주기 함수
- [TIL : UIViewController의 생명주기 함수](https://github.com/isGeekCode/TIL/blob/main/Mobile-IOS/NSObject_UIResponder_UIViewController_lifeCycle.md)


