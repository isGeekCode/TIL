푸시 에러 : 원격 저장소와 커밋 기록이 다른 경우

Git은 원격 저장소를 가지고 있어 각각 다른 장소에서도 접근이 가능하다.
하지만 각각 다른 장소에서 해당 작업을 이어가기 위해서는 각 장소의 로컬 저장소도 동기화를 시켜주어야한다.
만약 동기화가 잘 이루어지지않는경우, 특히 A장소에서 원격저장소에 푸시를 하고 B장소에서 동기화를 완료하지 않고 새로운 푸시를 하게 되면 에러가 발생한다. 

아래는 이 에러를 해결하기 위한 몇가지 방법이다.

에러 메세지
```
$ git push


To https://github.com/isGeekCode/TIL.git
 ! [rejected]        main -> main (non-fast-forward)
error: failed to push some refs to 'https://github.com/isGeekCode/TIL.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```


방법 1. 
커밋수 자체가 많지않을 경우에 가장 빠르게 해결이 가능한 방법이다.
푸시를 했을 때, 아래와 같은 화면이 나오면 별다른 작업을 하지않는 이상 빠르게 끝낼 수 있다.

<img width="570" alt="스크린샷 2023-03-06 오전 9 17 54" src="https://user-images.githubusercontent.com/76529148/222997295-217da12c-93d6-45e9-b0f9-0ad1e02f22b3.png">

이 화면이 나온다면 그대로 아래 순서로 입력한다.
- 키보드 ESC
- :wq
- 키보드 엔터
- 화면을 나오면 그대로 `git pull`입력
- 정상적으로 git pull 처리후 그대로 git push

방법 2. 병합을 중단처리하고 이어가기
커밋도 많고 방법1에서 나온화면에서 정상적이지 않은 방법으로 처리가 안됐다면 이방법을 써야한다. 
- 소스트리를 이용한다면 HEAD를 날리면된다.
- 터미널을 이용한다면 아래 명령어를 입력한다.
```
git merge --abort
```
위 명령어를 실행하면 현재의 병합 작업을 중단하고 MERGE_HEAD 파일을 삭제할 수 있다. 그러면 다음에 병합 작업을 다시 시작할 수 있다.
- 그 다음 다시 `git push`처리하면 정상 작동한다. 

## 기억하기
무엇보다 작업공간이 여러 곳이거나 Git Action 등으로 로컬 정보가 원격 정보가 다른 경우가 있다면 항상 git pull을 습관화 하는 것이 좋다. 
