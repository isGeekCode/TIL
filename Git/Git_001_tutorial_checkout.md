# Git - 튜토리얼(1) : 브랜치 생성하기. 리스트 확인, 브랜치 체크아웃

소스트리도 자주 사용하지만.. 에러가 너무 많다..... 킹받아서 정리..

## 브랜치 생성하면서 체크아웃하기

```
// 브랜치 체크아웃
git checkout new-branch
// 브랜치 생성하며 체크아웃하기
git checkout -b new-branch
```

## 브랜치 생성하기
git branch 명령어로 생성 및 리스트 확인이 가능하다.
```
// new-branch 이름의 브랜치 생성하기
git branch new-branch
```

## 브랜치 리스트 확인하기
```
// 현재 저장소에서 사용 가능한 모든 로컬 브랜치 목록보기
git branch

// 로컬 저장소와 연결된 모든 브랜치
git branch -a

// 로컬 저장소와 연결된 원격 저장소의 브랜치 목록
git branch -r
```

- History
    - 230413 : 초안 작성
