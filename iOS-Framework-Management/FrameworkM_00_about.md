# Framework란 무엇인가

- 참고 : [Apple Document Archive - What are Frameworks?](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFrameworks/Concepts/WhatAreFrameworks.html)


<br><br>

## 프레임워크의 정의와 구성

프레임워크란, dynamic shared library(동적 공유 라이브러리), nib 파일, 이미지 파일, localized String(지역화된 문자열), 헤더파일, 참조 문서등과 같은 shared resources(공유자원)을 하나의 패키지로 묶은 계층적 디렉토리이다.  

여러 애플리케이션이 이러한 자원을 동시에 사용할 수 있다.  

<br><br>

## 번들과의 관계
프레임워크는 번들의 형태로 존재하며, 이는 파일과 자원이 패키징되는 방식을 의미한다.  
프레임워크는. Finder에서 폴더처럼 보이기 떄문에 개발자가 내용을 쉽게 탐색하고 필요한 자원을 찾을 수 있다.  

<br><br>

## 프레임워크와 라이브러리의 비교


프레임워크와 라이브러리 모두 개발자가 소프트웨어를 개발할 때, 재사용 가능한 코드의 집합을. 제공한다.


아주 가볍게 정리하면, 

프레임워크를 사용할 때에는 프레임워크의 규칙을 따라야한다.  


어디에 어떻게 코드를 써야할지 규칙이 있기 때문이다.  

어떤 기능을 구현할 때, 라이브러리를 사용하는 거라면 개발자는 라이브러리 없이도 구현할 수 있다.  

또한 라이브러리는 해당 자리를 다른 라이브러리로 대체할 수도 있다.  그럼에도 프로젝트가 망가지지 않는다.  


이에 대한 예시를 들어보면

Framework로는 UIKit,  Library로는 유명한 통신관련 라이브러리인 Alamofire를 들 수 있다.  

UIKit을 사용해보면 UIViewController에는 ViewDidLoad()라는 메서드가 있다.  


```swift
import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // 여기서 UILabel을 생성하고 화면에 추가하는 등의 작업을 할 수 있다.
        setLabel()
    }
    
    func setLabel() {
        let label = UILabel()
        label.text = "Hello world"
        label.backgroundColor = .systemYellow
        view.addSubview(label)
        // 별도의 제약조건 코드는 생략
    }
}
```

이 메서드는 프레임워크가 앱의 생명주기 중 적절한 시점에 호출하는 메서드이다.  
이처럼 프레임워크는 앱의 전반적인 흐름을 관리하며, 개발자들은 앞서 등장한 ViewDidLoad()와 같은 '훅'을 사용해 필요한 코드를 사용한다.  

<br><br>

또 라이브러리를 살펴보기위해 Almofire를 살펴보자.  

```swift
import Alamofire

Alamofire.request("https://api.example.com/getData").responseJSON { response in
    switch response.result {
    case .success(let value):
        print("Response JSON: \(value)")
    case .failure(let error):
        print("Error: \(error)")
    }
}
```

<br>

이 코드에서는 Alamofire 라이브러리의 request 함수를 사용하여 네트워크 요청을 하고 있다.  

개발자는 필요할 때 라이브러리의 함수를 호출하여 특정 작업(여기서는 HTTP 요청)을 수행한다. 

라이브러리는 단순히 특정 기능을 제공하는 도구이며, 애플리케이션의 전반적인 흐름을 제어하지 않는다.
   
또한 Alamofire가 없어도 네이티브 기능으로 충분히 구현이 가능하고, Alamofire와  비슷한 기능을 하는 라이브러리와 대체할 수도 있다.  



   
   

