# Flutter 상태관리 기초 - Stateless와  Stateful 

## 0. 시작하기에 앞서 알아야할 내용

앱은 main() 함수에서 runApp()을 호출하면서 시작되며, 일반적으로 이 함수는 MaterialApp 또는 CupertinoApp을 반환합니다.  
이 앱들은 보통 home 속성을 통해 앱의 첫 화면을 구성하는 위젯을 설정하게 되며,  
여기에 들어갈 수 있는 것이 오늘 다룰 StatelessWidget과 StatefulWidget입니다.

### 0-1. StatelessWidget이란?

Flutter에서 모든 UI는 위젯으로 구성되며, 그 중에서도 가장 기본이 되는 위젯이 `StatelessWidget`입니다.

`StatelessWidget`은 말 그대로 상태(State)가 없는 위젯입니다.  
이 위젯은 **내부 데이터가 변하지 않고**, 생성 시점에 주어진 값을 기반으로 UI를 구성합니다.

✅ 특징:
- 상태를 저장하지 않음
- 외부에서 전달받은 데이터만으로 build() 실행
- 다시 build하려면 새로운 인스턴스를 생성해야 함

```dart
class HelloText extends StatelessWidget {
  final String name;

  const HelloText({super.key, required this.name});

  @override
  Widget build(BuildContext context) {
    return Text('Hello, $name!');
  }
}
```

위 예제에서 `HelloText`는 이름을 받아 텍스트를 출력하는 `StatelessWidget`입니다.  
이 위젯은 `name`이 바뀌지 않는 한, 상태를 저장하거나 변경하지 않습니다.

✳️ 요약: StatelessWidget은 “정적인 UI 구성 요소”입니다.

### 0-2. 상태란 무엇인가?



## 1️⃣ Stateless와 Stateful 개요

Flutter에서 상태는 UI에 영향을 주는 데이터이며, 이 데이터를 효과적으로 관리하는 것이 앱 개발의 핵심이다.  
상태를 가지지 않는 `StatelessWidget`에서, 상태를 반영할 수 있는 `StatefulWidget`으로 전환하는 과정이 상태관리의 첫걸음이다.

<br><br>

---

## 2️⃣ 핵심 개념 요약

| 개념      | 설명    |
|--------|-----------|
| `StatefulWidget` | 상태를 가질 수 있는 동적 위젯                                          |
| `State`        | 위젯의 상태를 저장하고 `build()`를 실행하는 클래스                    |
| `setState()`   | 상태 값을 변경하고 UI를 다시 빌드하도록 알리는 메서드                 |
| `initState()`  | 위젯이 처음 빌드될 때 한 번만 호출되는 초기화 메서드                   |

<br><br>

---

## 3️⃣ 기본 흐름

1. `StatefulWidget` 클래스 생성  
2. `State` 내부에 상태 변수 선언  
3. UI 요소에서 `setState()` 호출로 상태 변경  
4. 변경된 값을 기반으로 UI가 다시 그려짐

<br><br>

---

## 4️⃣ 실습 코드

```dart
class MyCounter extends StatefulWidget {
  const MyCounter({super.key});

  @override
  State<MyCounter> createState() => _MyCounterState();
}

class _MyCounterState extends State<MyCounter> {
  int _count = 0;

  void _increment() {
    setState(() {
      _count++;
    });
  }

  @override
  void initState() {
    super.initState();
    print("초기화 로직 실행");
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        Text('카운트: $_count'),
        ElevatedButton(
          onPressed: _increment,
          child: const Text('증가'),
        ),
      ],
    );
  }
}
```

<br><br>

---

## 5️⃣ 주의사항

- `setState()`는 불필요하게 호출되지 않도록 주의  
- 상태가 많아질 경우 구조 분리 고려 필요

<br><br>

---

## 6️⃣ 요약 정리

Flutter 상태 관리의 출발점은 `StatefulWidget`과 `setState()`이다.  
작은 단위부터 상태 흐름을 이해하고 관리하는 습관이 중요하다.

<br><br>

---

## 7️⃣ 관련 문서

- [StatefulWidget 공식 문서](https://api.flutter.dev/flutter/widgets/StatefulWidget-class.html)  
- [setState 공식 설명](https://api.flutter.dev/flutter/widgets/State/setState.html)
