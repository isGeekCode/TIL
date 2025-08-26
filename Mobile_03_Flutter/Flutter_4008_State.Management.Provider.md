# Flutter 상태관리: Provider 패키지 입문 가이드

> Provider의 기본 개념부터 설치, 필수 API(`read / watch / select`), 실전 패턴, 그리고 가장 간단한 Counter 앱까지 단계적으로 익힐 수 있습니다.

---

## 1) 왜 Provider인가?
- Flutter 기본 상태관리 `setState`는 **한 위젯 내부**에서만 유효합니다. 여러 위젯이 같은 상태를 공유하려면 **전달(Prop drilling)** 이 복잡해지죠.
- `InheritedWidget`/`InheritedNotifier`로 직접 구현할 수 있지만 **보일러플레이트**가 많습니다.
- **Provider**는 이 모든 걸 깔끔하게 래핑한 **표준 라이브러리**입니다.
  - 의존성 주입(DI) + 상태 공유 + 생명주기를 **간단한 문법**으로 해결
  - `ChangeNotifierProvider`, `Provider`, `FutureProvider`, `StreamProvider`, `ProxyProvider` 등 다양한 시나리오 지원

핵심 아이디어: **상태를 트리의 상위에서 제공(Provide)** 하고, 하위 위젯은 **필요한 시점에 구독(Watch/Select)하거나 한 번만 읽기(Read)** 합니다.

---

## 2) 설치
`pubspec.yaml`에 Provider 의존성을 추가합니다.
```yaml
dependencies:
  flutter:
    sdk: flutter
  provider: ^6.1.2   # 최신 버전 확인 권장
```
그리고 코드에서 임포트:
```dart
import 'package:provider/provider.dart';
```

---

## 3) 용어와 필수 API 빠르게 이해하기
- **ChangeNotifier**: 상태 + `notifyListeners()` 를 가진 클래스로, ViewModel 역할에 자주 사용됩니다.
- **ChangeNotifierProvider**: `ChangeNotifier`를 트리에 주입하는 Provider.
- **context.read<T>()**: 값을 **한 번만 읽기** (구독 X). 보통 버튼 onPressed 같은 **콜백**에서 사용.
- **context.watch<T>()**: 값을 **구독**하고 변경 시 **리빌드**.
- **context.select<T, R>(selector)**: 값의 **일부(R)** 만 구독해 **부분 리빌드 최소화**.
- **Consumer<T>**: 특정 빌더 영역만 구독하고 싶을 때 사용(리빌드 범위 축소).
- **MultiProvider**: 여러 Provider를 한 번에 묶어 주입.

---

## 4) 단계별 학습 로드맵
1. **ViewModel 만들기**: `ChangeNotifier` 상속, 상태 + 메서드 정의
2. **주입(Provide)**: 최상단(또는 필요한 스코프)에 `ChangeNotifierProvider`
3. **소비(Consume)**: 화면에서 `watch / read / select`로 접근
4. **최적화**: `Consumer`, `Selector`, 위젯 분리로 리빌드 범위 제어
5. **확장**: `MultiProvider`, `FutureProvider/StreamProvider`, `ProxyProvider`

---

## 5) 가장 작은 예: Counter (요약판)
### 5-1) ViewModel
```dart
class CounterVM extends ChangeNotifier {
  int _count = 0;
  int get count => _count;

  void increment() { _count++; notifyListeners(); }
  void decrement() { _count--; notifyListeners(); }
}
```

### 5-2) 주입
```dart
void main() {
  runApp(
    ChangeNotifierProvider(
      create: (_) => CounterVM(),
      child: const MyApp(),
    ),
  );
}
```

### 5-3) 소비
```dart
class MyApp extends StatelessWidget {
  const MyApp({super.key});
  @override
  Widget build(BuildContext context) {
    final count = context.watch<CounterVM>().count; // 구독
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: const Text('Provider Counter')),
        body: Center(child: Text('Count: $count', style: const TextStyle(fontSize: 32))),
        floatingActionButton: Column(
          mainAxisAlignment: MainAxisAlignment.end,
          children: [
            FloatingActionButton(
              onPressed: context.read<CounterVM>().increment, // 액션(구독 X)
              child: const Icon(Icons.add),
            ),
            const SizedBox(height: 12),
            FloatingActionButton(
              onPressed: context.read<CounterVM>().decrement,
              child: const Icon(Icons.remove),
            ),
          ],
        ),
      ),
    );
  }
}
```

---

## 6) 초심자를 위한 개념 확장
### 6-1) `watch` vs `read` vs `select`
- **watch**: 값이 바뀌면 **해당 빌드 메서드 영역을 리빌드**. UI 바인딩에 사용.
- **read**: 값만 **한 번 읽고 리빌드 영향 없음**. 버튼/콜백에서 액션 호출용.
- **select**: VM 전체가 아니라 **필요한 조각만 구독**. 예) `select((vm) => vm.count)`

### 6-2) `Consumer<T>`로 리빌드 범위 축소
```dart
Consumer<CounterVM>(
  builder: (_, vm, __) => Text('Count: ${vm.count}'),
)
```
- 화면의 일부만 리빌드하고 싶을 때 사용 (나머지 위젯은 고정).

### 6-3) `MultiProvider`
```dart
MultiProvider(
  providers: [
    Provider(create: (_) => ApiClient()),
    Provider(create: (ctx) => UserService(ctx.read<ApiClient>())),
    ChangeNotifierProvider(create: (ctx) => UserVM(ctx.read<UserService>())),
  ],
  child: const MyApp(),
)
```

### 6-4) 비동기 상태: `FutureProvider` / `StreamProvider`
```dart
final userNameProvider = FutureProvider<String>(
  create: (_) async => await fetchUserName(),
);
// 소비는 context.watch<AsyncValue<String>>() 패턴 대신 Consumer로 값/로딩/에러 분기 처리
```
> 초심자 단계에서는 `ChangeNotifier`로 시작하고, 필요해질 때 확장하세요.

---

## 7) 실전 팁 (초심자 필독)
- **절대 build() 안에서 ViewModel을 생성하지 마세요.** Provider의 `create:`를 사용 (생성·dispose 자동 관리).
- **watch를 콜백 안에서 쓰지 마세요.** 콜백에는 `read`를 사용하세요.
- **값 일부만 필요하다면 select**로 부분 리빌드.
- Provider는 **필요한 스코프(화면/섹션)** 에만 배치해 리빌드 범위 최소화.
- 상태 모델을 **불변 + copyWith**로 관리하면 디버깅과 테스트가 쉬워집니다.

---

## 8) 종합 예제: Counter 앱 (완성 코드)
아래 코드는 위 개념을 모두 반영한 **가장 간단하지만 바람직한** Counter 예제입니다.

```dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

// 1) ViewModel
class CounterVM extends ChangeNotifier {
  int _count = 0;
  int get count => _count;

  void increment() { _count++; notifyListeners(); }
  void decrement() { _count--; notifyListeners(); }
}

// 2) Entry: DI 구성
void main() {
  runApp(
    ChangeNotifierProvider(
      create: (_) => CounterVM(),
      child: const MyApp(),
    ),
  );
}

// 3) View
class MyApp extends StatelessWidget {
  const MyApp({super.key});
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: const Text('Provider Counter')),
        body: const _CounterBody(),
        floatingActionButton: const _CounterButtons(),
      ),
    );
  }
}

// 4) 값 표시(구독)
class _CounterBody extends StatelessWidget {
  const _CounterBody();
  @override
  Widget build(BuildContext context) {
    final count = context.select<CounterVM, int>((vm) => vm.count); // 부분 구독
    return Center(
      child: Text('Count: $count', style: const TextStyle(fontSize: 40)),
    );
  }
}

// 5) 액션(읽기)
class _CounterButtons extends StatelessWidget {
  const _CounterButtons();
  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.end,
      children: [
        FloatingActionButton(
          onPressed: context.read<CounterVM>().increment,
          child: const Icon(Icons.add),
        ),
        const SizedBox(height: 12),
        FloatingActionButton(
          onPressed: context.read<CounterVM>().decrement,
          child: const Icon(Icons.remove),
        ),
      ],
    );
  }
}
```

포인트
- `select`로 텍스트 위젯만 리빌드 → **효율적 갱신**
- 버튼은 `read`로 액션만 호출 → **불필요한 리빌드 없음**
- `ChangeNotifierProvider`가 **생성/해제 라이프사이클**을 관리 → **메모리/구독 누수 방지**

---

## 9) 다음 단계
- 작은 화면 상태 → `ChangeNotifier` + Provider로 충분
- API/로컬 DB/권한 등 **비즈니스 로직**은 `Service/Repository`로 분리해 Notifier는 **얇게 유지**
- 비동기 데이터가 많아지면 `FutureProvider/StreamProvider`도 도입
- 복잡도가 커지면 `Riverpod`, `Bloc` 등으로 확장 검토

---

### 요약
- Provider는 Flutter에서 **가장 표준적인 상태 공유/DI 도구**
- `watch/read/select`만 정확히 이해해도 실전에서 80%는 해결
- 작은 예제를 먼저 완성하고, 점진적으로 스코프/비동기/구조화를 넓혀갈 것



## 10) 실습: TheCatAPI + Provider 예제
이번 섹션에서는 `Provider`와 `Dio`를 활용해 TheCatAPI에서 고양이 이미지를 가져와 화면에 표시하는 간단한 앱을 만들어봅니다. 


- **Model**: API에서 받은 JSON을 파싱하는 `CatImage` 클래스
- **API 서비스**: `Dio`를 사용해 HTTP 요청 처리
- **ViewModel**: `ChangeNotifier`를 상속받아 데이터 요청 및 상태 관리
- **Provider 주입**: `ChangeNotifierProvider`로 ViewModel을 트리에 등록
- **UI**: `GridView`로 고양이 이미지들을 보여줌


아래는 완성된 `main.dart` 예제 코드입니다.
```dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:dio/dio.dart';

// 1) 모델
class CatImage {
  final String id;
  final String url;
  final int? width;
  final int? height;

  CatImage({
    required this.id,
    required this.url,
    this.width,
    this.height,
  });

  factory CatImage.fromJson(Map<String, dynamic> json) {
    return CatImage(
      id: json['id'] as String,
      url: json['url'] as String,
      width: json['width'] is int ? json['width'] as int : null,
      height: json['height'] is int ? json['height'] as int : null,
    );
  }
}

// 2) API 서비스 (dio 사용)
class CatApiService {
  final Dio _dio;

  CatApiService({String? apiKey})
      : _dio = Dio(BaseOptions(
    baseUrl: 'https://api.thecatapi.com/v1/',
    headers: {
      'Content-Type': 'application/json',
      if (apiKey != null && apiKey.isNotEmpty) 'x-api-key': apiKey,
    },
    connectTimeout: const Duration(seconds: 10),
    receiveTimeout: const Duration(seconds: 10),
  ));

  Future<List<CatImage>> fetch({
    int limit = 10,
    int page = 0,
    String size = 'med',
    String mimeTypes = 'jpg',
    bool hasBreeds = true,
    String order = 'RANDOM',
  }) async {
    try {
      final res = await _dio.get(
        'images/search',
        queryParameters: {
          'size': size,
          'mime_types': mimeTypes,
          'format': 'json',
          'has_breeds': hasBreeds,
          'order': order,
          'page': page,
          'limit': limit,
        },
      );

      final List data = res.data as List;
      return data.map((e) => CatImage.fromJson(e)).toList();
    } on DioException catch (e) {
      throw Exception('Dio error: ${e.message}');
    } catch (e) {
      throw Exception('Unknown error: $e');
    }
  }
}

// 3) ViewModel
class CatVM extends ChangeNotifier {
  final CatApiService _service;
  CatVM(this._service);

  final List<CatImage> _items = [];
  List<CatImage> get items => List.unmodifiable(_items);

  bool _loading = false;
  bool get loading => _loading;

  String? _error;
  String? get error => _error;

  int _page = 0;

  Future<void> refresh() async {
    _items.clear();
    _page = 0;
    await loadMore();
  }

  Future<void> loadMore({int limit = 10}) async {
    if (_loading) return;
    _loading = true;
    _error = null;
    notifyListeners();

    try {
      final result = await _service.fetch(limit: limit, page: _page);
      _items.addAll(result);
      _page++;
    } catch (e) {
      _error = e.toString();
    } finally {
      _loading = false;
      notifyListeners();
    }
  }
}

// 4) 앱 엔트리
void main() {
  runApp(
    MultiProvider(
      providers: [
        Provider(create: (_) => CatApiService()), // Service
        ChangeNotifierProvider(
          create: (ctx) => CatVM(ctx.read<CatApiService>()),
        ), // ViewModel
      ],
      child: const MyApp(),
    ),
  );
}

// 5) 뷰
class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: MainScreen(),
    );
  }
}

class MainScreen extends StatelessWidget {
  const MainScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final vm = context.watch<CatVM>();

    return Scaffold(
      appBar: AppBar(title: const Text('Cat Gallery')),
      body: Builder(
        builder: (context) {
          if (vm.loading && vm.items.isEmpty) {
            return const Center(child: CircularProgressIndicator());
          }
          if (vm.error != null) {
            return Center(child: Text('Error: ${vm.error}'));
          }

          return RefreshIndicator(
            onRefresh: vm.refresh,
            child: GridView.builder(
              padding: const EdgeInsets.all(8),
              gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                crossAxisCount: 3,
                mainAxisSpacing: 8,
                crossAxisSpacing: 8,
              ),
              itemCount: vm.items.length,
              itemBuilder: (context, index) {
                final cat = vm.items[index];
                return GestureDetector(
                  onTap: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (_) => FullScreenImage(url: cat.url),
                      ),
                    );
                  },
                  child: Image.network(
                    cat.url,
                    fit: BoxFit.cover,
                    loadingBuilder: (context, child, progress) {
                      if (progress == null) return child;
                      return const Center(child: CircularProgressIndicator());
                    },
                    errorBuilder: (context, error, stack) =>
                    const Icon(Icons.error, color: Colors.red),
                  ),
                );
              },
            ),
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () => vm.loadMore(),
        child: const Icon(Icons.refresh),
      ),
    );
  }
}

class FullScreenImage extends StatelessWidget {
  final String url;
  const FullScreenImage({super.key, required this.url});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(backgroundColor: Colors.white),
      body: Center(
        child: InteractiveViewer( // 줌/드래그까지 가능
          child: Image.network(url, fit: BoxFit.contain),
        ),
      ),
    );
  }
}
```

