# Cocoa Design Pattern - Singleton (싱글톤 패턴)

싱글톤 패턴이란, 
특정 용도로 객체를 하나만 생성하여, 공용으로 사용하고 싶을 때 사용하는 디자인 패턴이다.

## 싱글톤 예시

아래처럼 클래스명을 그대로 담는다.
하지만 반드시 shared로 사용할 필요는 없다. 
원리상 또다른 객체를 만들지않고 한 객체만 계속해서 사용하는 것도 싱글톤이라고 할 수 있다.

### 생성방법
```swift
class Singleton {
    static let shared = Singleton()
    private init() {}
}
```
### 접근방법
```swift
let singleton = Singleton.shared
```

## 모델을 담고 있는 싱글톤 예시
### 생성방법

```swift
class Singleton {
    static let shared = Singleton()
    private init() {}
    
    var model: Model?
}
// 만약 class라면
class Model {
    let name: String
    
    init(name: String) {
        self.name = name
    }
}

// 만약 struct라면
struct Model {
    let name: String
    
    init(name: String) {
        self.name = name
    }
}
```

### 접근방법
```swift
Singleton.shared.model = Model(name: "My Model")
print(Singleton.shared.model?.name) 
```

## 싱글턴을 사용하는 이유
- 여러군데에서 정보를 수집해야할 때 용이하다.
- class가 참조타입인 것을 이용해 생성되어있는 곳에서는 어디에서든 같은 값을 가지게 된다.


## 특징

### static을 사용해 전역으로 저장한다. 
### init함수 접근제어자를 private으로 지정한다
혹시라도 init함수를 호출해서 Instance를 또 생성하는 것을 막기위해 
`init()`함수 생성자를 private 으로 지정해준다.

## 장단점

### 장점
- 한 번의 Instance만 생성하므로 메모리 낭비를 방지할 수 있음
- Singleton Instance는 전역 Instance로 다른 클래스들과 자원 공유가 쉬움
- DBCP(DataBase Connection Pool)처럼 공통된 객체를 여러개 생성해서 사용해야하는 상황에서 많이 사용 (쓰레드풀, 캐시, 대화상자, 사용자 설정, 레지스트리 설정, 로그 기록 객체등)
### 단점
- ingleton Instance가 너무 많은 일을 하거나, 많은 데이터를 공유시킬 경우 다른 클래스의 Instance들 간 결합도가 높아져 "개방=폐쇄" 원칙을 위배함 (객체 지향 설계 원칙 어긋남)
- 따라서 수정과 테스트가 어려워짐

## 다른 곳에서 사용하는 Singleton
다른 언어에서도 Singleton을 생성하는 것은 **Multi Threading 환경에서 Thread-Safe하지 않다.**

**여러 쓰레드가 만약 동시에 Singleton을 생성**하면, 경우에 따라 **Instance가 2개 3개 생성될 수도 있다.**

### Objc

→ **dispatch_once 사용**

```objectivec
@interface UserInfo : NSObject
 
+ (instancetype)sharedInstance;
 
@end
 
 
@implementation UserInfo
 
+ (instancetype)sharedInstance {
    static UserInfo *shared = nil;
 
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        shared = [[UserInfo alloc] init];
    });
 
    return shared;
}
 
@end
```

### Java

→ LazyHolder 사용

### Kotlin

→ Object / companion object 사용
→ SharedPreference : iOS의 userDefault와 같은 역할

### Swift

→ 따로 작업을 하지 않아도 static를 이용해 타입프로퍼티로 생성하면 사용시점에 초기화 (lazy) 된다.

그래서 Singleton Instance가 최초생성시까지 메모리에 올라가지않고  **dispatch_once가 자동으로 적용된다.** 

‼️ 싱글톤 생성에 있어서 아주 안전하다.


## 6. iOS에서 사용하는 Singleton들

자체적으로 싱글톤 선언되어있는 것들

```swift
let screen = UIScreen.main                     // 좌표공간, 앱 프레임, 스크린경계, 기기화면의 배율 (스케일)
let userDefault = UserDefaults.standard        // 앱 저장정보 : 앱을 껐다켜도 저장됨
let application = UIApplication.shared         // 현재 실행 중인 앱을 나타내는 객체
let fileManager = FileManager.default          // 앱마다 자기만의 공간을 가지고 있는데, 이 공간을 관리하는 매니저
let notification = NotificationCenter.default  // 앱 내에서 메세지를 던지면 아무데서나 이 메세지를 받을 수 있게 하는 역할
URLSession.shared.dataTask                     // 네트워크 작업을 위한 객체
UIApplication.shared.open(URL
URLCache.shared.removeAllCachedResponses       // 앱 전반에서 캐시된 데이터를 공유하고 관리
```
