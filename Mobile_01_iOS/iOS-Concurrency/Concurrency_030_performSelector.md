# GCD - performSelector를 이용한 비동기 작업


`NSObject` 클래스의 `performSelector` 메서드를 사용하여 메인 스레드에서 특정 메서드를 호출하도록 예약할 수 있다.


### 사용법

```swift
class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        performSelector(onMainThread: #selector(updateUI), with: nil, waitUntilDone: false)
    }

    @objc func updateUI() {
        // 메인 스레드에서 실행되어야 하는 작업
        print("test")
    }
}
```
