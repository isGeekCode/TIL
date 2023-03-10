# NSObjet-UIResponder-UIView-UIImageView - 경로를 통해 이미지 다운로드하여 세팅하기
이미지를 Assets에 넣어서 사용하기도 하지만 URL을 통해 가져오는 경우가 있다.
이때 이미지를 다운로드하고 이미지를 세팅하는 동안 다른 작업을 해야하는 경우도 있다.
그땐 Sync처리가 되어있는경우 앱이 잠시 멈추는 듯한 상황이 생기기 때문에 동시에 여러작업이 수반되어야하는 경우는 특별히 스레드를 분배해주어야한다. 

```swift

    func loadImage(from imageUrl: String) -> UIImage? {

        guard let url = URL(string: imageUrl) else { return nil }
        guard let data = try? Data(contentsOf: url) else { return nil }

        let image = UIImage(data: data)
        return image

    }
```

## 비동기처리하는 경우
이미지 다운로드 자체는 global.async로 처리하고, UIImage의 이미지를 교체하는 것은 main.async에서 작업을 한다. 이렇게 되면 이작업 외에도 다른 작업들을 동시에 작업할 수가 있다.
```swift

    let downloadUrl = "http://www.naver.com"
    DispatchQueue.global().async {
        print("global().async로 이미지 다운로드 시작")
        let image = self.loadImage(from: downloadUrl)
        
        DispatchQueue.main.async {
            print("main.async로 이미지 변경")
            self.imageView.image = image
        }
    }
```

## 동기처리하는 경우
모두 Sync처리되어있어 이미지 다운로드가 되기전까지는 어떤 작업도 할수가 없다. 

```swift
    let downloadUrl = "http://www.naver.com"

    let image = loadImage(from: downloadUrl)
    imageView.image = image

```
