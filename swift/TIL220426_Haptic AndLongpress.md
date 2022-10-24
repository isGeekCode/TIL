# 롱프레스 및 햅틱진동 구현하기

- 롱프레스 시간은 3초로 지정
- 햅틱진동 구현
  - AudioToolbox 사용

\***\*1. AudioToolbox Framework 추가해주기\*\***

- **프로젝트 - General - Framework, Libraries, and Embedded Content**
- AudioToolbox.framework 찾아서 Add

1. **헤더파일추가하기**
   - swift: `Import`
   - objc : `#import <AudioToolbox/AudioToolbox.h>`
2. 진동메서드 구현

   1519, 1520, 1521

   - `AudioServicesPlaySystemSound(1520);`

진동메서드관련 소들이 블로그 참고

[https://babbab2.tistory.com/36](https://babbab2.tistory.com/36)

진동메서드관련 종류별 소개

[https://medium.com/@mavydasb/ios-haptic-feedback-for-iphone-7-and-6s-1bc6e7f1c285](https://medium.com/@mavydasb/ios-haptic-feedback-for-iphone-7-and-6s-1bc6e7f1c285)

Objective - c

```objectivec
#import <AudioToolbox/AudioToolbox.h>

//MARK: - ViewDidLoad

UILongPressGestureRecognizer *longPress = [[UILongPressGestureRecognizer alloc] initWithTarget:self action:@selector(longPress:)];
[self.selectServerButton addGestureRecognizer:longPress];
longPress.minimumPressDuration = 2;

//MARK: - Func
- (void)longPress:(UILongPressGestureRecognizer*)gesture {
    NSLog(@"longPressAct");
    AudioServicesPlaySystemSound(1520);
		// 구현할 기능 넣기
}
```

Swift

```swift
import AudioToolbox

//MARK: - ViewDidLoad

// add gesture recognizer
     let longPress = UILongPressGestureRecognizer(target: self, action: #selector(longPress(_:)))
     self.selectServerButton.addGestureRecognizer(longPress)
    // 롱프레스 시간설정
    longPress.minimumPressDuration = 2

//MARK: - Func

/// long press 제스쳐 인식
    @objc func longPress(_ guesture: UILongPressGestureRecognizer) {
        if guesture.state == UIGestureRecognizer.State.began {
            print("LongPressGesture is Recognized")
				    AudioServicesPlaySystemSound(1520);

            // 구현할 기능 넣기
        }
            return
      }
```
