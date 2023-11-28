# NSObject_UIResponder_UIView : UITabBar

pickerView는 여러 개의 데이터 리스트에서 하나를 골라 사용하는 UIView객체이다.  

선택한 데이터는 비즈니스로직을 거쳐 가공된다. 

<img width="300" alt="스크린샷 2023-11-28 오전 10 24 42" src="https://github.com/isGeekCode/TIL/assets/76529148/90bc76f6-8ca4-4d3e-913d-ee101ec45bc9">

<br><br>
## 선언

```swift

import UIKit

class ViewController: UIViewController {

    lazy var textLabel = {
       let label = UILabel()
        label.font = UIFont.boldSystemFont(ofSize: 25)
        label.translatesAutoresizingMaskIntoConstraints = false
        return label
    }()
    
    lazy var myPickerView = {
        let pickerView = UIPickerView()
        pickerView.delegate = self
        pickerView.dataSource = self
        pickerView.translatesAutoresizingMaskIntoConstraints = false

        return pickerView
    }()
    
    lazy var resetBtn = {
       let button = UIButton()
        button.setTitle("Reset", for: .normal)
        button.titleLabel?.font = UIFont.boldSystemFont(ofSize: 15)
        button.backgroundColor = .systemTeal
        button.translatesAutoresizingMaskIntoConstraints = false
        
        let action = UIAction { [weak self] _ in
            guard let self else { return }
            resetAction()
        }
        button.addAction(action, for: .touchUpInside)
        
        return button
    }()
    
    let resetText = "과일을 골라주세요"
    let fruits = ["사과", "바나나", "체리"]
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setLayout()
        textLabel.text = resetText
    }
    
    func setLayout() {
        view.addSubview(myPickerView)
        view.addSubview(textLabel)
        view.addSubview(resetBtn)

        NSLayoutConstraint.activate([
            myPickerView.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            myPickerView.centerYAnchor.constraint(equalTo: view.centerYAnchor),
            
            textLabel.bottomAnchor.constraint(equalTo: myPickerView.topAnchor, constant: -50),
            textLabel.centerXAnchor.constraint(equalTo: view.centerXAnchor),

            resetBtn.topAnchor.constraint(equalTo: myPickerView.bottomAnchor, constant: 50),
            resetBtn.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            resetBtn.widthAnchor.constraint(equalToConstant: 150),
            resetBtn.heightAnchor.constraint(equalToConstant: 70),
        ])
    }
    
    func resetAction() {
        textLabel.text = resetText
        myPickerView.selectRow(0, inComponent: 0, animated: true) // 원하는 위치로 스크롤
    }
}


extension ViewController: UIPickerViewDelegate, UIPickerViewDataSource {
    func numberOfComponents(in pickerView: UIPickerView) -> Int {
        return 1
    }
    
    func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        return fruits.count
    }
    
    func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? {
        return fruits[row]
    }
    
    func pickerView(_ pickerView: UIPickerView, didSelectRow row: Int, inComponent component: Int) {
        textLabel.text = fruits[row]
    }
}

```


## 간단한 프로젝트
<img width="300" alt="스크린샷 2023-11-28 오전 10 29 57" src="https://github.com/isGeekCode/TIL/assets/76529148/28fcf808-dd26-42e9-a0cd-8b1cc5e6b0ba">


```swift
import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var textLabel: UILabel!
    
    let resetText = "과일을 골라주세요"
    let fruits = ["사과", "바나나", "체리"]
    
    override func viewDidLoad() {
        super.viewDidLoad()
        textLabel.text = "과일을 골라주세요"
    }
    
    
    @IBAction func resetAction(_ sender: Any) {
        
        textLabel.text = "과일을 골라주세요"
    }
}


extension ViewController: UIPickerViewDelegate, UIPickerViewDataSource {
    func numberOfComponents(in pickerView: UIPickerView) -> Int {
        return 1
    }
    
    func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        return fruits.count
    }
    
    func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? {
        return fruits[row]
    }
    
    func pickerView(_ pickerView: UIPickerView, didSelectRow row: Int, inComponent component: Int) {
        textLabel.text = fruits[row]
    }
}

```

<br><br>

<img width="300" alt="스크린샷 2023-11-28 오전 10 27 34" src="https://github.com/isGeekCode/TIL/assets/76529148/70ec8645-1d76-42bc-a453-76444e2c3c8c">

<br><br>

## Model 분리하기
```swift

import UIKit

class ViewController: UIViewController {
    
    @IBOutlet weak var textLabel: UILabel!
    
    let dataManager = DateManager()

    override func viewDidLoad() {
        super.viewDidLoad()
        textLabel.text = dataManager.firstText
    }
    
    
    @IBAction func resetAction(_ sender: Any) {
        textLabel.text = dataManager.firstText
    }
}


extension ViewController: UIPickerViewDelegate, UIPickerViewDataSource {
    func numberOfComponents(in pickerView: UIPickerView) -> Int {
        return 2
    }
    
    func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        
        if component == 0 {
            return dataManager.firstList.count
        } else {
            return dataManager.secondList.count
        }
         
    }
    
    func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? {
        
        if component == 0 {
            return dataManager.firstList[row]
        } else {
            return dataManager.secondList[row]
        }
    }
    
    func pickerView(_ pickerView: UIPickerView, didSelectRow row: Int, inComponent component: Int) {
        dataManager.updateCurrentText(firstRow: pickerView.selectedRow(inComponent: 0), secondRow: pickerView.selectedRow(inComponent: 1))
        textLabel.text = dataManager.currentText
    }
}

class DateManager {
    
    let firstList = ["빨간", "녹색", "파란", "노란"]
    let secondList = ["사과", "바나나", "체리"]
    
    var currentText = ""
    let firstText = "과일을 골라주세요"


    init(currentText: String = "") {
        self.currentText = currentText
    }
    
    func updateCurrentText(firstRow: Int, secondRow: Int) {
        currentText = "\(firstList[firstRow]) \(secondList[secondRow]) "
    }
}

```


## History

- 231128: 초안작성
