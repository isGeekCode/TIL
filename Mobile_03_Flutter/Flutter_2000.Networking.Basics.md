# Flutter - 네트워크 통신 기초 (RESTful API 중심)

---

## 📌 개요


Flutter 앱에서는 외부 서버와 데이터를 주고받기 위해 주로 HTTP 기반의 RESTful API를 사용한다. 

> **용어 정리**  
> - **클라이언트(Client)**: 요청(Request)을 보내는 쪽 → Flutter 앱  
> - **서버(Server)**: 요청을 받아 응답(Response)을 돌려주는 쪽 → 백엔드 API  
>
> ⚠️ 주의: 여기서 클라이언트/서버는 “갑/을” 관계가 아니라, **누가 먼저 요청을 시작하느냐**의 역할 기준이다.



---

## 1️⃣ 네트워크 통신이란?

- 클라이언트가 서버에 요청(Request) → 서버가 응답(Response) 반환
- 주로 JSON 형식 데이터 교환
- 대표적인 통신 방식: RESTful API (GET, POST, PUT, DELETE)

---

### 📌 Flutter에서의 네트워킹 기본 절차

1. 클라이언트(앱)가 서버에 **요청(Request)** 을 보냄
2. 서버는 요청을 받아 **응답(Response)** 을 반환
3. 응답 데이터(JSON 문자열)를 Dart에서 객체(Map/List)로 변환
4. 모델 클래스에 매핑해 사용
5. 패 시 예외 처리 및 상태 코드 분기

### 🔍 개발 단계 디버깅 팁
- 처음 API를 다룰 때는 응답 구조를 확실히 알기 위해 `print(jsonDecode(res.body).runtimeType)`을 출력해보자.
- `Map<String, dynamic>` → 객체(JSON Object), `List<dynamic>` → 배열(JSON Array)
- 이렇게 확인한 뒤 코드에서 `if (data is Map) ... else if (data is List) ...` 분기로 안전하게 처리할 수 있다.
   

---

## http 패키지 사용하기 (권장 기본)
### 설치
```yaml
dependencies:
  http: ^1.2.0
```

### JSON 객체 응답
```dart
final res = await http.get(Uri.parse(url));
if (res.statusCode == 200) {
  final data = jsonDecode(res.body);
  print('title: ${data['title']}');
}
```

### JSON 리스트 응답

```dart
final res = await http.get(Uri.parse(url));
final list = jsonDecode(res.body) as List<dynamic>;
for (final item in list) {
  print(item['url']);
}

/*
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}
*/


```

#### 📌 2. JSON 리스트 (List) 형태 응답

예: `[{"url": "a.jpg"}, {"url": "b.jpg"}]`

```dart
import 'package:http/http.dart' as http;
import 'dart:convert';

Future<void> fetchCatImages() async {
  const url = 'https://api.thecatapi.com/v1/images/search?limit=10';
  try {
    final res = await http.get(Uri.parse(url));
    if (res.statusCode == 200) {
      final List<dynamic> list = jsonDecode(res.body);
      // 첫 번째 이미지 URL 출력 (존재할 때만)
      if (list.isNotEmpty && list.first is Map<String, dynamic>) {
        print('first url: ${list.first['url']}');
      }
      // 모든 URL 출력
      for (final item in list) {
        if (item is Map<String, dynamic> && item['url'] != null) {
          print('url: ${item['url']}');
        }
      }
    } else {
      print('❌ server error: ${res.statusCode}');
    }
  } catch (e) {
    print('🌐 network error: $e');
  }
}
```

### 🚨 http에서의 에러 처리 패턴

- **상태 코드 분기**: `res.statusCode == 200` 성공, 4xx/5xx는 에러 메시지 분기
- **네트워크 예외**: `try/catch`로 `SocketException` 등 포착
- **파싱 예외**: `jsonDecode`도 실패할 수 있으니 별도 `try/catch` 가능
- **타임아웃**: `.timeout(...)` 으로 지연 방지

```dart
Future<void> fetchWithTimeout() async {
  const url = 'https://jsonplaceholder.typicode.com/posts/1';
  try {
    final res = await http
        .get(Uri.parse(url))
        .timeout(const Duration(seconds: 5)); // 5초 타임아웃
    if (res.statusCode == 200) {
      final data = jsonDecode(res.body);
      print('title: ${data['title']}');
    } else if (res.statusCode == 404) {
      print('❌ not found (404)');
    } else {
      print('⚠️ unexpected: ${res.statusCode}');
    }
  } on TimeoutException {
    print('⏱️ timeout');
  } catch (e) {
    print('🌐 network error: $e');
  }
}
```

#### ✅ JSON 구조 확인 팁

- 응답의 최상단이 `{}` 이면 `Map`으로 받는다.
- `[]` 이면 `List`로 받는다.
- 복합 구조일 경우, 먼저 최상단 형태를 확인 후 내부를 점차적으로 파싱한다.
- `http` 응답은 문자열이므로 `jsonDecode`로 Map/List로 변환한 뒤 키/인덱스로 접근한다.

---

### (참고) HttpClient로 직접 구현하기

- Flutter 내장 dart:io로도 요청 가능 (패키지 설치 불필요)
- 하지만 코드가 장황하고 실무에서 잘 쓰지 않음 → 학습용 참고

```dart
import 'dart:io';
import 'dart:convert';

void main() async {

    final client = HttpClient();
    try {
      final urlStr = "https://jsonplaceholder.typicode.com/posts/1";

      final request = await client.getUrl(Uri.parse(urlStr));
      final response = await request.close();  // 요청 마무리 + 응답 받기

      if (response.statusCode == HttpStatus.ok) {
        final body = await response.transform(utf8.decoder).join();
        print(body);
      }
    } catch (e) {
      print('error: $e');
    } finally {
      client.close(); // 네트워크 리소스 해제
    }
}
```

👉 하지만 코드가 장황하고 관리가 불편하기 때문에, 보통은 **http 패키지**나 **Dio 패키지**를 설치해서 더 간결하게 작성한다.

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
- (다음 학습) Dio 기초: `Flutter_2002.Dio.Basics.md`

---

## History

- 260626: 초안 작성
