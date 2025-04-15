# Git 브랜치 전략 3종 요약 (Git Flow / GitHub Flow / GitLab Flow)


## 1️⃣ Git Flow – 안정성과 릴리즈 관리에 강한 전략



![|500](https://i.imgur.com/hb0W5a4.png)  
<sub>사진출처: [유튜브 채널 : Carl McGruder - Development Approaches Git Flow and GitHub Flow](https://www.youtube.com/watch?v=w2r0oLFtXAw)</sub>  


<br><br>

> 릴리즈 주기가 길고, 배포 전 QA나 검증 프로세스가 중요한 팀에서 사용  
> 브랜치 역할이 명확하고, 각 단계별로 책임이 분리됨

  

- **영구 브랜치**: `master`(배포용), `develop`(개발용)
- **일시 브랜치**: `feature/*`(기능 개발), `release/*`(QA), `hotfix/*`(긴급 수정)

  

```

feature/* → develop  

develop → release/*  

release/* → master  

hotfix/* → master & develop

```

  
- `--no-ff` 머지로 병합 커밋 기록 보존

- 복잡하지만 품질 보장이 중요한 서비스에 적합 (예: 금융, 공공기관)

  
<br><br>

---
  

## 2️⃣ GitHub Flow – 빠른 배포에 유리한 전략

  
![|500](https://i.imgur.com/lyd5CCJ.png)  
<sub>사진출처: [유튜브 채널 : Carl McGruder - Development Approaches Git Flow and GitHub Flow](https://www.youtube.com/watch?v=w2r0oLFtXAw)</sub>    

<br><br>

> 소규모 팀이나 스타트업에서, 빠르게 개발하고 바로 배포하는 환경에 적합  

> 브랜치 구조가 단순하고, CI/CD 연동이 전제됨

  

- **사용 브랜치**: `main` + `feature-*`

- 모든 작업은 `main`에서 분기 → `PR` 머지 후 자동 배포

  

```
feature-* → PR → main (merge & 배포)
```

  

- 브랜치 이름은 `feat/`, `fix/`, `chore/` 등 명확하게 작성
- 테스트는 PR 단계에서 수행 → 코드 리뷰, CI가 핵심

  

<br><br>

  

---

  

## 3️⃣ GitLab Flow – Git Flow와 GitHub Flow의 절충안

![|500](https://i.imgur.com/ip0X08w.png)  
<sub>사진출처: [유튜브 채널 : Carl McGruder - Development Approaches Git Flow and GitHub Flow](https://www.youtube.com/watch?v=w2r0oLFtXAw)</sub>  

<br><br>

> 빠른 배포는 필요하지만, pre-release 테스트도 중요한 경우에 적합  
> `pre-production`이라는 중간 브랜치를 둬서 QA 테스트를 별도로 수행



구성 브랜치
- `feature/*` → 개발 브랜치  
- `master` → 통합 브랜치  
- `pre-production` → QA 검증 브랜치  
- `production` → 실 배포

  
```

feature/* → master  

master → pre-production  

pre-production → production

```

  

- 릴리즈 흐름은 GitHub Flow처럼 빠르지만, 테스트 안정성을 보강
- 실무에서 가장 현실적인 브랜치 전략으로 많이 쓰임



<br><br>


---

  

## 🧠 전략 선택 요약

| 상황 | 추천 전략 | 주요 브랜치 |
|------|-----------|---|
| 빠른 기능 배포 / 자동화 중심 팀 | GitHub Flow | main, feature/ |
| 안정성, QA 중시 서비스 | Git Flow | master, develop, feature/  , release/ , hotfix/ |
| 빠른 반복 + 테스트 분리 필요 | GitLab Flow | master, pre-production, production, feature/ |

  
---



## ✍️ 실전 팁

- 전략을 정했더라도 팀 내 **명확한 브랜치 명명 규칙**과 **머지 전략**이 없으면 흐트러짐  
- `release`, `hotfix`를 도입하려면 **릴리즈 노트 작성 or 버전 태깅 체계**도 함께 필요  
- GitLab Flow는 **CI/CD 파이프라인 자동화**와 함께 사용하면 효율이 극대화됨
