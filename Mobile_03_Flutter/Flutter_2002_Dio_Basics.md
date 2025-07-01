# Flutter - Dio 사용 기초

---

## 📌 개요

Flutter에서 `Dio`는 강력하고 유연한 HTTP 클라이언트로, `http` 패키지보다 더 많은 기능 (Interceptor, FormData, Timeout 등)을 제공한다.  
이 문서에서는 Dio의 기초 사용법과 간단한 예제를 정리한다.

---

## 1️⃣ Dio 설치

```yaml
dependencies:
  dio: ^5.4.0
```

---

## 1️⃣ 기본 사용 방법

`Dio`는 아래와 같이 간단히 인스턴스를 생성하여 사용할 수 있습니다.  
이 방식이 가장 기본적인 사용 방식입니다.

```dart
import 'package:dio/dio.dart';

void fetchData() async {
  final dio = Dio(); // Dio 인스턴스 생성
  final response = await dio.get('https://api.thecatapi.com/v1/images/search?limit=1'); // GET 요청
  print(response.data); // 응답 데이터 출력
}
```

---

## 2️⃣ Dio 객체 구성 및 옵션 설정

`Dio`는 인스턴스를 생성한 후 다양한 옵션을 지정할 수 있습니다.  
`BaseOptions`를 활용하면 기본 URL, 헤더, 타임아웃 등을 설정할 수 있으며, 이는 **선택적(Optional)** 구성입니다.

```dart
import 'package:dio/dio.dart';

final dio = Dio(BaseOptions(
  baseUrl: 'https://api.thecatapi.com/v1', // 기본 URL 설정
  connectTimeout: const Duration(seconds: 5), // 연결 타임아웃 설정
  receiveTimeout: const Duration(seconds: 3), // 응답 타임아웃 설정
  headers: {
    'Content-Type': 'application/json', // 기본 헤더 설정
  },
));
```

---

## ☝️ Dio 싱글턴 패턴 예제

Dio는 네트워크 요청 시 재사용성을 높이기 위해 싱글턴(Singleton) 패턴으로 구성하는 것이 일반적이다.

```dart
class ApiClient {
  static final ApiClient _instance = ApiClient._internal(); // 내부 인스턴스 생성
  late final Dio dio; // Dio 객체 선언

  factory ApiClient() => _instance; // 외부에서 접근할 수 있는 factory 생성자

  ApiClient._internal() {
    dio = Dio(BaseOptions(
      baseUrl: 'https://api.thecatapi.com/v1', // 기본 URL
      connectTimeout: const Duration(seconds: 5), // 연결 타임아웃
      receiveTimeout: const Duration(seconds: 3), // 수신 타임아웃
      headers: {
        'Content-Type': 'application/json', // 기본 헤더
      },
    ));
  }
}
```

이렇게 구성하면 `ApiClient().dio.get(...)` 형태로 어디서든 동일한 Dio 인스턴스를 사용할 수 있다.  
싱글턴 패턴에 대한 자세한 설명은 [Flutter_3001_Singleton_Pattern.md](Flutter_3001_Singleton_Pattern.md) 문서를 참고하세요.

---

## 3️⃣ GET 요청 예제

```dart
Future<void> fetchCatImages() async {
  try {
    final response = await Dio().get('https://api.thecatapi.com/v1/images/search?limit=5'); // GET 요청

    if (response.statusCode == 200) {
      final data = response.data; // 응답 데이터
      print('🐱 이미지 URL: ${data[0]['url']}'); // 첫 번째 이미지의 URL 출력
    }
  } catch (e) {
    print('❗ 에러 발생: $e'); // 에러 처리
  }
}
```

---

## 4️⃣ POST 요청 예제

```dart
Future<void> sendData() async {
  final dio = Dio(); // Dio 인스턴스 생성

  try {
    final response = await dio.post(
      'https://jsonplaceholder.typicode.com/posts', // POST 요청 보낼 URL
      data: {
        "title": "Flutter Dio",
        "body": "This is a test post.",
        "userId": 1,
      },
    );

    print('✅ 응답 데이터: ${response.data}'); // 응답 출력
  } catch (e) {
    print('❌ 에러 발생: $e'); // 에러 처리
  }
}
```

---


## HISTORY
- 250701 : 초안작성
    - 아워홈 프로젝트
