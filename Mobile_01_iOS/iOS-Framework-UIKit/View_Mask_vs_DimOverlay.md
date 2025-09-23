# UIView 투명 영역 구현: 마스크 vs 딤 오버레이

## 1. Mask(Core Animation Layer Mask)란?
- `CALayer.mask`는 해당 레이어가 화면에 그릴 수 있는 영역을 **마스크 레이어의 알파 값**으로 제한합니다.
- 마스크 레이어에서 알파가 1(흰색)에 가까우면 표시되고, 0(검정)에 가까우면 잘립니다.
- 상위 레이어의 서브레이어·콘텐츠 전체가 마스크의 영향을 받으므로, 특정 영역만 투명하게 뚫거나 둥근 모서리를 만들 때 자주 사용합니다.

### 기본 사용 절차
1. 마스크를 적용할 뷰/레이어의 프레임 기준으로 `UIBezierPath`를 만듭니다.
2. `CAShapeLayer`에 `path`와 `fillColor`를 지정합니다. (알파가 1인 색을 사용)
3. 필요하면 `fillRule = .evenOdd`를 주어 안쪽/바깥쪽을 동시에 정의합니다.
4. 타깃 뷰의 `layer.mask`에 위 레이어를 할당합니다.

```swift
private func setMaskTransparency() {
    let overlayBounds = overlayContainerView.bounds
    let focusRect = scanAreaView.convert(scanAreaView.bounds, to: overlayContainerView)

    let path = UIBezierPath(rect: overlayBounds)
    path.append(UIBezierPath(roundedRect: focusRect, cornerRadius: 10))

    let maskLayer = CAShapeLayer()
    maskLayer.frame = overlayBounds
    maskLayer.path = path.cgPath
    maskLayer.fillRule = .evenOdd
    maskLayer.fillColor = UIColor.white.cgColor

    overlayContainerView.layer.mask = maskLayer
    overlayContainerView.backgroundColor = UIColor.black.withAlphaComponent(0.6)
}
```

- 위 코드는 **중앙 ROI는 알파 0, 나머지는 알파 1**이 되도록 만들어 투명 구멍을 냅니다.
- 마스크를 갱신할 때는 `maskLayer.path` 또는 `maskLayer.frame`을 다시 계산하여 애니메이션을 줄 수도 있습니다.

## 2. 현재 코드의 딤 오버레이 방식 (Sublayer + evenOdd)
`ScanViewController`의 `setTransparency()`는 마스크 대신 반투명 레이어를 **오버레이로 얹는** 접근을 택합니다.

```swift
private func setTransparency() {
    let focusRectInScanView = scanAreaView.convert(scanAreaView.bounds, to: overlayContainerView)

    let path = UIBezierPath(rect: overlayContainerView.bounds)
    let focusPath = UIBezierPath(roundedRect: focusRectInScanView, cornerRadius: 10)
    path.append(focusPath)

    let layer: CAShapeLayer = {
        if let l = dimOverlayLayer { return l }
        let l = CAShapeLayer()
        l.fillRule = .evenOdd
        l.fillColor = UIColor.black.withAlphaComponent(0.6).cgColor
        l.zPosition = 1
        overlayContainerView.layer.addSublayer(l)
        dimOverlayLayer = l
        return l
    }()

    layer.frame = overlayContainerView.bounds
    layer.path = path.cgPath
}
```

- overlay 뷰는 별도의 마스크 없이 그대로 표시됩니다.
- `CAShapeLayer`를 서브레이어로 추가하고, `evenOdd`를 이용해 ROI 영역만큼 경로를 두 번 그려 **ROI 내부는 그려지지 않도록** 만듭니다.
- 실제로는 배경에 아무 색도 칠하지 않았기 때문에 가운데 영역은 투명(=카메라가 보임), 주변은 설정한 색상으로 반투명하게 덮입니다.

## 3. 두 방법의 차이와 선택 기준

| 항목 | `layer.mask` 사용 | 딤 오버레이 서브레이어 |
| --- | --- | --- |
| 적용 대상 | 뷰 전체를 마스크로 잘라냄 | 기존 뷰 위에 반투명 레이어를 추가 |
| 레이어 구조 | `overlayContainerView`의 콘텐츠가 마스크에 따라 잘림 | 마스크 없이 오버레이 레이어만 시각 효과 담당 |
| 터치 영역 | 마스크가 터치 전달에 영향 없음 → 오버레이 아래 뷰 터치 가능 | 동일. 단, 추가 서브레이어에 히트 테스트 없음 |
| 애니메이션 | 마스크의 path 애니메이션으로 자연스러운 강조 가능 | 마찬가지로 path 애니메이션으로 유사 효과 구현 가능 |
| 재사용성 | 다른 뷰에도 쉽게 적용. 하지만 마스크가 존재하면 해당 뷰의 모든 서브콘텐츠가 잘림 | 오버레이 레이어만 따로 전환할 수 있어, 같은 컨테이너에 여러 효과 레이어를 겹치기 쉬움 |
| 성능 | GPU에서 마스크 계산. 복잡한 path가 많으면 비용 증가 | 단순 반투명 채우기. 안티앨리어싱 포함하지만 일반적으로 부담 적음 |
| 디버깅 | 마스크는 계층 구조에서 눈에 보이지 않아 파악이 어려움 | 서브레이어가 그대로 보이므로 인터페이스 디버깅이 용이 |

### 정리 포인트
- **마스크 방식**은 뷰 자체를 깔끔하게 clip 하고 싶을 때 적합합니다. 예: 카메라 프리뷰를 둥근 모서리로 자르거나, 특정 영역만 보여줄 때.
- **딤 오버레이 방식**은 "투명 구멍 + 주변 딤 처리"처럼 특정 효과를 겹칠 때 직관적입니다. 마스크보다 디버깅이 쉽고, 오버레이의 색이나 그라데이션을 바꾸는 것도 단순합니다.
- 현재 구현은 ROI 강조가 주 목적이므로, 오버레이 레이어를 유지하면서 필요 시 다른 장치(애니메이션, 추가 가이드 라인 등)를 쉽게 더할 수 있습니다.
- 만약 오버레이 외에 추가 UI를 `overlayContainerView` 안에서 렌더링해야 하고, 그것들이 마스크의 영향을 받으면 곤란하다면 현재 방식이 더 안정적입니다. 반대로 overlay 자체를 완전히 클립해야 한다면 마스크 방식이 깔끔합니다.

## 4. 실무에서의 팁
- **좌표 변환:** 두 방식 모두 `scanAreaView.convert(_, to:)`로 ROI를 overlay 좌표계로 변환해야 정확한 경계가 생깁니다.
- **갱신 타이밍:** `viewDidLayoutSubviews` 또는 로테이션 대응 시 마스크/레이어 프레임을 반드시 재설정해야 합니다.
- **애니메이션:** `CABasicAnimation(keyPath: "path")`로 path 변경 애니메이션을 주면 스캔 영역 확대/축소 효과를 자연스럽게 만들 수 있습니다.
- **접근성:** VoiceOver 사용자를 위해 ROI 위치/안내를 별도의 라벨로 제공하면 좋습니다. 오버레이는 시각 효과일 뿐이므로 음성 안내도 함께 고려하세요.
