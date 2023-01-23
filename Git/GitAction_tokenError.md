# Git Actions - Permission to ....git denied to github-actions

Git Action을 TIL에서 한번 써보니 ReadMe를 자동업데이트하는것에 맛들려서 응용해보려고 했다.
새로운 workflow를 만들어서 기존 TIL과 똑같은 세팅을 했지만 자꾸 에러가 났다 메세지를 보니 아래와 같았다.

```
remote: Permission to 깃주소.git denied to github-actions[bot].
83
fatal: unable to access '깃주소': The requested URL returned error: 403
```

바로 권한이 없는 것이었다.
이해가 안되는 것이 내 레포지토리에서 내가 세팅한게 왜 허용이 안되는가 했지만 아래 레퍼런스링크에서 방법을 찾았다.

### 해결방법
- 레포지토리 설정 - actions - general 클릭
- Workflow permissions 을 Read and Write로 세팅

<img width="1320" alt="스크린샷 2023-01-23 오후 9 06 00" src="https://user-images.githubusercontent.com/76529148/214035664-65b61651-76e0-412e-b24f-cee3799ef248.png">


### 해당 옵션 설명
이 리포지토리에서 워크플로를 실행할 때 GITHUB_TOKEN에 부여된 기본 권한을 선택합니다. YAML을 사용하여 워크플로에서 더 세분화된 권한을 지정할 수 있습니다.





레퍼런스 
- https://github.blog/changelog/2021-04-20-github-actions-control-permissions-for-github_token/

