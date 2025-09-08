# DynamicSplash 세팅하기

이 앱은 3단계의 스플래시를 가진다. 

- launchScreen
- customSplashView
- dynamicSplash

LaunchScreen

- launchScreen.storyboard에서 설정하고 시간을 제어할 수 없다.
- 궂이 하려면 appDelegate에서  Thread.sleep처리해야한다.

```swift
Thread.sleep(forTimeInterval: 1.0)
```

customSplashView

여기서는 launchScreen과 동일한 image를 세팅한다. splash단계에서 앱 구동, 운영에 필요한 정보들을 준비하는 단계이다. 

그리고 dynamicSplash가 추가적으로 있는지 API통신을 한다. 

dynamicSplash가 존재하는 경우 Image, gif, mov, none  타입체크를 하고 

API결과값을 파싱해서 dynamicSplash에 사용할 컨텐츠를 다운로드하고 

그 동안 customSplashView가 유지되어야한다. 

# 작업단계

## 모델링

API를 받기전 결과값, URL, 명세서를  확인

Model구조를 짠다. 

```swift
// MARK: Response

{
    "data": {
        "bannerCntList": [
            {
                "bannerAutoSn": "999",
                "bannerCntentAutoSn": "1008",
                "bannerCntentCatCd": "IMG",
                "sortSeqNo": 1,
                "cntentFileNm": "4fe9b910-2022-416b-9f4e-d62a00807fef.png",
                "cntentFilePathNm": "/banimg/202212/",
                "htmlCntent": "",
                "linkUrl": "http://naver.com",
                "cntentNm": "모바일배너",
                "linkDisplayYn": "Y"
            }
        ]
    },
    "status": 200,
    "message": "SUCCESS"
}

// SplashURL : 도메인 + cntentFilePathNm + cntentFileNm
```

해당 Response를 quickType사이트를 이용해 Model 세팅

```swift
import Foundation

// MARK: - DynamicSplashModel
struct DynamicSplashModel: Codable {
    var data: DataClass?
    var status: Int?
    var message: String?
}

// MARK: - DataClass
struct DataClass: Codable {
    var bannerCntList: [BannerCntList]?
}

// MARK: - BannerCntList
struct BannerCntList: Codable {
    var bannerAutoSn, bannerCntentAutoSn, bannerCntentCatCD: String?
    var sortSeqNo: Int?
    var cntentFileNm, cntentFilePathNm, htmlCntent: String?
    var linkURL: String?
    var cntentNm, linkDisplayYn: String?

    enum CodingKeys: String, CodingKey {
        case bannerAutoSn, bannerCntentAutoSn
        case bannerCntentCatCD = "bannerCntentCatCd"
        case sortSeqNo, cntentFileNm, cntentFilePathNm, htmlCntent
        case linkURL = "linkUrl"
        case cntentNm, linkDisplayYn
    }
}
```

## 테스트로직 구현

### JSON 생성

아직 JSON파일을 받지않기 때문에 임시로 사용하기위해 샘플 Response와  동일한 JSON생성

```swift
/// <임시> JSON 생성하는 함수
    func makeJSON() -> String? {
        let myBannerCntList = BannerCntList(bannerAutoSn: "999", bannerCntentAutoSn: "1008", bannerCntentCatCD: "IMG", sortSeqNo: 1, cntentFileNm: "4fe9b910-2022-416b-9f4e-d62a00807fef.png", cntentFilePathNm: "/banimg/202212/", htmlCntent: "", linkURL: "http://naver.com", cntentNm: "모바일배너", linkDisplayYn: "Y")
        let myDataClass = DataClass(bannerCntList: [myBannerCntList])
        let myDynamicSplashModel = DynamicSplashModel(data: myDataClass, status: 200, message: "SUCCESS")
        
        let encoder = JSONEncoder()
        encoder.outputFormatting = [.prettyPrinted, .sortedKeys]
        let jsonData = try? encoder.encode(myDynamicSplashModel)
        
        guard let jsonData = jsonData, let jsonString = String(data: jsonData, encoding: .utf8) else { return nil}
        print("==================\n생성한 json :: \n\(jsonString)\n==================")
        return jsonString
        
    }
```

### JSON처리

Data를 가지고 내가 가진 Model에 Decode처리할 함수세팅

```swift
/// 들어온 Data를  사용할수 있는 객체로 리턴하는 함수
    /// - Parameter parseData: Data
    /// - Returns: BannerCntList
    func parseJSON(_ parseData: Data) -> BannerCntList? {
        print("parseData: \(parseData)")

        let decoder = JSONDecoder()

        do {
            let decodedData = try decoder.decode(DynamicSplashModel.self, from: parseData)
            print("decodedData: \n\(decodedData)")
            let myDataClass = DataClass(bannerCntList: decodedData.data?.bannerCntList)
            
            print("myDataClass: \n\(myDataClass)")
            if let bannerList = myDataClass.bannerCntList {
                print("bannerList: \n\(bannerList)")
                let myBannerList = bannerList[0]
                print("myBannerList: \n\(myBannerList)")
                
                let parsedBannerCntList = BannerCntList(bannerAutoSn: myBannerList.bannerAutoSn, bannerCntentAutoSn: myBannerList.bannerAutoSn, bannerCntentCatCD: myBannerList.bannerCntentCatCD, sortSeqNo: myBannerList.sortSeqNo, cntentFileNm: myBannerList.cntentFileNm, cntentFilePathNm: myBannerList.cntentFilePathNm, htmlCntent: myBannerList.htmlCntent, linkURL: myBannerList.linkURL, cntentNm: myBannerList.cntentNm, linkDisplayYn: myBannerList.linkDisplayYn)
                print("parsedBannerCntList: \n\(parsedBannerCntList)")
                return parsedBannerCntList

            }
        }
        catch {
            print("파싱 실패")
            return nil
        }
        return nil
    }
```

makeJSON()과 parseJSON() - JSON을 만들고 파싱하는 두 함수를 이어주는 함수 생성

내가 직접 JSON을 만들었기 때문에 추후 URLSession을 구현해야한다. 

```swift
/// <임시>JSON Decoder를 통해 모델값 가져오는 함수
    func jsonDecode() {
        guard let json = makeJSON() else {return}
        let data = json.data(using: .utf8)
        guard let safeData = data,
              let jsonParse = parseJSON(safeData) else { return }
        print("==================\n파싱한 json :: \n\(jsonParse)\n==================")
        getContentType(jsonParse)
    }
```

JSON으로 받은 내용으로 dynamicSplash를 구분하고 분기처리

추후 각 타입은 enum으로 수정필요

```swift
func getContentType(_ responseModel: BannerCntList) {
        
        // 기본값 IMG
        let content = responseModel.bannerCntentCatCD
//        let content = "NONE"

        switch content {
        case "IMG":
            dynamicSplashContentType = "IMG"
            isDynamicSplash = true

        case "MOV":
            dynamicSplashContentType = "MOV"
            isDynamicSplash = true

        case "GIF":
            dynamicSplashContentType = "GIF"
            isDynamicSplash = true

        case "NONE":
            dynamicSplashContentType = ""
            isDynamicSplash = false
        default:
            dynamicSplashContentType = "IMG"
            isDynamicSplash = true
        }
        
            setDynamicSplash(model: responseModel)
    }
```

다이나믹 스플래시를 세팅하고 종료시키는 로직

- TEST URL의 경우: Image의 경로 하드코딩
- PRD URL의 경우 : 받은 API Response를 통해 생성
- API수신내용에 따라 isDynamicSplash를 수정하고  dynamicSplash를 생성할지 현재 customSplashView를 제거할지 분기처리

```swift

func setDynamicSplash(model: BannerCntList) {
        /// PRD URL
//        let URLString = makeString(model)
        /// TEST URL
        let URLString = "http://www.naver.com"
        print("URLString: \(URLString)")

        if isDynamicSplash {
            activeDynamicSplash(isDynamicSplash: isDynamicSplash, URLString: URLString, duration: 4)
        } else {
            print("isDynamicSplash is False")
            // MARK: 종료제어
            DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
                self.removeFromSuperview()
                print("종료 제어")
            }

        }
}

```

파라미터에 들어온 모델을 이용해 image의 경로를 생성하는 함수

```swift
func makeString(_ responseModel: BannerCntList) -> String {
    
        if let cntentFilePathNm = responseModel.cntentFilePathNm, let cntentFileNm = responseModel.cntentFileNm {
            Configs.tempSplashDirectoryURL = Configs.tempDynamicSplashHostMain + cntentFilePathNm + cntentFileNm
  
           return Configs.tempSplashDirectoryURL
        } else {
            return ""
        }
    }
```

이미지 URL을 받아서 loadImage함수로 global에서 다운로드처리

이미지 세팅은 main에서 처리후 정해진 시간만큼 보여주고 종료처리

```swift
func activeDynamicSplash(isDynamicSplash: Bool, URLString: String, duration : Double) {
        
        DispatchQueue.global().async {
            print("global().async로 이미지 다운로드 시작")
            let image = self.loadImage(from: URLString)

            DispatchQueue.main.async {
                print("main.async로 이미지 변경")
                self.splashImageViewReset(With: image)
                
                DispatchQueue.main.asyncAfter(deadline: .now() + duration) {
                    self.removeFromSuperview()
                    print("종료 제어")
                }
            }
        }
    }
```

이미지 URL 을 다운받아서 image로 리턴

```swift
func loadImage(from imageUrl: String) -> UIImage? {

        guard let url = URL(string: imageUrl) else { return nil }
        guard let data = try? Data(contentsOf: url) else { return nil }

        let image = UIImage(data: data)
        return image

    }
```

## RESTfulAPI

API개발이 완료되면 API연결작업을 실시한다. 

API URL을 가지고 다이나믹스플래시 여부를 체크하는 로직시작하기

splashInfoGetAPI함수의 completion에 담긴 result를 이용한다. 

```swift
func checkDynamicSplash() {
     
        let url = Configs.dynamicSplashAPIUrl
        print("dynamicSplashURL: \(url)")

        splashInfoGetAPI(with: url) { result, message in
            
            switch result{
            case .failure(let falseData):
                print("error: \(falseData.localizedDescription)")
            case .success(let data):
                if let splashData = data {
                    print("통신성공: \(splashData)")
                    self.getContentType(splashData)
                }
            }
        }
    }
```

RESTfulAPI 시작

네트워크 체크후, API 통신 시작,  completion에는 Result타입으로 성공시 받을타입, Error를 세팅한다. 

NetworkError는 error타입을 enum으로 정의했다.

completion(.success(    ) )안에 넣을 파싱 결과값은  상단 테스트단계에서 이미구현완료.

함수를 그대로 사용한다. 

```swift
enum NetworkError: Error {
    case noConnection
    case noResult
    case someError
}

func splashInfoGetAPI(with urlString: String, completion: @escaping(Result<BannerCntList?, NetworkError>, _ message: String?) -> Void) {
        
        if !Reachability.isConnectedToNetwork() {
            completion(.failure(.noConnection), Message.networkError)
            return
        }

        guard let url = URL(string: urlString) else { return }
        
        URLSession.shared.dataTask(with: url) { data, response, error in

            if error != nil {
                completion(.failure(.someError), nil)
            }
            
            guard let safeDate = data else {
                completion(.failure(.noResult), nil)
                return
            }
            print("data: \(data)")
            if let jsonParse = self.parseJSON(safeDate) {
                print("Completion넣을 jsonParse: \(jsonParse)")
                completion(.success(jsonParse), nil)
            } else {
                completion(.failure(.noResult), nil)
            }
            
        }.resume()
    }
```

### 전체 로직 간단정리

1. 직접 JSON을 생성해서  그값을 통해 splash를 구동하는 로직을 먼저 구현
2. API통신하는 부분을 구현해서 1번에 그대로 사용

# Comment

### 실수했던 점:

- CodeingKey를 주의할것
    
    quickType을 이용하여 모델링을 하는데 codingKey를 보는 세팅을 해제하는 바람에 바로 위에 쓰여진 1번 단계에선 제대로 동작했지만 2번에서는 동작하지않았다. 
    

### 유익했던 점

- JSON을 생성해보기도 하고 사용해보면서 이해도가 많이 올랐다.
