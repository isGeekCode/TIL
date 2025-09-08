# UIAlertView Deprecated in iOS 9, Replaced by UIAlertController in iOS 10.0

```
'UIAlertView' is deprecated: first deprecated in iOS 9.0 - UIAlertView is deprecated. Use UIAlertController with a preferredStyle of UIAlertControllerStyleAlert instead
```

<br><br>

UIAlertView는 iOS에서 사용되던 클래스로, 사용자에게 정보를 제공하거나, 사용자로부터 간단한 입력을 받기 위한 경고창을 표시하는 데 사용되었다.
  
그러나 UIAlertView는 iOS 9부터 사용이 중단되었으며,  
그 기능은 iOS10.0부터 등장한 UIAlertController에 의해 대체되었다.  
UIAlertController를 사용하면 경고창(alert) 또는 액션 시트(action sheet) 형태의 인터페이스를 구현할 수 있다.  

<br><br>

## AlertView

AlertView를 기본 세팅에서 다시 사용해보려고 했지만,  
아래 메서드와 함께 APP이 강제 종료된다.  
```
Thread 1: "UIAlertView is deprecated and unavailable for UIScene based applications, please use UIAlertController!"
```

AlertView는 AppDelegate에서만 동작하기 때문에 SceneDelegate환경이라면 SceneDelegate를 지우고 진행해야한다.  

- [ScenDelegate를 없애는 방법](https://h1guitar.tistory.com/144)

  <img width="300" alt="IMG_8317" src="https://github.com/isGeekCode/TIL/assets/76529148/e5c68420-6c31-4c96-afc7-0511c46d4392">  

<br><br>

### 선언방법

```swift
// Swift
let alertView = UIAlertView(title: "제목",
                            message: "메시지",
                            delegate: self,
                            cancelButtonTitle: "취소",
                            otherButtonTitles: "확인")
alertView.show()


// Objc
UIAlertView *alertView = [[UIAlertView alloc] initWithTitle:@"제목"
                                                    message:@"메시지"
                                                   delegate:self
                                          cancelButtonTitle:@"취소"
                                          otherButtonTitles:@"확인"];
[alertView show];
```

<br><br>

### 동적으로 버튼 추가하기

  <img width="300" alt="IMG_8320" src="https://github.com/isGeekCode/TIL/assets/76529148/eabf3bab-663e-4467-bd02-f7f475205083">  

```swift
// Swift
let alertView = UIAlertView(title: "제목",
                            message: "메시지",
                            delegate: self,
                            cancelButtonTitle: "취소",
                            otherButtonTitles: "확인")
let buttons = ["버튼1", "버튼2", "버튼3"]

for button in buttons {
    alertView.addButton(withTitle: button)
}

alertView.show()



// Objc
UIAlertView *alertView = [[UIAlertView alloc] initWithTitle:@"제목"
                                                    message:@"메시지"
                                                   delegate:self
                                          cancelButtonTitle:@"취소"
//                                        otherButtonTitles:@"확인"];
                                          otherButtonTitles:nil];

NSArray *buttons = @[@"버튼1", @"버튼2", @"버튼3"];
for (NSString *buttonTitle in buttons) {
    [alertView addButtonWithTitle:buttonTitle];
}

[alertView show];
```

### AlertViewDelegate

선택한 버튼에 대한 동작 정의하기
```swift
// swift
extension ViewController: UIAlertViewDelegate {
    
    func alertView(_ alertView: UIAlertView, clickedButtonAt buttonIndex: Int) {
        if buttonIndex == alertView.cancelButtonIndex {
            print("취소 버튼이 눌렸습니다.")
        } else {
            print("다른 버튼이 눌렸습니다.")
        }
        
        // 버튼 인덱스가져오기
        print("\(buttonIndex) 버튼이 눌렸습니다.")
        
        if (buttonIndex == 0) {
            // 취소버튼
            NSLog("취소 버튼의 액션")
        } else if (buttonIndex == 1) {
            NSLog("첫번째 버튼의 액션")
        } else {
            NSLog("나머지 버튼의 액션")
        }

        // 버튼 텍스트가져오기
        let buttonTitle = alertView.buttonTitle(at: buttonIndex)
        print("\(buttonTitle ?? "") 버튼이 눌렸습니다.")
    }
}




//objc

#import "ViewController.h"

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    
    UIAlertView *alertView = [[UIAlertView alloc] initWithTitle:@"제목"
                                                        message:@"메시지"
                                                       delegate:self
                                              cancelButtonTitle:@"취소"
//                                              otherButtonTitles:@"확인"];
                                              otherButtonTitles:nil];

    NSArray *buttons = @[@"버튼1", @"버튼2", @"버튼3"];
    for (NSString *buttonTitle in buttons) {
        [alertView addButtonWithTitle:buttonTitle];
    }

    [alertView show];
}


@end


@implementation ViewController (AlertViewDelegate)

- (void)alertView:(UIAlertView *)alertView clickedButtonAtIndex:(NSInteger)buttonIndex {
    // UIAlertViewDelegate 메서드 구현
    if (buttonIndex == alertView.cancelButtonIndex) {
        NSLog(@"취소 버튼이 눌렸습니다.");
    } else {
        NSLog(@"다른 버튼이 눌렸습니다.");
    }
    
    if (buttonIndex == alertView.firstOtherButtonIndex) {
        NSLog(@"첫 번째 '기타 버튼'이 눌렸습니다.");
    }
    
    // 버튼 인덱스 가져오기
    NSLog(@"%ld번째 버튼이 눌렸습니다.", (long)buttonIndex);
    
    if (buttonIndex == 0) {
        // 취소버튼
        NSLog(@"취소 버튼의 액션");
    } else if (buttonIndex == 1) {
        NSLog(@"첫번째 버튼의 액션");
    } else {
        NSLog(@"나머지 버튼의 액션");
    }

    
    // 버튼 텍스트 가져오기
    NSString *buttonTitle = [alertView buttonTitleAtIndex:buttonIndex];
    NSLog(@"'%@' 버튼이 눌렸습니다.", buttonTitle);
}

@end
```





## History
- 231208: 초안작성

