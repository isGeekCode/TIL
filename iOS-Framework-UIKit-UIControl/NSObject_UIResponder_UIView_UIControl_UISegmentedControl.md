# NSObject_UIResponder_UIView_UIControl : UISegmentedControl

UISegmentedControl은 아래와 같다.  

<img width="300" alt="ezgif-4-15e08494d6" src="https://github.com/isGeekCode/TIL/assets/76529148/83d38a3e-015a-48a8-926f-b9377eb7dd4b">

우리가 주로 보는 곳은 인증 화면에서 성별 선택하는 등의 양자택일 하는 곳에서 사용한다. 


## 사용법
```swift

class ViewController: UIViewController {

    @IBOutlet weak var mySegmentedControl: UISegmentedControl!
    
    @IBOutlet weak var resultLabel: UILabel!

    override func viewDidLoad() {
        super.viewDidLoad()
        resultLabel.text = "선택해주세요"
    }
    
    @IBAction func segmentedAction(_ sender: Any) {
        guard let sender = sender as? UISegmentedControl else { return }
        
        // 선택된 index값으로 분기처리
        if sender.selectedSegmentIndex == 0 {
            resultLabel.text = "First was selected"
        } else {
            resultLabel.text = "Second was selected"
        }
    }

```

### Code선언
```swift
import UIKit

class ViewController: UIViewController {
    
    lazy var mySegmentedControl: UISegmentedControl = {
        let control = UISegmentedControl(items: ["빨강", "파랑"])
        control.translatesAutoresizingMaskIntoConstraints = false
        control.addTarget(self, action: #selector(segmentedAction(_:)), for: .valueChanged)
        control.selectedSegmentIndex = 0
        return control
    }()
    
    lazy var resultLabel: UILabel = {
       let label = UILabel()
        label.text = "선택해주세요"
        label.font = UIFont.boldSystemFont(ofSize: 25)
        label.translatesAutoresizingMaskIntoConstraints = false
        return label
    }()

    
    lazy var resetBtn = {
        let button = UIButton()
        button.setTitle("Reset", for: .normal)
        button.titleLabel?.font = UIFont.boldSystemFont(ofSize: 15)
        button.backgroundColor = .systemBlue
        button.translatesAutoresizingMaskIntoConstraints = false
        let action = UIAction { _ in
            self.resetAction()
        }
        button.addAction(action, for: .touchUpInside)
        return button
    }()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setLayout()
        resultLabel.text = "선택해주세요"
    }
    
    @objc func segmentedAction(_ sender: UISegmentedControl) {
        print("sender.selectedSegmentIndex: \(sender.selectedSegmentIndex)")
        
        if sender.selectedSegmentIndex == 0 {
            resultLabel.text = "First was selected"
        } else {
            resultLabel.text = "Second was selected"
        }
    }
    
    func setLayout() {
        view.addSubview(mySegmentedControl)
        view.addSubview(resultLabel)
        view.addSubview(resetBtn)

        NSLayoutConstraint.activate([
            mySegmentedControl.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            mySegmentedControl.centerYAnchor.constraint(equalTo: view.centerYAnchor),
            
            resultLabel.bottomAnchor.constraint(equalTo: mySegmentedControl.topAnchor, constant: -50),
            resultLabel.centerXAnchor.constraint(equalTo: mySegmentedControl.centerXAnchor),

            resetBtn.topAnchor.constraint(equalTo: mySegmentedControl.bottomAnchor, constant: 50),
            resetBtn.centerXAnchor.constraint(equalTo: mySegmentedControl.centerXAnchor),
            resetBtn.widthAnchor.constraint(equalToConstant: 170),
            resetBtn.widthAnchor.constraint(equalToConstant: 50),
        ])
    }
    
    func resetAction() {
        print("resetBtn click")
        resultLabel.text = "선택해주세요"
        mySegmentedControl.selectedSegmentIndex = 0
    }
}
```


## UIAction을 사용하려면

마찬가지로 iOS14 부터 UIAction을 사용할 수 있게 되었다. 

여기서도 action을 생성해서 넣어줄 수 있다.  

```swift
    lazy var mySegmentedControl: UISegmentedControl = {
        let control = UISegmentedControl(items: ["빨강", "파랑"])
//        control.addTarget(self, action: #selector(segmentedAction(_:)), for: .valueChanged)
        control.selectedSegmentIndex = 0
        
        let action = UIAction { _ in 
            self.resultLabel.text =  control.selectedSegmentIndex == 0 ?  "0" : "1"
        }
        control.addAction(action, for: .valueChanged)
        
        return control
    }()
    
    lazy var resultLabel: UILabel = {
       let label = UILabel()
        label.text = "선택해주세요"
        label.font = UIFont.boldSystemFont(ofSize: 25)
        label.translatesAutoresizingMaskIntoConstraints = false
        return label
    }()

```
