# [iOS App Dev Tutorials] UIKit - Today앱 만들기(2) : Adopting collection views

<br>

<img width="600" alt="스크린샷 2023-10-30 오전 9 34 03" src="https://github.com/isGeekCode/TIL/assets/76529148/c250a45b-b536-43fa-9515-64d0e4949f72">

<br><br>

# Adopting collection views: 컬렉션뷰 채택하기


- CollectionView는 정렬된 데이터 항목 컬렉션을 관리하고 커스텀 가능한 레이아웃을 사용하여 표시한다.
- CollectionView를 채택하면 데이터, 레이아웃 및 프레젠테이션과의 관련성을 분리할 수 있어서 더욱 강력하고 확장성있는 앱을 만들 수 있다.

<br><br>

## Section 1. Displaying collections
### 컬렉션 보여주기


많은 앱에서 데이터와 관련된 Collection들을 보여준다. UIKit은 scroll가능한 View 안에 데이터를 셀로 효율적으로 표시하는 UICollectionView를 제공한다. 

CollectionView는 Section을 통해 셀을 유연하게 구성한다. 

예를 들어, 음악 앱에서는 CollectionView로 내 음악들을 재생 목록으로 표시하거나, 인기도, 장르, 분위기에 따라 Section을 구성할 수 있다. 


<img width="300" alt="스크린샷 2023-10-30 오전 9 34 03" src="https://github.com/isGeekCode/TIL/assets/76529148/eea8f4ea-ead0-47b9-82bf-09ef47e3f4d3">

<br><br>

최근의 콜렉션뷰는 자동으로 데이터의 상태 변환에 따라 애니메이션 효과를 준다. 그리고 코드를 체계적으로 관리하는 데도 좋다. UIKit은 콜렉션뷰를 생성하고 업데이트 하기위한 
Diffable Data Source, Compositional Layout, cell configuration을 제공한다.   
이러한 구성요소들은 우리의 앱을 모듈형식으로 관리하고 유지보수 및 추가 개발을 더 용이하게 만든다. 

<img width="600" alt="스크린샷 2023-10-30 오전 9 34 03" src="https://github.com/isGeekCode/TIL/assets/76529148/7e0fe4b8-fb5d-41c9-8f27-e8e39b79f79d">

<br><br>

이 문서에서는 CollectionView를 선언하는 방법과 구성요소들을 어떻게 채워갈지 설명한다. 
순서는 아래와 같다. 

1. CollectionView에 대한 data source 만들기
2. CollectionView의 셀을 구성하는 cell provider 구현하기
3. 데이터의 현재 state 생성하기
4. UI에 데이터 표시하기

<br><br>

## Section 2. Creating a diffable data source
### Diffable Data Source 만들기 : 비교가능한 data source 만들기

CollectionView는 UI에서 항목들을 어떻게 배치하고 표시할지에 관하여 다루므로
효과적으로 데이터 관리에 집중할 수 있다. 

UICollectionViewDiffableDataSource 제네릭 클래스는 CollectionView에 연동된 데이터의 업데이트를 효율적으로 관리하고 안전하게 제공하는 동작을 제공한다.

이전 단계에서 아래처럼 typealias를 통해 별명을 만들어서 사용하였다.
```swift
typealias DataSource = UICollectionViewDiffableDataSource<Int, String>
```

DataSource의 생성자 메서드인 `init(collectionView:cellProvider:)`를 통해 컬렉션 뷰와 cellProvider(셀 제공자)를 파라미터로 인스턴스를 만들 수 있다.

### 참고: UICollectionViewDiffableDataSource 요리조리 뜯어보기

지난 번 구현했던 내용에서도 분명 UICollectionViewDiffableDataSource를 만들었지만 provider는 존재하지 않았다.  

이걸 살펴보려고 한다.  

```swift

import UIKit

class ReminderListViewController: UICollectionViewController {
    typealias DataSource = UICollectionViewDiffableDataSource<Int, String>
    typealias Snapshot = NSDiffableDataSourceSnapshot<Int, String>


    var dataSource: DataSource!

    override func viewDidLoad() {
        super.viewDidLoad()


        let listLayout = listLayout()
        collectionView.collectionViewLayout = listLayout


        let cellRegistration = UICollectionView.CellRegistration {
            (cell: UICollectionViewListCell, indexPath: IndexPath, itemIdentifier: String) in
            let reminder = Reminder.sampleData[indexPath.item]
            var contentConfiguration = cell.defaultContentConfiguration()
            contentConfiguration.text = reminder.title
            cell.contentConfiguration = contentConfiguration
        }

        // 이 부분
        dataSource = DataSource(collectionView: collectionView) {
            (collectionView: UICollectionView, indexPath: IndexPath, itemIdentifier: String) in
            return collectionView.dequeueConfiguredReusableCell(
                using: cellRegistration, for: indexPath, item: itemIdentifier)
        }

        var snapshot = Snapshot()
        snapshot.appendSections([0])
        snapshot.appendItems(Reminder.sampleData.map { $0.title })
        dataSource.apply(snapshot)
        collectionView.dataSource = dataSource
    }


    private func listLayout() -> UICollectionViewCompositionalLayout {
        var listConfiguration = UICollectionLayoutListConfiguration(appearance: .grouped)
        listConfiguration.showsSeparators = false
        listConfiguration.backgroundColor = .clear
        return UICollectionViewCompositionalLayout.list(using: listConfiguration)
    }
}

```

<br><br>

위 코드의 표시한 부분에서는 cell provider는 보이지않지만 이 파라미터는 사실 아래와 같이 클로저형식을 가지고 있다.

Cell Provider는 재사용가능한 셀을 찾아서 가져오고, 그 셀에 내용과 스타일을 추가하기 위한 메서드이다. 이 메서드는 CollectionView의 각 셀에 대한 작업을 담당하고, 재사용가능한 셀을 활용해 효율적으로 화면ㅇ르 구성한다. 


<br><br>

```swift
// 여기서 <Int, String>을 사용해서 하단에서도 itemIdentifier를 String으로 사용해야한다. 
// 상황에 따라 String대신 UUID 타입이나 커스텀 클래스를 사용할 수 있다.
typealias DataSource = UICollectionViewDiffableDataSource<Int, String>

let cellRegistration = UICollectionView.CellRegistration {
    (cell: UICollectionViewListCell, indexPath: IndexPath, itemIdentifier: String) in
    let reminder = Reminder.sampleData[indexPath.item]
    var contentConfiguration = cell.defaultContentConfiguration()
    contentConfiguration.text = reminder.title
    cell.contentConfiguration = contentConfiguration
}

// MARK: 방법1.
dataSource = DataSource(collectionView: collectionView) {
    (collectionView: UICollectionView, indexPath: IndexPath, itemIdentifier: String) in
    return collectionView.dequeueConfiguredReusableCell(
        using: cellRegistration, for: indexPath, item: itemIdentifier)
}
        
// MARK: 방법2.
dataSource = DataSource(collectionView: collectionView, cellProvider: { collectionView, indexPath, itemIdentifier in
        return collectionView.dequeueConfiguredReusableCell(
            using: cellRegistration, for: indexPath, item: itemIdentifier)

})
        
        
// MARK: 방법3.
let cellProvider: (UICollectionView, IndexPath, String) -> UICollectionViewCell? = { 
    collectionView, indexPath, itemIdentifier in
    // 이 클로저에서 셀을 생성하고 데이터를 설정하여 리턴합니다.
    return collectionView.dequeueConfiguredReusableCell(
        using: cellRegistration, for: indexPath, item: itemIdentifier)
}

dataSource = DataSource(collectionView: collectionView, cellProvider: cellProvider)
```

또한 이 과정을 아래처럼 메서드로 분리할 수 있다.

```swift
typealias DataSource = UICollectionViewDiffableDataSource<Int, ReminderItem>

func makeDataSource() -> DataSource {
    let reminderCellRegistration = self.reminderCellRegistration()
    return DataSource(collectionView: collectionView) {
        collectionView, indexPath, item -> UICollectionViewCell? in
        return collectionView.dequeueConfiguredReusableCell(
            using: reminderCellRegistration, for: indexPath, item: item)
    }
}

lazy var dataSource = makeDataSource()

```

<br><br>


## Section 3. Defining cell configurations
### 셀 configuration 정의하기

컬렉션 뷰는 셀을 세팅할때 앱의 데이터를 요청한다.   
컬렉션 뷰는 화면에서 벗어난 셀을 자동으로 재활용하므로 앱은 셀을 작성해야 하는 횟수를 최소화할 수 있다.  
이 셀 재사용은 부드러운 스크롤링과 메모리 사용량 감소를 가져온다.

CollectionView Cell은 CollectionView 안에서 위치(섹션 및 항목)에 따라 스스로 구성된다.  
Cell은 내용과 스타일에 대한 설명은 configuration properties에 저장된다.


UICollectionViewListCell은 아래처럼 3가지 configuration property를 갖고있다.

- contentConfiguration: 셀의 레이블, 이미지, 버튼 등을 나타낸다.
- backgroundConfiguration: 셀의 배경 색상, 그래디언트, 이미지 및 기타 시각적 속성을 나타낸다.
- configurationState: 사용자가 선택하거나 강조 표시하거나 드래그하거나 상호 작용할 때 셀의 스타일을 나타낸다.

각 경우에, defaultContentConfiguration(기본 구성)으로 셀의 임시 구성 인스턴스를 요청하고,  

변경하려는 속성에 새로운 값을 설정한 다음, 
configuration을 다시 셀에 세팅한다.


아래 코드는 이전 섹션의 데이터 소스에서 제공된 reminder를 표시하기 위해 셀을 등록하고 구성하는 과정을 보여준다

```SWIFT
func reminderCellRegistration() ->
UICollectionView.CellRegistration<UICollectionViewListCell, ReminderItem> {
    return .init { cell, _, item in
        guard let reminder = item.reminder else { return }
        
        var configuration = cell.defaultContentConfiguration()
        configuration.text = reminder.title
        configuration.textProperties.color = .darkGray
        
        // 선택된 상태일 때 텍스트 색상 변경
        if cell.configurationState.isSelected {
            configuration.textProperties.color = .blue
        } else {
            configuration.textProperties.color = .darkGray
        }
        
        cell.contentConfiguration = configuration
        
        var backgroundConfig = UIBackgroundConfiguration.listPlainCell()
        backgroundConfig.cornerRadius = 8
        cell.backgroundConfiguration = backgroundConfig
    }
}
```

<br><br>

default list Cell Configuration의 property는 대부분의 앱을 개발하는데 충분하다.

이들은 기본적인 Text, Secondary Text, 그리고 Image 프로퍼티를 포함하고 있다.  

이 모듈은 뒷부분에서 Today앱의 reminder 세부 정보를 표시할 때 사용한다.

독창적인 style을 가진 List Collection Cell을 구현하기 위해 이 configuration 을 커스텀할 예정이다.   


<br><br>


## Section 4. Generating data source snapshots

CollectionView는 셀을 세팅하기 위해 앱 데이터에 대한 설명이 필요하다.  
CollectionView와 연결된 DiffableDataSource는  NSDiffableDataSourceSnapshot 인스턴스를 사용하여 특정시간의 데이터 상태를 나타낸다.  
CollectionView가 처음 로드될 때, 앱의 데이터가 변경될 때마다 새 snapshot을 생성한다.  

아래 메서드는 알람 목록을 설명하는 snapshot을 생성하는 과정을 보여준다.  

```swift
func applyInitialSnapshots() {
    // Define snapshot with same <section,item> types as the data source.
    var initialSnapshot = NSDiffableDataSourceSnapshot<Int, ReminderItem>()
    let reminderItems = reminderStore.reminders.map { reminder in
        return ReminderItem(reminder: reminder)
    }
    
    initialSnapshot.appendSections([0]) // There is only one section in this list.
    initialSnapshot.appendItems(reminderItems, toSection: 0)
    dataSource.apply(initialSnapshot, animatingDifferences: false)
}

```

<br><br>

업데이트 된 snapshot을 적용하면 시스템에서는 두 snapshot 간의 차이를 계산한다. 그리고 해당 셀에 변경 사항을 적용한다.  
이 프로세스는 항상 현재 데이터의 상태를 UI에 반영시킨다.  



<br><br>

## Section 5. Using modern collection views in Today

Today 앱은 CollectionView를 이용해 목록에 정보를 표시한다.  

ReminderListViewController 는 앱이 시작될 때, reminder 데이터 리스트를 CollectionView로 표시한다.  

이 List를 보여주는 ViewController 는 데이터가 변경될때, snapshot을 적용하여 UI에 현재 reminder 데이터 리스트를 반영한다. 


다음 튜토리얼에서는 사용자가 reminder 리스트를 누르면 생성되는  세부정보(제목, 마감일, 메모)를 보여줄 ReminderViewController 클래스를 만들 예정이다.  
그래서 detailViewController는 reminder 세부정보가 바뀔 때마다 snapshot을 적용하여 항상 reminder 데이터 상태가 UI에 반영될 것이다.  

 
<br><br>



## 여기서 익힐 수 있는 것

- [DiffableDataSource가 나온이유](https://gyuios.tistory.com/153)
