# Flutter setState 기본 개념과 활용법


<br>


## 개요
Flutter에서 상태 관리를 위한 기본 메커니즘인 `setState`의 개념과 사용법을 학습합니다.

상태 변경에 따른 UI 갱신 과정, 최소 빌드 영역 설정 방법, 그리고 StatefulWidget 내부에서 `setState`를 사용할 때 주의해야 할 점들을 이해하고, 간단한 카운터 예제와 위젯 분리를 통한 최적화 예제를 통해 실습합니다.

<br><br>



## 시작하기 전에 알아두면 좋은 것들
- Flutter는 선언적 UI 프레임워크로, 상태가 변경되면 UI를 다시 그려야 합니다.
- `StatefulWidget`과 `StatelessWidget`의 차이와 역할을 이해하고 있어야 합니다.
- `setState`는 `StatefulWidget`의 상태를 변경하고 UI를 갱신하는 기본 메서드입니다.
- 불필요한 빌드를 줄이기 위해 빌드 영역을 최소화하는 방법이 중요합니다.

<br><br>

---

## 개념 정리


### 1. setState 기본 개념
- `setState`는 `StatefulWidget`의 상태를 변경하고, 변경된 상태를 기반으로 UI를 다시 빌드하도록 플러터에게 알리는 메서드입니다.
- `setState` 내부에서 상태를 변경한 후 호출해야 하며, 호출 시 프레임워크는 `build` 메서드를 다시 실행합니다.

<br><br>

---

### 2. 상태 변경과 UI 갱신 과정
- 상태가 변경되면 `setState`가 호출되고, 플러터는 해당 위젯의 `build` 메서드를 호출하여 UI를 갱신합니다.
- 이 과정은 매우 빠르며, 변경된 부분만 다시 그려집니다.

<br><br>

---

### 3. 최소 빌드 영역 설정
- `setState`를 호출하면 해당 `State` 객체의 `build` 메서드가 다시 실행됩니다.
- 따라서 상태 변경에 영향을 받는 위젯만 분리하여 최소 영역만 빌드하도록 설계하는 것이 성능 최적화에 중요합니다.

<br><br>

---

### 4. StatefulWidget 내부에서 setState 사용 시 주의사항
- `setState`는 반드시 `State` 객체 내에서 호출해야 하며, 위젯이 마운트된 상태에서만 호출해야 합니다.
- 비동기 작업 후 `setState` 호출 시 위젯이 이미 언마운트된 경우 예외가 발생할 수 있으므로 `mounted` 속성을 확인하는 것이 좋습니다.

<br><br>

---

## 예제 코드


### 1. 간단한 카운터 예제 (버튼 클릭 시 값 증가)
```dart
import 'package:flutter/material.dart';

class CounterApp extends StatefulWidget {
  @override
  _CounterAppState createState() => _CounterAppState();
}

class _CounterAppState extends State<CounterApp> {
  int _count = 0;

  void _incrementCounter() {
    setState(() {
      _count++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('간단한 카운터 예제'),
      ),
      body: Center(
        child: Text(
          '클릭 횟수: $_count',
          style: TextStyle(fontSize: 24),
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        child: Icon(Icons.add),
      ),
    );
  }
}
```

<br><br>

---

### 2. 위젯 분리를 통한 최소 빌드 영역 제어 예제
```dart
import 'package:flutter/material.dart';

class OptimizedCounterApp extends StatefulWidget {
  @override
  _OptimizedCounterAppState createState() => _OptimizedCounterAppState();
}

class _OptimizedCounterAppState extends State<OptimizedCounterApp> {
  int _count = 0;

  void _incrementCounter() {
    setState(() {
      _count++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('최소 빌드 영역 제어 예제'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            StaticTextWidget(),
            CounterText(count: _count),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        child: Icon(Icons.add),
      ),
    );
  }
}

class StaticTextWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    print('StaticTextWidget 빌드');
    return Text(
      '이 텍스트는 상태 변경에 영향을 받지 않습니다.',
      style: TextStyle(fontSize: 18),
    );
  }
}

class CounterText extends StatelessWidget {
  final int count;

  const CounterText({Key? key, required this.count}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    print('CounterText 빌드');
    return Text(
      '클릭 횟수: $count',
      style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
    );
  }
}
```

<br><br>

---

## 실무 적용 포인트
- 상태 변경이 UI에 미치는 영향을 명확히 파악하고, 불필요한 빌드를 줄이기 위해 위젯을 분리하세요.
- `setState`는 간단한 상태 관리에 적합하며, 복잡한 상태 관리가 필요할 경우 Provider, Bloc 등 다른 상태 관리 라이브러리를 고려하세요.
- 비동기 작업 후 `setState` 호출 시 위젯이 마운트 상태인지 확인하여 예외를 방지하세요.

<br><br>

---

## 요약 정리
- `setState`는 StatefulWidget의 상태를 변경하고 UI를 갱신하는 기본 메서드입니다.
- 상태 변경 시 `build` 메서드가 다시 실행되어 UI가 업데이트됩니다.
- 최소 빌드 영역을 설계하여 성능 최적화를 할 수 있습니다.
- `setState` 호출 시 위젯의 마운트 상태를 확인하는 것이 안전합니다.

<br><br>
---


## 실습 과제
1. 간단한 카운터 앱을 만들어 버튼 클릭 시 숫자가 증가하도록 구현하세요.
2. 위젯을 분리하여 상태 변경이 발생하지 않는 부분은 다시 빌드되지 않도록 최적화해보세요.
3. 비동기 작업(예: 버튼 클릭 후 2초 후 상태 변경) 후 `setState` 호출 시 위젯이 언마운트된 경우를 처리하는 코드를 작성해보세요.

<br><br>

---

## HISTORY
- 2024-06-XX: Flutter setState 기본 개념 및 활용법 문서 작성 및 예제 추가.
