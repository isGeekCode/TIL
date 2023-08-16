# random함수를 이용해 Random한 숫자 뽑아내기
Random한 Int 값을 뽑기 위해서는 random 함수를 이용하면 된다.

## Random Int 값 뽑기
```swift
let num = Int.random(in: 0...10)
print(num)

// 2
```

## Random Float 값 뽑기
```swift
let num = Float.random(in: 0...10)
print(num)

// 3.35322
```


## Collection으로부터 Random 값 뽑아내기
단, output 값은 nullable한 Optional 값으로 나온다.


```swift
Array.randomElement()
List.randomElement()

let num = (0...10).randomElement()
print(num)

// Optional(5)
```
