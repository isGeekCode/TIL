Responder Chain에 대하여

iOS에서의 Responder Chain은 이벤트 처리시스템의 일부로, <br>

사용자의 터치, 키 입력과 같은 이벤트를 어떻게 처리할지 결정하는 메커니즘이다.  

그래서 Responder Chain으로 뭔가 기능을 구현한다기보단 이걸 잘 이해하면  
  
앱의 계층 구현과 동작을 구현할 때 도움이 된다.  
<br>

Responder Chain은 말그대로 반응할 수 있는 객체들이 사슬처럼 연결된 것을 말한다.  

이 객체들은 UIResponder를 상속하고 있고, UIApplication과 UIViewController, UIView와 UIView를 상속하는 UIControl 등이 포함된다.  

<br><br>

일단 기본적인 Reponder Chain의 로직을 살펴보자

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
3. 이벤트 처리를 하는 것이다.  
4. 처리할 곳을 못 찾으면 이벤트는 사라진다.  

<br><br>

좀더 자세하게 살펴보자.  

### 이벤트 발생
사용자가 화면을 터치하면, 이벤트가 발생한다.

이벤트는 아래와 같은 종류가 있다.

- Touch Event  
    - 사용자의 터치, 탭, 스와이프와 같은 제스처에 반응한다.  
- Motion Event  
    - 가속도계, 자이로스코프를 이용한 기기의 움직임에 반응한다.  
- Remote Control Event  
    - 이어폰이나 리모트 컨트롤을 사용하여 음악 재생, 일시정지 등의 제어가 가능하다.  
- Press Event`(tvOS)`  
    - AppleTV의 Siri Remote와 같은 입력장치의 프레스 이벤트를 처리한다.  
    
이밖에도 다양한 이벤트가 존재한다.  

<br><br>

## First Responder

이벤트가 발생하면, iOS의 시스템은 첫번째 응답자에게 이 이벤트를 처리할 기회를 준다.  

첫번째 응답자는 사용자의 입력에 직접 반응하는 객체일 수 있다.  

이 Responder는 일반적으로 화면에 직접 보이지 않을 수도 있다.
   


<br><br>

iOS앱을 만들다보면, `becomeFirstResponder()`나 `resignFirstResponder()`메서드를 본 적이 있을 것이다.  

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


<br><br>

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
```Swift
override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
    print("@@@@의 touchesBegan 호출")
    super.touchesBegan(touches, with: event)
}

```
<br><br>

또한 Button은 특별하게도 touchesBegan()메서드가 존재하면 super.touchesBegan(touches, with: event)메서드가 있어야 addTarget된 메서드가 실행이 된다.  
<br>
<br>
만약 Button에서 View로 responder를 넘기고 싶다면 버튼의 유저상호작용을 false로 처리하면된다.  
```swift
button.isUserInteractionEnabled  = false
```
이렇게 하면 button 자체는 first Responder가 되지만 이벤트 처리를 상위 응답자로 넘기게 된다.



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


<br><br>









<br><br><br>

## History
- 230731 : 초안작성
