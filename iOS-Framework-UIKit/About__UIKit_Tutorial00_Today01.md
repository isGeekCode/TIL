# [iOS App Dev Tutorials] UIKit - Today앱 만들기(1) : Creating a list View

<br>

<img width="600" alt="스크린샷 2023-10-30 오전 9 34 03" src="https://github.com/isGeekCode/TIL/assets/76529148/cf82834b-028b-4704-9205-936900e1c7ca">

<br><br>

# Creating a list View : 목록 View 만들기

이 앱의 첫 화면에는  CollectionView 가 있고, 이 콜렉션 뷰 안에 목록 (list) 레이아웃이 담겨있다.

그리고 이 리스트에 사용자의 일일 미리알림을 표시하게 되는 것이다

- CollectionView를 구성해서 List표시하기
- content configuration을 이용하여 셀의 Appearence 정의하기
- 데이터가 변경될 때, UI가 업데이트되도록 셀에 비교가능한 data source에 연결

<br><br>

## Section 1. Create a Project 
원하는 위치에 새 프로젝트를 생성한다.


## Section 2. Add a collection view controller
### UICollectionViewController추가하기

<img width="300" alt="스크린샷 2023-10-30 오전 9 34 03" src="https://github.com/isGeekCode/TIL/assets/76529148/01d441c1-3cc7-4acc-af1f-44f1a5127f98">


스토리보드에 ViewController를 추가한다.

ViewController는 View와 Data 모델들의 사일을 연결하는 다리 역할을 한다.

각 ViewController는 View 계층구졸르 관리하고 View에 있는 요소들을 업데이트하고 사용자 인터페이스에 따른 이벤트에 응답하는 일을 담당한다. 

이 앱에는 CollectionViewController를 사용할 예정이고, 이를 위해 InterfaceBuilder(IB; 스토리보드)를 사용한다. 

CollectionView는 grid, 열(column), 행(row) 또는 테이블에 셀을 표시할 수 있다.


<br><br>

## Section 3. Create a reminder model
### Reminder 모델 생성하기


<img width="300" alt="스크린샷 2023-10-30 오전 9 34 03" src="https://github.com/isGeekCode/TIL/assets/76529148/c26b56b1-d7b3-4836-a59b-62e7c82e7bb3">


UIKit앱의 일반적인 디자인 패턴인 MVC( Model - View - Controller ) 디자인 패턴에 따라 앱을 구성하자.

- View 객체는 데이터를 시각적으로 표현한다.
- Model 객체는 앱의 데이터와 비즈니스 로직을 관리한다.
- Model이 View를 직접 수정하지 않고, View가 Model에 직접 영향을 미치지 않도록 보장하는 ViewController를 만들자.

목록에 미리 알림을 나타낼 데이터 모델을 만들자  

Reminder.swift라는 새 파일을 구현한다.  
  
    
```swift
struct Reminder {
    var title: String
    var dueDate: Date
    var notes: String? = nil
    var isComplete: Bool = false
}
```

<br><br>
  
### 테스트용 더미데이터 생성

파일 맨 아래에 샘플 미리 알림 데이터를 저장할 확장 extension을 추가하고  `#if DEBUG`를 블록 안에 넣는다

플래그 `#if DEBUG`는 릴리스용 앱을 빌드할 때 포함된 코드가 컴파일되지 않도록 하는 컴파일 지시문이다.

디버그 빌드에서 코드를 테스트하거나 다음 단계에서 수행할 샘플 테스트 데이터를 제공하기 위해 이 플래그를 사용할 수 있다.


- 전체코드
```swift
//
//  Reminder.swift
//  Today
//
//  Created by bang_hyeonseok on 2023/10/27.
//

import Foundation

struct Reminder {
    var title: String
    var dueDate: Date
    var notes: String? = nil
    var isComplete: Bool = false
}


#if DEBUG
extension Reminder {
    
    static var sampleData = [
        Reminder(
            title: "Submit reimbursement report",
            dueDate: Date().addingTimeInterval(800.0),
            notes: "Don't forget about taxi receipts"),
        
        Reminder(
            title: "Code review",
            dueDate: Date().addingTimeInterval(14000.0),
            notes: "Check tech specs in shared folder",
            isComplete: true),
        
        Reminder(
            title: "Pick up new contacts",
            dueDate: Date().addingTimeInterval(24000.0),
            notes: "Optometrist closes at 6:00PM"),
        
        Reminder(
            title: "Add notes to retrospective",
            dueDate: Date().addingTimeInterval(3200.0),
            notes: "Collaborate with project manager",
            isComplete: true),
        
        Reminder(
            title: "Interview new project manager candidate",
            dueDate: Date().addingTimeInterval(60000.0),
            notes: "Review portfolio"),
        
        Reminder(
            title: "Mock up onboarding experience",
            dueDate: Date().addingTimeInterval(72000.0),
            notes: "Think different"),
        
        Reminder(
            title: "Review usage analytics",
            dueDate: Date().addingTimeInterval(83000.0),
            notes: "Discuss trends with management"),
        
        Reminder(
            title: "Confirm group reservation",
            dueDate: Date().addingTimeInterval(92500.0),
            notes: "Ask about space heaters"),
        
        Reminder(
            title: "Add beta testers to TestFlight",
            dueDate: Date().addingTimeInterval(101000.0),
            notes: "v0.9 out on Friday")
    ]

}
#endif
```

<br><br>

## Section 4. Configure the collection as a list
List로 Collection 구현하기

compositional Layout을 이용하여 콜렉션뷰 모양을 구현할 수 있다.

Compositional Layout을 사용하면 Section, Group, item 들을 조합해 구현할 수 있다.

Section은 item의 group을 둘러싼 Container View를 말한다.

<img width="300" alt="스크린샷 2023-10-30 오전 9 34 03" src="https://github.com/isGeekCode/TIL/assets/76529148/52042ead-9854-47b6-86f6-51c374cf7427">

<br><br>


- listLayout() : 이 메서드는 그룹화된 appearance가 적용된 새로운 list configuration   변수를 생성한다.
    - 리턴되는 `UICollectionViewCompositionalLayout`은  `UICollectionViewLayout` 타입이다.
    
```swift
private func listLayout() -> UICollectionViewCompositionalLayout {
    var listConfiguration = UICollectionLayoutListConfiguration(appearance: .grouped)
}
```

<br><br>

- 전체코드
    
```swift
//
//  ReminderListViewController.swift
//  Today
//
//  Created by bang_hyeonseok on 2023/10/27.
//

import UIKit

class ReminderListViewController: UICollectionViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

                //  View 계층구조 메모리에 새로운 layout을 선언
        let listLayout = listLayout()
        collectionView.collectionViewLayout = listLayout
    }

    private func listLayout() -> UICollectionViewCompositionalLayout {
        var listConfiguration = UICollectionLayoutListConfiguration(appearance: .grouped)
                // 구분기호를 비활성화하고, 배경색을 clear로 설정
        listConfiguration.showsSeparators = false
        listConfiguration.backgroundColor = .clear
                // 새로운 compositional Layout을  반환처리
        return UICollectionViewCompositionalLayout.list(using: listConfiguration)
    }
}
```
    
<br><br>

    
## Section 5. Configure the data source
데이터 소스 구현

- CollecitonView에 셀을 등록
- content configuration을 사용하여 셀 모양 정의
- 셀을 데이터 소스에 연결
- 데이터가 변경될때,  UI를 업데이트하고 애니메이션을 적용하는 diffable data source를 사용

<img width="300" alt="스크린샷 2023-10-30 오전 9 34 03" src="https://github.com/isGeekCode/TIL/assets/76529148/b4c8791a-d3ad-4834-b522-93a07e1a38c6">

<br><br>

이제 diffableDataSource(비교가 가능한 데이터 소스)에 셀을 연결한다.

- typealias를 통해서 diffableDataSource에 대한 별칭을 추가
    - 별칭은 보다 표현력이 뛰어난 변수명으로 기존 유형을 참조하는 데 유용하게 사용가능하다.
    
```swift
    typealias DataSource = UICollectionViewDiffableDataSource<Int, String>

```
    
<br><br>

암식적으로 래핑을 해제하는 타입을 추가한다.

- 옵셔널에 값이  있지 않으면 앱이 즉시 종료 되는 런타임 오류가 발생할 위험이 있다.

```swift
var dataSource: DataSource!
```

<br><br>

콜렉션뷰를  diffable data source 생성자에 전달하여 diffable data source를 collection View에 연결처리한다. 

- 초기화에서는 컬렉션 뷰에 대한 셀을 구성하고 반환하는 클로저를 전달한다. 클로저는 컬렉션 뷰의 셀 위치에 대한 인덱스 경로와 항목 식별자를 허용한다.
- 셀을 등록하여 해당 셀을 queue(대기열)에서 제외시키고 리턴한다.
    - 모든 item에 대해 새로운 셀을 생성할 수 있지만 생성에 대한 cost가 비싸져서 앱의 퍼포먼스를 저하시킨다. 셀을 다시 사용함으로서 item이 많더라도 원할하게 동작할 수 있다

```swift
dataSource = DataSource(collectionView: collectionView) {
            (collectionView: UICollectionView, indexPath: IndexPath, itemIdentifier: String) in
    return collectionView.dequeueConfiguredReusableCell(
            using: cellRegistration, for: indexPath, item: itemIdentifier)
}
```

<br><br>

- 전체코드

```swift
import UIKit

class ReminderListViewController: UICollectionViewController {
        // 비교가능한 데이터소스에 셀을 연결한다
    typealias DataSource = UICollectionViewDiffableDataSource<Int, String>

    var dataSource: DataSource!

    override func viewDidLoad() {
        super.viewDidLoad()

        let listLayout = listLayout()
        collectionView.collectionViewLayout = listLayout

        let cellRegistration = UICollectionView.CellRegistration {
            (cell: UICollectionViewListCell, indexPath: IndexPath, itemIdentifier: String) in
            let reminder = Reminder.sampleData[indexPath.item]
                        // 사전 정의된 system스타일로  content Configuration을 생성
            var contentConfiguration = cell.defaultContentConfiguration()
            contentConfiguration.text = reminder.title
            cell.contentConfiguration = contentConfiguration
        }

        dataSource = DataSource(collectionView: collectionView) {
            (collectionView: UICollectionView, indexPath: IndexPath, itemIdentifier: String) in
            return collectionView.dequeueConfiguredReusableCell(
                using: cellRegistration, for: indexPath, item: itemIdentifier)
        }
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

데이터 소스를 생성하고 초기화했다.

이제 데이터가 변경되면 dataSource에 알려야한다.

<br><br>

## Section 6. Apply a snapshot
스냅샷 적용하기

Diffable Data Source는 SnapShot을 통해 데이터 상태를 관리한다.

스냅샷은 특정시점의 데이터 상태`(State)`를 나타낸다. 

스냅샷을 사용하여 데이터를 표시하려면 

- 스냅샷을 생성하고
- 표시하려는 데이터 상태로 스냅샷을 채운다음
- UI에 스냅샷을 적용한다.

<img width="300" alt="스크린샷 2023-10-30 오전 9 34 03" src="https://github.com/isGeekCode/TIL/assets/76529148/187ba7c3-c821-4371-97c7-430ee2374941">

<br><br>

1. Diffable Data Source Snapshot에 대한 typealias`(별칭)`를 세팅
2. ViewDidLoad에서 빈 스냅샷을 생성해서 여기에 Section을 추가한다.
3. 알림 제목만 포함된 배열을 가져와서 snapshot의 item으로 적용한다. 
4. 생성한 snapShot을 dataSource에 적용한다.
5. 생성한 dataSource를 다시 CollectionView의 dataSource로 적용한다.

<br><br>

- 전체코드

```swift
import UIKit

class ReminderListViewController: UICollectionViewController {
    typealias DataSource = UICollectionViewDiffableDataSource<Int, String>
        // 1. Diffable Data Source Snapshot에 대한 typealias(별칭)을 세팅
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

        dataSource = DataSource(collectionView: collectionView) {
            (collectionView: UICollectionView, indexPath: IndexPath, itemIdentifier: String) in
            return collectionView.dequeueConfiguredReusableCell(
                using: cellRegistration, for: indexPath, item: itemIdentifier)
        }

                // 2. ViewDidLoad에서 빈 스냅샷을 생성해서 여기에 Section을 추가한다.
        var snapshot = Snapshot()
        snapshot.appendSections([0])
                // 3. 알림 제목만 포함된 배열을 가져와서 snapshot의 item으로 적용한다. 
                /*
                    var reminderTitles = [String]()
            for reminder in Reminder.sampleData {
                reminderTitles.append(reminder.title)
            }
                    snapshot.appendItems(reminderTitles)
                */
        snapshot.appendItems(Reminder.sampleData.map { $0.title })
                // 4. 생성한 snapShot을 dataSource에 적용한다.
        dataSource.apply(snapshot)
                // 5. 생성한 dataSource를 다시 CollectionView의 dataSource로 적용한다.
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


이제 앱을 빌드하면 아래처럼 나온다.


<img width="300" alt="스크린샷 2023-10-30 오전 9 34 03" src="https://github.com/isGeekCode/TIL/assets/76529148/9195849e-13c6-4452-a906-cdadf67a80e9">

## 문제

### Q1. Which responsibility does NOT belong to a view controller?
> ViewController에 해당하지 않는 책임은?

- 1. Defining business logic
    - 비즈니스 로직 정의
- 2. Managing a view hierarchy
    - View의 계층구조 관리
- 3. Updating content in views
    - View에서의 Content 업데이트
- 4. Responding to events in the user interface
    - UI의 이벤트 반응

### Q2. Which item is NOT a component of compositional layout?
> CompositionalLayout에 해당하지 않는 것은?

- 1. Configuration
- 2. Group
- 3. Item
- 4. Section


### Q3. Which object represents the state of your data at a specific point in time?
> 특정 시점에서의 데이터 상태를 나타내는 객체는?

- 1. Content Configuration
- 2. Diffable data source
- 3. Snapshot


## 정답

> - Q1 : ViewController에 해당하지 않는 책임은?
>> - A1 : 1번. Defining business logic
>>> - 1번 : O - MVC 디자인 패턴에서 모델 객체는 앱의 데이터와 비즈니스 로직을 관리한다.   
>>> - 2번 : X - 각 뷰 컨트롤러는 뷰 계층 구조를 관리한다.  
>>> - 3번 : X - 뷰 컨트롤러는 데이터가 변경될 때 뷰의 콘텐츠를 업데이트하는 브리지 역할을 한다.  
>>> - 4번 : X - 뷰 컨트롤러는 사용자가 버튼을 탭하는 것과 같은 사용자 인터페이스의 이벤트에 응답한다.  

> - Q2 : CompositionalLayout에 해당하지 않는 것은?
>> - A2 : 1번. configuration
>>> - 1번 : O - Configuration은 View 내부에 있는 Cell 모양을 정의하지만, Compositional Layout의 구성요소는 아니다.
>>> - 2번 : X - group은 Compositional Layout에서 두번째로 큰 요소이다. 
>>> - 3번 : X - item은 Compositional Layout에서 가장 작은 요소이다.  
>>> - 4번 : X - Section은 Compositional Layout에서 가장 큰 요소이다.  

> - Q3 : 특정 시점의 데이터 상태를 나타내는 객체는?
>> - A3 : 3번. Snapshot
>>> - 1번 : X - content configuration은 셀과 같은 개별적인 요소의 스타일을 표현한다.
>>> - 2번 : X - diffable data source에는 데이터의 상태를 나타내기 위한 세팅이 필요하다.
>>> - 3번 : O - Snapshot을 구성하고 적용하면 데이터의 현재 상태를 생성하고 UI에 데이터를 표시할 수 있다.



## 여기서 익힐 수 있는 것

- DiffableDataSource와 Snapshot을 이용한 CollectionView생성하기
    - 이 방법을 사용하면 자동으로 애니메이션이 적용된다.
    - Compositional Layout
    - Snapshot
- 디버그모드에서 테스트코드 생성하기
