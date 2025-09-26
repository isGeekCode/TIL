# Info.plist : (값 가져오기, 권한)

## 1. 개요
Info.plist 파일은 iOS 앱의 설정 파일 중 하나로, 앱에 대한 기본 정보를 포함합니다. 이 파일은 앱의 이름, 버전, 빌드 번호, 아이콘 파일 이름, 사용 권한 등 앱 실행에 필요한 다양한 정보를 담고 있습니다. iOS 시스템은 앱을 설치하고 실행할 때 이 정보를 참고합니다.

Info.plist 파일은 iOS 앱 번들의 루트 디렉토리에 위치하며, XML 형식으로 작성됩니다. 일반적으로 Xcode에서 자동으로 생성되지만, 개발자가 직접 작성하거나 수정할 수도 있습니다.

---

## 2. Info.plist 파일의 위치와 타겟 관계
Info.plist 파일은 여러 위치에 존재할 수 있습니다.

- 프로젝트 루트 디렉토리에 있는 Info.plist 파일
- Xcode 프로젝트 내 각 타겟(Target)의 Info.plist 파일

보통 이 두 파일은 동일하지만, 타겟별로 다른 Info.plist 파일을 지정할 수도 있습니다. 예를 들어, 개발 환경과 배포 환경에 따라 서로 다른 Info.plist를 사용할 수 있으며, Xcode 설정에서 Info.plist 파일 위치를 변경할 수도 있습니다.

따라서, Info.plist를 수정하거나 확인할 때는 현재 작업 중인 타겟의 Info.plist 파일을 기준으로 하며, 루트 디렉토리의 파일과 일치하는지 확인하는 것이 좋습니다.

---

## 3. Target Info 탭과 Info.plist 파일의 관계
Xcode의 Target → Info 탭(Custom iOS Target Properties)에서 보이는 값과 실제 Info.plist 파일의 내용은 본질적으로 연결되어 있습니다. 다만, Info.plist에는 `$(PRODUCT_BUNDLE_IDENTIFIER)`와 같은 **치환 매크로**가 포함되어 있고, Target Info 탭에서는 빌드 설정에 의해 치환된 실제 값이 표시됩니다.

즉, 두 곳은 같은 소스를 바라보지만, "원본 매크로 vs 치환된 결과"라는 차이로 값이 다르게 보일 수 있습니다.

- **Info.plist 파일**: 원본 정의, 매크로 값 유지  
- **Target Info 탭**: 빌드 세팅이 적용된 결과를 UI로 표시  

최종적으로 앱에 반영되는 값은 빌드 결과물(.app 번들 내부)의 Info.plist에서 확인해야 합니다.

---

## 4. Info.plist에 자주 포함되는 주요 항목
Info.plist에는 앱을 만들 때 기본적으로 다음과 같은 키들이 포함됩니다. 주니어 개발자라면 최소한 이 항목들을 이해하는 것이 좋습니다.

- **CFBundleIdentifier** : 앱의 고유 식별자 (예: com.company.appname)
- **CFBundleName / CFBundleDisplayName** : 앱 이름, 홈 화면에 표시되는 이름은 DisplayName으로 지정
- **CFBundleShortVersionString** : 사용자에게 보이는 앱 버전 (예: 1.0.0)
- **CFBundleVersion** : 빌드 번호 (내부 관리용, 앱스토어 제출 시 필수)
- **CFBundleExecutable** : 실행 파일 이름 (일반적으로 자동 생성)
- **LSRequiresIPhoneOS** : 앱이 반드시 iOS 환경에서 실행되어야 함을 명시
- **UIRequiredDeviceCapabilities** : 앱 실행에 필요한 하드웨어 기능 지정 (예: camera, gps)
- **UIBackgroundModes** : 백그라운드에서 동작이 필요한 경우 지정 (예: audio, fetch, location)
- **NSCameraUsageDescription / NSPhotoLibraryUsageDescription 등** : 개인정보 접근 권한 요청 문구 (필수)
- **CFBundleURLTypes** : 앱에서 지원하는 URL 스킴, 다른 앱에서 이 앱을 열 수 있게 함
- **UIApplicationSceneManifest** : SceneDelegate 및 멀티 윈도우 관련 설정

이 외에도 앱 기능에 따라 다양한 키들이 추가될 수 있습니다.

---

## 5. 프로젝트 생성 직후 기본 구성 (템플릿 기준)

### 자동으로 채워지는 값 (Generate Info.plist File = Yes)
Xcode에서 새 iOS 앱 프로젝트를 생성하면, 기본 템플릿은 아래 항목들을 Build Settings에 입력된 값에 따라 자동으로 Info.plist에 반영합니다.

- **CFBundleIdentifier** ← `PRODUCT_BUNDLE_IDENTIFIER`
- **CFBundleName** ← `PRODUCT_NAME`
- **CFBundleExecutable** ← `EXECUTABLE_NAME`
- **CFBundlePackageType** ← `APPL`
- **CFBundleShortVersionString** ← `MARKETING_VERSION`
- **CFBundleVersion** ← `CURRENT_PROJECT_VERSION`
- **LSRequiresIPhoneOS** ← 기본 포함
- **UISupportedInterfaceOrientations** ← 템플릿 기본값 (보통 Portrait)

### 템플릿 기본으로 포함되는 항목 (파일/Info 탭에서 확인 가능)
- **UIApplicationSceneManifest**
  - `UIApplicationSupportsMultipleScenes` (기본 false)
  - `UISceneConfigurations` → Application Role에 대한 `SceneDelegate` 지정
- **UIMainStoryboardFile** : `Main`
- **UILaunchStoryboardName** : `LaunchScreen`

위 항목들은 Generate Info가 켜져 있으면 최종 Info.plist에 병합됩니다.

### 개발자가 직접 추가/관리해야 하는 항목 (필수 아님, 앱 기능에 따라)
- **권한(Privacy)** : `NSCameraUsageDescription`, `NSPhotoLibraryUsageDescription`, `NSLocationWhenInUseUsageDescription` 등
- **백그라운드 모드** : `UIBackgroundModes` (audio/fetch/location 등)
- **URL 스킴** : `CFBundleURLTypes`
- **필요 기능** : `UIRequiredDeviceCapabilities` (예: camera, gps)
- **쿼리 스킴(iOS 9+)** : `LSApplicationQueriesSchemes` (다른 앱 스킴 열람 시)

### 최소 Info.plist 예시 (슬림 형태)
Generate Info가 켜져 있고, 커스텀은 URL 스킴만 사용하는 경우:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>CFBundleURLTypes</key>
  <array>
    <dict>
      <key>CFBundleTypeRole</key>
      <string>Editor</string>
      <key>CFBundleURLSchemes</key>
      <array>
        <string>escapelock</string>
      </array>
    </dict>
  </array>
</dict>
</plist>
```

---

## 6. 변경 시 주의사항
Info.plist 파일은 앱 실행 중에 읽혀서 필요한 정보를 가져오기 때문에, 파일 내용이 변경되면 반드시 앱을 다시 빌드해야 변경 사항이 반영됩니다.

---

## 7. 코드에서 Info.plist 값 가져오기

앱 내에서 Info.plist에 정의된 값을 읽어올 때는 `Bundle.main.infoDictionary`를 사용합니다.

### Swift 예시
```swift
if let infoDict = Bundle.main.infoDictionary {
    // Info.plist에서 값을 가져와서 사용
    let version = infoDict["CFBundleShortVersionString"] as? String
    let build = infoDict["CFBundleVersion"] as? String
    // ...
}
```

### Objective-C 예시
```objective-c
NSDictionary *infoDict = [[NSBundle mainBundle] infoDictionary];
NSString *version = [infoDict objectForKey:@"CFBundleShortVersionString"];
NSString *build = [infoDict objectForKey:@"CFBundleVersion"];
// ...
```

---

이 가이드는 Info.plist 파일의 역할과 구조, Xcode 내에서의 위치 및 관리 방법, 그리고 앱에서의 활용법을 이해하는 데 도움을 주기 위해 작성되었습니다.
