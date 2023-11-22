# Array - 특정값이 동일하거나 포함한 경우 찾기 :  firstIndex()

배열(Array)은 프로그래밍에서 가장 기본적인 자료 구조 중 하나이며, 데이터 요소(element)를 담는 용도로 사용된다.

Swift에서 배열에서 특정 값이 포함된 요소의 인덱스를 찾으려면, firstIndex 메서드를 사용할 수 있다. firstIndex 메서드는 배열에서 첫 번째로 해당 값을 갖는 요소의 인덱스를 반환하며, 해당 값이 없는 경우 nil을 반환한다.


## 포함한 경우찾기
아래 예시는 배열에서 해당 값이 포함된 값을 찾아서 해당 위치에 다른 값을 할당하는 내용이다.
```swift

let array = ["apple", "banana", "orange juice", "grape"]

if let index = array.firstIndex(where: { $0.contains("juice") }) { 
    print(array[index] : \(array[index]))
}
```


## 동일한 경우 찾기

이때 firstIndex를 사용하는 방법은 두가지이다. 

- of 파라미터를 사용하는 경우, 특정 index를 구한다. 
- where 파라미터를 사용하는 경우, 특정 index를 찾아서 클로저를 리턴하여 메서드를 구현할 수 있다.  


  
```swift
// 배열에 juice가 있는지 찾는 코드

let array = ["apple", "banana", "orange juice", "grape", "juice"]

let index = array.firstIndex(of: "juice")

if let index = array.firstIndex(where: { $0 == "juice" }) {
    print(array[index] : \(array[index]))
}

```



## 예제2. 
이 방법은 IOS에서 웹뷰를 다룰때, 들어온 query를 가공할때 유용하다.


```swift
// 들어온 URL
let urlString = "good_name=수채화+파란커튼&good_no=86060&currency=410&pay_method=CARD&site_name=HootTown&shop_name=GeekCode&buyr_name=isID&buyr_tel1=01022073306"
```

### 1. 만약 good_name을 가공한다면 이 urlString을 `&`를 이용하여 잘라준다.

```swift
var stringArr = urlString.components(separatedBy: "&")
```


### 2. `firstIndex`함수를 이용하여 indexPath를 가져온다.

```swift
let goodNameNum = stringArr.firstIndex { $0.contains("good_name=") }
guard let goodNameIndex = goodNameNum else { return }

```
### 2. 해당 indexPath의 값을 가져온다.


```swift
let goodNameQuery = stringArr[goodNameIndex]
guard let goodNameValue = goodNameQuery.components(separatedBy: "good_name=").last else { return }

print(goodNameValue) //  수채화+파란커튼
```

### 3. 다시 배열에 쿼리로 추가한다. 필요할 경우 해당 index로 넣어준다.
```swift

let newText = "보타닉+화분"
let newGoodName = "good_name=\(newText)"

// 그냥 배열에 추가하는 경우
stringArr.append(newGoodName)


// 해당 index에 넣을 경우
stringArr[goodNameIndex] = newGoodName
```

### 4. 다시 `&`을 넣어서 하나의 String으로 합치기

```swift
let newArray = stringArr.joined(separator: "&")
```
