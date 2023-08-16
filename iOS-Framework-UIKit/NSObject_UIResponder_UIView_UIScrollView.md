# NSObject_UIResponder_UIView_UIScrollView

UIScrollView는 iOS 앱에서 스크롤 가능한 컨텐츠를 제공하기 위해 사용되는 뷰. 

또한 사용자가 화면을 스크롤하여 보이지 않는 부분의 컨텐츠를 볼 수 있게 한다. 

주로 이미지 뷰어, 웹 브라우저, 맵 뷰 등에서 사용된다.

특히!! 우리에게 익숙한 UITableView, UITextView의 상위 클래스다. 그래서 스크롤이 된다!!

## 포함된 주요 구성 요소

- Content View: 스크롤 가능한 컨텐츠를 포함하는 뷰
  - UIScrollView는 이 뷰를 스크롤하여 보이지 않는 부분의 컨텐츠를 볼 수 있게 한다.

- Scroll Indicators: 사용자가 스크롤할 수 있는지를 나타내는 인디케이터. 수평 및 수직 스크롤 인디케이터를 모두 제공할 수 있다.

- Paging: UIScrollView를 사용하여 페이지 뷰를 구현할 수 있다. 페이지 뷰는 여러 페이지로 구성된 단일 스크롤 뷰입이다.

- Zooming: UIScrollView를 사용하여 확대 / 축소 가능한 뷰를 만들 수 있다. 사용자는 제스처를 사용하여 뷰를 확대하거나 축소할 수 있다.

## 스크롤뷰에서 이해해야하는 것
(Content Layout 영역 >= Frame Layout 영역)
- Content Layout
    - 실제로 스크롤해서 보여질 전체 뷰를 담는 Layout
- Frame Layout
    - 스크린에 보이는 만큼의 Layout

## History
- 230508 : 초안작성
