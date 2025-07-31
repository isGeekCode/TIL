# Flutter - StatefulWidget Life-cycle

## 개요

`StatefulWidget`은 내부 상태(state)의 변화에 따라 UI가 변경되는 위젯이다.  
위젯은 생성부터 제거까지 일련의 생명주기를 따르며,  
각 단계는 상태 초기화, 의존성 반영, UI 재구성, 리소스 해제 등의 목적을 가진다.  
이 흐름을 이해하면 `setState()`의 타이밍이나 `build()`가 언제 다시 호출되는지를 명확히 파악할 수 있다.

<br><br>



## 생명주기 주요 메서드 정리

| 메서드 | 설명 | 호출 시점 |
|--------|------|-----------|
| createState() | 연결된 State 객체 생성 | 위젯 최초 생성 시 |
| initState() | 상태 초기화 로직 수행 | 트리에 삽입 직후 1회 |
| didChangeDependencies() | 종속성 변경 감지 | initState() 직후, 또는 InheritedWidget 변경 시 |
| build() | UI 구성 | Dirty 상태 시마다 호출 |
| setState() | 상태 변경 트리거 | 호출 즉시 Dirty 마킹 |
| didUpdateWidget() | 부모 위젯으로부터 새 위젯 인스턴스 수신 시 | 기존 State 유지 |
| deactivate() | 위젯 트리에서 제거 직전 | 재삽입 가능성 있음 |
| dispose() | 영구 제거 직전 호출 | 리소스 해제 처리 시점 |


<br><br>

---


## 🖼️ 생명주기 다이어그램

StatefulWidget의 생명주기 흐름과 상태 전이 과정을 시각화한 다이어그램

![](https://i.imgur.com/AvjtS9c.png)

<br><br>

---


## 🔍 다이어그램 해설

생명주기는 크게 3단계로 구분된다.

| 구간 | 설명 | 포함 메서드 |
|------|------|-------------|
| **Creation** | State 객체 생성 및 초기화 단계 | `createState`, `initState`, `didChangeDependencies` |
| **Update Cycle** | 상태 변경에 따른 UI 재빌드 단계 | `setState`, `build`, `didUpdateWidget` |
| **Disposal** | 트리에서 제거되는 정리 단계 | `deactivate`, `dispose` |

다이어그램에는 Dirty와 Clean이라는 두 가지 상태가 등장한다.  
이는 Flutter가 해당 위젯을 재빌드할지 판단하는 기준이다.

- Dirty 상태: 다시 build가 호출되어야 하는 상태이다. 예를 들어 `setState()`를 부르면 이 위젯은 Dirty로 표시된다.
- Clean 상태: 화면이 최신 상태여서 다시 그릴 필요가 없는 상태이다.

Flutter는 Dirty 상태인 위젯만 찾아서 다시 build()를 실행한다.  
build가 끝나면 그 위젯은 다시 Clean 상태로 바뀐다.

위젯이 Dirty 상태가 되는 경우는 보통 아래 3가지이다.

1. 위젯이 처음 만들어질 때
2. 사용자가 `setState()`를 호출해 상태가 바뀌었을 때
3. 부모 위젯이 바뀌거나, 부모의 상태가 바뀌어서 자식 위젯도 영향을 받을 때



- `setState()`를 부르면 위젯이 Dirty로 표시되고, 다음 프레임에서 `build()`가 다시 호출된다.
- `didUpdateWidget()`은 부모 위젯이 새로 바뀌었을 때 실행된다.



<br><br>

---


## 개념 요약

| 개념 | 정의 |
|------|------|
| **Dirty 상태** | 빌드 필요 상태. `setState` 또는 `didUpdateWidget` 호출 후 진입. Dirty로 마킹된 위젯만 선택적으로 다시 빌드됨 |
| **Clean 상태** | UI가 최신 상태로, 추가 작업 불필요 |
| **Mounted** | 위젯이 트리에 등록된 상태 (`mounted == true`) |
| **Disposal 시점** | 리소스 정리를 수행해야 하는 종료 단계 |


<br><br>

## History
- 260730: 초안작성
