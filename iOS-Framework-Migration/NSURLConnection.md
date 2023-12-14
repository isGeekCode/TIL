# NSURLConnection Deprecated in iOS 9, Replaced by URLSession in iOS 7

```
'connectionWithRequest:delegate:' is deprecated: first deprecated in iOS 9.0 - Use NSURLSession (see NSURLSession.h)
```


URLSession은 iOS 7.0부터 도입되었지만 iOS 9.0부터 NSURLConnection의 대체제로 사용되기 시작한다. 

URLSession으로 대체된 주된 이유는 URLSession이 제공하는 개선된 기능과 유연한 네트워킹 아키텍쳐 때문이다.  

## URLSession에서 보다 나아진 점
- 백그라운드에서의 네트워킹 지원
- Session 기반의 구성
- 더 나아진 멀티테스킹과 성능
- 다운로드 및 업로드 작업 관리
- 더 풍부한 API 자원
- 보안 및 최신 기능

### 백그라운드에서의 네트워킹 지원
URLSession은 앱이 백그라운드에서 실행될 때도 데이터를 전송하거나 받을 수 있는 기능을 제공한다.   
이는 대용량 파일을 다운로드하거나 업로드할 때 특히 유용하다.  
  
NSURLConnection은 이러한 기능을 지원하지 않아, 앱이 활성 상태일 때만 데이터 통신이 가능했다.




### Session 기반의 구성
URLSession은 멀티태스킹을 더 효율적으로 지원하며, 특히 복잡한 네트워크 요청을 처리하는 데 있어 더 나은 성능을 제공한다.

- 그룹화된 네트워크 작업 관리
- 고유한 세션 구성
- 세션의 유연성
- 효율적인 자원 관리


좀더 설명하자면,



### 기본사용법
```swift
let url = URL(string: "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&count=3")!
let task = URLSession.shared.dataTask(with: url) { data, response, error in
    if let error = error {
        print("Error: \(error)")
        return
    }
    if let data = data {
        // 데이터 사용
        // print("Data: \(data)")
        
        let receivedDataString = String(data: data as Data,
                                        encoding: .utf8) ?? "Invalid data encoding"
        print("Received Data: \(receivedDataString)")
    }
}
task.resume()

```

### 그룹화된 네트워크 작업 관리
URLSession의 클로저는 기본적으로 비동기적인 동작을 한다.  
그래서 각 dataTask는 별도의 스레드에서 병렬적으로 실행이 된다.   
그리고 dataTask가 완료되면 콜백 함수를 호출해 데이터, 응답, 에러 등을 처리할 수 있게 된다.   

```
let session = URLSession.shared

let url1 = URL(string: "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&count=1")!
let url2 = URL(string: "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&count=1")!

let task1 = session.dataTask(with: url1) { data, response, error in
    if let error = error {
        print("Error in task 1: \(error)")
        return
    }
    if let data = data, let string = String(data: data, encoding: .utf8) {
        print("Response from task 1: \(string)")
    }
}

let task2 = session.dataTask(with: url2) { data, response, error in
    if let error = error {
        print("Error in task 2: \(error)")
        return
    }
    if let data = data, let string = String(data: data, encoding: .utf8) {
        print("Response from task 2: \(string)")
    }
}

task1.resume()
task2.resume()

```


### 고유한 세션 구성

특정 요구 사항에 맞게 세션을 구성할 수 있다.  
예를 들어, 타임아웃 설정, 캐시 정책, 셀룰러 네트워크 접근 등을 세션별로 다르게 설정할 수 있다.  

```swift
let configuration = URLSessionConfiguration.default
configuration.timeoutIntervalForRequest = 20.0 // 20초 타임아웃
configuration.requestCachePolicy = .reloadIgnoringLocalCacheData // 캐시 무시
configuration.allowsCellularAccess = false // 셀룰러 네트워크 사용 금지

let customSession = URLSession(configuration: configuration)

let task = customSession.dataTask(with: URL(string: "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&count=3")!) { data, response, error in
    // 데이터 처리
}
task.resume()
```
  
  
### 세션의 유연성
다양한 상황에 맞게 여러 세션을 생성하고 사용할 수 있다.

```swift
// 셀룰러 네트워크를 사용하는 세션
let cellularConfiguration = URLSessionConfiguration.default
cellularConfiguration.allowsCellularAccess = true

let cellularSession = URLSession(configuration: cellularConfiguration)

// 셀룰러 네트워크를 사용하지 않는 세션
let wifiConfiguration = URLSessionConfiguration.default
wifiConfiguration.allowsCellularAccess = false

let wifiSession = URLSession(configuration: wifiConfiguration)

```

### 효율적인 자원 관리

세션 구성을 통해 네트워크 자원을 효율적으로 관리한다.  
예를 들어, 백그라운드 세션을 사용하여 앱이 백그라운드 상태일 때도 데이터를 처리할 수 있다.  

```swift
let backgroundConfiguration = URLSessionConfiguration.background(withIdentifier: "com.example.myapp.background")
backgroundConfiguration.isDiscretionary = true // 시스템에 의해 최적의 시간에 실행

let backgroundSession = URLSession(configuration: backgroundConfiguration)

let downloadTask = backgroundSession.downloadTask(with: URL(string: "https://api.example.com/largefile")!)
downloadTask.resume()

```

URLSessionConfiguration.background를 사용하는 백그라운드 세션에서 파일을 다운로드하는 경우, 다운로드가 완료된 후에 실행될 콜백을 구현하기 위해서는 URLSessionDownloadDelegate 프로토콜을 사용해야 한다.  
  
백그라운드 세션은 앱이 백그라운드 상태에 있거나 종료된 후에도 작업을 완료할 수 있으며,  
완료 시 다운로드 관련 이벤트를 처리하기 위한 델리게이트 메서드를 호출한다.  







### 
### 
### 

# NSURLConnection
이 클래스는 네트워크 연결을 설정하고, 데이터를 전송하며, 서버로부터의 응답을 받는 데 사용되었다.  


## NSURLConnectionDataDelegate 프로토콜

### connection(_:didReceiveResponse:):
- 서버로부터 응답을 받기 시작할 떄 호출된다.  

### connection(_:didReceiveData:):
- 데이터의 일부가 서버로 부터 수신될 때마다 호출된다.   

### connectionDidFinishLoading(_:):
- 모든 데이터가 성공적으로 수신되었을 때, 호출된다.  

### connection(_:didFailWithError:):
- 연결실패, 네트워크 오류, 타임아웃 등 다양한 이유로 인해서도 호출 될 수 있다.     
- Error 객체를 통해 어떤 문제가 발생했는지 확인할 수 있다.  


## NSURLConnection으로 RESTfulAPI
```swift
class ViewController: UIViewController {
    
    var responseData: NSMutableData?

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemRed

        // URL을 설정합니다.
        if let url = URL(string: APIService.apiURL) {
            // NSURLRequest 객체를 생성합니다.
            let request = URLRequest(url: url)
            
            // NSURLConnection을 이용해 요청을 보냅니다.
            let connection = NSURLConnection(request: request, delegate: self)

            // 응답 데이터를 위한 초기화
            responseData = NSMutableData()
        }
    }
}

extension ViewController: NSURLConnectionDataDelegate {

        // 데이터가 수신시작시 호출된다.
    func connection(_ connection: NSURLConnection, didReceive response: URLResponse) {
        // 데이터 초기화
        responseData?.length = 0
    }

    // 데이터의 조각이 들어올 때마다 호출된다.
    func connection(_ connection: NSURLConnection, didReceive data: Data) {
        responseData?.append(data)
    }
    
    // 데이터 수신 완료
    func connectionDidFinishLoading(_ connection: NSURLConnection) {
        if let data = responseData {
            do {
                
// MARK: 받은 데이터를 문자열로 변환하여 출력 (디버깅용)
                let receivedDataString = String(data: data as Data,
                                                encoding: .utf8) ?? "Invalid data encoding"
                print("Received Data: \(receivedDataString)")

// MARK: 받은 데이터를 Codable을 통해 파싱
//                if let data = responseData {
//                    do {
//                        // JSON 데이터를 APOD 배열로 파싱
//                        let apods = try JSONDecoder().decode([APOD].self, from: data as Data)
//                        // 파싱된 데이터 출력
//                        for apod in apods {
//                            print("""
//                                  ------------------------
//                                    - Title: \(apod.title)
//                                    - Date: \(apod.date)
//                                    - URL: \(apod.imgURLStr)
//                                  """)
//                        }
//                    } catch {
//                        print("JSON parsing error: \(error)")
//                    }
//                }

// MARK: JSON 파싱
//                if let jsonArray = try JSONSerialization.jsonObject(with: data as Data, options: []) as? [[String: Any]] {
//                    for item in jsonArray {
//                        if let title = item["title"] as? String,
//                           let date = item["date"] as? String,
//                           let url = item["url"] as? String {
//                            print("""
//                                  ------------------------
//                                    - Title: \(title)
//                                    - Date: \(date)
//                                    - URL: \(url)
//                                  """)
//                        }
//                    }
//                }
//            } catch let error as NSError {
//                print("Error parsing JSON: \(error.localizedDescription)")
            }
        }
    }


    // 에러가 발생했을 때 호출된다.
    func connection(_ connection: NSURLConnection, didFailWithError error: Error) {
        print("Connection failed with error: \(error.localizedDescription)")
    }
}

class APIService {
    static let apiKey = "DEMO_KEY"
    static let fetchCount = 2
    static let apiURL = "https://api.nasa.gov/planetary/apod?api_key=\(apiKey)&count=\(fetchCount)"
}
```

## URLSession으로 RESTfulAPI

```
class ViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // URL 설정
        if let url = URL(string: APIService.apiURL) {
            // URLSession을 사용한 데이터 요청
            let task = URLSession.shared.dataTask(with: url) { data, response, error in
                // 에러 처리
                if let error = error {
                    print("Error: \(error.localizedDescription)")
                    return
                }

                // 데이터 처리
                if let data = data {
                    self.handleReceivedData(data)
                }
            }
            // 요청 시작
            task.resume()
        }
    }
    
    // 받은 데이터 처리
    private func handleReceivedData(_ data: Data) {
        do {
            // MARK: 받은 데이터를 문자열로 변환하여 출력 (디버깅용)
            let receivedDataString = String(data: data, encoding: .utf8) ?? "Invalid data encoding"
            print("Received Data: \(receivedDataString)")
            
            // MARK: Codable을 이용한 JSON 파싱
//                do {
//                    // JSON 데이터를 APOD 배열로 파싱
//                    let apods = try JSONDecoder().decode([APOD].self, from: data as Data)
//                    // 파싱된 데이터 출력
//                    for apod in apods {
//                        print("""
//                              ------------------------
//                                - Title: \(apod.title)
//                                - Date: \(apod.date)
//                                - URL: \(apod.imgURLStr)
//                              """)
//                    }
//                }
//            
//            } catch {
//                print("JSON parsing error: \(error)")
//            }
        
            
            // MARK: JSONSerialization을 사용한 파싱
//            if let jsonArray = try JSONSerialization.jsonObject(with: data as Data, options: []) as? [[String: Any]] {
//                for item in jsonArray {
//                    if let title = item["title"] as? String,
//                       let date = item["date"] as? String,
//                       let url = item["url"] as? String {
//                        print("""
//                              ------------------------
//                                - Title: \(title)
//                                - Date: \(date)
//                                - URL: \(url)
//                              """)
//                    }
//                }
//            }
            
        } catch {
            print("Error parsing data: \(error)")
        }
    }
}


class APIService {
    static let apiKey = "DEMO_KEY"
    static let fetchCount = 2
    static let apiURL = "https://api.nasa.gov/planetary/apod?api_key=\(apiKey)&count=\(fetchCount)"
}

// APOD 구조체 정의
struct APOD: Codable {
    let title: String
    let date: String
    let description: String
    let type: String
    let imgURLStr: String

    enum CodingKeys: String, CodingKey {
        case title
        case date
        case description = "explanation"
        case type = "media_type"
        case imgURLStr = "url"
    }
}
```




NSURLSession과 NSURLConnection의 주요 차이점
NSURLConnection : NSURLConnection으로 네트워크 연결을 맺고 있다가 만약 시스템이 인터럽트를 걸었다고 가정합시다. 그러면 앱이 백그라운드로 가게 되고 앱에서 전송받고 있던 모든데이터가 날아가게 됩니다.

NSURLSession : 이러한 문제를 해결해주고 다운로드 작업자체에서 우리를 해방시켜줬습니다. NSURLSession은 네트워크연결을 알아서 관리해줍니다. AppDelegate에서 application:handleEventsForBackgroundURLSession:completionHandler 메소드를 구현하셔서 백그라운드 다운로드도 직접 관리해줄 수 있습니다.**그러니까 NSURLSession을 사용하시면 네트워크 연결을 체크하실 필요가 없습니다. OS가 알아서 해주거든요.
