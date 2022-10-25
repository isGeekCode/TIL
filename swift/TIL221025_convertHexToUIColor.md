hex값을 UIcolor로 변환하는 방법

```swift
extension UIColor {
    /// Hex값으로 컬러 생성하기
    /// alpha값이 있는경우, alpha값 파라미터를 사용할 것
    /// - Parameters:
    ///   - hex: 16진수
    ///   - alpha: 투명도, (optional)
    convenience init(hex: Int, alpha: CGFloat = 1.0) {
        let components = (
            red: CGFloat((hex >> 16) & 0xff) / 255,
            green: CGFloat((hex >> 08) & 0xff) / 255,
            blue: CGFloat((hex >> 00) & 0xff) / 255
        )
        self.init(red: components.red, green: components.green, blue: components.blue, alpha: alpha)
    }
}
```

사용예

```swift
static let test1Color = UIColor(hex: 0x00D7F1)
static let test2Color = UIColor(hex: 0x00D7F1, alpha: 0.5)
```

hexString코드를 UIColor로 변환하는 방법

```swift
    static func colorWithHex(rgbHex: Int, alpha: CGFloat = 1.0) -> UIColor {

        let red = (CGFloat((rgbHex & 0xFF0000) >> 16)) / 255.0
        let green = (CGFloat((rgbHex & 0x00FF00) >> 8)) / 255.0
        let blue = (CGFloat(rgbHex & 0x0000FF)) / 255.0

        return UIColor(red: red, green: green, blue: blue, alpha: alpha)
    }
```

사용예

```
    static let test3Color = UIColor.colorFromHex(hex: "#751485")
```
