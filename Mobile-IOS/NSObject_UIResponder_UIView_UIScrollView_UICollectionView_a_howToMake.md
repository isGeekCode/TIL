# NSObject_UIResponder_UIView_UIScrollView_UICollectionView : 레이아웃

CollectionView는 iOS에서 다양한 방식으로 데이터를 표시하는 컴포넌트로, TableView와 비슷한 역할을 한다. 하지만 TableView와는 몇 가지 중요한 차이점이 있다.

## 차이점

- 다양한 레이아웃: TableView는 단일 열로 구성된 리스트를 표시하는 데 주로 사용된다. 하지만 CollectionView는 다양한 레이아웃을 가지고 있어 그리드, 스택, 플로우 레이아웃 등 다양한 형태로 데이터를 표현할 수 있다.

- 유연한 셀 디자인: TableView에서는 모든 셀이 동일한 모양을 가지지만, CollectionView는 다양한 셀 디자인을 지원한다. 각 셀은 고유한 디자인과 레이아웃을 가질 수 있으며, 데이터에 따라 동적으로 변경할 수 있다.

- 다중 열 및 섹션: TableView는 주로 단일 열을 가지는 리스트를 표시하는 데 사용되지만, CollectionView는 다중 열을 가질 수 있다. 또한, 섹션을 사용하여 데이터를 그룹화하고 여러 열로 표시할 수도 있다.


## 공통된 특징

- 뷰 재사용: TableView는 재사용 가능한 셀을 사용하여 효율적인 메모리 관리를 할 수 있다. CollectionView도 TableView와 동일한 방식으로 셀 재사용을 지원하여 대규모 데이터 세트의 표시와 성능을 향상시킬 수 있다.

- 커스텀 레이아웃: CollectionView는 커스텀 레이아웃을 구현할 수 있는 유연성을 제공한다. 원하는 방식으로 아이템의 위치와 크기를 지정하여 완전히 사용자 정의된 레이아웃을 만들 수 있다.

이러한 차이점들로 인해 CollectionView는 TableView보다 더 다양한 데이터 표현 방식과 유연성을 제공하며, 데이터를 시각적으로 풍부하게 표현할 수 있다. 

TableView는 단순한 리스트 표시에 적합하고, CollectionView는 더 복잡하고 다양한 데이터 표현에 유용하다.


## 템플릿

```swift
import UIKit

class ViewController: UIViewController {

    // 임의의 리스트 데이터
    let itemList = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

    let collectionView: UICollectionView = {
        let layout = UICollectionViewFlowLayout()
        let collectionView = UICollectionView(frame: .zero, collectionViewLayout: layout)
        // collectionView의 속성들 설정
        collectionView.backgroundColor = .white
        collectionView.showsVerticalScrollIndicator = false
        collectionView.showsHorizontalScrollIndicator = false
        // 셀 등록
        collectionView.register(UICollectionViewCell.self, forCellWithReuseIdentifier: "Cell")
        return collectionView
    }()

    override func viewDidLoad() {
        super.viewDidLoad()
        setupCollectionView()
    }

    private func setupCollectionView() {
        // 콜렉션 뷰의 delegate와 dataSource 설정
        collectionView.delegate = self
        collectionView.dataSource = self

        // 콜렉션 뷰의 오토레이아웃 설정
        collectionView.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(collectionView)
        NSLayoutConstraint.activate([
            collectionView.topAnchor.constraint(equalTo: view.topAnchor),
            collectionView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            collectionView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
            collectionView.bottomAnchor.constraint(equalTo: view.bottomAnchor)
        ])
    }
}

extension ViewController: UICollectionViewDelegate, UICollectionViewDataSource {
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return itemList.count
    }

    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "Cell", for: indexPath)
        // 셀의 내용 설정
        cell.backgroundColor = .blue
        cell.textLabel?.text = itemList[indexPath.item]
        return cell
    }
}

extension ViewController: UICollectionViewDelegateFlowLayout {
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
        // 셀의 크기 설정
        return CGSize(width: 100, height: 100)
    }

    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, minimumInteritemSpacingForSectionAt section: Int) -> CGFloat {
        // 셀 사이의 수평 간격 설정
        return 10
    }

    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, minimumLineSpacingForSectionAt section: Int) -> CGFloat {
        // 셀 사이의 수직 간격 설정
        return 10
    }
}

```
