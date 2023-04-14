
# OSI 7 Layer - 3. Network Layer(네트워크 계층)

여러 대의 컴퓨터가 연결된 네트워크 상에서 다른 네트워크와 데이터를 전송하기 위한 경로를 결정한다. 이를 위해 IP 주소를 할당하고, 라우팅을 수행한다.

2계층 데이터링크 계층에서는 MAC주소를 통해 특정 하드웨어를 찾아가는 데 사용된다면, 3계층 네트워크 계층에서는 IP주소를 사용해 데이터를 목적지까지 전달하도록 한다.


## 📌 IP(Internet Protocol: 인터넷 프로토콜)
각 컴퓨터들은 고유한 주소를 가지고 있다.
그래서 A컴퓨터에서 B컴퓨터로 정보를 보낼 때, 이 고유한 주소를 사용한다.

그런데 우리는 어떻게 각각의 IP를 알아내서 사용할 수 있을까

### URL, Domain 그리고 DNS
URL(Uniform Resource Locator)은 특정 웹페이지나 파일의 위치를 나타내는 주소다.

이 주소는 `도메인 이름`과 `경로` 등으로 구성되어있다.

이 주소를 이용하여 웹페이지를 사용자가 요청하면,

먼저 DNS(Domain Name System)서버에서 해당 이름에 대응되는 IP주소를 찾아내고,

이 IP주소를 이용하여 서버에 접속한다.

따라서 사용자가 입력하는 URL은 최종적으로 IP주소로 전환되어 데이터가 전송된다.

<img width="580" alt="스크린샷 2023-04-14 오후 3 40 51" src="https://user-images.githubusercontent.com/76529148/231970340-02293988-f6f9-477d-9ee8-43820d6de525.png">


## 📌 Packet : 패킷
3계층 네트워크 계층에서는 IP 프로토콜을 이용하여 데이터를 전송한다.

이때 데이터를 패킷이라는 단위로 나누어 목적지까지 전송한다.

각 패킷에는 출발지와 목적지의 IP 주소, 데이터 조각 등의 정보를 포함한다.
(패킷에 대한 좀더 자세한 얘기는 하단에 참고)


## 📌 Routing
네트워크 계층은 상위계층인 전송계층에서 받은 데이털르 패킷으로 분할하고, 목적지 주소를 확인하여 해당 목적지로 전달하는 역할을 한다.

또한 하위계층인 데이터링크 계층에서 전송받은 패킷을 수신하여 데이터를 추출하고, 상위계층인 전송계층으로 전달한다. 


## 📌 세부동작
### 보내는 쪽
- 3계층 Encoding : 데이터를 패킷 단위로 분할.
    - 3계층 Encoder의 Input에 데이터를 넣어준다.
    - 3계층 Encoder의 Output에서 패킷을 내보낸다.
    - 패킷 단위로 전송
- 2계층 Encoding : 패킷을 Framing.
    - 2계층 Encoder의 Input에 패킷을 넣어준다.
    - 2계층 Encoder의 Output에서 데이터(Frame)를 내보낸다.
    - Frame 단위로 전송
- 1계층 Encoding : 데이터(Frame)를 전기 신호로 전환.
    - 1계층 Encoder의 Input에 Frame을 넣어준다.
    - 1계층 Encoder의 Output에서 0과 1의 전기 신호를 내보낸다.
- 전기 신호로 발신

### 중계하는 쪽
- 전기 신호를 수신
- 1계층 Decoding : 전기 신호를 데이터(Frame)로 복원.
    - 1계층 Decoder의 Input에 전기 신호를 넣어준다.
    - 1계층 Decoder의 Output에서 데이터(Frame)를 내보낸다.
    - Frame 단위로 전송
- 2계층 Decoding : 데이터(Frame)을 패킷으로 복원.
    - 2계층 Decoder의 Input에 Framing된 데이터를 넣어준다.
    - 2계층 Decoder의 Output에서 패킷을 내보낸다.
    - 패킷 단위로 전송
    
- 3계층 Decoding
    - 3계층 Decoder의 Input에 패킷을 넣어준다.
    - 3계층 Decoder의 Output에서 원래의 데이터로 복원한다.

- 3계층 Routing : 패킷을 열어서 목적지를 확인하고 다음 목적지로 전송
    - 3계층 Encoder의 Input에 데이터를 넣어준다.
    - 3계층 Encoder의 Output에서 패킷을 내보낸다.
    - 패킷 단위로 전송
    - 목적지에 도착할때까지 라우팅 반복

### 받는 쪽
- 아날로그 신호를 수신
- 1계층 Decoding : 전기 신호를 데이터(Frame)로 복원.
    - 1계층 Decoder의 Input에 전기 신호를 넣어준다.
    - 1계층 Decoder의 Output에서 데이터(Frame)를 내보낸다.
    - Frame 단위로 전송
- 2계층 Decoding : 데이터(Frame)을 패킷으로 복원.
    - 2계층 Decoder의 Input에 Framing된 데이터를 넣어준다.
    - 2계층 Decoder의 Output에서 패킷을 내보낸다.
    - 패킷 단위로 전송
- 3계층 Decoding : 패킷을 데이터로 복원.
    - 3계층 Decoder의 Input에 패킷을 넣어준다.
    - 3계층 Decoder의 Output에서 원래의 데이터로 복원한다.
    - 복원한 데이터를 상위 계층으로 전송한다.
    
<img width="597" alt="스크린샷 2023-04-14 오후 4 37 07" src="https://user-images.githubusercontent.com/76529148/231978120-bf3cb539-235a-46e7-9989-803fa170dcc1.png">


## 📌 정리

수많은 네트워크들의 연결로 이루어지는 inter - network 속에서
- 어딘가에 있는 목적지 컴퓨터로 데이터를 전송하기 위해,
- IP 주소를 이용해서 길을 찾고 (Routing)
- 자신의 다음 라우터에게 데이터를 넘겨주는 기능(Forwarding)


## 📌 패킷에 대해 

IP 패킷은 크게 헤더(Header)와 페이로드(Payload)로 구성된다.
IP 패킷은 3계층에서만 사용되며, 이 패킷은 다음 계층인 4계층 전송 계층으로 전달된다.

IP 패킷은 인터넷 상에서 데이터를 전송하는 데 사용한다.

### Header
IP 주소, 프로토콜 번호, 패킷 길이, TTL(Time to Live) 등의 정보가 포함된다.

TTL은 패킷이 네트워크 상에서 전달되는 동안에 제한된 수의 라우터를 통과할 수 있는 최대 횟수를 의미한다.

### Payload
패킷의 실제 데이터를 나타낸다.

### 패킷으로 정보를 전달하는 인터넷
인터넷은 일종의 패킷 교환망(Packet Switching Network)으로,

데이터를 패킷 단위로 나누어 전송하고,

목적지에서 이를 다시 조합하여 원래의 데이터로 복원한다.

이러한 패킷 교환망은 데이터를 효율적으로 전송할 수 있도록 만든다.



## 📌 p2p에서의 패킷

우리가  P2P 파일 공유, 토렌트를 통하여 전송하는 데이터 패킷도

TCP/IP 프로토콜을 사용하여 전송되며,

이는 3계층에서 사용되는 IP 패킷으로 구성된다.





## 📌 참고링크
- [우아한테크코스 - 히히 : OSI 7 Layer](https://www.youtube.com/watch?v=1pfTxp25MA8)
- [우아한테크코스 모아보기](https://github.com/365kim/techotalk)


## 📌 History
- 230414 : 초안작성
