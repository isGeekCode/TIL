# 오토레이아웃에 대하여

이번 공부는 정대리님의 오토레이아웃 셀프사이징 유튜브 영상을 토대로 정리했습니다.

출처: https://www.youtube.com/watch?v=RsulV-KCtss

# 오토레이아웃의 개념

레이아웃을 자동으로 계산

1.  뷰의 위치 : 앵커로 제공
    -   가로 → X축
    -   세로 → Y축
2.  뷰의 크기 : 스크린사이즈를 기반으로 뷰의 크기 제공가능
    -   width
    -   height

![오토레이아웃-001 (1) (1)](https://user-images.githubusercontent.com/76529148/168416422-4959426e-d4c1-4eec-835b-29515efcca19.png)

## Constraint

-   First item: X를
-   Second item: Y로

## conflicting Constraint

오토레이아웃시 UI에 서로 충돌하는 Constraint를 넣어줄 경우, 좌우 앵커가 우선이 된다.

-   Constraint를 지워도 되고, 빨간 버튼을 눌러서 충돌하는 값을 선택해도 지워진다.

![스크린샷 2022-05-14 오후 4 39 23](https://user-images.githubusercontent.com/76529148/168416418-b4d8fcaf-c37a-4c79-85dd-e69244fe18b8.png)

## 스토리보드에서 복제하기

필요한 것을 클릭하고 option⌥ 을 누른상태로 드래그 한다.

## 다른 객체와 상대적으로 위치잡기

새로 만든 B를 A의 기준에 맞추려면 B를 클릭하고 ⌃ 을 누르고 A에 드래그 하면 여러가지 선택을 할 수 있다.

-   Top, Bottom, Leading, Trailing : 위아래왼쪽오른쪽 기준에 맞출 수 있음
-   Center Vertically : 세로축의 중앙에 위치
-   Center Horizontally : 가로축의 중앙에 위치
-   Equal Widths, Equal Heights : 가로 / 세로에 맞추기
-   Aspect Ratio : 가로세로 비율값을 지정 가능

![스크린샷 2022-05-14 오후 4 30 13](https://user-images.githubusercontent.com/76529148/168416421-01d70c3b-4ab6-4a11-9d3b-397d838914cd.png)

## View 에 컨텐츠가 길 경우

만약 컨텐츠의 양이 많을 경우에는 레이아웃을 잡을 때

가로 혹은 세로로 길어질 것을 생각하고 만들어야한다.

View자체에 Height를 주지말고 Content의 끝을 superView에 맞춰주면 같이 길어진다.