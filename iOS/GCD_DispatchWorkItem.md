
DispatchWorkItem은 Grand Central Dispatch(GCD)에서 제공하는 클래스 중 하나로, 비동기 작업을 처리할 수 있는 객체다. 작업을 실행할 블록(block)을 가지고 있고, 큐에 추가하여 비동기적으로 실행할 수 있다.

아래는 DispatchWorkItem 클래스의 주요 특징이다.

- 실행할 작업을 포함하는 객체.
- GCD 큐에 추가하여 비동기적으로 실행할 수 있다.
- 작업 실행 중 취소, 일시 중지, 재개 등을 조작할 수 있다.
- 작업 실행 후의 결과값을 가져올 수 있다.
- DispatchWorkItem은 GCD의 다른 기능과 결합하여 사용할 수 있다.


- 장점
    - 비동기 작업 처리를 더욱 세밀하게 제어할 수 있다는 점이 있다.
    - DispatchWorkItem은 GCD의 다른 기능과 결합하여 사용할 수 있기 때문에, 여러 가지 기능을 조합하여 더욱 복잡한 비동기 작업을 처리할 수 있다.

- 단점
    - DispatchWorkItem을 사용하여 비동기 작업을 처리하면, 코드가 복잡해질 수 있다.
    - 작업을 일시 중지하거나, 실행 결과값을 가져오기 위해 추가적인 코드가 필요하다.
    - 잘못 사용할 경우 메모리 누수 등의 문제가 발생할 수도 있다.

## DispatchWorkItem를 사용하는 간단한 예제
Queue에 쌓인 작업의 순서가 필요없을 때, 빠르게 만들어 사용이 가능하다.

**Step1. 상단 옵셔널 변수 세팅**
**Step2. DispathWorkItem 세팅**
**Step3. DispatchWorkItem의 여부 체크**

DispatchWorkItem의 여부 체크 항상  DispathWorkItem 세팅 앞에 세팅
```swift
// Step1. 상단 옵셔널 변수 세팅
var delayedWorkItem: DispatchWorkItem?


func setDispatchQueue() {

    // 이부분에서 체크를 해주어야한다.
    cancelScheduleUIChanges()

    // Step2. DispathWorkItem 세팅
    delayedWorkItem = DispatchWorkItem {
        print("트랜지션 실행")
        label.font = UIFont.systemFont(ofSize: 10, weight: .regular)
        
        UIView.transition(with: label, duration: 0.5, options: .transitionCrossDissolve) {
            label.textColor = .darkGray
        }
        UIView.transition(with: button, duration: 0.5, options: .transitionCrossDissolve) {
            button.setImage(normalImage, for: .normal)
        }
    }
    print("트랜지션 예약")
    DispatchQueue.main.asyncAfter(deadline: .now() + 0.1, execute: delayedWorkItem!)
}

// Step3. DispatchWorkItem의 여부 체크
func cancelScheduleUIChanges() {
      if let workItem = delayedWorkItem {

          if !workItem.isCancelled {
              print("트랜지션 취소")
              workItem.cancel()
          }
      }
}
```
