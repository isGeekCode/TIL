# Flutter - 화면 전환(Navigator)

---

## Navigator는 스택 구조
- Flutter에서 화면 이동은 Navigator를 통해 관리된다.
- Navigator는 내부적으로 스택 구조를 사용한다.
- push 하면 쌓이고, pop 하면 이전 화면으로 돌아간다.

<br><br>
---

## Navigator 주요 메서드

| 메서드 | 설명 | 뒤로가기 가능 여부 | 사용 예시 |
|--------|------|------------------|-----------|
| `push` | 현재 스택 위에 새 화면 추가 | 가능 | 일반 화면 전환 |
| `pushReplacement` | 현재 화면을 새 화면으로 교체 | 불가능 | 스플래시 종료 |
| `pushAndRemoveUntil` | 모든 이전 화면 제거 후 새 화면 push | 불가능 | 로그인 후 홈으로 이동 |
| `pop` | 현재 화면 제거 | 가능 | 뒤로가기 |

<br><br>
---

## push 계열 사용 예시

```dart
// push
Navigator.of(context).push(
  MaterialPageRoute(builder: (_) => const SecondPage()),
);

// pushReplacement
Navigator.of(context).pushReplacement(
  MaterialPageRoute(builder: (_) => const HomePage()),
);

// pushAndRemoveUntil
Navigator.of(context).pushAndRemoveUntil(
  MaterialPageRoute(builder: (_) => const HomePage()),
  (route) => false,
);
```

<br><br>
---

## 메서드 선택 기준

- `push`: 뒤로가기가 필요한 일반적인 전환
- `pushReplacement`: 이전 페이지가 불필요할 때
- `pushAndRemoveUntil`: 이전 내비게이션 기록 전체 제거가 필요할 때

---

## fullscreenDialog 옵션
- iOS 스타일로 아래서 위로 뜨는 모달 느낌
```dart
Navigator.of(context).push(
  MaterialPageRoute(
    builder: (_) => const SomePage(),
    fullscreenDialog: true,
  ),
);
```

<br><br>
---

## Android 물리 버튼과의 관계

- Android에서는 물리 '뒤로가기' 버튼이 `Navigator.pop()`을 호출한다.
- `pushReplacement`, `pushAndRemoveUntil`을 사용하면 뒤로 갈 화면이 없어 앱이 종료될 수 있다.

### WillPopScope 사용 예시

```dart
WillPopScope(
  onWillPop: () async {
    final shouldExit = await showDialog(
      context: context,
      builder: (_) => AlertDialog(
        title: Text('앱을 종료할까요?'),
        actions: [
          TextButton(onPressed: () => Navigator.pop(context, false), child: Text('아니오')),
          TextButton(onPressed: () => Navigator.pop(context, true), child: Text('예')),
        ],
      ),
    );
    return shouldExit ?? false;
  },
  child: Scaffold(
    body: Center(child: Text('홈')),
  ),
)
```

---

## HISTORY
- 260626: 초안 작성
