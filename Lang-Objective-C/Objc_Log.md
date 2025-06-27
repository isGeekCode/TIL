# ObjC - 로그찍기

Swift프로젝트만 평소에 보다가 Objective-c로 가끔 작업을 할때가 있다.
그런데 이따금 하는 작업에 로그를 찍는데 매번 까먹는 로그쓰는 방법...

스트레스를 받지않기 위해 남긴다.

```objc
<!--NSDictionary *infoDict = [[NSBundle mainBundle] infoDictionary];-->
<!--NSString *kakaoAppKey = [infoDict objectForKey:@"KAKAO_APP_KEY"];-->

<!--일반로그 찍기-->
NSLog(@"kakaoAppKey");
<!--변수로그 찍기-->
NSLog(@"kakaoAppKey : %@", kakaoAppKey);
```

## History
- 230421 : 초안작성
