데이터 바인딩이란


프로그래밍에서 사용되는 여러 기술과 패턴 중 하나로,  
데이터의 상태를 서로 연결하며 동기화하는 기술을 말한다.  

데이터 바인딩을 통해 뷰(UI)와 모델(Model)사잉의 데이터를 자동으로 동기화하여  
사용자 인터페이스를 효율적으로 관리할 수 있게한다.

일반적으로 간단한 앱의 MVC패턴에서는 직접 모두 구현할 수 있지만,

기본적으로 MVX형태의 패턴에는 중요한 요소로 작용한다.

하지만 비교적 러닝 커브가 높으니 시간을 두고 숙지해야한다.

<br><br>

## 데이터바인딩을 사용하는 상황

<br>

### View의 업데이트
데이터가 변경되면 자동으로 View가 업데이트되어 최신 데이터를 사용자에게 보여준다.

예를 들어, 텍스트 필드의 값이 변경되면 해당 값이 바로 레이블에 반영되는 것을 들 수 있다.

<br><br>

### 양방향 데이터 바인딩
사용자 입력이 데이터에 반영되고, 동시에 데이터의 변경이 View에 자동으로 반영되는 상호작용이 필요한 경우에 사용된다. 

위의 예와 연결하면, 사용자가 텍스트 필드에 값을 입력하면, 해당 값이 모델에 바로 반영되고, 모델값이 바뀌면 해당 값이 텍스트 필드에 자동으로 업데이트 되는 것을 들 수 있다.

<br><br>

### 이벤트 핸들링

사용자의 액션 또는 이벤트가 발생할 때, 해당 이벤트를 바로 처리하거나 모델에 반영하여 적절한 수행하는 경우 사용된다.  

예를 들어, 버튼 클릭 이벤트를 핸들링하여 특정동작을 수행하는 경우를 들 수 있다.  



## iOS에서 데이터 바인딩을 위해 사용할 수 있는 기술들
- Native구현
    - KVC(Key-Value Coding)
    - KVO(Key-Value Observing)
    - 프로퍼티 옵저버(Property Observer)
    - 옵저버 패턴
    - NotificationCenter 

- 추가사항
    - RxSwift / RxCocoa
    - Combine
    - SwiftUI Binding
    - ReactoreKit

각각의 내용은 TIL페이지에서의 포스팅을 하는대로 업로드하려고 한다.
- Native구현
    - KVC(Key-Value Coding)
    - KVO(Key-Value Observing)
<br><br>   
### 프로퍼티 옵저버
[TIL : 프로퍼티 옵저버(willSet / didSet) - 프로퍼티(2.5)](https://github.com/isGeekCode/TIL/blob/main/swift/aboutProperty205.md)
<br><br>
### 옵저버 패턴
[TIL : Cocoa Design Pattern - Observer 옵저버 패턴](https://github.com/isGeekCode/TIL/blob/main/IOS-Architecture/CocoaDesignPattern_Observer.md)
    - NotificationCenter 

- 추가사항
    - RxSwift / RxCocoa
    - Combine
    - SwiftUI Binding
    - ReactoreKit
