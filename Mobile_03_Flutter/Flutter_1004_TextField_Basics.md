# Flutter - TextField 가이드


## 1. 개념

`TextField`는 상태를 가지는 위젯으로 텍스트 입력 상자를 표시한다. 컨트롤러, 장식, 키보드 타입, 콜백 등을 통해 사용자 입력을 처리하도록 커스터마이징할 수 있다. 기본적으로 자체적으로 텍스트를 관리하지만, `TextEditingController`를 사용하면 텍스트와 변경 사항을 프로그래밍적으로 제어할 수 있다.

 
## 4. 예제


### 4.1 기본 TextField (외관)

```dart
TextField(
  decoration: InputDecoration(
    labelText: 'Enter your name',
    border: OutlineInputBorder(), 
  ),
)
```

기본적인 텍스트 입력 상자이다.<br><br>

### 4.2 값 가져오기 (Controller 사용)

```dart
final TextEditingController _controller = TextEditingController();

@override
void dispose() {
  _controller.dispose();
  super.dispose();
}

// 위젯 트리 내에서:
TextField(
  controller: _controller,
  decoration: InputDecoration(
    labelText: 'Email',
    prefixIcon: Icon(Icons.email),
  ),
)
```

컨트롤러를 사용해 텍스트를 프로그래밍적으로 제어할 수 있다.<br><br>

### 4.3 입력 변화 처리

```dart
TextField(
  onChanged: (value) {
    print('Current input: $value');
  },
)
```

입력 값이 변경될 때마다 콜백을 실행한다.<br><br>


## 5. 주요 속성 표

| 속성          | 설명                                                                                           |
|:------------- |:--------------------------------------------------------------------------------------------- |
| controller    | 편집 중인 텍스트를 관리한다. 프로그래밍적 접근을 위해 `TextEditingController`를 사용한다.    |
| decoration    | `InputDecoration`을 통해 레이블, 아이콘, 테두리, 힌트 등 시각적 요소를 추가한다.              |
| obscureText   | 텍스트를 숨긴다(예: 비밀번호 입력 시). Boolean 값이다.                                       |
| keyboardType  | 키보드 종류를 설정한다(예: 텍스트, 숫자, 이메일).                                           |
| onChanged     | 텍스트가 변경될 때 호출되는 콜백이다.                                                       |

<br><br>

## 6. 실용적인 팁

1. **컨트롤러는 항상 dispose 처리:** `TextEditingController`를 사용하면 위젯의 `dispose()` 메서드에서 반드시 해제하여 리소스를 확보한다.
2. **장식 사용으로 UX 개선:** 레이블, 힌트, 아이콘을 활용해 사용자가 입력해야 할 내용을 명확히 한다.
3. **키보드 타입 설정 중요:** 예상 입력에 맞게 `keyboardType`을 설정한다(예: `TextInputType.emailAddress`).
4. **비밀번호 입력 시 텍스트 숨김:** 민감한 입력에는 `obscureText: true`를 사용한다.
5. **검증:** 폼 위젯과 함께 사용하여 입력값 검증을 구현한다.

<br><br>

## 7. 선택적 고급 사용법

1. **InputFormatters:** `inputFormatters` 속성으로 입력을 제한하거나 형식을 지정할 수 있다.
2. **포커스 관리:** `FocusNode`를 사용해 포커스를 프로그래밍적으로 제어할 수 있다.
3. **커스텀 스타일:** 텍스트 스타일, 커서 색상 등을 오버라이드해 브랜드에 맞게 꾸밀 수 있다.
4. **텍스트 선택 제어:** 텍스트 선택 기능을 커스터마이징하거나 비활성화할 수 있다.

<br><br>

## 8. 흔한 문제점

1. **키보드가 UI를 가림:** 작은 화면에서 키보드가 `TextField`를 가릴 수 있다. 이때는 `SingleChildScrollView`를 사용하거나 `Scaffold`에서 `resizeToAvoidBottomInset: true`를 설정한다.
2. **컨트롤러 해제 누락:** `TextEditingController`를 해제하지 않으면 메모리 누수가 발생할 수 있다.
3. **성능 문제:** 컨트롤러를 가진 위젯이 과도하게 재빌드되면 지연이 발생할 수 있으니 불필요한 재빌드를 피한다.
4. **검증 부족:** 입력값을 검증하지 않으면 오류나 불편한 사용자 경험이 발생할 수 있다.

<br><br>

## 9. 요약

`TextField`는 텍스트 입력을 위한 필수 Flutter 위젯으로 유연하고 커스터마이징이 가능하다. 프로그래밍적 접근을 위해 컨트롤러를 사용하고, 사용성을 위해 장식을 추가하며, 입력 변화를 처리해 인터랙티브한 기능을 구현한다. 리소스 관리와 사용자 경험을 항상 고려해야 한다.

<br><br>

## 10. HISTORY

- 250902 : 최초 작성  
