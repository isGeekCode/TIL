# Flutter - 상태관리 개요

Flutter 앱을 개발할 때 중요한 개념 중 하나는 상태 관리(State Management)이다.  
이 문서에서는 Flutter에서 상태가 무엇인지, 그리고 어떤 방식으로 관리되는지 개요 수준에서 정리한다.

<br><br>

## 상태(State)란?

상태란 앱 동작 중 변할 수 있는 데이터를 말한다.  
사용자 입력, 네트워크 응답, 시간 경과 등에 따라 UI는 변경되어야 하며, 이를 결정하는 데이터가 상태이다.

Flutter에서의 상태는 크게 두 가지로 나뉜다.

- **임시 상태 (Ephemeral State)**  
  - 단일 위젯 내에서만 사용되는 상태  
  - UI의 일시적 변화 관리 (예: 버튼 눌림, 텍스트 필드 포커스 등)  
  - `StatefulWidget`과 `setState()`로 관리

- **앱 상태 (App State)**  
  - 앱 여러 부분에서 공유되는 상태  
  - 장기적으로 유지되는 정보 (예: 사용자 설정, 로그인 토큰 등)  
  - 전역 접근과 효율적인 관리가 필요  
  - Provider, Riverpod, Bloc 등의 라이브러리로 관리

<br><br>

## 상태 관리가 중요한 이유

- **UI 일관성 유지**: 상태 변화가 UI에 정확히 반영되어야 함  
- **코드 구조화**: 상태와 UI 로직을 분리하면 유지보수가 쉬워짐  
- **성능 최적화**: 필요한 부분만 빌드하여 성능을 확보할 수 있음  
- **확장성 확보**: 앱이 커질수록 상태 관리 체계가 중요해짐

<br><br>

## 상태 관리 방식의 진화

### 1. `setState()`와 StatefulWidget

Flutter의 기본 상태 관리 방식이다.  
위젯 내부에서 간단한 상태를 직접 관리한다.

```dart
class CounterWidget extends StatefulWidget {
  @override
  _CounterWidgetState createState() => _CounterWidgetState();
}

class _CounterWidgetState extends State<CounterWidget> {
  int _count = 0;

  void _incrementCount() {
    setState(() {
      _count++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Text('카운트: $_count'),
        ElevatedButton(
          onPressed: _incrementCount,
          child: Text('증가'),
        ),
      ],
    );
  }
}
```

- 장점: 간단하고 직관적  
- 단점: 깊은 위젯 트리에서는 상태 전달이 어려움

<br><br>

### 2. InheritedWidget

Flutter 내장 메커니즘으로, 하위 위젯에 상태를 전달할 수 있다.  
직접 구현은 복잡할 수 있지만 데이터 전파에는 효율적이다.

```dart
class CounterInheritedWidget extends InheritedWidget {
  final int count;
  final Function incrementCount;

  CounterInheritedWidget({
    required this.count,
    required this.incrementCount,
    required Widget child,
  }) : super(child: child);

  @override
  bool updateShouldNotify(CounterInheritedWidget oldWidget) {
    return count != oldWidget.count;
  }

  static CounterInheritedWidget of(BuildContext context) {
    return context.dependOnInheritedWidgetOfExactType<CounterInheritedWidget>()!;
  }
}
```

- 장점: 위젯 트리 전파 가능  
- 단점: 코드 작성이 번거롭고 복잡함

<br><br>

### 3. Provider

InheritedWidget을 래핑한 라이브러리로, 더 직관적인 API를 제공한다.

```dart
// 상태 클래스
class CounterModel with ChangeNotifier {
  int _count = 0;
  int get count => _count;

  void increment() {
    _count++;
    notifyListeners();
  }
}

// Provider 설정
ChangeNotifierProvider(
  create: (context) => CounterModel(),
  child: MyApp(),
),

// 데이터 사용
Consumer<CounterModel>(
  builder: (context, counter, child) {
    return Text('카운트: ${counter.count}');
  },
)
```

- 장점: 사용하기 쉽고 이해하기 쉬움  
- 단점: 복잡한 상태를 다루기엔 한계가 있음

<br><br>

### 4. 그 외 현대적 솔루션

- **Riverpod**: Provider의 개선 버전. 테스트성과 안정성이 뛰어남  
- **Bloc/Cubit**: 비즈니스 로직 분리 중심의 구조  
- **MobX**: 반응형 프로그래밍 기반  
- **Redux**: 예측 가능한 상태 컨테이너

<br><br>

## 상태 관리 선택 가이드

어떤 솔루션이 적합할지는 다음 기준을 참고하면 좋다.

- 앱의 복잡도  
- 팀의 경험과 선호도  
- 학습 곡선  
- 성능 요구사항  
- 테스트 용이성

<br><br>

## 다음 섹션 예고

이후 문서에서는 각 상태 관리 기법을 다음과 같은 순서로 자세히 다룰 예정이다:

- `setState()`와 `ValueNotifier`  
- `InheritedWidget`과 `Provider`  
- `Riverpod`  
- TodoList 실습으로 실제 적용

<br><br>

## 요약

- 상태 관리는 Flutter에서 매우 중요한 개념이다  
- 상태는 임시 상태와 앱 상태로 구분할 수 있다  
- 다양한 상태 관리 도구가 있으며, 상황에 따라 선택해야 한다  
- 상태 관리를 잘하면 앱의 유지보수성, 성능, 확장성이 높아진다
