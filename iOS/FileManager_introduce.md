# FileManager - 사용하기

참고: [https://leeari95.tistory.com/32](https://leeari95.tistory.com/32)

```swift
let fileManager = FileManager.default
```

default는 FileManager의 싱글톤 인스턴스를 만들어준다. 

```swift
let documentsPath = fileManager.urls(for: .documentDirectory, in: .userDomainMask)[0]
```

urls 메서드는 요청된 도메인에서 지정된 공통 디렉토리에 대한 URL배열을 리턴해준다. 

첫번째 파라미터인 .documentDirectory는 검색경로 디렉토리다. 

- for: 폴더를 정해주는 요소, Download혹은 document 등등

두번째 파라미터는 Domain을 나타내는 파라미터다.

- in: 제한을 걸어주는 요소. 그이상은 못가게하는 요소이다

 

이걸 이용해서 Documents 디렉토리의 URL(Path)를 알게됐다.

이제 이걸 이용하면 파일을 추가할 수 있고 폴더를 추가할 수도  있다.

그러려면 파일의 이름 혹은 폴더의 이름을 정해줘야한다. 

```swift
let documentsPath = fileManager.urls(for: .documentDirectory, in: .userDomainMask)[0]

let directoryPath = documentsPath.appendingPathComponent("test-name")
```

여기에 

경로 설정하기

```swift
let fileManager = FileManager.default
let documentsPath = fileManager.urls(for: .documentDirectory, in: .userDomainMask)[0]
let directoryPath = documentsPath.appendingPathComponent("test-name")
```

폴더추가하기

```swift
do {
    // 아까 만든 디렉토리 경로에 디렉토리 생성 (폴더가 만들어진다.)
    try fileManager.createDirectory(at: directoryPath, withIntermediateDirectories: false, attributes: nil)
} catch let e {
    print(e.localizedDescription)
}
```

디렉토리 폴더에 파일을 추가하는 방법

내용집어넣기

```swift

let textPath: URL = directoryPath.appendingPathComponent("hi.txt")

// 아까 만든 'hi.txt' 경로에 텍스트 쓰기
if let data: Data = "안녕하세요.".data(using: String.Encoding.utf8) { // String to Data
    do {
        try data.write(to: textPath) // 위 data를 "hi.txt"에 쓰기
    } catch let e {
        print(e.localizedDescription)
    }
}
```


```
    func fileDownload(url: String) {
        guard let url = URL(string: url) else { return }
        print("input url: \(url)")
        let fileManager = FileManager.default // 인스턴스 생성
        let documentsURL = fileManager.urls(for: .documentDirectory, in: .userDomainMask)[0] // 도큐먼트 URL가져오기

        let fileName = url.lastPathComponent.removingPercentEncoding ?? ""
        let originalFileName = url.lastPathComponent
        
        print("documentsURL:\(documentsURL)")
        print("fileName:\(fileName)")
        print("originalFileName:\(originalFileName)")

        // 가져온 도큐먼트URL경로를 파일을 저장할 Directory로 설정
        let fileURL = documentsURL.appendingPathComponent(fileName)
        print("fileURL: \(fileURL)")
        //확장자 추출
        let ext = fileURL.lastPathComponent.components(separatedBy: ".").last ?? ""
        print("확장자 - ext: \(ext)")
        
        
        // URL Session 생성
        let sessionConfig = URLSessionConfiguration.default
        let session = URLSession(configuration: sessionConfig)
        print("url.: \(url)")
        print("url.: \(url.path)")
        
        // 서버의 파일 URL 추출, URL Request 생성
        let strArr = url.path.components(separatedBy: "url=")
        let urlStr = URL(string: strArr.last!)!
        let request = URLRequest(url: urlStr)
        
        // 파일 다운로드 통신 시작
        let task = session.downloadTask(with: request) { tempLocalUrl, response, error in
            if let tempLocalUrl = tempLocalUrl, error == nil {
                
                if let statusCode = (response as? HTTPURLResponse)?.statusCode {
                    print("download success status code ::: \(statusCode)")
                }
                
                do {
                    let fileURLString = (documentsURL.absoluteString + originalFileName).replacingOccurrences(of: "file://", with: "")
                    let isExist = fileManager.fileExists(atPath: fileURLString)
                    
                    if !isExist {
                        try fileManager.copyItem(at: tempLocalUrl, to: fileURL)
                    } else {
                        // 파일이 존재하는 경우
                        let onlyFileName = fileName.replacingOccurrences(of: ".\(ext)", with: "")
                        let fileNamesExt = onlyFileName.appending("(1)").appending(".\(ext)")
                        print("이름 변경 확인 ::: \(fileNamesExt)")
                        
                        // 도큐먼트 경로에 새로만튼 파일 경로 설정
                        let fileNameChangeUrl = documentsURL.appendingPathComponent(fileNamesExt)
                        // 파일 쓰기
                        try fileManager.copyItem(at: tempLocalUrl, to: fileNameChangeUrl)
                        
                    }
                    
                    let alert = UIAlertController(title: "", message: "첨부파일 다운로드에 성공했습니다.", preferredStyle: .alert)
                    let ok = UIAlertAction(title: "확인", style: .default) { _ in
                        self.dismiss(animated: true)
                    }

                    alert.addAction(ok)

                    DispatchQueue.main.async {
                        self.present(alert, animated: false, completion: nil)
                    }
                    
                } catch {
                    print("Error creating file \(fileURL) ::: error ::: \(error)")
                    
                    let alert = UIAlertController(title: "", message: "파일 다운로드에 실패했습니다.", preferredStyle: .alert)
                    let ok = UIAlertAction(title: "확인", style: .default) { _ in
                        self.dismiss(animated: true)
                    }
                    
                    alert.addAction(ok)
                    DispatchQueue.main.async {
                        self.present(alert, animated: false, completion: nil)
                    }
                }
                
            } else {
                print("error took place while downloading a file error ::: \(String(describing: error))")
                
                let alert = UIAlertController(title: "", message: "파일 다운로드에 실패했습니다.", preferredStyle: .alert)
                let ok = UIAlertAction(title: "확인", style: .default) { _ in
                    self.dismiss(animated: true)
                }
                alert.addAction(ok)
                
                DispatchQueue.main.async {
                    self.present(alert, animated: false, completion: nil)
                }
            }
        }
        task.resume()
    }
}

```
