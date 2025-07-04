# Flutter - 상태관리 개요

Flutter 앱을 개발할 때 중요한 개념 중 하나는 상태 관리(State Management)이다.  
이 문서에서는 Flutter에서 상태가 무엇인지, 그리고 어떤 방식으로 관리되는지 개요 수준에서 정리한다.

<br><br>

## 상태(State)란?

상태란 앱 동작 중 변할 수 있는 데이터를 말한다.  
사용자 입력, 네트워크 응답, 시간 경과 등에 따라 UI는 변경되어야 한다.

- 버튼을 누르면 숫자가 올라가고,  
- 로그인을 하면 이름이 보이고,  
- 시간이 지나면 타이머가 줄어드는 것처럼.

이렇게 **UI가 바뀌게 만드는 데이터**를  **“상태”**라고 부른다.

Flutter에서의 상태는 크게 두 가지로 나뉜다.

### 임시 상태 (Ephemeral State)
- 단일 위젯 내에서만 사용되는 상태  
- UI의 일시적 변화 관리 (예: 버튼 눌림, 텍스트 필드 포커스 등)  
- `StatefulWidget`에서 `setState()`로 관리한다

### 앱 상태 (App State)
- 앱 여러 부분 혹은 전체에서 공유되는 상태  
- 예
    - 로그인한 사용자 정보
    - 장바구니 안에 든 상품 목록
    - 테마(다크모드 설정 등)
- 여러 화면에서 이 값을 참고하거나 바꿔야하므로 전역 접근과 효율적인 관리가 필요하다.
    - Provider, Riverpod, Bloc 등의 라이브러리로 관리한다.

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

  // ✅ 상태 (State): UI에 영향을 주는 값
  int _count = 0;

  void _incrementCount() {
    setState(() {
      // ✅ 상태 변경
      _count++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Text('카운트: $_count'), // ✅ 상태 값 사용        
        ElevatedButton(
          // ✅ 상태 변경 트리거
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

<br>

> `setState()`는 해당 클래스 안에서만 작동하기 때문에  
> 하위 위젯에서 직접 상태를 공유하거나 수정하려면 콜백 전달 또는 상태 관리 도구가 필요하다.

<br><br>

### 2. InheritedWidget

Flutter 내장 메커니즘으로, 하위 위젯에 상태를 전달할 수 있다.  
직접 구현은 복잡할 수 있지만 데이터 전파에는 효율적이다.

- 🧭 한눈에 보는 구조 요약
```text
CounterInheritedWidget
└── Scaffold
    └── Column
        ├── CountText        // 상태 표시
        └── IncrementButton  // 상태 변경
```

- 상위 위젯인 `CounterInheritedWidget`이 전체 UI를 감싸고 있고,  
  자식 위젯들은 `context`를 통해 상태 값과 메서드에 접근한다.



```dart
// ✅선언 
// 원래는 build 에서 바로 Scaffold를 리턴하지만 먼저 InheritedWidget로 감싸서 전달할 state를 상위에 선언한다. 

class _InheritedWidgetPageState extends State<InheritedWidgetPage> {
  // ✅ 전달할 State와 함수
  int _count = 0;

  // 상태를 증가시키는 함수 (자식 위젯에서 접근 가능하게 공유됨)
  void _incrementCount() {
    setState(() {
      _count++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return CounterInheritedWidget(
      // ✅ 전달할 State를 이니셜라이저로 전달

      count: _count,
      incrementCount: _incrementCount,
      // ✅ 실제 화면에 표시되는 곳
      child: Scaffold(
        body: const Center(
          child: Column(
            children: [
              // ✅ 전달할 하위 위젯
              CountText(),      // 상태 표시 위젯
              IncrementButton(),// 상태 변경 위젯
            ]
      )));
  )}
}
// 이렇게 감싸두면, 하위 위젯에서 context로 값을 꺼낼 수 있게 된다.


// 상태 표시 위젯
class CountText extends StatelessWidget {
  const CountText({super.key});

  @override
  Widget build(BuildContext context) {
    // ✅ 상위에서 제공한 CounterInheritedWidget으로부터 값 가져오기
    final inherited = CounterInheritedWidget.of(context);
    return Text(
        '카운트: ${inherited.count}',
        style: const TextStyle(fontSize: 24));
  }
}

// 상태 변경 위젯
class IncrementButton extends StatelessWidget {
  const IncrementButton({super.key});

  @override
  Widget build(BuildContext context) {
    // ✅ 상위에서 제공한 CounterInheritedWidget의 함수 사용
    final inherited = CounterInheritedWidget.of(context);
    return ElevatedButton(
      onPressed: () => inherited.incrementCount(),
      child: const Text('증가'),
    );
  }
}

class CounterInheritedWidget extends InheritedWidget {
  final int count; // 공유할 상태 값
  final Function incrementCount; // 공유할 상태 변경 함수
  
  
  // ✅ 생성자에서 공유할 상태를 받아 초기화
  CounterInheritedWidget({
    required this.count,
    required this.incrementCount,
    required Widget child,
  }) : super(child: child);


  // 이전 값과 새로운 값이 다를 때만 하위 위젯을 다시 빌드하도록 알림
  @override
  bool updateShouldNotify(CounterInheritedWidget oldWidget) {
    return count != oldWidget.count;
  }


  // ✅ context를 통해 트리 상단에 있는 CounterInheritedWidget을 찾는 정적 메서드
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
