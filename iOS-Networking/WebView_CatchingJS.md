# WebView - 웹에서 앱으로 보내는 JavaScript 수신하기 : WKScriptMessageHandler

웹에서 앱으로 JavaScript를 보낼 수가 있다.

- 순서
    - WebView생성시 JavaScript메서드를 등록
    - WKScriptMessageHandler 프로토콜 메서드 구현

<br><br>

## 등록방법

WebView를 생성할 때 들어가는 변수는 아래와 같다. 
- 웹뷰의 frame
- configuration 


```swift

    var webView: WKWebView!


    func initWebView() {

        let configuration = WKWebViewConfiguration.init()
        let contentController = WKUserContentController()

        // js -> native
        contentController.add(LeakAvoider(delegate: self), name: "JavaScriptName")
        // 원래 아래 코드이지만 메모리 누수방지를 위해 LeakAvoider를 사용
        // contentController.add(self, name: "JavaScriptName")


        // JAVA InterFace
        configuration.preferences = preferences
        configuration.userContentController = contentController
        
        mainWebView = WKWebView(frame: .zero, configuration: configuration)
        
        // Constraint 부분 생략
}
```

<br><br>

## 등록된 JavaScript가 들어올때 동작을 세팅하는 부분

이때 javascript를 보낼때 message에 javascript를 보내고 body값을 원하는 형태로 파싱해서 사용한다.

- 타입이 맞지않으면 앱이 종료될 수 있으니 예외처리를 해주자

```swift
// MARK: - WKScriptMessageHandler
extension MainViewController: WKScriptMessageHandler {

    /// message name: javascript 명
    func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) {

        print("get message at main vc \(message.name)")

        if message.name == "JavaScriptName" {
            if let dict = message.body as? NSDictionary {
                if let moveUrlStr = dict["url"] as? String, let moveUrl = URL(string: moveUrlStr) {
                    print("이동할 URL:: \(moveUrl)")
                }
            }
        }
    }
}
```

<br><br>

## deinit을 하는 경우

화면이 여러개라면 메모리 누수를 방지하고자 ViewController의 deinit 시점에  
등록된 JavaScript들을 지워주는 것이 좋다. 

```swift

class ViewController: UIViewController {

    deinit {
        mainWebView.configuration.userContentController.removeScriptMessageHandler(forName: "myJavaScriptName")
    
        mainWebView.scrollView.delegate = nil
        mainWebView.uiDelegate = nil
        mainWebView.navigationDelegate = nil
        mainWebView = nil
    }
}
```

<br><br>

## LeakAvoider

WKScriptMessageHandler 프로토콜을 구현한 객체를   
WKUserContentController의 메시지 핸들러로 직접 추가하면,   
messageHandler가 WKUserContentController에 대한 강한 참조를 가지게 된다.   

이는 메시지 핸들러가 WKUserContentController 객체에 대한 참조를 끊지 않고 메모리에서 해제되지 않을 가능성이 있으며, 이로 인해 메모리 누수가 발생할 수 있다.  


LeakAvoider 클래스는 메시지 핸들러와의 강한 참조 대신 약한(weak) 참조를 사용하여 메모리 누수를 방지한다.  
LeakAvoider 객체가 WKScriptMessageHandler 객체를 가리키는 동안에만 메시지 핸들러가 메모리에 유지되고, LeakAvoider 객체가 해제되면 그에 따라 메시지 핸들러도 자동으로 메모리에서 해제된다.  

따라서 LeakAvoider라는 중개자 클래스를 사용하면 효율적으로 메모리 누수를 방지할 수 있다.  

### 코드 

```swift
import UIKit
import WebKit

/// WKScriptMessageHandler의 메모리 누수방지를 위한 클래스
class LeakAvoider: NSObject, WKScriptMessageHandler {
    weak var delegate: WKScriptMessageHandler?
    init(delegate: WKScriptMessageHandler) {
        self.delegate = delegate
        super.init()
    }

    func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) {
        self.delegate?.userContentController(userContentController, didReceive: message)
    }
}


// Objective - C 에서 사용하려면 아래처럼 @objc를 넣어주어야한다. 
import UIKit
import WebKit

/// WKScriptMessageHandler의 메모리 누수방지를 위한 클래스
@objc class LeakAvoider: NSObject, WKScriptMessageHandler {
    weak var delegate: WKScriptMessageHandler?
    
    @objc init(delegate: WKScriptMessageHandler) {
        self.delegate = delegate
        super.init()
    }

    @objc func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) {
        self.delegate?.userContentController(userContentController, didReceive: message)
    }
}



// Objective -c 로 구현하는경우

// LeakAvoider.h
#import <WebKit/WebKit.h>

@interface LeakAvoider : NSObject<WKScriptMessageHandler>

@property (nonatomic, weak) id<WKScriptMessageHandler> delegate;

- (instancetype)initWithDelegate:(id<WKScriptMessageHandler>)delegate;

@end

// LeakAvoider.m
#import "LeakAvoider.h"

@implementation LeakAvoider

- (instancetype)initWithDelegate:(id<WKScriptMessageHandler>)delegate {
    self = [super init];
    if (self) {
        self.delegate = delegate;
    }
    return self;
}

- (void)userContentController:(WKUserContentController *)userContentController didReceiveScriptMessage:(WKScriptMessage *)message {
    [self.delegate userContentController:userContentController didReceiveScriptMessage:message];
}

@end
```


Objective - c 에서 적용을 해야한다면 아래와 같이 세팅한다.

```swift

LeakAvoider *leakAvoider = [[LeakAvoider alloc] initWithDelegate:self];
[contentController addScriptMessageHandler:leakAvoider name:@"MyJavaScriptName"];

```

<br><br>

### History

- 231006 : 내용 수정
