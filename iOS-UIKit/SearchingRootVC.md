# UIKit에서 RootViewController 찾기


### iOS13 이전 AppDelegate 이용

```SWIFT
if let appDelegate = UIApplication.shared.delegate as? AppDelegate {
    if let rootViewController = appDelegate.window?.rootViewController {
        // rootViewController를 사용하여 필요한 작업 수행
    }
}
```

<br><br><br>

### iOS13 이후, SceneDelegate의 connectedScenes 사용하여 찾기

- 1. 앱의 첫 번째 연결된 UIWindowScene의 delegate를 가져오고,   

- 2. 이 delegate가 SceneDelegate 타입인지 확인  

- 3. 해당 SceneDelegate의 window?.rootViewController를 사용하여 rootViewController를 얻어오는 방식  


이 방법은 멀티 창 환경을 고려하여 SceneDelegate를 통해 각각의 윈도우에 접근하고 그에 따른 뷰 컨트롤러를 가져오는 방식이다.



```SWIFT
let sceneDelegate = UIApplication.shared.connectedScenes.first?.delegate as? SceneDelegate
if let rootViewController = sceneDelegate?.window?.rootViewController {
    // rootViewController를 사용하여 필요한 작업 수행
}

```

<br><br><br>

### iOS13 이후, isKeyWindow 사용하여 찾기

- 1. 앱 내에서 키 윈도우를 찾아서  
- 2. 그 윈도우의 rootViewController를 가져오는 방식  

 키 윈도우는 현재 사용자 입력을 받는 활성화된 창을 나타내며,  
 
예를 들어 터치나 키보드 입력이 해당 창으로 전달된다.  
  
이 방식은 현재 활성화된 창의 rootViewController에 접근하는 데 사용된다.


<br><br>


```SWIFT
let window = UIApplication.shared.windows.filter { $0.isKeyWindow }.first
if let rootViewController = window?.rootViewController {
    // rootViewController를 사용하여 필요한 작업 수행
}

```

## History
- 230809: 초안작성
