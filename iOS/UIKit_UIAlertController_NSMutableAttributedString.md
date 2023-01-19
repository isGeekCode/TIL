# UIKit - UIAlertController : 장문의 얼럿 만들기

얼럿을 정말 길게 써야할 때가 있다.
커스텀뷰를 만들어도되지만 궂이 만들지않아도 간단하게 수정이 가능하다.

### NSMutableParagraphStyle
문단 스타일 속성의 하위 속성 값을 변경하기 위한 개체다.
텍스트가 들어가는 곳에서 이것을 이용해 여러 문단스타일을 수정가능하다.

### NSMutableAttributedString
- 텍스트 부분에 대한 관련 속성(예: visual style, 하이퍼링크 또는 접근성 데이터)이 있는 변경 가능한 문자열을 말한다.
- 해당부분은 StoryBoard에서는 텍스트부분에서 Attributed로 설정하면 선택이 가능해진다. 

# Source Code
```swift
let msg = """
          1. 동해물과 백두산이 마르고 닳도록
          하느님이 보우하사 우리나라 만세
          무궁화 삼천리 화려 강산
          대한 사람 대한으로 길이 보전하세

          2. 남산 위에 저 소나무 철갑을 두른 듯
          바람 서리 불변함은 우리 기상일세
          무궁화 삼천리 화려 강산
          대한 사람 대한으로 길이 보전하세

          3. 가을 하늘 공활한데 높고 구름 없이
          밝은 달은 우리 가슴 일편단심일세
          무궁화 삼천리 화려 강산
          대한 사람 대한으로 길이 보전하세

          4. 이 기상과 이 맘으로 충성을 다하여
          괴로우나 즐거우나 나라 사랑하세
          무궁화 삼천리 화려 강산
          대한 사람 대한으로 길이 보전하세
          """

// 문단스타일생성
let paragraphStyle = NSMutableParagraphStyle()
paragraphStyle.alignment = .left

// NSMutableAttributedString 생성 및 문단스타일 세팅
let messageText = NSMutableAttributedString(
    string: msg,
    attributes: [
        NSAttributedString.Key.paragraphStyle: paragraphStyle,
        NSAttributedString.Key.font : UIFont.systemFont(ofSize: 13, weight: .regular),
        NSAttributedString.Key.foregroundColor : UIColor.black
    ]
)
// 따로 NSMutableAttributedString을 추가한다면 message는 비워도된다. 
let alert = UIAlertController(title: "장문의 얼럿만들기", message: "", preferredStyle: .alert)
//생성한 alertController에 setValue를 통해 메세지내용을 추가한다. 
alert.setValue(messageText, forKey: "attributedMessage")
let confirm = UIAlertAction(title: "확인", style: .default)
alert.addAction(confirm)
self.present(alert, animated: true) { }
```

# 적용화면
<img width="303" alt="스크린샷 2023-01-19 오후 10 13 42" src="https://user-images.githubusercontent.com/76529148/213451917-c6fbdefb-6b9e-433d-bea1-c9edb2927aca.png">
