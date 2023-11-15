# 23년 7월 회고 / 8월 목표

### 이번달 목표

- iOS관련 커뮤니티 행사에서 할수있는 것을 하기
    - 부산 iOS IGA 세션발표
    - KWDC23 진행 스텝 업무
- WWDC23에서 새롭게 나온 것들 살펴보기
- 깃헙 README 자동화 업그레이드
- iOS기본기 닦기
    - 로드맵 갱신하기
    - 체크리스트대로 진행하기

<br><br>

## 업무 성과

- 앱내 로고 관리 시스템 구축
    - 행사때마다 로고이미지를 추가하여 배포하는 작업을 API로 동작하도록 변경하였다.
    - 그로 인해 관련 작업에 대한 iOS 앱 배포 심사를 생략할  수 있었고 2-3일의 시간을 세이브
    - 한 기능에 대하여 API구조설계부터 일정 조율까지 웹팀, 안드로이드팀, iOS팀의 업무를 조율해보는 경험.
- 하이브리드 프로젝트에서 웹스키마, 쿼리를 사용하여 ViewController를 웹에서 관리할 수 있도록 했다.
    - 해당 작업으로 특별한 케이스에 대한  iOS 앱 배포 심사를 생략할  수 있었고 2-3일의 시간을 세이브

<br><br><br>

## 기여활동

### 부산 iOS IGA에서 스피커로 참여

- 세션명 : 기타리스트에서 swift 개발자가된 이야기 그리고 무결성(Apple DeviceCheck API 사용하기)
- 일시 : 23년 7월 8일
- 단체명 : 부산 iOS iGA
- 내용
    1. 기타리스트에서 iOS개발자로
        - 전직 기타리스트에서 어떻게 iOS개발자로 이직할 수 있었는지에 대하여
        - 늦게 시작한 커리어에서 빠르게 성장하기 위한 전략
    2. 기술공유 : Apple에서 제공해준 DeviceCheck API
        - 앱을 재설치해도 애플서버로부터 값을 가져올 수 있는 방법
- 느낀 점
    - 스피커 경험에 있어서 두번째 경험인데, 준비하는 스케쥴관리가 생각보다 어려웠다.
    - 스토리텔링이 매끄럽지않아서 전날 다소 수정하였다.
    - 사람들이 뭘 궁금해 하는지에 대하여 고민해 볼 수 있던 시간이었다.
    - 사람들에게 내 고민의 결과를 들려주는 것이 생각보다 즐거웠다. → 난 무대체질인가 보다.
    - 음악교육 15년 경력이 여기에도 많은 도움이 됐다.

- 이번 기회를 통해 얻은 새로운 목표
    - 정기적으로 발표기회를 갖고 싶다.
        - 새로운 기술을 정리하고 설명하는 과정에서 스스로에게 정말 많은 도움이 됐다.
    - iOS관련 교육을 해보고 싶다.
        - 나도 다른 사람에게 도움을 받아 공부했기에, 나도 공유하고 싶다.

### KWDC23 스텝 참여
- 국내 최초 최대 규모의 IOS 컨퍼런스에 자원봉사자로 참여해서 세션장소 관리를 진행
- 짧은평
    - 모든 준비는 아니었지만, 스텝수준의 준비과정부터 마지막까지, 행사장의 보이지 않는 곳에서 일해보니 정말 많은 개발자들이 보였다. 준비하는 과정 중에서도 오거나이저들의 열정이 보였다. 더 어렸고, 결혼하기 이전이었더라면 함께 하고 싶다고 몸을 던졌을 정도로 멋진 단체였다.
- 느낀 점
    - 다양한 사람들을 만나면서 네트워킹을 할 수 있었다.
    - 특히 스피커들을 만나기 전에 이 사람들의 이전 발표들을 미리 보고 갔었고, 정말 존경스러웠다.
        - 나도 언젠간 이런 곳에서 발표 해볼 수 있을까?
    - 커뮤니티 활동의 중요성을 다시금 느꼈다.
        - Let’Swift
        - Let us go
        - async Swift
        - swift 코딩클럽
    - 발표를 준비하는 루틴
        - 주제수집 및 수요 확인
        - 주제 선정
        - 주제 연구
        - 발표 대본 작성
            - 초고
            - 탈고

### 이달의 TIL 리스트

- inout 키워드에 대하여
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Swift/swift_keywordInout.md)
- defer 키워드에 대하여
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Swift/swift_keywordDefer.md)
- CocoaPods에서 SPM으로 마이그레이션 하는 방법
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Library/About_SPM.md)
- Git - 브랜치 삭제하기
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/Git/Git_branch_Delete.md)
- Git - username 변경하기
    - [TIL 링크]
- 여러가지 버전관리정책
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/ComputerScience/VersionLint.md)
- 앱스토어에 올라간 버전정보 수정하기
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-AppStore/AppStore_ChangeVersionInfo.md)
- PreviewProvider에서 여러가지 기기를 동시에 보는 방법
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Framework-SwiftUI_UIKit/PreviewProvier.md)
- CLLocation사용하기 - 위치 정보를 가져오는 방법
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Development/CLLocation_a_howToUse.md)
- CLLocation사용하기 - 비콘 정보를 가져오는 방법
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Development/CLLocation_beacon.md)
- WebView - 네비게이션컨트롤러 목록으로 웹뷰 관리하는 방법
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Networking/WebView_catchNavigation.md)
- 깃허브 Git Action 기초 사용방법 익히기
    - [[TIL 링크 : 초기 구현하기]](https://github.com/isGeekCode/TIL/blob/main/CI_CD/GithubAction_A_tutorial00.md)
    - [[TIL 링크 : on 섹션 수정하기]](https://github.com/isGeekCode/TIL/blob/main/CI_CD/GithubAction_A_tutorial00.md)
    - [[TIL 링크 : 실행할 스크립트 짜보기]](https://github.com/isGeekCode/TIL/blob/main/CI_CD/GithubAction_A_tutorial00.md)
- 화면전환 - UITabBarController 이해하기
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-ScreenTranport/tabbarController.md)
- 화면전환 - UINavigationController 이해하기
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-ScreenTranport/navigationController.md)
- UITabBar 알아보기
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Framework-UIKit/NSObject_UIResponder_UIView_UITabBar.md)
- 화면전환 - Segue를 이용한 화면이동
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-ScreenTranport/segue.md)
- Cocoa Design Pattern - Observer 옵저버 패턴
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Architecture/Architecture_101_De_CocoaDesignPattern_Observer.md)
- 샘플앱 생성 : 투두리스트앱
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/Sample-App-List/sample_000todoList.md)
- UIKit을 선언형으로 코딩하는 방법
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Extensions/UIKitLikeSwiftUI.md)
- 샘플앱 생성 : 그림판앱
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/Sample-App-List/sample_001pictureApp.md)
- 이미지처리 - iOS에서 화면캡처하기
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-RelatedImage/imageSave.md)
- info.plist관련 에러
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/About-Error/xcodeError_BuildInputFile.md)


<br><br>

## 다음달 목표

- 원티드 SwiftUI 관련 강좌 4회
- UIKit 톺아보기
    - 아직 UIKit에서 모르는게 많다.
    - 동작부터 구성 요소까지 개발자 문서를 쭉 따라가보기
