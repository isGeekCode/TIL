# ObjC - Control Flow : Switch문

## 기본적인 사용법
Objc의 switch문에서 가장 주의해야할 것은 

case 마다 마지막에 break;를 넣어줘야한다는 것이다.  
그렇지않으면 전부 마지막 case의 값을 가져오는 상황이 발생하곤한다.  

```swift
- (void) checkBtn:(NSInteger)btnTag {
    NSString *eventStr = @"";
    switch (btnTag) {
        case 2:
            eventStr = @"버튼2";
            break;

        case 3:
            eventStr = @"버튼3";
            break;

        case 4:
            eventStr = @"버튼4";
            break;

        default: // 버튼 1, 2는 필요없음
            break;
    }
    NSLog(@"버튼클릭::: %@", eventStr);
}
```


## History
- 231122 : 초안작성
