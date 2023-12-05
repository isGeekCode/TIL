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
