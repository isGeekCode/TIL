# NSObject - Timer

타이머를 만들 수 있는 타입이다.

- 특정 시간이 지난 후 시작되어 지정된 메세지를 대상 객체로 보내는 타이머이다.
- 타이머를 생성할 때에는 반복 여부를 지정한다.
- 타이머는 Run Loop와 함께 작동하는데, Run Loop는 타이머에 대한 strong Reference를 유지하므로, Run Loop에 추가한 후 타이머에 대한 strong Reference를 유지할 필요가 없다.

## 반복 타이머

### @objc 함수이용하여 사용하기

- 동일한 런 루프에서 특정 TimeInterval 간격으로 실행한다
- 타이머 기능을 정지하려면 Invalidate() 메서드를 호출

```swift
let timer = Timer.scheduledTimer(timeInterval: 1.0, target: self, selector: #selector(startTimer), userInfo: nil, repeats: true)

// 타이머 시작
@objc func startTimer() {
  print("Timer Start!")
}

// 타이머 종료
func stopTimer() {
  timer.invalidate()
}
```

### 후행클로저를 이용하여 사용하기

```swift
let timer = Timer.scheduledTimer(withTimeInterval: 1.0, repeats: true) { timer in
  print("Timer Start!")
}
```

### 주요 프로퍼티

- `[isValid: Bool](https://developer.apple.com/documentation/foundation/timer/1408249-isvalid)`
    - 타이머가 현재 유효한지 여부를 나타내는 부울 값
- `fireDate: [Date](https://developer.apple.com/documentation/foundation/date)`
    - 타이머가 더 이상 유효하지 않은 경우 타이머가 실행된 마지막 날짜
- `[timeInterval: TimeInterval](https://developer.apple.com/documentation/foundation/timer/1409024-timeinterval)`
    - 타이머의 시간 간격(초)입니다.
- `[userInfo: Any?](https://developer.apple.com/documentation/foundation/timer/1408911-userinfo)`
    - 보낼 정보
    

## Userinfo사용하기

### 변수로 구현하기

userInfo에 들어갈 변수를 구현해서 넣어주면

selector함수안에서 내용을 옵셔널캐스팅하여 변수값도 변화시킬 수 있다.

```swift

class CustomTimerInfo {
    var count = 0
}

class ViewController {

var myTimerInfo = CustomTimerInfo()

  override func viewDidLoad() {
    
    _ = Timer.scheduledTimer(timeInterval: 1, target: self, selector: #selector(update), userInfo: myTimerInfo, repeats: true)

  }
  
  @objc func update(_ timer: Timer) {
         guard let timerInfo = timer.userInfo as? CustomTimerInfo else { return }

         timerInfo.count += 1
         print(timerInfo.count)
         print("myTImerInfo: \(myTimerInfo.count)")
     }

}
```

### Dictionary로 구현하기

또 아래처럼 selector함수를 Dictionary로도 구현할 수 있다.

```swift

let timer = Timer.scheduledTimer(timeInterval: 1.0, target: self, selector: #selector(update(timer:)), userInfo: ["score": 10], repeats: true)

public func update(timer: NSTimer)
{
    if  let userInfo = timer.userInfo as? [String: Int],
        let score = userInfo["score"] {
        print("You scored \(score) points!")
    }
}
```
