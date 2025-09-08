# SwiftUI - View 프로토콜

SwiftUI에서 View는 View Protocol을 채택하는 구조체다.  

이 말은 즉,  
UIView와 달리 View는 어떤 stored property도 상속받지 않는다는 말이다.  

SwiftUI는 이 View 계층을 효율적인 데이터구조만 가지고 엄청 자주 만들고 없애는 것을 반복한다.  

## 프로퍼티
View 프로토콜은 `body`라는 프로퍼티 하나만을 요구한다.  
이 `body`프로퍼티는 이 자체로 `View`다. 

어떤 View든지 이 Viewd의 body 안에 있는 View를 렌더링하게 된다.  

## @State

State로 프로퍼티를 선언하면 SwiftUI가 알아서 읽고 써야하는 타이밍을 재고있게 된다.  

State로 감싸진 값이 바뀐다는 것 : 상태값이 바뀐다.  
그러면 body에 다시 물어보게 되는 것이다.  
그래서 View가 refresh되고 렌더링까지 이뤄지게 되는것이다.  

---
아 어렵네

## History
- 231212: 초안작성
