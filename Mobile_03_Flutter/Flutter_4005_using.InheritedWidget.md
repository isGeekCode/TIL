# InheritedWidget 기본 구조와 동작 방식


<br>

## InheritedWidget이 필요한 이유

Flutter에서 상태를 여러 위젯에 공유하려면 단순히 setState만으로는 한계가 있다.
예를 들어, 부모에서 만든 데이터를 자식 여러 개가 동시에 접근하려면 트리 전체를 따라 값 전달을 해야 하는데, 이는 번거롭고 복잡하다.

이 문제를 해결하기 위해 InheritedWidget이 등장하였다.
트리에 Provider를 배치하고, 필요한 곳에서 참조하는 구조이다.

<br>

---
## 동작원리

핵심은 `BuildContext.dependOnInheritedWidgetOfExactType<T>()` 메서드이다.
- Consumer 위젯이 이 메서드를 호출하면, Flutter는 **해당 Consumer가 Provider를 “구독”**하게 만들어 준다.
- 이후 Provider의 값이 바뀌면, 구독 중인 Consumer가 다시 build되면서 최신 값을 반영한다.

즉, 구독과 변경 알림이 자동으로 연결되는 것이 InheritedWidget의 핵심 원리이다.


<br><br>

---
## 기본 구조
InheritedWidget을 직접 사용할 때는 보통 3개의 역할이 필요하다:

1.    상태 관리자 (State Manager)
    •    값 보관 및 변경 책임.
    •    변경되면 Provider에 새로운 상태를 바인딩한다.
2.    Provider (InheritedWidget 확장)
    •    위젯 트리에 상태와 메서드를 배포한다.
    •    updateShouldNotify를 통해 Consumer에게 갱신 여부를 알려준다.
3.    Consumer (데이터를 소비하는 위젯)
    - context.dependOnInheritedWidgetOfExactType로 Provider에 접근한다.
    - Provider로부터 받은 데이터를 UI에 반영한다.


<br>

## 예제코드

```dart
import 'package:flutter/material.dart';

main() => runApp(MyApp());

// MARK: State Manager 역할
class MyApp extends StatefulWidget {
  const MyApp({super.key});
  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  int count = 0;

  void _increment() {
    setState(() {
      count = count + 1;
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: CounterProvider(
        _increment,
        count: count,
        child: MainScreen(),
      ),
    );
  }
}

// MARK: Consumer 역할
class MainScreen extends StatelessWidget {
  const MainScreen({super.key});
  @override
  Widget build(BuildContext context) {
    final provider = CounterProvider.of(context);

    return Scaffold(
      appBar: AppBar(title: Text('Main Screen')),
      body: Center(child: Text('Count: ${provider.count}')),
      floatingActionButton: FloatingActionButton(
        onPressed: provider.increment,
        child: Icon(Icons.add),
      ),
    );
  }
}
 
// MARK: Provider 역할
class CounterProvider extends InheritedWidget {
  final int count;
  final void Function() increment;

  const CounterProvider(
    this.increment, {
    super.key,
    required super.child,
    required this.count,
  });

  static CounterProvider of(BuildContext context) {
    final result = context.dependOnInheritedWidgetOfExactType<CounterProvider>();
    assert(result != null, 'No CounterProvider found in context');
    return result!;
  }

  @override
  bool updateShouldNotify(CounterProvider oldWidget) {
    return oldWidget.count != count;
  }
}
```

<br>

### 코드 분석
- MyApp (State Manager)
    - count 값과 _increment 메서드를 관리한다.
    - 값이 바뀔 때마다 새로운 상태를 CounterProvider에 주입한다.
- CounterProvider (Provider)
    - count와 increment를 트리에 배포한다.
    - updateShouldNotify로 변경 여부를 Consumer에게 알려준다.
- MainScreen (Consumer)
    - CounterProvider.of(context)로 상태를 받아온다.
    - provider.count를 화면에 출력한다.
    - provider.increment를 버튼에 연결해 값 갱신을 수행한다.


<br><br>

## 다른 상태 관리 방식 비교
- setState → 위젯 하나 내부 전용
- ChangeNotifier → 여러 위젯 구독
- InheritedWidget → 트리 전역 또는 특정 영역 공유

### setState
- StatefulWidget 내부에서만 동작하는 가장 단순한 방식이다.
- 호출 시 해당 위젯 전체가 다시 빌드된다.
- 적합한 경우: 작은 위젯 내부에서만 상태를 관리할 때.

### ChangeNotifier
- 여러 위젯이 같은 상태를 구독할 수 있는 옵저버 패턴이다.
- notifyListeners() 호출 시 구독 중인 위젯만 다시 빌드된다.
    - 이 위젯들의 setState가 실행된다고 이해하면 된다.
- InheritedNotifier나 Provider와 결합해 전역 공유에 자주 사용된다.
- 적합한 경우: 여러 위젯이 동시에 상태를 공유해야 할 때.


### InheritedWidget
- 트리 자체에 상태를 심어 하위 위젯이 context로 접근한다.
- 구독 중인 위젯만 다시 빌드된다.
- 적합한 경우: 테마, 사용자 정보, 로케일 같은 전역적 상태 공유.



📌 방식별로 보면
- setState → “나 바뀌었어! 내 build() 다시 실행해!”
- ChangeNotifier → “나 바뀌었어! 나를 구독 중인 애들만 다시 빌드해!”
- InheritedWidget → “값이 달라지면 트리 아래 구독자 위젯만 빌드해!”
- Riverpod/Bloc → 같은 원리, 다만 더 구조적이고 확장성 있게 래핑한다.


### 상태관리 학습흐름도
- setState → 기초
- ValueNotifier → 단일 값 옵저버 패턴
- InheritedWidget → 상태를 트리 전역에 공유
- ChangeNotifier → 다수 상태 관리 + 옵저버 패턴
- InheritedNotifier → InheritedWidget + ChangeNotifier (Provider의 기초)


## Provider라는 명칭
Provider라는 이름은 원래 CS 전반에서 "무언가를 공급하는 역할"이라는 의미로 자주 쓰인다. 

Flutter에서도 이 컨벤션을 따라, InheritedWidget을 감싸는 클래스를 만들 때 보통 `~Provider`라는 이름을 붙인다.  

예: `CounterProvider`, `ThemeProvider`, `AuthProvider`

한편, Flutter의 **공식 상태관리 라이브러리인 `provider` 패키지**는 InheritedWidget과 InheritedNotifier를 기반으로 만들어졌다. 단순 값부터 `ChangeNotifier`, `Future`, `Stream`까지 다양한 상태를 Provider로 감싸 공급할 수 있고, 하위 위젯은 `context.watch<T>()`, `context.read<T>()`, `Consumer<T>` 같은 API를 통해 간단하게 접근할 수 있다.  




## 실무 적용 포인트

- `InheritedWidget`은 특정 부분의 위젯들끼리 데이터를 나눌 때 적합하다. 앱 전체 상태는 `Provider`나 `Riverpod` 같은 도구를 사용하는 것이 더 편리하다.
- `updateShouldNotify`를 잘 설계하여 불필요하게 다시 그리는 일을 줄여야 한다.
- `of(context)`는 반드시 `InheritedWidget` 아래에서 호출해야 한다. 빌드 과정 외부에서는 주의해야 한다.
- 상태가 자주 바뀌면 `InheritedNotifier`(예: `ChangeNotifier`)를 사용하면 더 세밀하게 제어할 수 있다.

<br><br>

---


## 확장 개념 

### InheritedNotifier 소개

`InheritedNotifier<T extends Listenable>`는 내부에 `Listenable`(예: `ChangeNotifier`)를 넣어서, 상태가 바뀌면 알림을 보내고 필요한 위젯만 다시 그리게 한다. `Provider` 패키지가 이런 방법을 사용한다.

```dart
class AppState extends InheritedNotifier<MyViewModel> {
  const AppState({Key? key, required MyViewModel notifier, required Widget child})
    : super(key: key, notifier: notifier, child: child);

  static MyViewModel of(BuildContext context) {
    final inherited = context.dependOnInheritedWidgetOfExactType<AppState>();
    assert(inherited != null, 'No AppState found in context');
    return inherited!.notifier!;
  }
}
```




<br><br>

---


## 실습 과제

1. `ThemeInheritedWidget`을 만들어서 앱에서 라이트 모드와 다크 모드를 변경해 보아야 한다. 위젯들이 자동으로 변경되어야 한다.
2. 기존에 `ChangeNotifier`를 사용하던 동적 리스트 관리 예제를 `InheritedNotifier`로 변경해 보아야 한다. 다시 그려지는 부분이 어떻게 달라지는지 비교해야 한다.
3. `updateShouldNotify`가 항상 `false`를 반환하도록 변경한 뒤 앱이 어떻게 동작하는지 관찰하고 결과를 정리해야 한다.

<br><br>

---


## HISTORY

- 250820 : 최초 작성
- 250821 : 각 상태관리 방법 비교 추가
