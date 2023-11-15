# 23년 8월 회고 / 9월 목표


## 지난 목표

- 원티드 SwiftUI 관련 강좌 4회
- UIKit 톺아보기
    - 아직 UIKit에서 모르는게 많다.
    - 동작부터 구성 요소까지 개발자 문서를 쭉 따라가보기

## 지난 목표에 따른 피드백

- 원티드 SwiftUI 관련 강좌 4회
    → 원티드 X 야곰 의 SwiftUI 공식문서를 통해 실습해봤다.
    - 느낀 점
        - 처음으로 공식문서를 진지하게 찾아봤다. 이렇게 공부해야하는구나? 공부하는 방법을 새롭게 안 느낌이다. 생각보다 샅샅히 공부하는 것은 어려웠고, 꽤나 지루한 일일 수 있겠다. 적절한 동기가 동반 되어야할 것 같다.
- UIKit 톺아보기
    - 아직 UIKit에서 모르는게 많다.
    - 동작부터 구성 요소까지 개발자 문서를 쭉 따라가보기
        → 위 원티드 강좌를 통해 늦게 세우게 된 목표이다. SwiftUI를 해보면서 오히려 UIKit 에 대한 공식문서가 관심이 생겼다.
        

## 업무 성과

- 앱내 바코드 스캐너 기능 개발
    - 기존에 사용하던 직접삽입 바코드스캐너를 수정하여 MyNB앱에 세팅하였다.
    - 이 바코드 스캐너를 통해 해당 지점의 상품 바코드를 읽어 재고량을 리턴시킨다.
    - 바코드 스캐너 샘플을 하나 더 만들어서 다른 프로젝트에서 예제로 사용할 수 있는 템플릿 생성

- dispatch workItem 사용 튜토리얼 문서 작성
    - 상황에 따라 사용할 수 있는 GCD자료를 생성하였다.

- 단말기 대여 요청 템플릿 작성
    - 팀 노션에 대여 요청시 여러가지 체크리스트를 생성해서 업로드하였다.
    - 보통은 한번 대여하는데 여러번 질문응답을 주고 받았어야했는데 시간을 절약할 수 있게 되었다.

- 하이브리드 프로젝트에서 웹스키마, 쿼리를 사용하여 ViewController를 웹에서 관리하도록 처리 + 업그레이드
    - 기존에는 웹에서 일련의 동작을 세팅했지만 여러 메서드를 세팅하면서 이전 동작이 안될때가 있었다.
    - 그래서 DispatchGroup을 이용한 직렬 처리 도입을 통해, 스키마, 쿼리를 통해 작업한 내용을 앱내에서 DispatchGroup을 이용해 직렬 처리가  가능해짐.
    - 해당 작업으로 특별한 케이스에 대한 iOS 앱 배포 심사를 생략할 수 있었고 2-3일의 시간을 세이브

<br><br>

## 이달의 공연
- 레베카 : 테이, 리사

<br><br>


## 이달의 TIL 리스트

- Foundation 프레임워크에는 뭐가 있나
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Hierachy/IOS_Hierachy_Foundation.md)
- UIKit 프레임워크에는 뭐가 있나
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Hierachy/IOS_Hierachy_UIKit.md)
- 알고리즘이란
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/Algorithm/About_Algorithm.md)
- 선택정렬
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/Algorithm/algorithm00_selectionSort.md)
- 버블정렬 (작성중)
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/Algorithm/algorithm01_bubbleSort.md)
- UIKit으로 구현된 화면에 SwiftUI View를 추가하기 : UIHostingController
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Framework-SwiftUI_UIKit/PreviewProvider_UIHostingController.md)
- UIKit에서 SwiftUI의 Preview 사용하기
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Framework-SwiftUI_UIKit/PreviewProvier.md)
- UIKit에서 SwiftUI의 Preview관련 함수 만들어 사용하기
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Framework-SwiftUI_UIKit/PreviewProvier3.md)
- 직렬화(Serialization)
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/ComputerScience/Serialization.md)
- Foundation - JSONSerialization 직렬화하기
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Foundation/Foundation_JSONSerialization.md)

- iOS에서 JSON다루기(1): Encode JSONData
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Development/iOS_JSONSerialization_Encode.md)
- iOSiOS에서 JSON다루기(2): Decode JSONData
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Development/iOS_JSONSerialization_Decode.md)
- Network Programming - RESTful APIs 사용하기
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Networking/Network_RestfulAPI.md)
- MarkDown - 표 만들기 (Table)
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/Docs/MarkDown_Table.md)

- Apple Document Words - 단어장
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/About-IT/iOS_words.md)
- present - UIKit to SwiftUI
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-ScreenTranport/present_UIKitToSwiftUI.md)
- 정리 : iOS에서의 화면관리 및 전환
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-ScreenTranport/A_Various_switchingScene.md)
- Core Animation 프레임워크(작성중)
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Framework-CoreAnimation/About_CA_000_.md)
- SNS Login - Kakao
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Library/SNSLogin_kakao.md)
- SNS Login - Naver
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Library/SNSLogin_naver.md)
- Data Structure - 다양한 데이터 구조, iOS에서 사용하는 데이터 구조
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/ComputerScience/DataStructure.md)
- 프로그래밍 패러다임 - Functional Programming(함수형 프로그래밍)
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/ComputerScience/programming_00_Functional_.md)
- Functional Programming - 모나드 이해하기
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/ComputerScience/programming_00_Functional_Monade.md)
- Terminal 기초 사용법
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/ComputerScience/Terminal.md)
- 디자인패턴이란
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Architecture/Architecture_100_De_Intro_.md)
- 아키텍쳐패턴이란, 디자인패턴과 아키텍쳐의 차이
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Architecture/Architecture_200_Arc_Intro.md)
- Cocoa Design Pattern - Delegate 델리게이트 패턴
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Architecture/Architecture_101_De_CocoaDesignPattern_Delegate.md)
- Clean Architecture(클린 아키텍쳐)
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Architecture/Architecture_401_CleanArchitecture.md)
- MVC -> MVP -> MVVM : Caculator
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Architecture/Architecture_301_MVCToMVPToMVVM_Calculator.md)
- MVC -> MVP -> MVVM : ColorSelectApp
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Architecture/Architecture_301_MVCToMVPToMVVM_ColorSwitchApp.md)
- VC -> MVC : Custom UICollectionView
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Architecture/Architecture_301_MVC_CollectionView.md)
- String Protocol - String to Data
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Foundation/StringProtocol_stringToData.md)
- AVFoundation - AVPlayer 사용하기
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Foundation/AboutAVPlayer.md)
- AVFoundation - TTS : Text-To-Speech
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Foundation/AVFoundation_AVSpeechSynthesizer.md)
- Swift - Codable 다루기
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Swift/Codable.md)
- Attribute - @frozen
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Swift/Attribute_frozen.md)
- [Apple Document] - About the app launch sequence : 앱의 실행되는 순서에 관하여
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Framework-UIKit/About_UIKit_005AppLaunchSequnce.md)
- UIKit기반 앱의 간단한 화면 인터페이스 구조
    - [[TIL 링크]](https://github.com/isGeekCode/TIL/blob/main/iOS-Framework-UIKit/About_UIKit_050WindowsAnsScreens_Screens_SimpleUIKitInterface.md)


## 9월 목표

- UIKit 톺아보기
    - 동작부터 구성 요소까지 개발자 문서를 쭉 따라가보기
