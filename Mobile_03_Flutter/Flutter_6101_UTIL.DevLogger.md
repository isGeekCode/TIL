
# bLogger


`bLogger`는 호출 스택 정보를 분석해 현재 시간, 파일명, 라인 번호, 클래스명, 메서드명과 함께 로그를 출력하는 함수입니다.  
Flutter 프로젝트에서 로그의 가독성을 높이고, 로그 위치 정보를 자동으로 포함시켜 디버깅을 쉽게 할 수 있도록 돕습니다.

- 로그 포맷 예시:  
  ```
  12:34:56|main.dart:15|MyClass|myMethod| - 메시지 내용
  ```

## 예제 코드

```dart
/// [bLogger]
///
/// 호출 스택을 분석해 현재 시간, 파일명, 라인 번호, 클래스명, 메서드명을 포함한 로그를 출력합니다.
///
/// - [message]: 로그 뒤에 추가로 출력할 메시지 (없으면 기본 정보만 표시)
/// - [name]: DevTools에서 필터링할 때 사용할 로그 이름 (기본값 `'bLogger'`)
///
/// 사용 예시:
/// bLogger(); // 기본 정보 출력
/// bLogger('데이터 로드 완료'); // 메시지 포함 출력
///
/// DevTools에서 name 필터로 `'bLogger'`를 선택하면 해당 로그만 볼 수 있습니다.
void bLogger([String? message, String name = 'bLogger']) {
  // 현재 시간을 시:분:초 형식으로 포맷팅
  final now = DateTime.now();
  final timeStr =
      "${now.hour.toString().padLeft(2, '0')}:${now.minute.toString().padLeft(2, '0')}:${now.second.toString().padLeft(2, '0')}";

  // 현재 호출 스택을 문자열로 가져와 줄 단위로 분리
  final frames = StackTrace.current.toString().split('\n');

  if (frames.length > 1) {
    final frame = frames[1];
    // 예: #1      myFunction (package:my_app/main.dart:15:5)
    // 정규식은 호출 스택의 두 번째 줄에서 메서드명, 파일 경로, 라인 번호를 추출
    final regex = RegExp(r'#1\s+(.+) \((.+):(\d+):\d+\)');
    final match = regex.firstMatch(frame);

    if (match != null) {
      String methodName = match.group(1) ?? '';
      final filePath = match.group(2) ?? '';
      final lineNumber = match.group(3) ?? '';
      final fileName = filePath.split('/').last;

      // 익명 클로저 표기인 '.<anonymous closure>'를 제거해서 가독성 향상
      methodName = methodName.replaceAll('.<anonymous closure>', '').trim();

      // 클래스명과 메서드명을 분리 (예: ClassName.methodName)
      String className = '';
      String realMethodName = methodName;
      if (methodName.contains('.')) {
        final parts = methodName.split('.');
        className = parts[0];
        realMethodName = parts.sublist(1).join('.');
      }
      // 로그 메시지 포맷 구성: 시간|파일명:라인번호|클래스명|메서드명|메시지
      String logBase;
      if (className.isNotEmpty) {
        logBase = "$timeStr|$fileName:$lineNumber|$className|$realMethodName|";
      } else {
        logBase = "$timeStr|$fileName:$lineNumber|$realMethodName|";
      }
      final logText = message != null ? "$logBase - $message" : logBase;
      // 실제 로그 출력: DevTools에서 name 필터를 사용해 필터링 가능
      dev.log(logText, name: name);

      return;
    }
  }

  // 파싱 실패 시 기본 로그 출력 (시간과 메시지만 표시)
  final fallbackBase = "[$timeStr]";
  final fallbackText = message != null ? "$fallbackBase - $message" : fallbackBase;
  dev.log(fallbackText, name: name);
}
```

<BR><BR>

---

# TimeTracker

`TimeTracker`는 코드 실행 시간을 측정하고 로그로 출력하는 싱글톤 클래스입니다.  
Flutter 앱 전체에서 하나의 인스턴스를 사용해 특정 코드 구간의 실행 시간을 손쉽게 측정할 수 있습니다.


```dart
/// [TimeTracker]
///
/// Singleton class for tracking elapsed time between `start()` and `end()` calls.
///
/// Usage:
/// TimeTracker.instance.start('Loading Data');
/// // ... code to measure ...
/// TimeTracker.instance.end();
///
class TimeTracker {
  /// The singleton instance of [TimeTracker].
  static final TimeTracker instance = TimeTracker._internal();

  int? _startTimeMillis;
  int? _endTimeMillis;
  String? _label;

  /// Private constructor.
  TimeTracker._internal();

  /// Starts tracking time.
  ///
  /// Optionally provide a [label] for the operation being measured.
  ///
  void start([String? label]) {
    _startTimeMillis = DateTime.now().millisecondsSinceEpoch;
    _label = label ?? '';
    _endTimeMillis = null;
  }

  /// Ends tracking and logs the elapsed time in milliseconds using [bLogger].
  ///
  /// If called before [start()], logs a warning.
  /// If [label] is provided, only ends if it matches the stored label.
  void end([String? label]) {
    if (_startTimeMillis == null) {
      bLogger('Warning: TimeTracker.end() called before start()', 'TimeTracker');
      return;
    }
    // If a label is provided, check if it matches the stored label
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
