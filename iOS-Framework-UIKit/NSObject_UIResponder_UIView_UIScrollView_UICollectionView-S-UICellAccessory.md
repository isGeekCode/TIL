# UICellAccessory : UICollectionView에 사용하는 악세서리 Struct

UICellAccessory 는 UICollectionViewListCell 에 추가할 수 있는 시각적 요소로, iOS 14.0 부터 사용 가능하다.



UIKit에서 시스템 악세서리의 위치는 미리 정의되어있다.  
그래서 시스템에서 렌더링 순서와 셀의 어느쪽에 표시되는지를 자동으로 결정한다.  
이 악세서리는 Array에 추가되는 방식으로 세팅되는데 이 순서자체는 실제 배치순서에 영향을 주지않는다.  

## 악세서리의 종류
- .outlineDisclosure
- .disclosureIndicator
- .delete
- .reorder
- .checkmark
- .insert
- .multiselect
- .label
- .detail
- .popUpMenu

<br><br>

이 악세서리들을 생성해서 추가할 때에는 아래처럼 추가하게 된다.  

```swift
cell.accessories = [
    .outlineDisclosure(displayed: .always),
    .disclosureIndicator(displayed: .always),
    .delete(displayed: .always),
    .reorder(displayed: .always),
    .checkmark(displayed: .always),
    .insert(displayed: .always),
    .multiselect(displayed: .always),
    .label(text: "hello", displayed: .always),
    .detail( displayed: .always),
    .popUpMenu(
        UIMenu(children: [
            UIAction(title: "첫번째", handler: { _ in  }),
            UIAction(title: "두번째", handler: { _ in })
        ]),
        displayed: .always)
]
```
  
<br><br>

이때 공통적으로 들어가는 것은 .displayed인데, 이 값은 아래같이 표시되는 조건을 의미한다.  
- always : accessory 가 언제나 표시됩니다.
- whenEditing : cell 이 editing mode 일때만 accessory 가 표시됩니다.
- whenNotEditing : cell 이 editing mode 가 아닐때만 accessory 가 표시됩니다.

때문에 `cell.accessories = [.delete()]` 처럼 표시하면 기본 값인 whenEditing이 설정되서 기본적으론 보이지않고 Editing 모드로 들어가야 볼수가 있게된다.  



