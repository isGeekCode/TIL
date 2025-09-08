# 단방향 데이터 플로우(Unidirectial Data Flow, UDF)

> **Redux 스타일?**
> 
> **Redux 스타일**이란 **단방향 데이터 흐름(Unidirectional Data Flow, UDF)**을 기반으로 한 상태 관리 패턴이다.
> - 애플리케이션의 상태(State)를 **중앙에서 관리(Store)**
> - 상태 변경은 **액션(Action) → 리듀서(Reducer) → 새로운 상태(State) 생성**의 흐름을 따른다. 
> - Redux 스타일은 **불변성(Immutable State)과 순수 함수(Pure Function)를 기반으로 상태를 관리하는 방식**을 의미한다.



### 전신

Redux 스타일은 **Facebook이 먼저 만든 “Flux” 패턴에서 영향을 받음**.

  

✔ **Flux (2014, Facebook)**

• Facebook에서 **MVC의 문제를 해결하기 위해 만든 단방향 데이터 흐름 패턴**

• Action → Dispatcher → Store → View 형태로 데이터가 한 방향으로 흐름


🔽

✔ **Redux (2015, Dan Abramov)**

• Flux를 더 단순하게 만든 버전 (Dispatcher 제거)

• Action → Reducer → Store → View 형태로 **완전한 단방향 데이터 흐름을 정립**

• 상태(State)가 불변(Immutable)하도록 강제 → **시간 여행 디버깅(Time Travel Debugging) 가능**

• Redux가 React.js와 함께 대중화되면서, **단방향 데이터 흐름이 “Redux 스타일”이라고 불리기 시작**



## 1️⃣ MVC의 한계 → 단방향 데이터 흐름 필요성 대두


과거에는 대부분의 UI 개발에서 **MVC (Model-View-Controller)** 패턴을 사용했지만,

이 방식은 **앱의 규모가 커질수록 상태(State) 관리가 어려워지는 문제점**이 있었다.

  
✔ **문제점 (MVC, MVVM의 한계)**

• 상태 변경이 여러 곳(ViewModel, Controller 등)에서 발생하여,

**“어떤 액션이 상태를 변경했는지 추적하기 어려움”**

• **데이터 흐름이 복잡해져서, 디버깅과 유지보수가 어려워짐**

• **멀티스레드 환경에서 상태 동기화 문제 발생**

  

🔽 **해결책: 데이터가 한 방향으로만 흐르면 상태 관리가 쉬워질 것!**

🔽 **이 개념을 구현한 대표적인 라이브러리가 바로 Redux!**


##  Redux 스타일이 적용된 다양한 아키텍처

  

Redux의 개념이 iOS, Android, 웹 등 여러 플랫폼에 영향을 주면서,

비슷한 개념을 따르는 다양한 아키텍처가 등장했다. 

| 아키텍처                    | 플랫폼                                    | 구현                                        |
| --------------------------- | ----------------------------------------- | ------------------------------------------- |
| **Redux**                   | React, Vue, Angular                       | View, Action, Reducer, Store                |
| **ReactorKit**              | UIKit (RxSwift 의존)                      | View, Action, Reactor, State                |
| **ReSwift**                 | UIKit (ReSwift 의존)                      | View, Action, Store, State, Reducer         |
| **TCA**                     | SwiftUI (Combine)                         | View, Store(Action, Reducer, State, effect) |
| **MVI** | (SwiftUI / UIKit),  (Rx/Combine) 사용가능 | View, Intent, Model, State                  |
|                             |                                           |                                             |



## 단방향과 양방향의 차이

| 구분                 | 단방향 데이터 흐름                             | 양방향 데이터 흐름                               |
| -------------------- | ---------------------------------------------- | ------------------------------------------------ |
| **데이터 흐름 방향** |  단방향 (→)                                   | 양방향 (↔️)                                      |
| **흐름 설명**        | Intent(Action) → Logic(Reducer) → State → View | M↔C→V, M↔P↔V, M↔VM←V                             |
| **대표 패턴**        | Redux, TCA, ReactorKit, MVI                    | MVC, MVP, MVVM                                   |
| **상태 변경 책임**   | 상태는 한 곳(Store)이 책임지고 관리            | 상태가 여러 곳(ViewModel, View 등)에서 변경 가능 |
| **장점**             | 데이터 흐름이 예측 가능                        | 구조가 직관적 (빠른 학습 가능)                   |
| **단점**             | 코드가 다소 장황할 수 있음                     | 데이터 흐름 추적이 어려움 (특히 대규모 앱에서)   |









  

  


---
## History
- 250302 : 초안 추가
- 250304 : Redux 스타일이 적용된 다양한 아키텍처
