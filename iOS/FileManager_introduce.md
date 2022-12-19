# FileManager - 사용하기

참고: [https://leeari95.tistory.com/32](https://leeari95.tistory.com/32)

```swift
let fileManager = FileManager.default
```

default는 FileManager의 싱글톤 인스턴스를 만들어준다. 

```swift
let documentsPath = fileManager.urls(for: .documentDirectory, in: .userDomainMask)[0]
```

urls 메서드는 요청된 도메인에서 지정된 공통 디렉토리에 대한 URL배열을 리턴해준다. 

첫번째 파라미터인 .documentDirectory는 검색경로 디렉토리다. 

- for: 폴더를 정해주는 요소, Download혹은 document 등등

두번째 파라미터는 Domain을 나타내는 파라미터다.

- in: 제한을 걸어주는 요소. 그이상은 못가게하는 요소이다

 

이걸 이용해서 Documents 디렉토리의 URL(Path)를 알게됐다.

이제 이걸 이용하면 파일을 추가할 수 있고 폴더를 추가할 수도  있다.

그러려면 파일의 이름 혹은 폴더의 이름을 정해줘야한다. 

```swift
let documentsPath = fileManager.urls(for: .documentDirectory, in: .userDomainMask)[0]

let directoryPath = documentsPath.appendingPathComponent("test-name")
```

여기에 

경로 설정하기

```swift
let fileManager = FileManager.default
let documentsPath = fileManager.urls(for: .documentDirectory, in: .userDomainMask)[0]
let directoryPath = documentsPath.appendingPathComponent("test-name")
```

폴더추가하기

```swift
do {
    // 아까 만든 디렉토리 경로에 디렉토리 생성 (폴더가 만들어진다.)
    try fileManager.createDirectory(at: directoryPath, withIntermediateDirectories: false, attributes: nil)
} catch let e {
    print(e.localizedDescription)
}
```

디렉토리 폴더에 파일을 추가하는 방법

내용집어넣기

```swift

let textPath: URL = directoryPath.appendingPathComponent("hi.txt")

// 아까 만든 'hi.txt' 경로에 텍스트 쓰기
if let data: Data = "안녕하세요.".data(using: String.Encoding.utf8) { // String to Data
    do {
        try data.write(to: textPath) // 위 data를 "hi.txt"에 쓰기
    } catch let e {
        print(e.localizedDescription)
    }
}
```
