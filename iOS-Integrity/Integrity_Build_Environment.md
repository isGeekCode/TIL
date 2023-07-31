# Integrity - 앱 설치환경 체크

****애플리케이션이 신뢰할 수 있는 소스에서 설치되었나요?****

무결성관련 체크를 위해 빌드환경을 체크해야하는 상황이 생긴다. 

이 앱이 앱스토어에서 빌드했는지, 테스트플라잇인지, 로컬인지를 확인할 수 있도록 말이다. 

앱소스를 정확하게 식별하기 위해서는 몇단계의 검증을 거친다.

- **모바일 프로비저닝 프로파일의 존재여부**
- **App Store 영수증 데이터 파일 분석**
- **샌드박스 영수증 데이터 파일 분석** – 앱이 TestFlight를 통해 배포되었을 때 표시됨

### 첫번째 검증조건: isSimulator

시뮬레이터인지 디바이스인지 체크하는 Bool값

```swift
    private func isSimulator() -> Bool {
        
        #if arch(i386) || arch(x86_64)
        return true
        #else
        return false
        #endif
    }
```

### 두번째 검증조건: isAppStoreReceiptSandbox

- 앱스토어영수증이 있는지 체크하는 Bool값
- 사용자가 App Store에서 앱을 다운로드한 경우, 앱에는 영수증이 항상 존재한다.
- 샌드박스에서 앱이 Xcode 또는 Testflight를 사용하여 설치한 경우, 구매가 완료될 때까지 영수증이 없다.
- 테스트플라잇을 통해 배포되었을때 내용을 확인할 수 있다.

‼️ 영수증 이름은 언제든지 변경될 수 있기 때문에  이것 하나로는 매우 취약한 솔루션이다.

 `appStoreReceiptURL.lastPathComponent == "sandboxReceipt"`

Step1. 시뮬레이터체크

Step2. Bundle.main의 `appStoreReceiptURL`이 있는지 확인

Step3. 그 URL에 `sandboxReceipt`가 있는지 확인

```swift
    private func isAppStoreReceiptSandbox() -> Bool {
        
        if isSimulator() {
            return false
        } else {
            guard let url = Bundle.main.appStoreReceiptURL else {
                return false
            }
// 혹은 FileManager.default.fileExists(atPath: Bundle.main.appStoreReceiptURL.path)

            guard url.lastPathComponent == "sandboxReceipt" else {
                return false
            }
            return true
        }
    }
```

### 세번째 검증조건: hasEmbeddedMobileProvision

**모바일 프로비저닝 파일이 nil이라면 true를 리턴하는 Bool값**

- mobileProvision 파일은 Ad-Hoc 배포에 대한 명확한 지표이다.
- embedded.mobileprovision 파일이 있는 경우 .ipa 파일은 Apple App Store에서 가져온 것이 아님
- mobileProvision 파일을 통해 앱스토어가 아니라 개발자가 배포한 앱을 설치할 수 있다.
- MobileProvision에 대해 간단한 정리가 되어있는 naljin님 링크 [[여기]](https://sujinnaljin.medium.com/ios-%ED%94%84%EB%A1%9C%EB%B9%84%EC%A0%80%EB%8B%9D-%ED%94%84%EB%A1%9C%ED%8C%8C%EC%9D%BC%EC%9D%B4%EB%9E%80-ipa%EC%97%90%EC%84%9C-%EA%B9%8C%EB%B3%B4%EA%B8%B0-ccf629e4c68a)

```swift
// Bundle.main.path(forResource: "embedded", ofType: "mobileprovision") != nil

private func hasEmbeddedMobileProvision() -> Bool {
    guard Bundle.main.path(forResource: "embedded", ofType: "mobileprovision") == nil else {
        return true
    }
    return false
}
```

# SourceCode

```swift
extension UIApplication {
    
    // MARK: Public
    func isRunningInTestFlightEnvironment() -> Bool {
        if isSimulator() {
            return false
        } else {
            if isAppStoreReceiptSandbox() && !hasEmbeddedMobileProvision() {
                return true
            } else {
                return false
            }
        }
    }
    
    func isRunningInAppStoreEnvironment() -> Bool {
        if isSimulator(){
            return false
        } else {
            if isAppStoreReceiptSandbox() || hasEmbeddedMobileProvision() {
                return false
            } else {
                return true
            }
        }
    }

    // MARK: Private
    private func hasEmbeddedMobileProvision() -> Bool {
        guard Bundle.main.path(forResource: "embedded", ofType: "mobileprovision") == nil else {
            return true
        }
        return false
    }
    
    private func isAppStoreReceiptSandbox() -> Bool {
        
        if isSimulator() {
            return false
        } else {
            guard let url = Bundle.main.appStoreReceiptURL else {
                return false
            }
            guard url.lastPathComponent == "sandboxReceipt" else {
                return false
            }
            return true
        }
    }
    
    private func isSimulator() -> Bool {
        
        #if arch(i386) || arch(x86_64)
        return true
        #else
        return false
        #endif
    }
}
```

# **Reference**

- [https://iosdevblog.com/2021/01/13/is-the-application-installed-from-a-trusted-source/](https://iosdevblog.com/2021/01/13/is-the-application-installed-from-a-trusted-source/)
- [https://gist.github.com/SergLam/609e2dc76b9f321877f4fb7fe8e26fdf](https://gist.github.com/SergLam/609e2dc76b9f321877f4fb7fe8e26fdf)

**mobileProvision**

- [https://sujinnaljin.medium.com/ios-프로비저닝-프로파일이란-ipa에서-까보기-ccf629e4c68a](https://sujinnaljin.medium.com/ios-%ED%94%84%EB%A1%9C%EB%B9%84%EC%A0%80%EB%8B%9D-%ED%94%84%EB%A1%9C%ED%8C%8C%EC%9D%BC%EC%9D%B4%EB%9E%80-ipa%EC%97%90%EC%84%9C-%EA%B9%8C%EB%B3%B4%EA%B8%B0-ccf629e4c68a)
- [https://engineering.linecorp.com/ko/blog/ios-code-signing/](https://engineering.linecorp.com/ko/blog/ios-code-signing/)
