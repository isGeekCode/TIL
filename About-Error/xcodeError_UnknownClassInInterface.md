# Xcode Error - Unknown class @@ in Interface Builder file.

[Storyboard] Unknown class in Interface Builder file.

퇴근시간 20분전, Xcode로 내일부터 새롭게 작업할 프로젝트를 작성했는데
빌드가 안되는 것은 아니지만 하단에 에러로그가 찍힌다. 굉장히 찝찝하다.

![img1 daumcdn-3](https://user-images.githubusercontent.com/76529148/198202481-ec19044b-8412-45ea-95cd-0c0b399d9943.jpg)

이번 만큼은 에러로그없는 쾌적한 Xcode를 만들기 위해 바로 원인을 찾으려했는데 엄청나게 간단한 문제였다.

```
 Unknown class _ViewController in Interface Builder file
```

이 오류는 Xcode의 버그라고 알려져있기도 했지만 버그가 아니라 리얼 나의 실수일 수도 있다.
Xcode가 워낙 버그가 많다고 하지만 이번엔 진짜 나 때문.

## 문제확인

일단 StoryBoard를 열어보면 내가 지금 사용하는 ViewController의 Identity Inspector에 Custom Class부분을 확인한다.
Class와 Module부분을 보면 여기가 정상인지 확인해본다.

### 확인해야할 것

1. Class가 실제 Class명과 일치하는 지 확인할 것
2. Module을 재선택해볼 것 - 단순히 Module 필드의 오른쪽 화살표를 클릭한 후 모듈을 선택하거나, Module TextBox를 클릭하고 엔터를 치면 해결된다는 의견이 있다
   <img width="257" alt="스크린샷 2022-10-27 오후 2 29 07" src="https://user-images.githubusercontent.com/76529148/198200618-fd319b01-cf46-4611-90a0-ec6088877319.png">

3. Compile Sources에 등록 여부 확인하기 - 프로젝트 설정 / Build Phases / Compile Sources 섹션에 ViewController가 모두 추가되어있는지 확인한다.
   <img width="738" alt="스크린샷 2022-10-27 오후 2 36 10" src="https://user-images.githubusercontent.com/76529148/198200583-4a155c5a-6d87-4578-ab08-ff63cb8c7c01.png">

### 내 경우

- 기본 ViewController로 되어있는걸 MainViewController로 변경하는 과정에서 2번부분에서 에러가 난 것이었다.
  그러니까 난 초보중의 초보라는 것이 판명났단 것이다.

![img1 daumcdn](https://user-images.githubusercontent.com/76529148/198200979-29ca6830-d326-4fe5-aa04-c599d8f49f4d.jpg)

근데 애초에. 스토리보드 안쓸건데 이거 없애면 그만 아닌가?? 해볼까??

++++++

안생긴다.. 아니 애초에 에러가 났던 이유가 Main.Storyboard안에서 충돌난 거였는데 말이지.
Main.Storyboard 없는 프로젝트를 진행하면.. 안생긴다는것을 배웠다.

그말은 애초에 그냥 파일 지우면 해결됐다는 이야기.

![20220319_6235a1a82d792](https://user-images.githubusercontent.com/76529148/198203384-bf62c878-444f-4758-a0aa-2ee1cf4d3c15.jpg)
