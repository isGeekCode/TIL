# Info.plist : (값 가져오기, 권한)

앱의 설정 파일 중 하나로, 앱에 대한 기본 정보를 포함한다.

이 파일은 앱의 이름, 버전, 빌드 번호, 아이콘 파일 이름, 사용 권한 등을 포함하며, 

iOS 시스템에서 앱을 설치하고 실행할 때 필요한 정보를 제공한다.

Info.plist 파일은 iOS 앱 번들의 루트 디렉토리에 위치하고 XML 형식으로 작성된다.

앱 개발자가 직접 작성할 수도 있지만, 일반적으로 Xcode에서 자동으로 생성된다.

## 변경이 사항이 있다면
앱 실행 중에 Info.plist 파일을 읽어들여서 필요한 정보를 가져오기 때문에

Info.plist 파일의 내용이 변경되면 앱을 다시 빌드해야 한다.

## Info.plist의 정보 가져오기
### 사용법

아래는 앱버전과 빌드버전을 가져오는 코드 예시.
- **Swift**  
`Bundle.main.infoDictionary`를 이용한다.
```
if let infoDict = Bundle.main.infoDictionary {
    // Info.plist에서 값을 가져와서 사용.
    let version = infoDict["CFBundleShortVersionString"] as? String
    let build = infoDict["CFBundleVersion"] as? String
    // ...
}
```
- **Objective - C**  
Objective-C에서는 NSBundle 클래스를 사용하여 Info.plist의 값을 가져올 수 있다.
```
NSDictionary *infoDict = [[NSBundle mainBundle] infoDictionary];
NSString *version = [infoDict objectForKey:@"CFBundleShortVersionString"];
NSString *build = [infoDict objectForKey:@"CFBundleVersion"];
// ...

```

### AppVersion 가져오기
아래 링크 참고
- [TIL : AppVersion 가져오기](https://github.com/isGeekCode/TIL/blob/main/Xcode/InfoPlist_appVersion.md)


## 접근권한
- [TIL : 여러가지 접근권한](https://github.com/isGeekCode/TIL/blob/main/Xcode/PrivercyPermission_various.md)
