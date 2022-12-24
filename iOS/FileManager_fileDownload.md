# FileManager - 파일 다운로드하기


URL을 통해 이미지가 아닌 파일을 다운로드하는 상황이 있다.
사진은 사진첩에 고이 들어가지만, 애플에서는 앱에서 파일앱에 저장하게 되고 그곳의 경로와 파일명, 확장자를 정확하게 저장해주어야한다. 
특히, 확장자를 적지않으면 읽을 수 없는 형태로 들어가게 된다.


이 글은 총 두 챕터이다. 
- Chapter 1. 파일다운로드 시도하고 성공 실패시 얼럿을 띄우는 로직
- Chapter 2. 파일 다운로드를 시도했을 때, 해당 이름이 있는 경우를 위한 로직

## Chapter 1. 파일다운로드 시도하고 성공 실패시 얼럿을 띄우는 로직

지난번 글에서 소개한 fileManager 생성과정을 진행하고 파일 다운로드를 시작한다. 

### fileManager 생성

```
        guard let url = URL(string: url) else { return }
        print("input url: \(url)")
        let fileManager = FileManager.default // 인스턴스 생성
        let documentsURL = fileManager.urls(for: .documentDirectory, in: .userDomainMask)[0] // 도큐먼트 URL가져오기

        let fileName = url.lastPathComponent.removingPercentEncoding ?? ""
        let originalFileName = url.lastPathComponent
        
        print("documentsURL:\(documentsURL)")
        print("fileName:\(fileName)")
        print("originalFileName:\(originalFileName)")

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
        print("url: \(url)")
        print("url.path: \(url.path)")
        
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
                    // 파일 경로 설정
                    let fileURLString = (documentsURL.absoluteString + originalFileName).replacingOccurrences(of: "file://", with: "")
                    
                    // 파일 저장 시도
                    try fileManager.copyItem(at: tempLocalUrl, to: fileURL)
                    
                    
                    // 성공얼럿
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
```



### FileDownload 전체코드

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
        print("url: \(url)")
        print("url.path: \(url.path)")
        
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
                        // MARK: 방법 1 숫자 추가
                        let onlyFileName = fileName.replacingOccurrences(of: ".\(ext)", with: "")
                        do {
                            let filePath = documentsURL.absoluteString.replacingOccurrences(of: "file://", with: "")
                            let fileList = try fileManager.contentsOfDirectory(atPath: filePath )
                            var fileArray = [String]()
                            for fileName in fileList {
                                fileArray.append(fileName)
                            }

                            let filteredArray = fileArray.filter { $0.contains(onlyFileName) }
                            let stringArray = filteredArray.map {
                                $0.replacingOccurrences(of: onlyFileName, with: "")
                                  .replacingOccurrences(of: ".\(ext)", with: "")
                                  .replacingOccurrences(of: "(", with: "")
                                  .replacingOccurrences(of: ")", with: "")
                            }

                            let maxNum = stringArray.filter{ $0.isEmpty == false }
                                                    .map { Int($0)! }
                                                    .max()
                            guard let newNum = maxNum else {return}
                            
                            // 도큐먼트 경로에 새로운 파일 경로 설정
                            let fileNamesExt = onlyFileName.appending("(\(newNum + 1))").appending(".\(ext)")
                            let fileNameChangeUrl = documentsURL.appendingPathComponent(fileNamesExt)
                            try fileManager.copyItem(at: tempLocalUrl, to: fileNameChangeUrl)
                        }
                        catch {
                            print("[Error] : \(error.localizedDescription)")
                        }

                        //MARK: - 방법 2
                        // 파일이 존재하는 경우 제거 후 다시 다운로드
//                        try fileManager.removeItem(atPath: fileURLString)
//                        let isNewValueExist = fileManager.fileExists(atPath: fileURLString)
//                        if !isNewValueExist {
//                            print("isNewValueExist: \(isNewValueExist)")
//                            print("!isExist: \(!isExist)")
//
//                            try fileManager.copyItem(at: tempLocalUrl, to: fileURL)
//                        }
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


```
