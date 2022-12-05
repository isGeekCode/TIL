# UICollectionView - 프로퍼티 옵저버 didSet과 isSelected

UICollectionViewCell은 isSelected라는 Bool값이 있어

셀을 클릭할 때 아래와 같이 override하여 나타낼 수 있다. 

```swift
class RoomCollectionViewCell: UICollectionViewCell {
    
    let titleLabel = UILabel()
    let backgroundView = UIView()
    
    override var isSelected: Bool {

        didSet {
            if isSelected {
                backgroundView.backgroundColor = UIColor.symbolColor
                titleLabel.textColor = UIColor.black
                titleLabel.layer.borderWidth = 0.0
            } else {
                backgroundView.backgroundColor = UIColor.clear      
            }        
        }
    }
```
