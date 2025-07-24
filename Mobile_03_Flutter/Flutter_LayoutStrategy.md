# Flutter 레이아웃 구현 전략

## 1. 선언형 UI 구조로의 전환

- 기존 명령형 UI (예: iOS의 UIKit, Android의 Android View)는 부모 기준의 좌표/제약 조건 직접 지정
- Flutter는 선언형 구조: 상태에 따라 UI를 선언 → 프레임워크가 변화 반영  
  (iOS의 SwiftUI, Android의 Jetpack Compose와 유사한 개념)
- 레이아웃 구성 흐름: "바깥에서 안으로" 설계

---

## 2. 외곽부터 좁혀가는 설계 흐름
- 명령형 UI는 콘텐츠의 위치를 직접 지정하는 방식 (내부에서 외부로 배치)
- 선언형 UI는 외부 레이아웃이 내부 콘텐츠의 범위를 제약하는 구조
- Flutter는 외곽부터 제약(Padding, SafeArea 등)을 설정하고, 그 안에 콘텐츠를 배치하는 방식이 자연스러움


- 디버깅 시: 색상 있는 **Container**로 레이아웃 범위 확인 → Flutter Inspector의 **Show Guidelines** 기능 활용

---

## 3.  StatusBar  영역의 제한
기본적으로 SafeArea를 사용하면 StatusBar로의 영역을 침범하지않고 Layout을 구현할 수 있다.  
다만 안드로이드의 여러 조건에 따라 StatusBar가 겹쳐지는 등의 이슈가 있어서 SafeArea를 사용하기보단  MediaQuery를 통해 StatusBar의 길이를 가져와서 처리를 하는게 바람직하다. 

- 시스템 UI 대응:
  - iOS: SafeArea 사용 가능
  - Android: 기기별, 버전별로 차이가 생길 수 있다. 

```dart
return Scaffold(  
  body: SafeArea(child: Padding(  
    padding: const EdgeInsets.fromLTRB(10, 0, 10, 0),  
    child: Container(color: Colors.red),  
  )),  
);
```



- 수동 여백 처리:
  - 예시:
    ```dart
    padding: EdgeInsets.only(top: MediaQuery.of(context).padding.top)
    ```
- 핵심: 중심 콘텐츠(Container 등)를 기준으로, 외곽부터 안전 영역과 여백 정의 → 콘텐츠 배치


---



## 4. 적용 예시

- 구조 설계 흐름:
  1. Scaffold
  2. SafeArea or padding
  3. Outer Padding (`EdgeInsets.symmetric`)
  4. Column/ListView
  5. 콘텐츠 위젯 배치



- 시스템 UI 대응:
  - iOS: SafeArea 사용 가능
  - Android: 기기별, 버전별로 차이가 생길 수 있다. 

```dart
return Scaffold(  
  body: SafeArea(child: Padding(  
    padding: const EdgeInsets.fromLTRB(10, 0, 10, 0),  
    child: Container(color: Colors.red),  
  )),  
);
```



- 수동 여백 처리:
  - 예시:
    ```dart
    padding: EdgeInsets.only(top: MediaQuery.of(context).padding.top)
    ```
- 핵심: 중심 콘텐츠(Container 등)를 기준으로, 외곽부터 안전 영역과 여백 정의 → 콘텐츠 배치



- 적용 샘플:
  ```dart
  return Scaffold(
    body: Padding(
      padding: EdgeInsets.only(top: MediaQuery.of(context).padding.top),
      child: Container(color: Colors.red),
    ),
  );
  ```

---

## 5. 결론

- SafeArea는 범용이지만, 플랫폼 간 일관성 확보에는 한계 있음
- MediaQuery 기반 수동 처리로 명확한 제어 가능
- Flutter의 레이아웃은 "부모 → 자식 → 콘텐츠"로 범위 축소하며 설계하는 구조가 효과적



## History
- 250718 : 초안작성

