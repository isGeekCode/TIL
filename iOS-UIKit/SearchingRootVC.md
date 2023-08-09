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


```SWIFT
let sceneDelegate = UIApplication.shared.connectedScenes.first?.delegate as? SceneDelegate
if let rootViewController = sceneDelegate?.window?.rootViewController {
    // rootViewController를 사용하여 필요한 작업 수행
}

```

<br><br><br>

### iOS13 이후, isKeyWindow 사용하여 찾기


```SWIFT
let window = UIApplication.shared.windows.filter { $0.isKeyWindow }.first
if let rootViewController = window?.rootViewController {
    // rootViewController를 사용하여 필요한 작업 수행
}

```

## History
- 230809: 초안작성
