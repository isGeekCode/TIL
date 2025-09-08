# 볼륨버튼 캐치하기

- 방법1. NotificationCenter 이용하기
- 방법2. KVO 이용하기
    - 현대적 KVO 사용법
    - 전통적 KVO 사용법

## 방법1. NotificationCenter 이용하기
iOS14 이전에는 시스템 볼륨 변경에 대한 Notification name인
`AVSystemController_SystemVolumeDidChangeNotification` 를 이용해 
노티피케이션을 받았다.  

그리고 iOS15부터는 `SystemVolumeDidChange`로 Notification name이 변경됐지만,
Apple에서는 KVO를 활용하기를 권고한다.  

```swift

import UIKit
import MediaPlayer

class ViewController: UIViewController {
    
    private let volumeView = MPVolumeView()
    private var lastVolumeChangeTime: Date?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        if #available(iOS 15, *) {
            NotificationCenter.default.addObserver(self, selector: #selector(volumeChanged(_:)), name: NSNotification.Name(rawValue: "SystemVolumeDidChange"), object: nil)
        } else {
            NotificationCenter.default.addObserver(self, selector: #selector(volumeChanged(_:)), name: NSNotification.Name(rawValue: "AVSystemController_SystemVolumeDidChangeNotification"), object: nil)
        }
    }
    
    @objc func volumeChanged(_ notification: NSNotification) {
        if #available(iOS 15, *) {
            volumeControlIOS15(notification)
        }
        else {
            volumeControlIOS14(notification)
        }
    }
    
    func volumeControlIOS14(_ notification: NSNotification) {
        if let volume = notification.userInfo!["AVSystemController_AudioVolumeNotificationParameter"] as? Float {
            print("volumeControlIOS14 :: \(volume)")
        }
    }
    
    func volumeControlIOS15(_ notification: NSNotification) {
        if processVolumeChangeIfNeeded() {
            if let volume = notification.userInfo!["Volume"] as? Float {
                print("volumeControlIOS15 :: \(volume)")
            }
        }
    }
    
    /// IOS15 이후부터 사용가능한 Notification이 두번 호출되는 현상을 캔슬처리
    private func processVolumeChangeIfNeeded() -> Bool {
        let now = Date()
        // 마지막 변경 시간과 현재 시간을 비교.
        if let lastChange = lastVolumeChangeTime,
           now.timeIntervalSince(lastChange) < 0.1 {
            // 마지막 변경 이후 시간이 매우 짧다면 이 호출을 무시하고, 처리하지 않음.
            return false
        } else {
            // 마지막 변경 시간을 업데이트하고, 처리할 준비가 되었음을 리턴.
            lastVolumeChangeTime = now
            return true
        }
    }
    
    deinit {
        NotificationCenter.default.removeObserver(self)
    }
}




```


## 방법2. KVO 이용하기

### 현대적 KVO 사용법
```swift
import UIKit
import AVFoundation

class ViewController: UIViewController {
    
    private var volumeObservation: NSKeyValueObservation?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        let audioSession = AVAudioSession.sharedInstance()
        
        // 오디오 세션 활성화
        do {
            try audioSession.setActive(true)
        } catch {
            print("Audio Session Activation Error: \(error)")
        }
        
        volumeObservation = audioSession.observe(\.outputVolume) { [weak self] (session, changes) in
            guard let self = self else { return }
            let newVolume = session.outputVolume
            // 볼륨 변화에 따른 동작
            print("newVolume::: \(newVolume)")
        }
    }

    deinit {
        // 관찰자 제거
        volumeObservation?.invalidate()
    }
}

```

### 전통적인 KVO 사용하기

```swift
import UIKit
import AVFoundation

class ViewController: UIViewController {
    
    // 볼륨 관찰을 위한 컨텍스트
    private var volumeContext = 0
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 오디오 세션 인스턴스 가져오기
        let audioSession = AVAudioSession.sharedInstance()
        
        // 오디오 세션 카테고리 설정
        do {
            try audioSession.setCategory(.playback, mode: .default)
            try audioSession.setActive(true)
        } catch {
            print("Audio Session Error: \(error)")
        }
        
        // 볼륨 관찰자 추가
        audioSession.addObserver(self,
                                 forKeyPath: "outputVolume",
                                 options: [.new],
                                 context: &volumeContext)
    }
    
    override func observeValue(forKeyPath keyPath: String?,
                               of object: Any?,
                               change: [NSKeyValueChangeKey : Any]?,
                               context: UnsafeMutableRawPointer?) {
        // 볼륨 변경 감지
        if context == &volumeContext,
           keyPath == "outputVolume",
           let volumeChange = change?[.newKey] as? Float {
            // 볼륨 변경에 따른 UI 업데이트
            updateUI(forVolume: volumeChange)
        } else {
            super.observeValue(forKeyPath: keyPath, of: object, change: change, context: context)
        }
    }
    
    private func updateUI(forVolume volume: Float) {
        // 볼륨에 따라 UI 업데이트 로직
        print("Volume has changed to: \(volume)")
    }
    
    deinit {
        // 관찰자 제거
        AVAudioSession.sharedInstance().removeObserver(self, forKeyPath: "outputVolume", context: &volumeContext)
    }
}

```
