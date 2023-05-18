# Integrity - Secure Enclave

Secure Enclave는 Apple SoC(System on Chip)에 통합된 전용 보안 하위 시스템이다.
즉, 암호화 기능만을 수행하는 iOS(OS)에 완전히 독립된 하드웨어다.

메인 프로세서와 격리되어 추가적인 보안 계층을 제공하며, 응용 프로그램 프로세서 커널이 손상된 경우에도 민감한 사용자 데이터를 안전하게 보관하도록 설계되었다. 

이는 하드웨어 신뢰 루트를 확립하기 위한 Boot ROM, 효율적이고 안전한 암호화 작업을 위한 AES 엔진 및 보호된 메모리 등 SoC와 동일한 설계 원리를 따른다. 

Secure Enclave는 저장 장치를 포함하지 않지만 응용 프로그램 프로세서 및 운영 체제에서 사용하는 NAND 플래시 저장 장치와는 별도로 연결된 저장 장치에 정보를 안전하게 저장하는 메커니즘을 가지고 있다.

![9b2f5a428b7beec9647d6a75130b58be](https://github.com/isGeekCode/TIL/assets/76529148/c00f56d3-8737-4348-839f-ea227bb3a599)

## Secure Enclave 프로세서
Secure Enclave 프로세서는 Secure Enclave에 주요 컴퓨팅 성능을 제공한다. 가장 강력한 분리를 제공하고자 Secure Enclave 전용으로만 사용된다. 이를 통해 공격 대상 소프트웨어와 동일한 실행 코어를 공유하는 악성 소프트웨어에 의존하는 사이드 채널 공격을 방지할 수 있다.

Secure Enclave 프로세서는 L4 마이크로커널의 Apple 맞춤형 버전을 실행한다. 또한 느린 클럭 속도에서 효율적으로 작동하도록 설계되어 클럭 및 전력 공격으로부터 보호하는 데 도움이 된다. A11 및 S4부터 Secure Enclave 프로세서는 재전송 방지 기능, 보안 시동, 전용 난수 발생기 및 자체 AES 엔진을 갖춘 메모리 보호 엔진 및 암호화된 메모리를 포함한다.

## 레퍼런스
- [애플 가이드](https://support.apple.com/ko-kr/guide/security/sec59b0b31ff/web)
- [CryptoKit 및 Secure Enclave](https://www.andyibanez.com/posts/cryptokit-secure-enclave/)
- [주말동안 알아본 Secure Enclave](https://rhammer.tistory.com/392/)

## History 
- 230518 : 레퍼런스링크
