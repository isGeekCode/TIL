# UICollectionView with DiffableDataSource
iOS13부터 DiffableDataSource를 이용한 CollectionView가 등장했다.  


## 예제1




## 예제1 전체코드
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


class ViewController: UIViewController {
    // 2. UICollectionView 및 DataSource 정의
    lazy var collectionView: UICollectionView = {
        let layout = UICollectionViewFlowLayout()
        layout.itemSize = CGSize(width: 100, height: 100)
        
        let collectionView = UICollectionView(frame: .zero,
                                              collectionViewLayout: layout)
        collectionView.translatesAutoresizingMaskIntoConstraints = false
        collectionView.register(UICollectionViewCell.self, forCellWithReuseIdentifier: "cell")
        collectionView.delegate = self

        return collectionView
    }()
    
    
    private var dataSource: UICollectionViewDiffableDataSource<Section, Item>!

    override func viewDidLoad() {
        super.viewDidLoad()
        setupCollectionView()
    }

    private func setupCollectionView() {
        
        view.addSubview(collectionView)

        collectionView.delegate = self  // Delegate 설정


        // 2. NSLayoutConstraint를 사용하여 제약 조건 설정
        NSLayoutConstraint.activate([
            collectionView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
            collectionView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            collectionView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
            collectionView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor)
        ])

        // 3. DataSource 및 기타 설정
        configureDataSource()

    }

    private func configureDataSource() {
        // 5. DataSource 설정 및 셀 구성
        dataSource = UICollectionViewDiffableDataSource<Section, Item>(collectionView: collectionView) {
            (collectionView, indexPath, item) -> UICollectionViewCell? in
            let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "cell", for: indexPath)
            cell.backgroundColor = .systemRed
            return cell
        }
        
        applyInitialSnapshots() // 초기 데이터 로드

    }

    private func applyInitialSnapshots() {
        // 6. 초기 데이터 스냅샷 적용
        var snapshot = NSDiffableDataSourceSnapshot<Section, Item>()
        snapshot.appendSections([.main])
        snapshot.appendItems([
            Item(title: "First"),
            Item(title: "Second"),
        ])
        dataSource.apply(snapshot, animatingDifferences: false)
    }
}

extension ViewController: UICollectionViewDelegate {
    
    func collectionView(_ collectionView: UICollectionView, didSelectItemAt indexPath: IndexPath) {
        // 셀이 선택되었을 때 호출됩니다.
        // 새로운 아이템 추가
        let newItem = Item(title: "New Item \(Date())")
        var currentSnapshot = dataSource.snapshot()
        currentSnapshot.appendItems([newItem], toSection: .main)
        dataSource.apply(currentSnapshot, animatingDifferences: true)
    }
}
```



## 예제2

```swift


```
