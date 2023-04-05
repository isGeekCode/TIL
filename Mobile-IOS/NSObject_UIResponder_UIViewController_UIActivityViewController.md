# NSObject_UIResponder_UIViewController_UIActivityViewController : 공유하기 기능

## UIActivityViewController
앱에서 정말 많이 사용하는 기능 중 하나가 공유하기 기능이다. 

![IMG_0656](https://user-images.githubusercontent.com/76529148/229722540-fd57f876-14c7-4ef5-992e-2502eb5464b6.PNG)

아마 익숙할 것이다. 
UIActivityViewController는 이렇게 앱에서 공유 기능을 구현할 때 사용된다.

사용자가 공유할 수 있는 다양한 옵션(메일, 페이스북, 트위터 등)을 표시하고, 선택한 옵션을 통해 공유할 데이터(이미지, 텍스트, 링크 등)를 처리한다.

## 주의사항
- iPad에서는 popover 스타일로 띄워야 한다.
    - 애플심사시 iPad로 테스트를 하기때문에 리젝원인이 될 수 있다.
- iPhone이나 iPod touch에서는 modal 스타일로 띄워야 한다.

## activityItems

UIActivityViewController를 생성할때 파라미터로 activityItems이 들어간다. 
activityItems는 [Any] 타입이므로, 아무 타입의 아이템을 넣는 것이 가능하다.
전달하고 싶은 text, image 등등을 배열에 넣어주면 된다. 

## 간단한 사용법

기본적으론 아래 세단계에 걸쳐 생성이 가능하다.
- 공유할 내용(activityItems) 생성
- activityViewController 생성
- 생성한 activityViewController를 present

```swift
func goShare() {

    // 공유할 내용 세팅
    let text = "https://www.naver.com"
    let activityItems: [Any] = [text]

    // 공유할 객체 생성
    let activityViewController = UIActivityViewController(activityItems: activityItems, applicationActivities: nil)
    
    // 공유할 객체를 화면으로 present
    present(activityViewController, animated: true, completion: nil)
}
```

## excludedActivityTypes

- 필수아님
- 액티비티 뷰에서 기본적으로 제공하는 서비스 중 제외할 서비스를 지정하는 부분


### 사용법
```swift

    // 이닛하는 부분
    let activityVC = UIActivityViewController(activityItems: activityItems, applicationActivities: nil)
    // 제외하는 부분
    activityVC.excludedActivityTypes = [.postToTwitter, .postToWeibo, .postToVimeo, .postToFlickr, .postToFacebook, .postToTencentWeibo]

    // 생성한 activityVC객체 띄우기
    self.present(activityVC, animated: true, completion: nil)
```

## UIActivityType

제어가능한 타입들은 아래와 같다.
```
// 읽기 목록에 추가
static let addToReadingList: UIActivityType

// 에어드롭으로 공유하기
static let airDrop: UIActivityType

// 연락처에 지정
static let assignToContact: UIActivityType

// Paste Board에 복사
static let copyToPasteboard: UIActivityType

// 메일 보내기
static let mail: UIActivityType

// 메시지 보내기
static let message: UIActivityType

// iBooks에서 열기
static let openInIBooks: UIActivityType

// 페이스북에 공유하기
static let postToFacebook: UIActivityType

// Flickr에 공유하기
static let postToFlickr: UIActivityType

// Tencent Weibo에 공유하기
static let postToTencentWeibo: UIActivityType

// 트위터에 공유하기
static let postToTwitter: UIActivityType

// Vimeo에 공유하기
static let postToVimeo: UIActivityType

// SinaWeibo에 공유하기
static let postToWeibo: UIActivityType

// 프린트
static let print: UIActivityType

// 카메라 롤에 저장하기
static let saveToCameraRoll: UIActivityType

// PDF 생성(iOS 11 부터 사용가능)
static let markupAsPDF: UIActivityType

```

# completionWithItemsHandler

```swift
typealias CompletionWithItemsHandler = (UIActivity.ActivityType?, Bool, [Any]?, Error?) -> Void
```
activityViewController에는 completionWithItemsHandler라는 함수가 있다.
이 함수를 사용하면 공유를 실행한 다음의 동작을 구현할 수 있다.

아래 네가지의 completionHandler가 있다.
- activityType : 지정한 activity 일 때의 동작을 구현가능하다.
- completed : 성공 여부를 지정할 수 있다.
- returnedItems : activityType에 따라 달라지는 returnedItems을 제어하는데 사용
- activityError : 에러발생시 처리

### activityType

completionWithItemsHandler에서는 특정 activityType을 지정해서 동작을 구현할 수 있다.

### 예시1)
```swift
activityViewController.completionWithItemsHandler = { activityType, completed, returnedItems, error in
    if completed && activityType == .mail {
        if let emailItem = returnedItems?.first as? NSDictionary {
            if let recipients = emailItem["MFMailComposeRecipients"] as? [String] {
                print("Email recipients: \(recipients)")
            }
            if let subject = emailItem["MFMailComposeSubject"] as? String {
                print("Email subject: \(subject)")
            }
        }
    }
}

```


### 예시2)
```swift
activityViewController.completionWithItemsHandler = { activityType, completed, returnedItems, error in
    if completed && activityType == .airDrop {
        if let url = returnedItems?.first as? URL {
            // AirDrop으로 공유된 파일 URL 처리
            print("Shared file URL: \(url.absoluteString)")
        }
    }
}

```


### returnedItems

returnedItems은 위에 예시1, 예시2 처럼 activityType에 따라 다른 값을 가질 수 있다.
아래 내용 외에도 정말 다양한 값들을 가질 수 있다.

- UIActivityType.postToFacebook
    - com.facebook.sdk:image : Facebook에 업로드된 이미지 URL
    - com.facebook.sdk:place : Facebook 위치 정보
    - com.facebook.sdk:people_ids : Facebook 태그된 사용자 ID
    - com.facebook.sdk:place_name : Facebook 장소 이름
- UIActivityType.postToTwitter
    - public.text : Twitter 메시지 텍스트
    - public.url : Twitter 메시지 URL
    - com.twitter.android.posting.extra.USERS : Twitter 태그된 사용자 이름
    - com.twitter.android.posting.extra.HASHTAGS : Twitter 해시태그
- UIActivityType.mail
    - public.message : 이메일 본문 메시지
    - public.html : 이메일 HTML 본문 메시지
    - public.subject : 이메일 제목
    - public.recipients : 이메일 수신자 이메일 주소
- UIActivityType.copyToPasteboard
    - public.utf8-plain-text : 복사된 텍스트
    - public.url : 복사된 URL
    - public.jpeg : 복사된 이미지
    - public.png : 복사된 PNG 이미지
- UIActivityType.saveToCameraRoll
    - public.jpeg : 저장된 JPEG 이미지
    - public.png : 저장된 PNG 이미지
    - public.mpeg-4 : 저장된 동영상
- UIActivityType.message
    - public.text : 문자 메시지 텍스트
    - public.url : 문자 메시지 URL
    - public.file-url : 문자 메시지 파일 URL
    - public.png : 문자 메시지 이미지
- UIActivityType.postToWeibo
    - com.sina.weibo.content.text : Weibo 메시지 텍스트
    - com.sina.weibo.content.objectID : Weibo 메시지 ID
    - com.sina.weibo.content.title : Weibo 메시지 제목
    - com.sina.weibo.content.picture : Weibo 이미지 URL
- UIActivityType.addToReadingList
    - public.url : 추가된 URL
- UIActivityType.postToVimeo
    - com.vimeo.sdk.videoUrl : Vimeo 동영상 URL
- UIActivityType.postToFlickr
    - public.url : Flickr 이미지 URL
    - public.jpeg : Flickr 이미지
    - public.png : Flickr 이미지
- UIActivityType.openInIBooks
    - com.apple.iwork.document.pages : Pages 문서
    - com.apple.iwork.document.numbers : Numbers 문서
    - com.apple.iwork.document.keynote : Keynote 문서
- UIActivityType.openInAdobeReader
    - com.adobe.pdf : Adobe Reader PDF 문서


## 참고링크
- [공유 메뉴 : UIActivityViewController 띄우기](http://yoonbumtae.com/?p=5080) 
- [Activity View Controller](https://www.zehye.kr/ios/2020/03/12/12iOS_activity_view_controller) 
- [애플문서 : uiactivityviewcontroller / activitytype](https://developer.apple.com/documentation/uikit/uiactivity/activitytype)
- [애플문서 : uiactivityviewcontroller / completionwithitemshandler](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/completionwithitemshandler) 
