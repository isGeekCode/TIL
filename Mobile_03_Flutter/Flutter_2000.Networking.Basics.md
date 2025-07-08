# Flutter - 네트워크 통신 기초 (RESTful API 중심)

---

## 📌 개요

Flutter 앱에서는 외부 서버와 데이터를 주고받기 위해 주로 HTTP 기반의 RESTful API를 사용한다. 이 문서에서는 Flutter에서의 네트워킹 개념과 기본 HTTP 요청 처리 흐름을 설명한다.

---

## 1️⃣ 네트워크 통신이란?

- 클라이언트(Flutter 앱)가 서버에 요청(Request)을 보내고, 서버는 응답(Response)을 반환하는 구조
- 주로 JSON 형식의 데이터를 주고받음
- 대표적인 통신 방식: RESTful API (GET, POST, PUT, DELETE)

---

## 2️⃣ 기본 HTTP 요청 흐름

Flutter에서는 `http` 패키지 또는 `Dio` 패키지를 주로 사용한다.



### ✅ http 패키지 예제

HTTP 응답 데이터는 JSON 형태로 오는데, 그 구조에 따라 처리 방식이 달라진다.

#### 📌 1. JSON 객체 (Map) 형태 응답

예: `{ "name": "John", "age": 30 }`


```dart
import 'package:http/http.dart' as http;
import 'dart:convert';

Future<void> fetchUserData() async {
    final response = await http.get(Uri.parse('https://example.com/user'));

    if (response.statusCode == 200) {
    final data = jsonDecode(response.body); // Map<String, dynamic>
    print('User name: ${data['name']}');
    }
}
```

#### 📌 2. JSON 리스트 (List) 형태 응답

예: `[{"url": "a.jpg"}, {"url": "b.jpg"}]`

```dart
Future<void> fetchCatImages() async {
    final response = await http.get(Uri.parse('https://api.thecatapi.com/v1/images/search?limit=10'));

    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      print('url : ${data['url']}');
    } else {
      print('Error loading data: ${response.statusCode}');
    }
}
```

#### ✅ JSON 구조 확인 팁

- 응답의 최상단이 `{}` 이면 `Map`으로 받는다.
- `[]` 이면 `List`로 받는다.
- 복합 구조일 경우, 먼저 최상단 형태를 확인 후 내부를 점차적으로 파싱한다.

---

## 3️⃣ 주요 HTTP 메서드

| 메서드 | 설명 |
|--------|------|
| `GET` | 데이터 조회 |
| `POST` | 새로운 데이터 생성 |
| `PUT` | 데이터 전체 수정 |
| `PATCH` | 데이터 일부 수정 |
| `DELETE` | 데이터 삭제 |

---

## 4️⃣ JSON 데이터 처리

- 서버에서 주로 JSON 형식으로 데이터를 주고받는다.
- Dart의 `jsonDecode`, `jsonEncode`를 활용
- 모델 클래스와 `fromJson`, `toJson` 패턴으로 매핑

```dart
class User {
  final String name;
  final int age;

  User({required this.name, required this.age});

  factory User.fromJson(Map<String, dynamic> json) {
    return User(name: json['name'], age: json['age']);
  }

  Map<String, dynamic> toJson() {
    return {'name': name, 'age': age};
  }
}
```

---

## 📎 참고

- [http 패키지 공식 문서](https://pub.dev/packages/http)
- [RESTful API 개념](https://restfulapi.net/)

---

## History

- 260626: 초안 작성
