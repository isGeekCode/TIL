# Git Flow

> 기능별 브랜치 전략

**(예정중)**

## 개요
Git Flow는 Vincent Driessen이 제안한 브랜치 모델로, 기능 개발, 릴리즈, 핫픽스를 체계적으로 관리합니다.

## 브랜치 종류
- **master**: 배포 가능한 상태
- **develop**: 개발 브랜치
- **feature**: 기능 개발
- **release**: 릴리즈 준비
- **hotfix**: 긴급 수정

## 흐름
1. develop에서 feature 브랜치 생성
2. 기능 개발 완료 후 develop에 머지
3. 릴리즈 준비 시 release 브랜치 생성
4. 배포 후 master와 develop에 머지
5. 긴급 수정 시 hotfix 브랜치에서 작업

## 장단점
- 장점: 체계적, 안정적
- 단점: 복잡함, 브랜치가 많음
