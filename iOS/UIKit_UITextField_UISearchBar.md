# UIKit - UISearchBar

### 왼쪽아이콘
`searchBar.setImage(UIImage(named: "icSearchNonW"), for: .search, state: .normal)`

- 서치바의 왼쪽 돋보기 아이콘 이미지 세팅은 `.setImage` 
- `for:UISearchBar.Icon.search(서치아이콘)`
- `state: .normal`


### 오른쪽 아이콘
- 서치바의 오른쪽 엑스버튼 이미지 세팅(검색했을 때)와 마찬지이지만 for에는 .clear(검색한 문장을 없앨때 아이콘)로만 바꿔주시면 됩니다.

### 세팅하기
```swift

    lazy var searchBar: UISearchBar = {
      let searchBar = UISearchBar()
//        $0.placeholder = ""
      searchBar.searchTextField.tintColor = .black
      searchBar.searchBarStyle = .minimal
      searchBar.setImage(UIImage(named: "icCancel"), for: .clear, state: .normal)
      searchBar.setImage(UIImage(named: "icSearchNonW"), for: .search, state: .normal)
      return searchBar
    }()
    
    
    func setSearchBar() {
    
    guard let textfield = searchBar.value(forKey: "searchField") as? UITextField else { return }

    textfield.backgroundColor = .systemGray6
    textfield.textColor = .black
    textfield.attributedPlaceholder = NSAttributedString(string: textfield.placeholder ?? "검색", attributes: [NSAttributedString.Key.foregroundColor : UIColor.black])

    //왼쪽 아이콘 이미지넣기
    if let leftView = textfield.leftView as? UIImageView {
        leftView.image = leftView.image?.withRenderingMode(.alwaysTemplate)
        leftView.tintColor = .black
    }

    //오른쪽 x버튼 이미지넣기
    if let rightView = textfield.rightView as? UIImageView {
        rightView.image = rightView.image?.withRenderingMode(.alwaysTemplate)
    }
    
    }
}
```

### UITextField
- [TIL정리](https://github.com/isGeekCode/TIL/blob/main/iOS/UIKit_UITextField.md)
