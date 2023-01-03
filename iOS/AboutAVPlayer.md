# AVPlayer 사용하기

Avplayer는 AVfoundation 을 import하여 사용한다. 

따로 AVPlayerController를 이용할 수도 있다.

### 파일이름으로 사용하기

```swift
guard let path = Bundle.main.path(forResource: "videoTest", ofType: "mp4") else { return }
var player = AVPlayer(url: URL(fileURLWithPath: path))
let playerLayer = AVPlayerLayer(player: player)
playerLayer.frame = self.splashImageView.frame
self.layer.addSublayer(playerLayer)
playerLayer.videoGravity = .resizeAspect
play()
```

### URL로 사용하기

```swift
guard let pathURL = URL(string: "http://www.test.com/videotest.mp4") else {return}
var player = AVPlayer(url: customURL)
let playerLayer = AVPlayerLayer(player: player)
playerLayer.frame = self.splashImageView.frame
self.layer.addSublayer(playerLayer)
playerLayer.videoGravity = .resizeAspect
player.play()
```

# AVPlayerItem

AVPlayer 자체만 생성하고 재생할 item을 따로 만들어 바꿔줄 수 있다.

AVPlayer를 init할때 자동으로 기본 AVplayerItem이 생성되기때문에 ‘바꿔’준다.

### AvplayerItem Init / replaceCurrentItem

```swift
var player = AVPlayer()

playerLayer.frame = self.splashImageView.frame // setConstraints
self.layer.addSublayer(playerLayer)            // addSubLayer
playerLayer.videoGravity = .resizeAspect       // setAspect

// setURL
guard let path = Bundle.main.path(forResource: "videoTest", ofType: "mp4") else { return }
let customPlayerItem = AVPlayerItem(url: pathURL)
player.replaceCurrentItem(with: customplayerItem)

player.play()
```

이미 생성한 다음에는 재생할 item을 따로 만들어서 바꿔 사용이 가능하다. 

```swift
guard let path = Bundle.main.path(forResource: "videoTest", ofType: "mp4") else { return }
var player = AVPlayer(url: URL(fileURLWithPath: path))

playerLayer.frame = self.splashImageView.frame // setConstraints
self.layer.addSublayer(playerLayer)            // addSubLayer
playerLayer.videoGravity = .resizeAspect       // setAspect

// new Item init
guard let pathURL = URL(string: "http://www.test.com/videotest.mp4") else {return}
let customPlayerItem = AVPlayerItem(url: pathURL)
player.replaceCurrentItem(with: customplayerItem)

player.play()
```

## Video Gravity

- resize
    - 비디오가 늘어나 레이어의 경계를 채운다. 비율변경됨.
- resizeAspect
    - 비율을 유지하고 레이어 경계내에서만 유지
    - 화면 가로세로축이 맞지않아 player바깥은 하위 뷰계층이 보이기때문에 isHidden을 고려할 것
- resizeAspectFill
    - 비디오의 비율을 유지하고 레이어의 경계를 채운다. 가운데만 표시됨.

# 종료를 제어하기위한 3가지 방법

## 1. Notification

기본적으로 NotificationCenter 에서 AVPlayer와 관련된 함수를 캐치할 수 있다.

이중에 종료관련해서는 `NSNotification.Name.AVPlayerItemDidPlayToEndTime` 를 통해 영상이 끝까지 재생되었는지 확인할 수 있다.

```swift
// set Notification
NotificationCenter.default.addObserver(self, selector: #selector(didEndPlayAction(_:)), name: NSNotification.Name.AVPlayerItemDidPlayToEndTime, object: nil)

@objc func didEndPlayAction(_ notification: Notification) {
  print("didEndPlayAction")
}
```

## 2.  MainThread에서 제어하여 특정시간만큼 보여주기

같은 시점에서 해주기위해 동일한 쓰레드에서 실행하였다.

```swift
DispatchQueue.main.async {
        self.player.play()
            
        DispatchQueue.main.asyncAfter(deadline: .now() + 2 {
                self.player.pause()
        }
}
```

## 3. addBoundaryTimeObserver로 시간제어하기

이 함수는 CMTime이라는 시간을 나타내는 구조체를 통해 특정시점을 세팅하고 캐치할 수 있게 한다. 

CMTime을 NSValue로 파싱하고 그걸 Array에 담아 파라미터로 사용한다. 

```swift
let player = AVPlayer()

// AVPlayerLayer Init
let playerLayer = AVPlayerLayer(player: player)
playerLayer.frame = self.splashImageView.frame
self.layer.addSublayer(playerLayer)
playerLayer.videoGravity = .resizeAspect

// set Path
let urlString = "https://www.geekcode.com"
guard let customURL = URL(string: urlString) else {return}
let customPlayerItem = AVPlayerItem(url: customURL)
self.player.replaceCurrentItem(with: customPlayerItem)

// 캐치할 시간 세팅
let targetCMTime = CMTime(seconds: duration, preferredTimescale: 1)
//        let seconds = CMTimeGetSeconds(targetCMTime)
//        print("seconds: \(seconds)")
let timeNSValue = NSValue(time: targetCMTime)
let targetTimeArray = [timeNSValue]
let mainQueue = DispatchQueue.main

player.addBoundaryTimeObserver(forTimes: targetTimeArray, queue: mainQueue) {
        // 캐치하는 시점에 실행할 함수세팅
    self.splashViewDismiss() // dismiss처리함수
}
self.player.play()
```

어레이에 여러 시간을 세팅이 가능하다

```swift
let targetNSValue = NSValue(time: CMTime(seconds: 6, preferredTimescale: 1))
let targetNSValue2 = NSValue(time: CMTime(seconds: 2, preferredTimescale: 1))
let targetNSValue3 = NSValue(time: CMTime(seconds: 4, preferredTimescale: 1))

var targetTimeArray = [targetNSValue]
targetTimeArray.append(targetNSValue2)
targetTimeArray.append(targetNSValue3)

let mainQueue = DispatchQueue.main

        
player.addBoundaryTimeObserver(forTimes: targetTimeArray, queue: mainQueue) {
    print("캐치")
    self.player.pause()
//    테스트 
//    DispatchQueue.main.asyncAfter(deadline: .now() + 3) {
//        self.player.play()
//    }
}
self.player.play()
```

Audio 관련 참고

[https://wlgusdn700.tistory.com/82](https://wlgusdn700.tistory.com/82)
