# Notifications - IOS에서 사용하는 알림의 종류
iOS에서 사용하는 알림의 종류는 다음과 같다.
NotificationCenter를 제외하고는 우리가 아는 앱의 알림의 형태를 띈다.


## Push Notification (서버 -> 기기)
앱을 실행하지 않은 상태에서도 앱에서 발생하는 이벤트에 대한 알림을 받을 수 있도록 해주는 기술입니다. 알림 서버를 통해 사용자의 기기로 알림을 전송하며, 앱이 백그라운드에 있을 때도 알림을 받을 수 있다.

## Local Notification (기기내부 -> 기기)
앱 내에서 발생하는 이벤트에 대한 알림을 사용자에게 보내는 기술이다. 로컬 알림은 앱 내부에서 처리되기 때문에 인터넷 연결이 필요없다.

## 🍊 NotificationCenter (앱 내부 -> 다른 객체나 모듈)
앱 내에서 다른 객체나 모듈 간에 데이터를 전달하기 위한 기능이다. NotificationCenter를 사용하면 앱 내에서 다양한 이벤트를 감지하고, 이벤트에 따른 액션을 수행할 수 있다.

## Silent Push Notification  (서버 -> 기기)
Push Notification과 유사하지만, 앱을 실행하지 않은 상태에서도 앱에서 데이터를 백그라운드에서 처리할 수 있도록 해준다.

앱 서버에서 Apple Push Notification 서버(APNS)를 통해 iOS 기기로 전송한다. 기기에서는 Silent Push Notification을 받으면 앱이 실행되지 않은 상태에서도 백그라운드에서 실행될 수 있는 처리를 수행하고, 필요한 경우에만 UI 알림을 표시하거나 다른 작업을 수행한다.

## Rich Push Notification (서버 -> 기기)
Push Notification에 이미지, 비디오 등의 다양한 미디어 콘텐츠를 추가하여 보다 풍부한 알림을 제공할 수 있다.

Push Notification과 마찬가지로, 앱 서버에서 Apple Push Notification 서버(APNS)를 통해 iOS 기기로 전송된다. Push Notification과 달리, Rich Push Notification에는 이미지, 비디오, 오디오 등의 미디어 콘텐츠가 포함될 수 있으며, 이러한 콘텐츠는 APNS를 통해 전송한다.



## User Notification Framework
iOS 10부터 도입된 기술로, Local Notification과 Push Notification을 모두 지원한다. User Notification Framework를 사용하면, 알림의 디자인 및 동작 방식을 보다 세밀하게 제어할 수 있다.
