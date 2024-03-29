# Block6 앱 만들기



## 기본 레이아웃 구성
```
//
//  ViewController.swift
//  uikitPractice
//
//  Created by bang_hyeonseok on 11/28/23.
//

import UIKit



class MainViewController: UIViewController {

    var dataManager = BlockDataManager()
    
    lazy var dateLabel: UILabel = {
        let label = UILabel()
        label.translatesAutoresizingMaskIntoConstraints = false
        let today = Date()
        let dateFormatter = DateFormatter()
        dateFormatter.dateStyle = .none
        dateFormatter.dateFormat = "yyyy-MM-dd"
        let dateStr = dateFormatter.string(from: today)
        label.text = dateStr
        
        return label
    }()
    lazy var collectionView: UICollectionView = {
        let layout = UICollectionViewFlowLayout()
        layout.scrollDirection = .vertical
        layout.sectionInset = UIEdgeInsets(top: 5, left: 0, bottom: 5, right: 0)
        
        let collectionView = UICollectionView(frame: .zero, collectionViewLayout: layout)
        collectionView.delegate = self
        collectionView.dataSource = self
        collectionView.translatesAutoresizingMaskIntoConstraints = false
        collectionView.backgroundColor = .white // 배경색 설정
        collectionView.register(UICollectionViewCell.self, forCellWithReuseIdentifier: "cell")

        return collectionView
    }()

    override func viewDidLoad() {
        super.viewDidLoad()

        view.backgroundColor = .white

        title = "Today"
//        navigationController?.navigationBar.prefersLargeTitles = true
        
        view.addSubview(dateLabel)
        view.addSubview(collectionView)
        NSLayoutConstraint.activate([
            
            
            dateLabel.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 10),
            dateLabel.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),

            
            collectionView.topAnchor.constraint(equalTo: dateLabel.bottomAnchor, constant: 10),
            collectionView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor),
            collectionView.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor),
            collectionView.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor),
        ])

    }
}

extension MainViewController: UICollectionViewDelegate, UICollectionViewDataSource {

    func numberOfSections(in collectionView: UICollectionView) -> Int {
        return dataManager.itemSections.count
    }

    // 섹션안의 item갯수
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return dataManager.itemSections[section].itemSection.count
    }

    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "cell", for: indexPath)
        // 셀 커스터마이징
        let view = UIView()
        let titleLabel = UILabel()
        view.translatesAutoresizingMaskIntoConstraints = false
        titleLabel.translatesAutoresizingMaskIntoConstraints = false
        titleLabel.font = UIFont.boldSystemFont(ofSize: 20)
        cell.contentView.addSubview(view)
        view.addSubview(titleLabel)
        titleLabel.textColor = .black
        let safeAreaLayoutGuide = cell.contentView.safeAreaLayoutGuide
        NSLayoutConstraint.activate([
            view.topAnchor.constraint(equalTo: safeAreaLayoutGuide.topAnchor),
            view.bottomAnchor.constraint(equalTo: safeAreaLayoutGuide.bottomAnchor),
            view.leadingAnchor.constraint(equalTo: safeAreaLayoutGuide.leadingAnchor, constant: 10),
            view.trailingAnchor.constraint(equalTo: safeAreaLayoutGuide.trailingAnchor, constant: -10),
            
            titleLabel.centerYAnchor.constraint(equalTo: view.centerYAnchor),
            titleLabel.centerXAnchor.constraint(equalTo: view.centerXAnchor),
        ])
        
        let item = dataManager.itemSections[indexPath.section].itemSection[indexPath.row]

        if item.itemName == "" {
            titleLabel.text = "오늘의 블럭을 추가해주세요"
        } else {
            titleLabel.text = item.itemName
        }
//        let item = ItemSection.itemSections[indexPath.section].itemSection[indexPath.row]

        
        view.layer.cornerRadius = 10
        view.backgroundColor = .systemGray5

        return cell
    }
}

extension MainViewController: UICollectionViewDelegateFlowLayout {

    // 각 섹션에서 셀 간의 최소 수직 간격을 결정
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, minimumLineSpacingForSectionAt section: Int) -> CGFloat {
        return 1
    }
    
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
        
        // 섹션의 높이 = view.bounds.height * 0.06 * 셀갯수
        let sectionCount = CGFloat(dataManager.itemSections.count)
        print("여기 또 타는지 보자구:: \(sectionCount)")
        let height = (collectionView.bounds.height - (2 * sectionCount * 5)) / sectionCount

        return CGSize(width: collectionView.bounds.width, height: height)
    }
    
    func collectionView(_ collectionView: UICollectionView, didSelectItemAt indexPath: IndexPath) {
        print("didSelectItemAt: \(indexPath)")
        let count = dataManager.itemSections.count
        let newItem = ItemModel(itemName: "block\(count+1)")
        dataManager.addItemToSection(indexPath.section, item: newItem)
        
        // 레이아웃 무효화 및 데이터 리로드
//        collectionView.collectionViewLayout.invalidateLayout()

        collectionView.reloadData()

    }
}


class BlockDataManager {
    var itemSections: [ItemSection] = [
        ItemSection(itemSection: [
            ItemModel(itemName: "오늘의 블럭을 추가해주세요")
        ])
    ]
    
    
    func addItemToSection(_ section: Int, item: ItemModel) {
        if itemSections.count < 6 {
            itemSections.append(ItemSection(itemSection: [item]))
        }
    }


}

```


## DiffableDataSource로 변경
```swift

import UIKit

// 1. 데이터 모델 정의
struct Item: Hashable {
    let id = UUID()
    let title: String
}

enum Section {
    case main
}

class MainViewController: UIViewController {
    // 2. UICollectionView 및 DataSource 정의
    lazy var collectionView: UICollectionView = {
        let layout = UICollectionViewFlowLayout()
        layout.scrollDirection = .vertical
        layout.sectionInset = UIEdgeInsets(top: 5, left: 0, bottom: 5, right: 0)

        let collectionView = UICollectionView(frame: .zero,
                                              collectionViewLayout: layout)
        collectionView.translatesAutoresizingMaskIntoConstraints = false
        collectionView.delegate = self
        collectionView.register(CustomCollectionViewCell.self, forCellWithReuseIdentifier: CustomCollectionViewCell.identifier)

        return collectionView
    }()
    
    lazy var dateLabel: UILabel = {
        let label = UILabel()
        label.translatesAutoresizingMaskIntoConstraints = false
        let today = Date()
        let dateFormatter = DateFormatter()
        dateFormatter.dateStyle = .none
        dateFormatter.dateFormat = "yyyy-MM-dd"
        let dateStr = dateFormatter.string(from: today)
        label.text = dateStr
        
        return label
    }()

    
    
    private var dataSource: UICollectionViewDiffableDataSource<Section, Item>!

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .white
        title = "Today"
        setupCollectionView()
    }

    private func setupCollectionView() {
        
        view.addSubview(dateLabel)
        view.addSubview(collectionView)
        NSLayoutConstraint.activate([
            
            dateLabel.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 10),
            dateLabel.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),

            
            collectionView.topAnchor.constraint(equalTo: dateLabel.bottomAnchor, constant: 10),
            collectionView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor),
            collectionView.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor),
            collectionView.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor),
        ])

        // 3. DataSource 및 기타 설정
        configureDataSource()

    }

    private func configureDataSource() {
        // 5. DataSource 설정 및 셀 구성
        dataSource = UICollectionViewDiffableDataSource<Section, Item>(collectionView: collectionView) {
            (collectionView, indexPath, item) -> UICollectionViewCell? in
            let cell = collectionView.dequeueReusableCell(withReuseIdentifier: CustomCollectionViewCell.identifier, for: indexPath) as! CustomCollectionViewCell
            cell.configure(with: item.title)
            return cell
        }
        
        applyInitialSnapshots() // 초기 데이터 로드

    }

    private func applyInitialSnapshots() {
        // 6. 초기 데이터 스냅샷 적용
        var snapshot = NSDiffableDataSourceSnapshot<Section, Item>()
        snapshot.appendSections([.main])
        snapshot.appendItems([
            Item(title: "Block 1"),
        ])
        dataSource.apply(snapshot, animatingDifferences: false)
    }
}

extension MainViewController: UICollectionViewDelegateFlowLayout {
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
        // 현재 스냅샷에서 전체 아이템의 수를 계산
        let itemCount = dataSource.snapshot().numberOfItems

        // 각 섹션의 높이를 계산
        let sectionHeight = (collectionView.bounds.height - (2 * CGFloat(itemCount) * 5)) / CGFloat(itemCount)

        // 셀의 크기 반환
        return CGSize(width: collectionView.bounds.width, height: sectionHeight)
    }
}

extension MainViewController: UICollectionViewDelegate {
    
    func collectionView(_ collectionView: UICollectionView, didSelectItemAt indexPath: IndexPath) {
        // 현재 스냅샷의 아이템 수
        let currentSnapshot = dataSource.snapshot()
        let itemCount = currentSnapshot.numberOfItems
        // 새로운 아이템 생성 (아이템 개수 + 1)
        let newItem = Item(title: "Block \(itemCount + 1)")

        // 새 스냅샷에 아이템 추가
        var newSnapshot = currentSnapshot
        newSnapshot.appendItems([newItem], toSection: .main)

        // 스냅샷 적용
//        dataSource.apply(newSnapshot, animatingDifferences: true)
        
//        // 레이아웃 강제 업데이트
//        collectionView.collectionViewLayout.invalidateLayout()
        // 스냅샷 적용 및 전체 뷰 갱신
        dataSource.apply(newSnapshot, animatingDifferences: true) {
            // 모든 셀을 새로 그리도록 컬렉션 뷰에 지시
//            collectionView.reloadData()
        }

    }
}



import UIKit

class CustomCollectionViewCell: UICollectionViewCell {
    static let identifier = "CustomCollectionViewCell"
    
    
    lazy var titleLabel: UILabel = {
        let label = UILabel()
        label.textAlignment = .center
        label.textColor = .black
        label.translatesAutoresizingMaskIntoConstraints = false
        return label
    }()
    
    lazy var containerView: UIView = {
        let view = UIView()
        view.translatesAutoresizingMaskIntoConstraints = false
        view.backgroundColor = .systemGray
        view.layer.cornerRadius = 30

        return view
    }()

    override init(frame: CGRect) {
        super.init(frame: frame)
        contentView.addSubview(containerView)
        containerView.addSubview(titleLabel)
        
        NSLayoutConstraint.activate([
        
            containerView.topAnchor.constraint(equalTo: self.contentView.topAnchor),
            containerView.bottomAnchor.constraint(equalTo: self.contentView.bottomAnchor),
            containerView.leadingAnchor.constraint(equalTo: self.contentView.leadingAnchor, constant: 10),
            containerView.trailingAnchor.constraint(equalTo: self.contentView.trailingAnchor, constant: -10),
                    
            titleLabel.centerXAnchor.constraint(equalTo: containerView.centerXAnchor),
            titleLabel.centerYAnchor.constraint(equalTo: containerView.centerYAnchor),
        ])
        
        
        
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    override func prepareForReuse() {
        super.prepareForReuse()
        titleLabel.text = nil // 텍스트 초기화
    }

    
    func configure(with title: String) {
        titleLabel.text = title
    }
}

```

## Item 추가 동작 구현 


```swift
//
//  ViewController.swift
//  CollectionViewApp
//
//  Created by bang_hyeonseok on 12/5/23.
//

import UIKit

// 1. 데이터 모델 정의
struct Item: Hashable {
    let id = UUID()
    let title: String
    
    // Add this static property
    static let initialData: [Item] = [
        Item(title: "Block 1"),
        Item(title: "Block 2"),
    ]
}

enum Section {
    case main
}

class MainViewController: UIViewController {
    // 2. UICollectionView 및 DataSource 정의
    lazy var collectionView: UICollectionView = {
        let layout = UICollectionViewFlowLayout()
        layout.scrollDirection = .vertical
        layout.sectionInset = UIEdgeInsets(top: 0, left: 0, bottom: 0, right: 0)
        
        let collectionView = UICollectionView(frame: .zero,
                                              collectionViewLayout: layout)
        collectionView.translatesAutoresizingMaskIntoConstraints = false
        collectionView.delegate = self
        collectionView.register(CustomCollectionViewCell.self, forCellWithReuseIdentifier: CustomCollectionViewCell.identifier)
        
        return collectionView
    }()
    
    lazy var dateLabel: UILabel = {
        let label = UILabel()
        label.translatesAutoresizingMaskIntoConstraints = false
        let today = Date()
        let dateFormatter = DateFormatter()
        dateFormatter.dateStyle = .none
        dateFormatter.dateFormat = "yyyy-MM-dd"
        let dateStr = dateFormatter.string(from: today)
        label.text = dateStr
        
        return label
    }()
    
    
    
    private var dataSource: UICollectionViewDiffableDataSource<Section, Item>!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .white
        title = "Today"
        setupCollectionView()
    }
    
    private func setupCollectionView() {
        
        view.addSubview(dateLabel)
        view.addSubview(collectionView)
        NSLayoutConstraint.activate([
            
            dateLabel.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 10),
            dateLabel.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            
            
            collectionView.topAnchor.constraint(equalTo: dateLabel.bottomAnchor, constant: 10),
            collectionView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor),
            collectionView.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor),
            collectionView.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor),
        ])
        
        // 3. DataSource 및 기타 설정
        configureDataSource()
        
    }
    
    private func configureDataSource() {
        // 5. DataSource 설정 및 셀 구성
        dataSource = UICollectionViewDiffableDataSource<Section, Item>(collectionView: collectionView) {
            (collectionView, indexPath, item) -> UICollectionViewCell? in
            let cell = collectionView.dequeueReusableCell(withReuseIdentifier: CustomCollectionViewCell.identifier, for: indexPath) as! CustomCollectionViewCell
            cell.configure(with: item.title)
            return cell
        }
        
        applyInitialSnapshots() // 초기 데이터 로드
        
    }
    
    private func applyInitialSnapshots() {
        // 6. 초기 데이터 스냅샷 적용
        var snapshot = NSDiffableDataSourceSnapshot<Section, Item>()
        snapshot.appendSections([.main])
//        snapshot.appendItems([
//            Item(title: "Block 1"),
//        ])
        snapshot.appendItems(Item.initialData)  // Use the static property here

        dataSource.apply(snapshot, animatingDifferences: false)
        

    }
    
    
}

extension MainViewController: UICollectionViewDelegateFlowLayout {
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
        // 현재 스냅샷에서 전체 아이템의 수를 계산
        let itemCount = dataSource.snapshot().numberOfItems
        
        // 각 섹션의 높이를 계산
        let sectionHeight = (collectionView.bounds.height - (2 * CGFloat(itemCount) * 5)) / CGFloat(itemCount)
        
        // 셀의 크기 반환
        return CGSize(width: collectionView.bounds.width, height: sectionHeight)
    }
}

extension MainViewController: UICollectionViewDelegate {
    
    func collectionView(_ collectionView: UICollectionView, didSelectItemAt indexPath: IndexPath) {
        // 현재 스냅샷의 아이템 수
        let currentSnapshot = dataSource.snapshot()
        let itemCount = currentSnapshot.numberOfItems
        // 새로운 아이템 생성 (아이템 개수 + 1)
        let newItem = Item(title: "Block \(itemCount + 1)")
        
        // 새 스냅샷에 아이템 추가
        var newSnapshot = currentSnapshot
        newSnapshot.appendItems([newItem], toSection: .main)
        dataSource.apply(newSnapshot, animatingDifferences: true) {
        }
    }
}



import UIKit

class CustomCollectionViewCell: UICollectionViewCell {
    static let identifier = "CustomCollectionViewCell"
    
    
    lazy var titleLabel: UILabel = {
        let label = UILabel()
        label.textAlignment = .center
        label.textColor = .black
        label.translatesAutoresizingMaskIntoConstraints = false
        return label
    }()
    
    lazy var containerView: UIView = {
        let view = UIView()
        view.translatesAutoresizingMaskIntoConstraints = false
        view.backgroundColor = .systemGray
        view.layer.cornerRadius = 30
        
        return view
    }()
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        contentView.addSubview(containerView)
        containerView.addSubview(titleLabel)
        
        NSLayoutConstraint.activate([
            
            containerView.topAnchor.constraint(equalTo: self.contentView.topAnchor),
            containerView.bottomAnchor.constraint(equalTo: self.contentView.bottomAnchor),
            containerView.leadingAnchor.constraint(equalTo: self.contentView.leadingAnchor, constant: 10),
            containerView.trailingAnchor.constraint(equalTo: self.contentView.trailingAnchor, constant: -10),
            
            titleLabel.centerXAnchor.constraint(equalTo: containerView.centerXAnchor),
            titleLabel.centerYAnchor.constraint(equalTo: containerView.centerYAnchor),
        ])
        
        
        
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    override func prepareForReuse() {
        super.prepareForReuse()
        titleLabel.text = nil // 텍스트 초기화
    }
    
    
    func configure(with title: String) {
        titleLabel.text = title
    }
}


```


## Item 제거 동작 구현 및 텍스트필드 입력단 추가


<img width="300" alt="ezgif-2-e99683b865" src="https://github.com/isGeekCode/TIL/assets/76529148/7f3feeee-e0db-4276-bd0d-09334e5505f5">


```swift


import UIKit

// 1. 데이터 모델 정의
struct Item: Hashable {
    let id = UUID()
    let title: String
    
    // Add this static property
    static let initialData: [Item] = [
        Item(title: "Block 1"),
        Item(title: "Block 2"),
    ]
}

enum Section {
    case main
}

class MainViewController: UIViewController {
    // 2. UICollectionView 및 DataSource 정의
    lazy var collectionView: UICollectionView = {
        let layout = UICollectionViewFlowLayout()
        layout.scrollDirection = .vertical
        layout.sectionInset = UIEdgeInsets(top: 0, left: 0, bottom: 0, right: 0)
        let collectionView = UICollectionView(frame: .zero,
                                              collectionViewLayout: layout)
        collectionView.translatesAutoresizingMaskIntoConstraints = false
        collectionView.delegate = self
        collectionView.register(CustomCollectionViewCell.self, forCellWithReuseIdentifier: CustomCollectionViewCell.identifier)
        return collectionView
    }()
    
    lazy var dateLabel: UILabel = {
        let label = UILabel()
        label.translatesAutoresizingMaskIntoConstraints = false
        let today = Date()
        let dateFormatter = DateFormatter()
        dateFormatter.dateStyle = .none
        dateFormatter.dateFormat = "yyyy-MM-dd"
        let dateStr = dateFormatter.string(from: today)
        label.text = dateStr
        
        return label
    }()
    
    lazy var plusBtn: UIButton = {
        var config = UIButton.Configuration.plain()
        // UIAction 생성
        let action = UIAction { [weak self] _ in
            // 버튼이 탭될 때 실행할 코드
            guard let self else { return }
            checkAddAction()
        }
        let symbolConfig = UIImage.SymbolConfiguration(pointSize: 20, weight: .bold, scale: .large) // 이미지의 크기와 스케일을 조정

        config.image = UIImage(systemName: "plus", withConfiguration: symbolConfig)
        
        let button = UIButton(configuration: config, primaryAction: action)
        button.translatesAutoresizingMaskIntoConstraints = false
        return button
    }()
    
    lazy var minusBtn: UIButton = {
        var config = UIButton.Configuration.plain()
        // UIAction 생성
        let action = UIAction { [weak self] _ in
            // 버튼이 탭될 때 실행할 코드
            guard let self else { return }
            checkMinusAction()
        }
        let symbolConfig = UIImage.SymbolConfiguration(pointSize: 20, weight: .bold, scale: .large) // 이미지의 크기와 스케일을 조정

        config.image = UIImage(systemName: "minus", withConfiguration: symbolConfig)
        
        let button = UIButton(configuration: config, primaryAction: action)
        button.translatesAutoresizingMaskIntoConstraints = false
        return button
    }()
    
    private func toggleButtonColor(targetBtn: UIButton, _ value: Bool) {
        if var config = targetBtn.configuration {
            // 색상을 systemRed로 설정
            let symbolConfig = UIImage.SymbolConfiguration(pointSize: 20, weight: .bold, scale: .large)
            let imageName = targetBtn == plusBtn ? "plus" : "minus"
            config.image = UIImage(systemName: imageName, withConfiguration: symbolConfig)?
                .withTintColor(value ? .systemBlue : .lightGray, renderingMode: .alwaysOriginal)
            targetBtn.configuration = config
        }
    }

    private var dataSource: UICollectionViewDiffableDataSource<Section, Item>!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .white
        title = "Today"
        setupCollectionView()
    }
    
    private func setupCollectionView() {
        
        view.addSubview(dateLabel)
        view.addSubview(minusBtn)
        view.addSubview(plusBtn)
        view.addSubview(collectionView)
        NSLayoutConstraint.activate([
            
            dateLabel.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 10),
            dateLabel.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            
            
            minusBtn.heightAnchor.constraint(equalToConstant: 40),
            minusBtn.widthAnchor.constraint(equalToConstant: 40),
            minusBtn.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor, constant: -10),
            minusBtn.centerYAnchor.constraint(equalTo: dateLabel.centerYAnchor),

            
            plusBtn.heightAnchor.constraint(equalToConstant: 40),
            plusBtn.widthAnchor.constraint(equalToConstant: 40),
            plusBtn.trailingAnchor.constraint(equalTo: minusBtn.leadingAnchor),
            plusBtn.centerYAnchor.constraint(equalTo: dateLabel.centerYAnchor),
            
            
            collectionView.topAnchor.constraint(equalTo: dateLabel.bottomAnchor, constant: 10),
            collectionView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor),
            collectionView.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor),
            collectionView.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor),
        ])
        
        // 3. DataSource 및 기타 설정
        configureDataSource()
    }
    
    private func configureDataSource() {
        // 5. DataSource 설정 및 셀 구성
        dataSource = UICollectionViewDiffableDataSource<Section, Item>(collectionView: collectionView) {
            (collectionView, indexPath, item) -> UICollectionViewCell? in
            let cell = collectionView.dequeueReusableCell(withReuseIdentifier: CustomCollectionViewCell.identifier, for: indexPath) as! CustomCollectionViewCell
            cell.configure(with: item.title)
            return cell
        }
        
        applyInitialSnapshots() // 초기 데이터 로드
        
    }
    
    private func applyInitialSnapshots() {
        // 6. 초기 데이터 스냅샷 적용
        var snapshot = NSDiffableDataSourceSnapshot<Section, Item>()
        snapshot.appendSections([.main])
//        snapshot.appendItems([
//            Item(title: "Block 1"),
//        ])
        snapshot.appendItems(Item.initialData)  // Use the static property here

        dataSource.apply(snapshot, animatingDifferences: false)
    }
    
    /// 마이너스 로직
    private func checkMinusAction() {
        print(#function)
        // 현재 스냅샷의 아이템 수
        let currentSnapshot = dataSource.snapshot()
        let itemCount = currentSnapshot.numberOfItems

        if itemCount >= 2 {
            minusItem()
        }         
    }
    
    /// 마이너스 아이템 및 UI업데이트
    private func minusItem() {
        var currentSnapshot = dataSource.snapshot()

        if !currentSnapshot.itemIdentifiers.isEmpty {
            // Remove the last item
            currentSnapshot.deleteItems([currentSnapshot.itemIdentifiers.last!])

            // Apply the updated snapshot
            dataSource.apply(currentSnapshot, animatingDifferences: true)

            // Additional UI updates (if needed)
            DispatchQueue.main.async {
                let updatedItemCount = self.dataSource.snapshot().numberOfItems
                if updatedItemCount == 1 {
                    self.toggleButtonColor(targetBtn: self.minusBtn, false)
                    self.minusBtn.isEnabled = false
                } 
                
                self.toggleButtonColor(targetBtn: self.plusBtn, true)
                self.plusBtn.isEnabled = true

            }
        }
    }

    
    private func checkAddAction() {
        
        print(#function)

        // 현재 스냅샷의 아이템 수
        let currentSnapshot = dataSource.snapshot()
        let itemCount = currentSnapshot.numberOfItems

        if itemCount < 6 {
            // 새로운 아이템 생성 (아이템 개수 + 1)
            setTextAlert()
        }         
    }
    
    private func setTextAlert() {
        
        
        // Alert Controller 생성
        let alertController = UIAlertController(title: "", message: "블록이름을 입력하세요", preferredStyle: .alert)

        // TextField 추가
        alertController.addTextField { textField in
            textField.placeholder = "제목"
        }

        let addAction = UIAlertAction(title: "추가", style: .default) { [weak self, weak alertController] _ in
            guard let self = self,
                  let alertController = alertController,
                  let textField = alertController.textFields?.first,
                  let text = textField.text, !text.isEmpty else { return }

            // 새 Item 생성 및 추가
            let newItem = Item(title: text)
            self.addNewItem(item: newItem)
        }

        // '취소' 액션
        let cancelAction = UIAlertAction(title: "취소", style: .cancel)

        // 액션을 Alert Controller에 추가
        alertController.addAction(addAction)
        alertController.addAction(cancelAction)

        // Alert 표시
        
        DispatchQueue.main.async {
            self.present(alertController, animated: true)
        }

    }
    
    private func addNewItem(item: Item) {
        // 현재 스냅샷의 아이템 수
        let currentSnapshot = dataSource.snapshot()
        // 새 스냅샷에 아이템 추가
        var newSnapshot = currentSnapshot
        newSnapshot.appendItems([item], toSection: .main)
        dataSource.apply(newSnapshot, animatingDifferences: true) {
            print("된거??")
            
            DispatchQueue.main.async {
                let currentSnapshot = self.dataSource.snapshot()
                print("몇개야 :\(currentSnapshot.numberOfItems)")

                if currentSnapshot.numberOfItems == 6 {
                    self.toggleButtonColor(targetBtn: self.plusBtn, false)
                    self.plusBtn.isEnabled = false
                } 
                
                self.toggleButtonColor(targetBtn: self.minusBtn, true)
                self.minusBtn.isEnabled = true

            }

        }
    }
}

extension MainViewController: UICollectionViewDelegateFlowLayout {
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
        // 현재 스냅샷에서 전체 아이템의 수를 계산
        let itemCount = dataSource.snapshot().numberOfItems
        // 각 섹션의 높이를 계산
        let sectionHeight = (collectionView.bounds.height - (2 * CGFloat(itemCount) * 5)) / CGFloat(itemCount)
        // 셀의 크기 반환
        return CGSize(width: collectionView.bounds.width, height: sectionHeight)
    }
}

extension MainViewController: UICollectionViewDelegate {
    
    func collectionView(_ collectionView: UICollectionView, didSelectItemAt indexPath: IndexPath) {
        print("indexPath: \(indexPath)")
    }
}



import UIKit

class CustomCollectionViewCell: UICollectionViewCell {
    static let identifier = "CustomCollectionViewCell"
    
    
    lazy var titleLabel: UILabel = {
        let label = UILabel()
        label.textAlignment = .center
        label.textColor = .black
        label.translatesAutoresizingMaskIntoConstraints = false
        return label
    }()
    
    lazy var containerView: UIView = {
        let view = UIView()
        view.translatesAutoresizingMaskIntoConstraints = false
        view.backgroundColor = .systemYellow
        view.layer.cornerRadius = 30
        
        return view
    }()
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        contentView.addSubview(containerView)
        containerView.addSubview(titleLabel)
        
        NSLayoutConstraint.activate([
            
            containerView.topAnchor.constraint(equalTo: self.contentView.topAnchor),
            containerView.bottomAnchor.constraint(equalTo: self.contentView.bottomAnchor),
            containerView.leadingAnchor.constraint(equalTo: self.contentView.leadingAnchor, constant: 10),
            containerView.trailingAnchor.constraint(equalTo: self.contentView.trailingAnchor, constant: -10),
            
            titleLabel.centerXAnchor.constraint(equalTo: containerView.centerXAnchor),
            titleLabel.centerYAnchor.constraint(equalTo: containerView.centerYAnchor),
        ])
        
        
        
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    override func prepareForReuse() {
        super.prepareForReuse()
        titleLabel.text = nil // 텍스트 초기화
    }
    
    
    func configure(with title: String) {
        titleLabel.text = title
    }
}

```


```swift
////
////  ViewController.swift
////  CollectionViewApp
////
////  Created by bang_hyeonseok on 12/5/23.
////

import UIKit

// 1. 데이터 모델 정의
struct Item: Hashable {
    let id = UUID()
    let title: String
    
    // Add this static property
    static let initialData: [Item] = [
        Item(title: "Block 1"),
        Item(title: "Block 2"),
    ]
}

enum Section {
    case main
}

// MARK: - ViewController
class MainViewController: UIViewController {
    // 2. UICollectionView 및 DataSource 정의
    lazy var collectionView: UICollectionView = {
        let layout = UICollectionViewFlowLayout()
        layout.scrollDirection = .vertical
        layout.sectionInset = UIEdgeInsets(top: 0, left: 0, bottom: 0, right: 0)
        let collectionView = UICollectionView(frame: .zero,
                                              collectionViewLayout: layout)
        collectionView.translatesAutoresizingMaskIntoConstraints = false
        collectionView.delegate = self
//        collectionView.register(CustomCollectionViewCell.self, forCellWithReuseIdentifier: CustomCollectionViewCell.identifier)
        collectionView.register(CustomCollectionViewListCell.self, forCellWithReuseIdentifier: CustomCollectionViewListCell.identifier)

        return collectionView
    }()
    
    lazy var dateLabel: UILabel = {
        let label = UILabel()
        label.translatesAutoresizingMaskIntoConstraints = false
        let today = Date()
        let dateFormatter = DateFormatter()
        dateFormatter.dateStyle = .none
        dateFormatter.dateFormat = "yyyy-MM-dd"
        let dateStr = dateFormatter.string(from: today)
        label.text = dateStr
        
        return label
    }()
    
    lazy var plusBtn: UIButton = {
        var config = UIButton.Configuration.plain()
        // UIAction 생성
        let action = UIAction { [weak self] _ in
            // 버튼이 탭될 때 실행할 코드
            guard let self else { return }
            checkAddAction()
        }
        let symbolConfig = UIImage.SymbolConfiguration(pointSize: 20, weight: .bold, scale: .large) // 이미지의 크기와 스케일을 조정

        config.image = UIImage(systemName: "plus", withConfiguration: symbolConfig)
        
        let button = UIButton(configuration: config, primaryAction: action)
        button.translatesAutoresizingMaskIntoConstraints = false
        return button
    }()
    
    // 편집 버튼 추가
    lazy var editButton: UIBarButtonItem = {
        let button = UIBarButtonItem(title: "Edit",
                                     style: .plain,
                                     target: self, action: #selector(toggleEditMode))
        return button
    }()

    
    lazy var minusBtn: UIButton = {
        var config = UIButton.Configuration.plain()
        // UIAction 생성
        let action = UIAction { [weak self] _ in
            // 버튼이 탭될 때 실행할 코드
            guard let self else { return }
            checkMinusAction()
        }
        let symbolConfig = UIImage.SymbolConfiguration(pointSize: 20, weight: .bold, scale: .large) // 이미지의 크기와 스케일을 조정

        config.image = UIImage(systemName: "minus", withConfiguration: symbolConfig)
        
        let button = UIButton(configuration: config, primaryAction: action)
        button.translatesAutoresizingMaskIntoConstraints = false
        return button
    }()
    

    private var dataSource: UICollectionViewDiffableDataSource<Section, Item>!
    // 편집 모드 플래그
    var isEditingMode = false

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .white
        title = "Today"
        navigationItem.rightBarButtonItem = editButton
        setupCollectionView()
    }
    
    private func setupCollectionView() {
        
        view.addSubview(dateLabel)
        view.addSubview(plusBtn)
        view.addSubview(collectionView)
        NSLayoutConstraint.activate([
            
            dateLabel.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 10),
            dateLabel.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            
            
            plusBtn.heightAnchor.constraint(equalToConstant: 40),
            plusBtn.widthAnchor.constraint(equalToConstant: 40),
            plusBtn.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor, constant: -10),
            plusBtn.centerYAnchor.constraint(equalTo: dateLabel.centerYAnchor),
            
            collectionView.topAnchor.constraint(equalTo: dateLabel.bottomAnchor, constant: 10),
            collectionView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor),
            collectionView.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor),
            collectionView.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor),
        ])
        
        // 3. DataSource 및 기타 설정
        configureDataSource()
    }
    
    private func configureDataSource() {
        // 5. DataSource 설정 및 셀 구성
        dataSource = UICollectionViewDiffableDataSource<Section, Item>(collectionView: collectionView) {
            (collectionView, indexPath, item) -> UICollectionViewListCell? in
            let cell = collectionView.dequeueReusableCell(withReuseIdentifier: CustomCollectionViewListCell.identifier, for: indexPath) as! CustomCollectionViewListCell
            cell.configure(with: item.title)
            return cell
        }
        
        applyInitialSnapshots() // 초기 데이터 로드
        
    }
    
    private func applyInitialSnapshots() {
        // 6. 초기 데이터 스냅샷 적용
        var snapshot = NSDiffableDataSourceSnapshot<Section, Item>()
        snapshot.appendSections([.main])
        snapshot.appendItems(Item.initialData)  // Use the static property
        dataSource.apply(snapshot, animatingDifferences: false)
    }
    
    @objc private func toggleEditMode() {
        isEditingMode = !isEditingMode
        collectionView.isEditing = isEditingMode
        editButton.title = isEditingMode ? "Done" : "Edit"

        collectionView.performBatchUpdates(nil)

    }

    private func toggleButtonColor(targetBtn: UIButton, _ value: Bool) {
        if var config = targetBtn.configuration {
            // 색상을 systemRed로 설정
            let symbolConfig = UIImage.SymbolConfiguration(pointSize: 20, weight: .bold, scale: .large)
            let imageName = targetBtn == plusBtn ? "plus" : "minus"
            config.image = UIImage(systemName: imageName,
                                   withConfiguration: symbolConfig)?
                .withTintColor(value ? .systemBlue : .lightGray,
                               renderingMode: .alwaysOriginal)
            targetBtn.configuration = config
        }
    }

    /// 마이너스 로직
    private func checkMinusAction() {
        print(#function)
        // 현재 스냅샷의 아이템 수
        let currentSnapshot = dataSource.snapshot()
        let itemCount = currentSnapshot.numberOfItems

        if itemCount >= 2 {
            setDeleteAlert()
        }         
    }
    
    /// 마이너스 아이템 및 UI업데이트
    private func minusItem() {
        var currentSnapshot = dataSource.snapshot()

        if !currentSnapshot.itemIdentifiers.isEmpty {
            // Remove the last item
            currentSnapshot.deleteItems([currentSnapshot.itemIdentifiers.last!])

            // Apply the updated snapshot
            dataSource.apply(currentSnapshot, animatingDifferences: true)

            // Additional UI updates (if needed)
            DispatchQueue.main.async {
                let updatedItemCount = self.dataSource.snapshot().numberOfItems
                if updatedItemCount == 1 {
                    self.toggleButtonColor(targetBtn: self.minusBtn, false)
                    self.minusBtn.isEnabled = false
                } 
                
                self.toggleButtonColor(targetBtn: self.plusBtn, true)
                self.plusBtn.isEnabled = true

            }
        }
    }

    
    private func checkAddAction() {
        
        print(#function)
        // 현재 스냅샷의 아이템 수
        let currentSnapshot = dataSource.snapshot()
        let itemCount = currentSnapshot.numberOfItems

        if itemCount < 6 {
            // 새로운 아이템 생성 (아이템 개수 + 1)
            setTextAlert()
        }         
    }
    
    private func setTextAlert() {
        
        // Alert Controller 생성
        let alertController = UIAlertController(title: "", message: "블록이름을 입력하세요", preferredStyle: .alert)

        // TextField 추가
        alertController.addTextField { textField in
            textField.placeholder = "제목"
        }

        let addAction = UIAlertAction(title: "확인", style: .default) { [weak self, weak alertController] _ in
            guard let self = self,
                  let alertController = alertController,
                  let textField = alertController.textFields?.first,
                  let text = textField.text, !text.isEmpty else { return }

            // 새 Item 생성 및 추가
            let newItem = Item(title: text)
            self.addNewItem(item: newItem)
        }

        // '취소' 액션
        let cancelAction = UIAlertAction(title: "취소", style: .destructive)

        alertController.addAction(cancelAction)
        alertController.addAction(addAction)

        // Alert 표시
        
        DispatchQueue.main.async {
            self.present(alertController, animated: true)
        }
    }
    
    private func setDeleteAlert() {
        // Alert Controller 생성
        let alertController = UIAlertController(title: "", message: "정말로 삭제하시겠습니까", preferredStyle: .alert)

        let addAction = UIAlertAction(title: "확인", style: .default) { [weak self] _ in
            guard let self else { return }
            minusItem()
        }

        // '취소' 액션
        let cancelAction = UIAlertAction(title: "취소", style: .destructive)

        alertController.addAction(cancelAction)
        alertController.addAction(addAction)

        // Alert 표시
        
        DispatchQueue.main.async {
            self.present(alertController, animated: true)
        }

    }
    
    private func addNewItem(item: Item) {
        // 현재 스냅샷의 아이템 수
        let currentSnapshot = dataSource.snapshot()
        // 새 스냅샷에 아이템 추가
        var newSnapshot = currentSnapshot
        newSnapshot.appendItems([item], toSection: .main)
        dataSource.apply(newSnapshot, animatingDifferences: true) {
            
            DispatchQueue.main.async {
                let currentSnapshot = self.dataSource.snapshot()
                print("몇개야 :\(currentSnapshot.numberOfItems)")

                if currentSnapshot.numberOfItems == 6 {
                    self.toggleButtonColor(targetBtn: self.plusBtn, false)
                    self.plusBtn.isEnabled = false
                } 
                
                self.toggleButtonColor(targetBtn: self.minusBtn, true)
                self.minusBtn.isEnabled = true

            }

        }
    }
}

extension MainViewController: UICollectionViewDelegateFlowLayout {
 
    
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
        // 현재 스냅샷에서 전체 아이템의 수를 계산
        let itemCount = dataSource.snapshot().numberOfItems
        // 각 섹션의 높이를 계산
        let sectionHeight = (collectionView.bounds.height - (2 * CGFloat(itemCount) * 5)) / CGFloat(itemCount)
        // 셀의 크기 반환
        return CGSize(width: collectionView.bounds.width, height: sectionHeight)
    }
}

extension MainViewController: UICollectionViewDelegate {
    
    func collectionView(_ collectionView: UICollectionView, didSelectItemAt indexPath: IndexPath) {
        print("indexPath: \(indexPath)")
        if let cell = collectionView.cellForItem(at: indexPath) as? CustomCollectionViewListCell {
//            cell.isSelected = false // 셀의 선택 상태 해제
            print("cell.isSelected: \(cell.isSelected)")
            cell.backgroundColor = .clear
        }

        
    }
    
    func collectionView(_ collectionView: UICollectionView, canEditItemAt indexPath: IndexPath) -> Bool {
        // 모든 셀이 편집 가능하게 설정
        return true
    }

    func collectionView(_ collectionView: UICollectionView, commit editingStyle: UITableViewCell.EditingStyle, forItemAt indexPath: IndexPath) {
        if editingStyle == .delete {
            // 셀 삭제 로직 구현
            var snapshot = dataSource.snapshot()
            if let item = dataSource.itemIdentifier(for: indexPath) {
                snapshot.deleteItems([item])
                dataSource.apply(snapshot)
            }
        }
    }
}



class CustomCollectionViewListCell: UICollectionViewListCell {
    static let identifier = "CustomCollectionViewListCell"

    lazy var titleLabel: UILabel = {
        let label = UILabel()
        label.textAlignment = .center
        label.textColor = .black
        label.translatesAutoresizingMaskIntoConstraints = false
        return label
    }()
    
    lazy var containerView: UIView = {
        let view = UIView()
        view.translatesAutoresizingMaskIntoConstraints = false
        view.backgroundColor = .systemGray5
        view.layer.cornerRadius = 30
        
        return view
    }()
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        self.backgroundColor = .clear
        contentView.addSubview(containerView)
        containerView.addSubview(titleLabel)
        print("되는거야2")

        NSLayoutConstraint.activate([

            containerView.topAnchor.constraint(equalTo: self.contentView.topAnchor),
            containerView.bottomAnchor.constraint(equalTo: self.contentView.bottomAnchor),
            containerView.leadingAnchor.constraint(equalTo: self.contentView.leadingAnchor, constant: 10),
            containerView.trailingAnchor.constraint(equalTo: self.contentView.trailingAnchor, constant: -10),
            
            titleLabel.centerXAnchor.constraint(equalTo: containerView.centerXAnchor),
            titleLabel.centerYAnchor.constraint(equalTo: containerView.centerYAnchor),
        ])
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    override func prepareForReuse() {
        super.prepareForReuse()
        titleLabel.text = nil // 텍스트 초기화
    }
    
    
    func configure(with title: String) {
        titleLabel.text = title
    }
    
    override func updateConfiguration(using state: UICellConfigurationState) {
        super.updateConfiguration(using: state)

        // 편집 모드에 따라 액세서리 설정
        if state.isEditing {
            // 편집 모드일 때 삭제 버튼을 표시
            accessories = [.delete(displayed: .whenEditing, actionHandler: { [weak self] in
                // 삭제 로직 구현
                self?.handleDeleteAction()
            })]
        } else {
            // 편집 모드가 아닐 때는 액세서리 제거
            accessories = []
        }
    }
    
    private func handleDeleteAction() {
        
        print(#function)
        // 삭제 처리 로직
    }


}

```



## Editing모드 - delete 구현

```swift

// 1. 데이터 모델 정의
struct Item: Hashable {
    let id = UUID()
    let title: String
    
    // Add this static property
    static let initialData: [Item] = [
        Item(title: "Block 1"),
        Item(title: "Block 2"),
    ]
}

enum Section {
    case main
}

class MainTabBarController: UITabBarController {

    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.tabBar.backgroundColor = UIColor.systemGray6 

        
        let todayVC = UINavigationController(rootViewController: MainViewController()) 
        let calendarVC = UINavigationController(rootViewController: MainViewController()) 
        let settingVC = UINavigationController(rootViewController: MainViewController()) 

        // UIKit, SwiftUI
        todayVC.tabBarItem = UITabBarItem(title: "오늘",
                                                  image: UIImage(systemName: "house.fill"),
                                                  selectedImage: nil)
        // Networking,
        calendarVC.tabBarItem = UITabBarItem(title: "달력",
                                                  image: UIImage(systemName: "square.grid.3x3.fill"),
                                                  selectedImage: nil)
        settingVC.tabBarItem = UITabBarItem(title: "설정",
                                                  image: UIImage(systemName: "gear"),
                                                  selectedImage: nil)


        self.viewControllers = [
            todayVC,
            calendarVC,
            settingVC,
        ]
    }
}




// MARK: - ViewController
class MainViewController: UIViewController {
    
    // MARK: - Var
    private var dataSource: UICollectionViewDiffableDataSource<Section, Item>!
    // 편집 모드 플래그
    var isEditingMode = false

    // MARK: - UIComponents
    // 2. UICollectionView 및 DataSource 정의
    lazy var collectionView: UICollectionView = {
        let layout = UICollectionViewFlowLayout()
        layout.scrollDirection = .vertical
        layout.sectionInset = UIEdgeInsets(top: 0, left: 0, bottom: 0, right: 0)
        let collectionView = UICollectionView(frame: .zero,
                                              collectionViewLayout: layout)
        collectionView.translatesAutoresizingMaskIntoConstraints = false
        collectionView.delegate = self
//        collectionView.register(CustomCollectionViewCell.self, forCellWithReuseIdentifier: CustomCollectionViewCell.identifier)
        collectionView.register(CustomCollectionViewListCell.self, forCellWithReuseIdentifier: CustomCollectionViewListCell.identifier)
    
        return collectionView
    }()
    
    lazy var dateLabel: UILabel = {
        let label = UILabel()
        label.translatesAutoresizingMaskIntoConstraints = false
        let today = Date()
        let dateFormatter = DateFormatter()
        dateFormatter.dateStyle = .none
        dateFormatter.dateFormat = "yyyy-MM-dd"
        let dateStr = dateFormatter.string(from: today)
        label.text = dateStr
        
        return label
    }()
    

    lazy var plusButton: UIBarButtonItem = {
        let action = UIAction { [weak self] _ in
            // 버튼이 탭될 때 실행할 코드
            self?.checkAddAction()
        }
        return UIBarButtonItem(systemItem: .add, primaryAction: action)
    }()
    
    // 편집 버튼 추가
    lazy var editButton: UIBarButtonItem = {
        let button = UIBarButtonItem(title: "Edit",
                                     style: .plain,
                                     target: self,
                                     action: #selector(toggleEditMode))
        return button
    }()

    // TODO: 삭제필요
    lazy var minusBtn: UIButton = {
        var config = UIButton.Configuration.plain()
        // UIAction 생성
        let action = UIAction { [weak self] _ in
            // 버튼이 탭될 때 실행할 코드
            guard let self else { return }
            checkMinusAction()
        }
        let symbolConfig = UIImage.SymbolConfiguration(pointSize: 20, weight: .bold, scale: .large) 
        config.image = UIImage(systemName: "minus", withConfiguration: symbolConfig)
        
        let button = UIButton(configuration: config, primaryAction: action)
        button.translatesAutoresizingMaskIntoConstraints = false
        return button
    }()


    
    private func updatePlusButtonState() {
        let itemCount = dataSource.snapshot().numberOfItems
        if itemCount >= 6 {
            plusButton.tintColor = .lightGray
            plusButton.isEnabled = false
        } else {
            plusButton.tintColor = .systemBlue
            plusButton.isEnabled = true
        }
    }    

    // MARK: - Functions
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .white
        title = "Today"
        navigationItem.rightBarButtonItems = [editButton, plusButton]
        setupCollectionView()
        updatePlusButtonState()
    }
    
    private func setupCollectionView() {
        
        view.addSubview(dateLabel)
        view.addSubview(collectionView)
        NSLayoutConstraint.activate([
            
            dateLabel.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 10),
            dateLabel.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
                        
            collectionView.topAnchor.constraint(equalTo: dateLabel.bottomAnchor, constant: 10),
            collectionView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor),
            collectionView.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor),
            collectionView.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor),
        ])
        
        // 3. DataSource 및 기타 설정
        configureDataSource()
    }
    
    private func configureDataSource() {
        // 5. DataSource 설정 및 셀 구성
        dataSource = UICollectionViewDiffableDataSource<Section, Item>(collectionView: collectionView) {
            (collectionView, indexPath, item) -> UICollectionViewListCell? in
            let cell = collectionView.dequeueReusableCell(withReuseIdentifier: CustomCollectionViewListCell.identifier, for: indexPath) as! CustomCollectionViewListCell
            cell.configure(with: item.title)
            cell.delegate = self
            let view = UIView()
            view.backgroundColor = .clear
            cell.selectedBackgroundView = view
            return cell
        }
        
        applyInitialSnapshots() // 초기 데이터 로드
        
    }
    
    private func applyInitialSnapshots() {
        // 6. 초기 데이터 스냅샷 적용
        var snapshot = NSDiffableDataSourceSnapshot<Section, Item>()
        snapshot.appendSections([.main])
        snapshot.appendItems(Item.initialData)  // Use the static property
        dataSource.apply(snapshot, animatingDifferences: false)
    }
    
    @objc private func toggleEditMode() {
        collectionView.isEditing.toggle()
        editButton.title = collectionView.isEditing ? "Done" : "Edit"
        collectionView.performBatchUpdates(nil)
    }

    private func toggleButtonColor(targetBtn: UIButton, _ value: Bool) {
        if var config = targetBtn.configuration {
            // 색상을 systemRed로 설정
            let symbolConfig = UIImage.SymbolConfiguration(pointSize: 20, weight: .bold, scale: .large)
//            let imageName = targetBtn == plusBtn ? "plus" : "minus"
            guard let btnImage = UIImage(systemName: "plus",
                                         withConfiguration: symbolConfig) else { return }
            btnImage.withTintColor(value ? .systemBlue : .lightGray, 
                                   renderingMode: .alwaysOriginal)
            config.image =  btnImage
            targetBtn.configuration = config
        }
    }

    /// 마이너스 로직
    private func checkMinusAction() {
        print(#function)
        // 현재 스냅샷의 아이템 수
        let currentSnapshot = dataSource.snapshot()
        let itemCount = currentSnapshot.numberOfItems

        if itemCount >= 2 {
            setDeleteAlert()
        }         
    }
    
    /// 마이너스 아이템 및 UI업데이트
    private func minusItem() {
        var currentSnapshot = dataSource.snapshot()

        if !currentSnapshot.itemIdentifiers.isEmpty {
            // Remove the last item
            currentSnapshot.deleteItems([currentSnapshot.itemIdentifiers.last!])

            // Apply the updated snapshot
            dataSource.apply(currentSnapshot, animatingDifferences: true) {
                self.updatePlusButtonState() // 셀 삭제 후 plusButton 상태 업데이트
            }
        }
    }

    
    private func checkAddAction() {
        
        print(#function)
        // 현재 스냅샷의 아이템 수
        let currentSnapshot = dataSource.snapshot()
        let itemCount = currentSnapshot.numberOfItems

        if itemCount < 6 {
            // 새로운 아이템 생성 (아이템 개수 + 1)
            setTextAlert()
        }         
    }
    
    private func setTextAlert() {
        
        // Alert Controller 생성
        let alertController = UIAlertController(title: "", message: "블록이름을 입력하세요", preferredStyle: .alert)

        // TextField 추가
        alertController.addTextField { textField in
            textField.placeholder = "제목"
        }

        let addAction = UIAlertAction(title: "확인", style: .default) { [weak self, weak alertController] _ in
            guard let self = self,
                  let alertController = alertController,
                  let textField = alertController.textFields?.first,
                  let text = textField.text, !text.isEmpty else { return }

            // 새 Item 생성 및 추가
            let newItem = Item(title: text)
            self.addNewItem(item: newItem)
        }

        // '취소' 액션
        let cancelAction = UIAlertAction(title: "취소", style: .destructive)

        alertController.addAction(cancelAction)
        alertController.addAction(addAction)

        // Alert 표시
        
        DispatchQueue.main.async {
            self.present(alertController, animated: true)
        }
    }
    
    private func setDeleteAlert() {
        // Alert Controller 생성
        let alertController = UIAlertController(title: "", message: "정말로 삭제하시겠습니까", preferredStyle: .alert)

        let addAction = UIAlertAction(title: "확인", style: .default) { [weak self] _ in
            guard let self else { return }
            minusItem()
        }

        // '취소' 액션
        let cancelAction = UIAlertAction(title: "취소", style: .destructive)

        alertController.addAction(cancelAction)
        alertController.addAction(addAction)

        // Alert 표시
        
        DispatchQueue.main.async {
            self.present(alertController, animated: true)
        }

    }
    
    private func addNewItem(item: Item) {
        // 현재 스냅샷의 아이템 수
        let currentSnapshot = dataSource.snapshot()
        // 새 스냅샷에 아이템 추가
        var newSnapshot = currentSnapshot
        newSnapshot.appendItems([item], toSection: .main)
        dataSource.apply(newSnapshot, animatingDifferences: true) {
            self.updatePlusButtonState()
        }
    }
}

extension MainViewController: UICollectionViewDelegateFlowLayout {
 
    
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
        // 현재 스냅샷에서 전체 아이템의 수를 계산
        let itemCount = dataSource.snapshot().numberOfItems
        // 각 섹션의 높이를 계산
        let sectionHeight = (collectionView.bounds.height - (2 * CGFloat(itemCount) * 5)) / CGFloat(itemCount)
        // 셀의 크기 반환
        return CGSize(width: collectionView.bounds.width, height: sectionHeight)
    }
    
//    func collectionView(_ collectionView: UICollectionView, shouldHighlightItemAt indexPath: IndexPath) -> Bool {
//        return false
//    }

}

extension MainViewController: UICollectionViewDelegate {
    
    func collectionView(_ collectionView: UICollectionView, didSelectItemAt indexPath: IndexPath) {
        print("indexPath: \(indexPath)")
        if let cell = collectionView.cellForItem(at: indexPath) as? CustomCollectionViewListCell {
//            cell.isSelected = false // 셀의 선택 상태 해제
//            cell.isHighlighted = false
            print("cell.isSelected: \(cell.isSelected)")
//            cell.backgroundColor = .clear
            print("cell.isHighlighted: \(cell.isHighlighted)")

        }

        
    }    
}


extension MainViewController: CustomCollectionViewListCellDelegate {
    func deleteItem(cell: CustomCollectionViewListCell) {
        guard let indexPath = collectionView.indexPath(for: cell),
              let item = dataSource.itemIdentifier(for: indexPath) else { return }

        var snapshot = dataSource.snapshot()
        snapshot.deleteItems([item])
        dataSource.apply(snapshot, animatingDifferences: true)
    }
}

protocol CustomCollectionViewListCellDelegate: AnyObject {
    func deleteItem(cell: CustomCollectionViewListCell)
}

class CustomCollectionViewListCell: UICollectionViewListCell {
    static let identifier = "CustomCollectionViewListCell"
    weak var delegate: CustomCollectionViewListCellDelegate?

    override var isSelected: Bool {
        didSet {
            print(#function)
        }
    }
    
    
    lazy var titleLabel: UILabel = {
        let label = UILabel()
        label.textAlignment = .center
        label.textColor = .black
        label.translatesAutoresizingMaskIntoConstraints = false
        return label
    }()
    
    lazy var containerView: UIView = {
        let view = UIView()
        view.translatesAutoresizingMaskIntoConstraints = false
        view.backgroundColor = .systemGray5
        view.layer.cornerRadius = 30
        
        return view
    }()
    
    override init(frame: CGRect) {
        super.init(frame: frame)
//        self.backgroundColor = .clear
        contentView.addSubview(containerView)
        containerView.addSubview(titleLabel)
        print("되는거야2")

        NSLayoutConstraint.activate([

            containerView.topAnchor.constraint(equalTo: self.contentView.topAnchor),
            containerView.bottomAnchor.constraint(equalTo: self.contentView.bottomAnchor),
            containerView.leadingAnchor.constraint(equalTo: self.contentView.leadingAnchor, constant: 10),
            containerView.trailingAnchor.constraint(equalTo: self.contentView.trailingAnchor, constant: -10),
            
            titleLabel.centerXAnchor.constraint(equalTo: containerView.centerXAnchor),
            titleLabel.centerYAnchor.constraint(equalTo: containerView.centerYAnchor),
        ])
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    override func prepareForReuse() {
        super.prepareForReuse()
        titleLabel.text = nil // 텍스트 초기화
    }
    
    
    func configure(with title: String) {
        titleLabel.text = title
    }
    
    override func updateConfiguration(using state: UICellConfigurationState) {
        super.updateConfiguration(using: state)
        
        // 편집 모드에 따라 액세서리 설정
        if state.isEditing {
            // 편집 모드일 때 삭제 버튼을 표시
//            accessories = [.delete(displayed: .whenEditing,
//                                   actionHandler: { [weak self] in
//                guard let self = self else { return }
//                // 삭제 로직 구현
//                self.delegate?.deleteItem(cell: self)
//            })]
            
            // delete 액션
            let deleteAction = UICellAccessory.delete(displayed: .whenEditing) { [weak self] in
                print("deleteAction")
                guard let self = self else { return }
                self.delegate?.deleteItem(cell: self)

            }
            let reorderAction = UICellAccessory.reorder(displayed: .always,
                                                        options: .init(showsVerticalSeparator: false))
            accessories = [deleteAction, reorderAction ]

        } else {
            // 편집 모드가 아닐 때는 액세서리 제거
            accessories = []
        }
    }
}

    
```

## Reorder 구현
리스트를 드래그해서 순서를 변경하는 것은 굉장히 흔한 경험이다.  

```swift

// MARK: - ViewController
class MainViewController: UIViewController {
    
    // MARK: - Var
    private var dataSource: UICollectionViewDiffableDataSource<Section, Item>!
    // 편집 모드 플래그
    var isEditingMode = false

    // MARK: - UIComponents
    // 2. UICollectionView 및 DataSource 정의
    lazy var collectionView: UICollectionView = {
        let layout = UICollectionViewFlowLayout()
        layout.scrollDirection = .vertical
        layout.sectionInset = UIEdgeInsets(top: 0, left: 0, bottom: 0, right: 0)
        let collectionView = UICollectionView(frame: .zero,
                                              collectionViewLayout: layout)
        collectionView.translatesAutoresizingMaskIntoConstraints = false
        collectionView.delegate = self
        collectionView.register(CustomCollectionViewListCell.self, forCellWithReuseIdentifier: CustomCollectionViewListCell.identifier)
    
        return collectionView
    }()
    
    lazy var dateLabel: UILabel = {
        let label = UILabel()
        label.translatesAutoresizingMaskIntoConstraints = false
        let today = Date()
        let dateFormatter = DateFormatter()
        dateFormatter.dateStyle = .none
        dateFormatter.dateFormat = "yyyy-MM-dd"
        let dateStr = dateFormatter.string(from: today)
        label.text = dateStr
        
        return label
    }()
    

    lazy var plusButton: UIBarButtonItem = {
        let action = UIAction { [weak self] _ in
            // 버튼이 탭될 때 실행할 코드
            self?.checkAddAction()
        }
        return UIBarButtonItem(systemItem: .add, primaryAction: action)
    }()
    
    // 편집 버튼 추가
    lazy var editButton: UIBarButtonItem = {
        let button = UIBarButtonItem(title: "Edit",
                                     style: .plain,
                                     target: self,
                                     action: #selector(toggleEditMode))
        return button
    }()


    
    private func updatePlusButtonState() {
        let itemCount = dataSource.snapshot().numberOfItems
        if itemCount >= 6 {
            plusButton.tintColor = .lightGray
            plusButton.isEnabled = false
        } else {
            plusButton.tintColor = .systemBlue
            plusButton.isEnabled = true
        }
    }    
    
    private func updateAllButtonStates() {
        let snapshot = dataSource.snapshot()
        let itemCount = snapshot.numberOfItems

        
        let isPlusBtnEnable = itemCount < 6
        let isEditBtnEnable = !(itemCount == 1 && snapshot.itemIdentifiers.first == Item.tutorialItem)

        configureButtonAppearance(button: plusButton, isEnabled: isPlusBtnEnable)
        configureButtonAppearance(button: editButton, isEnabled: isEditBtnEnable)
    }



    private func configureButtonAppearance(button: UIBarButtonItem, isEnabled: Bool) {
        button.isEnabled = isEnabled
        button.tintColor = isEnabled ? .systemBlue : .lightGray
    }

    
    // MARK: - Functions
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .white
        title = "Today"
        navigationItem.rightBarButtonItems = [editButton, plusButton]
        setupCollectionView()
        collectionView.dragDelegate = self
        collectionView.dropDelegate = self
        collectionView.dragInteractionEnabled = true
        loadItems()

        // 저장된 데이터가 없으면 초기 데이터 로드
        if dataSource.snapshot().numberOfItems == 0 {
            applyInitialSnapshots()
        } 
        updateAllButtonStates() 
    }
    
    private func setupCollectionView() {
        
        view.addSubview(dateLabel)
        view.addSubview(collectionView)
        NSLayoutConstraint.activate([
            
            dateLabel.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 10),
            dateLabel.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
                        
            collectionView.topAnchor.constraint(equalTo: dateLabel.bottomAnchor, constant: 10),
            collectionView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor),
            collectionView.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor),
            collectionView.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor),
        ])
        
        // 3. DataSource 및 기타 설정
        configureDataSource()
    }
    
    private func configureDataSource() {
        // 5. DataSource 설정 및 셀 구성
        dataSource = UICollectionViewDiffableDataSource<Section, Item>(collectionView: collectionView) {
            (collectionView, indexPath, item) -> UICollectionViewListCell? in
            let cell = collectionView.dequeueReusableCell(withReuseIdentifier: CustomCollectionViewListCell.identifier, for: indexPath) as! CustomCollectionViewListCell
            cell.configure(with: item.title)
            cell.delegate = self
            let view = UIView()
            view.backgroundColor = .clear
            cell.selectedBackgroundView = view
            return cell
        }
        
    }
    
    
    @objc private func toggleEditMode() {
        collectionView.isEditing.toggle()
        editButton.title = collectionView.isEditing ? "Done" : "Edit"
        collectionView.performBatchUpdates(nil)
    }
    
    private func checkAddAction() {
        
        print(#function)
        // 현재 스냅샷의 아이템 수
        let currentSnapshot = dataSource.snapshot()
        let itemCount = currentSnapshot.numberOfItems

         
        if itemCount == 1,
           let firstItem = currentSnapshot.itemIdentifiers.first,
           firstItem.title == Item.initialMessage {
            // 첫 번째 아이템이 "내용을 추가해주세요" 메시지일 때 새 아이템 추가
            setTextAlert(isFirstItem: true)
        } else {
            // 기존 로직
            setTextAlert(isFirstItem: false)
        }

    }
    
    private func setTextAlert(isFirstItem: Bool) {
        
        // Alert Controller 생성
        let alertController = UIAlertController(title: "", message: "블록이름을 입력하세요", preferredStyle: .alert)

        // TextField 추가
        alertController.addTextField { textField in
            textField.placeholder = "제목"
        }

        let addAction = UIAlertAction(title: "확인", style: .default) { [weak self, weak alertController] _ in
            guard let self = self,
                  let alertController = alertController,
                  let textField = alertController.textFields?.first,
                  let text = textField.text, !text.isEmpty else { return }

            guard let todayStr = dateLabel.text else { return }
            if isFirstItem {
                // 새 Item 생성 및 추가
                let newItem = Item(title: text, date: todayStr)
                self.addNewItem(item: newItem, replacingFirstItem: true)

            } else {
                // 새 Item 생성 및 추가
                let newItem = Item(title: text, date: todayStr)
                self.addNewItem(item: newItem)
            }
        }

        // '취소' 액션
        let cancelAction = UIAlertAction(title: "취소", style: .destructive)

        alertController.addAction(cancelAction)
        alertController.addAction(addAction)

        // Alert 표시
        
        DispatchQueue.main.async {
            self.present(alertController, animated: true)
        }
    }
    
    private func presentDeleteAlert(completionHandler: @escaping () -> Void) {
        
        let alertController = UIAlertController(title: "", message: "정말로 삭제하시겠습니까", preferredStyle: .alert)

        let deleteAction = UIAlertAction(title: "확인", style: .default) { _ in
            completionHandler()
        }

        let cancelAction = UIAlertAction(title: "취소", style: .destructive)

        alertController.addAction(cancelAction)
        alertController.addAction(deleteAction)

        DispatchQueue.main.async {
            self.present(alertController, animated: true)
        }

    }

    
    private func addNewItem(item: Item, replacingFirstItem: Bool = false) {
        var newSnapshot = dataSource.snapshot()
        if replacingFirstItem {
            newSnapshot.deleteItems([newSnapshot.itemIdentifiers.first!])
        }
        newSnapshot.appendItems([item], toSection: .main)
        dataSource.apply(newSnapshot, animatingDifferences: true) {
            self.updateAllButtonStates()
            self.saveItems()
        }
    }
    
    
    // MARK: Data Save & Load
    private func saveItems() {
        print(#function)
        
        let currentSnapshot = dataSource.snapshot()
        let items = currentSnapshot.itemIdentifiers
        // 아이템 저장
        if let encoded = try? JSONEncoder().encode(items) {
            UserDefaults.standard.set(encoded, forKey: "savedItems")
        }

        // 날짜별 존재 여부 저장
        // 동일 날짜 중복방지를 위해 Set 사용
        var datesWithItems = Set<String>()
        items.forEach { datesWithItems.insert($0.date) }
        UserDefaults.standard.set(Array(datesWithItems), forKey: "datesWithItems")
    }

    private func loadItems() {
        print(#function)
        if let savedItems = UserDefaults.standard.object(forKey: "savedItems") as? Data {
            if let decodedItems = try? JSONDecoder().decode([Item].self, from: savedItems) {
                var snapshot = NSDiffableDataSourceSnapshot<Section, Item>()
                snapshot.appendSections([.main])
                snapshot.appendItems(decodedItems)
                dataSource.apply(snapshot, animatingDifferences: false)
            }
        }
    }
    
    private func applyInitialSnapshots() {
        print(#function)
        var snapshot = NSDiffableDataSourceSnapshot<Section, Item>()
        snapshot.appendSections([.main])

        guard let todayStr = dateLabel.text else { return }
        let tutorialItem = Item(title: Item.initialMessage, date: todayStr)
        snapshot.appendItems([tutorialItem])
        
        dataSource.apply(snapshot, animatingDifferences: false)
    }


}

extension MainViewController: UICollectionViewDelegateFlowLayout {
 
    
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
        // 현재 스냅샷에서 전체 아이템의 수를 계산
        let itemCount = dataSource.snapshot().numberOfItems
        // 각 섹션의 높이를 계산
        let sectionHeight = (collectionView.bounds.height - (2 * CGFloat(itemCount) * 5)) / CGFloat(itemCount)
        // 셀의 크기 반환
        return CGSize(width: collectionView.bounds.width, height: sectionHeight)
    }
}

extension MainViewController: UICollectionViewDelegate {
    
    func collectionView(_ collectionView: UICollectionView, didSelectItemAt indexPath: IndexPath) {
        print("indexPath: \(indexPath)")
        if let cell = collectionView.cellForItem(at: indexPath) as? CustomCollectionViewListCell {
            
        }
    }
}

extension MainViewController: UICollectionViewDragDelegate, UICollectionViewDropDelegate {
    func collectionView(_ collectionView: UICollectionView, itemsForBeginning session: UIDragSession, at indexPath: IndexPath) -> [UIDragItem] {
        
        guard let item = dataSource.itemIdentifier(for: indexPath) else { return [] }
        let itemProvider = NSItemProvider(object: item.id.uuidString as NSString)
        let dragItem = UIDragItem(itemProvider: itemProvider)
        dragItem.localObject = item
        return [dragItem]
    }
    
    func collectionView(_ collectionView: UICollectionView, canHandle session: UIDropSession) -> Bool {
        return true

//        return session.canLoadObjects(ofClass: NSString.self)
    }

    func collectionView(_ collectionView: UICollectionView, dropSessionDidUpdate session: UIDropSession, withDestinationIndexPath destinationIndexPath: IndexPath?) -> UICollectionViewDropProposal {
        return UICollectionViewDropProposal(operation: .move,
                                            intent: .insertAtDestinationIndexPath)
    }
    
    func collectionView(_ collectionView: UICollectionView, performDropWith coordinator: UICollectionViewDropCoordinator) {

        guard let destinationIndexPath = coordinator.destinationIndexPath,
              let item = coordinator.items.first,
              let sourceIndexPath = item.sourceIndexPath else {
            return
        }


        // 스냅샷을 가져옴
        var snapshot = dataSource.snapshot()

        // 해당 아이템을 식별
        guard let identifier = dataSource.itemIdentifier(for: sourceIndexPath) else {
            return
        }

        // 스냅샷에서 아이템을 삭제 및 새 위치에 삽입
        snapshot.deleteItems([identifier])
        if let destinationIdentifier = dataSource.itemIdentifier(for: destinationIndexPath) {
            snapshot.insertItems([identifier], beforeItem: destinationIdentifier)
        } else {
            snapshot.appendItems([identifier], toSection: .main)
        }

        // 스냅샷을 적용
        dataSource.apply(snapshot, animatingDifferences: true) {
            self.saveItems()
        }
        
    }
}


extension MainViewController: CustomCollectionViewListCellDelegate {
    
    func deleteItem(cell: CustomCollectionViewListCell) {

        presentDeleteAlert { [weak self] in
            self?.performDeletion(cell)
        }
    }
    
    private func performDeletion(_ cell: CustomCollectionViewListCell) {
        guard let indexPath = collectionView.indexPath(for: cell),
              let item = dataSource.itemIdentifier(for: indexPath) else { return }

        var snapshot = dataSource.snapshot()
        
        if snapshot.numberOfItems == 1 {
            // 마지막 아이템 삭제 시, 튜토리얼 아이템 추가 및 편집 모드 종료

            snapshot.deleteItems([item])
            snapshot.appendItems([Item.tutorialItem], toSection: .main)
            
            collectionView.isEditing = false // 편집 모드 종료
            editButton.title = "Edit" // 버튼 타이틀 변경

        } else {
            snapshot.deleteItems([item])
        }

        dataSource.apply(snapshot, animatingDifferences: true) {
            self.updateAllButtonStates()
            self.saveItems()
        }
    }

}

protocol CustomCollectionViewListCellDelegate: AnyObject {
    func deleteItem(cell: CustomCollectionViewListCell)
}

class CustomCollectionViewListCell: UICollectionViewListCell {
    static let identifier = "CustomCollectionViewListCell"
    weak var delegate: CustomCollectionViewListCellDelegate?

    override var isSelected: Bool {
        didSet {
            print(#function)
        }
    }
    
    
    lazy var titleLabel: UILabel = {
        let label = UILabel()
        label.textAlignment = .center
        label.textColor = .black
        label.translatesAutoresizingMaskIntoConstraints = false
        return label
    }()
    
    lazy var containerView: UIView = {
        let view = UIView()
        view.translatesAutoresizingMaskIntoConstraints = false
        view.backgroundColor = .systemGray5
        view.layer.cornerRadius = 30
        
        return view
    }()
    
    override init(frame: CGRect) {
        super.init(frame: frame)
//        self.backgroundColor = .clear
        contentView.addSubview(containerView)
        containerView.addSubview(titleLabel)

        NSLayoutConstraint.activate([

            containerView.topAnchor.constraint(equalTo: self.contentView.topAnchor),
            containerView.bottomAnchor.constraint(equalTo: self.contentView.bottomAnchor),
            containerView.leadingAnchor.constraint(equalTo: self.contentView.leadingAnchor, constant: 10),
            containerView.trailingAnchor.constraint(equalTo: self.contentView.trailingAnchor, constant: -10),
            
            titleLabel.centerXAnchor.constraint(equalTo: containerView.centerXAnchor),
            titleLabel.centerYAnchor.constraint(equalTo: containerView.centerYAnchor),
        ])
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    override func prepareForReuse() {
        super.prepareForReuse()
        titleLabel.text = nil // 텍스트 초기화
    }
    
    
    func configure(with title: String) {
        titleLabel.text = title
    }
    
    override func updateConfiguration(using state: UICellConfigurationState) {
        super.updateConfiguration(using: state)
        
        
        // 편집 모드에 따라 액세서리 설정
        if state.isEditing {

            let deleteAction = UICellAccessory.delete(displayed: .whenEditing) { [weak self] in
                print("deleteAction")
                guard let self = self else { return }
                self.delegate?.deleteItem(cell: self)

            }
            accessories = [deleteAction]

        } else {
            // 편집 모드가 아닐 때는 액세서리 제거
            accessories = []
        }
    }
}

``` 


