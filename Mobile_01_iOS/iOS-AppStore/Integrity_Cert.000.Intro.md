# Integrity Cert Series - Intro

## 개요
이 시리즈는 iOS 개발 과정에서 필수적인 인증서/키/프로비저닝 프로파일 관리 개념을 정리한다.  
CSR, CER, Provisioning Profile, Xcode Managed Signing, p8/p12 Key 파일 등 전반적인 흐름을 다룬다.

---

## 학습 흐름도
키(Key) → CSR → CER → Provisioning Profile → 빌드 & 서명(Signing)

---

## 문서 구성
- **100_CSR-CER**: CSR 생성과 CER 발급 기본
- **200_Dev-vs-Dist**: 개발용 vs 배포용 인증서
- **300_Keys-p8-p12**: Key 파일 종류 및 Apple Portal 변화
- **400_Provisioning-Profile**: 수동 관리와 프로비저닝 프로파일
- **500_Xcode-Managed**: Xcode 자동 서명과 xc 리소스
- **600_Keychain-Mapping**: 개인키/공개키와 Keychain 매핑 구조
- **700_Team-Sharing**: 팀 협업 시 인증서 전달 및 개인키 불필요 이유
- **800_Checklist**: 온보딩, 만료 알림, 배포 전 점검
- **899_Glossary-FAQ**: 용어 정리와 자주 묻는 질문

---

## 참고
- 기존 문서: `Integrity_Certificate.md`, `Integrity_Certificate_Provisioning.md`
- 관련 Apple 문서: Certificates, Identifiers & Profiles 가이드
