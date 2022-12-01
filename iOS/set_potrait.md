# How to Set - 세로모드 고정

## Step1.

Project - General - Device Orientation - Potrait 체크

만약 여기서 해결이 안되는  경우, Step2 진행

## Step2.

```swift
// AppDelegate.swift

func application(_ application: UIApplication, supportedInterfaceOrientationsFor window: UIWindow?) -> UIInterfaceOrientationMask {
        
        // 세로방향 고정
        return UIInterfaceOrientationMask.portrait
    }
```
