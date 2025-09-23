# UIProgressView


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

## 상태값에 따른 체크

```swift
    @IBOutlet weak var progressBar: UIProgressView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 프로그래스바 초기값 설정
        setProgressBar(progress: 0.5)
        
        // 타이머 시작
        startTimer()

    }

    func setProgressBar(progress: Float) {
        progressBar.progress = progress
    }
    
    func updateProgressBar(progress: Float) {
        // 애니메이션 효과와 함께 프로그래스바 업데이트
        UIView.animate(withDuration: 0.5) {
            self.progressBar.setProgress(progress, animated: true)
        }
        
        // 프로그래스바가 100%가 되었을 때 처리할 함수
        if progress == 1.0 {
            progressBarComplete()
        }
    }
    
    func progressBarComplete() {
        // 프로그래스바가 100%가 되었을 때 처리할 코드 작성
        print("프로그래스바 완료!")
    }
    
    /// 특정 기준(시간)에 따라 함수를 체크하여 진행도 체크, 상황에 따라 커스텀 필요
    /// 어떤 기준을 가지고 퍼센트를 산정할지 정해야한다.
    func startTimer() {
      var progress: Float = 0.0
      let timer = Timer.scheduledTimer(withTimeInterval: 0.1, repeats: true) { timer in
          progress += 0.01
          
          if progress >= 1.0 {
              timer.invalidate()
              self.updateProgressBar(progress: 1.0)
          } else {
              self.updateProgressBar(progress: progress)
          }
      }
      timer.fire()
    }
}
```
