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




## 실습 과제 1. 간단한 카운터앱
1. 간단한 카운터 앱을 만들어 버튼 클릭 시 숫자가 증가하도록 구현하세요.
2. 위젯을 분리하여 상태 변경이 발생하지 않는 부분은 다시 빌드되지 않도록 최적화해보세요.
3. 비동기 작업(예: 버튼 클릭 후 2초 후 상태 변경) 후 `setState` 호출 시 위젯이 언마운트된 경우를 처리하는 코드를 작성해보세요.

<br><br>

## 실습 과제 2. : 다양한 state 사용한 Counter

두 개의 counter 변수를 갖고 화면 업데이트하기

```dart
class MainScreen extends StatefulWidget {
  const MainScreen({super.key});

  @override
  State<MainScreen> createState() => _MainScreenState();
}

class _MainScreenState extends State<MainScreen> {
  int counter = 0;
  int counter2 = 0;

  void _updateCounter(int rowNum, int delta) {
    setState(() {
      if (rowNum == 0) {
        counter = (counter + delta).clamp(0, 5);
      } else {
        counter2 = (counter2 + delta).clamp(0, 5);
      }
    });
  }

  bool _isMaximumed(int counterNum) {
    return counterNum >= 5;
  }

  bool _isMinimumed(int counterNum) {
    return counterNum <= 0;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Main')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('Counter 1 is $counter'),
            Text('Counter 2 is $counter2'),
          ],
        ),
      ),
      floatingActionButtonLocation: FloatingActionButtonLocation.endFloat,
      floatingActionButton: Column(
        mainAxisSize: MainAxisSize.min,
        mainAxisAlignment: MainAxisAlignment.end,

        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.end,
            children: [
              FloatingActionButton(
                backgroundColor: _isMaximumed(counter)
                    ? Colors.grey
                    : Theme.of(context).colorScheme.primaryContainer,
                onPressed: _isMaximumed(counter)
                    ? null
                    : () => _updateCounter(0, 1),
                child: Icon(
                  Icons.add,
                  color: _isMaximumed(counter)
                      ? Colors.white
                      : Theme.of(context).colorScheme.secondary,
                ),
              ),
              SizedBox(width: 40),

              FloatingActionButton(
                backgroundColor: _isMinimumed(counter)
                    ? Colors.grey
                    : Theme.of(context).colorScheme.primaryContainer,
                onPressed: _isMinimumed(counter)
                    ? null
                    : () => _updateCounter(0, -1),
                child: Icon(
                  Icons.remove,
                  color: _isMinimumed(counter)
                      ? Colors.white
                      : Theme.of(context).colorScheme.secondary,
                ),
              ),
            ],
          ),

          SizedBox(height: 40),

          Row(
            mainAxisAlignment: MainAxisAlignment.end,
            children: [
              FloatingActionButton(
                backgroundColor: _isMaximumed(counter2)
                    ? Colors.grey
                    : Theme.of(context).colorScheme.primaryContainer,
                onPressed: _isMaximumed(counter2)
                    ? null
                    : () => _updateCounter(1, 1),
                child: Icon(
                  Icons.add,
                  color: _isMaximumed(counter2)
                      ? Colors.white
                      : Theme.of(context).colorScheme.secondary,
                ),
              ),
              SizedBox(width: 40),

              FloatingActionButton(
                backgroundColor: _isMinimumed(counter2)
                    ? Colors.grey
                    : Theme.of(context).colorScheme.primaryContainer,
                onPressed: _isMinimumed(counter2)
                    ? null
                    : () => _updateCounter(1, -1),
                child: Icon(
                  Icons.remove,
                  color: _isMinimumed(counter2)
                      ? Colors.white
                      : Theme.of(context).colorScheme.secondary,
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
/Users/banghyeonseok/Library/Mobile\ Documents/iCloud~md~obsidian/Documents/TIL_Server/TIL

```




## 실습과제 3. 다양한 state 사용한 Counter

### 목표


5초 동안만 카운터를 조작할 수 있는 앱 만들기.

---

### **기능 조건**

1. **counter** 초기값은 0.
2. **시작 버튼**을 누르면:
	- counter를 0으로 초기화.
    - 남은 시간을 5초로 설정.
    - 5초 동안 “증가 버튼” 활성화.    
3. 5초가 지나면:
    - “증가 버튼” 비활성화.
    - 남은 시간이 0으로 표시.
4. 화면에 표시할 내용:
    - 현재 counter 값.
    - 남은 시간(초).
5. “증가 버튼”의 동작: 누를 때마다 counter +1.
6. setState로 상태를 갱신.



```dart


class MainScreen extends StatefulWidget {
  const MainScreen({super.key});

  @override
  State<MainScreen> createState() => _MainScreenState();
}

class _MainScreenState extends State<MainScreen> {
  int sum = 0;
  int remainSeconds = 5;

  bool isValid = false;

  Timer? _timer;

  void _increment() {
    setState(() {
      sum++;
    });
  }

  void _startTimer() {
    print('start');

    _stopTimer();
    setIncrementValid();
    _timer = Timer.periodic(Duration(seconds: 1), (timer) {
      setState(() {
        remainSeconds--;
        if (remainSeconds <= 0) {
          _stopTimer();
          remainSeconds = 5;
          sum = 0;
        }
      });
      print("Timer!! $remainSeconds");
    });
  }

  void setIncrementValid() => updateIsValid(true);
  void setIncrementInvalid() => updateIsValid(false);

  void updateIsValid(bool value) => setState(() => isValid = value);


  void _stopTimer() {
    if (_timer != null && _timer!.isActive) {
      print('기존 timer stop');
      setIncrementInvalid();
      _timer?.cancel();
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('Counter is $sum'),
            Text('남은 시간 : $remainSeconds초'),

            SizedBox(height: 30),

            ElevatedButton(
              onPressed: !isValid ? null : _increment,
              child: Text('Increase'),
            ),

            SizedBox(height: 30),

            ElevatedButton(
              onPressed: _startTimer,
              child: Text('start'),
            ),
          ],
        ),
      ),
    );
  }
}

```
