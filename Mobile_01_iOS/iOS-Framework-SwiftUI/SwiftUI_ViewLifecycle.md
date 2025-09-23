# SwiftUI View 생명주기 정리

## 1. SwiftUI의 기본 철학
- SwiftUI는 선언형(directive)으로 UI 상태를 기술하고, 상태가 바뀔 때마다 **뷰를 다시 그리는 대신 새로운 뷰를 계산**합니다.
- 따라서 UIKit처럼 명시적인 `viewDidLoad`/`viewWillAppear` 이벤트가 없고, **상태가 곧 라이프사이클**을 좌우합니다.

## 2. 주요 생명주기 훅
| 상황 | 대표 훅 / 속성 | 설명 |
| --- | --- | --- |
| 뷰가 처음 등장할 때 | `onAppear` | 뷰가 렌더링되어 사용자에게 보이기 직전에 한 번 호출됩니다. 네트워크 로딩, 애니메이션 시작 등에 사용. |
| 뷰가 사라질 때 | `onDisappear` | 뷰가 계층에서 제거될 때 호출. 타이머 해제, 리소스 정리 등. |
| 상태값이 변경될 때 | `@State`, `@Binding`, `@ObservedObject`, `@EnvironmentObject` | 값이 바뀌면 해당 값을 참조하는 바디가 다시 계산되며, 필요하면 전체 뷰 트리가 리렌더링됩니다. |
| 장면(신) 상태 전환 | `@Environment(\.scenePhase)` | 앱이 `active`, `inactive`, `background` 상태로 옮겨갈 때 감지. |
| 작업(Task) 동작 | `.task { }` | 뷰가 나타날 때 비동기 작업을 시작하고, 필요시 취소됩니다. |

## 3. 상태 기반 수명 주기와 State 보존 규칙
- `@State`는 뷰가 **동일한 identity**를 유지하는 동안 값을 보존하고, 뷰가 완전히 제거되면 초기값으로 리셋됩니다.
- `@ObservedObject` / `@EnvironmentObject`는 외부에서 소유하므로 뷰가 사라져도 객체 자체는 살아있습니다.
- `@StateObject`는 뷰에서 소유하는 객체를 생성할 때 사용하며, 최초 생성 이후에는 뷰가 리로드되어도 동일 인스턴스를 재사용합니다.

## 4. SwiftUI와 UIKit의 대응 관계
| UIKit 생명주기 | SwiftUI에서 고려할 포인트 |
| --- | --- |
| `viewDidLoad` | `onAppear`, `.task`에서 초기 데이터 불러오기 |
| `viewWillAppear` / `viewDidAppear` | `onAppear`는 한 번만 호출될 수도 있고(조건부 렌더링), 반복해서 호출될 수도 있어 idempotent 하게 작성 필요 |
| `viewWillDisappear` / `viewDidDisappear` | `onDisappear`에서 리소스 정리 |
| `viewDidLayoutSubviews` | SwiftUI에서는 레이아웃 재계산을 시스템이 처리, 필요시 `GeometryReader`로 레이아웃 값을 추적 |

## 5. 실무 팁
- `onAppear`는 여러 번 호출될 수 있으므로, 중복 실행 방지 로직이나 상태 플래그를 사용합니다.
- 비동기 작업은 `.task`나 `Task {}`를 활용하고, `onDisappear`에서 `Task.cancel()`로 안전하게 종료합니다.
- `scenePhase`를 감지해 백그라운드 진입 시 데이터 저장, 포그라운드 복귀 시 최신 데이터 동기화를 수행합니다.
- UIKit과 혼용 시, UIKit 생명주기를 SwiftUI에 전달하려면 `UIViewControllerRepresentable`/`Coordinator` 패턴을 이용합니다.

## 6. 참고 문서
- [Apple 공식 문서 - Managing model data in your apps](https://developer.apple.com/tutorials/app-dev-training/managing-model-data-in-your-apps)
- [Apple 공식 문서 - Handling user interface updates](https://developer.apple.com/documentation/swiftui/) (관련 섹션)
