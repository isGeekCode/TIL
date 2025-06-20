# Android - Basic : 안드로이드의 기본 앱구조

안드로이드의 기본 앱 구조는 크게 4가지 요소로 구성된다.

## 액티비티(Activity)
안드로이드에서 앱의 화면을 담당하는 가장 기본적인 요소다. 하나의 액티비티는 하나의 화면을 담당하며, 다른 액티비티로 전환하여 화면을 변경할 수 있다. 
- iOS에서는 UIViewController가 화면을 담당하는 기본적인 요소다.

## 서비스(Service)
안드로이드에서 백그라운드에서 동작하는 기능을 담당한다. 
- iOS에서는 백그라운드에서 동작하는 기능을 담당하는 것으로는 주로 백그라운드 작업 처리를 위한 Operation Queue나 Dispatch Queue를 사용한다.

## 콘텐츠 제공자(Content Provider)
안드로이드에서 데이터를 관리하고 다른 앱에서 접근할 수 있도록 제공하는 요소다. 
- iOS에서는 데이터 관리를 위해 Core Data나 Realm 등의 데이터베이스를 사용하며, 데이터 공유를 위해서는 iOS에서 제공하는 공유 확장(extension)을 사용할 수 있다.

## 브로드캐스트 리시버(Broadcast Receiver)
안드로이드에서 다른 앱에서 발생하는 이벤트를 받아서 처리하는 요소다. 
- iOS에서는 Notification Center를 사용하여 앱 간 이벤트를 처리할 수 있다.

## + 프래그먼트
안드로이드에서는 프래그먼트(Fragment)를 사용하여 하나의 액티비티에서 여러 개의 UI 구성 요소를 관리할 수 있다. 
- iOS에서는 UIViewController와 컨테이너 뷰를 사용하여 비슷한 효과를 구현할 수 있다.

## 요약
안드로이드의 기본 앱 구조는 액티비티, 서비스, 콘텐츠 제공자, 브로드캐스트 리시버 등으로 구성되며, iOS에서는 UIViewController, Operation Queue, Dispatch Queue, Core Data, Notification Center 등의 기능을 사용하여 비슷한 효과를 구현할 수 있다.
