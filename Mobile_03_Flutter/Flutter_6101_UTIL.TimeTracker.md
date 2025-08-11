
# TimeTracker

`TimeTracker`는 코드 실행 시간을 측정하고 로그로 출력하는 싱글톤 클래스입니다.  
Flutter 앱 전체에서 하나의 인스턴스를 사용해 특정 코드 구간의 실행 시간을 손쉽게 측정할 수 있습니다.


```dart
/// [TimeTracker]
///
/// `start()`와 `end()` 호출 사이의 경과 시간을 추적하는 싱글톤 클래스입니다.
///
/// Usage:
/// TimeTracker.instance.start('Loading Data');
///  ... 측정할 코드 ...
/// TimeTracker.instance.end();
///
class TimeTracker {

  static final TimeTracker instance = TimeTracker._internal();

  int? _startTimeMillis;
  int? _endTimeMillis;
  String? _label;

  /// Private constructor.
  TimeTracker._internal();

  void start([String? label]) {
    _startTimeMillis = DateTime.now().millisecondsSinceEpoch;
    _label = label ?? '';
    _endTimeMillis = null;
  }

  void end([String? label]) {
    if (_startTimeMillis == null) {
      bLogger('Warning: TimeTracker.end() called before start()', 'TimeTracker');
      return;
    }
    // 초기화
    if (label != null) {
      if (_label != label) {
        bLogger('Warning: TimeTracker.end() label "$label" does not match started label "${_label ?? ''}"', 'TimeTracker');
        return;
      }
    }
    _endTimeMillis = DateTime.now().millisecondsSinceEpoch;
    final elapsed = _endTimeMillis! - _startTimeMillis!;
    final usedLabel = _label != null && _label!.isNotEmpty ? _label : 'operation';
    bLogger('Elapsed time for $usedLabel: ${elapsed}ms', 'TimeTracker');
    // Reset for next measurement
    _startTimeMillis = null;
    _endTimeMillis = null;
    _label = null;
  }
}

final tt = TimeTracker.instance;
```

## 4. 예제 UI 코드

```dart
import 'package:flutter/material.dart';
import 'dart:developer' as dev;

/// Example Flutter UI demonstrating TimeTracker usage.

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: const MainScreen(),
    );
  }
}

class MainScreen extends StatefulWidget {
  const MainScreen({super.key});

  @override
  State<MainScreen> createState() => _MainScreenState();
}

class _MainScreenState extends State<MainScreen> {
  void _startPressed() {
    tt.start('Test Operation');
  }

  void _endPressed() {
    tt.end('Test Operation');
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('TimeTracker Example'),
      ),
      floatingActionButtonLocation: FloatingActionButtonLocation.centerFloat,
      floatingActionButton: Row(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          FloatingActionButton(
            heroTag: 'startBtn',
            onPressed: _startPressed,
            backgroundColor: Colors.green,
            child: const Icon(Icons.play_arrow),
          ),
          const SizedBox(width: 16),
          FloatingActionButton(
            heroTag: 'endBtn',
            onPressed: _endPressed,
            backgroundColor: Colors.red,
            child: const Icon(Icons.stop),
          ),
        ],
      ),
    );
  }
}
```

---

## HISTORY

- 250811: 최초 작성 및 기본 기능 구현 
