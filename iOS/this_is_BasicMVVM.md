# 간단한 MVC구조 예제

원문 [https://www.kodeco.com/34-design-patterns-by-tutorials-mvvm](https://www.kodeco.com/34-design-patterns-by-tutorials-mvvm)

[https://lsh424.tistory.com/68](https://lsh424.tistory.com/68)

깃: https://github.com/lsh424/MVVM_iOS

MVC정리 [https://lsh424.tistory.com/44](https://lsh424.tistory.com/44)

!![img1 daumcdn-8](https://user-images.githubusercontent.com/76529148/203563725-d61b46bb-c471-41c2-b45d-01233ebdc1c9.png)

```swift
├── AppDelegate
│   ├── AppDelegate.swift
│   └── SceneDelegate.swift
│
├── Controllers
│   ├── ViewController.swift
│   └── ViewController2.swift
│
├── Models
│   └── Dog.swift 
│
├── ViewModels
│   └── DogViewModel.swift
│
└── Views
    └── DogView.swift
```





## 실제로 화면에 나올 내용

- 강아지 이미지
- 품종
- 나이
- 분양가

이게 서버로부터 내려온다면 아래와 같은 정보가 내려올 것이다.

```swift
name: String
birthday: Date
breed: enum // 여러 품종 표현을 위해 enum 사용
imageURL: String /// 로컬이미지라면 imageName
```

## Model

```swift
// Dog.swift

class Dog {

    // 품종
    enum Breed {
        case maltese
        case pomeranian
        case pug
        case poodle
    }

    let name: String
    let birthday: Date   //나이를 위해 현재날짜 - 출생일 
    let breed: Breed
    let imageName: String
    
    // 초기값
    init(name: String = "pomeranian", birthday: Date = Date(timeIntervalSinceNow: (-2 * 86500 * 380)), breed: Breed = .pomeranian, imageName: String = "pomeranian.jpeg") {
        self.name = name
        self.birthday = birthday
        self.breed = breed
        self.imageName = imageName
    }
}

```

name과 imageName은 바로 사용하지만, 나이는 Dog Model에서 받아온 birthday 데이터를 가지고 ViewModel에서 가공한다. 분양가 또한 Dog Model의 품종을 가지고 ViewModel을 통해 가공해준다. 

## ViewModel 생성

```swift
class DogViewModel {
    let dog: Dog
    let calendar: Calendar
    
    init(){
        self.dog = Dog()
        self.calendar = Calendar(identifier: .gregorian)
    }
    
    var name: String {
        return dog.name
    }
    
    var imageName: String {
        return dog.imageName
    }
    
    var ageText: String {
        let today = calendar.startOfDay(for: Date())
        let birthday = calendar.startOfDay(for: dog.birthday)
        let components = calendar.dateComponents([.year], from: birthday, to: today)
        let age = components.year == nil ? 0 : components.year!
        return "\(age) years old"
    }
    
    var adoptionFeeText: String {
        switch dog.breed {
            case .maltese:
                return "₩200000"
            case .pomeranian:
                return "₩500000"
            case .poodle:
                return "₩600000"
            case .pug:
                return "₩400000"
        }
    }
}
```

## View 생성하기

데이터를 표시할 View를 생성한다. 

프로퍼티 옵저버에 들어갈 변수는 아래있어도 포착할 수 있다.

```swift
class DogView: UIView {
    
    // CodeUI
    var imageName: String  = "" {
        willSet {
            imageView.image = UIImage(named: newValue)
        }
    }
    
    let imageView: UIImageView = {
        let imageView = UIImageView()
        imageView.translatesAutoresizingMaskIntoConstraints = false
        return imageView
    }()
    
    let nameLabel: UILabel = {
        let label = UILabel()
        label.textAlignment = .left
        label.font = UIFont(name: "AvenirNextCondensed-MediumItalic", size: 20)!
        label.textColor = .white
        label.translatesAutoresizingMaskIntoConstraints = false
        return label
    }()
    
    let ageLabel: UILabel = {
        let label = UILabel()
        label.textAlignment = .left
        label.font = UIFont(name: "AvenirNextCondensed-MediumItalic", size: 20)!
        label.textColor = .white
        label.translatesAutoresizingMaskIntoConstraints = false
        return label
    }()
    
    let adoptionFeeLabel: UILabel = {
        let label = UILabel()
        label.textAlignment = .left
        label.font = UIFont(name: "AvenirNextCondensed-MediumItalic", size: 20)!
        label.textColor = .white
        label.translatesAutoresizingMaskIntoConstraints = false
        return label
    }()
    
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        
        backgroundColor = UIColor(red: 28/255, green: 28/255, blue: 30/255, alpha: 1)
        
        addSubview(imageView)
        addSubview(nameLabel)
        addSubview(ageLabel)
        addSubview(adoptionFeeLabel)

        
        // Layout
        imageView.topAnchor.constraint(equalTo: self.topAnchor, constant: 50).isActive = true
        imageView.centerXAnchor.constraint(equalTo: self.centerXAnchor).isActive = true
        imageView.widthAnchor.constraint(equalTo: self.widthAnchor, multiplier: 0.804).isActive = true
        imageView.heightAnchor.constraint(equalTo: self.heightAnchor, multiplier: 0.804).isActive = true
        
        nameLabel.topAnchor.constraint(equalTo: imageView.bottomAnchor, constant: 30).isActive = true
        nameLabel.leadingAnchor.constraint(equalTo: imageView.leadingAnchor, constant: 10).isActive = true
        
        ageLabel.topAnchor.constraint(equalTo: nameLabel.bottomAnchor, constant: 20).isActive = true
        ageLabel.leadingAnchor.constraint(equalTo: ageLabel.leadingAnchor, constant: 0).isActive = true
        
        adoptionFeeLabel.topAnchor.constraint(equalTo: ageLabel.bottomAnchor, constant: 20).isActive = true
        adoptionFeeLabel.leadingAnchor.constraint(equalTo: nameLabel.leadingAnchor, constant: 0).isActive = true
    }
    
    required init?(coder: NSCoder) {
        fatalError("init?(coder:) is not supported")
    }
}
```

## ViewController생성하기

```swift
class ViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // View
        let dogView = DogView()
        
        let viewModel = DogViewModel()
        viewModel.configure(dogView)
        
        self.view.addSubview(dogView)
        
        // layout
        dogView.translatesAutoresizingMaskIntoConstraints = false
        dogView.topAnchor.constraint(equalTo: self.view.topAnchor, constant: 135).isActive = true
        dogView.centerXAnchor.constraint(equalTo: self.view.centerXAnchor).isActive = true
        dogView.widthAnchor.constraint(equalTo: self.view.widthAnchor, multiplier: 0.9).isActive = true
        dogView.bottomAnchor.constraint(equalTo: self.view.bottomAnchor, constant: -100).isActive = true
    }
}
```

ViewModel과 ViewController연결하기

```swift
extension DogViewModel {
    func configure(_ view: DogView) {
        view.nameLabel.text = name
        view.imageName = imageName
        view.ageLabel.text = ageText
        view.adoptionFeeLabel.text = adoptionFeeText
    }
}
```
간단한 구조를 만들어봤다.

그리고 이걸 응용해서 한가지 구조를 더 만들어보자.
바로 만들어서 그리 부드러운 예제가 아니다.


```swift
// MARK: - Model
class Company {
    
    // 직군
    enum Job {
        case developer
        case designner
        case planner
        case marketer
    }
    
    let name: String
    let dateOfJoinging: Date
    let job: Job
    let imageName: String
    
    init(name: String = "pomeranian", dateOfJoinging: Date = Date(timeIntervalSinceNow: (-2 * 86500 * 380)), job: Job = .developer, imageName: String = "pomeranian.jpeg") {
        self.name = name
        self.dateOfJoinging = dateOfJoinging
        self.job = job
        self.imageName = imageName
    }
}
```

```swift
// MARK: - View
class PersonView: UIView {
    
    // 뷰를 스토리보드로 만들지 않고 코드로 작성시 사용
    var imageName: String = "" {
        willSet {
            imageView.image = UIImage(named: newValue)
        }
    }
    
    let imageView: UIImageView = {
        let imageView = UIImageView()
        imageView.translatesAutoresizingMaskIntoConstraints = false
        return imageView
    }()
    
    let nameLabel: UILabel = {
        let nameLabel = UILabel()
        nameLabel.textAlignment = .left
        nameLabel.font = UIFont(name: "AvenirNextCondensed-MediumItalic",size: 20)!
        nameLabel.textColor = .white
        nameLabel.translatesAutoresizingMaskIntoConstraints = false
        return nameLabel
    }()
    
    let ageLabel: UILabel = {
        let ageLabel = UILabel()
        ageLabel.textAlignment = .left
        ageLabel.font = UIFont(name: "AvenirNextCondensed-MediumItalic",size: 20)!
        ageLabel.textColor = .white
        ageLabel.translatesAutoresizingMaskIntoConstraints = false
        return ageLabel
    }()
    
    let adoptionFeeLabel: UILabel = {
        let adoptionFeeLabel = UILabel()
        adoptionFeeLabel.textAlignment = .left
        adoptionFeeLabel.font = UIFont(name: "AvenirNextCondensed-MediumItalic",size: 20)!
        adoptionFeeLabel.textColor = .white
        adoptionFeeLabel.translatesAutoresizingMaskIntoConstraints = false
        return adoptionFeeLabel
    }()
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        
        backgroundColor = UIColor(red: 28/255, green: 28/255, blue: 30/255, alpha: 1)
        
        addSubview(imageView)
        addSubview(nameLabel)
        addSubview(ageLabel)
        addSubview(adoptionFeeLabel)
        
        
        // layout
        imageView.topAnchor.constraint(equalTo: self.topAnchor, constant: 50).isActive = true
        imageView.centerXAnchor.constraint(equalTo: self.centerXAnchor).isActive = true
        imageView.widthAnchor.constraint(equalTo: self.widthAnchor, multiplier: 0.804).isActive = true
        imageView.heightAnchor.constraint(equalTo: self.widthAnchor, multiplier: 0.804).isActive = true
        
        nameLabel.topAnchor.constraint(equalTo: imageView.bottomAnchor, constant: 30).isActive = true
        nameLabel.leadingAnchor.constraint(equalTo: imageView.leadingAnchor, constant: 10).isActive = true
        
        ageLabel.topAnchor.constraint(equalTo: nameLabel.bottomAnchor, constant: 20).isActive = true
        ageLabel.leadingAnchor.constraint(equalTo: nameLabel.leadingAnchor, constant: 0).isActive = true
        
        adoptionFeeLabel.topAnchor.constraint(equalTo: ageLabel.bottomAnchor, constant: 20).isActive = true
        adoptionFeeLabel.leadingAnchor.constraint(equalTo: ageLabel.leadingAnchor, constant: 0).isActive = true
    }
    
    required init?(coder: NSCoder) {
        fatalError("init?(coder:) is not supported")
    }
}
```

```swift
// MARK: - ViewModel
class PersonViewModel {
    let person: Company
    let calendar: Calendar
    
    init(){
        self.person = Company()
        self.calendar = Calendar(identifier: .gregorian)
    }
    
    var name: String {
        return person.name
    }
    
    var imageName: String {
        return person.imageName
    }
    
    var ageText: String {
        let today = calendar.startOfDay(for: Date())
        let dateOfJoinging = calendar.startOfDay(for: person.dateOfJoinging)
        let components = calendar.dateComponents([.year], from: dateOfJoinging, to: today)
        let age = components.year == nil ? 0 : components.year!
        return "\(age) 연차"
    }
    
    var greetingMSG: String {
        switch person.job {
        case .developer:
                return "Hello World"
        case .designner:
                return "그림이 좋아요"
        case .marketer:
                return "광고할분 오세요"
        case .planner:
                return "기획을 해드립니다"
        }
    }
}

extension PersonViewModel {
    func configure(_ view: PersonView) {
        view.nameLabel.text = name
        view.imageName = imageName
        view.ageLabel.text = ageText
        view.adoptionFeeLabel.text = greetingMSG
    }
}
```

```swift
class ViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // View
        let personView = PersonView()
        
        let viewModel = PersonViewModel()
        viewModel.configure(personView)
        
        self.view.addSubview(personView)
        
        // layout
        personView.translatesAutoresizingMaskIntoConstraints = false
        personView.topAnchor.constraint(equalTo: self.view.topAnchor, constant: 135).isActive = true
        personView.centerXAnchor.constraint(equalTo: self.view.centerXAnchor).isActive = true
        personView.widthAnchor.constraint(equalTo: self.view.widthAnchor, multiplier: 0.9).isActive = true
        personView.bottomAnchor.constraint(equalTo: self.view.bottomAnchor, constant: -100).isActive = true
    }
}
```
