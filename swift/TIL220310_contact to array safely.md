## 📌 안전하게 배열에 접근하는 방법

`하단의 2번째 방법을 함수화`

일반적으로 배열에 index를 통해 접근하는 상황을 최소화해야하는 것이 옳지만 어쩔 수 없는 상황이 발생하곤 한다.

Swift에서는 좀 더 안전한 처리를 위해 함수 단에서 `guard`를 지원합니다.

하지만 `Array`의 경우 `index`를 통해 접근해서 가져오는 값이 `Optional`타입이 아니기 때문에 접근하는 `index`가 유효하지 않은 경우에는 꼼짝없이 `Fatal error: Index out of range`메세지가 발생합니다.

```swift
let arr = [1,2,3,4]
arr[4] // Fatal error: Index out of range
```

예를 들어 API통신을 통해 배열이 생성되는데 생성한 배열에 값이 추가 되지않은 경우, 호출을 하게 되면 앱이 종료 될 수가 있습니다. 추가적으로 예외처리를 해줄 수는 있겠지만 처음부터 안전한 방법을 만들면 추가적인 예외처리가 없어도 되겠죠.

해당 `Array`를 `index`를 통해 접근했을 때 `Optional`타입으로 반환 해주면

명시적인 장치를 통해서 해당 index에 값이 존재하지 않는 상황에 대한 예외 처리를 진행할 수 있기 때문에 비교적 안전하게 배열에 접근을 진행할 수 있습니다.

아래 `Extension`을 추가하면 해당 배열에 접근하려는 `index`가 유효한지 판단한 뒤 유효할 경우 실제 `Element`를 반환하고 아닌 경우 `nil` 값을 넘겨주게 됩니다.

```swift
extension Collection {
    subscript (safe index: Index) -> Element? {
        return indices.contains(index) ? self[index] : nil
    }
}
```

실제로 적용한 예는 아래와 같습니다.

```swift
let arr = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa"]

func getElementCount(_ index: Int) -> Int {
    guard let value = arr[safe: index] else { return 0 }
    return value.count
}

(-5..<10).forEach {
    print("\($0) : \(getElementCount($0))")
}

/*
[RESULT]
-2 : 0
-1 : 0
0 : 1
1 : 2
2 : 3
3 : 4
4 : 5
5 : 6
6 : 0
7 : 0
*/

```

## 📌 추가적으로 안전하게 배열에 접근하는 방법

### **1. isNotEmpty**

: 해당 배열에 값이 들어 있는지 파악하는 방식으로 위의 에러를 피할 수 있습니다.

```swift
...
if people.isNotEmpty {
  ...
  print(people[0].name)
  ...
  people.remove(people[0])
}
```

이렇게 한다면 안전하겠지만 대신 print문에서 0번째 인덱스를 접근하는 첨자 참조 크래시가 발생할 수도 있습니다.

이에 아래에는 조금 더 안전한 방법입니다.

### **2. safe [가장 추천]**

: safe로 해당 배열이 있는지 판단하고 접근 ( 위에서 소개한 내용 )

`중간에 중간에 있는 인덱스를 안전하게 조회/접근할 때`

```swift
if let person = people[safe: 0] {
  ...
  print(person.name)
  ...
  people.remove(person)
}
```

safe로 해당 배열의 인덱스 값이 있는지 안전하게 조회하고 접근하여 사용한다면 print에서 첨자 참조 크래시를 방지할 수 있습니다.

### **3. first**

: 인덱스의 첫번째 요소 접근

```swift
if let person = people.first {
  ...
  print(person.name)
  ...
  people.remove(person)
}
```

이렇게 옵셔널 바인딩 부분에서 first로 접근한다면 첨자 참조 크래시도 나지 않고 안전하게 접근 및 사용할 수 있습니다.

이렇게 간단한 배열 조회에도 다양하고 안전하게 접근하는 방법에 대해 알아봤습니다.

# [Library] **Hero**

[\*\*🌐 LINK](https://cocoapods.org/pods/Hero) → CocoaPods 사이트\*\*

[https://github.com/HeroTransitions/Hero](https://github.com/HeroTransitions/Hero)

`업데이트 내용이 있을 수 있기 때문에 자세한 내용은 상단 링크를 한번 살펴보고 사용할 것.`

# Hero

**Hero** 는 iOS 뷰 컨트롤러 전환을 빌드하기 위한 라이브러리입니다. UIKit의 성가신 전환 API 위에 선언적 레이어를 제공하여 개발자가 사용자 지정 전환을 쉽게 수행할 수 있도록 합니다.

**사용법**

1. 활성화

`self.hero.isEnabled = true`

1. `heroID`, `heroModifiers` 설정

**property**

`heroID` :

`heroModifiers` : 애니메이션을 정의

**애니메이션 템플릿종류**

- `heroModalAnimationType`
- `heroNavigationAnimationType`
- `heroTabBarAnimationType`

참고용 이미지

![JeRkv (1).svg](<https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ea2bc88f-cbdd-41db-a33b-dced027e9f5b/JeRkv_(1).svg>)

![JeRke.svg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d7934878-5333-4a7b-9161-7e09e1e7e080/JeRke.svg)

![JeRkf.svg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0a577e50-6a2f-4b88-8df4-6bbd10abd14f/JeRkf.svg)

![JeRkJ.svg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/74bfdd22-b6ce-4df5-ad9f-15a8163bdcfe/JeRkJ.svg)

![68747470733a2f2f63646e2e7261776769742e636f6d2f6c6b7a68616f2f4865726f2f656262336632632f5265736f757263 (1).svg](<https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c84f6f7e-3b43-4c6f-a92a-bbe1e39b2171/68747470733a2f2f63646e2e7261776769742e636f6d2f6c6b7a68616f2f4865726f2f656262336632632f5265736f757263_(1).svg>)

![68747470733a2f2f63646e2e7261776769742e636f6d2f6c6b7a68616f2f4865726f2f656262336632632f5265736f757263.svg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6e9e4dd6-8deb-478d-a7ab-cd76b80cff43/68747470733a2f2f63646e2e7261776769742e636f6d2f6c6b7a68616f2f4865726f2f656262336632632f5265736f757263.svg)

# Installation

# CocoaPods

Add the following entry to your Podfile:

`pod 'Hero'`

Then run `pod install`.

Don't forget to `import Hero` in every file you'd like to use Hero.

# Carthage

Add the following entry to your `Cartfile`:

```
github "HeroTransitions/Hero"
```

Then run `carthage update`.

If this is your first time using Carthage in the project, you'll need to go through some additional steps as explained [over at Carthage](https://github.com/Carthage/Carthage#adding-frameworks-to-an-application).

# Swift Package Manager

To integrate using Apple's Swift package manager, add the following as a dependency to your `Package.swift`:

```swift
.package(url: "https://github.com/HeroTransitions/Hero.git", .upToNextMajor(from: "1.3.0"))
```

and then specify `"Hero"` as a dependency of the Target in which you wish to use Hero. Here's an example `PackageDescription`:

```swift
// swift-tools-version:4.0
import PackageDescription

let package = Package(
    name: "MyPackage",
    products: [
        .library(
            name: "MyPackage",
            targets: ["MyPackage"]),
    ],
    dependencies: [
        .package(url: "https://github.com/HeroTransitions/Hero.git", .upToNextMajor(from: "1.6.1"))
    ],
    targets: [
        .target(
            name: "MyPackage",1.6.1
            dependencies: ["Hero"])
    ]
)
```
