# 네트워킹 - 각종 URL의 유효성 검사

## 1. CanOpenURL을 통한 유효성검사
- URL(string:) 초기화를 시도하여 URL 객체를 생성한다. 이때 if let 구문을 사용하여 옵셔널 바인딩을 수행. 
- URL 객체가 생성되었다면 UIApplication.shared.canOpenURL(url) 메서드를 호출하여 해당 URL이 유효한지 검사한다. 
- canOpenURL(_:) 메서드는 해당 URL을 열 수 있는지 여부를 나타내는 부울 값을 반환한다.

```swift
func isValidUrl(_ urlString: String) -> Bool {
    if let url = URL(string: urlString) {
        return UIApplication.shared.canOpenURL(url)
    }
    return false
}

if isValidUrl("https://www.example.com") {
    // 유효한 URL
} else {
    // 유효하지 않은 URL
}
```
## 2. 이미지나 동영상 파일이 있는 경로에 접근하여 파일 URL인지 유효성 검사
- 입력받은 문자열이 파일 URL인지를 검사
- URL(string:)을 이용하여 URL 객체를 생성하고, 이 객체가 파일 URL인지를 검사. 
- 이후 FileManager 객체를 이용하여 파일이 실제로 존재하는지를 검사. 
- 파일이 존재하지 않거나, 파일 URL이 아닌 경우 false를 반환하고, 파일 URL이고 파일이 존재하는 경우에는 true를 반환.
```swift
func isValidFileUrl(_ fileUrlString: String) -> Bool {
    guard let fileUrl = URL(string: fileUrlString) else {
        return false // URL 초기화 실패
    }
    
    let fileManager = FileManager.default
    if !fileManager.fileExists(atPath: fileUrl.path) {
        return false // 파일이 존재하지 않음
    }
    
    if let urlScheme = fileUrl.scheme, urlScheme.hasPrefix("http") {
        // HTTP나 HTTPS URL이면 다운로드 가능
        return true
    } else {
        // HTTP나 HTTPS URL이 아닌 경우 다운로드 불가능
        return false
    }
}

if isValidFileUrl("file:///path/to/image.jpg") {
    // 유효한 파일 URL
} else {
    // 유효하지 않은 파일 URL
}

```

## 3. URL에 대한 응답을 체크하기 위한 유효성 검사
- URL(string:)을 이용하여 URL 객체를 생성, 이 객체가 올바른 URL인지를 검사. 
- 이후 URLRequest 객체를 생성하고, 이 객체를 이용하여 URLSession의 dataTask(with:completionHandler:) 메서드를 이용하여 URL 요청.
- 이때 요청에 대한 응답 코드(status code)를 확인하여, 코드가 200~299 범위 내에 있는 경우 URL이 유효하다고 판단하고 true를 반환.

```swift
func checkUrlResponse(_ urlString: String, completion: @escaping (Bool) -> Void) {
    guard let url = URL(string: urlString) else {
        completion(false)
        return
    }

    let request = URLRequest(url: url, cachePolicy: .reloadIgnoringLocalAndRemoteCacheData, timeoutInterval: 10.0)

    URLSession.shared.dataTask(with: request) { data, response, error in
        if let error = error {
            print("Error: \(error.localizedDescription)")
            completion(false)
            return
        }

        if let httpResponse = response as? HTTPURLResponse, (200...299).contains(httpResponse.statusCode) {
            completion(true)
        } else {
            completion(false)
        }
    }.resume()
}

```
