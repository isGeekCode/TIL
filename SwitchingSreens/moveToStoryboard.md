# present - CodeUI to StoryBoard

이번에 빠르게 작업을 했었던 사례였다.

첫번째 페이지: ViewController1 - 코드 UI

두번째 페이지: ViewController2 - 스토리보드 UI

두번째 페이지같은 경우는 반복사용해야하는 경우도 많고 시간이 촉박하기때문에 스토리보드를 선택하게 되었는데 문제는 화면전환에서 발생했다.

일단 세팅을 따로 하지않으면 ViewController.swift에 구현한 상태로 연결이 되기 때문에 텅텅빈 두번째 페이지를 만나게 된다.

## 구현방법

### Step1. `ViewController2.swift` 에서 구분용 변수 세팅

- storyboardName
- storyboardID

```swift
// ViewController2.swift

import Foundation
import UIKit

class ViewController2: UIViewController {
    let storyboardName = "Main"
    let storyboardID = "VC2"
}
```

### Step2. 스토리보드에서 세팅

- storyboardID
- **inherit Module From Target  체크필수‼️‼️**

### Step3. `ViewController1.swift` 에서 화면전환 구현

```swift
//
//  ViewController1.swift
//
//

import UIKit

class ViewController1: UIViewController {

    //MARK: 이동처리할 함수
    func presentVC2() {
    
        let vc = ViewController2()
        let storyboardName = vc.storyboardName
        let storyboardID = vc.storyboardID
    
        let storyboard = UIStoryboard(name: storyboardName, bundle: Bundle.main)
        let viewController = storyboard.instantiateViewController(identifier: storyboardID)
    
        present(viewController, animated: true)
    }
}
```

## 로직설명

- 첫 번째 ViewController에서 Storyboard를 가지고 화면 초기화
- storyboard객체를 storyboardName을 가지고 탐색
- storyboard안에 기입한 storyboardID를 가지고 ViewController 초기화
- storybaordName은 Storyboard파일 이름이며, storyboardID는 ViewController의 ID를 의미

++++++++++++++++++++++++++++

### TODO

- nib을 사용하는 경우도 추가하기
- MVVM일경우 추가 공부필요
    
    [https://ios-development.tistory.com/214](https://ios-development.tistory.com/214)
