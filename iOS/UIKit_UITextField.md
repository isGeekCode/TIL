# UIKit - UITextField

## 텍스트필드 아이콘 넣기
```
    let imageView = UIImageView()
    let magnifyingGlassImage = UIImage(systemName: "magnifyingglass", withConfiguration: UIImage.SymbolConfiguration(weight: .regular))?.withTintColor(.darkGray, renderingMode: .alwaysOriginal)
    imageView.image = magnifyingGlassImage    
    imageView.frame = CGRect(x: 0, y: 5, width: 45, height: 20)
    imageView.contentMode = .scaleAspectFit
    textField.leftViewMode = .always
    textField.leftView = imageView
```


# 참고링크
- https://stackoverflow.com/questions/35056705/convert-c-to-swift-add-magnifying-glass-icon-to-uitextfield
- https://stackoverflow.com/questions/37452813/padding-before-textfield-icon
