# 라이브러리 - Kingfisher 사용하기
Kingfisher를 이용하면 이미지다운로드 중 gif도 세팅이 가능하다.
더 좋은 점은 이미지 캐싱이 가능하다는 것이다.

## 이미지 다운로드 하기
- gif도 동일하게 사용가능

```swift
guard let url = URL(string: urlString) else { return }

imageView.kf.setImage(with: url, options: .none){ result in
    switch result {
    case .success:
        print("Image download Success")

    case .failure(let error):
        print("Image download failed: \(error.localizedDescription)")
    }
}
```

## 이미지 캐시 삭제하기
### 모든 이미지 캐시 삭제
```swift
// Remove all.
cache.clearMemoryCache()
cache.clearDiskCache { print("Done") }

// Remove only expired.
cache.cleanExpiredMemoryCache()
cache.cleanExpiredDiskCache { print("Done") }
```

### 특정 URL 이미지 캐시 삭제

```swift
let url = URL(string: "http://example.com/image.jpg")!
KingfisherManager.shared.cache.removeImage(forKey: url.absoluteString)

```

### 모든 이미지 캐시 중, 만료된 캐시 삭제

```swift
KingfisherManager.shared.cache.cleanExpiredDiskCache()

```

혹은 앱 내 모든 URL 캐시데이터를 삭제하려면
```swift
URLCache.shared.removeAllCachedResponses()
```
