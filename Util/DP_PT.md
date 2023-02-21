# dp와 pt에 대하여 (Feat. 포인트란)
모바일 앱 개발에서 dp와 pt는 둘 다 화면상에서 크기와 위치를 표현하는 단위다. 그러나 dp는 안드로이드에서 사용하는 단위이고, pt는 iOS에서 사용하는 단위다.

dp는 "Density-independent Pixel"의 약자로, 밀도에 독립적인 픽셀을 나타낸다. 안드로이드 기기는 다양한 해상도와 화면 크기를 갖고 있기 때문에, 디바이스별로 화면 요소의 크기가 다르게 보일 수 있다. 이를 해결하기 위해, 안드로이드에서는 dp 단위를 사용한다. dp는 화면 크기와 밀도(DPI)에 따라 크기가 자동으로 조절되어, 동일한 크기의 UI 요소가 다른 크기로 보이지 않도록 한다.

pt는 "Point"의 약자로, iOS에서 사용하는 화면 크기의 단위다. pt는 화면의 해상도에 따라 크기가 일정하게 유지되기 때문에, 디바이스별로 크기가 다른 UI 요소를 만들기 적합하다. iOS에서는 디바이스별로 해상도가 다르기 때문에, pt를 사용하여 화면 크기를 조정하여 일관성 있는 UI를 제공할 수 있다.

따라서, 안드로이드에서는 dp를 사용하여 화면 크기와 밀도(DPI)에 독립적인 크기를 지정하고, iOS에서는 pt를 사용하여 해상도에 독립적인 크기를 지정한다.


## dp에서 pixel로 (android)
안드로이드에서는 디스플레이 크기와 밀도에 따라 화면 크기가 다양하다. 따라서 안드로이드에서는 "밀도 독립적 픽셀(DP, Density-independent pixels)"라는 개념을 사용하여 화면 크기를 정의한다.

그러나 개발자들이 일반적으로 레이아웃과 UI 디자인을 할 때 픽셀 단위를 사용하기 때문에, 안드로이드에서는 DP를 픽셀로 변환해야 할 필요가 있다. DP를 픽셀로 변환하는 방법은 다음과 같다.

```java
public int dpToPx(int dp) {
    DisplayMetrics displayMetrics = getContext().getResources().getDisplayMetrics();
    int px = Math.round(dp * (displayMetrics.xdpi / DisplayMetrics.DENSITY_DEFAULT));
    return px;
}
```
이 메소드는 DP 값을 픽셀로 변환하여 반환한다. dp 매개 변수에 변환할 DP 값을 전달하면 된다. 이 메소드에서는 getDisplayMetrics() 메소드를 사용하여 현재 화면의 DisplayMetrics를 가져온다. 그런 다음 xdpi 값을 기준으로 DP 값을 픽셀로 변환합니다. xdpi는 화면의 X축 dpi(도트/인치) 값을 나타낸다.

위의 코드에서 반환된 px 값은 변환된 픽셀 값을 나타내며, 이 값을 사용하여 뷰 크기를 설정할 수 있다.

## dp에서 pixel로 (iOS)

iOS에서는 "포인트(Point)"라는 개념을 사용하여 디바이스 독립적인 화면 크기를 정의한다. 하지만 UI 디자인을 할 때, 일반적으로 포인트 대신에 픽셀 단위를 사용하기 때문에, Swift에서는 DP를 픽셀로 변환하는 방법이 필요하다.

다음은 Swift에서 DP를 픽셀로 변환하는 방법이다.
```swift
func dpToPx(_ dp: CGFloat) -> CGFloat {
    let scale = UIScreen.main.scale
    let px = dp * scale
    return px
}
```

## 기기마다 달라지는 값
위의 코드에서, dp 매개 변수는 변환할 DP 값을 전달한다. UIScreen 클래스의 main 속성을 사용하여 현재 화면의 스케일 값을 가져온다. 이 스케일 값은 기본적으로 1.0, 2.0, 3.0 중 하나다. 그런 다음, dp 값에 스케일 값을 곱하여 픽셀 값을 계산한다.

이 코드에서 반환된 px 값은 변환된 픽셀 값을 나타내며, 이 값을 사용하여 뷰 크기를 설정할 수 있다.

`UIScreen.main.bounds.size.width`는 iOS에서 화면의 가로 폭을 나타내는 값이다. 이 값은 포인트 단위로 반환된다.

iOS에서 포인트(Point)는 디바이스 독립적인 화면 크기를 나타내는 단위이며, 레티나 디스플레이에서는 1포인트에 2픽셀을 사용한다. 따라서, UIScreen.main.bounds.size.width 값은 레티나 디스플레이에서 1포인트 당 2픽셀을 사용하므로 픽셀 단위로 계산하려면 해당 값을 화면의 스케일(scale) 값으로 곱해주면 된다.

예를 들어, 기기의 가로 해상도가 750포인트이고 스케일 값이 2x(레티나 디스플레이)인 경우, UIScreen.main.bounds.size.width 값은 750포인트이며, 픽셀 단위로 계산하면 750 * 2 = 1500픽셀이 된다.

따라서, UIScreen.main.bounds.size.width 값은 포인트 단위로 반환되지만, 디스플레이의 스케일 값과 함께 사용하면 해당 값의 픽셀 단위 크기를 계산할 수 있다.

## 레티나를 캐치하려면
iOS에서 현재 기기가 레티나 디스플레이인지 여부를 확인하려면 UIScreen 클래스의 scale 속성을 사용한다. scale 속성은 화면의 스케일 값(scale factor)을 나타내며, 이 값이 2.0 이상인 경우 레티나 디스플레이를 사용 중이라고 판단할 수 있다.

레티나 디스플레이는 iPhone 4부터 지원되며, iPhone 4에서는 스케일 팩터가 2.0이다. 이후 iPhone, iPad 및 iPod touch 디바이스에서도 레티나 디스플레이가 지원되며, 스케일 팩터는 일반적으로 2.0, 3.0 또는 4.0이다.

레티나 HD 디스플레이는 스케일 팩터가 3.0인 디바이스에서 지원된다. 이러한 디바이스 중 하나는 iPhone 6 Plus이다. 따라서, 레티나 HD 디스플레이가 사용 중인지 여부를 확인하려면 다음과 같이 코드를 작성할 수 있다.

예를 들어, 다음과 같이 UIScreen 객체를 사용하여 현재 기기의 화면 스케일 값을 가져올 수 있다.

```swift
let scale = UIScreen.main.scale

if scale == 3.0 {
    // 현재 기기는 레티나 HD 디스플레이를 사용 중입니다.
} else if scale >= 2.0 {
    // 현재 기기는 레티나 디스플레이를 사용 중입니다.
} else {
    // 현재 기기는 레티나 디스플레이를 사용하지 않습니다.
}
```

그리고 이걸 통해 enum으로 나누려면 이렇게 할 수 있다.

```swift
enum DeviceDisplayType {
    case standard // 레티나 디스플레이를 사용하지 않는 디바이스
    case retina // 레티나 디스플레이를 사용하는 디바이스
    case retinaHD // 레티나 HD 디스플레이를 사용하는 디바이스
}

let deviceDisplayType = getDeviceDisplayType()
switch deviceDisplayType {
case .standard:
    // 레티나 디스플레이를 사용하지 않는 디바이스
case .retina:
    // 레티나 디스플레이를 사용하는 디바이스
case .retinaHD:
    // 레티나 HD 디스플레이를 사용하는 디바이스
}


```
또한 아래와 같이 타입에 따라 pt값을 바꿔 사용할 수도 있다.

```swift
func getPtForDeviceDisplayType(_ pt: CGFloat) -> CGFloat {
    let screenScale = UIScreen.main.scale
    let deviceDisplayType = getDeviceDisplayType()
    
    switch deviceDisplayType {
    case .retina:
        return pt * 2
    case .retinaHD:
        return pt * 3
    default:
        return pt
    }
}

let pt = getPtForDeviceDisplayType(50)
print(pt)
```
