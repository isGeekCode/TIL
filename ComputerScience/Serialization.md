# 직렬화(Serialization)

- 참고링크
    - [TIL: iOS에서의 직렬화(Serialization하기)](https://github.com/isGeekCode/TIL/blob/main/iOS-Development/iOS_JSONSerializationMethod.md)
    - [TIL: JSONSerialization으로  직렬화하기](https://github.com/isGeekCode/TIL/blob/main/iOS-Foundation/Foundation_JSONSerialization.md)
    - [TIL: Codable로 직렬화하기](https://github.com/isGeekCode/TIL/blob/main/iOS-Swift/Codable.md)

<br><br>

직렬화란 데이터를 일련의 바이트나 비트열로 변환하는 과정을 말한다.  

컴퓨터에서는 데이터를 메모리에 저장하거나 파일에 쓰거나,   

또는 네트워크를 통해 전송하기 위해 데이터를 일련의 바이트로 변환해야할 필요가 있다.  

이때, 바이트로 변환하는 작업을 직렬화 라고 한다.  

<br><br>

직렬화는 다양한 데이터 형식을 지원하며, 데이터를 이진형식으로 저장하거나 전송할 수 있다.  

주로 데이터를 JSON,  XML, Protocol Buffers, MessagePack, BSON 등과 같은 형식으로 직렬화 하여 사용한다.  

직렬화는 데이터의 보존과 공유를 위해 매우 중요한 과정이기 때문에,  

서버와 클라이언트 간의 통신이나 데이터베이스에서 데이터를 저장하는 등 다양한 상황에서 사용된다. 

직렬화를 거꾸로 수행하는 과정은 역직렬화(Deserialization)라고 한다.  

<br><br><br>

## OSI 7 Layer에서의 직렬화
OSI 7계층은 네트워크 통신에서 데이터 전송을 단계별로 나누어 관리하는 모델로,   

각 계층마다 특정한 역할과 기능을 갖고 있다.  

<br><br><br>

### 물리계층
물리계층은 실제 데이터 전송을 담당하는 계층으로, 데이터를 전기신호로 변환하거나 무선신호로 변환하여 물리적인 매체를 통해 네트워크상에서 전송한다.  

물리계층에서는 데이터를 디지털 데이터로 변환하거나 디지털 데이터를 아날로그 신호로 변환하는 등의 직렬화 과정이  이루어진다.  물리 계층에서는 데이터 비트단위로 직렬화하고 전송하며, 이 작업은 전송 매체에 맞게 변환되어 전송된다.

<br><br><br>

### 데이터 링크 계층
데이터 링크 계층은 물리계층으로부터 받은 데이터를 프레임형태로 나누고, 각 프레임에 헤더와 트레일러를 추가하여 네트워크를 통해 안전하게 전송하는 역할을 한다.  

데이터 링크 계층에서도 데이터를 직렬화하여 전송하는 과정이 포함된다.  

데이터 링크 계층에서는 물리계층에서 받은 데이터 비트들을 프레임으로 그룹화하고, 이를 직렬화 하여 전송하게 된다.  


<br><br><br>

## History
- 230802 : 초안작성
