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
