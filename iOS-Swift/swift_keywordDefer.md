# Swift - 키워드 defer

defer는 Swift에서 사용되는 특별한 키워드이다. defer 블록에 작성된 코드는 해당 범위가 종료되는 시점에 실행된다. 범위는 함수 또는 메소드, 반복문, 조건문, switch-case문 등이 될 수 있다.


## 사용예

```swift
func fetchData() {
    startActivityIndicator() // 로딩 시작

    defer {
        stopActivityIndicator() // 함수가 끝날 때 로딩 뷰 종료
    }

    // 데이터를 가져오는 코드 (시간이 걸리는 작업)

    print("Data fetched")
}

```


```swift
self.startActivityIndicator()

let stampManager = StampApiManager()

stampManager.fetchNow { [weak self] result in
    // 모든 상황에서 Activity Indicator를 중지.
    defer { self?.stopActivityIndicator() }
    
    switch result {
    case .success(let result):
        print("result is : \(result)")
    case .failure(let error):
        print("An error occurred: \(error.localizedDescription)")
    }

    guard let self = self else { return }

    let layoutVC = LayoutViewController()
    self?.pushViewController(present: self?, viewController: layoutVC, completion: nil)
}

```

### 함수의 종료시점

```swift
func processFile(filename: String) throws {
    let file = openFile(filename)
    defer {
        closeFile(file)
    }
    
    while let line = try file.readline() {
        // 파일 처리 작업
    }
    // closeFile은 여기에서 호출된다.
}


func sayHelloThenGoodbye() {
    print("Hello")

    defer {
        print("Goodbye")
    }

    print("Nice to meet you")
}

/*
Hello
Nice to meet you
Goodbye

*/

```



### 함수의 종료시점

```swift
func processFile(filename: String) throws {
    let file = openFile(filename)
    defer {
        closeFile(file)
    }
    
    while let line = try file.readline() {
        // 파일 처리 작업
    }
    // closeFile은 여기에서 호출된다.
}
```

### if에서의 종료시점

```swift
func calculate(value: Int) {
    if value > 10 {
        print("Start processing value greater than 10")
        defer {
            print("End processing value greater than 10")
        }
        // 계산 코드
    } else {
        print("Start processing value not greater than 10")
        defer {
            print("End processing value not greater than 10")
        }
        // 다른 계산 코드
    }
}

```




### switch에서의 defer (모두 다른 곳에서의 defer)
```swift
func process(trafficLight: String) {
    switch trafficLight {
    case "red":
        print("Stop")
        defer {
            print("Stopped at red light.")
        }
        // 여기에 빨간 신호에 대한 추가 처리를 적어주세요.
    case "yellow":
        print("Prepare to stop")
        defer {
            print("Prepared to stop at yellow light.")
        }
        // 여기에 노란 신호에 대한 추가 처리를 적어주세요.
    case "green":
        print("Go")
        defer {
            print("Went at green light.")
        }
        // 여기에 초록 신호에 대한 추가 처리를 적어주세요.
    default:
        print("Invalid traffic light color")
        defer {
            print("Handled invalid traffic light color.")
        }
        // 여기에 유효하지 않은 신호색에 대한 추가 처리를 적어주세요.
    }
}
```

### switch에서의 defer (모두 동일한 defer)
```swift
func process(trafficLight: String) {
    defer {
        print("The traffic light processing has completed.")
    }
    
    switch trafficLight {
    case "red":
        print("Stop")
        // 여기에 빨간 신호에 대한 추가 처리를 적어주세요.
    case "yellow":
        print("Prepare to stop")
        // 여기에 노란 신호에 대한 추가 처리를 적어주세요.
    case "green":
        print("Go")
        // 여기에 초록 신호에 대한 추가 처리를 적어주세요.
    default:
        print("Invalid traffic light color")
        // 여기에 유효하지 않은 신호색에 대한 추가 처리를 적어주세요.
    }
}

```

### for문에서의 defer

```swift
for i in 1...5 {
    defer {
        print("End of iteration \(i)")
    }
    print("Start of iteration \(i)")
}
z
/*
Start of iteration 1
End of iteration 1
Start of iteration 2
End of iteration 2
Start of iteration 3
End of iteration 3
Start of iteration 4
End of iteration 4
Start of iteration 5
End of iteration 5
*/
```

