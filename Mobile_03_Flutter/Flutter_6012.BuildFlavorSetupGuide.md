# Flutter – Flavor를 이용한 빌드 환경 분리

`Flavor`는 Flutter에서 **빌드 환경(개발, 운영 등)을 명확하게 구분**하기 위한 기능입니다. 각 환경에 따라 앱의 아이콘, 번들 ID, API 주소, 설정 파일 등을 독립적으로 설정할 수 있으며, 빌드 시점에 원하는 환경을 선택하여 실행하거나 배포할 수 있습니다.

이 문서는 Flutter 프로젝트에서 `Flavor`를 활용해 `prd`, `dev`, `staging` 환경을 구분하는 방법을 설명합니다.

<br><br>

---

## 🎯 목적

- 빌드 대상에 따라 API 주소, 앱 이름, 번들 ID, 아이콘 등을 분리하여 관리  
- 운영/개발/스테이징 환경을 명확히 나누고 실수 방지  
- `--dart-define`보다 구조적인 환경 분리를 구현  

<br><br>

---

## 🧱 환경 예시

| 환경 | 설명 | 예시 도메인 |
|------|------|--------------|
| `prd` | 운영 | `https://api.example.com` |
| `dev` | 개발 | `https://dev.example.com` |
| `staging` | 중간 테스트 | `https://stg.example.com` |

<br><br>

---

## 📁 프로젝트 구조 예시

```
lib/
├── main_prd.dart        # 방법 ①: 환경별 main 파일 분리 방식
├── main_dev.dart
├── main_staging.dart
├── main.dart            # 방법 ②: 하나의 main.dart에서 분기 처리하는 방식
└── config/
    └── env_config.dart
```

<br><br>

---


## 🧩 코드 구성 예시

### `flavor_config.dart`

```dart
enum Flavor { prd, dev, staging }

class FlavorConfig {
  static late Flavor _flavor;

  static void setFlavor(Flavor flavor) {
    _flavor = flavor;
  }

  static String get baseUrl {
    switch (_flavor) {
      case Flavor.dev:
        return 'https://dev.example.com';
      case Flavor.staging:
        return 'https://stg.example.com';
      case Flavor.prd:
      default:
        return 'https://api.example.com';
    }
  }

  static bool get isDev => _flavor == Flavor.dev;
  static bool get isPrd => _flavor == Flavor.prd;
  static bool get isStaging => _flavor == Flavor.staging;
}
```

<br><br>

---

## 🧪 main 파일 예시 : 타겟별 main 파일처리– `main_dev.dart`

```dart
import 'package:flutter/material.dart';
import 'config/env_config.dart';

void main() {
  FlavorConfig.setFlavor(Flavor.dev);
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: '개발 환경',
      home: Scaffold(
        appBar: AppBar(title: const Text('DEV')),
        body: Center(child: Text('Base URL: ${FlavorConfig.baseUrl}')),
      ),
    );
  }
}
```

<br><br>

---

## 🧪 main 파일 예시 – 하나의 `main.dart`에서 Flavor 분기

`lib/main.dart` 파일 하나에서 환경을 런타임에 분기 처리할 수 있습니다.

```dart
import 'package:flutter/material.dart';
import 'config/flavor_config.dart';

void main() {
  const flavor = String.fromEnvironment('FLAVOR', defaultValue: 'prd');

  switch (flavor) {
    case 'dev':
      FlavorConfig.setFlavor(Flavor.dev);
      break;
    case 'staging':
      FlavorConfig.setFlavor(Flavor.staging);
      break;
    case 'prd':
    default:
      FlavorConfig.setFlavor(Flavor.prd);
      break;
  }

  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flavor 앱',
      home: Scaffold(
        appBar: AppBar(title: const Text('환경: FLAVOR')),
        body: Center(child: Text('Base URL: ${FlavorConfig.baseUrl}')),
      ),
    );
  }
}
```

실행 예시:

```bash
flutter run --flavor dev --dart-define=FLAVOR=dev -t lib/main.dart


flutter run --flavor prd --dart-define=FLAVOR=prd -t lib/main.dart

```

하지만 이때, 빌드환경(configuration)이 각 OS별로 설치되어야 해당 환경으로 실행을 할 수 있다.  


<br><br>

---

## ⚙️ Android 설정 – `build.gradle`
### 1. `build.gradle`
```gradle

// 코틀린인 경우 : build.gradle.kts 수정
android {
    ...
    flavorDimensions += "app"

    productFlavors {
        create("prd") {
            dimension = "app"
            applicationIdSuffix = ".prd"
            versionNameSuffix = "-prd"
            resValue("string", "app_name", "Flavors Prd")
        }
        create("dev") {
            dimension = "app"
            applicationIdSuffix = ".dev"
            versionNameSuffix = "-dev"
            resValue("string", "app_name", "Flavors Dev")
        }
        create("staging") {
            dimension = "app"
            applicationIdSuffix = ".stg"
            versionNameSuffix = "-staging"
            resValue("string", "app_name", "Flavors Staging")
        }
    }
}



android {
  ...
  flavorDimensions "app"
  productFlavors {
    dev {
      dimension "app"
      applicationIdSuffix ".dev"
      versionNameSuffix "-dev"
    }
    staging {
      dimension "app"
      applicationIdSuffix ".stg"
      versionNameSuffix "-stg"
    }
    prd {
      dimension "app"
    }
  }
}
```

### 2. `AndroidManifest.xml` 수정하기

android/app/src/main/AndroidManifest.xml  수정하기

```

 <application
        android:label="@string/app_name"

```



<br><br>

---

## ⚙️ iOS 설정

플러터 명령어 `flutter run --flavor dev`는 아래와 같은 의미를 가진다. 

- Xcode의 Build Configuration 이름 중에 Debug-dev를 찾는다. 

###  – Xcode Scheme 구성

1. Xcode 열기: `ios/Runner.xcworkspace`  
2. 메뉴 → Product → Scheme → New Scheme (dev, staging, prd 각각 생성)  
    - 이름을 동일하게 맞춰야한다.  
3. 각 Scheme에서 `Build Configuration`을 환경에 맞게 설정  
4. `Info.plist`의 `Bundle Identifier`를 환경마다 다르게 설정

- prd : 생성한 타겟명
    - Run     : Debug-prd
    - Test    : Debug-prd
    - Profile : Profile-prd
    - Analyze : Debug-prd
    - Archive : Release-prd

- dev
    - Run     : Debug-dev
    - Test    : Debug-dev
    - Profile : Profile-dev
    - Analyze : Debug-dev
    - Archive : Release-dev

- staging
    - Run     : Debug-staging
    - Test    : Debug-staging
    - Profile : Profile-staging
    - Analyze : Debug-staging
    - Archive : Release-staging


<br><br>

### Target-BuildSettings 추가
Build Settings에서 + 버튼을 눌러서 add User-Defined Setting을 누른다. 

변수명은 APP_DISPLAY_NAME 으로 생성한다. 
그리고 원하는 앱이름을 매핑한다. 
- APP_DISPLAY_NAME
    - Debug
    - Debug-dev : 앱이름-dev
    - Debug-prd : 앱이름
    - Debug-staging : 앱이름-staging
    - Profile
    - Profile-dev : 앱이름-dev
    - Profile-prd : 앱이름
    - Profile-staging : 앱이름-staging
    - Release
    - Release-dev : 앱이름-dev
    - Release-prd : 앱이름
    - Release-staging : 앱이름-staging
<br><br>

### Info.plist
CFBundleDisplayName 수정

```
<dict>
...
    <key>CFBundleDisplayName</key>
    <string>$(APP_DISPLAY_NAME)</string>
...
</dict>
</plist>

```



---


## 🚀 실행 및 빌드 

### 명령어로 빌드처리

아래 명령어들은 Flavor별로 앱을 실행하거나 빌드할 때 사용하는 명령입니다.

- `--flavor`: Android의 `build.gradle`에 정의된 `productFlavors` 중 어떤 flavor를 사용할지 지정합니다. 예: `dev`, `staging`, `prd`
- `-t`: `target`의 약자로, 실행할 진입점(main 함수가 정의된 Dart 파일)을 명시합니다. 예: `lib/main_dev.dart`, `lib/main_prd.dart`
- 즉, `--flavor`는 플랫폼 빌드 구성을 선택하고, `-t`는 Flutter 앱의 실행 진입점을 지정합니다.

참고로 `--flavor`에 지정된 문자열은 `enum Flavor { ... }`와 직접 연결되진 않으며, iOS에서는 Xcode의 Scheme 이름과 매칭되도록 구성해야 합니다.

```bash
// entrypoint가 다를 경우
flutter run --flavor dev -t lib/main_dev.dart
flutter run --flavor prd -t lib/main_prd.dart
flutter run --flavor staging -t lib/main_staging.dart

// 같을 경우
flutter run --flavor dev -t lib/main.dart
flutter run --flavor prd -t lib/main.dart
flutter run --flavor staging -t lib/main.dart
```

```bash
// entrypoint가 다를 경우
flutter build ios --flavor prd -t lib/main_prd.dart
flutter build apk --flavor dev -t lib/main_dev.dart
```

<br><br>

---

## Flutter IDE에서 GUI를 통한 빌드


![](https://i.imgur.com/n6qgwEh.png)

<br>

IDE에서 Edit Configurations를 누른다. 

기존 실행하던 main.dart를 복제하여 원하는 이름으로 설정한다. 

우측 입력창을 수정한다. 

- Name: Configuration 이름
- Dart entrypoint: main함수가 실행될 파일경로
- Additional run args: 
    - entrypoint가 다를 경우
        - `--flavor prd -t lib/main_prd.dart --dart-define=FLAVOR=prd`
        - `--flavor dev -t lib/main_dev.dart --dart-define=FLAVOR=dev`
        - `--flavor staging -t lib/main_staging.dart --dart-define=FLAVOR=staging`
    - entrypoint가 같을 경우
        - `--flavor prd -t lib/main.dart --dart-define=FLAVOR=prd`
        - `--flavor dev -t lib/main.dart --dart-define=FLAVOR=dev`
        - `--flavor staging -t lib/main.dart --dart-define=FLAVOR=staging`
- Build flavor
    - prd
    - dev
    - staging


![](https://i.imgur.com/SNyuRKJ.png)
<br>

<br><br>

---


## HISTORY
- 260623 : 초안작성
