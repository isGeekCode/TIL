## πΒ μμ νκ² λ°°μ΄μ μ κ·Όνλ λ°©λ²

`νλ¨μ 2λ²μ§Έ λ°©λ²μ ν¨μν`

μΌλ°μ μΌλ‘ λ°°μ΄μ indexλ₯Ό ν΅ν΄ μ κ·Όνλ μν©μ μ΅μνν΄μΌνλ κ²μ΄ μ³μ§λ§ μ΄μ© μ μλ μν©μ΄ λ°μνκ³€ νλ€.

Swiftμμλ μ’ λ μμ ν μ²λ¦¬λ₯Ό μν΄ ν¨μ λ¨μμΒ `guard`λ₯Ό μ§μν©λλ€.

νμ§λ§Β `Array`μ κ²½μ°Β `index`λ₯Ό ν΅ν΄ μ κ·Όν΄μ κ°μ Έμ€λ κ°μ΄Β `Optional`νμμ΄ μλκΈ° λλ¬Έμ μ κ·ΌνλΒ `index`κ° μ ν¨νμ§ μμ κ²½μ°μλ κΌΌμ§μμ΄Β `Fatal error: Index out of range`λ©μΈμ§κ° λ°μν©λλ€.

```swift
let arr = [1,2,3,4]
arr[4] // Fatal error: Index out of range
```

μλ₯Ό λ€μ΄ APIν΅μ μ ν΅ν΄ λ°°μ΄μ΄ μμ±λλλ° μμ±ν λ°°μ΄μ κ°μ΄ μΆκ° λμ§μμ κ²½μ°, νΈμΆμ νκ² λλ©΄ μ±μ΄ μ’λ£ λ  μκ° μμ΅λλ€. μΆκ°μ μΌλ‘ μμΈμ²λ¦¬λ₯Ό ν΄μ€ μλ μκ² μ§λ§ μ²μλΆν° μμ ν λ°©λ²μ λ§λ€λ©΄ μΆκ°μ μΈ μμΈμ²λ¦¬κ° μμ΄λ λκ² μ£ .

ν΄λΉΒ `Array`λ₯ΌΒ `index`λ₯Ό ν΅ν΄ μ κ·Όνμ λΒ `Optional`νμμΌλ‘ λ°ν ν΄μ£Όλ©΄

λͺμμ μΈ μ₯μΉλ₯Ό ν΅ν΄μ ν΄λΉ indexμ κ°μ΄ μ‘΄μ¬νμ§ μλ μν©μ λν μμΈ μ²λ¦¬λ₯Ό μ§νν  μ μκΈ° λλ¬Έμ λΉκ΅μ  μμ νκ² λ°°μ΄μ μ κ·Όμ μ§νν  μ μμ΅λλ€.

μλΒ `Extension`μ μΆκ°νλ©΄ ν΄λΉ λ°°μ΄μ μ κ·Όνλ €λΒ `index`κ° μ ν¨νμ§ νλ¨ν λ€ μ ν¨ν  κ²½μ° μ€μ Β `Element`λ₯Ό λ°ννκ³  μλ κ²½μ°Β `nil`Β κ°μ λκ²¨μ£Όκ² λ©λλ€.

```swift
extension Collection {
    subscript (safe index: Index) -> Element? {
        return indices.contains(index) ? self[index] : nil
    }
}
```

μ€μ λ‘ μ μ©ν μλ μλμ κ°μ΅λλ€.

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

## πΒ μΆκ°μ μΌλ‘ μμ νκ² λ°°μ΄μ μ κ·Όνλ λ°©λ²

### **1. isNotEmpty**

: ν΄λΉ λ°°μ΄μ κ°μ΄ λ€μ΄ μλμ§ νμνλ λ°©μμΌλ‘ μμ μλ¬λ₯Ό νΌν  μ μμ΅λλ€.

```swift
...
if people.isNotEmpty {
  ...
  print(people[0].name)
  ...
  people.remove(people[0])
}
```

μ΄λ κ² νλ€λ©΄ μμ νκ² μ§λ§ λμ  printλ¬Έμμ 0λ²μ§Έ μΈλ±μ€λ₯Ό μ κ·Όνλ μ²¨μ μ°Έμ‘° ν¬λμκ° λ°μν  μλ μμ΅λλ€.

μ΄μ μλμλ μ‘°κΈ λ μμ ν λ°©λ²μλλ€.

### **2. safeΒ [κ°μ₯ μΆμ²]**

: safeλ‘ ν΄λΉ λ°°μ΄μ΄ μλμ§ νλ¨νκ³  μ κ·Ό ( μμμ μκ°ν λ΄μ© )

`μ€κ°μ μ€κ°μ μλ μΈλ±μ€λ₯Ό μμ νκ² μ‘°ν/μ κ·Όν  λ`

```swift
if let person = people[safe: 0] {
  ...
  print(person.name)
  ...
  people.remove(person)
}
```

safeλ‘ ν΄λΉ λ°°μ΄μ μΈλ±μ€ κ°μ΄ μλμ§ μμ νκ² μ‘°ννκ³  μ κ·Όνμ¬ μ¬μ©νλ€λ©΄ printμμ μ²¨μ μ°Έμ‘° ν¬λμλ₯Ό λ°©μ§ν  μ μμ΅λλ€.

### **3. first**

: μΈλ±μ€μ μ²«λ²μ§Έ μμ μ κ·Ό

```swift
if let person = people.first {
  ...
  print(person.name)
  ...
  people.remove(person)
}
```

μ΄λ κ² μ΅μλ λ°μΈλ© λΆλΆμμ firstλ‘ μ κ·Όνλ€λ©΄ μ²¨μ μ°Έμ‘° ν¬λμλ λμ§ μκ³  μμ νκ² μ κ·Ό λ° μ¬μ©ν  μ μμ΅λλ€.

μ΄λ κ² κ°λ¨ν λ°°μ΄ μ‘°νμλ λ€μνκ³  μμ νκ² μ κ·Όνλ λ°©λ²μ λν΄ μμλ΄€μ΅λλ€.

# [Library] **Hero**

[\*\*πΒ LINK](https://cocoapods.org/pods/Hero) β CocoaPods μ¬μ΄νΈ\*\*

[https://github.com/HeroTransitions/Hero](https://github.com/HeroTransitions/Hero)

`μλ°μ΄νΈ λ΄μ©μ΄ μμ μ μκΈ° λλ¬Έμ μμΈν λ΄μ©μ μλ¨ λ§ν¬λ₯Ό νλ² μ΄ν΄λ³΄κ³  μ¬μ©ν  κ².`

# Hero

**Hero**Β λ iOS λ·° μ»¨νΈλ‘€λ¬ μ νμ λΉλνκΈ° μν λΌμ΄λΈλ¬λ¦¬μλλ€.Β UIKitμ μ±κ°μ  μ ν API μμ μ μΈμ  λ μ΄μ΄λ₯Ό μ κ³΅νμ¬ κ°λ°μκ° μ¬μ©μ μ§μ  μ νμ μ½κ² μνν  μ μλλ‘ ν©λλ€.

**μ¬μ©λ²**

1. νμ±ν

`self.hero.isEnabled = true`

1. `heroID`, `heroModifiers` μ€μ 

**property**

`heroID` :

`heroModifiers` : μ λλ©μ΄μμ μ μ

**μ λλ©μ΄μ ννλ¦Ώμ’λ₯**

- `heroModalAnimationType`
- `heroNavigationAnimationType`
- `heroTabBarAnimationType`

μ°Έκ³ μ© μ΄λ―Έμ§

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

Then runΒ `pod install`.

Don't forget toΒ `import Hero`Β in every file you'd like to use Hero.

# Carthage

Add the following entry to yourΒ `Cartfile`:

```
github "HeroTransitions/Hero"
```

Then runΒ `carthage update`.

If this is your first time using Carthage in the project, you'll need to go through some additional steps as explainedΒ [over at Carthage](https://github.com/Carthage/Carthage#adding-frameworks-to-an-application).

# Swift Package Manager

To integrate using Apple's Swift package manager, add the following as a dependency to yourΒ `Package.swift`:

```swift
.package(url: "https://github.com/HeroTransitions/Hero.git", .upToNextMajor(from: "1.3.0"))
```

and then specifyΒ `"Hero"`Β as a dependency of the Target in which you wish to use Hero. Here's an exampleΒ `PackageDescription`:

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
