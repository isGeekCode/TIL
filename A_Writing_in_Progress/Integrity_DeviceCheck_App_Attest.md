# Integrity - DeviceCheck & App Attest

앱과 콘텐츠를 보호하기 위해 만들어진 Apple의 강력한 사기 방지 도구인 App Attest 및 DeviceCheck를 사용하는 방법을 알아보자.

앱과 콘텐츠의 무단 수정을 차단하기 위해 App Attest를 앱에 통합하여 배포해보자.

또한 DeviceCheck를 사용하여 앱에서 프리미엄 콘텐츠를 받은 고객과 불법적인 수단을 통해 프리미엄 콘텐츠를 얻은 고객을 구별할 수 있도록 하는 방법을 알아보자.


# DeviceCheck 
애플에서 제공하는 고유한 디바이스 식별을 가능하게 해주는 API 서비스다.
WWDC17에 공개되어 iOS11부터 지원한다. 아쉽게도 해당 영상은 Apple에서 내려갔다.(왜지)

이 API는 애플 클라우드에서 2bit의 저장공간을 제공한다. 그래서 해당 디바이스의 상태를 기록할 수 있다. 이때 앱을 재설치, 아이클라우드 계정 변경, 공장 초기화를 해도 이 2bit는 유지가 된다. 

이 두 bit값의 의미는 개발자가 정의하여 자유롭게 사용이 가능하다. 
세팅할 수 있는 상태는 4가지만 존재한다. 
- 세팅할 수 있는 상태
    - [0, 0]
    - [1, 0]
    - [0, 1]
    - [1, 1]  

![img1 daumcdn-12](https://github.com/isGeekCode/TIL/assets/76529148/405caa0f-089c-49fd-b256-43f41fba71a4)
  
<p align="center">사용예시 - (이미지 출처 : 김종권의 iOS앱 개발 알아가기)</p>  


## DeviceCheck의 흐름
- 1. (App)장치 식별을 위한 임시 토큰 생성
- 2. (App -> Backend) token data를 post형식으로 Backend에 데이터를 보내 JWT 생성
- 3. (Backend -> Apple Server) backend에서 만든 JWT token data를 post형식으로 apple server에 전달 
- 4. (Apple Server -> Backend) apple에서 2bit 응답값과 상태를 Response
- 5. (Backend -> App) backend에서 보관 및 처리, iOS App에서 필요하면 상태 전달
    - (해당 디바이스가 blacklist인지.. 등)

![server-1](https://github.com/isGeekCode/TIL/assets/76529148/efcce0e6-5032-4714-9362-92c2cf8f86dd)


## 두 가지 방법
- 1번째. 중간에 Server를 두고 App <-> Server(Backend) <-> Apple Server
    - 위에서 설명한 5단계의 흐름과 동일하다.
- 2번째. 중간에 Serverless로 App <-> Apple Server
    - Backend에서 할 작업을 App내에서 처리한다.


### 1. (App)장치 식별을 위한 임시 토큰 생성부분

앱에서 DeviceCheck모듈안의 generateToken함수를 통해 TokenData 획득
```swift
import DeviceCheck

if DCDevice.current.isSupported { 
    DCDevice.current.generateToken { dataData, error in
      guard let dataData = dataData else {
        print("token is empty: \(error!.localizedDescription)")
        return
      }
      let tokenString = dataData.base64EncodedString()
      print("임시 DeviceToken :: \(tokenString)")
      // AgAAAHXbhcMDrOhwYgRYbuTll...+4V94A==
      
      // deviceToken은 Back-end로 가서 애플서버를 거쳐 다시 App으로 
      // use URLSession or something to send the token string to your server API
    }​
}

// 이 값을 서버로 보내주는 작업까지가 APP에서 하는 작업의 전부다.
```
  
- 주의할점
    - 시뮬레이터는 isSupported를 통과하지 않기때문에 테스트를 하려면 실제 디바이스를 사용한다.
    - 사용가능한 Apple Developer account가 프로젝트에 세팅이 되어있어야 한다.

  
### DeviceCheck Key 생성방법
DeviceCheck API를 사용하기 위해서는 Apple Developer 에서 DeviceCheck 키를 발급해야한다. 

- [Apple Developer Website](Developer.apple.com/account)에 들어간다.
- 인증서, 식별자 및 프로파일 카테고리 - 키 를 클릭한다. 
- 키 페이지에서 `+`버튼을 클릭
- 구분할 키 이름 입력 / DeviceCheck 체크박스를 체크 / Continue를 누른다.
- `Confirm`버튼 클릭
- 생성된 p8형식의 개인키(privateKey)를 다운로드 한다.
    - 이 파일은 최초 1회만 받을 수 있기때문에 잘 보관하자.
    
### DeviceCheck Flow를 위한 준비물
- Team ID
    - [Apple Developer Website](https://developer.apple.com/account) 에 들어가면 멤버십 세부 사항에서 찾을 수 있다.
- Key ID
    - 생성한 DeviceCheck키를 클릭하면 볼 수 있다.
- privateKey.p8

### Apple 사양의 JWT(JSON Web Token)형식 생성
- 알고리즘 : ES256
```
//HEADER:
{
  "alg": "ES256",
  "kid": Key ID
}
//PAYLOAD:
{
  "iss": Team ID,
  "iat": 요청 타임스탬프 (Unix Timestamp,EX:1556549164),
  "exp": 만료 타임스탬프 (Unix Timestamp,EX:1557000000)
}
//타임스탬프는 반드시 정수 형식이어야 한다
```

조합된 JWT 문자열: xxxxxx.xxxxxx.xxxxxx

![jwt-1](https://github.com/isGeekCode/TIL/assets/76529148/b1da6067-0613-4129-9884-27a4d4ee9f7d)
<p align="center">
    <a href="https://fluffy.es/devicecheck-tutorial/" style="text-align: center;">출처 : fluffy blog about DeviceCheck </a>
</p>  
  
  
### 루비코드
```ruby
require 'openssl'
require 'http'
require 'jwt'
require 'securerandom'

def jwt_token
  # use the content of the .p8 key file you downloaded, it should look like this :
  #-----BEGIN PRIVATE KEY-----
  #ILIKEFOXES
  #-----END PRIVATE KEY----
  private_key = ENV['DEVICE_CHECK_KEY_STRING']
  
  # the Key ID you saw earlier
  key_id = ENV['DEVICE_CHECK_KEY_ID']
  
  # Team ID of your Apple developer account
  team_id = ENV['DEVICE_CHECK_TEAM_ID']

  # Elliptic curve key, used to encrypt the JWT
  ec_key = OpenSSL::PKey::EC.new(private_key)
  jwt_token = JWT.encode({iss: team_id, iat: Time.now.to_i}, ec_key, 'ES256', {kid: key_id,})
end
```
### Php로 구현
```php
<?php
require_once "vendor/autoload.php";
use Zenstruck\JWT\Token;
use Zenstruck\JWT\Signer\OpenSSL\ECDSA\ES256;
use \Ramsey\Uuid\Uuid;

// _POST에서 deviceToken을 수신

$deviceToken = (isset($_POST["deviceToken"]) ? $_POST["deviceToken"] : null);

function generateJWT($teamId, $keyId, $privateKeyFilePath) {
    $payload = [
        "iss" => $teamId,
        "iat" => time()
    ];

    $header = [
        "kid" => $keyId
    ];

    $token = new Token($payload, $header);
    return (string)$token->sign(new ES256(), $privateKeyFilePath);
}

function postRequest($url, $jwt, $bodyArray) {
    $body = json_encode($bodyArray);

    $header = [
        "Authorization: Bearer ". $jwt,
        "Content-Type: application/x-www-form-urlencoded",
        "Content-Length: ".strlen($body)
    ];

    $context = [
        "http" => [
            "method"  => "POST",
            "header"  => implode("\r\n", $header),
            "content" => $body
        ]
    ];

    return file_get_contents($url, false, stream_context_create($context));
}

$teamId = "TEAMID";
$keyId = "KEYID";
$privateKeyFilePath = "PRIVATE KEY FILE PATH";
$jwt = generateJWT($teamId, $keyId, $privateKeyFilePath);

//  Response Payload
$body = [
    "device_token" => $deviceToken,
    "transaction_id" => Uuid::uuid4()->toString(),
    "timestamp" => ceil(microtime(true)*1000)
];
postRequest("https://api.development.devicecheck.apple.com/v1/query_two_bits", $jwt, $body);
// 대부분의 예제에서 개발API는 동작하지않는 경우가 있었다.
//  아직 정보를 설정하지 않은 경우 "Failed to find bit state"로 반환된다.
//  설정하고 있는 경우는 아래 형태로 반환된다.
/*
  {
    "bit0":true,
    "bit1":false,
    "last_update_time":"2017-06"
  }
*/

//  Update를 하는 경우
$body = [
    "device_token" => $deviceToken,
    "transaction_id" => Uuid::uuid4()->toString(),
    "timestamp" => ceil(microtime(true)*1000),
    "bit0" => true,
    "bit1" => false
];

postRequest("https://api.development.devicecheck.apple.com/v1/update_two_bits", $jwt, $body);
```
  
  
  
### Apple 서버로 데이터 전송
APNS 푸시 브로드캐스트와 마찬가지로 두종류의 환경(운영, 개발)이 있다.

1. 개발 환경: https://api.devicecheck.apple.com
2. 운영 환경: https://api.development.devicecheck.apple.com

제공되는 API 경로는 아래 3가지이다. 
- 기본도메인/v1/query_two_bits
- 기본도메인/v1/update_two_bits 
- 기본도메인/v1/validate_device_token

### 1. 저장되어있는 데이터 쿼리 요청하기
- 기본도메인/v1/query_two_bits
Header의 Authorization에는 위에서 생성한 JWT문자열을 입력한다.
```
//Headers:
Authorization: Bearer xxxxxx.xxxxxx.xxxxxx (조합된 JWT 문자열)

//Content(payload):
{
    device_token:deviceToken (조회할 deviceToken)
    transaction_id:UUID().uuidString (쿼리 식별자, 여기서 직접 UUID로 표시)
    timestamp: 요청 타임스탬프（"밀리세컨드"）（EX: 1556549164000）
}
```

### 루비코드
```ruby
require 'openssl'
require 'http'
require 'jwt'
require 'securerandom'

def query_two_bits(device_token)
  payload = {
    'device_token' => device_token,
    'timestamp' => (Time.now.to_f * 1000).to_i,
    'transaction_id' => SecureRandom.uuid
  }

  query_url = 'https://api.development.devicecheck.apple.com/v1/query_two_bits'
  response = HTTP.auth("Bearer #{jwt_token}").post(query_url, json: payload)

  # if there is no bit state set before, 
  # Apple will return the string 'Bit State Not Found' instead of json

  # if the bit state was set before, json below will be returned
  #{"bit0":false,"bit1":false,"last_update_time":"2018-10"}
end
```

### Response status
query_two_bits 및 update_two_bits를 통해 사용하여 서버와 통신할 때 아래 표에 나열된 응답 코드 중 하나를 받을 수 있다.

<img width="800" alt="스크린샷 2023-05-11 오후 2 02 38" src="https://github.com/isGeekCode/TIL/assets/76529148/54eea091-9f6e-4d89-ae65-4518e463fc2a">

<p align="center">
    <a href="https://developer.apple.com/documentation/devicecheck/dcdevice" style="text-align: center;">출처 : Apple Document : DeviceCheck </a>
</p> 

### Response payload
```
{
  "bit0": Int(0 또는 1),
  "bit1": Int(0 또는 1),
  "last_update_time": String："최종 수정 시간 YYYY-MM"
}
```


### 1. 저장되어있는 데이터 쿼리 update하기
- 기본도메인/v1/update_two_bits
```
//Headers:
Authorization: Bearer xxxxxx.xxxxxx.xxxxxx (조합된 JWT 문자열)

//Content(payload):
{
    device_token:deviceToken (조회할 deviceToken)
    transaction_id:UUID().uuidString (쿼리 식별자, 여기서 직접 UUID로 표시)
    timestamp: 요청 타임스탬프（"밀리세컨드"）（EX: 1556549164000）
    bit0: Int(0 또는 1),
    bit1: Int(0 또는 1),
}
```


### 루비코드
```ruby
require 'openssl'
require 'http'
require 'jwt'
require 'securerandom'

def update_two_bits(device_token, bit_zero, bit_one)
  payload = {
    'device_token' => device_token,
    'timestamp' => (Time.now.to_f * 1000).to_i,
    'transaction_id' => SecureRandom.uuid,
    'bit0': bit_zero, # true / false
    'bit1': bit_one # true / false
  }

  response = HTTP.auth("Bearer #{jwt_token}").post(update_url, json: payload)
  # Apple will return status 200 with blank response body if the update is successful
end
```

- Response 종류는 위와 동일

### Response 내용
update를 할때에는 따로 반환내용이 없다. 반환값이 200일 경우, update성공이다. 




## 2번째 CupertinoJWT 라이브러리를 이용한 Serverless 로직

```swift
//
//  ViewController.swift
//  DCDeviceTest
//
//  Created by 李仲澄 on 2019/4/29.
//  Copyright © 2019 ZhgChgLi. All rights reserved.
//
import UIKit
import DeviceCheck
import CupertinoJWT

extension String {
    var queryEncode:String {
        return self.addingPercentEncoding(withAllowedCharacters: .whitespacesAndNewlines)?.replacingOccurrences(of: "+", with: "%2B") ?? ""
    }
}
class ViewController: UIViewController {

    
    @IBOutlet weak var getBtn: UIButton!
    @IBOutlet weak var statusBtn: UIButton!
    @IBAction func getBtnClick(_ sender: Any) {
    
        DCDevice.current.generateToken { dataOrNil, errorOrNil in
            guard let data = dataOrNil else { return }
            
            let deviceToken = data.base64EncodedString()
            
            //正式情況：
            //POST deviceToken 到後端，請後端去跟蘋果伺服器查詢，然後再回傳結果給APP處理
            
            
            //!!!!!!以下僅為測試、示範所需，不建議用於正式環境!!!!!!
            //!!!!!!      請勿隨意暴露您的PRIVATE KEY    !!!!!!
                let p8 = """
                    -----BEGIN PRIVATE KEY-----
                    -----END PRIVATE KEY-----
                    """
                let keyID = "" //你的KEY ID
                let teamID = "" //你的Developer Team ID :https://developer.apple.com/account/#/membership
            
                let jwt = JWT(keyID: keyID, teamID: teamID, issueDate: Date(), expireDuration: 60 * 60)
            
                do {
                    let token = try jwt.sign(with: p8)
                    var request = URLRequest(url: URL(string: "https://api.devicecheck.apple.com/v1/update_two_bits")!)
                    request.httpMethod = "POST"
                    request.addValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
                    request.addValue("application/x-www-form-urlencoded", forHTTPHeaderField: "Content-Type")
                    let json:[String : Any] = ["device_token":deviceToken,"transaction_id":UUID().uuidString,"timestamp":Int(Date().timeIntervalSince1970.rounded()) * 1000,"bit0":true,"bit1":false]
                    request.httpBody = try? JSONSerialization.data(withJSONObject: json)
                    
                    let task = URLSession.shared.dataTask(with: request) { (data, response, error) in
                        guard let data = data else {
                            return
                        }
                        print(String(data:data, encoding: String.Encoding.utf8))
                        DispatchQueue.main.async {
                            self.getBtn.isHidden = true
                            self.statusBtn.isSelected = true
                        }
                    }
                    task.resume()
                } catch {
                    // Handle error
                }
            //!!!!!!以上僅為測試、示範所需，不建議用於正式環境!!!!!!
            //
            
        }

    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        DCDevice.current.generateToken { dataOrNil, errorOrNil in
            guard let data = dataOrNil else { return }
            
            let deviceToken = data.base64EncodedString()
            
            //正式情況：
                //POST deviceToken 到後端，請後端去跟蘋果伺服器查詢，然後再回傳結果給APP處理
            
            
            //!!!!!!以下僅為測試、示範所需，不建議用於正式環境!!!!!!
            //!!!!!!      請勿隨意暴露您的PRIVATE KEY    !!!!!!
                let p8 = """
                -----BEGIN PRIVATE KEY-----
                
                -----END PRIVATE KEY-----
                """
                let keyID = "" //你的KEY ID
                let teamID = "" //你的Developer Team ID :https://developer.apple.com/account/#/membership
            
                let jwt = JWT(keyID: keyID, teamID: teamID, issueDate: Date(), expireDuration: 60 * 60)
            
                do {
                    let token = try jwt.sign(with: p8)
                    var request = URLRequest(url: URL(string: "https://api.devicecheck.apple.com/v1/query_two_bits")!)
                    request.httpMethod = "POST"
                    request.addValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
                    request.addValue("application/x-www-form-urlencoded", forHTTPHeaderField: "Content-Type")
                    let json:[String : Any] = ["device_token":deviceToken,"transaction_id":UUID().uuidString,"timestamp":Int(Date().timeIntervalSince1970.rounded()) * 1000]
                    request.httpBody = try? JSONSerialization.data(withJSONObject: json)
                    
                    let task = URLSession.shared.dataTask(with: request) { (data, response, error) in
                        guard let data = data,let json = try? JSONSerialization.jsonObject(with: data, options: .mutableContainers) as? [String:Any],let stauts = json["bit0"] as? Int else {
                            return
                        }
                        print(json)
                        
                        if stauts == 1 {
                            DispatchQueue.main.async {
                                self.getBtn.isHidden = true
                                self.statusBtn.isSelected = true
                            }
                        }
                    }
                    task.resume()
                } catch {
                    // Handle error
                }
            //!!!!!!以上僅為測試、示範所需，不建議用於正式環境!!!!!!
            //
            
        }
        // Do any additional setup after loading the view.
    }


}

```

작업을 해보니 response는 아래 내용이 포함되어있다.
content-type을 보면 `application/json`이라고 나오는데 상황에 따라   `"text/plain`으로 나오는 경우도 있다. 여길 참고한다.

- Statue Code
- Headers
    - Content-Encoding
    - Content-Length
    - Content-Type
    - Date
    - Server
    - Strict-Transport-Security
    - apple-originating-system
    - apple-seq
    - apple-tk
    - x-apple-jingle-correlation-key
    - x-apple-request-uuid
    - x-content-type-options
    - x-frame-options
    - x-responding-instance
    - x-xss-protection

```
{ Status Code: 200, Headers {
    "Content-Encoding" =     (
        gzip
    );
    "Content-Length" =     (
        44
    );
    "Content-Type" =     (
        "application/json; charset=UTF-8"
    );
    Date =     (
        "Fri, 12 May 2023 02:00:53 GMT"
    );
    Server =     (
        Apple
    );
    "Strict-Transport-Security" =     (
        "max-age=31536000; includeSubdomains"
    );
    "apple-originating-system" =     (
        UnknownOriginatingSystem
    );
    "apple-seq" =     (
        0
    );
    "apple-tk" =     (
        false
    );
    "x-apple-jingle-correlation-key" =     (
        33C6GFPHY2UNZB5I5BSFUB7YWE
    );
    "x-apple-request-uuid" =     (
        
        // 보안상 비공개
    );
    "x-content-type-options" =     (
        nosniff
    );
    "x-frame-options" =     (
        SAMEORIGIN
    );
    "x-responding-instance" =     (
        "af-bit-store-7858cd868d-d4xxn"
    );
    "x-xss-protection" =     (
        "1; mode=block"
    );
} }
```

## 테스트 작업

### APP-SIDE
```swift

enum DeviceCheckType {
    case query
    case update
    case validation
    
    var path: String {
        switch self {
        case .query: return "query_two_bits"
        case .update: return "update_two_bits"
        case .validation: return "validate_device_token"
        }
    }
}

func appSideAction() {
    generateDeviceToken { deviceToken in
    
        // 생성된 deviceToken은 CustomServer로 보내는 과정 대신 server-side 함수로 구현
        // 통신 타입에 따라 세가지로 사용가능하다.
        /*
        self.serverSideAction(deviceToken: deviceToken, deviceCheckType: .validation)
        self.serverSideAction(deviceToken: deviceToken, deviceCheckType: .query)
        self.serverSideAction(deviceToken: deviceToken, deviceCheckType: .update, insertValue: [true, true])
        */
    }
}

/// DeviceToken을 생성하여 생성완료 시점을 확정하기 위해 Completion사용
func generateDeviceToken(completion: @escaping (String) -> ()) {
    var deviceToken = ""
    if DCDevice.current.isSupported {
        DCDevice.current.generateToken { dataData, error in
            guard let dataData = dataData else {
                print("token is empty: \(error!.localizedDescription)")
                return
            }
            deviceToken = dataData.base64EncodedString()
            completion(deviceToken)
            // AgAAAHXbhcMDrOhwYgRYbuTll...+4V94A==
        }
    }
}
```

### Server-Side
커스텀 서버에서 동작할 로직, JWT를 생성하여 Apple Server로 전송
테스트를 위해 앱안에서 Serverless로 구현

```swift
/// - Parameter deviceToken: 앱에서 생성된 토큰값
func serverSideAction(deviceToken : String, deviceCheckType: DeviceCheckType = .query, insertValue: [Bool] = [true, true]) {
    // Back-end 작업을 여기서 처리
    let jwt = self.generateJWT()
    if jwt.isEmpty { return }

    var json:[String : Any] = [
        "device_token" : deviceToken,
        "transaction_id" : UUID().uuidString,
        "timestamp" : Int(Date().timeIntervalSince1970.rounded()) * 1000
    ]

    let pathString = "https://api.devicecheck.apple.com/v1/\(deviceCheckType.path)"

    // UPDATE할때만 BIT가 추가된다.
    if deviceCheckType == .update {
        guard insertValue.count >= 2,
              let firstBit = insertValue.first,
              let secondBit = insertValue.last else { return }
        
        json["bit0"] = firstBit
        json["bit1"] = secondBit
    }
    print("json: \(json)")

//  통신부
    self.postDataForDeviceCheck(url: pathString, token: jwt, parameters: json) { resultData in

        guard let data = resultData else { return }
        print("responseData: \(data)")

    } errorHandler: { error in
        print("deviceCheckAPI error ::: \(error)")
    }
}

    func generateJWT() -> String {
        print("Back-end 작업 시작")

        let p8 = """
            -----BEGIN PRIVATE KEY-----
            // 고유값
            -----END PRIVATE KEY-----
            """
        let keyID = "PDJF이런값" //KEY ID
        let teamID = "3KFKS이런값" //Developer Team ID

        let jwt = JWT(keyID: keyID, teamID: teamID, issueDate: Date(), expireDuration: 60 * 60)
        print("JWT INIT::\(jwt)")
        
        do {
            let token = try jwt.sign(with: p8)
            print("jwt token String 생성완료 ::\n\(token)")
            return token

        } catch {
            print("error:\(error.localizedDescription)")
            return ""
        }
    }



func postDataForDeviceCheck(url: String, token: String, parameters: [String: Any], successHandler: @escaping (_ resultData: [String:Any]?)-> Void, errorHandler: @escaping (_ error: Error) -> Void) -> Void {
 print("들어온 url: \(url)")
    if let reqUrl = URL(string: url) {
        print("생성된 queryURL::\(reqUrl)")
        var request = URLRequest(url: reqUrl)
        request.httpMethod = "POST"
        request.addValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        
        if parameters.count > 0 {
            request.addValue("application/x-www-form-urlencoded", forHTTPHeaderField: "Content-Type")
            do {
                request.httpBody = try JSONSerialization.data(withJSONObject: parameters, options: .prettyPrinted)
            } catch {
                successHandler(nil)
                print("JSON Pasing Error")
            }
        }
    
    
        URLSession.shared.dataTask(with: request, completionHandler: { (data: Data?, response: URLResponse?, error: Error?) in
            //error 일경우 종료
            guard error == nil && data != nil else {
                if let err = error {
                    errorHandler(err)
                    print(err.localizedDescription)
                }
                return
            }
            
            // response를 확인하여 어떤 타입으로 들어오는지 확인할것
            // 서버에 값이 없는경우, 있는 경우에 따라 파싱방법이 달라져야한다. 
            guard let response = response else { return }
            print("response: \(response)")

                if let resultData = data {
                    // text/plain으로 들어올때 확인용
                    
                    if let resultString = NSString(data: resultData, encoding: String.Encoding.utf8.rawValue) {
                        let resultStr = String(resultString)
                        print("resultStr: \(resultStr)")
                        /*
                         최초 bit 값이 등록되지않은 경우는 Failed to find bit state 값이 나온다.
                         validation을 할경우: Unable to parse empty data
                         */

                        //메인쓰레드에서 출력하기 위해
                        DispatchQueue.main.async {
                            
                            do {
                                
                                if let json = try JSONSerialization.jsonObject(with: resultData, options: []) as? [String: Any] {
                                    // 파싱된 JSON 데이터에 접근하여 필요한 작업 수행
                                    // 예시: JSON 데이터에서 특정 키 값을 가져와서 처리
                                    print("jsonResult: \(json)")
                                    successHandler(json)
                                    // 다른 필요한 작업 수행
                                    
                                } else {
                                    // JSON 데이터 파싱에 실패한 경우
                                    print("Invalid JSON format")
                                }
                                
                            } catch {
                                errorHandler(error);
                                print("parsing error : \(error.localizedDescription)")
                            }
                        } // DispatchQueue
                        
                        
                    } //resultString
                } else {
                    print("data is Nil")
                } // resultData = data
            
        }).resume()


    } else {
        print("url is nil or empty")
    } // url check
}


```

###
```
        /*
         // MARK: 애플로 보내는 JWT 형식
         //HEADER:
         {
           "alg": "ES256",
           "kid": Key ID  // Developer 웹사이트에서 DeviceCheck키를 발급할 때, 적어둔 Key ID
         }
         //PAYLOAD:
         {
           "iss": Team ID,
           "iat": 요청 타임스탬프 (Unix Timestamp,EX:1556549164),
           "exp": 만료 타임스탬프 (Unix Timestamp,EX:1557000000)
         }
         //타임스탬프는 반드시 정수 형식이어야 한다
         
         // cupertinoJWT 특징
         - ES256 형식
         - issueDate에 들어가는 Date타입을 변환
         - expireDuration에 interval만 넣으면 자동으로 합산처리
      
      
        // MARK: 파라미터
        // update_two_bits
        let json:[String : Any] = [
            "device_token":deviceToken,
            "transaction_id":UUID().uuidString,
            "timestamp":Int(Date().timeIntervalSince1970.rounded()) * 1000,
            "bit0":true,
            "bit1":false
        ]
         
        // query_two_bits
        let json:[String : Any] = [
            "device_token":deviceToken,
            "transaction_id":UUID().uuidString,
            "timestamp":Int(Date().timeIntervalSince1970.rounded()) * 1000
        ]
         */

```


## 참고링크
- [AppleDocument: DeviceCheck Framework ](https://developer.apple.com/documentation/devicecheck)
- [Blog - 일회성 제안 또는 평가판을 실행하는 iOS의 완벽한 방법(Chinese)](https://medium.com/zrealm-ios-dev/ios-%E5%AE%8C%E7%BE%8E%E5%AF%A6%E8%B8%90%E4%B8%80%E6%AC%A1%E6%80%A7%E5%84%AA%E6%83%A0%E6%88%96%E8%A9%A6%E7%94%A8%E7%9A%84%E6%96%B9%E6%B3%95-swift-c5e7e580c341)
- [서버단 API (Japanese)](https://qiita.com/owen/items/85dff1e45083d2805140)
- [Blog - DeviceCheck API 사용 방법, 고유한 디바이스 ID (UDID 대체, Device block)](https://ios-development.tistory.com/848)
- [Blog - iOS 11: The DeviceCheck API](https://medium.com/the-traveled-ios-developers-guide/devicecheck-6f3eafac60e5)
- [Blog - [iOS/WWDC] App Attest & Device Check](https://jooeungen.tistory.com/entry/iOSWWDC-App-Attest-Device-Check)
- [WWDC21: AppAttest and DeviceCheck](https://developer.apple.com/videos/play/wwdc2021/10244/)
- [WWDC21: Safeguard your accounts, promotions, and content
](https://developer.apple.com/videos/play/wwdc2021/10110)
- [한번더 확인해봐야하는 WWDC15:Privacy your Apps](https://developer.apple.com/videos/play/wwdc2015/703/)
- [Blog - Uniquely identify iOS device using DeviceCheck (Tutorial)](https://fluffy.es/devicecheck-tutorial/)
  
  
## History
- 230511 : 초안 및 레퍼런스 작성
- 230512 : DeviceCheck 서버리스 구현 성공, 코드 편집후 업로드

