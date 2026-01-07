# Feature Flag (Feature Toggle)

> 기능을 코드로 켜고 끄기

**(예정중)**

## 개요
Feature Flag는 배포된 코드의 기능을 런타임에 켜거나 끌 수 있는 기술입니다.

## 사용 목적
- 미완성 기능을 배포하되 숨김
- A/B 테스트
- 점진적 롤아웃 (Canary Release)
- 긴급 기능 비활성화

## 구현 방법
```swift
if FeatureFlag.isEnabled(.newLoginUI) {
    // 새로운 로그인 UI
} else {
    // 기존 로그인 UI
}
```

## 종류
- **Release Toggles**: 미완성 기능 숨김
- **Experiment Toggles**: A/B 테스트
- **Ops Toggles**: 운영 제어
- **Permission Toggles**: 권한 제어

## 주의사항
- Flag가 쌓이면 복잡도 증가
- 정기적으로 제거 필요
- Flag 관리 도구 사용 권장

## 도구
- LaunchDarkly
- Firebase Remote Config
- Unleash
