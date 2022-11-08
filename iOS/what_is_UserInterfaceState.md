UserInterfaceState.xcuserState가 자꾸 뜰 때

Xcode작업을 하고 깃에 업로드를 하다보면 UserInterfaceState.xcuserstate 이 파일이 계속 보일 때가 있다.

그리고 프로젝트 파일을 그냥 훑어보기만해도 깃 백스테이지에 변화가 생겼다고 보이는게 여간 성가신게 아니다.

이 파일은 로컬중심으로 데이터가 생성되고 재구성하면서 파일이 생성된다.

혼자 할때는 계속 깃에 동기화를 해도 문제가 전혀없지만, 협업중에는 이걸 올리고 서로 머지를 하다가는 Conflict가 너무 자주 생겨버버려서 홧병으로 쓰러질 수가 있다.

이를 해결하기 위한 첫번째 방법은 .gitIgnore를 사용하는 것이다.

### 방법1: gitIgnore사용하기

ignore파일의 하단에 `*.xcuserstate`를 추가한다.

링크: [https://h1guitar.tistory.com/281](https://h1guitar.tistory.com/281)

그럼에도 해결이 안되면 직접적으로 깃 명령어로 추적 제외 처리한다.

### 방법2: **Git에서 Tracking 제외처리**

자세한 경로는 아래와 같다. 뭔가 길지만 단순히 경로를 입력한 것이다.

`// git rm --cached [Project Name].xcworkspace/xcuserdata/[User Name].xcuserdatad/UserInterfaceState.xcuserstate`

```bash
git rm --cache */UserInterfaceState.xcuserstate
git commit -m "Removed file that shouldn't be tracked"
```

이렇게 하면 더이상 git status에서 해당 파일을 추적하지 않는다.

소스트리 프로그램에서도 더이상 추적하지않는다.
