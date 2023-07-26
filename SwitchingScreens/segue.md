# Segue를 이용한 화면이동

iOS를 하게 되면 가장 처음엔 하나의 화면으로만 앱을 만들지만 상황에 따라 여러 개의 화면이 필요해진다. 

이 때, 화면을 전환하기 위해 여러가지 방법이 있는데, 전체적인 소개는 아래 링크를 참고하자.

이 글에서는 Segue를 통하여 화면 이동을 하는 방법을 소개하고자 한다.
- [TIL : iOS에서의 화면관리 및 전환](https://github.com/isGeekCode/TIL/blob/main/SwitchingScreens/A_Various_switchingScene.md)  

<br>
<br>


## 📌 Segue가 뭔가요

Segue는 한 뷰 컨트롤러에서 다른 뷰 컨트롤러로 전환을 수행하기위한 수단이다. 

이를 이용해 사용자가 앱 내에서 다른 화면으로 이동할 수 있도록 할 수 있다.
<br>
좀더 자세히 알아보자면

Segue의 클래스는 `UIStoryboardSegue`다.

이 클래스는 `ViewController`간의 이동을 관리하기 위해 추상화하고 전환하는데에 있어서의 세부사항을 캡슐화를 하는 클래스이다. 

이전 ViewController에서 새로운 ViewController로 전환할 때, `segue`인스턴스를 사용한다. 

<br>

**Segue에서 특별한 점을 소개하자면 아래와 같다.**

- 출발지 / 도착지
- identifier
- (modal일 경우)
    - modalPresentationStyle
    - modalTransitionStyle
    
<br>
<br>

### 🍊 출발지 / 도착지
Segue는 전 화면과 후 화면을 부드럽게 전환을 해야하기 때문에, 당연하게도 출발지와 목적지가 필요하다.
Segue는 스토리보드와 함께 사용하기 때문에 스토리보드에서 출발지와 도착지를 링크하면 된다.
<br>
<br>

### 🍊 identifier
한 화면에서 여러 개의 Segue가 존재할 수도 있고, 각 Segue에 따른 데이터가 필요할 수 있다.
이를 구별하기위해 사용하는 것이 identifier다.
<br>
<br>

### 🍊 Modal방식

modal방식이란, 

`현재의 화면을 보존하면서, 사용자의 주의를 새로운 작업에 집중시키기위해 전체 화면을 차지하는 방식`을 말한다. 

예를 들어, 사용자가 사진을 선택하거나, 이메일을 작성할 때 사용할 수 있다.

이런 경우에는 새로운 뷰가 현재 뷰를 완전히 가릴 수 있다.
 
<br>
<br>
<br>

## 📌 Segue 만들기

스토리보드에서 A화면에서 B화면으로 Segue를 만들어보자.

일단 필요한 것은 trigger가 될 요소를 만들어주는 것이다.
보통은 버튼을 trigger로 사용한다.
<br>
A 화면에서 버튼을 누르면 B 화면으로 이동하는 것이다.
<br>

- 시나리오
    - 화면A(노랑)
    - 버튼 클릭
    - 화면B(파랑)로 전환
<br>

### 🍊 1. segue 시작점, 끝점 선언

화면A(노랑)의 트리거(버튼)을 클릭하고 Control버튼을 누른 상태에서 화면B(파랑)로 드래그앤드랍 한다.

<img width="600" alt="스크린샷 2023-07-25 오후 4 24 23" src="https://github.com/isGeekCode/TIL/assets/76529148/f0b8b2e1-4b46-4ef6-ade4-4af67fb074ca">

<br>
<br>

### 🍊 2. 어떤 방식으로 전환할 지 선택

그러면 아래와 같이 선택을 위한 창이 생겨난다. 
가장 일반적으로 사용하는 것은 `Present Modally`. 이걸 선택해준다.  
  
<img width="200" alt="스크린샷 2023-07-25 오후 4 23 46" src="https://github.com/isGeekCode/TIL/assets/76529148/67c7fed0-0f1d-4e07-81b8-42f82d21e03a">

<br>
<br>

### 🍊 3. 연결된 화면
그러면 두 화면 사이에 줄이 생기고 줄을 클릭하면 우측 Attribute Pannel에서 identifier를 지정할 수도 있게 된다.

identifier를 설정하지 않아도 작동한다. 지금은 세팅하지않는다.

<img width="600" alt="스크린샷 2023-07-25 오후 4 21 46" src="https://github.com/isGeekCode/TIL/assets/76529148/47c9b7e0-2df1-48c8-8db1-46b4ee2e4b97">
    
<br>
<br>

### 🍊 4. 동작 화면
노란화면 (화면A)에서 버튼을 누르면 파란화면 (화면B)로 이동하는 것을 확인할 수 있다.  
  
<img width="300" alt="ezgif-3-d5a07d300a" src="https://github.com/isGeekCode/TIL/assets/76529148/b8cdcbb0-f14b-457f-b870-ea5c7352c7fc">
    
<br><br><br>
  
## 📌 Segue로 이동한 화면에서 되돌아가기
A화면에서 B화면으로 Segue를 통해 화면을 띄웠다.
작업을 마치고 이제 다시 A화면으로 돌아가는 방법을 알아보자.

이걸 구현하는 방법은 두 가지가 있다.

- B화면에서 `dismiss(animated:)` 메서드를 통해 돌아가기
- A화면으로 돌아올 `Unwind Segue` 구현하기

두 방법 모두 `@IBAction`을 구현해야한다.

<br><br><br>

---
### 🍊 첫번째 방법 : B화면에서 `dismiss(animated:)` 메서드를 통해 돌아가기 

- ⭐️ 1. B화면에서 트리거로 사용할 버튼을 만든다.
    - 스토리보드에서 Button 생성하기

<br>

- ⭐️ 2-1. 스토리보드를 통해 `@IBAction` 코드를 만든다.

    - 스토리보드에서 트리거가 될 버튼을 클릭하고 Control 버튼을 누른상태에서 코드 부분으로 드래그앤드랍한다.
    
        <img width="700" alt="스크린샷 2023-07-25 오후 4 55 44" src="https://github.com/isGeekCode/TIL/assets/76529148/80aad632-fe50-4169-a653-620068252533">
        
    - Action을 선택, 메서드명 입력, touchUpInside 를 선택하고 Connect
    
        <img width="400" alt="스크린샷 2023-07-25 오후 4 56 33" src="https://github.com/isGeekCode/TIL/assets/76529148/a3aed7e7-5f16-4d53-904a-0a296d7c9b3d">
        
    - 연결된 화면
    
        <img width="700" alt="스크린샷 2023-07-25 오후 4 59 01" src="https://github.com/isGeekCode/TIL/assets/76529148/4068640f-2913-4d8c-b765-9f233a15ea60">
        
    - 3번과정을 진행한다.
<br><br>
  
- ⭐️ 2-2. B화면의 ViewController 내부에서 `@IBAction` 메서드를 만든다.

    - 아래처럼 구현하면 `@`좌측에 빈 원이 하나 생긴다.
        ```swift
        @IBAction func dismissToA(_ sender: Any) {

        }
        ```

    - IBAction 좌측의 빈 원을 스토리보드의 트리거 버튼으로 드래그앤드랍한다. 그러면 링크된다.
    
        <img width="700" alt="스크린샷 2023-07-25 오후 5 05 12" src="https://github.com/isGeekCode/TIL/assets/76529148/7e75632e-c117-4808-8ab4-e355ada46570">
<br><br>
  
- ⭐️ 3. dismiss 메서드 구현
    ```swift
    @IBAction func dismissToA(_ sender: Any) {
        self.dismiss(animated: true)
    }
    ```
<br><br>
  
> 모달로 표시된 화면에서는 `self.dismiss()`메서드를 이용하여 이전 화면으로 돌아갈 수 있다.
> navigationController를 이용한 화면이라면 `popViewController()`메서드를 사용하여 이전 화면으로 돌아갈 수 있다.

<br><br>

- ⭐️ 4. 동작화면
<img width="300" alt="스크린샷 2023-07-25 오후 5 05 12" src="https://github.com/isGeekCode/TIL/assets/76529148/0dd0c1bf-f409-428c-be4c-ce251237e495">


<br><br><br>


---
### 🍊 두번째 방법 : A화면으로 돌아올 `Unwind Segue` 구현하기

- ⭐️ 1. B화면에서 트리거로 사용할 버튼을 만든다.
    - 스토리보드에서 Button 생성하기

<br>

- ⭐️ 2. 도착할 화면인 화면A(노랑)의 ViewController 내부에 `@IBAction` 메서드를 만든다.  
    unwind segue를 사용할 때는 구현한 메서드 내부에는 따로 `dismiss()`메서드를 구현할 필요가 없다.  
    자체가 현재 화면으로 돌아올 통로를 만들어주는 과정이기 때문이다.
    
    - 파라미터를 `segue: UIStoryboardSegue`로 세팅한다.
        ```swift
        @IBAction func unwindToA(segue: UIStoryboardSegue) {
            
        }
        ```

    - 메서드 내부에는 돌아올 때, 구현하고 싶은 동작을 구현할 수 있다.  
        completion() 처럼 사용하는 것이다. 
        
        
- ⭐️ 3. 스토리보드에서 unwind segue를 연결한다.
        
    - 돌아오기 시작할 화면B의 상단의 exit 버튼을 마우스 우클릭한다.
    
        <img width="700" alt="스크린샷 2023-07-26 오후 3 04 11" src="https://github.com/isGeekCode/TIL/assets/76529148/49976b7c-eb7f-4a47-9d5e-da4c917fd600">
        
    - 그러면 보이는 Segue를 선택해서 트리거가 될 버튼으로 연결한다.
      `이때 현재 프로젝트에 활성화 되어있는 UIStoryboardSegue가 여러 개 보일 수 있다.`  
      원하는 Segue를 확인하자.
    
        <img width="700" alt="스크린샷 2023-07-26 오후 3 04 20" src="https://github.com/isGeekCode/TIL/assets/76529148/38b0d449-7097-4802-b2ce-792724f0ab52">

        
    - 연결을 하면 팝업이 뜰텐데 action을 선택하자.
    
        <img width="700" alt="스크린샷 2023-07-26 오후 3 04 35" src="https://github.com/isGeekCode/TIL/assets/76529148/dbebf9b5-b714-4999-a775-c189088550fe">

<br><br>
        
- ⭐️ 4. 동작화면
<img width="300" alt="스크린샷 2023-07-25 오후 5 05 12" src="https://github.com/isGeekCode/TIL/assets/76529148/57c819d1-f86e-407d-b423-533e78872121">


<br><br><br>
---
### 🍊 두 방법의 차이

두 방법의 동작을 보면 사실상 동일해보인다. 

첫번째 방법은 화면A의 상단에 생성된 화면B에서 `self.dismiss()`메서드를 실행하는 것이다.

두번째 방법은 화면 A로 돌아갈 길을 만들기 위해 화면A의 내부 코드블럭에 `unwind segue`를 구현했다.


> 즉, 첫번째는 돌아오기 시작하려는 곳에서 실행하는 것이라면 두번째는 돌아올 도착지에서 실행하는 것이다. 


<br><br><br>


## 📌 Unwind Segue 응용하기

위에서 구현한 unwind의 장점은 돌아오려는 도착화면에서 지점을 만들어주는 방식이기 때문에
여러 화면에서 재사용이 가능하다.

<br>

아래 A(노랑), B(파랑), C(빨강) 세 화면을 보자. 모두 modal로 segue를 연결했다.

<img width="700" alt="스크린샷 2023-07-26 오후 3 36 35" src="https://github.com/isGeekCode/TIL/assets/76529148/87fe8858-f072-4471-b7f0-ca32f14a6215">

<br><br>

이 때 ViewController의 코드를 아래와 같이 각 A, B에 Unwind를 구현해보자.

```Swift
import UIKit

class ViewControllerA: UIViewController {
    @IBAction func unwindToA(segue: UIStoryboardSegue) { }
}

class ViewControllerB: UIViewController {
    @IBAction func unwindToB(segue: UIStoryboardSegue) { }
}

class ViewControllerC: UIViewController { }
```

생성한 `UIStoryboardSegue`를 각 화면에 연결하는데,

A로 돌아가는 segue는 

화면B와 화면C에 중복으로 세팅이 가능하다.
<br><br>

<img width="700" alt="스크린샷 2023-07-26 오후 3 41 19" src="https://github.com/isGeekCode/TIL/assets/76529148/413baeed-e0c1-4dd8-a17d-e6adfc7b3237">

<br><br>

- ⭐️ 4. 동작화면
<img width="300" alt="스크린샷 2023-07-25 오후 5 05 12" src="https://github.com/isGeekCode/TIL/assets/76529148/48f1d255-5cea-414b-b310-b7ed48db76bf">



<br><br><br>

    
```swift
import UIKit

class ViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
    }
    func createButton(title: String, action: Selector, yPos: CGFloat) {
        let screenWidth = UIScreen.main.bounds.width
        let buttonWidth: CGFloat = 200
        let xPos = (screenWidth - buttonWidth) / 2

        let button = UIButton(frame: CGRect(x: xPos, y: yPos, width: buttonWidth, height: 50))
        button.setTitle(title, for: .normal)
        button.setTitleColor(.white, for: .normal)
        button.backgroundColor = .darkGray
        button.addTarget(self, action: action, for: .touchUpInside)
        view.addSubview(button)
    }
}

class ViewControllerA: ViewController {

//    @IBAction func unwindToA(_ segue: UIStoryboardSegue) {
//        print("unwind")
//    }

    override func viewDidLoad() {
        super.viewDidLoad()
    }
}

class ViewControllerB: ViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        createButton(title: "Dismiss", action: #selector(dismissViewController), yPos: 100)
    }
    
    @objc func dismissViewController() {
        self.dismiss(animated: true)
    }

    @objc func popViewController() {
        self.dismiss(animated: true)
    }
}

extension UIApplication {
    class func topViewController() -> UIViewController? {
        if #available(iOS 13.0, *) {
            return shared.windows.first { $0.isKeyWindow }?.rootViewController?.topViewController
        } else {
            return shared.keyWindow?.rootViewController?.topViewController
        }
    }
}

extension UIViewController {
    var topViewController: UIViewController? {
        if let presentedViewController = presentedViewController {
            return presentedViewController.topViewController
        }
        if let navigationController = self as? UINavigationController {
            return navigationController.visibleViewController?.topViewController
        }
        if let tabBarController = self as? UITabBarController {
            return tabBarController.selectedViewController?.topViewController
        }
        return self
    }
}

class ViewControllerC: ViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        
        createButton(title: "Dismiss", action: #selector(dismissViewController), yPos: 100)
        createButton(title: "DismissToBlue", action: #selector(DismissToBlue), yPos: 200)
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        let destVC = segue.destination as? ViewControllerA
    }
    
    
    @objc func dismissViewController() {
        self.dismiss(animated: true)
    }
    
    @objc func DismissToBlue() {
        self.dismiss(animated: true) {
            if let topViewController = UIApplication.topViewController() {
                topViewController.dismiss(animated: true)
            }
        }
    }
}

```