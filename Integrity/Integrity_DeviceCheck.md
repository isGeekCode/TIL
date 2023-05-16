# Integrity - DeviceCheck

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

## DeviceCheck API의 한계성
이 API는 디바이스 식별을 하기 위한 인터페이스이다. 때문에 여러 확인 결과, 로직상 계정서비스를 이용하는 경우에는 적합하지 않다.
하지만 커스텀 로직을 생성한다면 `앱  <-> 서버`에서 동일한 로직에 계정에 대한 식별자를 추가함으로 사용 가능하다고 판단된다.

## DeviceCheck API로 할 수 있는 것
- 각 사용자가 앱을 처음 설치한 시점을 확인하거나, 특정 기능을 사용한 시점을 추적가능
    - 앱이 처음 설치되거나 특정 기능이 처음 사용될 때 DeviceCheck API를 사용하여 해당 시점의 타임스탬프를 설정할 수 있다. 이후에 이 타임스탬프를 조회하여 사용자가 앱을 처음 설치한 시점이나 특정 기능을 처음 사용한 시점을 확인할 수 있다.
- 사용자가 앱을 삭제하고 다시 설치한 경우에도 그 사용자의 앱 사용 기록을 유지
    - 일반적으로 앱을 삭제하면 앱의 사용 기록도 함께 삭제되지만, DeviceCheck API를 사용하면 앱을 삭제하고 다시 설치한 후에도 사용 기록을 유지할 수 있다. 이는 앱이 기기에 대한 정보를 Apple의 서버에서 안전하게 관리하기 때문.
- 사기나 악용을 방지하기 위해 각 기기에서 앱의 사용량을 제한.
    - 디바이스 A에서 사용자가 어뷰징을하여 정지를 먹은 경우, 동일한 디바이스로 다른 계정을 새로 생성해도 정지를 먹도록 하고싶은 경우 사용
    - 앱에서 프리미엄 콘텐츠를 받은 고객과 불법적인 수단을 통해 프리미엄 콘텐츠를 얻은 고객을 구별할 수 있다.
    - 예를 들어, 무료 체험 기간이나 할인 쿠폰 등을 한 기기에서 한 번만 사용할 수 있도록 제한하거나, 일정 시간 동안 특정 기능을 사용할 수 있는 횟수를 제한하는 등의 기능을 구현할 수 있다. 이를 통해 사용자가 여러 계정을 생성하여 이러한 제한을 우회하는 등의 사기나 악용을 방지할 수 있다.

## DeviceCheck의 흐름
- 1. (App)장치 식별을 위한 토큰 생성 (이 토큰은 앱을 재설치해도 동일하다)
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

제공되는 API의 엔드포인트는 아래 3가지이다. 
- 기본도메인/v1/query_two_bits
- 기본도메인/v1/update_two_bits 
- 기본도메인/v1/validate_device_token

### 각 엔드포인트의 설명

- query_two_bits
    - 기존에 등록한 bits 정보를 조회하는 데 사용
    - 등록한 적이 없다면 reponse data에 `Failed to find bit state`로 응답받는다.
- update_two_bits
    - 새로운 bits 정보를 등록하는 데 사용
    - 특별한 response data 가 없다
- validate_device_token
    - 이미 등록한 기기토큰의 유효성을 검사하기 위해 사용
    - 한번도 등록하지않은 기기는 query_two_bits를 사용
    - 특별한 response data 가 없다


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

- query_two_bits
    - 값을 넣은 적이 없는 경우
        - header에는 JSON이라 정의되어있지만 parse error를 받는다.
        - data를 String으로 변환하면 `Failed to find bit state`라는 메세지로 응답받는다
    - 값이 있는 경우 
        - response JSON
        - [
            "bit0": 1
            "bit1": 0,
            "last_update_time": 2023-05
          ]
- update_two_bits
    - header에는 text라고 정의되어있지만 text가 빈 칸으로 들어온다.
    - Status Code가 200 인걸로 판단이 가능하다.

- validate
    - header에는 JSON이라 정의되어있지만 JSON이 빈 칸으로 들어온다.
    - Status Code가 200 인걸로 판단이 가능하다.


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

- Statue Code
- Headers
    - Content-Encoding
        - payload의 압축 형식
    - Content-Length
        - payload의 용량
    - Content-Type
        - payload의 형식이 어떤 형식이고 인코딩 형식이 무엇인지
        - 예시
            - "application/json; charset=UTF-8"
            - "text/plain; charset=UTF-8"
    - Date
        - response 받은 날짜와 시간
    - Server
        - 서버가 Apple사의 서버임을 나타냄
    - Strict-Transport-Security
        - 예 : `"max-age=31536000; includeSubdomains"`
        - 엄격한 전송 보안 정책이 적용되어 있음을 표시. 보안 헤더 중 하나로, 브라우저에게 HTTPS를 통한 통신만 허용하고, 보안 기간이 1년(31536000초)으로 설정되었음을 표시. 서브도메인도 포함되어야 함을 의미.
    - apple-originating-system
        - request의 출처 
        - 예시 : `UnknownOriginatingSystem` (왜 알수없음???)
    - apple-seq
        - Apple 시퀀스 번호
    - apple-tk
        -  Bool타입으로 Apple token 여부
    - x-apple-jingle-correlation-key
        - Apple Jingle 키로, Apple 사에서 사용하는 내부 운용을 위한 키.
    - x-apple-request-uuid
        - Apple 요청 UUID로, Apple 사에서 생성된 요청의 고유 식별자
    - x-content-type-options
        - 브라우저에서 MIME 타입을 자동으로 감지하지 않도록 설정
    - x-frame-options
        - 브라우저에서 해당 응답을 iframe으로 사용할 수 있는지 제한. 
        - 예: `SAMEORIGIN` - 동일한 출처에서만 iframe으로 사용할 수 있음을 의미.
    - x-responding-instance
        - 이 헤더는 HTTP 응답에서 서버의 응답 인스턴스를 식별하는 데 사용.
        - 일반적으로 이 헤더는 로드 밸런서, 프록시 서버 또는 백엔드 서버 클러스터와 같은 환경에서 사용된다.
        - 각 서버 또는 인스턴스는 고유한 식별자를 가지며, 이를 통해 요청이 특정 서버 또는 인스턴스로 라우팅되었음을 확인할 수 있다.
    - x-xss-protection
        - 이 헤더는 브라우저에서 크로스 사이트 스크립팅(XSS) 공격을 방지하기 위한 보호 기능을 활성화하는 데 사용.
        - 이 헤더를 사용하여 브라우저가 XSS 공격을 탐지하고 차단하는 기능을 활성화할 수 있다.
        - 값으로 "1; mode=block"을 설정하면 브라우저는 XSS 공격을 감지하면 페이지 로딩을 차단하여 보안을 강화한다는 의미.
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
    guard let reqUrl = URL(string: url) else {
        print("url is nil or empty")
        return
    }
    print("request URL::\(reqUrl)")
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
        guard error == nil, let responseData = data else {
            if let error = error {
                // 오류 처리
                errorHandler(error)
                print("dataTask Error: \(error.localizedDescription)")
            }
            return
        }
        print("response : \(String(describing: response))\ndata : \(String(describing: data))");
        
        
        // 응답의 Content-Type 헤더 확인
        if let httpResponse = response as? HTTPURLResponse,
           let contentType = httpResponse.allHeaderFields["Content-Type"] as? String {
            
            if let dateString = httpResponse.allHeaderFields["Date"] as? String {
                // GMT를 한국시간으로 보여주기
                let dateFormatter = DateFormatter()
                dateFormatter.dateFormat = "E, d MMM yyyy HH:mm:ss zzz"
                dateFormatter.locale = Locale(identifier: "en_US_POSIX")
                dateFormatter.timeZone = TimeZone(abbreviation: "GMT")
                
                if let date = dateFormatter.date(from: dateString) {
                    let koreaTimeZone = TimeZone(identifier: "Asia/Seoul")
                    dateFormatter.timeZone = koreaTimeZone
                    dateFormatter.dateFormat = "yyyy-MM-dd HH:mm:ss"
                    
                    let koreaDateStr = dateFormatter.string(from: date)
                    print("Korea Time: \(koreaDateStr)")
                } else {
                    print("Failed to convert date")
                }
            }
            
            print("allHeaderFields: \(httpResponse.allHeaderFields)")
            
            if contentType.contains("application/json") {
                print("allHeaderFields.Content-Type: \(httpResponse.allHeaderFields["Content-Type"] as? String)")
                
                // JSON 데이터인 경우 파싱 수행
                do {
                    if let json = try JSONSerialization.jsonObject(with: responseData, options: []) as? [String: Any] {
                        // 파싱된 JSON 데이터 전체를 활용하는 경우
                        print("Parsed JSON: \(json)")
                        successHandler(json)
                    } else {
                        print("Invalid JSON format")
                    }
                } catch let error {
                    // JSON 데이터 파싱 중에 오류가 발생한 경우
                    if responseData.isEmpty {
                        print("Data is empty")
                    } else {
                        errorHandler(error)
                        print("Error: \(error)")
                        print("Error: \(error.localizedDescription)")
                        
                        // query인 경우에 body는 여기에 텍스트로만 온다.
                        if let responseString = String(data: responseData, encoding: .utf8) {
                            print("Response data string:\n \(responseString)")
                        }
                    }
                }
            } else if contentType.contains("text/plain") {
                // Content-Type이 JSON이 아닌 경우에 대한 처리
                print("Content-Type is TEXT")
                if let textData = String(data: responseData, encoding: .utf8) {
                    if !textData.isEmpty {
                        // 텍스트 데이터에 접근하여 필요한 작업 수행
                        print("Text Data: \(textData)")
                    } else {
                        print("Text Data is empty")
                    }
                    
                    // 필요한 작업을 수행한 후, successHandler 등을 호출하여 결과를 처리할 수 있음
                } else {
                    print("Failed to decode text data")
                }
                
            } else {
                print("Content-Type is not JSON, TEXT")
            }
        } // contentType 여부
    }).resume()
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
- 230515 : 테스트앱 구현
- 230516 : 각 엔드포인트별 분석 및 엔드포인트별 에러처리
