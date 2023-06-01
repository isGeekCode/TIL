# NSObject_UIResponder_UIViewController : 생성하기

UIViewController 클래스를 살펴보면 init과 관련하여 2가지를 확인할 수 있고, 추가적으로 팩토리 메소드 패턴인 instantiateViewController를 통하여도 생성할 수 있다.

## 기본생성자 init()
### NSObject를 채택하는 모든 클래스에서 사용
NSObject 프로토콜에 있다기보단 NSObject를 상속하는 클래스자체에 모두 구현되어있다.

## init(coder:)
Interface Builder에서 생성되는 초기화 구문

### NSCoding 프로토콜
UIViewController는 NSCoding이라는 프로토콜을 채택하고 있다.

UIKit 클래스 중 많은 것들이 NSCoding 프로토콜을 구현하고 있다. 따라서 UIView, UIViewController 및 그 하위 클래스 등이 init(coder:)를 가지고 있게된다.

스토리보드 시스템은 이 init(coder:)를 이용하여 객체를 생성한다. 스토리보드 파일은 결국 아카이브된 객체 정보를 XML 형식으로 저장한 것이다. 스토리보드를 로드할 때, 스토리보드에 있는 각 객체를 위해 init(coder:)가 호출되어 각 객체가 메모리에 복원된다.

 사용하는 형태는 아래와 같다.
```swift
    required init?(coder aDecoder: NSCoder) {
        super.init(coder: aDecoder)
        
        // Initialization code
    }
```
  
`init(coder:)`메서드는 `NSCoder`를 사용하여 객체를 복원하는 초기화(initialization) 메서드이다. 스토리보드에서 뷰 컨트롤러를 인스턴스화하면 NSCoder를 통해 해당 뷰 컨트롤러의 인스턴스를 디코딩하여 복원하게 된다. 이때 init(coder:) 메서드가 호출되어 객체를 초기화한다.

하지만 최초 프로젝트를 생성하면 UIViewController내부에 init(coder:)이 없는데도 불구하고 정상적으로 빌드되는 것을 확인할 수 있다. 


### 최초 실행시 에러가 나지않는 이유

- 기본 생성자(init())의 상속: 
    - UIViewController 클래스는 NSObject를 상속받는데, NSObject는 기본 생성자(init())를 가지고 있다. 이로 인해 UIViewController도 기본 생성자를 상속받을 수 있다. 스토리보드에서 초기화될 때, 기본 생성자인 init()가 자동으로 호출되어 뷰 컨트롤러를 초기화한다.

- @available 속성
    - UIViewController 클래스에는 @available 속성이 적용되어 있다. 이 속성은 클래스나 메서드의 사용 가능 여부를 지정하는 데 사용된다. @available 속성은 init(coder:)를 사용할 수 없는 경우, unavailable로 설정되어 해당 메서드를 사용할 수 없음을 나타낸다. 이로 인해 init(coder:)가 없는 경우에도 컴파일 시 에러가 발생하지 않는다.

- 스토리보드 설정
    - 스토리보드에서 뷰 컨트롤러의 클래스를 명시적으로 지정하는 경우, 해당 클래스가 init(coder:)를 구현하지 않더라도 초기화 과정에서 문제가 발생하지 않는다. 스토리보드에서 클래스를 지정하면, 인터페이스 빌더는 초기화에 필요한 정보를 뷰 컨트롤러 객체에 설정할 수 있다.

View나 Button과 같은 것을 커스텀하는 경우, 아래 두 가지의 초기화 구문이 필수이다.

```swift
class MyCustomView: UIView {

    @IBOutlet weak var mainTitle: UILabel!
    @IBOutlet weak var subTitle: UILabel!

    override init(frame: CGRect) {
        super.init(frame: frame)
        setupView()
    }

    required init?(coder aDecoder: NSCoder) {
        super.init(coder: aDecoder)
        setupView()
    }

    func setupView() {
        let view = UIView()
        view.frame = bounds
        view.autoresizingMask = [.flexibleWidth, .flexibleHeight]
        addSubview(view)
    }
}

```

## init(nibName:bundle:)
UIViewController의 인스턴스를 초기화하는 메소드다. 이 메소드는 주로 프로그래밍 방식으로 UIViewController를 초기화 할 때 사용된다. 특별히 nib파일을 생성해서 사용할때 필요하다. 

- 메소드의 매개변수
    - nib 파일 이름
    - 번들 : 해당 nib 파일이 위치한 번들

아래 코드에서 "MyViewController"는 nib 파일의 이름이다. 이 파일은 프로젝트의 메인 번들에 위치해야 한다.
```
let myViewController = MyViewController(nibName: "MyViewController", bundle: nil)
```


이 메소드는 ViewController가 실행될때 내부적으로 자동으로 실행되지않는다. 반드시 직접 명시해야한다. 
스토리보드를 사용한다면 init(coder:)를 사용하고 nib파일을 사용한다면 init(nibName:bundle:) 를 사용하자.


## instantiateViewController(withIdentifier:)
팩토리 메서드 패턴의 일종이다. 생성자를 사용한다기 보단 객체 생성로직을 다른 클래스에 위임한 것이라고 보면된다. 

스토리보드에서 특정 뷰 컨트롤러를 로드하려면, UIStoryboard의 instantiateViewController(withIdentifier:) 메소드를 사용할 수 있다. 이 메소드는 스토리보드 파일에서 식별자에 해당하는 뷰 컨트롤러를 로드하고 인스턴스화한다.

```
let storyboard = UIStoryboard(name: "Main", bundle: nil)
let viewController = storyboard.instantiateViewController(withIdentifier: "MyViewController") as! MyViewController

```

위 코드에서 "Main"은 스토리보드 파일의 이름이고, "MyViewController"는 스토리보드 내에 있는 뷰 컨트롤러의 식별자입니다. 이 식별자는 Interface Builder에서 설정할 수 있습니다.


instantiateViewController(withIdentifier:) 메소드는 스토리보드 파일에서 식별자에 해당하는 뷰 컨트롤러를 로드하고, 이 뷰 컨트롤러의 init(coder:) 메소드를 호출하여 인스턴스화한 후, 이 뷰 컨트롤러 인스턴스를 반환한다. 
