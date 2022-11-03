# 앱 빌드설정 선택하기

앱을 운영버전과 개발버전 혹은 QA버전으로 나누어 빌드하는 경우가 있다. 이를 위해 타겟을 여러개 두는 경우가 있지만, 운영과 개발만 사용하는 경우 간단하게 Edit Scheme를 통해 설정할 수 가 있다.

Xcode의 중앙 상단 에 앱의 아이콘부분 - Edit Schem 를 누른다.

<img width="173" alt="스크린샷 2022-11-03 오후 2 20 02" src="https://user-images.githubusercontent.com/76529148/199670178-80d05aec-ac9b-4fed-b1d7-291db17c89da.png">

그러면 각 동작별로 Release, Debug 모드를 사용할 것인지 선택할 수 있다.

만약 테스트플라잇에 디버그용으로 올릴용도라면 Archive에서 수정을 해야한다.

<aside>
‼️ 깃을  되돌리더라도 xcode 자체가 복구되진 않아서 Archive를 수정한게 변경되지않을 수 있으니 반드시 아카이빙 완료후 원복하는 습관을 갖도록 하자.

</aside>

<img width="194" alt="스크린샷 2022-11-03 오후 2 19 15" src="https://user-images.githubusercontent.com/76529148/199670168-3cb66ba5-b0da-48a1-b540-7abe3695d49d.png">

각 동작을 누르면 해당 동작의 빌드 설정을 선택가능하다.

<img width="564" alt="스크린샷 2022-11-03 오후 2 25 19" src="https://user-images.githubusercontent.com/76529148/199670192-7132aa91-bddb-4fbd-a09d-34dbb61c841e.png">
