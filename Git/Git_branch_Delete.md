# Git - 브랜치 삭제하기

작업이 길어지고 이제 더이상 브랜치를 사용하지 않을 수 있다.
또한 너무 Feature용 브랜치가 많아져서 관리를 위해 삭제해야하는 경우도 있다.

그럴땐 아래 커맨드를 입력하자

```
// local
git branch -d <브랜치 이름>

// origin
git push origin --delete <브랜치 이름>
```

만약 feature 폴더에 속해 있다면 그대로 입력하자

```
// local
git branch -d feature/<브랜치 이름>

// origin
git push origin --delete feature/<브랜치 이름>
```

삭제를 마치고 브랜치 목록을 확인해보자

```
git branch -r
```


## History
- 230710 : 초안작성
