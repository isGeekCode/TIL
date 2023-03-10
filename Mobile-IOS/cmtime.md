# CMTime

[https://developer.apple.com/documentation/coremedia/cmtime](https://developer.apple.com/documentation/coremedia/cmtime)

CM(Core Media)는 시간을 표현하는 구조체이다.  시간값은 분자, 시간척도는 분모로 사용한다. 

이 구조를 사용해 미디어 타임라인의 특정 숫자시간을 나타낼 수 있다.

간단히 말해 시간 second가 분자로, timeScale이 분모로 하여 CMTime객체가 만들어진다. 

AVFoundation를 통해 만들 수 있고 주로 미디어의 특정위치를 시간으로 표현할 때 사용한다. 

만약 CMTime(seconds: 2, preferredTimescale: 2)이라면 CMTime은 1초가 된다.

만약 CMTime(seconds: 2, preferredTimescale: 1)이라면 CMTime은 2초가 된다.

## CMTime 생성하기

`[init(value: CMTimeValue, timescale: CMTimeScale)](https://developer.apple.com/documentation/coremedia/cmtime/1489173-init)`

값과 시간 척도로 시간을 생성합니다.

`[init(value: CMTimeValue, timescale: CMTimeScale, flags: CMTimeFlags, epoch: CMTimeEpoch)](https://developer.apple.com/documentation/coremedia/cmtime/1489260-init)`

값, 시간 척도, 플래그 및 에포크로 시간을 생성합니다.

`[init(seconds: Double, preferredTimescale: CMTimeScale)](https://developer.apple.com/documentation/coremedia/cmtime/1489786-init)`

기본 시간 척도에서 초 수를 나타내는 시간을 만듭니다.

`[init()](https://developer.apple.com/documentation/coremedia/cmtime/1489141-init)`

유효하지 않은 값으로 시간을 생성합니다.

## CMTime 살피기

`seconds` : Double

시간을 초단위로 표현한 형태

`hasBeenRounded`: Bool

시스템이 시간을 반올림 했는지 여부체크하는 값

`isNumeric`: Bool

시간이 숫자이지 여부를 체크하는 값

## CMTime 계산하기

`[tatic func + (CMTime, CMTime) -> CMTime](https://developer.apple.com/documentation/coremedia/cmtime/2983480)`

두 시간의 합을 나타내는 새 시간을 반환합니다.

`[static func - (CMTime, CMTime) -> CMTime](https://developer.apple.com/documentation/coremedia/cmtime/2983481)`

두 시간 간의 차이를 나타내는 새 시간을 반환합니다.

## CMTime 비교

`[static func == (CMTime, CMTime) -> Bool](https://developer.apple.com/documentation/coremedia/cmtime/2983484)`

두 시간이 같은지 여부를 나타내는 부울 값을 반환합니다.

`[static func != (CMTime, CMTime) -> Bool](https://developer.apple.com/documentation/coremedia/cmtime/2983479)`

두 시간이 같지 않은지 여부를 나타내는 부울 값을 반환합니다.

`[static func < (CMTime, CMTime) -> Bool](https://developer.apple.com/documentation/coremedia/cmtime/2983482)`

시간이 다른 시간보다 빠른지 여부를 나타내는 부울 값을 반환합니다.

`[static func <= (CMTime, CMTime) -> Bool](https://developer.apple.com/documentation/coremedia/cmtime/2983483)`

시간이 다른 시간보다 빠르거나 같은지 여부를 나타내는 부울 값을 반환합니다.

`[static func > (CMTime, CMTime) -> Bool](https://developer.apple.com/documentation/coremedia/cmtime/2983485)`

시간이 다른 시간보다 늦은지 여부를 나타내는 부울 값을 반환합니다.

`[static func >= (CMTime, CMTime) -> Bool](https://developer.apple.com/documentation/coremedia/cmtime/2983486)`

시간이 다른 시간과 같거나 이후인지 나타내는 부울 값을 반환합니다.

## 상수

`[static let zero: CMTime](https://developer.apple.com/documentation/coremedia/cmtime/1400875-zero)`

시간 0을 나타내는 값입니다.

`[static let invalid: CMTime](https://developer.apple.com/documentation/coremedia/cmtime/1400807-invalid)`

잘못된 시간을 나타내는 값입니다.

`[static let indefinite: CMTime](https://developer.apple.com/documentation/coremedia/cmtime/1400777-indefinite)`

무기한 시간을 나타내는 값입니다.

`[static let negativeInfinity: CMTime](https://developer.apple.com/documentation/coremedia/cmtime/1400869-negativeinfinity)`

음의 무한대를 나타내는 값입니다.

`[static let positiveInfinity: CMTime](https://developer.apple.com/documentation/coremedia/cmtime/1400789-positiveinfinity)`

양의 무한대를 나타내는 값입니다.

관련 내용 체크

[https://velog.io/@wannabe_eung/iOS-AVFoundation을-이용하여-영상-진행바UISlider-구현하기](https://velog.io/@wannabe_eung/iOS-AVFoundation%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%98%EC%97%AC-%EC%98%81%EC%83%81-%EC%A7%84%ED%96%89%EB%B0%94UISlider-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0)
