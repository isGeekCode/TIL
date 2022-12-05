# URLSession 사용하기


참고 [https://furang-note.tistory.com/3](https://furang-note.tistory.com/33)

참고 [https://velog.io/@altmshfkgudtjr/Swift로-API-Request를-전송하기](https://velog.io/@altmshfkgudtjr/Swift%EB%A1%9C-API-Request%EB%A5%BC-%EC%A0%84%EC%86%A1%ED%95%98%EA%B8%B0)

**포스팅기반** → [https://techblog.woowahan.com/2704/](https://techblog.woowahan.com/2704/)

## 서론

서비스를 개발하는 것에 있어 API를 호출하고, 데이터를 받는 것은 매우 중요하다. API를 사용하지 않는 App은 한정된 정보만 가지고 있을 수 밖에 없다. 이번 글에서는 Swift를 사용해서 HTTP통신을 통해 서버와 통신하는 법을 알아보겠다.

## 선행 지식

📌 HTTP통신 (미정리)

📌 [URLSession과 URLSessionTask](https://www.notion.so/API-URLSession-9be5107668654267828d59f1a6aa8d83)

📌 탈출클로저

📌 Codable

📌 Optional Binding

기본적으로 서버와 통신하기 위해서는 아래 두가지 방법을 사용할 수가 있습니다.

- URLSession , URLRequest를 이용한 요청방식
- Alamofire라이브러리를 이용한 요청방식

## 초기세팅 - HTTP

기본적으로 iOS 개발을 진행하다 보면 SSL 인증이 되지 않는 사이트에 관해서 기본적으로 막고 있다는 것을 알게 된다.

### 방법1.

그렇다고, 처음 개발을 시작할 때부터 Https로 구현할 필요는 없다. `Info.plist` 에 들어가서 다음과 같이 설정을 진행해주자.

`Information Property List` > `App Transport Security Settings` > `Exception Domains` > `localhost` > `NSTemporaryExceptionAllowsInsecureHTTPLoads` 를 `YES`로 변경

![스크린샷 2022-02-25 오후 4.06.35.png](TIL220323_%20ec2db/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-02-25_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_4.06.35.png)

### 방법2

예전에 내가 쓴 글

[https://h1guitar.tistory.com/143](https://h1guitar.tistory.com/143)

Xcode는 iOS 9부터 HTTP 접근을 허용하지 않습니다.

따라서 리소스가 https 가 아니라면 불러오지 못합니다

Info에서 key 를 추가

`App Transport Security Settings - Allow Arbitrary Load`

`>` 를 활성화 시켜야 그에 맞는 value가 생성됨

`Yes`로 변환

![https://blog.kakaocdn.net/dn/5khjI/btrnV6c0OMq/Ex8O4MM0EWUV8KFcW4NBpK/img.png](https://blog.kakaocdn.net/dn/5khjI/btrnV6c0OMq/Ex8O4MM0EWUV8KFcW4NBpK/img.png)

이미지를 불러오는 스킴주소 등에서 문제가 될 수 있습니다.

## URLSession 사용하기

### URLSesson이란

기본적으로 제공하는 API, HTTP를 포함한 **여러가지 프로토콜을 지원, 인증, 쿠키, 캐시 등의 관리**를 지원.

또한, URLRequest는 요청에 대한 정보를 표현하는 객체이며, 이 객체를 URLSession을 사용하여 서버로 요청

참고 :

[iOS URLSession 이해하기 - Eth Dev Post](https://hcn1519.github.io/articles/2017-07/iOS_URLSession)

[Swift, URLSession가 무엇인지, 어떻게 사용하는지 알아봅니다. - 까칠코더(Minjun Ju 번역)](https://devmjun.github.io/archive/URLsession)

[https://velog.io/@altmshfkgudtjr/Swift로-API-Request를-전송하기](https://velog.io/@altmshfkgudtjr/Swift%EB%A1%9C-API-Request%EB%A5%BC-%EC%A0%84%EC%86%A1%ED%95%98%EA%B8%B0)

### URLSessionTask

- URLSessionTask는 서버에 데이터를 요청하는 하나의 Task를 표현합니다.
- URLSession의 data(with:) 메서드를 이용해 URL SessionTask를 생성할 수 있습니다.

1. 효율적으로 request를 사용하기 위해서 따로 request.swift라는 파일을 생성시켜준다. 이 파일에서 메소드별 동작을 구현한다. 먼저 전체구조를 확인하고 세부적으로 진행시켜보자.

```swift
import UIKit

struct Response: Codable {
    let success: Bool
    let result: String
    let message: String
}

/* Body가 없는 요청 */
func requestGet(url: String, completionHandler: @escaping (Bool, Any) -> Void) {

    ...

}

/* Body가 있는 요청 */
func requestPost(url: String, method: String, param: [String: Any], completionHandler: @escaping (Bool, Any) -> Void) {

    ...

}

/* 메소드별 동작 분리 */
func request(_ url: String, _ method: String, _ param: [String: Any]? = nil, completionHandler: @escaping (Bool, Any) -> Void) {
    if method == "GET" {
        requestGet(url: url) { (success, data) in
            completionHandler(success, data)
        }
    }
    else {
        requestPost(url: url, method: method, param: param!) { (success, data) in
            completionHandler(success, data)
        }
    }
}
```

우리는 다른 View 파일에서 request 함수를 사용할 것이다. 그리고 서버로부터 받은 데이터를 탈출클로저를 통해 View파일에서 사용할 수 있다.

위 코드를 통해 request함수를 사용하는 방식은 아래와 같다.

```swift
request("http://localhost:5000/test/get", "GET") { (success, data) in
  print(data)
}

// or

request("http://localhost:5000/test/post", "POST", ["key": "hello!"]) { (success, data) in
  print(data)
}
```

request함수의 첫번째 파라미터는 url, 두번째 파라미터는 method (통신방식), 세번째 파라미터는 optional로 Body에 들어갈 Dictionary타입의 데이터를 넣어준다.

### GET 메소드 사용

흐름을 파악하고 이제 동작하는 방식을 이해해보자.

```swift
func requestGet(url: String, completionHandler: @escaping (Bool, Any) -> Void) {
    guard let url = URL(string: url) else {
        print("Error: cannot create URL")
        return
    }

    var request = URLRequest(url: url)
    request.httpMethod = "GET"

    URLSession.shared.dataTask(with: request) { data, response, error in
        guard error == nil else {
            print("Error: error calling GET")
            print(error!)
            return
        }
        guard let data = data else {
            print("Error: Did not receive data")
            return
        }
        guard let response = response as? HTTPURLResponse, (200 ..< 300) ~= response.statusCode else {
            print("Error: HTTP request failed")
            return
        }
        guard let output = try? JSONDecoder().decode(Response.self, from: data) else {
            print("Error: JSON Data Parsing failed")
            return
        }
        completionHandler(true, output.result)
    }.resume()
}

// 또다른 방법들은 아래에 자세히

```

우리는 주로 guard 문법을 사용할 예정이다. → [참고 : guard문 Robin Kang](https://brunch.co.kr/@robinkangwgmv/4)

**LOGIC**

1. URL 객체 생성
2. Request 객체 생성 (+ 메소드 설정) → GET or etc
3. URLSession을 이용해서 데이터 요청
4. @escaping Closure을 이용한 외부 함수로 인자 전달
5. .resume()메서드를 호출해 요청을 보냄.

URLSession의 dataTask(with:) 메서드를 이용해 URLSessionDataTask를 생성한 task.resume() 메서드를 호출해 요청을 보냅니다.

resume()외에도 suspend(), calcel()등의 메서드가 존재하며 필요에 따라 사용할 수 있음

여기서 주목해야할 점은 제일 마지막 부분에서 `JSONDecoder()`를 실행시키는 부분이다. Swift4부터 등장한 Codable을 통해서 우리는 JSON 객체를 Dictionary타입으로 만들수 있게 되었는데, 이 코드에서는 이미 상단에 Codable을 선언했다.

```swift
struct Response: Codable {
    let success: Bool
    let result: String
    let message: String
}
```

![스크린샷 2022-02-28 오전 8.58.19.png](TIL220323_%20ec2db/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-02-28_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_8.58.19.png)

위 사진 처럼 항상 Response와 같은 구조를 반환해준다는 가정하에 Codable을 선언해준다. 그리고 JSONDecoder()를 통해서 일반 JSON에서 데이터를 파싱해준다.

### 그 외의 메소드를 사용

RESTful API를 사용한다는 가정하에 `GET` 메소드를 제외하고 다른 메소드들은 `body`를 포함할 수 있다. 그렇기에 body를 넣어주는 코드만 추가하고 나머지는 동일하게 작성해주자.

```swift
func requestPost(url: String, method: String, param: [String: Any], completionHandler: @escaping (Bool, Any) -> Void) {
    let sendData = try! JSONSerialization.data(withJSONObject: param, options: [])

    guard let url = URL(string: url) else {
        print("Error: cannot create URL")
        return
    }

    var request = URLRequest(url: url)
    request.httpMethod = method
    request.addValue("application/json", forHTTPHeaderField: "Content-Type")
    request.httpBody = sendData

    URLSession.shared.dataTask(with: request) { (data, response, error) in
        guard error == nil else {
            print("Error: error calling GET")
            print(error!)
            return
        }
        guard let data = data else {
            print("Error: Did not receive data")
            return
        }
        guard let response = response as? HTTPURLResponse, (200 ..< 300) ~= response.statusCode else {
            print("Error: HTTP request failed")
            return
        }
        guard let output = try? JSONDecoder().decode(Response.self, from: data) else {
            print("Error: JSON Data Parsing failed")
            return
        }

        completionHandler(true, output.result)
    }.resume()
}
```

서버에서 body 값을 JSON으로 받는다는 가정하에 Dictionary 타입으로 들어온 `param` 인자를 JSON으로 바꿔준다. 그리고서 `Content-Type`을 `application/json`으로 바꿔주고, body에 데이터를 추가해준다. 나머지 과정은 `GET`을 사용할 때와 동일하다.

# 여러가지 API 통신

## 1. 간단 형식

```swift
// 1. 전송할 값 준비

func requestGet(url: String, completionHandler: @escaping (Bool, Any) -> Void) {
// 2. url 객체 정의
    guard let url = URL(string: url) else {
        print("Error: cannot create URL")
        return
    }
// 3. URLRequest 객체 정의 및 요청 내용 담기 ( 이때, cachePolicy, timeoutInterval 도 사용 가능)
    var request = URLRequest(url: url)
    request.httpMethod = "GET"

// 4. URLSession 객체를 통해 전송 및 응답값 처리 로직
    URLSession.shared.dataTask(with: request) { data, response, error in
        guard error == nil else {
            print("Error: error calling GET")
            print(error!)
            return
        }
        guard let data = data else {
            print("Error: Did not receive data")
            return
        }
        guard let response = response as? HTTPURLResponse, (200 ..< 300) ~= response.statusCode else {
            print("Error: HTTP request failed")
            return
        }
        guard let output = try? JSONDecoder().decode(Response.self, from: data) else {
            print("Error: JSON Data Parsing failed")
            return
        }
        completionHandler(true, output.result)
    }.resume()
}

/**
do catch 로도 사용 가능

	if error == nil {
	      do {
	        if let json = try JSONSerialization.jsonObject(with: data!, options: .allowFragments) as AnyObject? {
	            completed(true, nil, json)
						  // completed(isSuccess: true, message:nil, json: json)
	        }
	    } catch let err as NSError {
	        completed(false, err.localizedDescription, nil)
					//  completed(isSuccess: false, message:err.localizedDescription, json: nil)
	    }
	} else {
	    completionHandler(false, error!.localizedDescription, nil)
			// completed(isSuccess: false, message:error!.localizedDescription, json: nil)
	}

	*/

// post

// 1. 전송할 값 준비
// 2. JSON 객체로 변환할 딕셔너리 준비
	//let param = ["create_name" : "kkkkkkkk", "create_age" : "909090"]
	//let postString = "create_name=13&create_age=Jack"

func requestPost(url: String, method: String, param: [String: Any], completionHandler: @escaping (Bool, Any) -> Void) {
    let sendData = try! JSONSerialization.data(withJSONObject: param, options: [])


// 3. URL 객체 정의
    guard let url = URL(string: url) else {
        print("Error: cannot create URL")
        return
    }


// 3. URLRequest 객체 정의 및 요청 내용 담기 ( 이때, cachePolicy, timeoutInterval 도 사용 가능)
    var request = URLRequest(url: url)
    request.httpMethod = method // "POST"

**// 4. HTTP 메시지에 포함될 헤더 설정**
    request.addValue("application/json", forHTTPHeaderField: "Content-Type")

// 5. body값 설정
//    let sendData = try! JSONSerialization.data(withJSONObject: param, options: [])
    request.httpBody = sendData

// 6. URLSession 객체를 통해 전송 및 응답값 처리 로직
    URLSession.shared.dataTask(with: request) { (data, response, error) in
        guard error == nil else {
            print("Error: error calling GET")
            print(error!)
            return
        }
        guard let data = data else {
            print("Error: Did not receive data")
            return
        }
        guard let response = response as? HTTPURLResponse, (200 ..< 300) ~= response.statusCode else {
            print("Error: HTTP request failed")
            return
        }
        guard let output = try? JSONDecoder().decode(Response.self, from: data) else {
            print("Error: JSON Data Parsing failed")
            return
        }

        completionHandler(true, output.result)
//7. POST전송
    }.resume()
}

```

## 2. 통신체크를 포함한 형식

```swift
static func get(_ url: String!, completionHandler: @escaping (_ isSuccess: Bool, _ message:String?, _ json: AnyObject?) -> ()) {
		        // 통신체크
						if Reachability.isConnectedToNetwork() == false {
            completed(false, Message.networkError, nil)
            return
        }

        var request = URLRequest(url: URL(string: url)!, cachePolicy: .reloadIgnoringLocalAndRemoteCacheData, timeoutInterval: Constants.requestTimeoutInterval)
        request.httpMethod = "GET"

        //let request = NSMutableURLRequest(URL: NSURL(string: url)!)
        let task = URLSession.shared.dataTask(with: request as URLRequest) { (data, response, error) -> Void in
//        let task = session.dataTask(with: request, completionHandler: {(data, response, error) -> Void in
            if error == nil {
                do {
                    if let json = try JSONSerialization.jsonObject(with: data!, options: .allowFragments) as AnyObject? {
                        completed(true, nil, json)
//                        completed(isSuccess: true, message:nil, json: json)
                    }
                } catch let err as NSError {
                    completed(false, err.localizedDescription, nil)
//                    completed(isSuccess: false, message:err.localizedDescription, json: nil)
                }
            } else {
                completionHandler(false, error!.localizedDescription, nil)
//                completed(isSuccess: false, message:error!.localizedDescription, json: nil)
            }
        }

        task.resume()
    }

//통신체크 구현
class Reachability {

    static func isConnectedToNetwork() -> Bool {
        guard let flags = getFlags() else { return false }
        let isReachable = flags.contains(.reachable)
        let needsConnection = flags.contains(.connectionRequired)
        return (isReachable && !needsConnection)
    }

    static func getFlags() -> SCNetworkReachabilityFlags? {
        guard let reachability = ipv4Reachability() ?? ipv6Reachability() else {
            return nil
        }
        var flags = SCNetworkReachabilityFlags()
        if !SCNetworkReachabilityGetFlags(reachability, &flags) {
            return nil
        }
        return flags
    }

    static func ipv6Reachability() -> SCNetworkReachability? {
        var zeroAddress = sockaddr_in6()
        zeroAddress.sin6_len = UInt8(MemoryLayout<sockaddr_in>.size)
        zeroAddress.sin6_family = sa_family_t(AF_INET6)

        return withUnsafePointer(to: &zeroAddress, {
            $0.withMemoryRebound(to: sockaddr.self, capacity: 1) {
                SCNetworkReachabilityCreateWithAddress(nil, $0)
            }
        })
    }

    static func ipv4Reachability() -> SCNetworkReachability? {
        var zeroAddress = sockaddr_in()
        zeroAddress.sin_len = UInt8(MemoryLayout<sockaddr_in>.size)
        zeroAddress.sin_family = sa_family_t(AF_INET)

        return withUnsafePointer(to: &zeroAddress, {
            $0.withMemoryRebound(to: sockaddr.self, capacity: 1) {
                SCNetworkReachabilityCreateWithAddress(nil, $0)
            }
        })
    }

}

// 멀티파트 사용시 사용함.
// param을 url형태로 만들어 줄때 사용 필요한 링크의 형식에 맞춰서 수정필요
static func HTTPArgumentsString(_ params: [String: AnyObject]) -> String {
        let arguments = NSMutableArray(capacity: params.count) as NSMutableArray!

        for (key, value) in params {
            arguments?.add("\(key)=\(value)")
        }
        return arguments!.componentsJoined(by: "&")
    }

// post형식의 API 호출
    static func post(_ url: String!, params: [String: AnyObject], isJsonProtocol: Bool = true, completed: @escaping (_ isSuccess: Bool, _ message:String?, _ json: AnyObject?) -> ()) {
        if Reachability.isConnectedToNetwork() == false {
            completed(false, Message.networkError, nil)
            return
        }


        var request = URLRequest(url: URL(string: url)!, cachePolicy: .reloadIgnoringLocalAndRemoteCacheData, timeoutInterval: Constants.requestTimeoutInterval)


        let parameters:[String: AnyObject]! = params

        request.httpMethod = "POST"

        if isJsonProtocol {
            request.addValue("application/json", forHTTPHeaderField: "Content-Type")
            request.addValue("application/json", forHTTPHeaderField: "Accept")
            request.addValue("iOS", forHTTPHeaderField: "User-Agent")

            do {
                request.httpBody = try JSONSerialization.data(withJSONObject: parameters, options: .prettyPrinted)
            } catch {
                completed(false, "JSON Parsing Error", nil)
            }

        }

        let task = URLSession.shared.dataTask(with: request as URLRequest) { (data, response, error) -> Void in
            if error == nil {
                do {
                    if let json = try JSONSerialization.jsonObject(with: data!, options: .allowFragments) as AnyObject! {
                        if json["result"] != nil {
                            if let success = json["result"] as? Bool {
                                completed(success, json["message"] as? String, json)
//                                completed(isSuccess: success, message: json["message"] as String?, json: json)
                            } else {
                                // 외부 통신용
                                completed(true, nil, json)
//                                completed(isSuccess: true, message: nil, json: json)
                            }
                        } else {
                            completed(true, nil, json)
//                            completed(isSuccess: true, message: nil, json: json)
                        }
                    }
                } catch let err as NSError {
                    completed(false, err.localizedDescription, nil)
//                    completed(isSuccess: false, message: err.localizedDescription, json: nil)
                }
            } else {
                completed(false, error!.localizedDescription, nil)
//                completed(isSuccess: false, message: error!.localizedDescription, json: nil)
            }
        }

        task.resume()

}

//사용예

if (redirectURL) {
            let dic = url.queryDictionary

// 1. 전송할 값 준비
// 쿼리에 필요한 값이 없다면 액션시트 보여주기

            if dic["code"] == nil {
                self.actionSheetPresentViewController(message: "code not found", animated: true, confirmAlertAction: nil)
                decisionHandler(WKNavigationActionPolicy.cancel)
                return
            }
// param 생성
//2. JSON 객체로 변환할 딕셔너리 준비
            let params = [
                "menuName": Instagram.menuName,
                "menuName_secret": Instagram.menuName_secret,
                "food_type": Instagram.food_type,
                "redirect_uri": Instagram.redirectURL,
                "code": dic["code"]! as String
            ]

//AbcURLSession에 생성한 post 함수 구현
            AbcURLSession.post(Instagram.oAuthURL, params: params as [String : AnyObject], isJsonProtocol: false) { (isSuccess, message, json) -> () in
                self.stopActivityIndicator()

                // message가 있을 경우에만 실행됨
                self.actionSheetPresentViewController(message: message, animated: true, confirmAlertAction: nil)

                DispatchQueue.main.async(execute: {
                    if isSuccess {
                        guard let map = json else { decisionHandler(WKNavigationActionPolicy.cancel); return }
                        guard let token = map["access_token"] as? String else {
                            self.actionSheetPresentViewController(message: "token not found", animated: true, confirmAlertAction: nil)
                            decisionHandler(WKNavigationActionPolicy.cancel)
                            return
                        }

                        UIApplication.appDelegate.instagramAccessToken = token
                        self.didOAuthCompleted(key: "")
                    }
                })
            }

        }

```

## URLRequest

1. 메소드 설정)
2. 바디에 들어갈 값들 생성

```swift

  var request = URLRequest(url: url)
    request.httpMethod = method // "GET" or "POST"

	//POST만
    request.addValue("application/json", forHTTPHeaderField: "Content-Type")
    request.httpBody = sendData

```

## \***\*캐시 데이터에 접근하기\*\***

### 개요

URL 로딩 시스템은 성능 향상과 네트워크 트래픽 감소를 위해서 응답 데이터를 메모리와 디스크 양쪽에 저장합니다.

[URLCache](https://www.notion.so/sagwa/app-frameworks/foundation/url-loading-system/urlcache) 클래스는 네트워크 리소스로부터의 응답을 캐싱하는데 사용됩니다. 앱에서 URLCache의 [shared](https://www.notion.so/sagwa/etc/not-found) 속성을 사용하여 공유 캐시 인스턴스에 직접 접근하는 것이 가능합니다. 아니면 다른 목적을 위해 [URLSessionConfiguration](https://www.notion.so/sagwa/app-frameworks/foundation/url-loading-system/urlsession/urlsessionconfiguration)에 고유한 캐시를 생성할 수도 있습니다.

### URL Request에 대한 캐시 정책 설정

각 [URLRequest](https://www.notion.so/sagwa/etc/not-found) 인스턴스에는 [URLRequest.CachePolicy](https://www.notion.so/sagwa/etc/not-found) 객체가 포함되어있어 캐싱을 수행해야 할지, 어떻게 캐싱할 것인지를 알려줍니다.

편의를 위해서 [URLSessionConfiguration](https://www.notion.so/sagwa/app-frameworks/foundation/url-loading-system/urlsession/urlsessionconfiguration)에는 [requestCachePolicy](https://www.notion.so/sagwa/etc/not-found)라는 속성이 있습니다. 이 Configuration을 사용하는 Session으로부터 생성된 모든 Request는 requestCachePolicy를 Configuration으로부터 상속받아 사용합니다.

표 1은 다양한 정책들이 어떻게 동작하는지를 설명합니다. 이 표는 서버 또는 로컬에서 캐시 및 원본 파일을 로딩하기 위한 각 정책의 기본 설정을 보여줍니다. 현재는 HTTP와 HTTPS 응답만 캐시가 가능하며 FTP 및 파일 URL에 대해서는 원본 소스에 응답을 허용할 것인지에 대해서만 정책 적용이 되고 있습니다.

**표 1. 캐시 정책과 각 정책의 동작**

![스크린샷 2022-03-23 오전 11.05.41.png](TIL220323_%20ec2db/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-03-23_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_11.05.41.png)

## 캐시에 직접 접근

세션 configuration 객체의 urlCache 속성을 사용하면 URLSession 객체의 캐시를 읽거나 쓸 수 있습니다.

특정 요청에 대해 캐시된 응답을 찾으려면 [cachedResponse(for:)](https://www.notion.so/sagwa/etc/not-found)을 호출하면 됩니다. 캐시된 데이터가 있다면 CachedURLResponse 객체를 반환하고 없으면 nil을 반환합니다.

캐시에서 사용되는 리소스를 검사할 수도 있습니다. [currentDiskUsage](https://www.notion.so/sagwa/etc/not-found), [diskCapacity](https://www.notion.so/sagwa/etc/not-found) 속성은 파일시스템 상의 캐시 리소스에 대해서, [currentMemoryUsage](https://www.notion.so/sagwa/etc/not-found)와 [memoryCapacity](https://www.notion.so/sagwa/etc/not-found)는 메모리 상의 캐시 리소스에 대해서 알려줍니다.

[removeCachedResponse(for:)](https://www.notion.so/sagwa/etc/not-found)을 사용하면 캐시된 개별 아이템을 삭제할 수도 있습니다. 특정 날짜 이전의 캐시된 아이템을 동시에 삭제하려면 [removeCachedResponses(since:)](https://www.notion.so/sagwa/etc/not-found) 메서드를, 전체 캐시를 삭제하려면 [removeAllCachedResponses()](https://www.notion.so/sagwa/etc/not-found) 메서드를 호출하면 됩니다.

## 프로그래밍적으로 캐시 처리하기

캐시 방식을 프로그래밍하려면 storeCachedResponse(\_:for:) 메서드에 새로운 CachedURLResponse 객체와 URLRequest 객체를 전달하면 됩니다.

일반적으로 캐시 관리는 URLSessionTask 객체가 응답을 처리하는 도중에 이루어집니다. 응답 단위로 캐시를 관리하기 위해서는 [URLSessionDataDelegate](https://www.notion.so/sagwa/etc/not-found)프로토콜의 [urlSession(\_:dataTask:willCacheResponse:completionHandler:)](https://www.notion.so/sagwa/etc/not-found) 메서드를 구현해야 합니다. 이 delegate 메서드는 upload task와 data task에서만 호출된다는 점에 주의하세요. background, ephemeral configuration으로 설정된 세션에서는 호출되지 않습니다.

이 delegate는 CachedURLResponse 객체와 completion handler를 파라미터로 받으며, completion handler에 다음 중의 하나를 전달하면서 호출하도록 되어 있습니다.

- 있는 그대로 캐시하기 위해서 제공된 CachedURLResponse 객체
- nil, 이 경우 캐시를 하지 않습니다.
- 새로 생성된 CachedURLResponse 객체, 일반적으로 제공된 객체를 기반으로 하지만 수정된 storagePolicy와 userInfo Dictionary를 포함합니다.

목록 1은 HTTPS 응답을 가로채서 인메모리 방식으로만 캐시하도록 urlSession(\_:dataTask:willCacheResponse:completionHandler:)를 구현하고 있습니다.
