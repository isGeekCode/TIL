# Flutter Navigator 1.0 - Push & Pop

## 개요

Navigator는 Flutter의 화면 전환을 담당하는 핵심 위젯이다.  
Navigator 1.0은 Stack 구조를 기반으로 명령형 방식의 화면 전환을 제공한다.  
즉, 화면을 push하여 쌓고, pop하여 되돌아가는 방식으로 작동한다.

각각의 화면은 `Route` 객체로 관리되며, `Route`는 단순히 "하나의 화면"을 의미한다.  
Navigator는 여러 개의 Route를 Stack처럼 쌓아서, 가장 위에 있는 화면을 보여준다.

Flutter에는 이 외에도 선언형 방식의 `Navigator 2.0`이 존재한다.  
이는 앱 상태와 URL을 함께 다루기 위한 방식으로, 웹이나 복잡한 내비게이션이 필요한 경우에 적합하다.  
본 문서에서는 기본 구조인 Navigator 1.0을 중심으로 설명한다.

<br><br>

## 동작 원리

- Navigator는 내부적으로 `Stack<Route>`을 유지한다.
- 새로운 화면을 보여줄 때는 `push()`를 통해 Route를 Stack에 추가한다.
- 이전 화면으로 돌아갈 때는 `pop()`을 사용하여 Stack에서 Route를 제거한다.
- Route는 `MaterialPageRoute`를 통해 생성한다.


<br><br>

## 주요 메서드

| 메서드 | 설명 |
|--------|------|
| `push()` | 새 Route를 Stack 위에 추가 |
| `pop()` | 현재 Route를 Stack에서 제거 |
| `pushReplacement()` | 현재 Route를 새로운 Route로 대체 |
| `pushAndRemoveUntil()` | 조건에 따라 기존 Route들을 제거한 후 새로운 Route로 이동 |
| `MaterialPageRoute` | 전환 애니메이션 포함 기본 Route 구현체 |

<br><br>

## 📦 예제 코드

```dart
Navigator.push(
  context,
  MaterialPageRoute(builder: (_) => SecondScreen()),
);
```

위 코드에서 사용된 주요 구성 요소는 다음과 같다:

- `context`: 현재 위젯의 위치 정보를 담고 있는 객체로, Navigator가 어떤 위치에서 동작해야 하는지를 알려준다.
- `MaterialPageRoute`: 전환 애니메이션과 함께 새로운 화면(Route)을 생성하는 Flutter의 기본 Route 구현체이다.
- `builder`: 새로운 화면을 구성하는 위젯을 반환하는 함수이며, 여기서는 `SecondScreen()`을 반환한다.

```dart
Navigator.pop(context, 'result');
```

<br><br>

## 🧪 실습 예제 요약

다음 예제는 Navigator 1.0의 기본 동작을 직접 체험할 수 있도록 구성되어 있다.

- `push()`: 새로운 화면으로 이동
- `pop()`: 현재 화면 제거 후 이전 화면으로 복귀
- `pushReplacement()`: 현재 화면을 제거하고 새 화면으로 전환
- `pushAndRemoveUntil()`: 모든 이전 화면을 제거하고 새 화면을 시작점으로 설정

```dart
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
    
	if (result != null) {  
	  ScaffoldMessenger.of(context).showSnackBar(  
	    SnackBar(content: Text('받은 값: $result')),  
	  );  
	}
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
```


<br><br>

## 🔄 복귀 동작 비교

| 방법 | 복귀 방식 | 특징 |
|------|-----------|------|
| `pop()` | 이전 화면으로 되돌아감 | Stack에서 현재 Route 제거 |
| `pushReplacement()` | 이전 화면 제거 후 새 화면 표시 | 복귀 불가 |
| `pushAndRemoveUntil()` | 모든 이전 화면 제거 후 새 화면 표시 | 완전 초기화 용도 |

<br><br>


## 💡 실전 사용 예시

| 상황 | 메서드 | 설명 |
|------|--------|------|
| 로그인 성공 후 홈으로 이동 | `pushReplacement()` | 로그인 화면 제거 |
| 온보딩 완료 후 앱 시작 화면으로 이동 | `pushAndRemoveUntil()` | 초기화 후 홈으로 이동 |
| 팝업 후 결과 반환 | `pop(result)` | 이전 화면에 결과 전달 |


<br><br>

## 🔗 참고 자료

- [Flutter 공식 문서 - Navigation and Routing](https://docs.flutter.dev/ui/navigation)


<br><br>

## History
- 250731 : 초안작성
