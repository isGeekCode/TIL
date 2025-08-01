# Flutter Navigator 1.0 - Push & Pop

## 개요

Navigator는 Flutter의 화면 전환을 담당하는 핵심 위젯이다.  
그중 Navigator 1.0은 Stack 구조를 기반으로 명령형 방식의 화면 전환을 제공한다.  
화면을 push하여 쌓고, pop하여 되돌아가는 방식으로 작동한다.

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

// 새로운 화면으로 이동
Navigator.push(
  context,
  MaterialPageRoute(builder: (_) => SecondScreen()),
);

// 현재 화면 종료 후 이전 화면으로 복귀
Navigator.pop(context); 
```

위 코드에서 사용된 주요 구성 요소는 다음과 같다:

- `context`: 현재 위젯의 위치 정보를 담고 있는 객체로, `Navigator`, `Theme`, `MediaQuery` 등 상위 위젯 트리에 접근할 수 있게 해준다.  
  특히 `Navigator`는 위젯 트리상에서 가장 가까운 `Navigator` 인스턴스를 찾아 해당 위치에서 화면 전환을 수행하게 된다.  
  따라서 올바른 `context`를 사용하는 것이 매우 중요하며, 잘못된 위치의 context를 사용할 경우 원하는 동작이 되지 않을 수 있다.
- `MaterialPageRoute`: 전환 애니메이션과 함께 새로운 화면(Route)을 생성하는 Flutter의 기본 Route 구현체이다.
- `builder`: 새로운 화면을 구성하는 위젯을 반환하는 함수이며, 여기서는 `SecondScreen()`을 반환한다.

<br><br>

## 데이터 전달

Navigator 1.0은 화면을 이동하면서 두 가지 방식으로 화면 간 데이터를 전달할 수 있다.

### 1. 생성한 페이지로 데이터 넘기기
새로운 화면을 생성하면서 데이터를 전달하고자 할 때는, `MaterialPageRoute`를 통해 `builder`에서 위젯을 생성할 때 **생성자 인자**로 넘겨준다.


```dart
// MainScreen → DetailScreen으로 데이터 전달

Navigator.push(
  context,
  MaterialPageRoute(
    builder: (_) => DetailScreen(title: '상세 페이지'),
  ),
);


// 전달받는 화면 (DetailScreen)
class DetailScreen extends StatelessWidget {
  final String title;
  const DetailScreen({required this.title});
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(title)),
      body: Center(child: Text('전달받은 값: $title')),
    );
  }
}
```
이 방식은 주로 화면 초기 상태 설정이나 표시할 내용을 외부에서 넘길 때 사용된다.


<br><br>

### 2. 복귀할 페이지로 데이터 반환하기
새로운 화면에서 어떤 값을 선택하거나 처리한 후, 그 결과를 이전 화면으로 전달해야 할 때 사용합니다.  
주로 선택 결과, 입력 값, 사용자 행동 결과 등을 이전 화면에서 받아 활용하는 용도로 쓰입니다.

예를 들어, 옵션 선택 화면에서 사용자가 항목을 선택하면  
`Navigator.pop(context, 선택한값)`을 통해 이전 화면에 그 값을 전달할 수 있습니다.
이전 화면은 `await Navigator.push(...)`를 통해 이 값을 기다리고, 후속 처리를 할 수 있습니다.


```dart
// 결과를 넘기는 화면 (예: ResultScreen)
Navigator.pop(context, '선택한 값');

// 결과를 받는 화면 (예: MainScreen)
final result = await Navigator.push(
  context,
  MaterialPageRoute(builder: (_) => ResultScreen()),
);

if (result != null) {
  ScaffoldMessenger.of(context).showSnackBar(
    SnackBar(content: Text('받은 값: $result')),
  );
}
```

result의 null 체크가 없으면 네비게이션의 백버튼을 눌러서 이동할 땐, 값 전달이 null로 들어가게 된다.  


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

## 🧪 Navigator 샘플 코드 모음

```dart
// 1️⃣ 새로운 화면으로 이동하는 기본 예제
ElevatedButton(
  onPressed: () {
    Navigator.push(
      context,
      MaterialPageRoute(builder: (_) => SecondScreen()),
    );
  },
  child: Text('1. 기본 Push'),
),

// 2️⃣ 값을 되돌려 받는 예제 (pop으로 결과 전달)
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

// 3️⃣ 현재 화면을 새로운 화면으로 대체 (뒤로 못 감)
ElevatedButton(
  onPressed: () {
    Navigator.pushReplacement(
      context,
      MaterialPageRoute(builder: (_) => ReplacementScreen()),
    );
  },
  child: Text('3. Push Replacement'),
),

// 4️⃣ 모든 이전 화면을 제거하고 새 화면으로 이동
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

// ✅ SecondScreen.dart
// 👉 단순 push로 이동한 예제 화면
class SecondScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('SecondScreen')),
      body: Center(child: Text('이 화면은 단순히 push로 이동한 화면입니다')),
    );
  }
}

// ✅ ResultScreen.dart
// 👉 값을 선택해 되돌려주는 예제 화면
class ResultScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('ResultScreen')),
      body: Center(
        child: ElevatedButton(
          onPressed: () {
            Navigator.pop(context, '🎯 결과 도착');
          },
          child: Text('결과 전달 후 복귀'),
        ),
      ),
    );
  }
}

// ✅ ReplacementScreen.dart
// 👉 현재 화면을 새로운 화면으로 대체하는 예제
class ReplacementScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('ReplacementScreen')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('이 화면은 이전 화면을 대체한 상태입니다.'),
            SizedBox(height: 16),
            ElevatedButton(
              onPressed: () {
                Navigator.pushReplacement(
                  context,
                  MaterialPageRoute(builder: (_) => MainScreen()),
                );
              },
              child: Text('초기화 버튼 (MainScreen으로 돌아가기)'),
            ),
          ],
        ),
      ),
    );
  }
}

// ✅ HomeScreen.dart
// 👉 모든 이전 화면을 제거한 후 이동하는 초기화 예제
class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('HomeScreen')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('이 화면은 모든 이전 화면이 제거된 상태입니다.'),
            SizedBox(height: 16),
            ElevatedButton(
              onPressed: () {
                Navigator.pushAndRemoveUntil(
                  context,
                  MaterialPageRoute(builder: (_) => MainScreen()),
                  (route) => false,
                );
              },
              child: Text('초기화 버튼 (MainScreen으로 돌아가기)'),
            ),
          ],
        ),
      ),
    );
  }
}
```

<br><br>

## 🧩 연습 문제

다음 시나리오에 따라 Navigator 1.0을 활용한 화면 전환 기능을 구현하라.

<br><br>

### 시나리오

MainScreen에서는 사용자에게 색상 선택 버튼을 보여준다.  
버튼을 누르면 ColorPickerScreen으로 이동하고, 거기서 색상을 선택하면 다시 MainScreen으로 돌아온다.  
선택한 색상은 MainScreen의 SnackBar로 표시된다.


<br><br>

### 요구사항

- `MainScreen` → `ColorPickerScreen`으로 `Navigator.push()`
- `ColorPickerScreen`에서는 "Red", "Blue", "Green" 버튼 중 하나를 누르면 `Navigator.pop(context, '색상')` 호출
- `MainScreen`에서는 `await`으로 반환된 값을 받아 `SnackBar`에 출력


<br><br>

### 예시 흐름

MainScreen → ColorPickerScreen → 색상 선택 후 pop() → MainScreen으로 결과 반환

<br>

## History
- 250731 : 초안작성
- 250801 : pop동작 작성
