# NSObject_UIResponder : UIResponder와 Responder Chain

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

Cocoa Touch의 이벤트는 아래와 같은 종류가 있다.

- Touch Event  
    - 사용자의 터치, 탭, 스와이프와 같은 제스처에 반응한다.  
- Motion Event  
    - 가속도계, 자이로스코프를 이용한 기기의 움직임에 반응한다.  
- Remote Control Event  
    - 이어폰이나 리모트 컨트롤을 사용하여 음악 재생, 일시정지 등의 제어가 가능하다.  
- Press Event`(tvOS)`  
    - AppleTV의 Siri Remote와 같은 입력장치의 프레스 이벤트를 처리한다.  


## First Responder

이벤트가 발생하면, iOS의 시스템은 첫번째 응답자에게 이 이벤트를 처리할 기회를 준다.  

첫번째 응답자는 사용자의 입력에 직접 반응하는 객체일 수 있다.  

이 Responder는 일반적으로 화면에 직접 보이지 않을 수도 있다.



특정 타입의 이벤트를 처리하려면, 리스폰더가 해당하는 메소드를 override해야한다. 


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

---

## Responder Chain : View의 이벤트 전달


리스폰더 체인(Responder Chain)은 iOS 애플리케이션에서 이벤트 처리 및 응답을 위한 객체 간의 관계를 나타내는 개념이다. 명칭 그대로 반응할 수 있는 객체들이 사슬처럼 연결된 것을 말한다.  

이 객체들은 UIResponder를 상속하고 있고, UIApplication과 UIViewController, UIView와 UIView를 상속하는 UIControl 등이 포함된다.  

이벤트가 발생하면, 이벤트를 수신한 객체(FirstResponder)가 이를 처리할 수 없는 경우,

이벤트를 상위 객체로 전달하면서 계속해서 이벤트를 처리할 객체를 찾아가는 과정을 의미한다.


리스폰더 체인은 객체 간의 관계를 나타내는 것뿐만 아니라, 이벤트를 처리하는 데 있어서도 매우 중요한 개념이다.  

그래서 Responder Chain으로 뭔가 기능을 구현한다기보단 이걸 잘 이해하면  
  
앱의 계층 구현과 동작을 구현할 때 도움이 된다.  

<br><br>

## Responder Chain의 흐름

- 이벤트 발생
- First Responder
- Responder Chain 탐색
- 이벤트 처리
- 이벤트 미처리

한번 살펴보면 마치 생명주기와 같은 느낌이 든다.

<br><br>
이벤트도 하나의 생명주기처럼,

1. 이벤트가 발생하고  
2. 처리할 곳을 찾고  
3. 해당 객체가 이벤트를 처리하게 된다.  
4. 처리할 곳을 못 찾으면 이벤트는 사라진다.  


### 리스폰더 체인의 동작
- 이벤트가 발생하면, 해당 이벤트를 수신한 객체가 이벤트를 처리할 수 있는지 확인.
    - 이 객체는 이벤트에 대한 응답 메서드(예: touchesBegan(_:with:))를 구현하고 있어야 한다.
- 이 객체가 이벤트를 처리할 수 없는 경우, 이벤트는 이 객체의 상위 객체로 전달된다.
    - 이 상위 객체는 또한 이벤트에 대한 응답 메서드를 구현하고 있어야 한다.
- 이와 같은 방식으로 이벤트는 계속해서 상위 객체로 전달되면서, 이벤트를 처리할 수 있는 객체를 찾아간다.

<br><br>

### 예시 : 시스템의 키보드의 input View

예를 들어, View는 이벤트를 상위 View로 전달하고,  

계층의 Root View는 이벤트를 해당 ViewController로 전달한다.  

리스폰더는 UIEvent객체를 처리하지만, input View를 통해 사용자 정의 input을 허용 할 수 있다.  

<br><br>

- 사용자가 UITextField및 UITextView객체를 화면 상에서 tap

- View가 첫번쨰 리스폰더가 되어 시스템 키보드 input View가 표시된다. 
 
- 마찬가지로, 시스템 정의 input View를 만들어 다른 리스폰더가 활성화 될 때 표시할 수 있다.
 
- 사용자 지정 input View를 리스폰더와 연결하려면, 해당 View를 리스폰더의 inputView프로퍼티에 할당한다.

<br><br><br>

## Responder Chain 을 관리하는 메서드

<img width="843" alt="스크린샷 2023-04-10 오후 4 57 30" src="https://user-images.githubusercontent.com/76529148/230855641-45ca411a-e785-4098-a082-7c12f6a4a45f.png">

이 함수들이 리스폰더 체인을 관리하는 메서드들이다.

특히 becomeFirstResponder()와 resignFirstResponder는 정말 많이 사용한다.

UIResponder > UIControl > UITextField 의 관계로 상속을 받고 있기 때문에
해당 메서드들을 호출 할 수 있는 것이다.


`becomeFirstResponder()`는 UIResponder클래스의 일부로, 특정객체가 First Responder가 되도록 요청하는데 사용하는 메서드이다.  

그래서 이 메서드는 텍스트입력을 받기위해 키보드를 활성화하는 것과 같은 상황에서 사용된다.  

```swift
myTextField.becomeFirstResponder()
```

이와 반대로, `resignFirstResponder()` 메서드는 객체가 First Responder 자격을 포기하도록 요청하는데 사용된다. 

이 밖에도 

- canBecomeFirstResponder
    - 객체가 First Responder가 될 수 있는지 여부를 결정하는 데 사용된다.  
    - 이 속성을 오버라이드하여 특정 조건에서만 First Responder가 되도록 할 수 있다.   
- canResignFirstResponder
    - 객체가 First Responder를 그만둘 수 있는지 여부를 결정하는 데 사용된다.  
    - 이 속성을 오버라이드하여 특정 조건에서만 실행되도록 할 수 있다.  
- isFirstResponder
    - 객체가 현재 First Responder인지 확인하는 데 사용된다.  


<img width="785" alt="스크린샷 2023-04-10 오후 5 00 59" src="https://user-images.githubusercontent.com/76529148/230856309-b908326c-3d8e-411a-add9-a64c54219973.png">
출처 : https://gingsoft.com/?p=1348

---

<br><br><br>

## Responder Chain 탐색

first Responder가 해당 이벤트를 처리하지 않으면, Responder Chain을 따라 올라가면서 처리할 응답자를 찾는다. 이때 UIResponder의 next 속성을 통해 다음 상위 응답자에게 이벤트가 전달된다.  
이 과정은 이벤트를 처리할 수 있는 응답자를 찾을 때까지 반복된다.

### Responder Chain 따라가보기
 
Responder chain의 일반적인 순서는 아래와 같다.  

- First Responder (예: 특정한 텍스트 필드나 버튼 등)
- 그 뷰의 상위 뷰 (Superview)
- 계속 상위 뷰를 타고 올라감
- 해당 뷰의 뷰 컨트롤러 (UIViewController)
- 만약 뷰 컨트롤러가 UINavigationController, UITabBarController 등의 컨테이너 뷰 컨트롤러에 포함되어 있다면 해당 컨테이너
- UIWindow
- UIApplication
- 앱의 다른 응답자 (예: AppDelegate)

하지만 `대부분` UIViewController단계까지만 동작한다고 생각하면 된다.  

그리고 반드시 기억해야할 것은  

Responder chain은 뷰의 시각적인 배열과는 상관없이 뷰 계층의 구조에 기반한다는 것이다.  

- 사례 : UIViewController - UIView - Button
  
보통 Button의 addTarget에 동작할 메서드를 추가하는데, responder chain을 위해선 아래 코드를 세팅한다.  

<br><br>

> UIResponder를 상속하는 객체는 모두 이 메서드가 존재한다.  
> 기본적으로 이벤트가 들어오면 Reponder Chain에 의해 실행되는 메서드이고.  
> super.touchBegan이 이어서 들어오도록 세팅되어있다.  

<br>

```Swift
override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
    print("@@@@의 touchesBegan 호출")
    super.touchesBegan(touches, with: event)
}

```
<br><br>

> Button은 특별하게도 `override touchesBegan()`메서드를 구현하면  
> 내부에 `super.touchesBegan(touches, with: event)`메서드가 있어야
> `addTarget`된 메서드가 실행이 된다.  

<br>
<br>

만약 Button에서 View로 responder를 넘기고 싶다면 버튼의 유저상호작용을 false로 처리하면된다.  
```swift
button.isUserInteractionEnabled  = false
```
이렇게 하면 button 자체는 first Responder가 되지만 이벤트 처리를 상위 응답자로 넘기게 된다.

button이 특정 View에 속해 있다면,  

다음 responder는 이 특정View가 된다. 


```swift

class ParentViewController: UIViewController {
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        print("ParentViewController의 touchesBegan 호출")
        super.touchesBegan(touches, with: event)
    }
}


class CustomView: UIView {
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        print("CustomView의 touchesBegan 호출")
        // Responder Chain을 따라 이벤트를 상위 객체로 전달
        super.touchesBegan(touches, with: event) // 필요한 경우, 상위 응답자로 더 전달
    }
}

class CustomButton: UIButton {
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        print("UIButton에서 터치 이벤트를 처리하였습니다.")
        // Responder Chain을 따라 이벤트를 addTarget된 함수로 전달
        super.touchesBegan(touches, with: event)
    }
}


class ViewController: ParentViewController {
    
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        print("ViewController의 touchesBegan 호출")
        super.touchesBegan(touches, with: event) // 필요한 경우, 상위 응답자로 더 전달
    }

    override func viewDidLoad() {
        super.viewDidLoad()

        let customView = CustomView(frame: CGRect(x: 50, y: 100, width: 200, height: 200))
        customView.backgroundColor = .systemBlue
        view.addSubview(customView)

        let customButton = CustomButton(type: .system)
        customButton.frame = CGRect(x: 50, y: 50, width: 100, height: 40)
        customButton.backgroundColor = .systemCyan
        customButton.setTitle("Custom Button", for: .normal)
        customButton.addTarget(self, action: #selector(buttonTapped), for: .touchUpInside) // 버튼 탭 이벤트 처리를 추가
        customView.addSubview(customButton)
        customButton.isUserInteractionEnabled  = false
    }

    @objc func buttonTapped() {
        print("Button이 탭되었습니다.")
    }
}
```

<br><br>

## 이벤트 처리

응답자가 해당 이벤트를 처리할 수 있는 메서드를 구현하고 있다면 이벤트가 처리된다.

<br><br>

## 이벤트 미처리

이벤트를 어떤 곳에서도 처리하지 않으면 이벤트는 사라진다.

<br><br>




## 참고링크
- [Zeddios - UIResponder](https://zeddios.tistory.com/538)
