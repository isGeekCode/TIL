# Dart에서의 싱글턴(Singleton) 패턴

---

## 📌 싱글턴이란?

- 애플리케이션 전체에서 **하나의 인스턴스만 존재**하도록 보장하는 디자인 패턴
- 보통 **공통 로직을 갖는 Manager, Service, Client** 등에서 활용

---

## 🔧 싱글턴 구현 방법

### 1. factory 생성자 방식

```dart
class Logger {
  static final Logger _instance = Logger._internal();

  factory Logger() {
    return _instance;
  }

  Logger._internal(); // private 생성자

  void log(String message) {
    print('LOG: $message');
  }
}
```

### 2. static getter 방식 (Lazy Initialization)
```dart
class ConfigManager {
  static ConfigManager? _instance;

  ConfigManager._(); // private 생성자


  static ConfigManager get instance {
    _instance ??= ConfigManager._();
    return _instance!;
  }
}
```


### 예시
플러터 - Dio 문서 참고


## 언제 사용하면 좋을까?
- API 클라이언트, 디버깅 로거, 설정 관리, 공유 상태 보관 등에 유용
- 상태 공유보다 상태 관리는 상태관리 패턴(Provider, Riverpod 등) 활용 권장


## History
