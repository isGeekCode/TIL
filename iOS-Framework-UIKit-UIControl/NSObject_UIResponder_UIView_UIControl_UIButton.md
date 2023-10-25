# NSObject_UIResponder_UIView_UIControl_UIButton

### 클릭시 알파값으로 하이라이트 처리하기

```swift

class CustomButton: UIButton {

   private let primaryTitle: UILabel = {
        let label = UILabel()
        label.textAlignment = .center
        return label
   }()
       
   override var isHighlighted: Bool {
        get {
            return super.isHighlighted
        }
        set {
            if newValue {
                primaryTitle.alpha = 0.5
                alpha = 0.8
            }
            else {
                primaryTitle.alpha = 1.0
                alpha = 1.0
            }
            super.isHighlighted = newValue
        }
    }
    
    // Add title as subview and set frame in layoutSubviews method
}
```
![qHVq8](https://user-images.githubusercontent.com/76529148/214476113-cc85839c-832a-493f-94da-f5f648bc78c9.gif)

