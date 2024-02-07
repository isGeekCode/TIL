# Git - 튜토리얼(3) : status, add, restore, reset

## status
현재 브랜치, 작업 디렉토리의 변경 사항, 스테이지에 있는 변경 사항 등을 보여준다.

<br><br>

### 사용법
```
git status
```

<br><br>

### 응답내용 읽는 방법

```
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   파일명
        new file:   새로운_파일명

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   파일명
```

여기서 Changes to be committed 섹션에 있는 정보가 스테이지에 있는 변경 사항입니다. "modified"라고 표시된 부분은 스테이지에 추가된 파일 중에서 변경된 파일을 나타내며, "new file"라고 표시된 부분은 스테이지에 추가된 새로운 파일을 나타냅니다.

스테이지에 있는 변경 사항을 git status 명령으로 확인할 때에는 "Changes to be committed" 섹션을 주목하면 됩니다.

<br><br><br>

## add
변경 사항을 스테이지에 추가한다.

<br><br>

```
# 모든 변경 사항을 스테이지에 추가
git add .

# 특정 파일을 스테이지에 추가
git add 파일명
```

<br><br><br>

## restore
작업 트리 또는 스테이지의 변경 사항을 취소하고 이전 상태로 복원한다.

git status를 사용하면 나오는 안내 메세지에도 이 명령어를 통해 unstage 하라는 내용이 나온다. 

```
# 작업 트리에서 변경 사항을 취소하고 최근 커밋 내용으로 복원
git restore 파일명

# 스테이지에서 변경 사항을 취소하고 작업 트리로 복원
git restore --staged 파일명
```

<br><br><br>

## reset
여러가지로 사용할 수 있다. 
커밋 기록을 변경하거나, 스테이지에서 변경 사항을 취소하거나, 작업 트리와 스테이지를 특정 커밋 상태로 이동시킨다.

단, reset은 커밋이 한 번이라도 되어서 HEAD 포인터를 가지고 있는 경우에 사용이 가능하다.  

```
# 스테이지에 있는 변경 사항을 작업 트리로 이동
git reset 파일명

# 모든 스테이지의 변경 사항을 작업 트리로 이동
git reset

# 특정 커밋으로 이동하고 해당 커밋 이후의 커밋 기록은 삭제
git reset 커밋_해시

# 특정 커밋으로 이동하고 해당 커밋 이후의 커밋 기록은 보존
git reset 커밋_해시 --soft
```


- 도움이 되는 링크
    - [wishlan 블로그](https://wishlan.tistory.com/entry/Git17-%EC%8A%A4%ED%85%8C%EC%9D%B4%EC%A7%80%EC%97%90-%EB%93%B1%EB%A1%9D%ED%95%9C%EC%98%AC%EB%A6%B0-%ED%8C%8C%EC%9D%BC%EC%9D%84-%EC%B7%A8%EC%86%8C%EC%82%AD%EC%A0%9C%ED%95%98%EA%B8%B0%EB%82%B4%EB%A6%AC%EA%B8%B0)
