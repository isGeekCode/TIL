# Flutter - Dio 사용 기초

---

## 📌 개요

Flutter에서 `Dio`는 강력하고 유연한 HTTP 클라이언트로, `http` 패키지보다 더 많은 기능 (Interceptor, FormData, Timeout 등)을 제공한다.  
이 문서에서는 Dio의 기초 사용법과 간단한 예제를 정리한다.

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

## 2️⃣ GET 요청 예제

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

## 3️⃣ POST 요청 예제

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

## 4️⃣ Dio 객체 구성 및 옵션 설정

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

### 🔍 로그 인터셉터(LogInterceptor) 추가

개발 중에는 요청/응답 정보를 확인할 수 있도록 `LogInterceptor`를 사용하는 것이 유용합니다.

```dart
dio.interceptors.add(LogInterceptor(
  request: true,
  requestHeader: true,
  requestBody: true,
  responseHeader: true,
  responseBody: true,
  error: true,
  logPrint: (log) => debugPrint('📡 [NETWORK] $log'), // 로그 출력 방식 지정
));
```

> `logPrint`를 활용하면 원하는 방식으로 로그를 커스터마이징할 수 있습니다.  
> 운영 환경에서는 민감한 정보를 출력하지 않도록 `requestBody`, `responseBody`를 false로 설정하는 것이 좋습니다.

### 🛠 커스텀 Interceptor 직접 구현

기본 제공되는 `LogInterceptor`보다 더 세밀하게 요청/응답 흐름을 제어하고 싶다면, `InterceptorsWrapper`를 사용하여 커스텀 인터셉터를 구현할 수 있습니다.  
이는 토큰 갱신, 공통 헤더 추가, 에러 공통 처리 등 고급 네트워크 핸들링에 유용합니다.

```dart
dio.interceptors.add(InterceptorsWrapper(
  onRequest: (options, handler) {
    print('🌐 [ApiClient] Request: ${options.uri}');
    return handler.next(options); // 요청을 계속 진행
  },
  onResponse: (response, handler) {
    print('📥 [ApiClient] Response: ${response.statusCode}');
    return handler.next(response); // 응답 처리를 계속 진행
  },
  onError: (DioError e, handler) {
    print('❗️ [ApiClient] Error: ${e.message}');
    return handler.next(e); // 에러 처리 계속 진행
  },
));
```

> 위와 같이 직접 Interceptor를 구성하면 요청 흐름을 세밀하게 제어할 수 있습니다.
> 예외 처리, 헤더 자동 주입, 리프레시 토큰 등의 고급 기능 구현에도 사용됩니다.

---

## 5️⃣ Dio 싱글턴 패턴 예제

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

---

## 6️⃣ 🧩 Dio 응용 구조 예시

### ✅ V1. 싱글턴 패턴 기반 구성

```dart
class ApiClient {
  static final ApiClient _instance = ApiClient._internal();
  final Dio _dio = Dio();

  factory ApiClient() {
    return _instance;
  }

  ApiClient._internal() {
    _dio.interceptors.add(InterceptorsWrapper(
      onRequest: (options, handler) {
        print('🌐 [ApiClient] Request: ${options.uri}');
        return handler.next(options);
      },
      onResponse: (response, handler) {
        print('📥 [ApiClient] Response: ${response.statusCode}');
        return handler.next(response);
      },
      onError: (DioError e, handler) {
        print('❗️ [ApiClient] Error: ${e.message}');
        return handler.next(e);
      },
    ));
  }

  Future<String?> fetchCatImageUrl() async {
    try {
      final response = await _dio.get('https://api.thecatapi.com/v1/images/search?limit=1');
      if (response.statusCode == 200) {
        return response.data[0]['url'];
      }
    } catch (e) {
      print('ApiClient fetch error: $e');
    }
    return null;
  }
}
```

---

### ✅ V2. Enum + 생성자 주입 기반 구성

```dart
enum CatApiEndpoint {
  fetchSingleImage,
  fetchMultipleImages;

  String get path {
    switch (this) {
      case CatApiEndpoint.fetchSingleImage:
        return 'v1/images/search?limit=1';
      case CatApiEndpoint.fetchMultipleImages:
        return 'v1/images/search?limit=10';
    }
  }
}

class ApiClientV2 {
  final Dio _dio;

  ApiClientV2(Dio dio)
      : _dio = dio..options.baseUrl = 'https://api.thecatapi.com/';

  Future<String?> fetchImageUrl({CatApiEndpoint endpoint = CatApiEndpoint.fetchSingleImage}) async {
    try {
      final response = await _dio.get(endpoint.path);
      if (response.statusCode == 200 && response.data is List && response.data.isNotEmpty) {
        return response.data[0]['url'];
      }
    } catch (e) {
      print('CatApiClientV2 fetch error: $e');
    }
    return null;
  }
}
```

---

### ✅ V3. Retrofit 스타일 구성

```dart
import 'package:retrofit/retrofit.dart';
import 'package:json_annotation/json_annotation.dart';

part 'networkModule.g.dart';

@RestApi(baseUrl: "https://api.thecatapi.com/v1")
abstract class CatApiService {
  factory CatApiService(Dio dio, {String baseUrl}) = _CatApiService;

  @GET("/images/search?limit=1")
  Future<List<CatImage>> getCatImages();
}

@JsonSerializable()
class CatImage {
  final String url;

  CatImage({required this.url});

  factory CatImage.fromJson(Map<String, dynamic> json) => _$CatImageFromJson(json);
  Map<String, dynamic> toJson() => _$CatImageToJson(this);
}
```

> 📌 `json_serializable`, `retrofit` 패키지와 `build_runner`를 통해 `.g.dart` 파일을 자동 생성해야 정상 동작합니다.

---

## HISTORY
- 250701 : 초안작성
    - 아워홈 프로젝트
