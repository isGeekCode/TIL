# Objc - Objc 프로젝트에서 Swift 라이브러리 사용하기



1. Swift 파일 생성
파일생성시 브릿지헤더를 생성할 건지 Xcode에서 자동으로 물어보는데 수락하자.


2. Swift 라이브러리 같은 경우는 이렇게 싱글톤 객체를 생성하여 사용가능하다. NSObject를 상속받아 구현한다. 

 
Objective-C 파일에서 Swift 파일의 소스를 사용하고 싶다면, Swift에서 @objc 어노테이션을 붙여주면 된다.
```swift
@objc class KakaoManagerV2: NSObject {
    
    @objc static let shared = KakaoManagerV2.init()
    
    override init() {
        super.init()
    }
}
```

3. 사용할 Objective-C 파일에서 Swift import하기
사용할 파일의 상단에서 `프로젝트이름-Swift.h`의 형태로 기입한다.

```swift
#import "프로젝트이름-Swift.h"

```

4. Bridging header 파일 생성
만약 없다면 생성해주자. 파일명은 `프로젝트이름-Bridging-Header`의 형태로 입력한다. 
1번에서 만약 자동으로 생성했다면 경로도 자동으로 잡아줄 것이다. 

Objective-c프로젝트에서 Swift파일을 가져와서 사용할때는 사실 브릿징헤더가 필요없어 보이지만....
있어야한다. 빈칸으로 두지만.. 파일이 있어야 정상 작동한다. 


5. 생성한 싱글턴 객체로 사용하기

```swift
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    
    // 아래처럼 사용
    [[KakaoManagerV2 shared] getInitSDKWithAppKey:@"앱키"];
```
