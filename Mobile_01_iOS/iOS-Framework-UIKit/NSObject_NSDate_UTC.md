# NSDate - Timezone: UTC, GMT, KST

NSDate 또는 Date 객체는 타임존 정보를 포함하지 않고 모두 UTC기준입니다. 따라서 해당 지역의 시각으로 표현하기 위해서는 `DateFormatter`를 사용해야 합니다.

```swift
extension Date {
    
    func toString( dateFormat format: String ) -> String {
        let dateFormatter = DateFormatter()
        dateFormatter.dateFormat = format
        dateFormatter.timeZone = TimeZone.autoupdatingCurrent
        dateFormatter.locale = Locale.current
        return dateFormatter.string(from: self)
    }
    
    func toStringKST( dateFormat format: String ) -> String {
        return self.toString(dateFormat: format)
    }
    
    func toStringUTC( dateFormat format: String ) -> String {
        let dateFormatter = DateFormatter()
        dateFormatter.dateFormat = format
        dateFormatter.timeZone = TimeZone(abbreviation: "UTC") 
        return dateFormatter.string(from: self)
    }
}
```

lldb

```swift
(lldb) po dateFormatter.locale
▿ Optional<Locale>
  ▿ some : en_KR (current)
    - identifier : "en_KR"
    - kind : "current"
```

## UTC / GMT / KST

### UTC

UTC(Universal Time Coordinated) : 세계협정시

세계협정시(UTC)는 세슘원자시계을 사용하는데

세슘원자시계는 세슘원자릐 주기적인 원자진동을 이용하는 것으로 진동수가

매초 9, 192, 631, 770회로, 그 오차는 3000년에 1초 정도로 매우 정확하다.

### GMT

GMT(Greenwich Mean Time) : 그리니치 표준시(세계 표준시)

런던교외의 그리니치 천문대의 자오선상에서의 평균 태양시를

기준으로 하여 전세계의 지방표준시를 나타냄

GMT와UTC는 거의 같다고 볼 수 있다.

요즘엔 UTC를 쓰고 GMT는 점차 사라져가고 있다.

UTC=GMT 둘다 경도0°를 기준으로 시각을 나타낸다.

### KST

KST(KST Korean Standard Time) :한국 표준 시간

**KST(한국표준시)는 UTC 에서 9 시간을 더한것과 같다**

**KST = UTC + 9 hours  →**  UTC, GMT+9:00

(동경135°도 기준 15°마다 1시간씩 차이)

UTC가 00시면 KST는 09시

UTC가 12시면 KST는 21시

UTC가 1월 1일 18시면 KST는 1월 2일 03시가 됩니다.

원래는 동경 127.5°를 기준으로 UTC+8:30 해야하나

대부분의 나라가 1시간씩 단위로 정하고

북한도 UTC+9:00 쓰기때문에

나중에 통일을 고려해 한국도 UTC+9:00 쓰게 되었다.

일본 표준시(JST)도 한국과 동일하게 UTC+9:00를 사용한다.

### 그 외 기준시간

세계 표준시 UTC는

프랑스권 사람들의 TUC(Temps Universel Coordonne) 와 영어권 사람들의 CUT(Coordinated Universal Time)가 서로 약어 분쟁을 하여 UTC로 통일되었다.

그리니치 천문대가 표준시의 기준임으로 GMT(Greenwich Mean Time) 는 UTC와 같다.

**■ 현재 우리나라의 시간을 기준으로 다른 타임존의 시간을 알고 싶을 경우...**

UTC, GMT(세계 표준시 ) : 한국시간에 9시간을 빼어 계산한다.

CEST(중부 유럽 서머타임)  : UTC+2 hours , 한국시간에 7시간을 빼어 계산한다.

BST(영국 서머타임)     : UTC+1 hour , 한국시간에 8시간을 빼어 계산한다.

EDT(미국동부 서머타임, 예:뉴욕)   : UTC-4 hours , 한국시간에 13시간을 빼어 계산한다.

CDT(미국중부 서머타임, 예:시카고)   : UTC-5 hours , 한국시간에 14시간을 빼어 계산한다.

CST(중국표준시, 예:타이페이)  : UTC+8 hours , 한국시간에 1시간을 빼어 계산한다.

**■ 다른 타임존의 시간을 기준으로  우리나라 시간을 알고 싶을 경우...**

UTC, GMT(세계 표준시 ) : 해당시간에 9시간을 더하여 계산한다.

CEST(중부 유럽 서머타임)  : UTC+2 hours , 해당시간에 7시간을 더하여 한국시간을 계산해낸다.

BST(영국 서머타임)     : UTC+1 hour , 해당시간에 8시간을 더하여 한국시간을 계산해낸다.

EDT(미국동부 서머타임, 예:뉴욕)   : UTC-4 hours , 해당시간에 13시간을 더하여 한국시간을 계산해낸다.

CDT(미국중부 서머타임, 예:시카고)   : UTC-5 hours , 해당시간에 14시간을 더하여 한국시간을 계산해낸다.

CST(중국표준시, 예:타이페이)  : UTC+8 hours , 해당시간에 1시간을 더하여 한국시간을 계산해낸다.
