# Integrity - 리플레이 공격(Replay attack)

프로토콜 상 메시지를 복사한 후 재전송함으로써 승인된 사용자로 오인하게 만들어 공격하는 방법

이용자가 제대로 맞는지를 확인하는 과정에서 서버 시스템은 이용자 사이에 전자서명과 같은 암호화한 데이터를 주고받는다.

그 도중에 제3자의 해커가 네트워크상에 왕래하고 있는 데이터를 복사해뒀다가 나중에 이를 그대로 서버에 전송해서 합법적 이용자를 가장하려는 시도를 말한다.

웹 서비스, 인증 부분, 접근 부분, 패킷 정보 재사용 부분 등에서 사용 가능하다.

* 블록체인에서 리플레이 공격이란?

 기존 코인과 하드포크로 인해 나오는 새로운 코인이 동일 인증키를 사용하기 때문에 한쪽 코인의 출금정보를 가지고 다른 쪽 코인 출금을 시도하는 행위입니다. 즉 개인 지갑에 저장된 암호화폐가 중복 출금되는 현상

>> 리플레이 방지 코드를 삽입하여 방지할 수 있음


### 공격 시나리오
1. A가 B에게 보내는 송금의뢰 메시지와 메시지 인증 코드를 H가 가로챔
H는 메시지와 메시지 인증코드를 그대로 다시 전송함으로써 A가 아님에도 송금요청을 할 수 있음

2. 공격자는 게시판에서 내용 입력 부분, 혹은 답변 부분의 XSS 취약점을 이용해 악의적인 스크립트 삽입
사용자들이 해당 게시물 접근시 자신도 모르게 인증 세션 정보를 공격자 서버에 전달
공격자는 해당 세션 정보를 자신의 세션 정보와 교체하면 획득한 사용자의 인증으로 서비스 이용 가능

### 대응 방안
1. 순서 번호(sequence number)
송신 메시지에 매회 1씩 증가하는 번호를 함께 전달

2. 타임스탬프(timestamp) 사용
송신 메시지에 현재 시각을 함께 전달

3. 비표(nonce) 사용
메시지를 수신하기에 앞서 수신자는 송신자에게 일회용의 랜덤한 값(nonce) 전달

4. 세션에 대한 만기 최소화 및 사용자 브라우저 종료시 바로 세션 파기

5. 세션내에 IP정보를 포함해 암호화



### 레퍼런스
- [리플레이 공격(Replay Attack)](https://blog.naver.com/kss9409/221593379033)

### History
- 230518 초안작성
