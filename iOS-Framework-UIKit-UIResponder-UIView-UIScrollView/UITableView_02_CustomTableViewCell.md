# UITableView - 커스텀 UITableViewCell

간단한 구조가 아니라 복잡한 구조를 반복해서 사용해주는 경우가 있다.  
이런 경우에는 따로 UITableViewCell 을 커스텀하여 생성해줄 수 있다.  

필요한 객체들을 커스텀셀 내부에 추가하여 만들 수 있는 것이다.  

## 커스텀 셀 구현

이번엔 명함 UI를 만들었다.  

여기서 특별한 점은 커스텀테이블뷰셀에서 직접 선언이 아닌 외부에서 값을 세팅하는 메서드를 구현했다는 것이다.  
tableView는 처리에 있어 다른 객체에 위임했기 때문에,  해당 객체에서 이 부분을 호출에 직접 값을 넣어주어야한다.  

```swift
func configure(name: String, title: String, contact: String) {
    nameLabel.text = name
    titleLabel.text = title
    contactLabel.text = contact
}
```

<br><br>

```swift
class BusinessCardTableViewCell: UITableViewCell {
    
    let nameLabel: UILabel = {
        let label = UILabel()
        label.translatesAutoresizingMaskIntoConstraints = false
        label.font = UIFont.boldSystemFont(ofSize: 20)
        label.textColor = .black
        return label
    }()
    
    let titleLabel: UILabel = {
        let label = UILabel()
        label.translatesAutoresizingMaskIntoConstraints = false
        label.font = UIFont.systemFont(ofSize: 16)
        label.textColor = .black
        return label
    }()
    
    let contactLabel: UILabel = {
        let label = UILabel()
        label.translatesAutoresizingMaskIntoConstraints = false
        label.font = UIFont.systemFont(ofSize: 14)
        label.textColor = .black
        return label
    }()
    
    let logoImageView: UIImageView = {
        let imageView = UIImageView()
        imageView.translatesAutoresizingMaskIntoConstraints = false
        imageView.image = UIImage(systemName: "person.fill")
        return imageView
    }()
    
    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        contentView.addSubview(nameLabel)
        contentView.addSubview(titleLabel)
        contentView.addSubview(contactLabel)
        contentView.addSubview(logoImageView)
        applyConstraints()
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    private func applyConstraints() {
        NSLayoutConstraint.activate([
            nameLabel.topAnchor.constraint(equalTo: contentView.topAnchor, constant: 20),
            nameLabel.leadingAnchor.constraint(equalTo: contentView.leadingAnchor, constant: 20),
            
            titleLabel.topAnchor.constraint(equalTo: nameLabel.bottomAnchor, constant: 30),
            titleLabel.leadingAnchor.constraint(equalTo: nameLabel.leadingAnchor),
            
            contactLabel.topAnchor.constraint(equalTo: titleLabel.bottomAnchor, constant: 10),
            contactLabel.leadingAnchor.constraint(equalTo: nameLabel.leadingAnchor),
            
            logoImageView.topAnchor.constraint(equalTo: contentView.topAnchor, constant: 10),
            logoImageView.trailingAnchor.constraint(equalTo: contentView.trailingAnchor, constant: -20),
            logoImageView.widthAnchor.constraint(equalToConstant: 50),
            logoImageView.heightAnchor.constraint(equalToConstant: 50),
        ])
    }
    
    func configure(name: String, title: String, contact: String) {
        nameLabel.text = name
        titleLabel.text = title
        contactLabel.text = contact
    }
}

```

<br><br>

## 커스텀 UITableViewCell로 타입캐스팅

사용하는데 있어서는 일반적인 셀 재사용 방법과 동일하지만,  dequeue처리할 때 타입캐스팅이 추가된다. 

기존에 사용하던 `dequeueReusableCell(withIdentifier:for:)` 메서드는 UITableViewCell를 리턴하기 때문에 
커스텀셀 내부에 선언한 객체들을 가져오려면 새로 구현한 커스텀 테이블뷰 셀 객체로 타입캐스팅 해주어야한다.  

```swift
func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    // 안전하게 캐스팅
    guard let cell = tableView.dequeueReusableCell(withIdentifier: "BusinessCardTableViewCell", for: indexPath) as? BusinessCardTableViewCell else {
        fatalError("Unable to dequeue CustomTableViewCell")
    }
    
    //혹은
    // let cell = tableView.dequeueReusableCell(withIdentifier: "BusinessCardTableViewCell", for: indexPath) as! BusinessCardTableViewCell 
    
    // 데이터바인딩
    cell.configure(name: "John Doe", 
                   title: "Software Engineer", 
                   contact: "john.doe@example.com")
    
    return cell
}
```


<br><br>

### 작업화면
<img width="356" alt="스크린샷 2023-01-28 오후 3 13 58" src="https://github.com/isGeekCode/TIL/assets/76529148/b8803c37-051a-4566-8d95-37b94cf36329">

<br><br>

### 전체코드
```swift
import UIKit

class ViewController: UIViewController {
    
    let tableView: UITableView = UITableView()
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        view.addSubview(tableView)
        tableView.frame = view.bounds
        
        tableView.delegate = self
        tableView.dataSource = self
        
        tableView.register(BusinessCardTableViewCell.self, forCellReuseIdentifier: "BusinessCardTableViewCell")
    }
}

extension ViewController: UITableViewDelegate, UITableViewDataSource {
    
    /// 테이블뷰 섹션 내부의 Row의 갯수를 선언하는 부분
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return 10
    }
    
    /// 테이블뷰의 cell이 어떻게 보여질지 선언하는 부분
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        guard let cell = tableView.dequeueReusableCell(withIdentifier: "BusinessCardTableViewCell", for: indexPath) as? BusinessCardTableViewCell else {
            fatalError("Unable to dequeue CustomTableViewCell")
        }
        
        cell.configure(name: "John Doe", 
                       title: "Software Engineer", 
                       contact: "john.doe@example.com")
        
        return cell
    }
    
    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
         return 200
    }
}


import UIKit

class BusinessCardTableViewCell: UITableViewCell {
    
    let nameLabel: UILabel = {
        let label = UILabel()
        label.translatesAutoresizingMaskIntoConstraints = false
        label.font = UIFont.boldSystemFont(ofSize: 20)
        label.textColor = .black
        return label
    }()
    
    let titleLabel: UILabel = {
        let label = UILabel()
        label.translatesAutoresizingMaskIntoConstraints = false
        label.font = UIFont.systemFont(ofSize: 16)
        label.textColor = .black
        return label
    }()
    
    let contactLabel: UILabel = {
        let label = UILabel()
        label.translatesAutoresizingMaskIntoConstraints = false
        label.font = UIFont.systemFont(ofSize: 14)
        label.textColor = .black
        return label
    }()
    
    let logoImageView: UIImageView = {
        let imageView = UIImageView()
        imageView.translatesAutoresizingMaskIntoConstraints = false
        imageView.image = UIImage(systemName: "person.fill")
        return imageView
    }()
    
    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        contentView.addSubview(nameLabel)
        contentView.addSubview(titleLabel)
        contentView.addSubview(contactLabel)
        contentView.addSubview(logoImageView)
        applyConstraints()
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    private func applyConstraints() {
        NSLayoutConstraint.activate([
            nameLabel.topAnchor.constraint(equalTo: contentView.topAnchor, constant: 20),
            nameLabel.leadingAnchor.constraint(equalTo: contentView.leadingAnchor, constant: 20),
            
            titleLabel.topAnchor.constraint(equalTo: nameLabel.bottomAnchor, constant: 30),
            titleLabel.leadingAnchor.constraint(equalTo: nameLabel.leadingAnchor),
            
            contactLabel.topAnchor.constraint(equalTo: titleLabel.bottomAnchor, constant: 10),
            contactLabel.leadingAnchor.constraint(equalTo: nameLabel.leadingAnchor),
            
            logoImageView.topAnchor.constraint(equalTo: contentView.topAnchor, constant: 10),
            logoImageView.trailingAnchor.constraint(equalTo: contentView.trailingAnchor, constant: -20),
            logoImageView.widthAnchor.constraint(equalToConstant: 50),
            logoImageView.heightAnchor.constraint(equalToConstant: 50),
        ])
    }
    
    // 데이터바인딩
    func configure(name: String, title: String, contact: String) {
        nameLabel.text = name
        titleLabel.text = title
        contactLabel.text = contact
    }
}

```
