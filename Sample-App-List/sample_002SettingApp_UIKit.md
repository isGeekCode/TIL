# Sample App : 설정앱 - UIKit(Code)




## 테이블뷰 세팅


```




```



## 모델



```swift
struct SettingModel {
    let imageName: String
    let titleString: String
    let iconBackgroundColor: UIColor
    let isDisclosure: Bool

    static let sampleModels = [
        
            SettingModel(imageName: "hourglass",
                         titleString: "스크린타임",
                         iconBackgroundColor: .systemIndigo,
                         isDisclosure: true),

            SettingModel(imageName: "airplane",
                         titleString: "에어플레인 모드",
                         iconBackgroundColor: .systemOrange,
                         isDisclosure: true),

            SettingModel(imageName: "wifi",
                         titleString: "Wi-Fi",
                         iconBackgroundColor: .systemBlue,
                         isDisclosure: true),
            
            SettingModel(imageName: "antenna.radiowaves.left.and.right",
                         titleString: "셀룰러",
                         iconBackgroundColor: .systemGreen,
                         isDisclosure: true),
            
            SettingModel(imageName: "personalhotspot",
                         titleString: "개인용 핫스팟",
                         iconBackgroundColor: .systemGreen,
                         isDisclosure: true),

        
            SettingModel(imageName: "gear",
                         titleString: "일반",
                         iconBackgroundColor: .lightGray,
                         isDisclosure: true),
            
            SettingModel(imageName: "accessibility",
                         titleString: "손쉬운 사용",
                         iconBackgroundColor: .systemBlue,
                         isDisclosure: true),
            
            SettingModel(imageName: "hand.raised.fill",
                         titleString: "개인정보 보호 및 보안",
                         iconBackgroundColor: .systemBlue,
                         isDisclosure: true),
        
            SettingModel(imageName: "key.fill",
                         titleString: "암호",
                         iconBackgroundColor: .lightGray,
                         isDisclosure: true),
            
    
        
            SettingModel(imageName: "hammer.fill",
                         titleString: "개발자",
                         iconBackgroundColor: .lightGray,
                         isDisclosure: true),
    ]
}


```


## Section별 그룹화

기존의 데이터를 Section별로 보여줄 수 있도록 SettingModel을 추상화 해준다.  

```swift
// 추가한 모델
struct SettingSection {
    let settings: [SettingModel]
}

// 기존 모델
struct SettingModel {
    let imageName: String
    let titleString: String
    let iconBackgroundColor: UIColor
    let isDisclosure: Bool
    let cellType: CellType
}

extension SettingSection {
    
    static let sampleSections = [
        
        SettingSection(settings: [
            SettingModel(imageName: "hourglass",
                         titleString: "스크린타임",
                         iconBackgroundColor: .systemIndigo,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
        ]),

        SettingSection(settings: [
            SettingModel(imageName: "airplane",
                         titleString: "에어플레인 모드",
                         iconBackgroundColor: .systemOrange,
                         isDisclosure: true,
                         cellType: CellType.settingCell),

            SettingModel(imageName: "wifi",
                         titleString: "Wi-Fi",
                         iconBackgroundColor: .systemBlue,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
            
            SettingModel(imageName: "antenna.radiowaves.left.and.right",
                         titleString: "셀룰러",
                         iconBackgroundColor: .systemGreen,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
            
            SettingModel(imageName: "personalhotspot",
                         titleString: "개인용 핫스팟",
                         iconBackgroundColor: .systemGreen,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
        ]),

        
        SettingSection(settings: [
            SettingModel(imageName: "gear",
                         titleString: "일반",
                         iconBackgroundColor: .lightGray,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
            
            SettingModel(imageName: "accessibility",
                         titleString: "손쉬운 사용",
                         iconBackgroundColor: .systemBlue,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
            
            SettingModel(imageName: "hand.raised.fill",
                         titleString: "개인정보 보호 및 보안",
                         iconBackgroundColor: .systemBlue,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
            
        ]),
        
        SettingSection(settings: [
            SettingModel(imageName: "key.fill",
                         titleString: "암호",
                         iconBackgroundColor: .lightGray,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
            
        ]),
        
        SettingSection(settings: [
            SettingModel(imageName: "hammer.fill",
                         titleString: "개발자",
                         iconBackgroundColor: .lightGray,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
        ])
    ]
}

```



초기화시 아래와 같이 style을 설정하면 그룹화된 UI를 구현할 수 있다.   

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

## didSelect 구현

```swift

extension SettingViewController: UITableViewDataSource, UITableViewDelegate {

    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        print("didSelectRowAt: \(indexPath)")
    }
}
```


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
    let isDisclosure: Bool
    let cellType: CellType
}

extension SettingSection {
    
    static let sampleSections = [
    
        // 첫번째 section
        SettingSection(settings: [
            SettingModel(imageName: "person.crop.circle.fill",
                         titleString: "방현석",
                         description: "Apple ID, iCloud+ 미디어 및 구입 항목",
                         iconBackgroundColor: .systemIndigo, // 사용안할 데이터
                         isDisclosure: true,
                         cellType: CellType.profileCell),
            ]),
        
        // 두번째 section
        SettingSection(settings: [
            SettingModel(imageName: "hourglass",
                         titleString: "스크린타임",
                         description: "", // 사용안할 데이터
                         iconBackgroundColor: .systemIndigo,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
            ]),
            
        // .... 나머지 데이터들
    ]
}
```

이제 섹션별로 이 더미데이터를 가져와서 세팅하도록 처리한다.  


```swift

extension SettingViewController: UITableViewDataSource, UITableViewDelegate {

    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
    
        return indexPath.section == 0 ? 80 : 50
    }

    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {

        let setting = sampleSections[indexPath.section].settings[indexPath.row]
        let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath)
        cell.selectionStyle = .none
        
        if indexPath.section == 0 {

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

        } else {
            // 일반 셀구현
        }
    }
}
```






이제 복잡해진 tableView 메서드를 아래와 같이 메서드로 분리하자.   


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

        let setting = sampleSections[indexPath.section].settings[indexPath.row]
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
    let isDisclosure: Bool
    let cellType: CellType
}


//데이터에도 적용

extension SettingSection {
    
    static let sampleSections = [
        SettingSection(settings: [
            SettingModel(imageName: "person.crop.circle.fill",
                         titleString: "방현석",
                         description: "Apple ID, iCloud+ 미디어 및 구입 항목",
                         iconBackgroundColor: .systemIndigo,
                         isDisclosure: true,
                         cellType: CellType.profileCell),
        ]),
        
        SettingSection(settings: [
            SettingModel(imageName: "hourglass",
                         titleString: "스크린타임",
                         description: "",
                         iconBackgroundColor: .systemIndigo,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
        ]),

        SettingSection(settings: [
            SettingModel(imageName: "airplane",
                         titleString: "에어플레인 모드",
                         description: "",
                         iconBackgroundColor: .systemOrange,
                         isDisclosure: true,
                         cellType: CellType.settingCell),

            SettingModel(imageName: "wifi",
                         titleString: "Wi-Fi",
                         description: "",
                         iconBackgroundColor: .systemBlue,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
            
            SettingModel(imageName: "antenna.radiowaves.left.and.right",
                         titleString: "셀룰러",
                         description: "",
                         iconBackgroundColor: .systemGreen,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
            
            SettingModel(imageName: "personalhotspot",
                         titleString: "개인용 핫스팟",
                         description: "",
                         iconBackgroundColor: .systemGreen,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
        ]),

        
        SettingSection(settings: [
            SettingModel(imageName: "gear",
                         titleString: "일반",
                         description: "",
                         iconBackgroundColor: .lightGray,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
            
            SettingModel(imageName: "accessibility",
                         titleString: "손쉬운 사용",
                         description: "",
                         iconBackgroundColor: .systemBlue,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
            
            SettingModel(imageName: "hand.raised.fill",
                         titleString: "개인정보 보호 및 보안",
                         description: "",
                         iconBackgroundColor: .systemBlue,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
            
        ]),
        
        SettingSection(settings: [
            SettingModel(imageName: "key.fill",
                         titleString: "암호",
                         description: "",
                         iconBackgroundColor: .lightGray,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
            
        ]),
        
        SettingSection(settings: [
            SettingModel(imageName: "hammer.fill",
                         titleString: "개발자",
                         description: "",
                         iconBackgroundColor: .lightGray,
                         isDisclosure: true,
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

        let setting = filteredSampleSections[indexPath.section].settings[indexPath.row]
        return setting.cellType == .profileCell ? 80 : 50
    }

    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {

        let setting = filteredSampleSections[indexPath.section].settings[indexPath.row]
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
```



## NavigationTitle 세팅하기

상단에 자동으로 세팅되는 타이틀효과는 네비게이션 컨트롤러의 기능이다.  
또 테이블뷰의 셀을 클릭했을 때, 네비게이션컨트롤러의 push이동을 하면 다음 화면에도 네비게이션 바를 세팅하여 일관성 있는 UI를 구성할 수 있다.  


이 기능을 사용하려면 현재 ViewController를 생성할 때, UINavigationController에 현재 ViewController를 넣어서 UINavigationController를 불러주어야한다.  

### 기존의 방법 : SettingVC 직접 호출

기존의 화면을 보여주기 위해선 SettingViewController를 직접 호출하였다.  

스토리보드를 사용했다면, 스토리보드의 SettingViewController에 is initial View Controller 설정되어있어야 했다.  

스토리보드를 아예 없앴다면 코드로 SceneDelegate(iOS13이후)이나 AppDelegate(iOS13이전)에서 rootViewController를 직접 설정했을 것이다.  


```swift

// SceneDelegate를 사용하는 경우 : iOS13 이후

class SceneDelegate: UIResponder, UIWindowSceneDelegate {

    var window: UIWindow?

    func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {

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


이제 네비게이션 컨트롤러가 세팅되었다면 ViewController에서 navigationController에 대한 코드를 삽입힌다.  

```swift

class SettingViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        
        navigationController?.navigationBar.prefersLargeTitles = true
        navigationItem.title = "내가 만든 설정 페이지"
    }
}
```


<br><br>

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


## SearchBar로 검색기능 추가하기

놀랍게도 navigationController에는 서치바를 제공해준다.  

서치바에서 검색결과에 따라 데이터를 변경하려면 아래와 같이 데이터를 만들어준다.  
```swift

class SettingViewController: UIViewController {

    let sampleSections = SettingSection.sampleSections
    // 검색 결과를 저장할 배열
    var filteredSampleSections = [SettingSection]()
}
```


서치바를 사용하는 방법은 아래와 같다.  
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


여기에 searchBar의 검색 조건에 따라 동작하도록 하기 위해선 searchController.searchResultsUpdater를 self로 선언하고 UISearchResultsUpdating 프로토콜을 채택해야한다.  

```swift

extension SettingViewController:  UISearchResultsUpdating {


    func updateSearchResults(for searchController: UISearchController) {
        guard let searchText = searchController.searchBar.text, !searchText.isEmpty else {
            filteredSampleSections = sampleSections
            tableView.reloadData()
            return
        }
        
        // 검색어에 따른 필터링
        filteredSampleSections = sampleSections.map { section in
            // 각 섹션에서 titleString이 검색어를 포함하는 설정들만 필터링
            let filteredSettings = section.settings.filter { setting in
                setting.titleString.lowercased().contains(searchText.lowercased())
            }
            return SettingSection(settings: filteredSettings)
        }
        .filter { !$0.settings.isEmpty } // 빈 섹션은 제거

        tableView.reloadData()
        print("filteredSampleSections::\n\(filteredSampleSections)")
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
        filteredSampleSections = sampleSections
        
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

    let sampleSections = SettingSection.sampleSections
    // 검색 결과를 저장할 배열
    var filteredSampleSections = [SettingSection]()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 데이터 초기화
        filteredSampleSections = sampleSections
    }
}

```

테이블뷰도 바라보는 데이터를 ViewController에서 선언한 데이터를 이용하도록 수정한다.  


```swift


extension SettingViewController: UITableViewDataSource, UITableViewDelegate {

    /// 섹션의 수
    func numberOfSections(in tableView: UITableView) -> Int {
        
        return filteredSampleSections.count
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        
        return filteredSampleSections[section].settings.count
    }
    
    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {

        let setting = filteredSampleSections[indexPath.section].settings[indexPath.row]
        return setting.cellType == .profileCell ? 80 : 50
    }

}
```



### 전체코드
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
    
    let sampleSections = SettingSection.sampleSections
    // 검색 결과를 저장할 배열
    var filteredSampleSections = [SettingSection]()

    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        filteredSampleSections = sampleSections
        
        let searchController = UISearchController(searchResultsController: nil)
        searchController.searchBar.delegate = self

        navigationController?.navigationBar.prefersLargeTitles = true
        navigationItem.title = "내가 만든 설정 페이지"
        
        // 검색 중에 배경을 흐리게 하지 않도록 설정
        searchController.obscuresBackgroundDuringPresentation = false
//        searchController.hidesNavigationBarDuringPresentation = false
        searchController.searchBar.placeholder = "검색"
        navigationItem.searchController =  searchController
        // 스크롤시에는 사라지도록 설정
        navigationItem.hidesSearchBarWhenScrolling = true
        
        // updateSearchResults(for:) 델리게이트를 사용을 위한 델리게이트 할당
        searchController.searchResultsUpdater = self

//        // navigationItem.titleView에 검색 바 설정
//        navigationItem.titleView = searchController.searchBar

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

            let image = UIImage(systemName: setting.imageName)?
                .withTintColor(.white, renderingMode: .alwaysOriginal)
                .applyingSymbolConfiguration(UIImage.SymbolConfiguration(pointSize: 20))

            let imageView = UIImageView(image: image)
            imageView.translatesAutoresizingMaskIntoConstraints = false
            imageView.contentMode = .scaleAspectFit 

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
            filteredSampleSections = sampleSections
            tableView.reloadData()
            return
        }
        
        // 검색어에 따른 필터링
        filteredSampleSections = sampleSections.map { section in
            // 각 섹션에서 titleString이 검색어를 포함하는 설정들만 필터링
            let filteredSettings = section.settings.filter { setting in
                setting.titleString.lowercased().contains(searchText.lowercased())
            }
            return SettingSection(settings: filteredSettings)
        }
        .filter { !$0.settings.isEmpty } // 빈 섹션은 제거

        tableView.reloadData()
        print("filteredSampleSections::\n\(filteredSampleSections)")
    }
}

extension SettingViewController: UISearchBarDelegate {
    func searchBarCancelButtonClicked(_ searchBar: UISearchBar) {
        // 검색 결과 배열을 원래 배열로 리셋
        filteredSampleSections = sampleSections
        // 테이블 뷰 리로드
        tableView.reloadData()
    }
}




extension SettingViewController: UITableViewDataSource, UITableViewDelegate {
    
    /// 섹션의 수
    func numberOfSections(in tableView: UITableView) -> Int {
        
        return filteredSampleSections.count
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        
        return filteredSampleSections[section].settings.count
    }
    
    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
        
        let setting = filteredSampleSections[indexPath.section].settings[indexPath.row]
        return setting.cellType == .profileCell ? 80 : 50
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        
        let setting = filteredSampleSections[indexPath.section].settings[indexPath.row]
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
        let setting = filteredSampleSections[indexPath.section].settings[indexPath.row]
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
    let isDisclosure: Bool
    let cellType: CellType
}

extension SettingSection {
    
    static let sampleSections = [
        SettingSection(settings: [
            SettingModel(imageName: "person.crop.circle.fill",
                         titleString: "방현석",
                         description: "Apple ID, iCloud+ 미디어 및 구입 항목",
                         iconBackgroundColor: .systemIndigo,
                         isDisclosure: true,
                         cellType: CellType.profileCell),
        ]),
        
        SettingSection(settings: [
            SettingModel(imageName: "hourglass",
                         titleString: "스크린타임",
                         description: "",
                         iconBackgroundColor: .systemIndigo,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
        ]),

        SettingSection(settings: [
            SettingModel(imageName: "airplane",
                         titleString: "에어플레인 모드",
                         description: "",
                         iconBackgroundColor: .systemOrange,
                         isDisclosure: true,
                         cellType: CellType.settingCell),

            SettingModel(imageName: "wifi",
                         titleString: "Wi-Fi",
                         description: "",
                         iconBackgroundColor: .systemBlue,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
            
            SettingModel(imageName: "antenna.radiowaves.left.and.right",
                         titleString: "셀룰러",
                         description: "",
                         iconBackgroundColor: .systemGreen,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
            
            SettingModel(imageName: "personalhotspot",
                         titleString: "개인용 핫스팟",
                         description: "",
                         iconBackgroundColor: .systemGreen,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
        ]),

        
        SettingSection(settings: [
            SettingModel(imageName: "gear",
                         titleString: "일반",
                         description: "",
                         iconBackgroundColor: .lightGray,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
            
            SettingModel(imageName: "accessibility",
                         titleString: "손쉬운 사용",
                         description: "",
                         iconBackgroundColor: .systemBlue,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
            
            SettingModel(imageName: "hand.raised.fill",
                         titleString: "개인정보 보호 및 보안",
                         description: "",
                         iconBackgroundColor: .systemBlue,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
            
        ]),
        
        SettingSection(settings: [
            SettingModel(imageName: "key.fill",
                         titleString: "암호",
                         description: "",
                         iconBackgroundColor: .lightGray,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
            
        ]),
        
        SettingSection(settings: [
            SettingModel(imageName: "hammer.fill",
                         titleString: "개발자",
                         description: "",
                         iconBackgroundColor: .lightGray,
                         isDisclosure: true,
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

## MVC로 리팩토링

현재 앱에서 가장 핵심 기능이라고 할 수 있는 것은 검색기능이라고 생각한다. 

여기서 다루는 데이터를 모두 모델에서 관리하도록 수정하려고 한다.  

기존에 갖고 있던 데이터는 SettingSection이라는 구조체 내부에 생성해둔 타입프로퍼티이다.   

이걸 UISearchResultsUpdating 에서 searchBar 검색결과에 따라  filteredSampleSections에 필터링된 결과를 부여하고, 검색 취소시 다시 sampleSections 데이터를 덮어씀으로 초기화 시켰다.  


```swift
class SettingViewController: UIViewController {

    let sampleSections = SettingSection.sampleSections
    // 검색 결과를 저장할 배열
    var filteredSampleSections = [SettingSection]()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 데이터 초기화
        filteredSampleSections = sampleSections
    }
}

extension SettingViewController:  UISearchResultsUpdating {
    
    func updateSearchResults(for searchController: UISearchController) {
        guard let searchText = searchController.searchBar.text, !searchText.isEmpty else {
            filteredSampleSections = sampleSections
            tableView.reloadData()
            return
        }
        
        // 검색어에 따른 필터링
        filteredSampleSections = sampleSections.map { section in
            // 각 섹션에서 titleString이 검색어를 포함하는 설정들만 필터링
            let filteredSettings = section.settings.filter { setting in
                setting.titleString.lowercased().contains(searchText.lowercased())
            }
            return SettingSection(settings: filteredSettings)
        }
        .filter { !$0.settings.isEmpty } // 빈 섹션은 제거

        tableView.reloadData()
        print("filteredSampleSections::\n\(filteredSampleSections)")
    }
}

extension SettingViewController: UISearchBarDelegate {
    func searchBarCancelButtonClicked(_ searchBar: UISearchBar) {

        // 검색 결과 배열을 원래 배열로 리셋
        filteredSampleSections = sampleSections
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

class SettingViewController: UIViewController {

    var dataManager = SettingDataManager()

//    let sampleSections = SettingSection.sampleSections
//    // 검색 결과를 저장할 배열
//    var filteredSampleSections = [SettingSection]()

    
    override func viewDidLoad() {
        super.viewDidLoad()
        
//      filteredSampleSections = sampleSections
    }
}


그리고 나머지 데이터 바인딩도 모두 Model의 데이터를 바라볼 수 있도록 수정한다.  

<br><br>


### 전체코드
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
//    let sampleSections = SettingSection.sampleSections
//    // 검색 결과를 저장할 배열
//    var filteredSampleSections = [SettingSection]()

    
    override func viewDidLoad() {
        super.viewDidLoad()
        
//        filteredSampleSections = sampleSections
        
        let searchController = UISearchController(searchResultsController: nil)
        searchController.searchBar.delegate = self

        navigationController?.navigationBar.prefersLargeTitles = true
        navigationItem.title = "내가 만든 설정 페이지"
        
        // 검색 중에 배경을 흐리게 하지 않도록 설정
        searchController.obscuresBackgroundDuringPresentation = false
//        searchController.hidesNavigationBarDuringPresentation = false
        searchController.searchBar.placeholder = "검색"
        navigationItem.searchController =  searchController
        // 스크롤시에는 사라지도록 설정
        navigationItem.hidesSearchBarWhenScrolling = true
        
        // updateSearchResults(for:) 델리게이트를 사용을 위한 델리게이트 할당
        searchController.searchResultsUpdater = self

//        // navigationItem.titleView에 검색 바 설정
//        navigationItem.titleView = searchController.searchBar

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

            let image = UIImage(systemName: setting.imageName)?
                .withTintColor(.white, renderingMode: .alwaysOriginal)
                .applyingSymbolConfiguration(UIImage.SymbolConfiguration(pointSize: 20))

            let imageView = UIImageView(image: image)
            imageView.translatesAutoresizingMaskIntoConstraints = false
            imageView.contentMode = .scaleAspectFit 

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
//            filteredSampleSections = sampleSections
//            tableView.reloadData()
//            return
//        }
//        
//        // 검색어에 따른 필터링
//        filteredSampleSections = sampleSections.map { section in
//            // 각 섹션에서 titleString이 검색어를 포함하는 설정들만 필터링
//            let filteredSettings = section.settings.filter { setting in
//                setting.titleString.lowercased().contains(searchText.lowercased())
//            }
//            return SettingSection(settings: filteredSettings)
//        }
//        .filter { !$0.settings.isEmpty } // 빈 섹션은 제거
//
//        tableView.reloadData()
//        print("filteredSampleSections::\n\(filteredSampleSections)")
//    }
    
    
}

extension SettingViewController: UISearchBarDelegate {
    func searchBarCancelButtonClicked(_ searchBar: UISearchBar) {
        
        // 검색 결과 배열을 원래 배열로 리셋
        dataManager.filterSettings(with: "")
//        filteredSampleSections = sampleSections
        
        // 테이블 뷰 리로드
        tableView.reloadData()
    }
}




extension SettingViewController: UITableViewDataSource, UITableViewDelegate {
    
    /// 섹션의 수
    func numberOfSections(in tableView: UITableView) -> Int {
        
        return  dataManager.filteredSections.count
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        
        return dataManager.filteredSections[section].settings.count
    }
    
    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
        let setting = dataManager.filteredSections[indexPath.section].settings[indexPath.row]
//        let setting = filteredSampleSections[indexPath.section].settings[indexPath.row]
        return setting.cellType == .profileCell ? 80 : 50
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let setting = dataManager.filteredSections[indexPath.section].settings[indexPath.row]
//        let setting = filteredSampleSections[indexPath.section].settings[indexPath.row]
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
//        let setting = filteredSampleSections[indexPath.section].settings[indexPath.row]
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
    let isDisclosure: Bool
    let cellType: CellType
}

extension SettingSection {
    
    static let sampleSections = [
        SettingSection(settings: [
            SettingModel(imageName: "person.crop.circle.fill",
                         titleString: "방현석",
                         description: "Apple ID, iCloud+ 미디어 및 구입 항목",
                         iconBackgroundColor: .systemIndigo,
                         isDisclosure: true,
                         cellType: CellType.profileCell),
        ]),
        
        SettingSection(settings: [
            SettingModel(imageName: "hourglass",
                         titleString: "스크린타임",
                         description: "",
                         iconBackgroundColor: .systemIndigo,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
        ]),

        SettingSection(settings: [
            SettingModel(imageName: "airplane",
                         titleString: "에어플레인 모드",
                         description: "",
                         iconBackgroundColor: .systemOrange,
                         isDisclosure: true,
                         cellType: CellType.settingCell),

            SettingModel(imageName: "wifi",
                         titleString: "Wi-Fi",
                         description: "",
                         iconBackgroundColor: .systemBlue,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
            
            SettingModel(imageName: "antenna.radiowaves.left.and.right",
                         titleString: "셀룰러",
                         description: "",
                         iconBackgroundColor: .systemGreen,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
            
            SettingModel(imageName: "personalhotspot",
                         titleString: "개인용 핫스팟",
                         description: "",
                         iconBackgroundColor: .systemGreen,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
        ]),

        
        SettingSection(settings: [
            SettingModel(imageName: "gear",
                         titleString: "일반",
                         description: "",
                         iconBackgroundColor: .lightGray,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
            
            SettingModel(imageName: "accessibility",
                         titleString: "손쉬운 사용",
                         description: "",
                         iconBackgroundColor: .systemBlue,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
            
            SettingModel(imageName: "hand.raised.fill",
                         titleString: "개인정보 보호 및 보안",
                         description: "",
                         iconBackgroundColor: .systemBlue,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
            
        ]),
        
        SettingSection(settings: [
            SettingModel(imageName: "key.fill",
                         titleString: "암호",
                         description: "",
                         iconBackgroundColor: .lightGray,
                         isDisclosure: true,
                         cellType: CellType.settingCell),
            
        ]),
        
        SettingSection(settings: [
            SettingModel(imageName: "hammer.fill",
                         titleString: "개발자",
                         description: "",
                         iconBackgroundColor: .lightGray,
                         isDisclosure: true,
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


## 셀을 클릭하면 디테일 화면으로 이동처리하기
```swift

extension SettingViewController: UITableViewDataSource, UITableViewDelegate {

    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        
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


