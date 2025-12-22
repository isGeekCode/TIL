# NSObject - UIFont

iOS UIFont 클래스는 다양한 글꼴 굵기를 지원한다. 기본적으로, iOS는 다음과 같은 5개의 표준 굵기를 제공한다.

- Ultra Light (최대한 가볍게)
- Thin (가볍게)
- Light (약간 가벼운)
- Regular (보통)
- Medium (약간 짙은)

또한, iOS는 Bold 및 Heavy 굵기를 지원한다. 이러한 굵기는 일반적으로 Regular 굵기보다 더 굵은 표시체다.

UIFont 클래스에서는 다음과 같은 weight 상수를 사용하여 다양한 굵기의 폰트를 생성할 수 있다.

- `UIFont.Weight.ultraLight`
- `UIFont.Weight.thin`
- `UIFont.Weight.light`
- `UIFont.Weight.regular`
- `UIFont.Weight.medium`
- `UIFont.Weight.semibold`
- `UIFont.Weight.bold`
- `UIFont.Weight.heavy`
- `UIFont.Weight.black`

예를 들어, bold 굵기의 폰트를 생성하려면 다음과 같이 작성할 수 있다.

```swift
let boldFont = UIFont.systemFont(ofSize: 16, weight: .bold)
```
비슷하게, heavy 굵기의 폰트를 생성하려면 다음과 같이 작성할 수 있습니다.

```swift
let heavyFont = UIFont.systemFont(ofSize: 16, weight: .heavy)
```

weight는 default값이 regular로 세팅되어있어서 단순하게 size만 세팅할 수도 있다.
```swift
let simpleFont = UIFont.systemFont(ofSize: 16)
```
