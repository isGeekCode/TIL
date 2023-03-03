# Git - Fork한 레포지토리 최신화 하기

생활코딩 생활iOS repo를 Fork받아서 PR을 한번 머지했는데
그다음 Fork된 repo에 원본으로부터, 현재까지 업데이트된 내용들을 가져와야하는 경우가 생겼다.

현재 remote된 주소 확인하기

입력
```
git remote -v
```

출력내용
```
origin    https://github.com/isGeekCode/Life-iOS.git (fetch)
origin    https://github.com/isGeekCode/Life-iOS.git (push)
```

## upstream 세팅하기

```
git remote add upstream https://github.com/Swift-Coding-Club/Life-iOS.git
```
 입력후 다시 remote된 주소를 확인하면 아래와 같이 나온다.
 
```
git remote -v

origin    https://github.com/isGeekCode/Life-iOS.git (fetch)
origin    https://github.com/isGeekCode/Life-iOS.git (push)
upstream    https://github.com/Swift-Coding-Club/Life-iOS.git (fetch)
upstream    https://github.com/Swift-Coding-Club/Life-iOS.git (push)
```

## 원본 repo와 동기화 하기
```
git fetch --all
```




## 업스트림 레포 변경하기

가끔 폴더명을 잘못 설정하거나, git 경로를 잘못된 걸 넣을 때가 있다.
나같은 경우는 upstream에 내 포크된 레포를 연동해서 수정할 필요가 있었다.
먼저 upstream을 삭제하고 다시 추가하는 방식인데 git버전에 따라 명령어가 다르다.


```
Older git versions:
git remote rm upstream

newer git versions:
git remote remove upstream
```

다시 upstream 추가
```
git remote add upstream https://github.com/Swift-Coding-Club/Life-iOS.git
```
