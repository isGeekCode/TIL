# View - UIImageView 핵심 가이드

## UIImageView는 언제 쓰나?
- 정적인(또는 자주 바뀌지 않는) 이미지를 표시할 때 사용하는 `UIView`의 서브클래스입니다.
- 애셋/번들의 정적 이미지뿐 아니라 네트워크에서 내려받은 이미지, 시스템 심볼, 애니메이션 이미지도 표시할 수 있습니다.
- `CALayer` 기반으로 동작하므로 `cornerRadius`, `shadow`, `mask` 등 그래픽 효과를 쉽게 적용할 수 있습니다.

## 반드시 기억할 프로퍼티
### `contentMode`
- 이미지가 뷰의 bounds와 비율이 다를 때 **어떻게 그려질지**를 결정합니다.
- 대표 옵션
  - `.scaleToFill` : 비율 무시, 가득 채움 → 왜곡 가능성 있음
  - `.scaleAspectFit` : 비율 유지, 전체가 보이도록 축소 → 여백 가능
  - `.scaleAspectFill` : 비율 유지, 가득 채우되 일부 잘림 허용 → 꽉 차지만 주변 잘릴 수 있음
  - `.center`, `.top`, `.bottom` 등 : 이미지를 특정 위치에 정렬하고 남는 부분은 잘립니다.
- 더 자세한 설명과 비교 이미지는 `Layout_ImageContentMode.md` 문서 참고.

### `clipsToBounds` / `layer.masksToBounds`
- 뷰의 경계를 벗어나는 하위 콘텐츠를 잘라낼지 여부. 둥근 모서리나 마스크 적용 시 자주 함께 사용합니다.

### `image` vs `highlightedImage`
- `image`는 기본 이미지, `highlightedImage`는 강조 상태(예: 버튼처럼 눌렸을 때) 표현용으로 사용할 수 있습니다.

## 실무에서 자주 쓰는 패턴
### 네트워크 이미지 로딩
- URL에서 이미지를 내려받아 설정할 때는 다운샘플링·캐싱·재사용 이슈를 고려해야 합니다.
- 구체적인 코드 예시는 `NSObject_UIResponder_UIView_UIImageView_setImageDownload.md` 문서를 참고하세요.

### 셀 재사용 대비 초기화
- `UITableViewCell`/`UICollectionViewCell` 안에서 이미지 뷰를 사용할 때는 `prepareForReuse()`에서 이미지/애니메이션을 초기화해 플리커를 방지합니다.


## 체크리스트
- 레이아웃 잡기 전에 `contentMode`와 `clipsToBounds`를 어떻게 둘지 먼저 결정한다.
- 네트워크 이미지면 캐싱 전략(Kingfisher, URLCache 등)을 미리 정리한다.
- 고해상도 이미지는 메모리를 많이 쓰므로 크기 조정, `preferredSymbolConfiguration`(SF Symbol) 등을 활용한다.
- 접근성: 필요 시 `isAccessibilityElement = true`, `accessibilityLabel` 등을 세팅해 스크린 리더 지원.

