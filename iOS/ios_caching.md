# IOS에 있어서 Caching
iOS에 있어서 캐싱이란
iOS기기에서 사용자가 앱을 사용하는 동안 데이터나 리소스를 저장하는 것을 말한다.  캐시는 데이터나 리소스를 반복적으로 다운로드할 필요가 없게 하고, 앱의 속도를 향상시키고, 네트워크 대역폭을 절약하게 할 수 있다.

일반적으로는 아래 4가지 방법을 사용한다.

- NSCache
- NSURLCache
- CoreData
- 라이브러리

## NSCache
객체를 메모리에 저장하는 캐시. 객체가 메모리에 남아있는 동안 앱에서 사용될 수 있다.

## NSURLCache
웹 리소스를 캐시하는 싱글턴 클래스. 네트워크를 통해 리소스를 다운로드하는 대신에 캐시에서 리소스를 불러올 수 있다.

### URLCache 인스턴스 생성하기
```swift
// URLCache 인스턴스 생성
let urlCache = URLCache.shared
```
### URLRequest를 사용하여 URL request 생성
```swift
// URLRequest 인스턴스 생성
if let url = URL(string: "https://example.com/image.jpg") {
    let request = URLRequest(url: url)
}
```
### URL request에 대한 Response 캐싱
URLSession으로 통신을 하고 결과값을 저장한다. 

```swift
// URLSession을 사용하여 데이터 요청
let task = URLSession.shared.dataTask(with: request) { (data, response, error) in
    if let error = error {
        print("Error: \(error)")
    } else if let data = data, let response = response as? HTTPURLResponse {
        // URL 요청에 대한 응답 캐싱
        let cachedResponse = CachedURLResponse(response: response, data: data)
        urlCache.storeCachedResponse(cachedResponse, for: request)
    }
}
task.resume()
```
### URL Request에 대한 캐시 검색
저장되어있던 response 캐시를 가져와서 데이터를 추출해 
필요한 타입으로 전환한다. 
아래코드는 data -> UIImage로 전환하는 코드이다. 
저장된 캐시가 없다면 URLSession을 이용해 데이터 다운로드를 실시한다. 

```swift
// URL 요청에 대한 캐시 검색
if let cachedResponse = urlCache.cachedResponse(for: request) {
    // 캐시된 응답 사용
    let data = cachedResponse.data
    let image = UIImage(data: data)
    DispatchQueue.main.async {
        self.imageView.image = image
    }
} else {
    // URL 요청으로부터 데이터 다운로드
    let task = URLSession.shared.dataTask(with: request) { (data, response, error) in
        if let error = error {
            print("Error: \(error)")
        } else if let data = data {
            DispatchQueue.main.async {
                // 이미지뷰에 이미지 설정
                let image = UIImage(data: data)
                self.imageView.image = image
            }
        }
    }
    task.resume()
}
```


```swift
```
## CoreData
iOS에서 데이터베이스를 사용하는 방법 중 하나. 앱의 데이터를 캐싱할 수 있다.

## 라이브러리를 이용한 이미지 캐싱 
이미지를 캐시하면 이미지를 다시 다운로드하지 않아도 되기 때문에 앱의 성능이 향상된다. 대표적으로는 SDWebImage, Kingfisher, AlamofireImage 등이 있다.
