# 오토레이아웃의 개념

레이아웃을 자동으로 계산


## Anchor
View를 액자라고 생각하고 전체 화면을 벽이라고 생각하자.

<img width="132" alt="스크린샷 2022-11-07 오전 11 14 25" src="https://user-images.githubusercontent.com/76529148/200213282-481e1bd7-5c5e-4ce9-a4be-b72199f47880.png">


액자는 걸지않으면 아래로 떨어지기때문에 Anchor(앙카)를 달아주어야한다. 자리를 잡으면 파란색 잡지못하면 빨간색으로 표시된다.

오토레이아웃의 성립조건

1. 너비와 높이 지정 : 스크린사이즈를 기반으로 뷰의 크기 설정
    - width
    - height
2. 위치 지정 : 앵커로 설정
    - 가로 → X축
    - 세로 → Y축

뷰를 기준으로 앵커를 양옆에 달아주면 Xcode자체에서는 기기의 화면을 알고있기 때문에 자동으로 크기를 잡아줄 수가 있다.

## Constraint

- First item: X를
- Second item: Y로부터
- Constraint 만큼

오토레이아웃을 잡을 뷰의 이름이 헷갈린다면 이름을 수정해서 확인해볼 수 있다.

First item: MainView.Leading

Second item: Safe Area Leading

Constraint : 100

이부분을 해석하면 아래와 같다

`MainView`의 Leading을 

`Safe Area Leading`으로부터 100 만큼 떨어지게 둔다.

## Align

앵커는 Top, Bottom, Leading, Ttrailing이 존재한다. 그외에도 

선택한 요소들을 특정 기준에 맞게 정렬하는 방법도 있다.

각 앵커의 TBLT에 맞게 맞출 수도 있고, Horizontal, Vertical의 중아에 맞게 설정또한 가능하다.