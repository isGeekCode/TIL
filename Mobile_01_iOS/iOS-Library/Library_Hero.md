# Library - Hero

[\*\*🌐 LINK](https://cocoapods.org/pods/Hero) → CocoaPods 사이트\*\*

[https://github.com/HeroTransitions/Hero](https://github.com/HeroTransitions/Hero)

`업데이트 내용이 있을 수 있기 때문에 자세한 내용은 상단 링크를 한번 살펴보고 사용할 것.`

# Hero

**Hero** 는 iOS 뷰 컨트롤러 전환을 빌드하기 위한 라이브러리이다. UIKit의 성가신 전환 API 위에 선언적 레이어를 제공하여 개발자가 사용자 지정 전환을 쉽게 수행할 수 있도록 만든다.

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

<br><br>

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

