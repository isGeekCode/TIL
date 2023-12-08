# NSObject_UIResponder_UIView_UIControl : UISlider


기본적인 Frame을 갖고있어 XY 축만 잡아주면 된다.  

## 간단한 사용법


```swift
class ViewController: UIViewController {

    @IBOutlet weak var slider: UISlider!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        slider.maximumValue = 30
        slider.minimumValue = 0
    }
     
    @IBAction func sliderAction(_ sender: Any) {
        guard let slider = sender as? UISlider else { return }
        print("\(slider.value)")
    }
```
