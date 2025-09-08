# 개념 - 페이로드(Payload)

페이로드(payload)는 전송되는 데이터를 의미한다.

데이터를 전송할 때, Header와 메타데이터, 에러 체크 비트 등과 같은 다양한 요소들을 함께 보냄으로서, 데이터 전송의 효율과 안정성을 높히게 된다.

이 때, 보내고자 하는 데이터 자체를 의미하는 것이 바로 페이로드다.

우리가 택배 배송을 보내고 받을 때,  
택배 물건이 페이로드이고, 송장이나 박스, 뾱뾱이와 같은 완충재 등등은 부가적인 것이기 때문에 페이로드가 아니다.

wiki에 정의되어있는 페이로드를 보면,  
> 페이로드(payload)라는 단어는 운송업에서 비롯하였는데,
> 지급(pay)해야 하는 적화물(load)을 의미합니다.
> 예를 들어, 유조선 트럭이 20톤의 기름을 운반한다면 트럭의 총 무게는 차체, 운전자 등의 무게 때문에 그것보다 더 될 것이다.
> 이 모든 무게를 운송하는데 비용이 들지만, 고객은 오직 기름의 무게만을 지급(pay)하게 된다. 그래서 ‘pay-load’란 말이 나온 것이다.


## 페이로드의 예
  
상황에 따라 페이로드는 다양한 형식과 전달 방식으로 사용될 수 있으며, 예시에서 보여드린 것처럼 데이터를 포함하는 다양한 형식의 텍스트나 구조화된 데이터 형식이 될 수 있다.

  
### 1. 웹 요청의 페이로드 (POST 요청)
```
POST /api/user HTTP/1.1
Host: example.com
Content-Type: application/json

{
  "name": "John Doe",
  "age": 30,
  "email": "john.doe@example.com"
}
```
위의 예시에서는 웹 요청이 이루어질 때 JSON 형식의 페이로드가 HTTP POST 요청의 본문에 포함된다. 클라이언트는 서버로 데이터를 전송하기 위해 POST 요청을 보내고, 해당 페이로드에 사용자 이름, 나이, 이메일과 같은 정보를 포함시킨다.

  
### 2. API 요청의 페이로드 (POST 요청)
```
POST /api/login HTTP/1.1
Host: api.example.com
Content-Type: application/x-www-form-urlencoded

username=johndoe&password=secret
```
위의 예시에서는 API 요청을 할 때 폼 데이터를 페이로드로 전송하는 방식이다. username과 password는 키와 값의 쌍으로 이루어진 폼 데이터이며, application/x-www-form-urlencoded 형식으로 인코딩되어 POST 요청의 본문에 포함된다.

  
### 3. 메시지 전송의 페이로드 (이메일)
```
Subject: Hello
From: sender@example.com
To: recipient@example.com

Hi there,

How are you doing?

Regards,
Sender
```
  
위의 예시는 이메일의 페이로드로 사용되는 내용이다. 페이로드는 이메일의 본문 내용이며, 메일의 제목, 발신자, 수신자, 본문 내용 등을 포함한다. 메시지의 내용 자체가 페이로드로 사용된다.

  
### 4. 파일 전송의 페이로드 (FTP)

FTP (파일 전송 프로토콜)를 사용하여 파일을 전송하는 경우, 페이로드는 실제 파일의 내용을 나타낸다. 파일 자체가 페이로드로 사용되며, 해당 파일 데이터를 서버로 전송하여 수신자가 파일을 받아 저장하거나 처리할 수 있다.


## History
- 230519 : 초안작성
