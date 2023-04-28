# NSObject_UIResponder_UIView_UIProgressView


프로그래스뷰는 아래그림처럼 어떤 작업을 진행중에 있다는 것을 사용자에게 보여줄때 사용한다.

![images_sainkr_post_11d60caa-fd13-4730-8b39-59d39e7ca3ec_image](https://user-images.githubusercontent.com/76529148/235186383-fc656315-8f3e-4fbe-8c39-13c10785c434.png)


## 선언
1. 스토리보드 또는 코드를 사용하여 UIProgressView를 생성.
2. 프로그래스바의 값을 업데이트하는 데 사용할 수있는 IBOutlet을 생성.

```swift
@IBOutlet weak var progressBar: UIProgressView!
```

3. 코드에서 값이 업데이트되면 해당 값을 프로그래스바에 할당.
```swift
progressBar.progress = 0.5 // 50%로 프로그래스바 업데이트

```
4. 값이 변경될 때마다 프로그래스바가 애니메이션되도록하려면, 애니메이션 효과를 추가 할 수 있다.
```swift
UIView.animate(withDuration: 0.5) {
    self.progressBar.setProgress(0.8, animated: true)
}
```

위와 같은 방법으로 UIProgressView를 사용하여 iOS 앱에서 간단한 프로그래스바를 만들 수 있다.
