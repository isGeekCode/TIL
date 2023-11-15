# Xcode 주석사용법

과거 Obejctive - C로 앱을 만들 때에는 `#pragma mark -` 라는 주석을 사용했어요.

그게 Swift로 바뀌면서 이제는 MARK 라는 주석으로 바뀌었습니다.

이를 포함해 Swift에서 사용하는 주석은 아래와 같습니다

```jsx
// MARK :  설명
// TODO :  할일
// FIXME : 고쳐야 할 부분
// !!! : rudrh
// ??? : 의문점
```

## 메서드 리스트

Xcode에서 상단에 있는 메서드리스트를 클릭해보면 주석처리한 부분과 메서드를 구분해 놓은것을 볼 수 있어요.

아울러 아이콘 모양도 살짝 달라요.

- MARK: 설명모양의 아이콘이 표시돼요
- TODO : 투두리스트 모양의 아이콘
- FIXME: 반창고 모양의 아이콘
- Ex : Extension
- M : Method
- P : Property

### 구분선

구분선을 만들기위해서는 기존의 pragma mark 뒤에 -를 붙이면돼요

그러면 메서드리스트에서 구분선이 등장하고, 코드라인에서도 구분선이 등장합니다~ 미니맵에서도 등장해요

![img1 daumcdn-2](https://user-images.githubusercontent.com/76529148/170830615-49418ba0-82b6-43d2-be5b-166b4ae425f4.png)

이상 오늘은 여러가지 주석에 대해 알아봤습니다.
