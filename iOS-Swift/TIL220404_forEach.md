## 여러개의 Action을 한번에 추가하기

콜렉션의 사용법중 forEach와 for in 이 있다. for in 모두 요소의 갯수만큼 반복하지만 for each는 클로저를 파라미터로 주고 요소 갯수만큼 반복한다.

즉,

**반복 실행하려는 코드를 파라미터로 받고, 저장된 요소는 클로저 상수로 전달된다**

**for - in**문은 우리가 **직접 구현**하는 "**반복문**"

하지만 **forEach**는 내가 반복하고 싶은 구문을

**forEach라는 함수의 파라미터**로 "**클로저**"로 작성해서 넘겨주는 것

그렇기 때문에,

**반복문 안에서만 사용**할 수 있는 **continue**, **break**는

**for - in 에선 사용 가능하지만, forEach에서는 불가능**

**내가 전달한 print 함수를 찍는 클로저를 nums 요소의 갯수(4)만큼 반복**

```swift
let nums: [Int] = [1, 2, 3, 4]

nums.forEach {
    print($0)       // 1 2 3 4
}
```

반복 index 보기

```swift
nums.enumerated().forEach {
    print("(index: \($0) num: \($1))")             // (index: 0 num: 1) (index: 1 num: 2) (index: 2 num: 3) (index: 3 num: 4)
}

nums.indices.forEach {
    print("(index: \($0) num: \(nums[$0]))")       // (index: 0 num: 1) (index: 1 num: 2) (index: 2 num: 3) (index: 3 num: 4)
}
```

or - in과 마찬가지로 **enumerated** 메서드나 **indices** 를 이용

Dictionary

```swift
let dict: [String : String] = ["A" : "Apple", "B" : "Banana", "C" : "Cherry"]

dict.forEach {
    print("(\($0.key) : \($0.value))")  // (B : Banana) (C : Cherry) (A : Apple)
}

dict.forEach { (key, value) in
    print("(\(key) : \(value))")        // (C : Cherry) (A : Apple) (B : Banana)
}

dict.keys.forEach {
    print($0)       // B C A
}

dict.values.sorted().forEach {
    print($0)       // Apple Banana Cherry
}
```

set

```swift
let nums: Set<Int> = [1, 2, 3, 4]

nums.forEach {
    print($0)               // 2 3 1 4
}
```

여러개의 얼럿액션버튼 배열을 생성해 alert이라는 얼럿컨트롤러에 foreach를 이용할 수 있다.

```swift
[
            prdButton,
            devButton,
            qaButton,
            cancelButton
        ].forEach {
            alert.addAction($0)
        }
```

마찬가지로 addSubView에서도 사용가능

```swift
override func loadView() {
        let view = UIView()
        self.view = view
        view.backgroundColor = .systemBackground
        [decreaseButton, valueLabel, increaseButton, activityIndicator].forEach {
            self.view.addSubview($0)
        }
```
