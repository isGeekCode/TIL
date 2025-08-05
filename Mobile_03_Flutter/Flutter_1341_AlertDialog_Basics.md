# AlertDialog 기초 사용법


<img src="https://i.imgur.com/0YN1ZWx.png" width="500" />

<br><br>

## 1. 개요

AlertDialog는 사용자의 명확한 응답을 유도하거나, 중요한 정보를 전달할 때 사용하는 모달 다이얼로그 위젯이다.
Flutter에서는 Material 디자인 시스템에 속하며, 확인, 취소, 경고 등의 상황에서 가장 기본적으로 사용되는 대화 상자다.

본 문서에서는 다음 내용을 중심으로 AlertDialog를 다룬다

- 기본 생성 방식 (showDialog와 AlertDialog의 관계)
- 버튼 구성 및 사용자 선택 처리
- 위젯 분리 방식 (함수, 클래스, 유틸 함수)
- Navigator와의 관계 및 결과 반환 처리
- iOS/Android OS 별 다이얼로그 대응 (CupertinoAlertDialog 포함)

iOS에서는 UIAlertController, Android에서는 Dialog가 각각 대응된다.
Flutter에서는 이들을 AlertDialog 또는 CupertinoAlertDialog로 통합하여 사용할 수 있다.

<br><br>

---

## 2. 시작 전에 알아두면 좋은 것들

- 다이얼로그는 내부적으로 Navigator를 통해 화면 위에 새로운 팝업 레이어를 띄우는 방식이다.
- `showDialog()`는 현재 화면 위에 다이얼로그를 표시하기 위해 `BuildContext`를 파라미터로 받는다.  
  이는 내부적으로 `Navigator.of(context).push(...)`를 통해 다이얼로그를 새로운 route로 추가하기 때문이다.
- `showDialog()` 함수는 `Future`를 반환한다. 이는 사용자의 선택 결과가 나중에 도착함을 의미하며, `await`을 통해 해당 결과를 기다릴 수 있다.
- AlertDialog는 내부적으로 `Dialog` 위젯을 기반으로 하고, `title`, `content`, `actions` 등의 속성을 제공한다.


<br><br>

---

## 3. 기본 구조
Dialog는 기본적으로 두단계를 걸쳐서 사용한다. 
- 1단계 : showDialog 메서드로 Dialog를 띄우는 부분
- 2단계 : AlertDialog : UI를 구현하는 부분

<br>

### showDialog
다이얼로그를 화면에 **표시**해주는 함수이다.  
Flutter에서는 `Material` 환경에서 해당 메서드에 접근할 수 있으며, 내부적으로 `Navigator`를 사용해 다이얼로그를 새로운 Route로 push하는 방식으로 동작한다.

- `context`는 현재 위젯의 위치를 전달하는 필수 파라미터이다. 이 정보는 `Navigator`가 현재 위젯 트리에서 어디에 다이얼로그를 추가할지 결정하는 데 사용된다.
- `builder`는 `BuildContext`를 인자로 받아 `AlertDialog` 등 다이얼로그 UI를 반환하는 함수이다.


아래 코드는 최소 구성으로 AlertDialog를 띄우는 방식이다.   
`builder:`는 `BuildContext`를 매개로 하는 함수이며, `AlertDialog`를 반환해야 한다.
```dart

// ✅ 완전 기본 사용 예
showDialog(
  context: context,
  builder: (context) => AlertDialog(),
);

// 혹은 
showDialog(
  context: context,
  builder: (context) {
    return AlertDialog();
  },
);
```

<br><br>

### AlertDialog
실제 다이얼로그의 UI를 구성하는 위젯이다.  
기본적으로 배경은 Dim 처리되며, 회색 처리된 바깥 영역을 탭하면 다이얼로그는 자동으로 닫힌다.

- 일반적으로 `title`과 `content`에는 `Text` 위젯을 넣어 정보를 전달한다.
- 다이얼로그 하단에 표시되는 선택지는 `actions` 리스트에 위젯으로 추가한다.
- 보통은 `TextButton`을 사용하지만, `Row`, `IconButton`, `ElevatedButton` 등 다양한 위젯을 자유롭게 구성할 수 있다.

이는 builder처럼 **위젯 트리를 개발자가 직접 구성**할 수 있게 열려 있는 구조이며, 복잡한 버튼 구성이 필요한 경우 유용하게 활용된다.


```dart
// ✅ 일반적인 기본 사용 예
showDialog(
  context: context,
  builder: (context) {
    return AlertDialog(
      title: Text('알림'),
      content: Text('정말 삭제하시겠습니까?'),
      actions: [
        TextButton(
          onPressed: () {
            Navigator.pop(context, false); // 취소
          },
          child: Text('취소'),
        ),
        TextButton(
          onPressed: () {
            Navigator.pop(context, true); // 확인
          },
          child: Text('확인'),
        ),
      ],
    );
  },
);
```

- `showDialog()`는 비동기로 동작하며, AlertDialog를 반환하는 `builder`를 요구한다.
- `Navigator.pop(context, result)`를 통해 다이얼로그를 닫고 결과를 반환할 수 있다.
- **Navigator**에 사용한 context는 builder에 파라미터로 들어간 context이다.  


---

## 4. 결과값 처리 (버튼 클릭 후 결과 받기)

```dart
void _showAlert(BuildContext context) async {
  final confirmed = await showDialog<bool>(
    context: context,
    builder: (context) => AlertDialog(
      title: Text('삭제 확인'),
      content: Text('정말 삭제하시겠습니까?'),
      actions: [
        TextButton(
          onPressed: () => Navigator.pop(context, false),
          child: Text('취소'),
        ),
        TextButton(
          onPressed: () => Navigator.pop(context, true),
          child: Text('확인'),
        ),
      ],
    ),
  );

  if (confirmed == true) {
    // 삭제 로직 실행
  }
}
```

<br>

---

### 다이얼로그의 결과값을 받는 방식

AlertDialog에서 `Navigator.pop(context, true)` 또는 `false`를 사용해 값을 반환하면,  
해당 값은 `await showDialog(...)`를 통해 받을 수 있다.

| 사용자 동작 | 반환 값 |
|--------------|-----------|
| "확인" 버튼 클릭 | `true` |
| "취소" 버튼 클릭 | `false` |
| 외부 영역 클릭 등으로 닫힘 | `null` |

```dart
if (confirmed == true) {
  // 확인 선택 시 실행할 로직
} else {
  // 취소 또는 외부 클릭 시 실행할 로직
}
```

이렇게 간단한 조건 분기로 사용자의 선택에 따라 다른 동작을 수행할 수 있다.

---

## AlertDialog 분리 및 재사용 방식

Flutter에서 AlertDialog를 다양한 방식으로 분리하여 사용할 수 있다. 아래는 실무에서 자주 사용되는 세 가지 구조이다.

| 방식 | 설명 | 장점 | 단점 |
|------|------|------|------|
| 위젯 함수 분리 | `Widget _buildDialog(BuildContext context)` 형태로 함수로 분리 | 간결하고 빠르게 작성 가능 | 복잡한 상태 제어에는 한계 |
| StatelessWidget 또는 StatefulWidget | 커스텀 Dialog 클래스로 분리 | 구조화된 관리, 테스트 용이 | 파일/코드가 분산될 수 있음 |
| 전역 유틸 함수 | `showConfirmDialog()` 형태로 어디서나 재사용 가능 | 호출부가 매우 간결함 | UI 커스터마이징에는 불리할 수 있음 |

<br><br>

### 위젯 함수 분리

```dart
Widget _buildConfirmDialog(BuildContext context) {
  return AlertDialog(
    title: Text('알림'),
    content: Text('정말 삭제하시겠습니까?'),
    actions: [
      TextButton(
        onPressed: () => Navigator.pop(context, false),
        child: Text('취소'),
      ),
      TextButton(
        onPressed: () => Navigator.pop(context, true),
        child: Text('확인'),
      ),
    ],
  );
}



// 사용예시
ElevatedButton(
  onPressed: ()  {
    showDialog(context: context, builder: _buildMyDialog);
  },
  child: Text('삭제하기'),
)
```

<br><br>

### 5.2 커스텀 Dialog 클래스로 분리

```dart
class ConfirmDialog extends StatelessWidget {
  final String title;
  final String content;

  const ConfirmDialog({Key? key, required this.title, required this.content}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return AlertDialog(
      title: Text(title),
      content: Text(content),
      actions: [
        TextButton(
          onPressed: () => Navigator.pop(context, false),
          child: Text('취소'),
        ),
        TextButton(
          onPressed: () => Navigator.pop(context, true),
          child: Text('확인'),
        ),
      ],
    );
  }
}

// 사용예시

ElevatedButton(
    onPressed: () async {
      final result = await showDialog<bool>(
        context: context,
        builder: (context) =>
            ConfirmDialog(
              title: '알림',
              content: '정말 삭제하시겠습니까?',
            ),
      );

      if (result == true) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('✅ 삭제가 완료되었다')),
        );
      } else if (result == false) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('❎ 삭제가 취소되었다')),
        );
      } else {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('ℹ️ 다이얼로그가 닫혔다')),
        );
      }
    },
    child: Text('삭제하기')
)

```

<br><br>

### 전역 유틸 함수 분리

✅ 1) Future<bool?>을 반환받아 처리하는 방식  
사용자는 `await` 키워드로 결과를 기다린 후 분기 처리를 할 수 있다.

```dart
Future<bool?> showConfirmDialog({
  required BuildContext context,
  String title = '알림',
  required String content,
  String cancelText = '취소',
  String confirmText = '확인',
}) {
  return showDialog<bool>(
    context: context,
    builder: (context) => AlertDialog(
      title: Text(title),
      content: Text(content),
      actions: [
        TextButton(
          onPressed: () => Navigator.pop(context, false),
          child: Text(cancelText),
        ),
        TextButton(
          onPressed: () => Navigator.pop(context, true),
          child: Text(confirmText),
        ),
      ],
    ),
  );
}


// 사용예시
final confirmed = await showConfirmDialog(
  context: context,
  content: '정말 삭제하시겠습니까?',
);

if (confirmed == true) {
  print('✅ 삭제가 완료되었다');
} else if (confirmed == false) {
  print('✅ 삭제가 취소되었다');
} else {
  print('✅ 다이얼로그가 닫혔다');
}


```

<br><br>

✅ 2) 콜백 기반 처리 방식  
확인/취소에 따라 미리 정의된 콜백을 실행하도록 분리한 방식이다.

```dart
/// 콜백 방식으로 처리하는 유틸 함수 버전
Future<void> showConfirmDialogWithCallbacks({
  required BuildContext context,
  String title = '알림',
  required String content,
  String cancelText = '취소',
  String confirmText = '확인',
  required VoidCallback onConfirm,
  VoidCallback? onCancel,
}) async {
  final result = await showDialog<bool>(
    context: context,
    builder: (context) => AlertDialog(
      title: Text(title),
      content: Text(content),
      actions: [
        TextButton(
          onPressed: () => Navigator.pop(context, false),
          child: Text(cancelText),
        ),
        TextButton(
          onPressed: () => Navigator.pop(context, true),
          child: Text(confirmText),
        ),
      ],
    ),
  );

  if (result == true) {
    onConfirm();
  } else {
    onCancel?.call();
  }
}


// 사용예시

ElevatedButton(
  onPressed: () async {
    await showConfirmDialogWithCallbacks(
      context: context,
      content: '정말 삭제하시겠습니까?',
      onConfirm: () {
        print('✅ 삭제가 완료되었다');
      },
      onCancel: () {
        print('✅ 삭제가 취소되었다');
      },
    );
  },
  child: Text('삭제하기'),
)
```

이처럼 Dialog를 함수, 위젯, 유틸 구조로 나누어 작성하면 유지보수성과 재사용성이 크게 향상된다.


<br><br>

---

### 🔍 다이얼로그 내에서 화면 복귀 처리

예를 들어, 두 번째 페이지 (`SecondPage`)에서 다이얼로그를 띄우고, 사용자의 선택에 따라 첫 번째 화면으로 복귀하고 싶을 때 다음과 같은 흐름으로 구현할 수 있다:

```dart
class SecondPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('SecondPage')),
      body: Center(
        child: ElevatedButton(
          onPressed: () async {
            final confirm = await showDialog<bool>(
              context: context,
              builder: (context) => AlertDialog(
                title: Text("확인 요청"),
                content: Text("첫 화면으로 돌아가시겠습니까?"),
                actions: [
                  TextButton(
                    onPressed: () => Navigator.pop(context, false),
                    child: Text("취소"),
                  ),
                  TextButton(
                    onPressed: () => Navigator.pop(context, true),
                    child: Text("확인"),
                  ),
                ],
              ),
            );

            if (confirm == true && context.mounted) {
              Navigator.pop(context); // SecondPage pop → MainScreen으로 복귀
            }
          },
          child: Text("Dialog 열기"),
        ),
      ),
    );
  }
}
```

여기서 주의할 점은 context의 위치이다.  
- `showDialog`에 넘기는 context와  
- 다이얼로그 내부에서 사용하는 `Navigator.pop(context)`의 context는 서로 다르지만,  
**Flutter에서는 builder에 전달되는 context가 다이얼로그에 대한 새로운 context임을 이해해야 한다.**

하지만 그 내부에서도 여전히 같은 위젯 트리 상의 context를 참조하기 때문에 `Navigator.pop(context)`는 안전하게 동작한다.  
다만, 외부 context(`outerContext`)를 별도로 보존하거나 사용할 필요가 있을 경우 명확하게 구분해 주는 것이 좋다.



<br><br>

---




### 플랫폼 대응 전역 다이얼로그 함수

플랫폼 별로 `CupertinoAlertDialog` 또는 `AlertDialog`를 사용해 다이얼로그 UI를 분기 처리할 수 있다.  
아래는 iOS/Android 모두에서 사용할 수 있도록 커스터마이징한 다이얼로그 예시이다.

```dart
import 'dart:io';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

Future<bool?> showPlatformDialog({
  required BuildContext context,
  String title = '알림',
  required String content,
  String cancelText = '취소',
  String confirmText = '확인',
}) {
  if (Platform.isIOS) {
    return showCupertinoDialog<bool>(
      context: context,
      builder: (_) => CupertinoAlertDialog(
        title: Text(title),
        content: Text(content),
        actions: [
          CupertinoDialogAction(
            onPressed: () => Navigator.pop(context, false),
            child: Text(
              cancelText,
              style: TextStyle(color: CupertinoColors.destructiveRed),
            ),
          ),
          CupertinoDialogAction(
            onPressed: () => Navigator.pop(context, true),
            child: Text(
              confirmText,
              style: TextStyle(color: CupertinoColors.systemBlue),
            ),
          ),
        ],
      ),
    );
  } else {
    return showDialog<bool>(
      context: context,
      builder: (_) => AlertDialog(
        title: Text(title),
        content: Text(content),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context, false),
            child: Text(cancelText),
          ),
          TextButton(
            onPressed: () => Navigator.pop(context, true),
            child: Text(confirmText),
          ),
        ],
      ),
    );
  }
}
```

#### 사용 예시:

```dart
ElevatedButton(
  onPressed: () async {
    final result = await showPlatformDialog(
      context: context,
      content: '정말 삭제하시겠습니까?',
    );

    if (result == true) {
      print("삭제 진행");
    }
  },
  child: Text('삭제하기'),
);
```


<br><br>

---

## 실습 과제: 사용자 이름 확인 Dialog

### 목표

버튼을 누르면 AlertDialog가 나타나고,  
다음과 같은 내용을 보여준다:  
- 제목: “확인 요청”  
- 내용: “정말 [사용자 이름]님을 삭제하시겠습니까?”  
- 버튼: “취소”, “삭제”

### 조건
- 이름은 변수 userName으로 미리 선언되어 있어야 한다  
(예: final userName = '홍길동';)  
- 사용자가 “삭제”를 누르면 true,  
“취소”를 누르면 false를 반환해야 한다  
- 결과에 따라 ScaffoldMessenger.of(context).showSnackBar()를 이용해 결과 메시지를 보여준다


예시 흐름  
- 버튼 누름  
- 다이얼로그 표시 (이름 포함된 메시지)  
- 선택에 따라 다이얼로그 닫힘  
- 화면 하단에 결과 메시지 표시



<br><br>

---

## HISTORY
- 250804 : 최초 작성
- 250805 : OS 대응 전역 함수 생성
