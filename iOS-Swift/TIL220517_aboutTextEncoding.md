# 텍스트인코딩에 관하여

우리가 URL 통신을 할때에는 String이 아닌 URL형태를 가지고 통신을 합니다.

URL은 String 형식을 URL형식으로 변환하는 과정을 통해 만들 수 있는데

이 과정속에는 아래의 검증과정이 포함되어있는 것을 볼 수 있어요

## addingPercentEncoding

이 함수는 지정된 Set에 없는 모든 문자를 백분율로 인코딩된 문자로 바꾸어 새로운 문자열을 반환해주는 함수에요.

이때 withAllowedCharacters의 파라미터로 들어가는 Set 요소들을 제외하고는 모두 아래처럼 퍼센트로 인코딩된 문자로 출력됩니다

예시 1

```swift
let urlStr = "www.naver.com/search?location=명동"
guard let encodedStr = urlStr.addingPercentEncoding(withAllowedCharacters: .urlQueryAllowed) else { return }

let url = URL(string: encodedStr)!
print(url.absoluteString)
// www.naver.com/search?location=%EB%AA%85%EB%8F%99
```

### withAllowedCharacters Xcode 기본 Sets

**_CharacterSet_**

각 Set 별로 알파벳, 숫자 외에 포함할 수 있는 특수문자의 목록입니다. 여기에 포함되지 않는 문자는 encoding이 되어서 변환됩니다.

- **urlUserAllowed → 15개**

```swift
! $ & \ ( ) * + , - . ; = _ ~
```

- **urlPasswordAllowed → 15개**
- `urlUserAllowed`와 같다.

```swift
! $ & \ ( ) * +  - . ; = _ ~
```

- **urlPathAllowed → 17개**
- `urlUserAllowed`에 비해 `;`가 없고 `/ : @` 가 더 있다.

```swift
! $ & \ ( ) * +  - . / : = @ _ ~
```

- **urlHostAllowed → 18개**
- `urlUserAllowed`에 비해 `: [ ]` 가 더 있다.

```swift
! $ & \ ( ) * +  - . : ; = [ ] _ ~
```

- **urlFragmentAllowed → 19개**
- `urlUserAllowed`에 비해 **`/ : ? @`** 가 더 있다.

```swift
! $ & \ ( ) * +  - . / : ; = ? @ _ ~
```

- **urlQueryAllowed → 19개**
- `urlFragmentAllowed`와 같다

```swift
! $ & \ ( ) * +  - . / : ; = ? @ _ ~
```

예시 1 에서 withAllowedCharacters 를 사용했지만 하단에서 %어쩌구가 발생한 이유느느 한글은 이 곳에 포함되어있지 않기 때문이에요.

한글은 마지막에 소개할게요.

예시 2

이 코드는 urlStr이 없다면 String을 생성하는 부분입니다. 바로 URL을 사용하지는 않고 값만 보관할 예정이라 URL형태로 인코딩하는 부분은 없어요.

- allowedCharacterSet을 따로 만들어 사용했어요

```swift
if self.urlStr != nil {
            let allowedCharacterSet = (CharacterSet(charactersIn: "{}|`\\^_").inverted)
            if let escapedString = self.urlStr.addingPercentEncoding(withAllowedCharacters: allowedCharacterSet) {
                //
            }
        }
```

예시3

바로 URL로 만들어 사용할 때는 URL로 변환 과정을 가집니다.

```swift
if let encoded = urlStr.addingPercentEncoding(withAllowedCharacters: .urlQueryAllowed), let myURL = URL(string: encoded) {
       print(myURL)
}
```

### 특수문자(한글등)에 Percent Encoding 을 하는 작업

URL을 호출할때에는 URL데이터형을 만들어 사용하는데, 이 과정에서 한글이 들어가거나, 스페이스 등이 들어가면 URL이 nil이 될 수 있어요.

그렇기 때문에 addingPercentEncoding을 사용해 허용되지않은 문자는 모두 일괄적으로 퍼센트인코딩하면 예시1 처럼 한글이 변환이 되지요.

### 방법1

Percent Encoding을 했을때 만약 되는지 안되는지 걱정된다면 확인해보는 가장 빠른 방법은

인코딩 된 링크를 웹에 붙여넣기 해봤을때 작동하면 되는거에요!!

### 방법2

아예 URL(string: imageURL)이 유효한지 테스트를 하고 유효하면 addingPercentEncoding를 안하는 방법

```swift
//한글 디렉토리테스트
    let extPhotoDir: String = "/UpLoad/Photo/202101/긱코드20,10.jpg"
    let hostUrl: String = "https://www.naver.com/"
    let imageURL:String = "\(hostUrl)\(extPhotoDir)"
    let imageDirStr: String = {
        if URL(string: imageURL) != nil {
            return imageURL

        } else {
            return imageURL.addingPercentEncoding(withAllowedCharacters: .urlQueryAllowed)!

        }
    }()

   let personImageUrl = URL(string: imageDirStr)

    do
    {
        let data = try Data(contentsOf: personImageUrl)
        self.myPagePersonImage.image = UIImage(data: data)
    }
    catch{
     print("사진이 없습니다")
    }
```

### 👍 방법3 → 요걸로 선택~!

`guard let personImageUrl = URL(string: imageDirStr) else { return}`
여기서 nil이 나는 지만 체크 해서 간소화

```swift
    let extPhotoDir: String = "/UpLoad/Photo/202101/긱코드20,10.jpg"
    let hostUrl: String = "https://www.naver.com"
    let imageURL:String = "\(hostUrl)\(extPhotoDir)"
// https://www.naver.com/UpLoad/Photo/202101/긱코드20,10.jpg
    guard let imageDirStr = imageURL.addingPercentEncoding(withAllowedCharacters: .urlQueryAllowed) else { return }
    print(imageDirStr)

    guard let personImageUrl = URL(string: imageDirStr) else { return}

    do
    {
        let data = try Data(contentsOf: personImageUrl)
        self.myPagePersonImage.image = UIImage(data: data)
    }
    catch{
     print("사진이 없습니다")
    }
```

## PercentEncoding / Decoding

흔히 URL 인코딩 / 디코딩이라고 부르는 것으로 문자의 16진수값 앞에 퍼센트를 붙여서 URI 규약(rfc3986)에서 문제없이 표현하는 목적으로 사용됩니다.

특수문자로 인정하는 범위가 Host, Path, Query 등에 따라서 달라지게 되며, 웹서버등 상황에 맞춰 사용하면 됩니다.(아래에서는 URLPathAllowedCharacterSet 를 사용했습니다.  Host 를 사용할 경우에는 '?' 까지도 인코딩되게 됩니다.)

Swift

```swift
funcurlEncode() ->String? {
return self.addingPercentEncoding(withAllowedCharacters:CharacterSet(charactersIn: "!*'();:@&=+$,/?%#[]{} ").inverted)
}

funcurlDecode() ->String? {
return self.removingPercentEncoding
}
```

Objective-C

```swift
- (NSString *)urlEncode {
/* Percent 인코딩 범위에 주의, URLHostAllowedCharacterSet 등 범위에 맞춰서 사용.  */
return [self stringByAddingPercentEncodingWithAllowedCharacters:[NSCharacterSetURLPathAllowedCharacterSet]];
}

- (NSString *)urlDecode {
return [self stringByRemovingPercentEncoding];
}
```
