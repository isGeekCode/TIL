# 앱심사 - 수출 규정 관련 문서가 누락됨(Missing Compliance) / 우회처리

TestFlight 업로드시 아래와 같은 메세지가 매번 뜨게 되어있다.

- 수출 규정 관련 문서가 누락됨(Missing Compliance)

## 우회하기

만약 앱에서 계속 암호화를 사용하지 않을 예정이라면

Xcode에서 Info.plist 설정을 해주면 TestFlight 업로드 시 더 이상 묻지 않고 자동으로 NO 처리된다.

**Info.plist에 아래 항목 추가**

※ Info.plist 파일 우클릭 > Open As를 선택하면 Source Code, Property List 버전을 선택할 수 있다.

- Source Code

```swift
<key>ITSAppUsesNonExemptEncryption</key>
<false/>
```

- Property List

```swift
Key : App Uses Non-Exempt Encryption
Type : Boolean
Value : NO
```
