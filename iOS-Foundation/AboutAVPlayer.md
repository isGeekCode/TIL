# AVFoundation - AVPlayer 사용하기

Avplayer는 AVfoundation 을 import하여 사용한다. 

따로 AVPlayerController를 이용할 수도 있다.

### 파일이름으로 사용하기

```swift
import UIKit
import AVKit
import AVFoundation

class ViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        playVideo()
    }

    func playVideo() {
        guard let path = Bundle.main.path(forResource: "fileName", ofType: "mp4") else { return }
        let filePathURL = URL(fileURLWithPath: path)
        let player = AVPlayer(url: filePathURL)
        let playerLayer = AVPlayerLayer(player: player)
        playerLayer.frame = self.view.bounds
        self.view.layer.addSublayer(playerLayer)
        playerLayer.videoGravity = .resizeAspect
        player.play()
    }
}
```

### URL로 사용하기

```swift
import UIKit
import AVKit
import AVFoundation

class ViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        playVideo()
    }

    func playVideo() {
        let urlPathStr = "http://down.humoruniv.com//hwiparambbs/data/editor/pdswait/e_s661a39001_c6c0d855eee53a714dbac585191e3e8bea0376ca.mp4"
        guard let urlPath = URL(string: urlPathStr) else { return }
        let player = AVPlayer(url: urlPath)
        let playerLayer = AVPlayerLayer(player: player)
        playerLayer.frame = self.view.bounds
        self.view.layer.addSublayer(playerLayer)
        playerLayer.videoGravity = .resizeAspect
        player.play()
    }
}
```

## AVPlayerViewController로 사용하기
AVPlayerViewController는 AVPlayer를 위한 기본 제공 사용자 인터페이스(UI)를 포함하는 뷰 컨트롤러다.  

이 방법은 비디오 재생을 위한 표준 컨트롤을 쉽게 제공하며, 전체 화면 재생과 같은 기능도 자동으로 처리한다.  

이때, 주의할 점은 AVPlayerViewControler를 호출하는 시점이 너무 빠르면 
아래와 같은 에러메세지가 발생한다.   

> Attempt to present <AVPlayerViewController: 0x10581b400> on <MoviePlayer.ViewController: 0x105207d90> (from <MoviePlayer.ViewController: 0x105207d90>) whose view is not in the window hierarchy
  
이 메세지는 현재 ViewController가 완전히 그려지지않았는데 ViewDidLoad에서 또 다른 VC를 Present한다고 발생하는 에러이다.  

그럴땐 아래 예시코드처럼 ViewDidAppear를 사용한다.  

```swift
class ViewController: UIViewController {
    
    func playVideo() {
        guard let path = Bundle.main.path(forResource: "dog", ofType: "mp4") else {
            print("비디오 파일을 찾을 수 없습니다.")
            return
        }
        
        let fileURL = URL(fileURLWithPath: path) 

        let player = AVPlayer(url: fileURL)
        let playerViewController = AVPlayerViewController()
        playerViewController.player = player

        present(playerViewController, animated: true) {
            player.play()
        }
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        
    }
    
    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
        playVideo()
    }
}

```

## AVPlayerLayer 직접 사용하기 (커스텀 UI)

AVPlayerLayer의 분리 사용은 추가적인 커스터마이징과 특정 미디어 재생 요구 사항에 대응하기 위한 유연성을 제공한다.  

표준 UI와 기능으로 충분한 경우, AVPlayerViewController를 사용하는 것이 더 간단하고 직관적일 수 있다.

또한 메서드 분리를 위해 전역변수로 만들 수 있겠다. 


아래처럼 버튼을 구현하기 위해 따로 분리

<img width="300" alt="스크린샷 2022-03-22 오후 1 32 04" src="https://github.com/isGeekCode/TIL/assets/76529148/54a0babd-ce30-47a9-85b4-b2be32670da5">

```swift
class ViewController: UIViewController {
    
    var player: AVPlayer?
    var playerLayer: AVPlayerLayer?
    
    //  Properties for Control
    var playPauseButton: UIButton!
    var timeLabel: UILabel!
    var progressSlider: UISlider!

    override func viewDidLoad() {
        super.viewDidLoad()
        setupPlayer()
        setupCustomControls()
    }

    func setupPlayer() {
        guard let path = Bundle.main.path(forResource: "dog", ofType: "mp4") else {
            print("비디오 파일을 찾을 수 없습니다.")
            return
        }
        let filePath = URL(fileURLWithPath: path) 
        
        player = AVPlayer(url: filePath)
        playerLayer = AVPlayerLayer(player: player)
        playerLayer?.frame = self.view.bounds
        if let playerLayer = self.playerLayer {
            self.view.layer.addSublayer(playerLayer)
        }
        player?.play()
    }

    override func viewDidLayoutSubviews() {
        super.viewDidLayoutSubviews()
        playerLayer?.frame = self.view.bounds
    }
    
    func setupCustomControls() {
        // 재생/일시 정지 버튼
        playPauseButton = UIButton(type: .system)
        playPauseButton.setImage(UIImage(systemName: "pause.fill"), for: .normal) // "playIcon"은 재생 이미지의 에셋 이름입니다.
        playPauseButton.addTarget(self, action: #selector(togglePlayPause), for: .touchUpInside)
        playPauseButton.frame = CGRect(x: 20, y: 100, width: 60, height: 30)
        self.view.addSubview(playPauseButton)

        // 시간 레이블
        timeLabel = UILabel(frame: CGRect(x: 20, y: 140, width: 100, height: 30))
        timeLabel.text = "00:00"
        self.view.addSubview(timeLabel)

        // 진행 상태 슬라이더
        progressSlider = UISlider(frame: CGRect(x: 20, y: 180, width: 300, height: 30))
        progressSlider.addTarget(self, action: #selector(sliderValueChanged), for: .valueChanged)
        self.view.addSubview(progressSlider)

        // 주기적으로 현재 재생 시간 업데이트
        let interval = CMTime(seconds: 1, preferredTimescale: CMTimeScale(NSEC_PER_SEC))
        player?.addPeriodicTimeObserver(forInterval: interval, queue: .main) { [weak self] time in
            let timeString = String(format: "%02d:%02d", Int(time.seconds / 60), Int(time.seconds.truncatingRemainder(dividingBy: 60)))
            self?.timeLabel.text = timeString
            if let duration = self?.player?.currentItem?.duration.seconds, duration > 0 {
                self?.progressSlider.value = Float(time.seconds / duration)
            }
        }
    }

    @objc func togglePlayPause() {
        if player?.rate == 0 {
            player?.play()
            playPauseButton.setImage(UIImage(systemName: "pause.fill"), for: .normal) // "pauseIcon"은 일시 정지 이미지의 에셋 이름입니다.
        } else {
            player?.pause()
            playPauseButton.setImage(UIImage(systemName: "play.fill"), for: .normal) // "pauseIcon"은 일시 정지 이미지의 에셋 이름입니다.
        }
    }

    @objc func sliderValueChanged() {
        if let duration = player?.currentItem?.duration {
            let totalSeconds = CMTimeGetSeconds(duration)
            let value = Float64(progressSlider.value) * totalSeconds
            let seekTime = CMTime(value: Int64(value), timescale: 1)
            player?.seek(to: seekTime)
        }
    }

}

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

### 어레이에 여러 시간 세팅하기

- 테스트 주석을 해제하면 정지하고 재생이 되는데 영상에서의 해당 시점에 도달하면 로그가 찍힌다. 
- 어레이의 순서에 상관없이 생성했던 타임라인에 따라 실행된다.
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
