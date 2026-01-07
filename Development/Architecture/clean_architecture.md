# Clean Architecture (클린 아키텍처)

> 계층 분리 아키텍처

**(예정중)**

## 개요
Clean Architecture는 Robert C. Martin(Uncle Bob)이 제안한 소프트웨어 아키텍처로, 관심사의 분리를 통해 유지보수성을 높입니다.

## 핵심 원칙
- 프레임워크 독립성
- 테스트 가능성
- UI 독립성
- 데이터베이스 독립성
- 외부 의존성 독립

## 계층 구조 (안쪽 → 바깥쪽)
1. **Entities** (엔티티): 핵심 비즈니스 규칙
2. **Use Cases** (유스케이스): 애플리케이션 비즈니스 규칙
3. **Interface Adapters**: 데이터 변환 (Presenters, Controllers)
4. **Frameworks & Drivers**: UI, DB, 외부 라이브러리

## 의존성 규칙
- 외부에서 내부로만 의존
- 내부는 외부를 몰라야 함

## 장점
- 테스트 용이
- 변경에 유연
- 기술 스택 교체 쉬움

## 단점
- 초기 복잡도 증가
- 보일러플레이트 코드

## 관련 개념
- Hexagonal Architecture
- Onion Architecture
- DDD
