# NSObject_UIResponder_UIView_UIControl : UITextField

## 스토리보드로 구현하기
1. 라이브러리로 부터 viewController 위로 텍스트필드를 올려둔다. (addSubView 처리)
2. 제약조건을 세팅한다. 
3. 델리게이트 링크시키기
4. Did End On Exit 링크시키기 : 텍스트필드에서 엔터를 누르면 실행되는 곳
    - textFieldShouldReturn 메서드와 동일한 동작

## textfield 사용하기
1. 프로토콜 채택
```swift
  extension ViewController: UITextFieldDelegate { }
```
2. delegate 선언
```swift
  textfield.delegate = self
```
3. delegate 함수 구현
아래는 return입력시 비활성화처리 코드
```swift

  func textFieldShouldReturn(_ textField: UITextField) -> Bool {
    textField.resignFirstResponder() // TextField 비활성화
    return true
  }

```

## 입력시작시키기
```swift
(TextField 또는 UISearchBar).becomeFirstResponder()
```


## 입력종료시키기
```swift
(TextField 또는 UISearchBar).resignFirstResponder()
```

```swift
extension ViewController: UITextFieldDelegate {
  
  textfield.delegate = self
  
  func textFieldShouldReturn(_ textField: UITextField) -> Bool {
    textField.resignFirstResponder() // TextField 비활성화
    return true
  }
}
```


## VC내부를 클릭하면 입력 종료시키기 
viewController 내부에 아래 코드를 입력한다.
```swift
  override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
    self.view.endEditing(true)
  }
```


## 텍스트필드 아이콘 넣기
```
    let imageView = UIImageView()
    let magnifyingGlassImage = UIImage(systemName: "magnifyingglass", withConfiguration: UIImage.SymbolConfiguration(weight: .regular))?.withTintColor(.darkGray, renderingMode: .alwaysOriginal)
    imageView.image = magnifyingGlassImage    
    imageView.frame = CGRect(x: 0, y: 5, width: 45, height: 20)
    imageView.contentMode = .scaleAspectFit
    textField.leftViewMode = .always
    textField.leftView = imageView
```

# Simulator Env

## Simulator로 테스트할 때 TextField를 클릭하여 현재 키보드 모양을 보고싶은데 보이지 않을 때 보이게 하는 방법

### Step1. Keyboard설정 들어가기
구버전 위치
- iOS Simulator -> Hardware -> Keyboard
신버전 위치
- I/O -> Keyboard
### Step2. "Connect Hardware Keyboard" 체크 해제

# 참고링크
- https://stackoverflow.com/questions/35056705/convert-c-to-swift-add-magnifying-glass-icon-to-uitextfield
- https://stackoverflow.com/questions/37452813/padding-before-textfield-icon
