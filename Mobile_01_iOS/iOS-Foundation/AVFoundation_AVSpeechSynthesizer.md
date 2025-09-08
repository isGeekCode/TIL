# AVFoundation - TTS : Text-To-Speech

이 기능은  iOS10부터 가능하다.

### 기억해야할 것

- AVSpeechSynthesizer객체는 UIViewController내부에서 초기에 변수로 정의되어있어야한다.

만약 함수안에서 로컬변수로 선언되면, 함수가 실행될때마다 새로운 AVSpeechSynthesizer를 생성한다. 그 과정에서 함수가 실행을 마치면 AVSpeechSynthesizer 인스턴스가 해제될 수 있다.

그래서 초기에 인스턴스 변수로 세팅을 하여 ViewController의 생명주기와 일치하게 세팅을 해주어야한다.


### 간단한 사용법
- 코드 구현

```swift
import UIKit
import AVFoundation


class ViewController: UIViewController {

    let synthesizer = AVSpeechSynthesizer()

    override func viewDidLoad() {
        super.viewDidLoad()
    }

    @IBAction func speakButtonTapped(_ sender: UIButton) {
            speakText()
    }

    func speakText() {


        let utterance = AVSpeechUtterance(string: "your string")

        utterance.voice = AVSpeechSynthesisVoice(language: "en-US")
        
        // 속도 지정 : (between 0.0 and 1.0)
        utterance.rate = 0.4
        
        // 소리의 높낮이 지정 : (between 0.0 and 2.0)
        utterance.pitchMultiplier = 0.7

        synthesizer.speak(utterance)
    }
}
```


### 프로퍼티

- rate : 속도 - between 0.0 and 1.0
- pitchMultiplier : 높낮이 - between 0.0 and 2.0
