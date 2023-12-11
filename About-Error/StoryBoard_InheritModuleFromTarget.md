# [StoryBoard] - Unknown class ViewControllerC in Interface Builder file

스토리보드를 구현하는 경우가 있다.  

빌드를 하고, 스토리보드로 구현한 페이지를 진입하는데 아래와 같은 메세지가 콘솔창에 나오는 경우가 있다.

```
"Unknown class ViewControllerC in Interface Builder file"
```

Unknown class??? 쎄하다...  
 
이런 경우, 구현한 버튼 Action 같은 걸 누르면 십중팔구 앱이 죽을 수가 있다.  

일단 이 메세지의 의미는  `스토리보드에서 ViewControllerC 클래스를 찾을 수 없다는 것`을 나타낸다.  


원인으로 들 수 있는 것은 아래 두가지가 있다.

- 1번 : 클래스 이름 오타
- 2번 : `Inherit Module From Target`옵션 체크를 안한 경우


1번과 2번을 설정하는 곳은 동일한 위치에 있다.  

<img width="500" alt="스크린샷 2023-09-21 오후 4 02 22" src="https://github.com/isGeekCode/TIL/assets/76529148/4878e53e-4875-4643-b76e-11664623f1f7">
  
<br><br>

## History
- 230921: 초안
