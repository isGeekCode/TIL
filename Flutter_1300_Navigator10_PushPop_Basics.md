# 🧭 Flutter Navigator 1.0 - Push & Pop

## 🔰 개요

Navigator는 Flutter의 기본 내비게이션 도구입니다. Navigator 1.0은 명령형 Stack 기반으로 화면을 쌓고 제거하는 방식입니다.

## 🧩 동작 원리

- `Navigator`는 내부적으로 `Stack<Route>` 구조로 라우트를 관리합니다.
- `push()`는 새 페이지를 추가하고, `pop()`은 현재 페이지를 제거합니다.
- 전환은 `MaterialPageRoute`로 처리하며, 애니메이션이 포함됩니다.

## 🛠 주요 메서드

| 메서드 | 설명 |
|--------|------|
| `push()` | 새 화면을 Stack 위에 추가 |
| `pop()` | 현재 화면을 제거하고 이전 화면으로 이동 |
| `pushReplacement()` | 현재 화면을 대체 |
| `pushAndRemoveUntil()` | 모든 화면을 제거하고 새 화면을 시작점으로 설정 |
| `MaterialPageRoute` | 애니메이션 포함 Route 생성자 |

## 🧪 실습 예제 요약

각 Navigator 동작을 실습할 수 있는 버튼 목록입니다.

```dart
ElevatedButton(...); // 기본 push
ElevatedButton(...); // pop with result
ElevatedButton(...); // pushReplacement
ElevatedButton(...); // pushAndRemoveUntil
```

## 🧠 사용 시나리오

| 상황 | 처리 방식 | 설명 |
|------|-----------|------|
| 상세 페이지 이동 | `push()` | 간단한 전환 |
| 데이터 반환 후 복귀 | `pop(result)` | 결과 전달 |
| 로그인 이후 홈으로 | `pushReplacement()` | 로그인 화면 제거 |
| 온보딩 이후 초기화 | `pushAndRemoveUntil()` | 모든 화면 제거 후 홈 |

## 💬 화면 간 복귀 설명

- 각 화면에서 어떤 방식으로 돌아오는지 텍스트로 표시됨
- pop: 이전 화면 자동 복귀
- pushReplacement: 이전 화면 제거, 새 화면 추가
- pushAndRemoveUntil: 모든 Stack 제거 → 초기화

## 💡 Navigator 2.0과의 차이

| 항목 | Navigator 1.0 | Navigator 2.0 |
|------|---------------|---------------|
| 방식 | 명령형 (imperative) | 선언형 (declarative) |
| 구조 | Stack API 호출 | 상태 기반 라우팅 |
| 사용 용도 | 간단한 앱 | 복잡한 URL 대응, 웹 |

## 🔗 참고 자료

- [Flutter 공식 문서](https://docs.flutter.dev/ui/navigation)

---

## 🧾 전체 예제 코드

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: MainScreen(),
    );
  }
}

class MainScreen extends StatelessWidget {
  const MainScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Navigator 1.0 예제')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            ElevatedButton(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (_) => SecondScreen()),
                );
              },
              child: Text('1. 기본 Push'),
            ),
            ElevatedButton(
              onPressed: () async {
                final result = await Navigator.push(
                  context,
                  MaterialPageRoute(builder: (_) => ResultScreen()),
                );
                ScaffoldMessenger.of(context).showSnackBar(
                  SnackBar(content: Text('받은 값: $result')),
                );
              },
              child: Text('2. Pop with Result'),
            ),
            ElevatedButton(
              onPressed: () {
                Navigator.pushReplacement(
                  context,
                  MaterialPageRoute(builder: (_) => ReplacementScreen()),
                );
              },
              child: Text('3. Push Replacement'),
            ),
            ElevatedButton(
              onPressed: () {
                Navigator.pushAndRemoveUntil(
                  context,
                  MaterialPageRoute(builder: (_) => HomeScreen()),
                  (route) => false,
                );
              },
              child: Text('4. Push And Remove Until'),
            ),
          ],
        ),
      ),
    );
  }
}

class SecondScreen extends StatelessWidget {
  const SecondScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Second Screen')),
      body: Center(
        child: Text('📄 기본 push로 이동한 화면입니다\n\n뒤로 가기 버튼 또는 Navigator.pop()으로 복귀'),
      ),
    );
  }
}

class ResultScreen extends StatelessWidget {
  const ResultScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Pop with Result')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('📤 값을 반환하며 pop\n\npop 시 MainScreen으로 결과 전달'),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                Navigator.pop(context, '👍 결과 반환');
              },
              child: Text('결과 반환하고 복귀'),
            ),
          ],
        ),
      ),
    );
  }
}

class ReplacementScreen extends StatelessWidget {
  const ReplacementScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Push Replacement')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('🔄 이전 화면을 대체하고 Main으로 이동\n\npushReplacement 사용'),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                Navigator.pushReplacement(
                  context,
                  MaterialPageRoute(builder: (_) => MainScreen()),
                );
              },
              child: Text('Main으로 돌아가기'),
            ),
          ],
        ),
      ),
    );
  }
}

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Push and Remove Until')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('🧹 모든 이전 화면 제거 후 Main으로 이동\n\npushAndRemoveUntil 사용'),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                Navigator.pushAndRemoveUntil(
                  context,
                  MaterialPageRoute(builder: (_) => MainScreen()),
                  (route) => false,
                );
              },
              child: Text('Main으로 돌아가기'),
            ),
          ],
        ),
      ),
    );
  }
}
```
