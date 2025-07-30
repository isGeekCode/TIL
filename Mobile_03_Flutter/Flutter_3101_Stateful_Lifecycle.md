# Flutter - StatefulWidget Lifecycle

## 개요

StatefulWidget은 내부 상태(state)에 따라 UI가 동적으로 변경되는 위젯이다.  
해당 위젯은 생성(Creation)부터 파기(Disposal)까지 일정한 생명주기 메서드 호출 흐름을 따르며,  
각 단계는 상태 초기화, 상태 변경 반영, 리소스 정리 등의 목적을 가진다.  
생명주기 흐름을 이해하면 `setState()` 호출 시점, `build()` 반복 호출 조건 등을 명확히 파악할 수 있다.

---
<br>

## 생명주기 주요 메서드 정리

| 메서드 | 설명 | 호출 시점 |
|--------|------|-----------|
| `createState()` | 연결된 `State` 객체 생성 | 위젯 최초 생성 시 |
| `initState()` | 상태 초기화 로직 수행 | 트리에 삽입 직후 1회 |
| `didChangeDependencies()` | 종속성 변경 감지 | `initState()` 직후, 또는 InheritedWidget 변경 시 |
| `build()` | UI 구성 | Dirty 상태 시마다 호출 |
| `setState()` | 상태 변경 트리거 | 호출 즉시 Dirty 마킹 |
| `didUpdateWidget()` | 부모 위젯으로부터 새 위젯 인스턴스 수신 시 | 기존 State 유지 |
| `deactivate()` | 위젯 트리에서 제거 직전 | 재삽입 가능성 있음 |
| `dispose()` | 영구 제거 직전 호출 | 리소스 해제 처리 시점 |

---
<br>

## 🔁 전체 생명주기 흐름 요약

```
createState() → initState() → didChangeDependencies() → build()
(setState() 호출 시 → Dirty → build() → Clean 반복)
위젯 업데이트 시 → didUpdateWidget() → build()
위젯 제거 시 → deactivate() → dispose()
```

---
<br>

## 🖼️ 생명주기 다이어그램

StatefulWidget의 생명주기 흐름과 상태 전이 과정을 시각화한 다이어그램:

![](https://i.imgur.com/AvjtS9c.png)

---
<br>

## 🔍 다이어그램 해설

다이어그램은 생명주기를 3단계로 구분한다:

| 구간 | 설명 | 포함 메서드 |
|------|------|-------------|
| **Creation** | State 객체 생성 및 초기화 단계 | `createState`, `initState`, `didChangeDependencies` |
| **Update Cycle** | 상태 변경에 따른 UI 재빌드 단계 | `setState`, `build`, `didUpdateWidget` |
| **Disposal** | 트리에서 제거되는 정리 단계 | `deactivate`, `dispose` |

- `setState()` 호출 시 Dirty 마킹 → 다음 프레임에서 `build()` 호출 → Clean 상태로 전환
- `didUpdateWidget()`은 부모 위젯에서 새로운 인스턴스를 전달한 경우 호출
- Clean 상태는 추가 렌더링이 필요 없는 상태를 의미

---
<br>

## 🧠 개념 요약

| 개념 | 정의 |
|------|------|
| **Dirty 상태** | 빌드 필요 상태. `setState` 또는 `didUpdateWidget` 호출 후 진입. Dirty로 마킹된 위젯만 선택적으로 다시 빌드됨 |
| **Clean 상태** | UI가 최신 상태로, 추가 작업 불필요 |
| **Mounted** | 위젯이 트리에 등록된 상태 (`mounted == true`) |
| **Disposal 시점** | 리소스 정리를 수행해야 하는 종료 단계 |
