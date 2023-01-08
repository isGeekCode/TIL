# Layout - CGRectMake는 뭘까

stackOverflow를 이용하여 tableview를 만들어보던중 생소한 함수를 발견했다.
```
tableView.frame = CGRectMake(0, 50, 320, 200)
```
그런데 해당 함수를 써보니 UIkit에 없다면서 에러가 발생한다.
찾아보니 CGSizeMake, CGVectorMake 함수도 존재한다. 

아래코드와 동일한 의미로 사용할 수 있다.
```swift
CGRect.init(x: 150, y: 150 , width: 60, height: 60)
CGRect(x: 150, y: 150 , width: 60, height: 60)

```

개발문서를 보면 용도는 같은 것 같은데 한번 뜯어봐야겠다.


















