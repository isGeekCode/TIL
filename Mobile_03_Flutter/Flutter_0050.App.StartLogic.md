# Flutter 앱 실행 흐름 이해하기

<br><br>
---

## 1. 개요

Flutter 앱이 어떻게 시작되는지를 이해하는 것은 전체 구조를 파악하는 데 중요한 출발점이다.  
이 문서에서는 `main()` 함수부터 시작하여 `MaterialApp` 또는 `CupertinoApp`을 통해 앱이 실행되는 흐름을 설명한다.

<br><br>
---

## 2. 시작하기 전에 알아두면 좋은 것들

- 모든 Flutter 앱은 `main()`에서 시작한다.  
- `runApp()`은 루트 위젯을 렌더링하는 함수이다.  
- `MaterialApp`과 `CupertinoApp`은 앱 전체를 감싸는 컨테이너 역할을 하며, 각각의 특성에 맞게 사용된다 → 자세한 설명은 5-1 참고.  
- 대부분의 경우 `MaterialApp`으로 시작하며, 특별한 목적(iOS 스타일 앱)이 있는 경우만 `CupertinoApp`을 사용한다.  

<br><br>
---

## 3. 개념 정리 / 기본 구조

Flutter 앱은 `main()` 함수로부터 실행을 시작한다.  
이 함수에서 `runApp()`이 호출되며, 이때 전달된 위젯이 앱의 루트 위젯이 된다.

<br><br>

### 3-1. main() → runApp()

이 단계는 모든 Flutter 앱의 필수 시작 지점이다.

```dart
void main() {
  runApp(MyApp());
}
```

<br><br>

- `main()` 함수는 앱의 진입점.  
- `runApp()`은 위젯 트리의 루트 역할을 하는 위젯을 렌더링 시작.  

<br><br>
---

### 3-2. MyApp → MaterialApp (또는 CupertinoApp)

```dart
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: HomePage(),
    );
  }
}
```

<br><br>

- `MaterialApp`: 테마, 라우팅, 로컬라이징 등 앱 전역 설정을 담당.  
- `CupertinoApp`: iOS 스타일 앱을 위한 설정 전용 위젯.  

대부분의 앱은 `MaterialApp` 또는 `CupertinoApp` 중 하나를 반드시 사용해야 한다.  

<br><br>
#### 3-2-1. 왜 MyApp은 StatelessWidget인가?

앱 자체에는 변경되는 상태가 없고, 구성만 담당하기 때문이다.  
이후 상태 변경이 필요한 경우는 `home`으로 지정한 화면 위젯에서 `StatefulWidget`을 사용한다.

<br><br>
#### MaterialApp 주요 속성 요약

| 속성           | 설명                          |
|----------------|-------------------------------|
| `title`        | 앱 제목                       |
| `theme`        | 테마 정보 (`ThemeData`)       |
| `home`         | 시작 화면 위젯                |
| `routes`       | 이름 기반 라우팅 테이블       |
| `initialRoute` | 앱 실행 시 시작할 라우트 지정 |

<br><br>
---

### 3-3. home 속성

- 앱 실행 시 최초로 보여줄 위젯을 지정.  
- 일반적으로 `Scaffold` 기반의 UI 구성 위젯이 배치된다.  
- 페이지는 보통 `StatelessWidget` 또는 `StatefulWidget`이 사용된다.  

<br><br>
---

### 3-4. 실행 구조 요약

```text
main()
└─ runApp()
    └─ MyApp
        └─ MaterialApp
            └─ home: HomePage()
```

<br><br>

- 위 구조는 Flutter 앱의 기본 실행 흐름.  
- 이후 모든 상태 관리, 네비게이션, 화면 구성은 이 구조를 기반으로 확장됨.  

<br><br>
---

## 4. 실무에서 자주 쓰이는 초기화 및 설정

초반에는 간단한 구조로 `main()`과 `runApp()`만 사용하는 경우가 많지만, 실무에서는 다음과 같은 초기화 작업이 함께 쓰이는 경우가 많다.

<br><br>
### 4-1. 비동기 초기화

Firebase, SharedPreferences, 환경 설정 등 비동기 초기화가 필요한 경우 `main()`을 `async`로 선언하고 `WidgetsFlutterBinding.ensureInitialized()`를 사용해야 한다.

```dart
void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

<br><br>
---

### 4-2. flavor 설정

앱을 QA / DEV / PROD 등 환경별로 구분할 때, `main.dart`를 여러 개 만들거나 `const String environment = 'dev';` 형태로 구분하여 초기 세팅을 나누는 구조도 자주 사용된다.

→ 관련 설정 예시는 [Build Flavor Setup Guide](https://github.com/isGeekCode/TIL/blob/main/Mobile_03_Flutter/Flutter_6012.BuildFlavorSetupGuide.md) 문서를 참고할 수 있다.



<br><br>
---

## 5. 확장 개념 / 보충 설명

<br><br>
### 5-1. CupertinoApp만 써야 할까?

`CupertinoApp`은 iOS 스타일의 디자인 요소와 동작을 구현할 때 사용하는 전용 앱 컨테이너이다. 하지만 다음과 같은 경우가 아니라면 반드시 사용할 필요는 없다.

- 디자인이 iOS 전용인 앱: 완전히 iOS 스타일 UI를 따르는 앱  
- Cupertino Navigation, Tab 사용: `CupertinoTabScaffold`, `CupertinoPageScaffold` 등 활용  

대부분의 앱에서는 `MaterialApp`을 사용하고, 필요 시 내부에서 `Cupertino` 위젯만 혼합 사용하는 것이 일반적이다.

iOS 앱도 `MaterialApp`으로 충분히 구현 가능하며, 실제 실무에서도 많이 사용된다.

<br><br>
---

## HISTORY
- 250729 : 최초 작성
