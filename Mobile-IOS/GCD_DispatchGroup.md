# GCD - DispatchGroup

DispatchGroup은 비동기 작업을 그룹화하고, 해당 그룹 내에서 모든 작업이 완료될 때까지 기다릴 수 있는 도구이다. 주로 여러 개의 비동기 작업을 추적하고, 모든 작업이 완료된 후에 추가적인 동작을 수행할 때 사용된다.

## 간단한 예시

### 예시 1: task
performAsyncTask1과 performAsyncTask2라는 두 개의 비동기 작업을 수행한다. group.enter()를 호출하여 각 작업이 시작됨을 알린다. 작업이 완료되면 group.leave()를 호출하여 작업이 완료되었음을 알린다.

group.notify(queue:)는 모든 작업이 완료된 후에 실행되는 클로저를 정의. 이 클로저는 모든 작업이 완료된 후에 호출되므로, "All tasks completed"라는 메시지를 출력한다.


```swift
let group = DispatchGroup()

group.enter()
performAsyncTask1 {
    print("Async Task 1 completed")
    group.leave()
}

group.enter()
performAsyncTask2 {
    print("Async Task 2 completed")
    group.leave()
}

group.notify(queue: .main) {
    print("All tasks completed")
}

// 비동기 작업 1
func performAsyncTask1(completion: @escaping () -> Void) {
    DispatchQueue.global().async {
        // 비동기 작업 수행
        // ...

        DispatchQueue.main.async {
            completion()
        }
    }
}

// 비동기 작업 2
func performAsyncTask2(completion: @escaping () -> Void) {
    DispatchQueue.global().async {
        // 비동기 작업 수행
        // ...

        DispatchQueue.main.async {
            completion()
        }
    }
}

```

### 예시 2: 이미지 다운로드

url1과 url2로부터 이미지를 다운로드하는 두 개의 비동기 작업이 있다. enter()를 호출하여 작업이 시작되었음을 알리고, 작업이 완료되면 leave()를 호출하여 작업이 완료되었음을 알린다.

group.notify(queue:)는 모든 작업이 완료되었을 때 실행되는 클로저를 정의. 이 클로저는 모든 이미지 다운로드 작업이 완료된 후에 실행한다. 이 예제에서는 단순히 "All images downloaded"라는 메시지를 출력하도록 되어 있다.



```swift
let group = DispatchGroup()

group.enter()
downloadImage(url: url1) { image in
    // 이미지 다운로드 완료
    print("Image 1 downloaded")
    group.leave()
}

group.enter()
downloadImage(url: url2) { image in
    // 이미지 다운로드 완료
    print("Image 2 downloaded")
    group.leave()
}

group.notify(queue: .main) {
    // 모든 이미지 다운로드 완료 후 실행
    print("All images downloaded")
}

func downloadImage(url: URL, completion: @escaping (UIImage?) -> Void) {
    DispatchQueue.global().async {
        // 이미지 다운로드 작업
        // ...

        // 다운로드 완료 후 호출
        DispatchQueue.main.async {
            completion(image)
        }
    }
}

```



### 예시 3: 이미지 다운로드

```swift
func viewDidLoad {

    let service = StampApiService()
        service.fetchNow { imagePathModels in
        
            for imagePathModel in imagePathModels {
                var listImages: [UIImage?] = []
                
                let imageType = imagePathModel.imageType
                
                let group = DispatchGroup()
                
                // normal 이미지 다운로드
                if let normalImageUrl = URL(string: imageType.normal.detailPath) {
                    group.enter()
                    downloadImage(with: normalImageUrl) { normalImage in
                        listImages.append(normalImage)
                        group.leave()
                    }
                }

                // on 이미지 다운로드
                if let onImageUrl = URL(string: imageType.on.detailPath) {
                    group.enter()
                    downloadImage(with: onImageUrl) { onImage in
                        listImages.append(onImage)
                        group.leave()
                    }
                }
                
                // off 이미지 다운로드
                if let offImageUrl = URL(string: imageType.off.detailPath) {
                    group.enter()
                    downloadImage(with: offImageUrl) { offImage in
                        listImages.append(offImage)
                        group.leave()
                    }
                }
                
                // 모든 이미지 다운로드 작업이 완료되면 작업 수행
                group.notify(queue: .main) {
                    // listImages 배열에 이미지가 추가되었으므로, 필요한 작업을 수행할 수 있다.
                    // 예를 들어, 이미지를 화면에 표시하거나 처리하는 등의 작업을 수행할 수 있다.
                    print("listImages: \(listImages)")
                }
                // ...

                // Use stickerArray for further processing or display
            }
        }
}

func downloadImage(with imageUrl: URL, completion: @escaping (UIImage?) -> Void) {
    DispatchQueue.global().async {
        if let imageData = try? Data(contentsOf: imageUrl),
           let image = UIImage(data: imageData) {
            DispatchQueue.main.async {
                completion(image)
            }
        } else {
            DispatchQueue.main.async {
                completion(nil)
            }
        }
    }
}

```


## History
- 230626 : 초안작성
