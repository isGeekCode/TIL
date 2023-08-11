# Git - 튜토리얼(4) : commit, push

## commit
스테이지에 있는 변경 사항을 커밋하여 저장소에 영구적으로 저장한다.

<br><br>

```
# 스테이지의 변경 사항을 커밋
git commit -m "커밋 메시지"
```

<br><br><br>

## push
로컬 저장소의 커밋을 원격 저장소로 업로드한다. 

이때 업스트림은 이미 설정되어 있어야 한다. 
```
git push 
```

### 업스트림브랜치를 지정하지않은 상태로 대상 브랜치 지정하여 push
```
git push origin main
```

### 업스트림브랜치를 변경하면서 해당 브랜치로 푸시하기

```
git push --set-upstream origin main

// 이후 아래 코드로 동일하게 동작
git push
```

## 업스트림(upstream)

`업스트림`은 Git에서 현재 브랜치가 어떤 원격 브랜치를 따라가야 하는지를 나타내는 개념이다. 

> git push, git pull, 그리고 git merge와 같은 명령을 실행할 때,  
> 브랜치 간의 관계가 설정된 업스트림을 기반으로 동작한다.

### 업스트림 변경하기

업스트림 변경은 아래와 같이 할 수 있다.

```
git branch --set-upstream-to origin/main
```

하지만 대부분의 경우, 타겟을 정해서 한번에 푸시한다. 
