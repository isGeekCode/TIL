# UIKit에서 SwiftUI처럼 만들어 사용하기


- [[원본 링크]](https://bugorbn.medium.com/creating-and-modifying-uikit-components-like-in-swiftui-bf0010a8f43)
<br>
점점 UIKit을 사용하는 쪽에서 SwiftUI를 위한 환경이 많이 나오고 있다.

다만 이렇게 사용하려면 몇가지는 선언을 해주어야만 한다.


<br>
아래처럼 사용이 가능하다.

```swift
let view = UIView()
    .backgroundColor(.systemRed)
    .clipsToBounds(true)
    .cornerRadius(20)

view.addSubview(customView)

```
살짝 솔깃한 코드모양이 아닐수 없다.


<br><br><br>

먼저 선언부 코드가 좀 길어서 사용법 부터 보자.

<br><br>

### 사용법
```swift
// TextfieldDelegate는 UITextfield 세팅때문에 존재
class ViewController: UIViewController, UITextFieldDelegate {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.view.backgroundColor = .white
        
        // let customView = UIView()
        let customView = UIView(frame: CGRect(x: 50, y: 100, width: 100, height: 100))
            .backgroundColor(.systemRed)
            .clipsToBounds(true)
            .cornerRadius(20)
        
        view.addSubview(customView)

        // let customButton = UIButton()
        let customButton = UIButton(frame: CGRect(x: 50, y: 250, width: 100, height: 50))
            .backgroundColor(.systemTeal)
            .clipsToBounds(true)
            .cornerRadius(20)
            .tintColor(.black)
            .setTitle("test", for: .normal)
            .action {
                actionTest()
            }
            .isUserInteractionEnabled(true)
        
        func actionTest() {
            print(#function)
        }

        
        view.addSubview(customButton)

        // let segmentedControl = UISegmentedControl()
        let segmentedControl = UISegmentedControl(frame: CGRect(x: 50, y: 350, width: 100, height: 50))
            .backgroundColor(.systemYellow)
            .clipsToBounds(true)
            .cornerRadius(20)
            .items(["One", "Two"])
        
        view.addSubview(segmentedControl)

        // let textField = UITextField()
        let textField = UITextField(frame: CGRect(x: 50, y: 450, width: 100, height: 50))
            .placeholder("Placeholder")
            .backgroundColor(.lightGray)
            .textColor(.black)
            .contentType(.URL)
            .autocorrectionType(.yes)
            .font(.boldSystemFont(ofSize: 12))
            .delegate(self)

        view.addSubview(textField)
    }
}


```

<br><br><br>


### 선언
```swift
protocol Stylable { }

extension UIView : Stylable { }

extension Stylable where Self: UIView {
    @discardableResult
    func cornerRadius(_ value: CGFloat) -> Self {
        self.layer.cornerRadius = value

        return self
    }

    @discardableResult
    func backgroundColor(_ value: UIColor) -> Self {
        self.backgroundColor = value

        return self
    }

    @discardableResult
    func clipsToBounds(_ value: Bool) -> Self {
        self.clipsToBounds = value

        return self
    }

    @discardableResult
    func contentMode(_ value: UIView.ContentMode) -> Self {
        self.contentMode = value

        return self
    }

    @discardableResult
    func isHidden(_ value: Bool) -> Self {
        self.isHidden = value

        return self
    }
}



extension Stylable where Self: UIButton {

    @discardableResult
    func setTitle(_ title: String?, for state: UIButton.State) -> Self {
        self.setTitle(title, for: state)
        return self
    }
}

extension Stylable where Self: UIControl {
    @discardableResult
    func action(_ value: (() -> Void)?, event: UIControl.Event = .touchUpInside) -> Self {
        let identifier = UIAction.Identifier(String(describing: event.rawValue))
        let action = UIAction(identifier: identifier) { _ in
            value?()
        }
        
        self.removeAction(identifiedBy: identifier, for: event)
        self.addAction(action, for: event)
        
        return self
    }
    
    @discardableResult
    func secondAction(_ value: ((Bool) -> Void)?, controlEvent: UIControl.Event = .valueChanged) -> Self {
        let identifier = UIAction.Identifier(String(describing: controlEvent.rawValue))
        let action = UIAction(identifier: identifier) { item in
            guard let control = item.sender as? UIControl else {
                return
            }
            value?(!control.isTracking)
        }
        
        self.removeAction(identifiedBy: identifier, for: controlEvent)
        self.addAction(action, for: controlEvent)
        
        return self
    }
    
    @discardableResult
    func isEnabled(_ value: Bool) -> Self {
        self.isEnabled = value
        
        return self
    }
    
    @discardableResult
    func isUserInteractionEnabled(_ value: Bool) -> Self {
        self.isUserInteractionEnabled = value
        
        return self
    }
    
    @discardableResult
    func tintColor(_ value: UIColor) -> Self {
        self.tintColor = value
        
        return self
    }
}

// MARK: - UISegmentedControl

extension UISegmentedControl {
    @discardableResult
    func items(_ items: [String]) -> Self {
        removeAllSegments()
        for (index, item) in items.enumerated() {
            insertSegment(withTitle: item, at: index, animated: false)
        }
        return self
    }
}

// MARK: - UITextField
extension Stylable where Self: UITextField {
    @discardableResult
    func text(_ value: String?) -> Self {
        self.text = value

        return self
    }

    @discardableResult
    func font(_ value: UIFont) -> Self {
        self.font = value

        return self
    }

    @discardableResult
    func textAlignment(_ value: NSTextAlignment) -> Self {
        self.textAlignment = value

        return self
    }

    @discardableResult
    func textColor(_ value: UIColor) -> Self {
        self.textColor = value

        return self
    }

    @discardableResult
    func capitalizationType(_ value: UITextAutocapitalizationType) -> Self {
        self.autocapitalizationType = value

        return self
    }

    @discardableResult
    func keyboardType(_ value: UIKeyboardType) -> Self {
        self.keyboardType = value

        return self
    }

    @discardableResult
    func isSecureTextEntry(_ value: Bool) -> Self {
        self.isSecureTextEntry = value

        return self
    }

    @discardableResult
    func autocorrectionType(_ value: UITextAutocorrectionType) -> Self {
        self.autocorrectionType = value

        return self
    }

    @discardableResult
    func contentType(_ value: UITextContentType?) -> Self {
        self.textContentType = value

        return self
    }

    @discardableResult
    func clearButtonMode(_ value: UITextField.ViewMode) -> Self {
        self.clearButtonMode = value

        return self
    }

    @discardableResult
    func placeholder(_ value: String?) -> Self {
        self.placeholder = value

        return self
    }

    @discardableResult
    func returnKeyType(_ value: UIReturnKeyType) -> Self {
        self.returnKeyType = value

        return self
    }
    
    @discardableResult
    func delegate(_ value: UITextFieldDelegate) -> Self {
        self.delegate = value

        return self
    }


    @discardableResult
    func atributedPlaceholder(
        _ value: String,
        textColor: UIColor,
        textFont: UIFont
    ) -> Self {
        let attributedString = NSAttributedString(
            string: value,
            attributes: [
                NSAttributedString.Key.foregroundColor: textColor,
                NSAttributedString.Key.font: textFont
            ]
        )

        self.attributedPlaceholder = attributedString

        return self
    }
}


```

<br><br><br>

## 총평

UIView와 UIControl에 대한 정의를 해줘야하고,  

UIView에 속한 몇가지 유니크한 객체들만의 변수, 함수들은 직접 구현해 줘야하기 때문에  

UIKit에 대한 이해도가 필요하다.

하지만 SwiftUI를 먼저 공부하고, UIKit을 공부하는 그 사이에서는 진입장벽을 많이 낮출 수도 있을 것같다.  


<br><br>


## History
- 230731 : 초안작성
