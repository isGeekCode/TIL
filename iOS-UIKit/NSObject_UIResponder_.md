# NSObject_UIResponder : Responder Chain 리스폰더 체인에 대하여

리스폰더 객체(Responder objects), 즉 UIResponder의 인스턴스는 UIKit 앱 이벤트 처리 백본(backbone)을 구성한다.

## UIResponder를 상속받는 객체

- UIResponder의 
  - UIApplication
  - UIView
    - UIWindow
  - UIViewController


이 객체들은 핵심객체들로 모두 리스폰더로서 동작할 수 있다.

어떤 이벤트가 발생하면, UIKit은 이를 처리할 수 있도록 앱의 리스폰더 객체에 전달하게 된다.

## 이벤트

Cocoa Touch에는 터치이벤트, 모션이벤트, 원격제어 이벤트 및 press이벤트를 비롯한 여러 종류의 이벤트가 있다.

특정 타입의 이벤트를 처리하려면, 리스폰더가 해당 메소드를 override해야한다.


### 예) 터치 이벤트

리스폰더는 UIKit에서 제공한 이벤트 정보를 사용하여 해당 터치의 변경사항을 추적하고, 앱의 인터페이스를 적절하게 업데이트해야한다.

- touchesBegan(_:with:)
- touchesMoved(_:with:)
- touchesEnded(_:with:)
- touchesCancelled(_:with:) 

## 처리되지않은 이벤트를 앱의 다른 부분으로 전달하는 작업을 관리

주어진 리스폰더가 이벤트를 처리하지않으면, `리스폰더 체인`의 다음 이벤트로 해당 이벤트를 전달한다.

UIKit은 미리 정의된 규칙을 사용하여 리스폰더 체인을 동적으로 관리하여 

어떤 객체가 이벤트를 수신한 다음에 어떤 객체를 선택할지 결정한다. 

## Responder Chain : View의 이벤트 전달


리스폰더 체인(Responder Chain)은 iOS 애플리케이션에서 이벤트 처리 및 응답을 위한 객체 간의 관계를 나타내는 개념이다.

이벤트가 발생하면, 이벤트를 수신한 객체(FirstResponder)가 이를 처리할 수 없는 경우,

이벤트를 상위 객체로 전달하면서 계속해서 이벤트를 처리할 객체를 찾아가는 과정을 의미한다.

리스폰더 체인은 객체 간의 관계를 나타내는 것뿐만 아니라, 이벤트를 처리하는 데 있어서도 매우 중요한 개념이다. 이벤트를 적절하게 처리하기 위해서는, 이벤트를 수신하는 객체와 해당 객체의 상위 객체들이 적절하게 이벤트를 처리할 수 있도록 리스폰더 체인을 잘 이해하고 활용해야 한다.


### 리스폰더 체인의 동작
- 이벤트가 발생하면, 해당 이벤트를 수신한 객체가 이벤트를 처리할 수 있는지 확인.
    - 이 객체는 이벤트에 대한 응답 메서드(예: touchesBegan(_:with:))를 구현하고 있어야 한다.
- 이 객체가 이벤트를 처리할 수 없는 경우, 이벤트는 이 객체의 상위 객체로 전달된다.
    - 이 상위 객체는 또한 이벤트에 대한 응답 메서드를 구현하고 있어야 한다.
- 이와 같은 방식으로 이벤트는 계속해서 상위 객체로 전달되면서, 이벤트를 처리할 수 있는 객체를 찾아간다.
- 이벤트를 처리할 객체를 찾은 후에는 해당 객체가 이벤트를 처리하게 된다.


예를들어 View는 이벤트를 상위 View로 전달하고, 계층의 Root View는 이벤트를 해당 ViewController로 전달한다.

리스폰더는 UIEvent객체를 처리하지만, input View를 통해 사용자 정의 input을 허용 할 수 있다.

### 시스템의 키보드의 input View

- 사용자가 UITextField및 UITextView객체를 화면 상에서 tap

- View가 첫번쨰 리스폰더가 되어 시스템 키보드 input View가 표시된다. 
 
- 마찬가지로, 시스템 정의 input View를 만들어 다른 리스폰더가 활성화 될 때 표시할 수 있다.
 
- 사용자 지정 input View를 리스폰더와 연결하려면, 해당 View를 리스폰더의 inputView프로퍼티에 할당한다.


## Responder Chain 을 관리하는 메서드

<img width="843" alt="스크린샷 2023-04-10 오후 4 57 30" src="https://user-images.githubusercontent.com/76529148/230855641-45ca411a-e785-4098-a082-7c12f6a4a45f.png">

이 함수들이 리스폰더 체인을 관리하는 메서드들이다.

특히 becomeFirstResponder()와 resignFirstResponder는 정말 많이 사용한다.

UIResponder > UIControl > UITextField 의 관계로 상속을 받고 있기 때문에
해당 메서드들을 호출 할 수 있는 것이다.


<img width="785" alt="스크린샷 2023-04-10 오후 5 00 59" src="https://user-images.githubusercontent.com/76529148/230856309-b908326c-3d8e-411a-add9-a64c54219973.png">
출처 : https://gingsoft.com/?p=1348

## 참고링크
- [Zeddios - UIResponder](https://zeddios.tistory.com/538)
