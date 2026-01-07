# Hexagonal Architecture (헥사고날 아키텍처)

> 포트와 어댑터 패턴

**(예정중)**

## 개요
Hexagonal Architecture는 Alistair Cockburn이 제안한 아키텍처로, 애플리케이션을 외부 의존성으로부터 분리합니다.

## 핵심 개념
- **Core** (핵심): 비즈니스 로직
- **Port** (포트): 인터페이스
- **Adapter** (어댑터): 구현체

## 구조
```
[UI Adapter] → [Port] → [Core] ← [Port] ← [DB Adapter]
[API Adapter] → [Port] →         ← [Port] ← [External API Adapter]
```

## 포트 종류
- **Inbound Port** (Primary): 애플리케이션으로 들어오는 요청
- **Outbound Port** (Secondary): 애플리케이션에서 나가는 요청

## 장점
- 테스트 용이 (Mock으로 교체)
- 기술 스택 독립
- 명확한 경계

## 예시
```swift
// Port (인터페이스)
protocol UserRepository {
    func save(user: User)
}

// Adapter (구현체)
class CoreDataUserRepository: UserRepository {
    func save(user: User) { ... }
}

class RealmUserRepository: UserRepository {
    func save(user: User) { ... }
}
```

## 관련 개념
- Clean Architecture
- DDD
