# TIL - Dart의 Factory 패턴 이해하기

---

## 📌 요약

- Factory Pattern은 객체 생성 로직을 외부에서 분리하는 디자인 패턴.
- Dart에서는 `factory` 생성자를 활용해 생성 로직을 제어할 수 있음.
- 동일한 객체를 반환하거나, 조건에 따라 하위 타입을 반환할 수 있음.

---

## 🧪 Dart에서의 factory 생성자 예

```dart
class Logger {
  static final Logger _instance = Logger._internal();

  factory Logger() {
    return _instance;
  }

  Logger._internal();

  void log(String msg) => print('LOG: $msg');
}
```

→ `Logger()` 호출 시 항상 같은 인스턴스를 반환 (싱글턴)

---

## 🧰 팩토리 메서드 예시

```dart
class Animal {
  void speak() => print('...');
}

class Dog extends Animal {
  @override
  void speak() => print('멍멍');
}

class Cat extends Animal {
  @override
  void speak() => print('야옹');
}

class AnimalFactory {
  static Animal create(String type) {
    if (type == 'dog') return Dog();
    if (type == 'cat') return Cat();
    return Animal();
  }
}
```

→ 클라이언트는 AnimalFactory.create(type)만 호출하면 됨

---

## 🧠 언제 쓰는가?

- 생성 비용이 높은 객체를 재사용할 때
- 타입 분기를 내부로 숨기고 싶을 때
- 여러 하위 타입 중 하나를 동적으로 선택할 때

---

## 🏛 GoF 기준 팩토리 패턴

- 인터페이스나 추상 클래스를 기반으로 동작
- 팩토리 메서드가 적절한 하위 클래스를 반환
- Dart에서 다음과 같이 구현할 수 있음:

```dart
abstract class Button {
  void render();
}

class AndroidButton implements Button {
  @override
  void render() => print('Android 버튼 렌더링');
}

class IOSButton implements Button {
  @override
  void render() => print('iOS 버튼 렌더링');
}

class ButtonFactory {
  static Button createButton(String platform) {
    if (platform == 'android') return AndroidButton();
    if (platform == 'ios') return IOSButton();
    throw Exception('Unknown platform');
  }
}
```

---

## HISTORY
- 250701 : 초안작성
