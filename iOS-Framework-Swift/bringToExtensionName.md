# 파일경로 String으로에서 확장자 추출하기

가끔 앱 내에서 API통신으로 이미지 등의 파일 경로를 받아서 처리해야하는 경우가 있다.
iOS에서는 일반 이미지나 gif, 영상 일때 각각 객체를 다른걸 사용해야하기때문에 구분을 해줘야한다.
그래서 아래처럼 확장자를 추출할 수 있다.

```swift
let fileTESTName = "example.txt"
guard let lastDotIndex = fileTESTName.lastIndex(of: ".") else {
    print("해당 경로에 확장자가 존재않지 않습니다")
    return
}
let extensionName = fileTESTName.suffix(from: lastDotIndex).dropFirst()
print("extensionName: \(extensionName))
```

### 설명
- lastIndex(of)를 사용하면 해당 String값 중 마지막 "."의 위치를 알 수 있다.
- suffix(from:)을 사용하면 해당 String값 중 `해당 위치부터`의 값을 가져올 수 있다. 
- dropFirst()를 이용해 첫글자(`"."`)를 떨어뜨리면 확장자만 가져올 수 있다.
