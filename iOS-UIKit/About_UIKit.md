# Apple Document - About App Development with UIKit

## 참고링크
- [원문: About App Development with UIKit](https://developer.apple.com/documentation/uikit/about_app_development_with_uikit#2928569)
- [TIL: UIKit을 상속하는 것들](https://github.com/isGeekCode/TIL/blob/main/iOS-Hierachy/IOS_Hierachy_UIKit.md)

UIKit은 iOS, 아이패드OS 또는 TVOS 앱의 핵심 인프라를 구성하는 데 사용할 수 있는 구성 요소를 포함하여 앱을 구축하는 데 사용할 수 있는 다양한 기능을 제공한다.  

- UI를 구현하기 위한 창과 뷰 아키텍처
- 앱에 멀티 터치 및 기타 유형의 입력을 전달하기 위한 이벤트 처리 인프라
- 사용자, 시스템 및 앱 간의 상호 작용을 관리하기 위한 메인 실행 루프   

UIKit은 또한 `애니메이션`, `문서`, `드로잉 및 인쇄`, `텍스트 관리 및 디스플레이`, `검색`, `앱 확장`, `리소스 관리` 및 `현재 장치에 대한 정보 가져오기`를 지원한다.  

또한 접근성 지원을 사용자 지정하고 다른 언어, 국가 또는 문화 지역에 대한 앱 인터페이스를 현지화할 수 있다.  

UIKit은 SwiftUI와도 원활한 작동이 가능해서 두 프레임워크간 인터페이스 요소를 혼합할 수 있다.

> 예를 들어, UIKit 뷰와 뷰 컨트롤러를 SwiftUI 뷰 안에 배치할 수 있으며 그 반대도 가능하다.
- [TIL: UIKit으로 구현된 화면에 SwiftUI View를 추가하기](https://github.com/isGeekCode/TIL/blob/main/iOS-SwiftUI_UIKit/PreviewProvider_UIHostingController.md)
 

## 특히 기억해야할것
UIKit을 설명하는 공식문서에 아래와 같이 나와있다.  
```
Important

Use UIKit classes only from your app’s main thread or main dispatch queue,
unless otherwise indicated in the documentation for those classes.
This restriction particularly applies to classes that derive from UIResponder or
that involve manipulating your app’s user interface in any way.
```

이 말은 UIKit 클래스들은 해당 클래스들의 문서에 명시되어있지 않은 이상, UIKit의 객체들을

오직 앱의 Main Thread나 Main Dispatch queue를 사용하라는 말이다. 

특히 UIResponder에서 파생되거나 앱의 사용자 인터페이스 조작과 관련된 클래스는 엄격히 `Main Thread`에서 사용해야한다. 



## UIKit App의 코드구조

UIKit은 시스템과 상호 작용하고, 앱의 메인 event Loop를 실행하고, 콘텐츠를 화면에 표시하는 등, 앱의 많은 핵심 개체를 제공한다. 

이런 개체들을 대부분 그대로(as-is) 사용하거나 아주 약간만 수정해서 사용하면 된다. 

그래서 앱을 구현하는 데 있어, 어떤 개체를 수정하고 언제 수정할지 아는 것이 중요하다.  

<br>  

UIKit 앱의 구조는 객체가 목적에 따라 분할되는 MVC(Model-View-Controller) 설계 패턴에 기반을 두고 있다.

- Model 객체는 앱의 데이터와 비즈니스 로직을 담당한다.
- View 객체는 데이터의 시각화를 담당한다.
- Controller 객체는 모델과 뷰 객체간 다리 역할을 하며 서로에게 데이터를 전달시킨다.  
  
  
<br>

아래 그림은 UIKit 앱의 일반적인 구조를 보여준다.  

- Model
먼저 앱의 데이터 구조를 나타내는 Model 개체가 있다.  

- View
또 View 부분을 보자. UIKit은 필요에 따라 데이터에 대한 커스텀 View를 구현할 수 있지만 대부분의 View 개체를 제공하고 있다.  

- Controller
ViewController와 Application Delegate는 Data 개체와 UIKit의 View 간의 데이터 교환을 컨트롤한다.  
  
<img width="600" alt="ff7aa08f-4857-44ce-88d5-7dacbef84509" src="https://github.com/isGeekCode/TIL/assets/76529148/81fe0c63-c11f-4199-a59b-427bbc024136">

<br>  

UIKit과 Foundation 프레임워크는 앱의 모델 개체를 정의하는 데 필요한 기본 타입들을 제공한다.  

UIKit은 디스크 기반 파일에 속하는 데이터 구조를 정리하기 위한 UIDocument 개체를 제공한다.

Foundation 프레임워크는 문자열, 숫자, 배열 및 기타 데이터 유형을 나타내는 기본 개체를 제공한다.

Swift Standard Library는 Foundation 프레임워크에서 사용할 수 있는 많은 동일한 유형을 제공한다.


---

UIKit은 컨트롤러 및 뷰 레이어에 있는 대부분의 개체를 제공한다.  

특히 UIKit은 일반적으로 콘텐츠를 화면에 표시하는 UIView 클래스를 정의한다.

Metal 및 기타 시스템 프레임워크를 사용해 콘텐츠를 화면에 직접 렌더링 할 수도 있다. 

UIApplication 개체는 앱의 메인 이벤트 루프를 실행시키고 앱의 전반적인 생명주기를 관리한다.  



## History
- 230804 : 초안작성
- 230807 : 하단부 번역
