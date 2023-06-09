# Git Error - RPC failed; curl 18 transfer closed with...


## 발견
회사 내부 깃을 git clone하던 중,
퍼센트가 안올라가더니 아래와 같이 에러메세지가 생성됐다.
```
error: RPC failed; curl 18 transfer closed with outstanding read data remaining
fetch-pack: unexpected disconnect while reading sideband packet
fatal: protocol error: bad pack header

```

## 원인
규모가 큰 레포지토리를 클론하려고 하는데 로컬에서 네트워크 상황이 좋지 않은 경우, 원격 연결이 끊어지고 클론이 취소가 된다.

## 해결방법
먼저 얕은 클론을 한 후(--depth 1) -> 점진적으로 레포를 가져온다(fetch --unshallow)

```
$ git clone http://github.com/myrepo --depth 1
$ cd myrepo
$ git fetch --unshallow
```
- git clone http://github.com/myrepo --depth 1
    - 지정한 URL의 Git 저장소를 클론한다. --depth 1 옵션은 얕은 클론을 수행하도록 지정하는데, 이는 최신 커밋 하나만을 가져옴으로써 전체 커밋 이력을 다운로드하지 않고 저장소를 더 가볍게 유지하는 역할을 한다. 이 옵션을 사용하면 초기 클론 시간과 저장소의 용량을 줄일 수 있다.

- cd myrepo
    - 클론된 저장소로 이동한다. myrepo는 저장소가 클론된 로컬 디렉토리의 이름을 나타낸다. 해당 디렉토리로 이동하여 이후의 Git 명령을 실행할 수 있다.

- git fetch --unshallow
    - 얕은 클론으로 생성된 저장소에 대해, 저장소의 전체 커밋 이력을 가져오기 위해 언샐로우(unshallow) 작업을 수행한다. 이 명령은 서버로부터 누락된 커밋들을 추가적으로 다운로드하여 저장소를 완전한 형태로 업데이트한다. 이후에는 전체 커밋 이력을 가지고 작업할 수 있다.


## History
- 230609 : 초안작성
