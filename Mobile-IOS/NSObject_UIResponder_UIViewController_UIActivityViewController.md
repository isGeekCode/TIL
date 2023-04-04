NSObject_UIResponder_UIViewController_UIActivityViewController : 공유하기

## UIActivityViewController
앱에서 정말 많이 사용하는 기능 중 하나가 공유하기 기능이다. 

![IMG_0656](https://user-images.githubusercontent.com/76529148/229722540-fd57f876-14c7-4ef5-992e-2502eb5464b6.PNG)

아마 익숙할 것이다. 
UIActivityViewController는 이렇게 앱에서 공유 기능을 구현할 때 사용된다.

사용자가 공유할 수 있는 다양한 옵션(메일, 페이스북, 트위터 등)을 표시하고, 선택한 옵션을 통해 공유할 데이터(이미지, 텍스트, 링크 등)를 처리한다.




## activityItems
activityItems에는 여러 아이템을 첨부할 수 있다.

타입이 [Any]이므로 말 그대로 아무 타입의 아이템을 넣는 것이 가능하다.
전달하고 싶은 text, image 등등을 배열에 넣어주면 된다. 



## excludedActivityTypes
액티비티 뷰에서 기본적으로 제공하는 서비스 중 제외할 서비스를 지정하는 부분이다.

아래와 같은 방법으로 사용한다.
```swift

    // 이닛하는 부분
    let activityVC = UIActivityViewController(activityItems: activityItems, applicationActivities: nil)
    // 제외하는 부분
    activityVC.excludedActivityTypes = [.postToTwitter, .postToWeibo, .postToVimeo, .postToFlickr, .postToFacebook, .postToTencentWeibo]

```

## excludedActivityTypes

iOS에서 제공하는 다양한 옵션은 아래와 같다.

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


## 주의사항
- iPad에서는 popover 스타일로 띄워야 한다.
- iPhone이나 iPod touch에서는 modal 스타일로 띄워야 한다.



```swift
    // 공유하기
    func goShare(_ urlQuery: String?) {
        guard let urlQuery = urlQuery else { return }
        let activityItems: [Any] = [urlQuery]

        let activityViewController = UIActivityViewController(activityItems: activityItems, applicationActivities: nil)
        activityViewController.completionWithItemsHandler = {(activity, success, items, error) in

            if success {
                if let sns = activity?.rawValue { }
            } else {
                print("share fail \(String(describing: activity?.rawValue))")
            }
        }
        present(activityViewController, animated: true, completion: nil)

    }
```

## 참고링크
- [공유 메뉴 : UIActivityViewController 띄우기](http://yoonbumtae.com/?p=5080) 
- [Activity View Controller](https://www.zehye.kr/ios/2020/03/12/12iOS_activity_view_controller) 

