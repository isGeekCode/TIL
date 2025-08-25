# InheritedNotifier 기본 구조와 동작 방식

## 개념

`InheritedNotifier`는 Flutter에서 상태 관리를 위해 사용되는 위젯 중 하나로, `ChangeNotifier`를 기반으로 하여 데이터의 변경을 감지하고 이를 하위 위젯들에게 효율적으로 전달하는 역할을 합니다. `InheritedWidget`과 `ChangeNotifier`의 장점을 결합한 형태로, 상태가 변경될 때마다 하위 위젯들을 자동으로 리빌드하게 만들어 UI의 일관성을 유지합니다.

기본적으로 `InheritedNotifier`는 `ChangeNotifier`를 감시하며, `ChangeNotifier`가 변경될 때 `InheritedNotifier`를 구독하는 하위 위젯들에게 알림을 전달합니다. 이를 통해 하위 위젯들은 필요한 데이터가 변경되었을 때만 리빌드되어 성능 최적화에 유리합니다.

---

## 동작 원리

1. **ChangeNotifier 등록**  
   `InheritedNotifier`는 생성자에서 `ChangeNotifier`를 받습니다. 이 `ChangeNotifier`는 상태를 보유하고 있으며, 상태가 변경될 때마다 리스너들에게 알림을 보냅니다.

2. **리스너 등록**  
   `InheritedNotifier`는 내부적으로 `ChangeNotifier`에 리스너를 등록합니다. 이 리스너는 상태가 변경되면 `InheritedNotifier`가 다시 빌드되도록 합니다.

3. **하위 위젯 접근**  
   하위 위젯들은 `BuildContext.dependOnInheritedWidgetOfExactType` 메서드를 통해 `InheritedNotifier`를 찾아 의존성을 등록합니다. 이로 인해 상태 변경 시 해당 위젯들이 리빌드됩니다.

4. **알림 전파**  
   `ChangeNotifier`가 상태 변경을 알리면, `InheritedNotifier`는 자신을 의존하고 있는 하위 위젯들에게 알리고, 하위 위젯들은 리빌드됩니다.

---

## 구조

```
InheritedNotifier<T extends ChangeNotifier>
  ├─ notifier: T
  ├─ child: Widget
  ├─ updateShouldNotify(InheritedNotifier oldWidget)
  └─ of(BuildContext context)  // static 메서드로 하위 위젯들이 접근
```

- `notifier`: 상태를 관리하는 `ChangeNotifier` 객체입니다.
- `child`: `InheritedNotifier`가 감싸는 하위 위젯입니다.
- `updateShouldNotify`: 상태 변경 시 알림을 보낼지 결정합니다. 기본적으로 `notifier`가 변경되었는지 비교합니다.
- `of`: 하위 위젯들이 `InheritedNotifier`를 찾아 의존성을 등록하는 편리한 메서드입니다.

---

## 예제 코드

아래는 `InheritedNotifier`를 사용하여 카운터 상태를 관리하는 간단한 예제입니다.

```dart
import 'package:flutter/material.dart';

// ChangeNotifier를 상속하여 상태 관리
class CounterNotifier extends ChangeNotifier {
  int _count = 0;

  int get count => _count;

  void increment() {
    _count++;
    notifyListeners(); // 상태 변경 알림
  }
}

// InheritedNotifier를 상속한 위젯
class CounterProvider extends InheritedNotifier<CounterNotifier> {
  CounterProvider({
    Key? key,
    required CounterNotifier notifier,
    required Widget child,
  }) : super(key: key, notifier: notifier, child: child);

  // 하위 위젯들이 CounterProvider를 쉽게 찾도록 static 메서드 제공
  static CounterNotifier of(BuildContext context) {
    final CounterProvider? provider =
        context.dependOnInheritedWidgetOfExactType<CounterProvider>();
    assert(provider != null, 'No CounterProvider found in context');
    return provider!.notifier!;
  }
}

void main() {
  final counterNotifier = CounterNotifier();

  runApp(
    CounterProvider(
      notifier: counterNotifier,
      child: const MyApp(),
    ),
  );
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final counter = CounterProvider.of(context);

    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: const Text('InheritedNotifier Example')),
        body: Center(
          child: Text(
            'Count: ${counter.count}',
            style: const TextStyle(fontSize: 40),
          ),
        ),
        floatingActionButton: FloatingActionButton(
          onPressed: () => counter.increment(),
          child: const Icon(Icons.add),
        ),
      ),
    );
  }
}
```

### 설명

- `CounterNotifier`는 카운터 상태를 관리하며, 상태 변경 시 `notifyListeners()`를 호출합니다.
- `CounterProvider`는 `InheritedNotifier`를 상속하여 `CounterNotifier`를 감시하고, 하위 위젯들이 쉽게 접근할 수 있도록 `of` 메서드를 제공합니다.
- `MyApp` 위젯은 `CounterProvider.of(context)`를 통해 상태에 접근하고, 상태가 변경되면 자동으로 리빌드됩니다.

---

## 비교

| 구분              | InheritedWidget                  | InheritedNotifier               | Provider (패키지)                |
|-----------------|-------------------------------|-------------------------------|-------------------------------|
| 상태 변경 감지 방식 | 직접 `updateShouldNotify` 구현 필요 | `ChangeNotifier` 기반 자동 감지 | 내부적으로 `InheritedNotifier` 또는 `ChangeNotifier` 사용 |
| 사용 편의성        | 다소 복잡                      | 비교적 간단                    | 매우 간단하고 다양한 기능 제공 |
| 성능               | 효율적이나 직접 관리 필요        | 효율적, 상태 변경 시만 알림      | 최적화 및 확장성 우수           |
| 상태 관리 방식      | 불변 데이터 전달                | 가변 상태, `ChangeNotifier` 활용 | 다양한 상태 관리 방식 지원      |
| 예제 코드 복잡도    | 다소 높음                     | 중간                         | 낮음                         |

---

## 실습 과제

1. `InheritedNotifier`를 사용하여 테마 색상을 변경하는 앱을 만들어보세요.  
   - `ChangeNotifier`를 사용해 테마 색상 값을 관리합니다.  
   - 버튼을 눌러 색상을 변경하면 앱 전체가 변경된 색상으로 리빌드됩니다.

2. `InheritedNotifier`와 `InheritedWidget`을 각각 사용해 간단한 상태 관리를 구현해보고, 두 방식의 차이를 코드와 실행 결과로 비교해보세요.

3. `CounterNotifier`에 `decrement()` 메서드를 추가하고, UI에 감소 버튼을 추가하여 상태 변경이 정상적으로 반영되는지 확인하세요.

---

## 확장 개념

- **`InheritedNotifier`의 재사용성**  
  `InheritedNotifier`는 여러 `ChangeNotifier`를 조합하여 복합 상태 관리에도 활용할 수 있습니다. 예를 들어, 여러 개의 `ChangeNotifier`를 하나의 상위 `ChangeNotifier`로 묶어 관리할 수 있습니다.

- **`InheritedNotifier`와 `Provider` 패키지**  
  Flutter 커뮤니티에서는 `InheritedNotifier`를 기반으로 한 `Provider` 패키지를 널리 사용합니다. `Provider`는 `InheritedNotifier`의 복잡성을 감추고, 더 많은 기능과 편의성을 제공합니다.

- **성능 최적화**  
  `InheritedNotifier`는 상태가 변경될 때 의존하는 하위 위젯만 리빌드하지만, 너무 많은 위젯이 의존성을 등록하면 성능 저하가 발생할 수 있습니다. 따라서 적절한 위젯 분리와 의존성 관리가 필요합니다.

- **다른 ChangeNotifier 파생 클래스와 결합**  
  `ValueNotifier`, `Listenable` 등 `ChangeNotifier`를 확장한 다양한 클래스를 `InheritedNotifier`와 함께 사용할 수 있습니다. 이를 통해 상태 관리의 유연성을 높일 수 있습니다.

---

`InheritedNotifier`는 Flutter에서 상태 변경을 효율적으로 알리고, UI를 자동으로 갱신하는 강력한 도구입니다. 이를 이해하고 활용하면, 복잡한 상태 관리도 간결하고 명확하게 구현할 수 있습니다.

## InheritedWidget 대비 개선점과 코드 차이

- 리빌드 범위 최소화 (필요한 하위만 리빌드)
- 부모 위젯 리빌드 불필요 (상태 변경 시 provider 자체는 리빌드되지 않음)
- 역할 분리: 상태 관리와 전달 분리
- 불변 패턴 강제 없음 (`ChangeNotifier`로 가변 상태 관리)
- 테스트 및 확장성 용이

### Before: InheritedWidget 기반

```dart
import 'package:flutter/material.dart';

class CounterProvider extends InheritedWidget {
  final int count;
  final VoidCallback increment;

  const CounterProvider({
    Key? key,
    required this.count,
    required this.increment,
    required Widget child,
  }) : super(key: key, child: child);

  static CounterProvider of(BuildContext context) {
    final CounterProvider? result =
        context.dependOnInheritedWidgetOfExactType<CounterProvider>();
    assert(result != null, 'No CounterProvider found in context');
    return result!;
  }

  @override
  bool updateShouldNotify(CounterProvider oldWidget) {
    return oldWidget.count != count;
  }
}

void main() {
  runApp(MyApp());
}

class MyApp extends StatefulWidget {
  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  int _count = 0;
  void _increment() => setState(() => _count++);

  @override
  Widget build(BuildContext context) {
    return CounterProvider(
      count: _count,
      increment: _increment,
      child: MaterialApp(
        home: Scaffold(
          body: Center(child: CounterWidget()),
          floatingActionButton: FloatingActionButton(
            onPressed: _increment,
            child: Icon(Icons.add),
          ),
        ),
      ),
    );
  }
}

class CounterWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final provider = CounterProvider.of(context);
    return Text('Count: ${provider.count}', style: TextStyle(fontSize: 32));
  }
}
```

### After: InheritedNotifier + ChangeNotifier

```dart
import 'package:flutter/material.dart';

class CounterNotifier extends ChangeNotifier {
  int _count = 0;
  int get count => _count;
  void increment() {
    _count++;
    notifyListeners();
  }
}

class CounterProvider extends InheritedNotifier<CounterNotifier> {
  const CounterProvider({
    Key? key,
    required CounterNotifier notifier,
    required Widget child,
  }) : super(key: key, notifier: notifier, child: child);

  static CounterNotifier of(BuildContext context) {
    final CounterProvider? provider =
        context.dependOnInheritedWidgetOfExactType<CounterProvider>();
    assert(provider != null, 'No CounterProvider found in context');
    return provider!.notifier!;
  }
}

void main() {
  final counterNotifier = CounterNotifier();
  runApp(
    CounterProvider(
      notifier: counterNotifier,
      child: MaterialApp(
        home: Scaffold(
          body: Center(child: CounterWidget()),
          floatingActionButton: FloatingActionButton(
            onPressed: counterNotifier.increment,
            child: Icon(Icons.add),
          ),
        ),
      ),
    ),
  );
}

class CounterWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final counter = CounterProvider.of(context);
    return Text('Count: ${counter.count}', style: TextStyle(fontSize: 32));
  }
}
```

### 핵심 변경 포인트

- **상태 위치**:  
  - before: 부모 `StatefulWidget`의 멤버  
  - after: 별도 `ChangeNotifier` 클래스에서 관리
- **변경 트리거**:  
  - before: `setState()`로 전체 부모 리빌드  
  - after: `notifyListeners()`로 구독 위젯만 리빌드
- **구독/접근 방식**:  
  - before: `of(context)`로 값만 전달  
  - after: `of(context)`로 notifier 전체 구독
- **리빌드 범위**:  
  - before: 부모 위젯 및 하위 전체 리빌드  
  - after: 하위 중 실제 구독 위젯만 리빌드
- **불변성 요구**:  
  - before: 값 변경 시 새 인스턴스 필요 (불변 패턴 권장)  
  - after: 내부 상태 변경(가변) 가능
- **확장성/테스트**:  
  - before: 테스트 어려움, 역할 혼재  
  - after: 상태/로직 분리로 단위 테스트·재사용 용이

### 마이그레이션 체크리스트

1. 기존 상태(`int count` 등)를 `ChangeNotifier` 하위 클래스로 이전
2. `setState()` 대신 `notifyListeners()` 호출로 변경
3. `InheritedWidget` → `InheritedNotifier<NotifierType>`로 교체
4. `updateShouldNotify` 직접 구현 제거 (자동 처리)
5. `of(context)`에서 notifier 반환하도록 수정
6. 상태 변경 트리거(버튼 등)에서 notifier 메서드 호출로 변경

### 성능 팁

- `InheritedNotifier` 범위를 최소화해서 필요한 위젯만 구독하도록 설계하세요.
- selector 패턴 또는 위젯 분리로 불필요한 리빌드 방지(부분 위젯만 구독).
- 리스트/맵 등 컬렉션 갱신 시, 변경 후에만 `notifyListeners()` 호출(불필요한 알림 최소화).



## 보일러플레이트와 Provider 패키지

`InheritedWidget`이나 `InheritedNotifier`를 직접 구현하면 `Provider` 클래스를 정의하고, `of(context)` 메서드를 작성하며, `updateShouldNotify`를 구현하는 등의 반복적인 보일러플레이트 코드가 발생합니다. 이러한 작업은 상태 관리를 위해 필수적이지만, 코드가 길어지고 복잡해질 수 있습니다.


### Provider 패키지

`Provider` 패키지는 Flutter에서 상태 관리를 간편하게 해주는 라이브러리로, `InheritedNotifier`를 기반으로 하면서 보일러플레이트를 줄이고 사용성을 크게 향상시켰습니다. `ChangeNotifierProvider`와 `Consumer` 위젯을 통해 상태를 쉽게 제공하고 구독할 수 있습니다.



