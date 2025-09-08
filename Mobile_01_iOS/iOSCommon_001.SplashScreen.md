# iOS - 스플래시 화면 구현 가이드 (정적 & 동적)

이 문서는 iOS 앱 개발에서 **스플래시 화면(Splash Screen)** 을 정적/동적으로 구현하는 방법을 설명합니다.  
스플래시의 기본 역할에 대한 설명은 별도 공통 문서에서 다루므로, 이 문서에서는 실질적인 구현 방법과 구조 설계에 중점을 둡니다.

<br>

## 1. 정적 스플래시 구현 (Launch Screen)

iOS는 앱 실행 시 시스템 레벨에서 자동으로 초기 화면(Launch Screen)을 표시합니다.  
이 화면은 앱이 메모리에 올라오는 동안 사용자에게 빈 화면 대신 보여주는 초기 인트로 역할을 합니다.

### 📌 설정 방법

- **Launch Screen.storyboard** 활용
    - 기본 Xcode 프로젝트 생성 시 포함됨
    - 앱 실행 직후 자동으로 표시되며 첫 ViewController가 나타날 때까지 유지됨
- **Assets.xcassets > LaunchImage**
    - 구버전(iOS 12 이하) 대응용 이미지 세트
- **Info.plist 설정**
    - `UILaunchStoryboardName` 키에 `LaunchScreen` 파일명을 명시

> 정적 스플래시는 앱이 느리게 시작될 경우에도 사용자에게 빠른 반응감을 주는 데 효과적입니다.

<br><br>

---

## 2. 동적 스플래시 구현 (Dynamic Splash)

정적 스플래시는 앱 코드 실행 전에 자동으로 표시되며 제어할 수 없습니다.  
반면 **동적 스플래시**는 앱이 실행된 이후, 사용자가 앱의 메인 화면을 보기 전까지의 UI 흐름을 앱이 직접 제어합니다.

일반적으로 `SplashViewController`를 별도로 생성해 정적 스플래시와 동일한 화면을 다시 구성하고,  
아래와 같은 초기 작업이 완료될 때까지 유지합니다:

- 서버 API 호출
- 사용자 인증 상태 확인
- 초기 데이터 다운로드
- 애니메이션 또는 로딩 효과 처리

### ✅ 동적 스플래시 구현 방식 요약

- 정적 스플래시와 동일한 UI를 앱 첫 화면에 다시 구현하여 전환 이질감 최소화
- SplashViewController 내에서 로딩, 인증, 조건 분기 등을 처리
- 서버에서 이미지, 공지사항, 동영상, 앱 버전 정보 등을 받아 표시하는 형태도 포함

<br><br>

### 2-1. 스토리보드 기반 Auto Layout (Interface Builder 방식)

`SplashViewController`를 스토리보드에서 시각적으로 구성하는 방식입니다.

1. **ViewController 추가 및 Identifier 설정**
   - Main.storyboard 또는 별도 storyboard에 "SplashViewController" 추가

2. **앱 진입 화면으로 설정**
   - SceneDelegate에서 rootViewController로 설정:
     ```swift
     let storyboard = UIStoryboard(name: "Main", bundle: nil)
     let splashVC = storyboard.instantiateViewController(withIdentifier: "SplashViewController")
     window?.rootViewController = splashVC
     window?.makeKeyAndVisible()
     ```

3. **Auto Layout을 이용한 UI 구성**
   - 로고 이미지, 배경 색상, 인디케이터 등을 Interface Builder에서 제약 조건으로 배치

> 시각적인 레이아웃 구성이 쉬워 디자이너 협업 시 유리합니다.

<br>

### 2-2. 코드 기반 Auto Layout (Programmatic 방식)

모든 UI 요소와 제약 조건을 코드로 작성합니다. 다양한 기기와 동적 처리에 적합합니다.

```swift
class SplashViewController: UIViewController {
    let logoImageView: UIImageView = {
        let imageView = UIImageView(image: UIImage(named: "splash_logo"))
        imageView.translatesAutoresizingMaskIntoConstraints = false
        return imageView
    }()

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .white
        view.addSubview(logoImageView)

        NSLayoutConstraint.activate([
            logoImageView.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            logoImageView.centerYAnchor.constraint(equalTo: view.centerYAnchor),
            logoImageView.widthAnchor.constraint(equalToConstant: 150),
            logoImageView.heightAnchor.constraint(equalToConstant: 150)
        ])
    }
}
```

> 코드 기반은 다크 모드, 회전, 동적 콘텐츠 대응이 유리하며, 재사용성과 테스트 가능성이 높습니다.

<br>

### 2-3. 네트워크 기반 Splash 흐름 예시

서버 통신은 프로젝트 구조에 따라 다양한 방식으로 구현됩니다.

- 직접 `URLSession`을 통해 요청을 만들 수도 있고
- 추상화된 `APIService` 구조를 통해 유지보수성을 높일 수도 있습니다.

여기서는 흐름의 예시만 소개하며, 통신 로직의 구체적인 구현은 별도 네트워크 처리 가이드 문서를 참고하세요.

<br><br>

---

## 3. 스플래시 종료 및 Main 화면 전환

초기 작업이 완료되면 스플래시를 종료하고 앱의 주요 화면으로 전환해야 합니다.  
전환 방식은 목적과 구조에 따라 선택됩니다.

<br>

### 3-1. SplashVC 제거 후 MainVC를 Root로 교체

```swift
let mainVC = MainViewController()
window?.rootViewController = mainVC
```

- 메모리 상에서 SplashVC 제거됨 (일반적인 방식)
- 되돌아갈 필요 없고, 앱 흐름이 단방향일 때 적합

<br>

### 3-2. SplashVC 위에 MainVC를 Present (Splash 유지)

```swift
let mainVC = MainViewController()
splashVC.present(mainVC, animated: false)
```

- SplashVC를 백그라운드에 남겨 상태 체크 등을 계속 진행 가능
- 예: 지속적인 버전 상태 체크, 글로벌 상태 감시 등


<br><br>

### 전환 방식 요약 비교

| 전환 방식      | 특징                       | 적합한 상황                     |
|----------------|----------------------------|----------------------------------|
| Root 교체      | 깔끔하게 스플래시 제거     | 초기화 작업 후 일반적인 전환 시 |
| Present 방식   | SplashVC가 계속 유지됨     | 글로벌 감시/백그라운드 필요 시 |

<br><br>

---


## HISTORY
- 260626: 초안작성
