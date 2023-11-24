# 마크다운에서 Toggle(Expander control) 기능 사용하기

마크다운 자체에서는 토글을 지원하지 않는다.  그래서  html의 태그를 이용해서 토글기능을 구현해야한다.  

## details태그
이 기능을 제공하는 html 태그가 details이다.  

그리고 div markdown="1"을 꼭 넣어줘야 하는데,  
이것은 jekyll에서 html사이에 markdown을 인식 하기 위한 코드이다.
> 사실 그러면 jekyll을 사용안하면 필요없지???


```
<details>
<summary>토글 접기/펼치기</summary>
<div markdown="1">

안녕

</div>
</details>
```
  
### 적용 
<details>
<summary>토글 접기/펼치기</summary>
<div markdown="1">

안녕

</div>
</details>

<br><br><br>
  
그렇다면 코드블록도 가능한가??

```
<details>
<summary>토글 접기/펼치기</summary>
<div markdown="1">

```swift
import UIKit

class ViewController: UIViewController {

    override func viewDidLoad {
        super.viewDidLoad()
        
        print("Hello world!!")
    }
}
```

</div>
</details>
```

<details>
<summary>토글 접기/펼치기</summary>
<div markdown="1">

```swift
import UIKit

class ViewController: UIViewController {

    override func viewDidLoad {
        super.viewDidLoad()
        
        print("Hello world!!")
    }
}
```

</div>
</details>


<br><br><br>

## History
- 231124: 초안작성
