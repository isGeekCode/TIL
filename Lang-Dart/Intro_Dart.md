# Intro: Dart

## Dart란 무엇인가?

Dart는 Google에서 개발한 클라이언트 최적화 프로그래밍 언어로, 모든 플랫폼에서 빠르고 안정적인 애플리케이션을 개발하기 위해 설계되었습니다. Dart는 Flutter 프레임워크의 기반이 되는 언어이며, 웹, 모바일, 데스크톱 애플리케이션을 개발하는 데 사용됩니다.

## Dart의 역사


- **2011년**: Google I/O에서 처음 발표
- **2013년**: Dart 1.0 출시
- **2018년**: Dart 2.0 출시 (타입 안전성 강화)
- **2021년**: Dart 2.13 출시 (null 안전성 도입)
- **2023년**: Dart 3.0 출시 (레코드, 패턴 매칭 도입)

Dart는 초기에 JavaScript를 대체하기 위한 웹 프로그래밍 언어로 시작했지만, 현재는 Flutter를 통한 크로스 플랫폼 애플리케이션 개발에 주로 사용됩니다.


## 특징

### 객체지향 언어

Dart는 클래스 기반의 객체 지향 언어입니다. 모든 것이 객체이며, 모든 객체는 클래스의 인스턴스입니다. 심지어 함수와 `null`도 객체입니다.

```dart
class Person {
  String name;
  int age;

  Person(this.name, this.age);

  void introduce() {
    print('안녕하세요, 저는 $name이고 $age살입니다.');
  }
}

void main() {
  final person = Person('홍길동', 30);
  person.introduce();  // 출력: 안녕하세요, 저는 홍길동이고 30살입니다.
```


### 강력한 타입 시스템

Dart는 정적 타입 언어이지만, 타입 추론을 지원하여 타입 명시를 생략할 수 있습니다.

```dart
// 타입 명시
String name = '홍길동';
int age = 30;

// 타입 추론
var name = '홍길동';    // String으로 추론
var age = 30;         // int로 추론
final height = 175.5;  // double로 추론
```

### 비동기 프로그래밍 지원
Dart는 `Future`, `Stream`, `async`, `await` 등을 통해 비동기 프로그래밍을 지원합니다.

```
Future<String> fetchData() async {
  // 비동기 작업 시뮬레이션
  await Future.delayed(Duration(seconds: 2));
  return '데이터';
}

void main() async {
  print('데이터 요청 시작');
  final data = await fetchData();
  print('받은 데이터: $data');
}
```

### Null 안전성
Dart 2.12부터 Null 안전성을 도입하여, 변수가 null 가능성을 타입 시스템에서 명시합니다.

```
// null이 될 수 없는 변수
String name = '홍길동';
// name = null;  // 컴파일 오류

// null이 될 수 있는 변수
String? nullableName = '홍길동';
nullableName = null;  // 허용됨
```


### 5. 다중 플랫폼 지원

Dart는 여러 플랫폼에서 실행될 수 있습니다:

- **네이티브 플랫폼**: Dart는 AoT(Ahead-of-Time) 컴파일을 통해 네이티브 바이너리로 컴파일됩니다. Flutter 앱은 이 방식으로 배포됩니다.
- **웹 플랫폼**: Dart는 JavaScript로 컴파일되어 브라우저에서 실행됩니다.
- **개발 환경**: Dart는 JIT(Just-in-Time) 컴파일을 통해 개발 중 핫 리로드와 같은 기능을 제공합니다.

### 6. 풍부한 표준 라이브러리

Dart는 다양한 기능을 제공하는 풍부한 표준 라이브러리를 포함하고 있습니다:

- 컬렉션 (`List`, `Map`, `Set` 등)
- 비동기 처리 (`Future`, `Stream`)
- 파일 I/O
- HTTP 클라이언트
- 정규 표현식
- 직렬화 지원
