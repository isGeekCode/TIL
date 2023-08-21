# MVC -> MVP -> MVVM : ColorSelectApp

이번엔 

### 동작설명
- 첫번째 토글을 켜면 Green이라는 값을 Label에 띄운다.
- 두번째 토글을 켜면 Yellow라는 값을 Label에 띄운다.
- 두 개가 모두 켜지면 두값 사잉에 and를 넣는다. 


<br><br>


# 단일 ViewController



<br><br>

### 전체코드

<details><summary>예시 코드</summary>

```swift

import UIKit

class ViewController: UIViewController {

    var statusLabal = UILabel()
    var greenSwitch = UISwitch()
    var yellowSwitch = UISwitch()
    
    override func viewDidLoad() {
        super.viewDidLoad()

        [statusLabal, greenSwitch, yellowSwitch].forEach {
            $0.translatesAutoresizingMaskIntoConstraints = false
            view.addSubview($0)
        }
        
        NSLayoutConstraint.activate([
            statusLabal.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            statusLabal.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 100),
            statusLabal.widthAnchor.constraint(equalToConstant: 300),
            statusLabal.heightAnchor.constraint(equalToConstant: 300),

            greenSwitch.topAnchor.constraint(equalTo: statusLabal.bottomAnchor, constant: 50),
            greenSwitch.centerXAnchor.constraint(equalTo: statusLabal.centerXAnchor),

            yellowSwitch.topAnchor.constraint(equalTo: greenSwitch.bottomAnchor, constant: 50),
            yellowSwitch.centerXAnchor.constraint(equalTo: greenSwitch.centerXAnchor),
        ])

        statusLabal.textAlignment = .center
        statusLabal.font = UIFont.systemFont(ofSize: 20)
        statusLabal.text = "Please choose a switch"
        statusLabal.layer.cornerRadius = 30
        statusLabal.clipsToBounds = true

        statusLabal.backgroundColor = .lightGray
        greenSwitch.onTintColor = .systemGreen
        yellowSwitch.onTintColor = .systemYellow

        [greenSwitch, yellowSwitch].forEach {
            $0.addTarget(self, action: #selector(setColorValue(_:)), for: .touchUpInside)
        }
    }

    @objc func setColorValue(_ sender: UISwitch) {
        var currentValue = ""

        if greenSwitch.isOn {
            currentValue += "Green"
        }
        
        if greenSwitch.isOn && yellowSwitch.isOn {
            currentValue += " and "
        }
        
        if yellowSwitch.isOn {
            currentValue += "Yellow"
        }
        
        if currentValue.isEmpty {
            currentValue = "Please choose a switch"
        }
    
        statusLabal.text = currentValue
    }
}

```

</details>


<br><br><br>

# View + Controller


- 기존 동작에서 UI부분만 전부 View로 이동
- 비즈니스 로직은 ViewController내부에 존재


### 어려웠던 점

View로부터 완벽하게 비즈니스 로직을 분리하기 어려웠다.  

예를 들어,  

View로부터 Toggle의 값을 가져오는데, 해당 각각의 값이 Green이나 Yellow를 결국 가져오는 로직이 필요했다.  

그런데 사실상 greenSwitch나 yellowSwitch의 값을 체크해서 String으로 변환하는 작업 자체는 UI와 관련된 작업이 아니기때문에 어려웠다.  


그래서 View에서 ViewController로 Delegate를 보낼때,  

```swift
// MARK: 유저 Input Delegation : View -> Controller
@objc private func setColorValue(_ sender: UISwitch) {
    let isGreen = sender == greenSwitch
    delegate?.didChangeSwitch(self, isOn: sender.isOn, isGreen: isGreen)
}

```

## 전체코드


<details><summary>예시 코드</summary>

```swift

import UIKit
// MARK: - VIEW

// MARK: 유저 Input Delegation : View -> Controller
protocol SelectColorViewDelegate: AnyObject {
    func didChangeSwitch(_ selectColorView: SelectColorView, isOn: Bool, isGreen: Bool)
}

class SelectColorView: UIView {

    private lazy var statusLabal: UILabel = {
       let label = UILabel()
        label.translatesAutoresizingMaskIntoConstraints = false
        label.textAlignment = .center
        label.font = UIFont.systemFont(ofSize: 20)
        label.text = "Please choose a switch"
        label.layer.cornerRadius = 30
        label.clipsToBounds = true
        label.backgroundColor = .lightGray

        return label
    }()
    
    private lazy var greenSwitch: UISwitch = makeSwitch(onTintColor: .systemGreen)
    private lazy var yellowSwitch: UISwitch = makeSwitch(onTintColor: .systemYellow)
    

    // MARK: 유저 Input Delegation : View -> Controller
    weak var delegate: SelectColorViewDelegate?
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        setupUI()
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    
    private func setupUI() {
        [statusLabal, greenSwitch, yellowSwitch].forEach {
            addSubview($0)
        }
        
        NSLayoutConstraint.activate([
            statusLabal.centerXAnchor.constraint(equalTo: safeAreaLayoutGuide.centerXAnchor),
            statusLabal.topAnchor.constraint(equalTo: safeAreaLayoutGuide.topAnchor, constant: 100),
            statusLabal.widthAnchor.constraint(equalToConstant: 300),
            statusLabal.heightAnchor.constraint(equalToConstant: 300),
            
            greenSwitch.topAnchor.constraint(equalTo: statusLabal.bottomAnchor, constant: 50),
            greenSwitch.centerXAnchor.constraint(equalTo: statusLabal.centerXAnchor),
            
            yellowSwitch.topAnchor.constraint(equalTo: greenSwitch.bottomAnchor, constant: 50),
            yellowSwitch.centerXAnchor.constraint(equalTo: greenSwitch.centerXAnchor),
        ])

    }
    
    private func makeSwitch(onTintColor: UIColor) -> UISwitch {
        let switchView = UISwitch()
        switchView.translatesAutoresizingMaskIntoConstraints = false
        switchView.onTintColor = onTintColor
        switchView.addTarget(self, action: #selector(setColorValue(_:)), for: .touchUpInside)
        return switchView
    }

}

extension SelectColorView {
    
    // MARK: 유저 Input Delegation : View -> Controller
    @objc private func setColorValue(_ sender: UISwitch) {
        let isGreen = sender == greenSwitch
        delegate?.didChangeSwitch(self, isOn: sender.isOn, isGreen: isGreen)
    }
    
    // MARK: View에 접근하여 update할 수 있도록 메서드 구현
    func setResultText(_ result: String) {
        statusLabal.text = result
    }
}

import UIKit

// MARK: - CONTROLLER

class ViewController: UIViewController {

    let selectColorView = SelectColorView()
    
    private var currentValueArray: [String] = []
    
    override func viewDidLoad() {
        super.viewDidLoad()

        selectColorView.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(selectColorView)
        
        NSLayoutConstraint.activate([
            selectColorView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
            selectColorView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor),
            selectColorView.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor),
            selectColorView.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor) 
        ])
        
        // MARK: 유저 Input Delegation : View -> Controller
        selectColorView.delegate = self
    }
}


extension ViewController : SelectColorViewDelegate {
    
    // MARK: 유저 Input Delegation : View -> Controller
    func didChangeSwitch(_ selectColorView: SelectColorView, isOn: Bool, isGreen: Bool) {
        let colorText = isGreen ? "Green" : "Yellow"
        if isOn {
            currentValueArray.append(colorText)
        } else {
            if let index = currentValueArray.firstIndex(where: { $0 == colorText }) {
                currentValueArray.remove(at: index)
            }
        }

        let newText = getAndValue(currentValueArray)
        
        // MARK: 유저 Input : View -> Controller
        selectColorView.setResultText(newText)
    }
    
    func getAndValue(_ arr: [String]) -> String {

        if arr.count == 1 {
            return arr[0]
        } else {
            let separator = " and "
            let joinedText = arr.joined(separator: separator)
            return joinedText
        }
    }
    
}


```


</details>


## History
- 230821: 예제 생성
