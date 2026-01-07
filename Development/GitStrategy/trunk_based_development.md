# Trunk-Based Development

> 메인 브랜치 중심 개발

**(예정중)**

## 개요
Trunk-Based Development는 개발자들이 짧은 주기로 메인 브랜치(trunk)에 직접 커밋하는 전략입니다.

## 핵심 원칙
- 하루에 최소 한 번 메인 브랜치에 머지
- 짧은 수명의 feature 브랜치 (1~2일)
- Feature Flag로 미완성 기능 숨김
- 지속적 통합(CI) 필수

## 장점
- 머지 충돌 최소화
- 빠른 피드백
- 지속적 배포 용이
- 브랜치 관리 부담 감소

## 단점
- Feature Flag 관리 필요
- 높은 테스트 자동화 요구
- 팀 숙련도 필요

## 적합한 환경
- 성숙한 CI/CD 파이프라인
- 자동화된 테스트
- 경험 많은 팀

## 관련 개념
- Feature Flag
- Continuous Integration
- Micro PR
