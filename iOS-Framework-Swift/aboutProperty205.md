# 프로퍼티 옵저버(willSet / didSet) - 프로퍼티(2.5)


- [[참고: 애플문서]](https://docs.swift.org/swift-book/LanguageGuide/Properties.html)
- [[참고: Zedd’s Blog]](https://zeddios.tistory.com/247)


**프로퍼티 시리즈**

- [저장프로퍼티(feat.클래스와 구조체) - 프로퍼티(1)](https://github.com/isGeekCode/TIL/blob/main/iOS-Swift/aboutProperty1.md)
- [연산프로퍼티(Getter/Setter) - 프로퍼티(2)](https://github.com/isGeekCode/TIL/blob/main/iOS-Swift/aboutProperty2.md)
- 🍊 **프로퍼티 옵저버(willSet / didSet) - 프로퍼티(2.5)**
- [타입프로퍼티(static) - 프로퍼티(3)](https://github.com/isGeekCode/TIL/blob/main/iOS-Swift/aboutProperty3.md)



# 프로퍼티 옵저버(Property Observers)

이전글에서 소개한 저장프로퍼티와 연산프로퍼티를 감시할 수 있다.

Apple

- 프로퍼티 옵저버는 자신이 정의한 "저장 프로퍼티"에 추가 할 수 있으며, super class(부모클래스)를 상속한 프로퍼티에도 추가 할 수 있습니다.
- 프로퍼티 옵저버는 새로운 값이 프로퍼티의 현재값과 "**동일하더라도**" 속성의 값이 설정(set)될 때 마다 호출됩니다.
- **lazy 저장 프로퍼티를 제외하고**, 정의된 저장 프로퍼티에 프로퍼티 옵저버를 추가할 수 있습니다.



# 옵저버 willSet , didSet

Swift에서는 프로퍼티에 get, set을 사용하거나 didSet, willSet을 사용 할 수 있다. 

하나의 프로퍼티에 get, set, didSet, willSet을 모두 함께 사용하지는 못한다.

- willSet : 값이 저장되기 직전에 호출
- didSet : 값이 저장된 직후에 호출

연산프로퍼티에서 set에 newValue라는 파라미터를 갖는 것 처럼

이 옵저버들은 아래와 같이 파라미터를 갖는다.  

```swift
class CustomCollectionViewCell: UICollectionViewCell {

        override var isSelected: Bool {

                willSet(newValue) {
                        print(" 변경될 값은 \(newValue)")
                }
                didSet(oldValue) {
                        print(" 변경된 값은 \(oldValue)")
                }

        }
}
```

set처럼 아래처럼 파라미터를 생략해서 사용가능하다.

```swift
class CustomCollectionViewCell: UICollectionViewCell {

        
        override var isSelected: Bool {

                willSet {
                        print(" 변경될 값은 \(newValue)")
                }
                didSet {
                        print(" 변경된 값은 \(oldValue)")
                }

        }
}
```

아래처럼 초기값을 선언해준 경우, 

didSet은 저장프로퍼티에 할당되기 전값이 oldValue로 반환된다.

```swift
class StepCounter {

    var totalSteps: Int = 0 {

        willSet(newTotalSteps) {

            print("totalSteps을 \(newTotalSteps)로 설정예정")
        }

        didSet(oldTotalSteps) {

            if totalSteps > oldTotalSteps  {

                print("\(totalSteps - oldTotalSteps)걸음이 추가되었습니다.")
            }
        }

    }
}

let stepCounter = StepCounter()
stepCounter.totalSteps = 200
// totalSteps를 200으로 설정예정
// 200걸음이 추가되었습니다. /// 200(newTotalSteps) - 0 (oldTotalSteps)

stepCounter.totalSteps = 360
// totalSteps를 360으로 설정예정
// 160걸음이 추가되었습니다. /// 360(newTotalSteps) - 200 (oldTotalSteps)

stepCounter.totalSteps = 896
// totalSteps를 896으로 설정예정
// 200걸음이 추가되었습니다. /// 896(newTotalSteps) - 360 (oldTotalSteps)
```
