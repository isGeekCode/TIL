### 2. ChangeNotifier

```dart
import 'package:flutter/material.dart';

class CounterNotifier extends ChangeNotifier {
  int _count = 0;

  int get count => _count;

  void increment() {
    _count++;
    notifyListeners();
  }

  void decrement() {
    _count--;
    notifyListeners();
  }
}

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final counter = CounterNotifier();

    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: const Text('ChangeNotifier Example')),
        body: Center(
          child: ListenableBuilder(
            listenable: counter,
            builder: (context, _) {
              return Text('Count: ${counter.count}', style: const TextStyle(fontSize: 32));
            },
          ),
        ),
        floatingActionButton: Column(
          mainAxisAlignment: MainAxisAlignment.end,
          children: [
            FloatingActionButton(
              onPressed: counter.increment,
              child: const Icon(Icons.add),
            ),
            const SizedBox(height: 8),
            FloatingActionButton(
              onPressed: counter.decrement,
              child: const Icon(Icons.remove),
            ),
          ],
        ),
      ),
    );
  }
}
```

**특징**
- `ChangeNotifier`는 여러 상태 변경을 관리할 수 있는 클래스입니다.
- `notifyListeners()` 호출 시 등록된 모든 리스너가 알림을 받습니다.
- 상태 관리와 UI 갱신을 분리하기 쉬워 확장성이 좋습니다.

**단점**
- 복잡한 상태 관리 시 코드가 장황해질 수 있습니다.
- 리스너가 많아지면 성능 저하 우려가 있습니다.
- 상태 공유 범위가 넓어질 경우 관리가 어려울 수 있습니다.

### 3. InheritedWidget

```dart
import 'package:flutter/material.dart';

class CounterProvider extends InheritedWidget {
  final int count;
  final VoidCallback increment;
  final VoidCallback decrement;

  const CounterProvider({
    Key? key,
    required this.count,
    required this.increment,
    required this.decrement,
    required Widget child,
  }) : super(key: key, child: child);

  static CounterProvider? of(BuildContext context) {
    return context.dependOnInheritedWidgetOfExactType<CounterProvider>();
  }

  @override
  bool updateShouldNotify(CounterProvider oldWidget) {
    return oldWidget.count != count;
  }
}

void main() {
  runApp(const MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  int _count = 0;

  void _increment() {
    setState(() {
      _count++;
    });
  }

  void _decrement() {
    setState(() {
      _count--;
    });
  }

  @override
  Widget build(BuildContext context) {
    return CounterProvider(
      count: _count,
      increment: _increment,
      decrement: _decrement,
      child: const MaterialApp(
        home: MainScreen(),
      ),
    );
  }
}

class MainScreen extends StatelessWidget {
  const MainScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final provider = CounterProvider.of(context)!;

    return Scaffold(
      appBar: AppBar(title: const Text('InheritedWidget Example')),
      body: Center(
        child: Text('Count: ${provider.count}', style: const TextStyle(fontSize: 32)),
      ),
      floatingActionButton: Column(
        mainAxisAlignment: MainAxisAlignment.end,
        children: [
          FloatingActionButton(
            onPressed: provider.increment,
            child: const Icon(Icons.add),
          ),
          const SizedBox(height: 8),
          FloatingActionButton(
            onPressed: provider.decrement,
            child: const Icon(Icons.remove),
          ),
        ],
      ),
    );
  }
}
```

**특징**
- `InheritedWidget`은 위젯 트리에서 데이터를 효율적으로 공유할 수 있게 해줍니다.
- 하위 위젯들이 데이터 변경 시 자동으로 rebuild 됩니다.
- Flutter의 기본 상태 공유 메커니즘으로 다른 상태 관리 라이브러리의 기반이 됩니다.

**단점**
- 직접 구현 시 코드가 복잡하고 장황해질 수 있습니다.
- 상태 변경 시 전체 위젯 트리가 리빌드되어 성능 저하 우려가 있습니다.
- 복잡한 상태 관리에는 적합하지 않으며, 보통 `InheritedWidget`을 래핑하는 라이브러리를 사용합니다.

---

### 비교 요약

| 방법           | 장점                                   | 단점                                   | 적합한 상황                       |
|----------------|--------------------------------------|---------------------------------------|----------------------------------|
| ValueNotifier  | 간단하고 직관적, 단일 값 상태 관리에 최적 | 복잡한 상태 관리에는 부적합            | 간단한 상태 변화, 단일 값 관리     |
| ChangeNotifier | 여러 상태 관리 가능, 확장성 좋음         | 리스너 많아지면 성능 저하, 코드 장황해질 수 있음 | 중간 규모 상태 관리, MVVM 패턴 등 |
| InheritedWidget| 위젯 트리에서 데이터 공유에 최적화       | 직접 구현 시 복잡, 전체 트리 리빌드 위험 | 앱 전역 상태 공유, 라이브러리 기반 |
