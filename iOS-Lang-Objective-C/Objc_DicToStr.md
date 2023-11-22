# ObjC - NSDictionary to NSString

## NSDictionary -> NSString 

```swift
NSMutableDictionary *jsonDic = [[NSMutableDictionary alloc] init];
[jsonDic setValue:[NSNumber numberWithBool:TRUE] forKey:@"result"];
[jsonDic setValue:@"test message" forKey:@"message"];

NSString *jsonDicStr = [NSString stringWithFormat:@"%@", jsonDic];
NSLog(@"jsonDicStr: %@", jsonDicStr);

/**
jsonDicStr: {
    message = "test message";
    result = 1;
}
*/
```

## NSDictionary -> NSData -> NSString 

```swift

NSMutableDictionary *jsonDic = [[NSMutableDictionary alloc] init];
[jsonDic setValue:[NSNumber numberWithBool:TRUE] forKey:@"result"];
[jsonDic setValue:@"test message" forKey:@"message"];

// NSData로 변경
NSData* jsonData = [NSJSONSerialization dataWithJSONObject:jsonDic options:NSJSONWritingPrettyPrinted error:nil];
// NSString으로 변경
NSString* jsonDataStr = [[NSString alloc] initWithData:jsonData encoding:NSUTF8StringEncoding];
NSLog(@"jsonDataStr: %@", jsonDataStr);

/**
jsonDicStr: {
    "result" : true,
    "message" : "test message"
}
*/
```


## History
- 231122 : 초안 작성
