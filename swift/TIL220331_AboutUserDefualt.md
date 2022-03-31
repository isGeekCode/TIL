# userDefault

**[Swift/iOS] Key, Value 형태로 값 저장하기 (UserDefaults)**

안드로이드에서는 Key, Value형태로 간단히 데이터를 저장할때 **SharedPreferences**를 사용한다

iOS에서는 간단하게 데이터를 기기에 저장할 때 **UserDefault**를 사용한다.

그러면 앱의 어느 곳에서나 데이터를 쉽게 읽고 저장할 수 있게된다.

뿐만아니라 앱을 종료해도 이 데이터는 지워지지않고 호출을 할 수 있다.

[Apple Developer Documentation](https://developer.apple.com/documentation/foundation/userdefaults)

UserDefaults는 **사용자 기본 설정과 같은 단일 데이터 값에 적합**

대량의 유사한 데이터 (테이블에 대한 레코드, 여러 사용자에 대한 데이터 등)를 저장해야하는 경우에는 sqlite 데이터베이스가 더 적합.

## **1. 데이터 저장하기**

- 첫번째 파라미터에는 여러가지 타입이 들어 갈 수 있다 (Float, Double, Int, Bool, URL.. TestSwitch.isOn 등 )

```swift
UserDefaults.standard.set(Any?, forKey: String)
```

## **2. 데이터 불러오기**

- 위에서 저장한 데이터의 유형에 따라 입맛에 맞게 데이터를 불러오면 된다

```swift
UserDefaults.standard.object(forkey: String)
UserDefaults.standard.url(forkey: String)
UserDefaults.standard.array(forkey: String)
UserDefaults.standard.dictionary(forkey: String)
UserDefaults.standard.string(forkey: String)
UserDefaults.standard.stringArray(forkey: String)
UserDefaults.standard.data(forkey: String)
UserDefaults.standard.bool(forkey: String)
UserDefaults.standard.integer(forkey: String)
UserDefaults.standard.float(forkey: String)
UserDefaults.standard.double(forkey: String)
UserDefaults.standard.dictionaryRepresentation(forkey: String)
```

**3. 데이터 삭제하기**

- 키값만 알면 삭제 할 수 있다

```swift
Userdefaults.standard.removeObjeect(forKey: String)
```
