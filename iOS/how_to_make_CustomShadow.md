# Layout - CustomShadow를 만드는 방법 (feat.CustomClass)


## 1. ios shadow blur spread 등등의 검색어로 스택오버플로우 자료 검색


```swift
extension CALayer {
  func applySketchShadow(
    color: UIColor = .black,
    alpha: Float = 0.5,
    x: CGFloat = 0,
    y: CGFloat = 2,
    blur: CGFloat = 4,
    spread: CGFloat = 0)
  {
    masksToBounds = false
    shadowColor = color.cgColor
    shadowOpacity = alpha
    shadowOffset = CGSize(width: x, height: y)
    shadowRadius = blur / 2.0
    if spread == 0 {
      shadowPath = nil
    } else {
      let dx = -spread
      let rect = bounds.insetBy(dx: dx, dy: dx)
      shadowPath = UIBezierPath(rect: rect).cgPath
    }
  }
}
```
## 2. CALayer+ 파일명 생성

### 코드설명
  ```
  extension CALayer {
  /// 뷰에 그림자 적용
  /// - Parameters
  ///   - color: 그림자 색 
  ///   - alpha: 투명도 
  ///   - x: 가로위치
  ///   - y: 세로위치 
  ///   - blur: 블러 - 흐릿함
  ///   - spread: 퍼짐정도
  func applySketchShadow(
    color: UIColor = .black,
    alpha: Float = 0.5,
    x: CGFloat = 0,
    y: CGFloat = 2,
    blur: CGFloat = 4,
    spread: CGFloat = 0)
  {
    masksToBounds = false
    shadowColor = color.cgColor
    shadowOpacity = alpha
    shadowOffset = CGSize(width: x, height: y)
    shadowRadius = blur / 2.0
    if spread == 0 {
      shadowPath = nil
    } else {
      let dx = -spread
      let rect = bounds.insetBy(dx: dx, dy: dx)
      shadowPath = UIBezierPath(rect: rect).cgPath
    }
  }
}

## 사용법

 실제로 그림자들은 각 요소에 동일하게 사용하기 때문에 따로 빼준다.
  ```swift

// 해당 어노테이션을 달아두면 스토리보드상에서 아래 inspectable달아둔 요소들을 수정할때 바로바로 스토리보드에서 확인가능
@IBDesignable
class CustomView: UIView {
  
  // 해당 어노테이션을 달아두면 스토리보드의 패널에서 GUI상에서 조작할수가 있다. 사실 이프로젝트는 노스토리보드라 필요없다.
  // 그러면 GUI에서 값을 넣어둠으로 바로 줄 수 있다.
  @IBInspectable
  var cornerRadius: CGFloat = 0 {
    didSet {
      // 값이 설정이 됐을때 알수 있는 부분
      self.layer.cornerRadius = cornerRadius
      
    }
  }
  
  // MARK: - Shadow
  
  @IBInspectable
  var hasShadow: Bool = false {
    didSet {
      if hasShadow {
        layer.applySketchShadow()
      }
    }
  }
```

이제 ViewController에서 hasShadow를  true로 해주면 미리 세팅해둔 그림자가 생성된다.


