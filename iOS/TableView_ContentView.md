# TableViewCell - ContentView

UITableViewCell안에는 여러 View들이 있습니다.

- contentView
- backgroundView
- selectedBackgroundView
- multipleSelectionBackgroundView

iOS 2.0부터 등장했던 녀석들이죠.

마찬가지로 UICollectionViewCell안에도 View들이 있습니다.

- contentView
- backgroundView
- selectedBackgroundView

얘네들은 iOS 6.0부터 등장했습니다.

오늘 이야기하는 contentView의 정의는 **`The content view of the cell object.`** 입니다.

cell 객체 안에 있는 contentView…라는… 설명 뭐지….

네 말그대로 Cell객체 안에 컨텐츠를 담당할 UIView라는 말 같아요.

UITableViewCell 객체의 content view는 cell에서 표시하는 **content의 default superview**입니다.

단순히 또 다른 view를 추가하여 cell을 커스텀하려면 cell을 editing mode로 전환하거나,

editing mode에서 벗어날 때 적절하게 배치되도록 content view에 추가해야합니다

끝.
