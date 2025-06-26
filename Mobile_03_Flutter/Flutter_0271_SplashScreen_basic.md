# 🚀 Flutter - Splash 구현

이 문서에서는 Flutter 앱에서 Splash를 설계하고 구현하는 전체 흐름을 정리합니다.




## 🚀 Flutter에서의 Splash 설계 결정 흐름

Splash는 단순한 화면 전환이 아니라, 앱의 첫 인상을 결정하는 **사용자 경험의 출발점**입니다.  
Flutter에서는 다양한 방법으로 Splash를 구현할 수 있으나, 앱의 특성과 목적에 따라 전략적으로 선택하는 것이 중요합니다.

---

### 📌 단계별 설계 결정

#### 1단계. Splash 화면이 필요한가?
| 조건 | 설명 |
|------|------|
| ✅ 필요 | 앱 초기 로딩 시간이 있거나, 브랜드 인상 전달 목적이 있을 때 |
| ❌ 불필요 | 앱이 즉시 화면을 그리며, 로딩 시간이 거의 없을 때 |

---

#### 2단계. 어떤 Splash 구성 방식이 적절한가?
| 구성 | 설명 | 권장 상황 |
|------|------|-----------|
| **정적만 사용** | OS 레벨의 LaunchScreen 또는 SplashTheme 만으로 구성 | 단순 로고 표시, 빠른 화면 전환이 필요한 앱 |
| **동적만 사용** | 앱 내에서 자체 SplashPage로만 구성 | 가벼운 앱 + 매우 빠른 실행 요구 시 |
| ✅ **정적 + 동적 조합** | 시스템 레벨에서 빠르게 화면 표시 후, 동적 화면에서 초기화 처리 | 대부분의 상용 앱 / 초기 API 호출, 버전체크 등 필요 시 |


---

#### 3단계. 플랫폼 진입 구조 선택

| 스타일 | 진입 구조 | 특징 | 추천 상황 |
|--------|-----------|------|-----------|
| ✅ **iOS 스타일** | `SplashPage`를 앱의 초기 진입점으로 사용하여 push 방식으로 전환 | 화면 전환이 명확하고 구조가 직관적 | 초기 상태 판단이 필요한 앱, 명시적 라우팅을 선호할 때 |
| **Android 스타일** | 웹뷰 등 실제 콘텐츠를 먼저 로드하고, 그 위에 splash를 덮어 표현 | Stack 또는 Layer 기반 제어 | WebView 기반 앱, splash가 부가적인 레이어일 때 |

> 선택은 앱의 구조적 목적과 기술 스택(WebView 유무 등)에 따라 달라질 수 있음.


<br><br>
---

## 정적 스플래시 구현

### iOS

iOS의 기본 스플래시는 iOS - 스플래시 파트 참고
[iOS - 스플래시 구현](Mobile_01_iOS/Flutter_0100_Setup.md)


### Android

Android의 정적 스플래시 구성은 Android - 스플래시 파트 참고  
[Android - 스플래시 구현](Mobile_02_Android/Flutter_0100_Setup.md)



### pub를 이용한 작업
[pub 릴리즈 노트](https://pub.dev/packages/flutter_native_splash)
정적 스플래시를 설정할 때 가장 널리 사용하는 도구는 `flutter_native_splash` 패키지입니다.  

- ✅ 코드 수정 없이 설정 가능 (`pubspec.yaml` 기반 구성)
- ✅ 플랫폼 별(iOS/Android) 설정을 동시에 처리
- ❌ 복잡한 애니메이션이나 조건 분기 로직은 미지원
- ⚠️ `flutter_launcher_icons` 패키지와 함께 사용할 경우 충돌 사례가 존재함. 동시에 사용하는 것을 지양할 것

가능하다면 앱 아이콘 설정과 정적 스플래시 모두 각 OS의 네이티브 방식으로 직접 구성하는 것을 추천합니다. pub 패키지는 간편하지만, 충돌이나 제한 사항이 있을 수 있으므로, 프로젝트 특성에 따라 전략적으로 선택하세요.


pubspec.yaml 파일에 필요한 설정을 추가하고 CLI 명령어를 실행하면, 자동으로 iOS 및 Android 설정이 반영됩니다.

1. 패키지 설치
```bash
flutter pub add flutter_native_splash
```

또는 pubspec.yaml에 직접 추가:

```yaml
dev_dependencies:
  flutter_native_splash: ^2.3.3
```

2. 설정 작성 (pubspec.yaml)

```yaml
flutter_native_splash:
  color: "#ffffff"
  image: assets/images/splash_logo.png
  android: true
  ios: true
  fullscreen: true
```

- `color`: 배경 색상
- `image`: 중앙에 표시할 로고 이미지 경로
- `fullscreen`: 상태바 숨김 여부

<br>

#### 3. 적용 명령어 실행

```bash
# 설치
flutter pub add flutter_native_splash

# 적용
flutter pub run flutter_native_splash:create

# 삭제
flutter pub run flutter_native_splash:remove

# 빌드 캐시 정리
flutter clean
```

flutter_native_splash 설정을 반복해서 변경하거나 테스트하는 경우,
삭제 → 캐시 정리 → 재적용 순으로 수행하는 것이 안전합니다.

pubspec.yaml을 수정한 경우에도 위 순서를 따라주면 변경 사항이 제대로 반영됩니다.

<br><br>
---


## 동적 스플래시 구현 (Dynamic Splash) - iOS Style

> 이 방식은 iOS 스타일의 진입 구조에 해당합니다.  
> 앱의 첫 진입점으로 SplashPage를 사용하고, 초기화 이후 홈 화면으로 전환하는 구조입니다.


플러터에서 동적 스플래시는 네이티브 splash가 끝난 뒤에 Flutter로 진입한 이후, 사용자가 직접 제어 가능한 화면을 의미합니다. 보통 초기 로딩이나 애니메이션, 초기 데이터 체크 등에서 사용됩니다.

### 1. stateful Widget 생성
동적스플래시는 개발자가 원하는 동작으로 제어하기 위해서 stateful로 생성한다.  

```dart
class SplashPage extends StatefulWidget {
  const SplashPage({super.key});

  @override
  State<SplashPage> createState() => _SplashPageState();
}

class _SplashPageState extends State<SplashPage> {
  @override
  Widget build(BuildContext context) {
    return const Placeholder(); // 수정필요
  }
}
```

### 2. entryPoint를 Splash로 지정하기
위에서 생성한 SplashPage를 main함수에서 실행하는 루트앱의 home으로 설정한다. 
```dart
void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: const SplashPage(),
    );
  }
}
```


### 2. 스플래시 이미지 구현
assets 폴더를 미리 구현할 것

 - `Image.asset()`으로 전체 화면 구성
```dart
return Scaffold(
    body: SizedBox.expand(
      child: Image.asset(
        'assets/images/splashImage.jpg',
        fit: BoxFit.cover,
      ),
    )
);
```

여기까지 진행하면 각 OS의 정적 스플래시 이후로 SplashPage를 띄우고 유지된다.  





이제 Splash 화면을 유지한 이유가 있을 것이다.  
보통 메인 화면으로 전환하기 전에 초기 설정값 로딩, 로그인 확인, 버전체크 등의 작업을 처리한다.  

이런 초기 작업은 `StatefulWidget`의 `initState()`에서 처리되며, 내부적으로 비동기 함수로 분리하는 경우가 많다.



```dart
@override
void initState() {
  super.initState();
  _initialize(); // 초기 작업 실행
}

Future<void> _initialize() async {
  // 예: 초기 데이터 로딩
  await Future.delayed(Duration(seconds: 2)); // 예시용 딜레이
  
  if (!mounted) return; // context 유효성 확인
  Navigator.of(context).pushReplacement(
    MaterialPageRoute(builder: (_) => const HomePage()),
  );
}
```

- `Future<void>`로 선언된 비동기 초기화 함수는 `await`로 동작하며, 그 사이에 위젯이 dispose될 수 있으므로 `if (!mounted)` 체크는 필수다.


<br><br>
---

### 3. 스플래시 종료

스플래시에서 필요한 작업이 끝난 후, 홈 화면 등으로 전환이 필요합니다.  
기본적으로 아래 두 가지 방식 중 하나를 사용합니다:

- `pushReplacement`: 스택의 현재 화면(Splash)을 제거하고 새 화면으로 교체
- `pushAndRemoveUntil`: 전체 스택을 비우고 새 화면으로 이동
> 각 방식의 예제, 스택 구조, 뒤로가기 대응 등은  
> 👉 [[Flutter_0400_Navigator_Basics.md]] 문서 참고

<br><br>

---


## 동적 스플래시 - Android 스타일 접근

위에서 설명한 방식은 iOS 스타일의 진입 구조였다.  
이제 Android 앱처럼 메인 콘텐츠(WebView 등)를 먼저 그리고, 그 위에 Splash를 레이어로 덮는 구조도 고려해볼 수 있다.

이 방식은 WebView 앱에서 흔히 사용되는 패턴이다.  
WebView를 포함한 실제 콘텐츠가 먼저 그려지고, 그 위에 Splash 화면이 `Stack`, `Overlay`, 또는 `AnimatedSwitcher` 등을 이용해 임시로 보여진다.  

보통의 흐름은 다음과 같다:

1. `MainPage`가 먼저 로드되고 내부에 WebView 또는 앱 핵심 뷰가 존재한다.
2. 그 위에 Splash용 위젯을 배치하여 화면을 덮는다.
3. 초기화 완료 또는 WebView의 특정 조건이 만족되면 Splash 위젯을 제거한다.

```dart
class MainPage extends StatefulWidget {
  const MainPage({super.key});

  @override
  State<MainPage> createState() => _MainPageState();
}

class _MainPageState extends State<MainPage> {
  bool _isSplashVisible = true;

  @override
  void initState() {
    super.initState();
    _init();
  }

  Future<void> _init() async {
    // 예: WebView 초기화, 토큰 체크 등
    await Future.delayed(const Duration(seconds: 2));
    setState(() => _isSplashVisible = false);
  }

  @override
  Widget build(BuildContext context) {
    return Stack(
      children: [
        const WebViewWidget(), // 실제 콘텐츠
        if (_isSplashVisible)
          Positioned.fill(
            child: Image.asset(
              'assets/images/splash.jpg',
              fit: BoxFit.cover,
            ),
          ),
      ],
    );
  }
}
```

이 방식은 Splash가 `메인 콘텐츠 내부`에 포함되어 컨트롤되는 점이 특징이다.  
명확한 페이지 전환이 없고, `레이어 제거`의 개념으로 동작한다.

> ✅ 장점: Splash가 부가적인 느낌을 주며, 자연스러운 전환 가능  
> ❌ 단점: 라우팅 흐름과 분리되어 있으며, 유지보수 측면에서 복잡도 증가 가능



<br><br>
---

## HISTORY
- 2560626: 초안작성
