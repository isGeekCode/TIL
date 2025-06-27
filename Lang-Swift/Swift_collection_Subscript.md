# Swift - Subscript(작성중)

subscript란 특정 타입뒤에 []를 붙여서 접근할 수 있도록 만든 것을 말한다.

가장 대표적인 예가 Array에서 해당 요소의 index를 입력하는 `sampleList[0]` 이나 Dictionary에서 특정 키값에 해당하는 value를 찾는 `sampleDic["key1"]` 같은 것들이 존재한다. 


딕셔너리 같은 경우, Xcode에서 Dictionary를 열어보면 아래와 같은 샘플코드가 들어있다.

```swift
    ///     let message = "Hello, Elle!"
    ///     var letterCounts: [Character: Int] = [:]
    ///     for letter in message {
    ///         letterCounts[letter, default: 0] += 1
    ///     }
    ///     // letterCounts == ["H": 1, "e": 2, "l": 4, "o": 1, ...]



    ///     var responseMessages = [200: "OK",
    ///                             403: "Access forbidden",
    ///                             404: "File not found",
    ///                             500: "Internal server error"]
    ///
    ///     let httpResponseCodes = [200, 403, 301]
    ///     for code in httpResponseCodes {
    ///         let message = responseMessages[code, default: "Unknown response"]
    ///         print("Response \(code): \(message)")
    ///     }
    ///     // Prints "Response 200: OK"
    ///     // Prints "Response 403: Access forbidden"
    ///     // Prints "Response 301: Unknown response"

```

default를 통해 해당 키값이 없다면 value에 해당 인자를 넣어줄 수 있다.
반면 해당 키값이 존재하며, default를 0으로 이후 += 1 이 붙게 되면 해당 키에 대한 밸류가 없다면 0, 있다면 for문을 순회하며 1씩 늘리게 된다.


그 밖에도 Subscript를 따로 구현할 수 있는데, 차후 추가 예정
