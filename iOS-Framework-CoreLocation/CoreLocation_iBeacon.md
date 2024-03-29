# Bluetooth, BLE, Beacon, iBeacon

## Bluetooth

단거리에서 무선으로 데이터를 전송하는 기술이다.  

블루투스는 산업, 과학, 의료용으로 할당된 ISM(Industrial Scientific and Medical) 주파수 대역인 2402~2480MHz 범위에 있는 총 79개의 채널을 사용한다.  

ISM은 전 세계가 공통적으로 할당된 주파수이기 때문에 전파 사용에 대한 허가를 받을 필요가 없는 영역대이다.  

이러한 이유로 시스템간의 전파 간섭이 생길 우려가 있어 블루투스는 주파수 호핑 방식을 취하고 있다.  
주파수 호핑이란 많은 수의 채널을 특정 패턴에 따라 빠르게 이동하며 데이터를 조금씩 전송하는 기법이다.  

즉, 블루투스는 할당된 79개 채널을 1초당 1,600번 호핑해 전파 간섭을 최소화하고 있다.  

<br><br>

### 페어링
블루투스 기기를 서로 연결하는 것을 ‘페어링(Pairing)’이라고 한다.  

예를 들어 스마트폰과 무선 이어폰을 연결한다면, 스마트폰이 마스터가 되고 이어폰이 슬레이브가 된다.  

스마트폰은 데이터를 제어하고 이어폰에 전송하며, 이어폰은 스마트폰에서 제어되고 데이터를 수신하여 음악이나 통화를 재생한다.  

<br><br>

### 페어링 과정
1. 블루투스 기능을 지원하는 마스터 기기와 슬레이브 기기를 준비

2. 슬레이브 기기에서 검색가능 상태로 블루투스 활성화

3. 마스터 기기에서 주변의 활성화된 블루투스 기기를 스캔

4. 마스터기기에 스캔된 슬레이브 기기에 페어링 요청을 전송

5. 슬레이브 기기에서 페어링 수락 또는 거절
    - 인증을 위해 암호 입력 요청 가능
    
6. 페어링 요청이 수락되면, 마스터와 슬레이브간의 페어링 완료 (핸드쉐이크)

블루투스 페어링이 완료되면 기기를 사용할 때, 주파수 호핑이 일어나게 된다.  

이 기술은 블루투스 통신에 사용되는 주요 기술 중 하나로, 일정한 주기로 2.4GHz 대역에서 79개의 주파수 채널을 변경하며 통신한다.  

이를 통해 두 장치간의 통신을 안정적으로 유지하고 무선 간섭을 최소화하기 위해 사용된다. 

<br><br>

### 중계기

마스터 기기가 될 노트북과 휴대폰이 블루투스를 지원하지 않을 경우에는 

마스터 기기에 USB로 연결되는 블루투스 동글과 같은 (dongle, 중계기)을 사용할 수 있다.  


<br><br>

## Beacon
비콘은 주변에 있는 장치들에게 신호를 발송하여 블루투스 기술을 이용해 위치 정보를 전송하는 작은 무선 송신 장치이다.  

주로 Bluetooth Low Energy(BLE)를 이용하여 동작하며, 소형화되어 휴대성이 좋다.

비콘은 보통 UUID(Universally Unique Identifier)를 포함한 식별자와 추가적인 정보인 Major 값과 Minor 값으로 구성된다. 비콘은 주변 장치들이 해당 비콘의 신호를 수신하여 식별하고, 이를 통해 위치 정보를 파악할 수 있다.

<br><br>

### 활용 분야

비콘은 주변 장치들이 비콘의 신호를 감지하고 이를 활용하여 다양한 서비스와 상호작용하는 데에 활용될 수 있다.

비콘은 다양한 분야에서 활용될 수 있는데 주로 위치 기반 서비스에서 사용되며, 실내 네비게이션, 광고 및 마케팅, 출결 체크, 자동화 시스템 등에 적용될 수 있다.  

- 마케팅 및 광고
    - 상점 내에서 고객에게 할인 정보를 제공
    - 박물관에서 전시물 설명
- 위치 기반 서비스
    - 실내에서 정확한 위치정보 제공
- 스마트홈(IoT)
    - 가정 내의 다양한 스마트 기기들을 연결하고, 자동화 및 편의성 제공
- 헬스케어
    - 환자 모니터링 등 의료기기에서 활용하여 의료 서비스의 질을 향상

<br><br>

### 비콘기술의 장점
- 정확성 : 정확한 위치를 제공하여, 건물 내부와 같이 GPS신호가 도달하지 않는 환경에서도 동작
- 저전력 : 오랜 배터리 수명을 가지고 있음
- 간편성 : 비콘 설정 및 관리가 용이하다.  
