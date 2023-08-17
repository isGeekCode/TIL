# Switch case let, If case let, guard case let


switch문을 if, guard 문으로 바꾼 것

switch문은 "=" 앞에 타입(case)을 명시하지만,

if case let, guard case let문은 "=" 앞에 값을 명시

case는 조건을 뜻하기 때문에 if, guard에서도 전부 조건으로 사용가능하다.

- enum 정의

```swift
enum Person {
    case name(String)
    case age(Int)
}
```

- switch 문

```swift
switch person {
case .name(let nameValue):
    print(nameValue)
case .age(let ageValue):
    print(ageValue)
}
```

- switch문 -> if case let

```swift
// 앞에 case문 타입을 먼저 쓴 후 뒤에 값이 위치
if case let Person.name(nameValue) = person {
    print(nameValue)
}
```

- switch문 -> guard case let

```swift
guard case let Person.name(nameValue) = person else {
    print("not exist")
    return
}
print(nameValue)
```

### rx에서 처리하는 switch case let

```swift
_ = rxswiftLoadImage(from: LARGER_IMAGE_URL)
            .observeOn(MainScheduler.instance)
            .subscribe({ result in
                switch result {
                case let .next(image):
                    self.imageView.image = image

                case let .error(err):
                    print(err.localizedDescription)

                case .completed:
                    break
                }
            })
```

next의 정의부를 찾아가면 아래와 같이 정의 되어있다.

```swift
public enum Event<Element> {
    /// Next element is produced.
    case next(Element)

    /// Sequence terminated with an error.
    case error(Swift.Error)

    /// Sequence completed successfully.
    case completed
}

extension Event: CustomDebugStringConvertible {
    /// Description of event.
    public var debugDescription: String {
        switch self {
        case .next(let value):
            return "next(\(value))"
        case .error(let error):
            return "error(\(error))"
        case .completed:
            return "completed"
        }
    }
}
```
