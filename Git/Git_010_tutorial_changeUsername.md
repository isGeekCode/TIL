# Git - 푸시한 커밋의 Author 변경하기(username과 user email 수정하기)

## 현재 Author 확인하기
```
git config --list
```
username과 user email을 수정한다.

```
git config user.name "유저이름"
git config user.email "유저이메일"
```
이 config의 author를 바꾸지 않으면 이후의 rebase 작업시 author와 commit 계정이 달라지게 된다.

## push된  Author 변경하기
바꾸려는 커밋보다 이전의 해시값을 확인하고 입력한다.

```
git rebase -i -p 해시값
```
-i 옵션은 인터랙티브 모드를 활성화하는 옵션이다. 명령을 실행하면 Git은 현재 브랜치의 최신 커밋부터 HEAD까지의 모든 커밋을 순서대로 나열하고, 이 중에서 리베이스할 커밋을 선택할 수 있는 인터랙티브한 화면을 제공한다.

-p 옵션은 리베이스 작업에서 커밋 패치를 생성하는 옵션이다. 이 옵션을 사용하면 리베이스할 커밋에서 변경된 내용만 추출하여 패치를 생성할 수 있다. 이 패치를 다른 브랜치에 적용하여, 해당 브랜치에도 변경 내용을 적용할 수 있다.

## 원하는 커밋 선택하기
이전 동작을 실행하면 커밋리스트가 나타나는데,

여기서 pick으로 된 부분에서 수정을 원하는 커밋의 pick부분을 e 로 수정한다.

### 수정하는 방법
- i를 누르면 insert모드로 변경된다.
- 방향키로 이동하여 pick를 지우고 e로 변경한다.
- 수정완료하면 esc를 누르고 :wq를 입력하여 나온다.

## 변경할 Author 정보 입력하기
방금 e로 수정한 커밋부터 순차로 수정하기 시작한다.
원하는 user name과 user email을 여기에서 입력한다.

- 이메일에는 <>를 포함하자
```
git commit --amend --author "유저이름 <유저이메일>"
```

여기까지 하면 방금 커밋읆 수정처리하였다.
여기서 아래 명령어로 커밋으로 넘어간다.
```
git rebase --continue
```
그러면 변경된 내역이 보여진다. `:wq`를 눌러 나온다.

만약 변경내역을 보지않으려면 위 명령어를 아래처럼 입력한다.
```
git rebase --continue --no-edit
```
성공하면 `Successfully rebased and updated 브랜치경로 ` 메세지가 나온다.

## 변경된 내역 push하기
origin에 있는 특정 브랜치에 push한다.
이때 `+`는 강제로 작업하기 위함이다.

```
// 예시
git push origin +develop
git push origin +master

git push origin +브랜치명
```

깃에 들어가서 정상적으로 반영 됐는지 확인한다.




### Comment
origin에 push 를 안하면 되기때문에 겁내지말자.
만약 잘못되면.. 롤백....롤백..

rebase 생각은 익숙치 않은데 몇번 더 해보면 자신감 생길듯하다.


### History
- 230417 : 작성
