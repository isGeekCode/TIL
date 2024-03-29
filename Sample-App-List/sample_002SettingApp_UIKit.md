# Sample App : 설정앱 - UIKit(Code)

<br>

설정앱의 기능은 아래와 같다.

- 최소기능
    - 그려질 화면
    - 섹션 분리
    - 셀타입분기처리
    - 검색기능
    
- 추가기능
    - 디테일화면 이동
    - MVC

<br><br>

## Contents

1. [테이블뷰 세팅](#테이블뷰-세팅)
   - [세팅화면](#세팅화면)
2. [데이터 모델 생성](#데이터-모델-생성)
   - [반영](#반영)
   - [적용화면_1](#적용화면_1)
3. [Section별 그룹화](#section별-그룹화)
   - [적용화면_2](#적용화면_2)
4. [셀 클릭 이벤트](#셀-클릭-이벤트)
   - [셀렉션 스타일](#셀렉션-스타일)
   - [didSelect 구현](#didselect-구현)
5. [첫번째 섹션을 Profile 전용 섹션으로 만들기](#첫번째-섹션을-profile-전용-섹션으로-만들기)
   - [적용화면_3](#적용화면_3)
6. [커스텀셀 적용하기](#커스텀셀-적용하기)
   - [적용화면_4](#적용화면_4)
7. [enum으로 셀 분기처리](#enum으로-셀-분기처리)
8. [NavigationTitle 세팅하기](#navigationtitle-세팅하기)
   - [기존 SettingVC만 직접 호출](#기존-settingvc만-직접-호출)
   - [NavigationVC에 넣어 부르기](#navigationvc에-넣어-부르기)
9. [SearchBar로 검색기능 추가하기](#searchbar로-검색기능-추가하기)
   - [적용화면_5](#적용화면_5)
   - [전체코드_1](#전체코드_1)
10. [MVC로 리팩토링](#mvc로-리팩토링)
    - [전체코드_2](#전체코드_2)
11. [셀을 클릭하면 디테일 화면으로 이동처리하기](#셀을-클릭하면-디테일-화면으로-이동처리하기)
    - [적용화면_6](#적용화면_6)





<br><br>

## 테이블뷰 세팅

<br><br>

```swift
class SettingViewController: UIViewController {
    
    lazy var tableView: UITableView = {
        let tableView = UITableView()
        tableView.translatesAutoresizingMaskIntoConstraints = false
        tableView.dataSource = self
        tableView.delegate = self
        tableView.register(UITableViewCell.self, forCellReuseIdentifier: "Cell")
        return tableView
    }()

    let data = Array(0...10).map{ "\($0)"}

    override func viewDidLoad() {
        super.viewDidLoad()

        view.addSubview(tableView)
        
        NSLayoutConstraint.activate([
            tableView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
            tableView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor),
            tableView.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor),
            tableView.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor),
        ])

    }
}


extension SettingViewController: UITableViewDataSource, UITableViewDelegate {
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return data.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {

        let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath)
        cell.textLabel?.text = data[indexPath.row]
        return cell
    }
}
```

<br><br>

[[Top]](#contents)

<br><br><br>

### 세팅화면

<img width="300" alt="스크린샷 2023-11-23 오전 9 56 24" src="https://github.com/isGeekCode/github-action-til-autoformat-readme/assets/76529148/beb4290d-85a5-4953-ad40-a993b3d5e78c">

<br><br>

[[Top]](#contents)

<br><br><br>


## 데이터 모델 생성

```swift
struct SettingModel {
    let imageName: String
    let titleString: String
    let iconBackgroundColor: UIColor

    static let sampleModels = [
        
            SettingModel(imageName: "hourglass",
                         titleString: "스크린타임",
                         iconBackgroundColor: .systemIndigo),

            SettingModel(imageName: "airplane",
                         titleString: "에어플레인 모드",
                         iconBackgroundColor: .systemOrange),

            SettingModel(imageName: "wifi",
                         titleString: "Wi-Fi",
                         iconBackgroundColor: .systemBlue),
            
            SettingModel(imageName: "antenna.radiowaves.left.and.right",
                         titleString: "셀룰러",
                         iconBackgroundColor: .systemGreen),
            
            SettingModel(imageName: "personalhotspot",
                         titleString: "개인용 핫스팟",
                         iconBackgroundColor: .systemGreen),

        
            SettingModel(imageName: "gear",
                         titleString: "일반",
                         iconBackgroundColor: .lightGray),
            
            SettingModel(imageName: "accessibility",
                         titleString: "손쉬운 사용",
                         iconBackgroundColor: .systemBlue),
            
            SettingModel(imageName: "hand.raised.fill",
                         titleString: "개인정보 보호 및 보안",
                         iconBackgroundColor: .systemBlue),
        
            SettingModel(imageName: "key.fill",
                         titleString: "암호",
                         iconBackgroundColor: .lightGray),
    
        
            SettingModel(imageName: "hammer.fill",
                         titleString: "개발자",
                         iconBackgroundColor: .lightGray),
    ]
}


```


<br><br>

[[Top]](#contents)

<br><br><br>

### 반영

<br><br>

```swift
class SettingViewController: UIViewController {

//    let data = Array(0...10).map{ "\($0)"}
    let settingModels = SettingModel.sampleModels

}

extension SettingViewController: UITableViewDataSource, UITableViewDelegate {

    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
//          return data.count
        return settingModels.count
    }



    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath)
//        cell.textLabel?.text = data[indexPath.row]
        cell.textLabel?.text = settingModels[indexPath.row].titleString
        cell.imageView?.image = UIImage(systemName: model[indexPath.row].imageName)

}
```

<br><br>

[[Top]](#contents)

<br><br><br>


### 적용화면_1

<img width="300" alt="스크린샷 2023-11-23 오전 10 08 06" src="https://github.com/isGeekCode/github-action-til-autoformat-readme/assets/76529148/ca5906b9-cd60-43b0-9efa-541416bb8c3a">

<br><br>

[[Top]](#contents)

<br><br><br>


## Section별 그룹화

기존의 데이터를 Section별로 보여줄 수 있도록 SettingModel을 추상화 해준다.  

<br><br>

```swift


// 기존 모델
struct SettingModel {
    let imageName: String
    let titleString: String
    let iconBackgroundColor: UIColor
}

// 추가한 모델
struct SettingSection {
    let settings: [SettingModel]
}

extension SettingSection {
    
    static let sampleSections = [
        
        // 첫번째 섹션
        SettingSection(settings: [
            SettingModel(imageName: "hourglass",
                         titleString: "스크린타임",
                         iconBackgroundColor: .systemIndigo),
        ]),

        // 두번째 섹션
        SettingSection(settings: [
            SettingModel(imageName: "airplane",
                         titleString: "에어플레인 모드",
                         iconBackgroundColor: .systemOrange),

            SettingModel(imageName: "wifi",
                         titleString: "Wi-Fi",
                         iconBackgroundColor: .systemBlue),
            
            SettingModel(imageName: "antenna.radiowaves.left.and.right",
                         titleString: "셀룰러",
                         iconBackgroundColor: .systemGreen),
            
            SettingModel(imageName: "personalhotspot",
                         titleString: "개인용 핫스팟",
                         iconBackgroundColor: .systemGreen),
        ]),

        // 세번째 섹션
        SettingSection(settings: [
            SettingModel(imageName: "gear",
                         titleString: "일반",
                         iconBackgroundColor: .lightGray),
            
            SettingModel(imageName: "accessibility",
                         titleString: "손쉬운 사용",
                         iconBackgroundColor: .systemBlue),
            
            SettingModel(imageName: "hand.raised.fill",
                         titleString: "개인정보 보호 및 보안",
                         iconBackgroundColor: .systemBlue),
            
        ]),
        
        // 네번째 섹션
        SettingSection(settings: [
            SettingModel(imageName: "key.fill",
                         titleString: "암호",
                         iconBackgroundColor: .lightGray),
            
        ]),
        
        // 다섯번째 섹션
        SettingSection(settings: [
            SettingModel(imageName: "hammer.fill",
                         titleString: "개발자",
                         iconBackgroundColor: .lightGray),
        ])
    ]
}

```

<br><br>

초기화시 아래와 같이 style을 설정하면 그룹화된 UI를 구현할 수 있다.   

<br><br>

```swift

lazy var tableView: UITableView = {
    let tableView = UITableView(frame: .zero, style: .insetGrouped)
    tableView.translatesAutoresizingMaskIntoConstraints = false
    tableView.dataSource = self
    tableView.delegate = self
    tableView.register(UITableViewCell.self, forCellReuseIdentifier: "Cell")
    return tableView
}()

```

<br><br>

데이터도 변경해준다.  

<br><br>

```swift
//    let settingModels = SettingModel.sampleModels
    let settingSections = SettingSection.sampleSections
```

<br><br>

데이터 바인딩도 변경한다.  

<br><br>

```swift
extension SettingViewController: UITableViewDataSource, UITableViewDelegate {
    
    // 섹션의 갯수 지정
    func numberOfSections(in tableView: UITableView) -> Int {
        return settingSections.count
    }
    
    // 섹션 내부의 row의 갯수 지정
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // return settingModels.count
          return settingSections[section].settings.count
    }
    
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {

    let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath)
    // 데이터 구조에 따라 달라질 수 있음
//    let setting = settingModels[indexPath.row]
    let setting = settingSections[indexPath.section].settings[indexPath.row]
    
    cell.imageView?.image = UIImage(systemName: setting.imageName)
    cell.textLabel?.text = setting.titleString

    return cell
}

    
```

<br><br>

[[Top]](#contents)

<br><br><br>

### 적용화면_2
<img width="300" alt="스크린샷 2023-11-23 오전 10 52 29" src="https://github.com/isGeekCode/github-action-til-autoformat-readme/assets/76529148/24605f26-df11-4bf5-9dde-ebbbf44bb3ef">

<br><br>

## 셀 클릭 이벤트

### 셀렉션 스타일
클릭시  셀의 선택색상을 조절할 수 있다. 

```swift
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {

        let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath)
        
        // 셀렉션 스타일
        cell.selectionStyle = .none
        
        let setting = settingSections[indexPath.section].settings[indexPath.row]
        
        cell.imageView?.image = UIImage(systemName: setting.imageName)
        cell.textLabel?.text = setting.titleString

        return cell
    }

```

<br><br>

[[Top]](#contents)

<br><br><br>

### didSelect 구현

```swift

extension SettingViewController: UITableViewDataSource, UITableViewDelegate {

    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        print("didSelectRowAt: \(indexPath)")
    }
}
```

<br><br>

[[Top]](#contents)

<br><br><br>


## 첫번째 섹션을 Profile 전용 섹션으로 만들기

indexPath의 0번째 섹션은 이제 프로필을 구현해보자.  

프로필로 사용할 데이터를 추가하자.  

다른 일반 셀과 달리 세부정보가 들어갈 텍스트가 필요하기 때문에, SettingModel에 description을 추가해준다.  
그리고 그 정보를 첫번째 섹션으로 찾아 사용할 수 있도록 추가해준다.  

```swift
struct SettingModel {
    let imageName: String
    let titleString: String
    let description: String  // 추가
    let iconBackgroundColor: UIColor
}

extension SettingSection {
    
    static let sampleSections = [
    
        // 첫번째 section
        SettingSection(settings: [
            SettingModel(imageName: "person.crop.circle.fill",
                         titleString: "방현석",
                         description: "Apple ID, iCloud+ 미디어 및 구입 항목",
                         iconBackgroundColor: .clear),
        ]),
        
        // 두번째 section
        SettingSection(settings: [
            SettingModel(imageName: "hourglass",
                         titleString: "스크린타임",
                         description: "", // 사용안할 데이터
                         iconBackgroundColor: .systemIndigo,
            ]),
        ]),
        
        // .... 나머지 데이터들
    ]
}
```

<br><br>

이제 섹션별로 이 더미데이터를 가져와서 세팅하도록 처리한다.  
섹션이 0 인 경우에는 imageView의 tintColor를 다르게 줘보자.

<br><br>

```swift

extension SettingViewController: UITableViewDataSource, UITableViewDelegate {
    
    // 첫번째 섹션의 높이를 분기처리
    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
    
        return indexPath.section == 0 ? 80 : 40
    }

    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {

        let setting = model[indexPath.section].settings[indexPath.row]
        let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath)
        cell.selectionStyle = .none
        
        
        cell.textLabel?.text = setting.titleString
        cell.imageView?.image = UIImage(systemName: setting.imageName)
        
        // 이미지뷰 tintColor 분기처리
        cell.imageView?.tintColor = indexPath.section == 0 ? .lightGray : .white
        cell.imageView?.backgroundColor = setting.iconBackgroundColor
    }
}
```

<br><br>

[[Top]](#contents)

<br><br><br>

### 적용화면_3
<img width="300" alt="스크린샷 2023-11-23 오전 11 13 01" src="https://github.com/isGeekCode/github-action-til-autoformat-readme/assets/76529148/5e7bb888-6da4-40a6-a6d1-21b169a793f3">

<br><br>

[[Top]](#contents)

<br><br><br>

이제 프로필과 구별된 높이 크기, tintColor를 볼 수 있다.  
그러나 imageView의 배경색상을 조절했지만, 이미지뷰가 이상하다는 것을 알 수 있다.  
  
기본 설정앱을 다시 살펴보자.    

<br><br>

<img width="300" alt="스크린샷 2023-11-23 오후 12 55 02" src="https://github.com/isGeekCode/github-action-til-autoformat-readme/assets/76529148/64110210-8ec9-4814-b7fd-9fe37db819f8">

<br><br>

## 커스텀셀 적용하기
설정앱에서는 상단 프로필 섹션과 하단의 구조가 다르다.  

그럼 이제 커스텀 셀을 만들어 보자.  

곧 복잡해질 예정이니 셀의 메서드를 분리하자.  

<br><br>

```swift


class SettingViewController: UIViewController {

    func configureProfileCell(_ cell: UITableViewCell, with setting: SettingModel) {
        // Profile 전용
    }
    
    func configureSettingCell(_ cell: UITableViewCell, with setting: SettingModel) {
        // 일반셀 전용
    }
}

extension SettingViewController: UITableViewDataSource, UITableViewDelegate {

    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {

        let setting = settingSections[indexPath.section].settings[indexPath.row]
        let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath)
        cell.selectionStyle = .none
        
        if indexPath.section == 0 {
            configureProfileCell(cell, with: setting)
        } else {
            configureSettingCell(cell, with: setting)
        }

        return cell
    }
}

```

<br><br>

레이아웃 메서드를 채우자.  

<br><br>

```swift

    func configureProfileCell(_ cell: UITableViewCell, with setting: SettingModel) {
        let imageView = {
            let image = UIImage(systemName: setting.imageName)
            let imageView = UIImageView(image: image)
            imageView.tintColor = .lightGray
            return imageView
        }()
        
        let titleLabel = UILabel()
        titleLabel.text = setting.titleString
        titleLabel.font = UIFont.boldSystemFont(ofSize: 13)

        let detailLabel = UILabel()
        detailLabel.text = setting.description
        detailLabel.font = UIFont.systemFont(ofSize: 13)

        
        [imageView, titleLabel, detailLabel].forEach { 
            cell.contentView.addSubview($0)
            $0.translatesAutoresizingMaskIntoConstraints = false
        }
        
        NSLayoutConstraint.activate([
            imageView.leadingAnchor.constraint(equalTo: cell.contentView.leadingAnchor, constant: 20),
            imageView.centerYAnchor.constraint(equalTo: cell.contentView.layoutMarginsGuide.centerYAnchor),
            imageView.widthAnchor.constraint(equalToConstant: 70),
            imageView.heightAnchor.constraint(equalToConstant: 70),
            
            titleLabel.leadingAnchor.constraint(equalTo: imageView.trailingAnchor, constant: 10),
            titleLabel.centerYAnchor.constraint(equalTo: imageView.centerYAnchor, constant: -10),

            detailLabel.leadingAnchor.constraint(equalTo: imageView.trailingAnchor, constant: 10),
            detailLabel.centerYAnchor.constraint(equalTo: imageView.centerYAnchor, constant: 10),
        ])
    }


    func configureSettingCell(_ cell: UITableViewCell, with setting: SettingModel) {
        
        let containerView = {
            let containerView = UIView()
            containerView.translatesAutoresizingMaskIntoConstraints = false
            containerView.backgroundColor = setting.iconBackgroundColor
            containerView.layer.cornerRadius = 5
            // 이미지와 containerView간의 여백 세팅
            containerView.clipsToBounds = true
            containerView.layoutMargins = UIEdgeInsets(top: 5, left: 5, bottom: 5, right: 5) 

            let image = UIImage(systemName: setting.imageName)

            let imageView = UIImageView(image: image)
            imageView.translatesAutoresizingMaskIntoConstraints = false
            imageView.contentMode = .scaleAspectFit 
            imageView.tintColor = .white

            containerView.addSubview(imageView)

            NSLayoutConstraint.activate([
                imageView.topAnchor.constraint(equalTo: containerView.layoutMarginsGuide.topAnchor),
                imageView.leadingAnchor.constraint(equalTo: containerView.layoutMarginsGuide.leadingAnchor),
                imageView.trailingAnchor.constraint(equalTo: containerView.layoutMarginsGuide.trailingAnchor),
                imageView.bottomAnchor.constraint(equalTo: containerView.layoutMarginsGuide.bottomAnchor)
            ])

            return containerView
        }()
        
        let textLabel = {
           let label = UILabel()
            label.text = setting.titleString
            label.textColor = .black
            label.translatesAutoresizingMaskIntoConstraints = false
            return label
        }()
        
        cell.contentView.addSubview(containerView)
        cell.contentView.addSubview(textLabel)
        
        NSLayoutConstraint.activate([
        
            containerView.leadingAnchor.constraint(equalTo: cell.contentView.leadingAnchor, constant: 20),
            containerView.centerYAnchor.constraint(equalTo: cell.contentView.centerYAnchor),
            containerView.widthAnchor.constraint(equalToConstant: 35), 
            containerView.heightAnchor.constraint(equalToConstant: 35), 
            
            textLabel.leadingAnchor.constraint(equalTo: containerView.trailingAnchor, constant: 10),
            textLabel.centerYAnchor.constraint(equalTo: containerView.centerYAnchor),
            
        ])
        cell.accessoryType = .disclosureIndicator

    }

```

<br><br>

[[Top]](#contents)

<br><br><br>

### 적용화면_4

<img width="300" alt="스크린샷 2023-11-23 오후 1 13 49" src="https://github.com/isGeekCode/github-action-til-autoformat-readme/assets/76529148/326b6d16-a805-4dba-a188-c68afb53346d">

<br><br>

[[Top]](#contents)

<br><br><br>

## enum으로 셀 분기처리

우리가 구현하는 셀의 타입은 두 가지이다. 

항상 첫번째 셀은 프로필셀, 나머지는 일반 세팅목록이 있는 셀들이다.  
현재는 테이블뷰의 indexPath라는 객체가 갖고있는 Section과 Row 정보를 가지고 UI를 구현중이지만,

사실 indexPath의 값을 이용해 사용하는것은 가급적 줄이는 것이 좋다.  기능을 추가하는 등의 유지보수시, indexPath가 꼬이면서 사이드이펙트가 발생할 확률이 높기 때문이다.  

아래와 같이 셀타입을 선언하고 기존의 Model에도 적용한다.  
```swift
enum CellType {
    case profileCell
    case settingCell
}

struct SettingSection {
    let settings: [SettingModel]
}

struct SettingModel {
    let imageName: String
    let titleString: String
    let description: String
    let iconBackgroundColor: UIColor
    let cellType: CellType // 타입추가
}


//데이터에도 적용

extension SettingSection {
    
    static let sampleSections = [
        SettingSection(settings: [
            SettingModel(imageName: "person.crop.circle.fill",
                         titleString: "방현석",
                         description: "Apple ID, iCloud+ 미디어 및 구입 항목",
                         iconBackgroundColor: .clear,
                         cellType: CellType.profileCell),
        ]),
        
        SettingSection(settings: [
            SettingModel(imageName: "hourglass",
                         titleString: "스크린타임",
                         description: "",
                         iconBackgroundColor: .systemIndigo,
                         cellType: CellType.settingCell),
        ]),

        SettingSection(settings: [
            SettingModel(imageName: "airplane",
                         titleString: "에어플레인 모드",
                         description: "",
                         iconBackgroundColor: .systemOrange,
                         cellType: CellType.settingCell),

            SettingModel(imageName: "wifi",
                         titleString: "Wi-Fi",
                         description: "",
                         iconBackgroundColor: .systemBlue,
                         cellType: CellType.settingCell),
            
            SettingModel(imageName: "antenna.radiowaves.left.and.right",
                         titleString: "셀룰러",
                         description: "",
                         iconBackgroundColor: .systemGreen,
                         cellType: CellType.settingCell),
            
            SettingModel(imageName: "personalhotspot",
                         titleString: "개인용 핫스팟",
                         description: "",
                         iconBackgroundColor: .systemGreen,
                         cellType: CellType.settingCell),
        ]),

        
        SettingSection(settings: [
            SettingModel(imageName: "gear",
                         titleString: "일반",
                         description: "",
                         iconBackgroundColor: .lightGray,
                         cellType: CellType.settingCell),
            
            SettingModel(imageName: "accessibility",
                         titleString: "손쉬운 사용",
                         description: "",
                         iconBackgroundColor: .systemBlue,
                         cellType: CellType.settingCell),
            
            SettingModel(imageName: "hand.raised.fill",
                         titleString: "개인정보 보호 및 보안",
                         description: "",
                         iconBackgroundColor: .systemBlue,
                         cellType: CellType.settingCell),
            
        ]),
        
        SettingSection(settings: [
            SettingModel(imageName: "key.fill",
                         titleString: "암호",
                         description: "",
                         iconBackgroundColor: .lightGray,
                         cellType: CellType.settingCell),
            
        ]),
        
        SettingSection(settings: [
            SettingModel(imageName: "hammer.fill",
                         titleString: "개발자",
                         description: "",
                         iconBackgroundColor: .lightGray,
                         cellType: CellType.settingCell),
        ])
    ]
}
```

<br><br>

이제 기존의 indexPath를 이용해 나눴던 분기처리를 type으로 수정해준다.  

<br><br>

```swift

extension SettingViewController: UITableViewDataSource, UITableViewDelegate {

    
    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {

        let setting = settingSections[indexPath.section].settings[indexPath.row]
        return setting.cellType == .profileCell ? 80 : 40
//        return indexPath.section == 0 ? 80 : 40
    }

    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {

        let setting = settingSections[indexPath.section].settings[indexPath.row]
        let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath)
        cell.selectionStyle = .none

//        if indexPath.section == 0 {
        if setting.cellType == .profileCell {
        case .profileCell:
            configureProfileCell(cell, with: setting)
        case .settingCell:
            configureSettingCell(cell, with: setting)
        }

        return cell
    }
```

<br><br>

[[Top]](#contents)

<br><br><br>


## NavigationTitle 세팅하기

상단에 자동으로 세팅되는 타이틀효과는 네비게이션 컨트롤러의 기능이다.  
또 테이블뷰의 셀을 클릭했을 때, 네비게이션컨트롤러의 push이동을 하면 다음 화면에도 네비게이션 바를 세팅하여 일관성 있는 UI를 구성할 수 있다.  


이 기능을 사용하려면 현재 ViewController를 생성할 때, UINavigationController에 현재 ViewController를 넣어서 UINavigationController를 불러주어야한다.  

<br><br>

[[Top]](#contents)

<br><br><br>

### 기존 SettingVC만 직접 호출

기존의 화면을 보여주기 위해선 SettingViewController를 직접 호출하였다.  

스토리보드를 사용했다면, 스토리보드의 SettingViewController에 is initial View Controller 설정되어있어야 했다.  

스토리보드를 아예 없앴다면 코드로 SceneDelegate(iOS13이후)이나 AppDelegate(iOS13이전)에서 rootViewController를 직접 설정했을 것이다.  

<br><br>

```swift

// SceneDelegate를 사용하는 경우 : iOS13 이후

class SceneDelegate: UIResponder, UIWindowSceneDelegate {

    var window: UIWindow?

    func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {

//        최초세팅 : 스토리보드의 설정을 따라가려면 이렇게 처리
//        guard let _ = (scene as? UIWindowScene) else { return }
        guard let windowScene = (scene as? UIWindowScene) else { return }
        window?.rootViewController = SettingViewController()
        window?.makeKeyAndVisible()
}

// AppDelegate만 사용하는 경우 : iOS13 이전

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {

        window?.rootViewController = SettingViewController()
        window?.makeKeyAndVisible() // UIWindow를 키 윈도우로 설정하고 표시

        return true
    }
}
```


<br><br>

[Top](#contents)

<br><br><br>

### NavigationVC에 넣어 부르기

스토리보드에선 Editor - Embed in - Navigation Controller 로 세팅할 수 있따. 

코드로 구현하는 경우 아래처럼 진행한다.  

```
// iOS13이후 SceneDelegate 사용하는 경우

class SceneDelegate: UIResponder, UIWindowSceneDelegate {

    var window: UIWindow?

    func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
        guard let windowScene = (scene as? UIWindowScene) else { return }

        let settingViewController = SettingViewController()
        let navigationController = UINavigationController(rootViewController: settingViewController)

        window = UIWindow(windowScene: windowScene)
        window?.rootViewController = navigationController
        window?.makeKeyAndVisible()
    }
}



// iOS13이전 AppDelegate만 사용하는 경우 

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {

        let settingViewController = SettingViewController()
        let navigationController = UINavigationController(rootViewController: settingViewController)
        window?.rootViewController = navigationController

        // UIWindow를 키 윈도우로 설정하고 표시
        window?.makeKeyAndVisible()

        return true
    }
}

```

<br><br>


이제 네비게이션 컨트롤러가 세팅되었다면 ViewController에서 navigationController에 대한 코드를 삽입힌다.  
타이틀을 설정하기위해 아래 코드를 삽입한다.  
viewController의 title에 접근해도 동일하다.  

최근의 NavigationBar의 라지타이틀을 설정하면, 스크롤에 따라 유동적인 UI를 볼 수 있다.  


```swift

class SettingViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        
        navigationController?.navigationBar.prefersLargeTitles = true
        navigationItem.title = "내가 만든 설정 페이지"
//        title = "내가 만든 설정 페이지"

    }
}
```

<br><br>

<img width="300" alt="ezgif-4-4f8d0e0a88" src="https://github.com/isGeekCode/TIL/assets/76529148/bb06145d-8cbf-4ab0-804a-48b88132babe">



<br><br>

[[Top]](#contents)

<br><br><br>

## SearchBar로 검색기능 추가하기

놀랍게도 navigationController에는 서치바를 제공해준다.  

서치바에서 검색결과에 따라 데이터를 변경하려면 아래와 같이 데이터를 만들어준다.  
```swift

class SettingViewController: UIViewController {


    let settingSections = SettingSection.sampleSections
    // 검색 결과를 저장할 배열
    var filteredSections = [SettingSection]()
}
```

<br><br>

서치바를 사용하는 방법은 아래와 같다.  
navigationItem의 titleView에 서치바를 추가할 수도 있지만. 그렇게 하면 최상단에 서치바가 생긴다.  
우리가 필요한건 라지타이틀 하단에 서치바가 유동적으로 생기는 것이기 때문에 titleView에는 세팅하지않는다.  

<br><br>

```swift
class SettingViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        // 초기화
        let searchController = UISearchController(searchResultsController: nil)
        // 검색 중에 배경을 흐리게 하지 않도록 설정
        searchController.obscuresBackgroundDuringPresentation = false
        searchController.searchBar.placeholder = "검색"
        navigationItem.searchController =  searchController
        // 스크롤시에는 사라지도록 설정
        navigationItem.hidesSearchBarWhenScrolling = true

        // updateSearchResults(for:) 델리게이트를 사용을 위한 델리게이트 할당
        searchController.searchResultsUpdater = self

//        navigationItem.titleView에 검색 바 설정
//        navigationItem.titleView = searchController.searchBar

        // 필요한 경우 추가적인 검색 컨트롤러 설정
        definesPresentationContext = true
    }
}
```

<br><br>


여기에 searchBar의 검색 조건에 따라 동작하도록 하기 위해선 searchController.searchResultsUpdater를 self로 선언하고 UISearchResultsUpdating 프로토콜을 채택해야한다.  

<br><br>

```swift

extension SettingViewController:  UISearchResultsUpdating {


    func updateSearchResults(for searchController: UISearchController) {
        guard let searchText = searchController.searchBar.text, !searchText.isEmpty else {
            filteredSections = settingSections
            tableView.reloadData()
            return
        }
        
        // 검색어에 따른 필터링
        filteredSections = settingSections.map { section in
            // 각 섹션에서 titleString이 검색어를 포함하는 설정들만 필터링
            let filteredSettings = section.settings.filter { setting in
                setting.titleString.lowercased().contains(searchText.lowercased())
            }
            return SettingSection(settings: filteredSettings)
        }
        .filter { !$0.settings.isEmpty } // 빈 섹션은 제거

        tableView.reloadData()
        print("filteredSections::\n\(filteredSections)")
    }
}
```

<br><br>

searchBar의 동작을 모두 구현하려면, 특히 취소버튼을 구현하려면 아래 메서드도 구현해야한다.  
searchBar는 navigationController에 추가했던 searchController에서 접근가능하다.  

<br><br>

```swift
class SettingViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        let searchController = UISearchController(searchResultsController: nil)
        searchController.searchBar.delegate = self
    }
}


extension SettingViewController: UISearchBarDelegate {
    func searchBarCancelButtonClicked(_ searchBar: UISearchBar) {
        
        // 검색 결과 배열을 원래 배열로 리셋
        filteredSections = settingSections
        
        // 테이블 뷰 리로드
        tableView.reloadData()
    }
}
```

<br><br>

그리고 마지막으로 tableView에서도 UI를 만들 때, filteredSampleSections를 기준으로 
UI를 생성하도록 수정해준다.  

초기에도 데이터가 있어야하기 때문에 ViewDidLoad에서 데이터를 초기화 해준다.  



```swift
class SettingViewController: UIViewController {

    let settingSections = SettingSection.sampleSections
    // 검색 결과를 저장할 배열
    var filteredSections = [SettingSection]()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 데이터 초기화
        filteredSections = settingSections
    }
}

```

<br><br>

테이블뷰도 바라보는 데이터를 ViewController에서 선언한 데이터를 이용하도록 수정한다.  

<br><br>

```swift


extension SettingViewController: UITableViewDataSource, UITableViewDelegate {

    /// 섹션의 수
    func numberOfSections(in tableView: UITableView) -> Int {
//        return settingSections.count
        return filteredSections.count
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        
//        return settingSections[section].settings.count

        return filteredSampleSections[section].settings.count
    }
    
    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {

//        let setting = settingSections[indexPath.section].settings[indexPath.row]
        let setting = filteredSampleSections[indexPath.section].settings[indexPath.row]
        return setting.cellType == .profileCell ? 80 : 50
    }

}
```

<br><br>

[[Top]](#contents)

<br><br><br>

### 적용화면_5

<img width="300" alt="ezgif-5-6b528b0e83" src="https://github.com/isGeekCode/github-action-til-autoformat-readme/assets/76529148/7a481015-2c1d-4b5f-9645-560064cad457">

<br><br>

[[Top]](#contents)

<br><br><br>

### 전체코드_1
```swift

import UIKit

class SettingViewController: UIViewController {
    
    lazy var tableView: UITableView = {
        let tableView = UITableView(frame: .zero, style: .insetGrouped)
        tableView.translatesAutoresizingMaskIntoConstraints = false
        tableView.dataSource = self
        tableView.delegate = self
        tableView.register(UITableViewCell.self, forCellReuseIdentifier: "Cell")
        return tableView
    }()
    
    let settingSections = SettingSection.sampleSections
    // 검색 결과를 저장할 배열
    var filteredSections = [SettingSection]()

    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        filteredSections = settingSections
        
        let searchController = UISearchController(searchResultsController: nil)
        searchController.searchBar.delegate = self

        navigationController?.navigationBar.prefersLargeTitles = true
        navigationItem.title = "내가 만든 설정 페이지"
        
        // 검색 중에 배경을 흐리게 하지 않도록 설정
        searchController.obscuresBackgroundDuringPresentation = false
        searchController.searchBar.placeholder = "검색"
        navigationItem.searchController =  searchController
        // 스크롤시에는 사라지도록 설정
        navigationItem.hidesSearchBarWhenScrolling = true
        
        // updateSearchResults(for:) 델리게이트를 사용을 위한 델리게이트 할당
        searchController.searchResultsUpdater = self

        // 필요한 경우 추가적인 검색 컨트롤러 설정
        definesPresentationContext = true

        
        view.backgroundColor = .systemGroupedBackground
        view.addSubview(tableView)
        
        NSLayoutConstraint.activate([
            tableView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
            tableView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor),
            tableView.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor),
            tableView.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor),
        ])
    }
    
    
    func configureProfileCell(_ cell: UITableViewCell, with setting: SettingModel) {
        let imageView = {
            let image = UIImage(systemName: setting.imageName)
            let imageView = UIImageView(image: image)
            imageView.tintColor = .lightGray
            return imageView
        }()
        
        let titleLabel = UILabel()
        titleLabel.text = setting.titleString
        titleLabel.font = UIFont.boldSystemFont(ofSize: 13)

        let detailLabel = UILabel()
        detailLabel.text = setting.description
        detailLabel.font = UIFont.systemFont(ofSize: 13)

        
        [imageView, titleLabel, detailLabel].forEach { 
            cell.contentView.addSubview($0)
            $0.translatesAutoresizingMaskIntoConstraints = false
        }
        
        NSLayoutConstraint.activate([
            imageView.leadingAnchor.constraint(equalTo: cell.contentView.leadingAnchor, constant: 20),
            imageView.centerYAnchor.constraint(equalTo: cell.contentView.layoutMarginsGuide.centerYAnchor),
            imageView.widthAnchor.constraint(equalToConstant: 70),
            imageView.heightAnchor.constraint(equalToConstant: 70),
            
            titleLabel.leadingAnchor.constraint(equalTo: imageView.trailingAnchor, constant: 10),
            titleLabel.centerYAnchor.constraint(equalTo: imageView.centerYAnchor, constant: -10),

            detailLabel.leadingAnchor.constraint(equalTo: imageView.trailingAnchor, constant: 10),
            detailLabel.centerYAnchor.constraint(equalTo: imageView.centerYAnchor, constant: 10),
        ])
    }
    
    func configureSettingCell(_ cell: UITableViewCell, with setting: SettingModel) {
        
        let containerView = {
            let containerView = UIView()
            containerView.translatesAutoresizingMaskIntoConstraints = false
            containerView.backgroundColor = setting.iconBackgroundColor
            containerView.layer.cornerRadius = 5
            containerView.clipsToBounds = true
            containerView.layoutMargins = UIEdgeInsets(top: 5, left: 5, bottom: 5, right: 5) 

            let image = UIImage(systemName: setting.imageName)

            let imageView = UIImageView(image: image)
            imageView.translatesAutoresizingMaskIntoConstraints = false
            imageView.contentMode = .scaleAspectFit 
            imageView.tintColor = .white

            containerView.addSubview(imageView)

            NSLayoutConstraint.activate([
                imageView.topAnchor.constraint(equalTo: containerView.layoutMarginsGuide.topAnchor),
                imageView.leadingAnchor.constraint(equalTo: containerView.layoutMarginsGuide.leadingAnchor),
                imageView.trailingAnchor.constraint(equalTo: containerView.layoutMarginsGuide.trailingAnchor),
                imageView.bottomAnchor.constraint(equalTo: containerView.layoutMarginsGuide.bottomAnchor)
            ])

            return containerView
        }()
        
        let textLabel = {
           let label = UILabel()
            label.text = setting.titleString
            label.textColor = .black
            label.translatesAutoresizingMaskIntoConstraints = false
            return label
        }()
        
        cell.contentView.addSubview(containerView)
        cell.contentView.addSubview(textLabel)
        
        NSLayoutConstraint.activate([
        
            containerView.leadingAnchor.constraint(equalTo: cell.contentView.leadingAnchor, constant: 20),
            containerView.centerYAnchor.constraint(equalTo: cell.contentView.centerYAnchor),
            containerView.widthAnchor.constraint(equalToConstant: 35), 
            containerView.heightAnchor.constraint(equalToConstant: 35), 
            
            textLabel.leadingAnchor.constraint(equalTo: containerView.trailingAnchor, constant: 10),
            textLabel.centerYAnchor.constraint(equalTo: containerView.centerYAnchor),
            
        ])
        cell.accessoryType = .disclosureIndicator

    }
}

extension SettingViewController:  UISearchResultsUpdating {
    func updateSearchResults(for searchController: UISearchController) {
        guard let searchText = searchController.searchBar.text, !searchText.isEmpty else {
            filteredSections = settingSections
            tableView.reloadData()
            return
        }
        
        // 검색어에 따른 필터링
            filteredSections = settingSections.map { section in
            // 각 섹션에서 titleString이 검색어를 포함하는 설정들만 필터링
            let filteredSettings = section.settings.filter { setting in
                setting.titleString.lowercased().contains(searchText.lowercased())
            }
            return SettingSection(settings: filteredSettings)
        }
        .filter { !$0.settings.isEmpty } // 빈 섹션은 제거

        tableView.reloadData()
        print("filteredSections::\n\(filteredSections)")
    }
}

extension SettingViewController: UISearchBarDelegate {
    func searchBarCancelButtonClicked(_ searchBar: UISearchBar) {
        // 검색 결과 배열을 원래 배열로 리셋
        filteredSections = settingSections
        // 테이블 뷰 리로드
        tableView.reloadData()
    }
}




extension SettingViewController: UITableViewDataSource, UITableViewDelegate {
    
    /// 섹션의 수
    func numberOfSections(in tableView: UITableView) -> Int {
        
        return filteredSections.count
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
    

        return filteredSections[section].settings.count
    }
    
    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
        
        let setting = filteredSections[indexPath.section].settings[indexPath.row]
        return setting.cellType == .profileCell ? 80 : 50
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        
        let setting = filteredSections[indexPath.section].settings[indexPath.row]
        let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath)
        cell.selectionStyle = .none

        switch setting.cellType {
        case .profileCell:
            configureProfileCell(cell, with: setting)
        case .settingCell:
            configureSettingCell(cell, with: setting)
        }

        return cell
    }

    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        
        let detailVC = DetailViewController()
        let setting = filteredSections[indexPath.section].settings[indexPath.row]
        detailVC.settingTitle = setting.titleString
        
        navigationController?.pushViewController(detailVC, animated: true)
    }
}

enum CellType {
    case profileCell
    case settingCell
}

struct SettingSection {
    let settings: [SettingModel]
}

struct SettingModel {
    let imageName: String
    let titleString: String
    let description: String
    let iconBackgroundColor: UIColor
    let cellType: CellType
}

extension SettingSection {
    
    static let sampleSections = [
        SettingSection(settings: [
            SettingModel(imageName: "person.crop.circle.fill",
                         titleString: "방현석",
                         description: "Apple ID, iCloud+ 미디어 및 구입 항목",
                         iconBackgroundColor: .clear,
                         cellType: CellType.profileCell),
        ]),
        
        SettingSection(settings: [
            SettingModel(imageName: "hourglass",
                         titleString: "스크린타임",
                         description: "",
                         iconBackgroundColor: .systemIndigo,
                         cellType: CellType.settingCell),
        ]),

        SettingSection(settings: [
            SettingModel(imageName: "airplane",
                         titleString: "에어플레인 모드",
                         description: "",
                         iconBackgroundColor: .systemOrange,
                         cellType: CellType.settingCell),

            SettingModel(imageName: "wifi",
                         titleString: "Wi-Fi",
                         description: "",
                         iconBackgroundColor: .systemBlue,
                         cellType: CellType.settingCell),
            
            SettingModel(imageName: "antenna.radiowaves.left.and.right",
                         titleString: "셀룰러",
                         description: "",
                         iconBackgroundColor: .systemGreen,
                         cellType: CellType.settingCell),
            
            SettingModel(imageName: "personalhotspot",
                         titleString: "개인용 핫스팟",
                         description: "",
                         iconBackgroundColor: .systemGreen,
                         cellType: CellType.settingCell),
        ]),

        
        SettingSection(settings: [
            SettingModel(imageName: "gear",
                         titleString: "일반",
                         description: "",
                         iconBackgroundColor: .lightGray,
                         cellType: CellType.settingCell),
            
            SettingModel(imageName: "accessibility",
                         titleString: "손쉬운 사용",
                         description: "",
                         iconBackgroundColor: .systemBlue,
                         cellType: CellType.settingCell),
            
            SettingModel(imageName: "hand.raised.fill",
                         titleString: "개인정보 보호 및 보안",
                         description: "",
                         iconBackgroundColor: .systemBlue,
                         cellType: CellType.settingCell),
            
        ]),
        
        SettingSection(settings: [
            SettingModel(imageName: "key.fill",
                         titleString: "암호",
                         description: "",
                         iconBackgroundColor: .lightGray,
                         cellType: CellType.settingCell),
            
        ]),
        
        SettingSection(settings: [
            SettingModel(imageName: "hammer.fill",
                         titleString: "개발자",
                         description: "",
                         iconBackgroundColor: .lightGray,
                         cellType: CellType.settingCell),
        ])
    ]
}


class DetailViewController: UIViewController {
    
    var settingTitle: String?

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .white
        navigationItem.title = settingTitle
    }
}

```

<br><br>

[[Top]](#contents)

<br><br><br>

## MVC로 리팩토링

현재 앱에서 가장 핵심 기능이라고 할 수 있는 것은 검색기능이라고 생각한다. 

여기서 다루는 데이터를 모두 모델에서 관리하도록 수정하려고 한다.  

기존에 갖고 있던 데이터는 SettingSection이라는 구조체 내부에 생성해둔 타입프로퍼티이다.   

이걸 UISearchResultsUpdating 에서 searchBar 검색결과에 따라  filteredSampleSections에 필터링된 결과를 부여하고, 검색 취소시 다시 sampleSections 데이터를 덮어씀으로 초기화 시켰다.  


```swift
class SettingViewController: UIViewController {

    let settingSections = SettingSection.sampleSections
    // 검색 결과를 저장할 배열
    var filteredSections = [SettingSection]()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 데이터 초기화
        filteredSections = settingSections
    }
}

extension SettingViewController:  UISearchResultsUpdating {
    
    func updateSearchResults(for searchController: UISearchController) {
        guard let searchText = searchController.searchBar.text, !searchText.isEmpty else {
            filteredSections = settingSections
            tableView.reloadData()
            return
        }
        
        // 검색어에 따른 필터링
        filteredSampleSections = settingSections.map { section in
            // 각 섹션에서 titleString이 검색어를 포함하는 설정들만 필터링
            let filteredSettings = section.settings.filter { setting in
                setting.titleString.lowercased().contains(searchText.lowercased())
            }
            return SettingSection(settings: filteredSettings)
        }
        .filter { !$0.settings.isEmpty } // 빈 섹션은 제거

        tableView.reloadData()
        print("filteredSections::\n\(filteredSections)")
    }
}

extension SettingViewController: UISearchBarDelegate {
    func searchBarCancelButtonClicked(_ searchBar: UISearchBar) {

        // 검색 결과 배열을 원래 배열로 리셋
        filteredSections = settingSections
        // 테이블 뷰 리로드
        tableView.reloadData()
    }
}
```

이제 이걸 새롭게 Model을 생성하여 Model로 이동시킨다.  

모델 SettingDataManager은 기존의 데이터를 갖고있고, 검색, 초기화 로직을 갖고있다.  


```swift
class SettingDataManager {
    private var originalSections = SettingSection.sampleSections
    var filteredSections: [SettingSection] = []

    init() {
        filteredSections = originalSections
    }

    func filterSettings(with searchText: String) {
        // 검색 내용이 없거나, 취소버튼 클릭
        if searchText.isEmpty {
            filteredSections = originalSections
        } else {
            filteredSections = originalSections.map { section in
                let filteredSettings = section.settings.filter { setting in
                    setting.titleString.lowercased().contains(searchText.lowercased())
                }
                return SettingSection(settings: filteredSettings)
            }
            .filter { !$0.settings.isEmpty }
        }
    }
}

```

<br><br>

이제 기존의 ViewController에서 선언하여 사용하던 데이터는 모델의 데이터를 사용하도록 수정한다.  

모델 내부에서 init시 초기화하기때문에 viewDidLoad에서 데이터를 다루던 것도 없애준다.  

```
class SettingViewController: UIViewController {

    var dataManager = SettingDataManager()

//    let settingSections = SettingSection.sampleSections
//    // 검색 결과를 저장할 배열
//    var filteredSections = [SettingSection]()

    
    override func viewDidLoad() {
        super.viewDidLoad()
        
//      filteredSections = settingSections
    }
}
```

그리고 나머지 데이터 바인딩도 모두 Model의 데이터를 바라볼 수 있도록 수정한다.  

<br><br>

[[Top]](#contents)

<br><br><br>


### 전체코드_2
```swift

import UIKit

class SettingViewController: UIViewController {
    
    lazy var tableView: UITableView = {
        let tableView = UITableView(frame: .zero, style: .insetGrouped)
        tableView.translatesAutoresizingMaskIntoConstraints = false
        tableView.dataSource = self
        tableView.delegate = self
        tableView.register(UITableViewCell.self, forCellReuseIdentifier: "Cell")
        return tableView
    }()
    
    var dataManager = SettingDataManager()
//    
//    let settingSections = SettingSection.sampleSections
//    // 검색 결과를 저장할 배열
//    var filteredSections = [SettingSection]()

    
    override func viewDidLoad() {
        super.viewDidLoad()
        
//        filteredSections = settingSections
        
        let searchController = UISearchController(searchResultsController: nil)
        searchController.searchBar.delegate = self

        navigationController?.navigationBar.prefersLargeTitles = true
        navigationItem.title = "내가 만든 설정 페이지"
        
        // 검색 중에 배경을 흐리게 하지 않도록 설정
        searchController.obscuresBackgroundDuringPresentation = false
        searchController.searchBar.placeholder = "검색"
        navigationItem.searchController =  searchController
        // 스크롤시에는 사라지도록 설정
        navigationItem.hidesSearchBarWhenScrolling = true
        
        // updateSearchResults(for:) 델리게이트를 사용을 위한 델리게이트 할당
        searchController.searchResultsUpdater = self

        // 필요한 경우 추가적인 검색 컨트롤러 설정
        definesPresentationContext = true

        
        view.backgroundColor = .systemGroupedBackground
        view.addSubview(tableView)
        
        NSLayoutConstraint.activate([
            tableView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
            tableView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor),
            tableView.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor),
            tableView.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor),
        ])
    }
    
    
    func configureProfileCell(_ cell: UITableViewCell, with setting: SettingModel) {
        let imageView = {
            let image = UIImage(systemName: setting.imageName)
            let imageView = UIImageView(image: image)
            imageView.tintColor = .lightGray
            return imageView
        }()
        
        let titleLabel = UILabel()
        titleLabel.text = setting.titleString
        titleLabel.font = UIFont.boldSystemFont(ofSize: 13)

        let detailLabel = UILabel()
        detailLabel.text = setting.description
        detailLabel.font = UIFont.systemFont(ofSize: 13)

        
        [imageView, titleLabel, detailLabel].forEach { 
            cell.contentView.addSubview($0)
            $0.translatesAutoresizingMaskIntoConstraints = false
        }
        
        NSLayoutConstraint.activate([
            imageView.leadingAnchor.constraint(equalTo: cell.contentView.leadingAnchor, constant: 20),
            imageView.centerYAnchor.constraint(equalTo: cell.contentView.layoutMarginsGuide.centerYAnchor),
            imageView.widthAnchor.constraint(equalToConstant: 70),
            imageView.heightAnchor.constraint(equalToConstant: 70),
            
            titleLabel.leadingAnchor.constraint(equalTo: imageView.trailingAnchor, constant: 10),
            titleLabel.centerYAnchor.constraint(equalTo: imageView.centerYAnchor, constant: -10),

            detailLabel.leadingAnchor.constraint(equalTo: imageView.trailingAnchor, constant: 10),
            detailLabel.centerYAnchor.constraint(equalTo: imageView.centerYAnchor, constant: 10),
        ])
    }
    
    func configureSettingCell(_ cell: UITableViewCell, with setting: SettingModel) {
        
        let containerView = {
            let containerView = UIView()
            containerView.translatesAutoresizingMaskIntoConstraints = false
            containerView.backgroundColor = setting.iconBackgroundColor
            containerView.layer.cornerRadius = 5
            containerView.clipsToBounds = true
            containerView.layoutMargins = UIEdgeInsets(top: 5, left: 5, bottom: 5, right: 5) 

            let image = UIImage(systemName: setting.imageName)

            let imageView = UIImageView(image: image)
            imageView.translatesAutoresizingMaskIntoConstraints = false
            imageView.contentMode = .scaleAspectFit 
            imageView.tintColor = .white

            containerView.addSubview(imageView)

            NSLayoutConstraint.activate([
                imageView.topAnchor.constraint(equalTo: containerView.layoutMarginsGuide.topAnchor),
                imageView.leadingAnchor.constraint(equalTo: containerView.layoutMarginsGuide.leadingAnchor),
                imageView.trailingAnchor.constraint(equalTo: containerView.layoutMarginsGuide.trailingAnchor),
                imageView.bottomAnchor.constraint(equalTo: containerView.layoutMarginsGuide.bottomAnchor)
            ])

            return containerView
        }()
        
        let textLabel = {
           let label = UILabel()
            label.text = setting.titleString
            label.textColor = .black
            label.translatesAutoresizingMaskIntoConstraints = false
            return label
        }()
        
        cell.contentView.addSubview(containerView)
        cell.contentView.addSubview(textLabel)
        
        NSLayoutConstraint.activate([
        
            containerView.leadingAnchor.constraint(equalTo: cell.contentView.leadingAnchor, constant: 20),
            containerView.centerYAnchor.constraint(equalTo: cell.contentView.centerYAnchor),
            containerView.widthAnchor.constraint(equalToConstant: 35), 
            containerView.heightAnchor.constraint(equalToConstant: 35), 
            
            textLabel.leadingAnchor.constraint(equalTo: containerView.trailingAnchor, constant: 10),
            textLabel.centerYAnchor.constraint(equalTo: containerView.centerYAnchor),
            
        ])
        cell.accessoryType = .disclosureIndicator

    }
}





extension SettingViewController:  UISearchResultsUpdating {
    
    func updateSearchResults(for searchController: UISearchController) {
        guard let searchText = searchController.searchBar.text else { return }
        dataManager.filterSettings(with: searchText)
        tableView.reloadData()
    }

// MARK: Model로 이동
//    func updateSearchResults(for searchController: UISearchController) {
//        guard let searchText = searchController.searchBar.text, !searchText.isEmpty else {
//            filteredSections = settingSections
//            tableView.reloadData()
//            return
//        }
//        
//        // 검색어에 따른 필터링
//        filteredSections = settingSections.map { section in
//            // 각 섹션에서 titleString이 검색어를 포함하는 설정들만 필터링
//            let filteredSettings = section.settings.filter { setting in
//                setting.titleString.lowercased().contains(searchText.lowercased())
//            }
//            return SettingSection(settings: filteredSettings)
//        }
//        .filter { !$0.settings.isEmpty } // 빈 섹션은 제거
//
//        tableView.reloadData()
//        print("filteredSections::\n\(filteredSections)")
//    }
    
    
}

extension SettingViewController: UISearchBarDelegate {
    func searchBarCancelButtonClicked(_ searchBar: UISearchBar) {
        
        // 검색 결과 배열을 원래 배열로 리셋
        dataManager.filterSettings(with: "")
//        filteredSections = settingSections
        
        // 테이블 뷰 리로드
        tableView.reloadData()
    }
}




extension SettingViewController: UITableViewDataSource, UITableViewDelegate {
    
    /// 섹션의 수
    func numberOfSections(in tableView: UITableView) -> Int {

//        return  filteredSections.count

        return  dataManager.filteredSections.count
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
//        return filteredSections[section].settings.count
        return dataManager.filteredSections[section].settings.count
    }
    
    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
        let setting = dataManager.filteredSections[indexPath.section].settings[indexPath.row]
//        let setting = filteredSections[indexPath.section].settings[indexPath.row]
        return setting.cellType == .profileCell ? 80 : 50
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let setting = dataManager.filteredSections[indexPath.section].settings[indexPath.row]
//        let setting = filteredSections[indexPath.section].settings[indexPath.row]
        let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath)
        cell.selectionStyle = .none
        // 셀 재사용시 초기화
        cell.contentView.subviews.forEach { $0.removeFromSuperview() }

        
        switch setting.cellType {
        case .profileCell:
            configureProfileCell(cell, with: setting)
        case .settingCell:
            configureSettingCell(cell, with: setting)
        }

        return cell
    }

    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        
        let detailVC = DetailViewController()
        let setting = dataManager.filteredSections[indexPath.section].settings[indexPath.row]
//        let setting = filteredSections[indexPath.section].settings[indexPath.row]
        detailVC.settingTitle = setting.titleString
        
        navigationController?.pushViewController(detailVC, animated: true)
    }
}

enum CellType {
    case profileCell
    case settingCell
}

struct SettingSection {
    let settings: [SettingModel]
}

struct SettingModel {
    let imageName: String
    let titleString: String
    let description: String
    let iconBackgroundColor: UIColor
    let cellType: CellType
}

extension SettingSection {
    
    static let sampleSections = [
        SettingSection(settings: [
            SettingModel(imageName: "person.crop.circle.fill",
                         titleString: "방현석",
                         description: "Apple ID, iCloud+ 미디어 및 구입 항목",
                         iconBackgroundColor: .clear,
                         cellType: CellType.profileCell),
        ]),
        
        SettingSection(settings: [
            SettingModel(imageName: "hourglass",
                         titleString: "스크린타임",
                         description: "",
                         iconBackgroundColor: .systemIndigo,
                         cellType: CellType.settingCell),
        ]),

        SettingSection(settings: [
            SettingModel(imageName: "airplane",
                         titleString: "에어플레인 모드",
                         description: "",
                         iconBackgroundColor: .systemOrange,
                         cellType: CellType.settingCell),

            SettingModel(imageName: "wifi",
                         titleString: "Wi-Fi",
                         description: "",
                         iconBackgroundColor: .systemBlue,
                         cellType: CellType.settingCell),
            
            SettingModel(imageName: "antenna.radiowaves.left.and.right",
                         titleString: "셀룰러",
                         description: "",
                         iconBackgroundColor: .systemGreen,
                         cellType: CellType.settingCell),
            
            SettingModel(imageName: "personalhotspot",
                         titleString: "개인용 핫스팟",
                         description: "",
                         iconBackgroundColor: .systemGreen,
                         cellType: CellType.settingCell),
        ]),

        
        SettingSection(settings: [
            SettingModel(imageName: "gear",
                         titleString: "일반",
                         description: "",
                         iconBackgroundColor: .lightGray,
                         cellType: CellType.settingCell),
            
            SettingModel(imageName: "accessibility",
                         titleString: "손쉬운 사용",
                         description: "",
                         iconBackgroundColor: .systemBlue,
                         cellType: CellType.settingCell),
            
            SettingModel(imageName: "hand.raised.fill",
                         titleString: "개인정보 보호 및 보안",
                         description: "",
                         iconBackgroundColor: .systemBlue,
                         cellType: CellType.settingCell),
            
        ]),
        
        SettingSection(settings: [
            SettingModel(imageName: "key.fill",
                         titleString: "암호",
                         description: "",
                         iconBackgroundColor: .lightGray,
                         cellType: CellType.settingCell),
            
        ]),
        
        SettingSection(settings: [
            SettingModel(imageName: "hammer.fill",
                         titleString: "개발자",
                         description: "",
                         iconBackgroundColor: .lightGray,
                         cellType: CellType.settingCell),
        ])
    ]
}


class DetailViewController: UIViewController {
    
    var settingTitle: String?

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .white
        navigationItem.title = settingTitle
    }
}


class SettingDataManager {
    private var originalSections = SettingSection.sampleSections
    var filteredSections: [SettingSection] = []

    init() {
        filteredSections = originalSections
    }

    func filterSettings(with searchText: String) {
        if searchText.isEmpty {
            filteredSections = originalSections
        } else {
            filteredSections = originalSections.map { section in
                let filteredSettings = section.settings.filter { setting in
                    setting.titleString.lowercased().contains(searchText.lowercased())
                }
                return SettingSection(settings: filteredSettings)
            }
            .filter { !$0.settings.isEmpty }
        }
    }
}

```

<br><br>

[Top](#contents)

<br><br><br>

## 셀을 클릭하면 디테일 화면으로 이동처리하기
```swift

extension SettingViewController: UITableViewDataSource, UITableViewDelegate {

    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        
//        print("didSelectRowAt: \(indexPath)")

        let detailVC = DetailViewController()
        let setting = dataManager.filteredSections[indexPath.section].settings[indexPath.row]
        detailVC.settingTitle = setting.titleString
        
        navigationController?.pushViewController(detailVC, animated: true)
    }
}


class DetailViewController: UIViewController {
    
    var settingTitle: String?

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .white
        navigationItem.title = settingTitle
    }
}


```

<br><br>

[[Top]](#contents)

<br><br><br>

### 적용화면_6

<img width="300" alt="ezgif-5-9673968c41" src="https://github.com/isGeekCode/github-action-til-autoformat-readme/assets/76529148/55c4695d-6bfd-4940-92b2-8a4fffe602b5">

<br><br>

[[Top]](#contents)

<br><br><br>

## History

- 231123: 초안 작성
