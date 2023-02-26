# Swift문법 기초
# 1. 변수 왜 그리고 어떻게 쓰는가?

변수라는 것은 마치 물건을 정리하는 것과 비슷한 용도로 사용한다.

영양제는 영양제를 따로 분류하는 곳에 두고, 옷은 옷장에, 음식은 냉장고에 있는 것처럼 어떤 공간에 물건을 넣어놓는 것은 목적성을 가지고 있다.

변수도 어떤 값을 보관하기 위해 사용하는 공간이다. 

이 공간에 이름을 부여하고 그 이름을 부르면 그안에 있는 것을 사용할 수 있는 것이다. 

### ➖ 변수만들기

ios에서 사용하는 언어는 한글을 지원한다. 간단하게 살펴보자.

```swift
let 내일입을옷 = 맨투맨티
```

Step1: `let` 을 쓰고 우측에 앞으로 부르고 싶은 `이름`을 적는다

Step2: `이름` 옆에 `=` 를 쓰고 우측에 담을 `내용물`을 적는다.

### ➖ 자료형

이 변수안에 들어가는 내용물에게도 종류라는 게 있을 것이다. 

맨투맨티 → 옷 , 떡볶이 → 음식 , TV → 가전제품 , 침대 → 가구

Swift언어에서도 우리가 다룰 특정 값에 따라 종류를 나눈다.

- 글자 → `String`
- 참, 거짓 → `Bool`
- 숫자
    - 정수 → `Int`   📌 양수와 음수 모두 넣을 수 있다.
    - 실수
        - 32비트 부동소수 → `Float`
        - 64비트 부동소수 → `Double`

일단 숫자부턴.. 핑핑 돌것 같은데 일단 처음에 사용할 것은 아래 4가지만 사용한다고 생각하면된다. 

- String
- Bool
- Int
- Float

### ➖ 변수에 타입 명시하기

위에서는 `let 이름 = 내용`의 형태로 변수를 만들었다. Swift는 자동으로 타입을 계산할 수 있기때문에 타입을 따로 써주지 않지만, 타입추론이 많아진다는 말은 생각이 많아져 앱이 느려진다는 말이다. 생각하게 하지말자.

타입을 넣어주면 직관적으로 전달할 수 있다.  이번엔 실제 코드로 만들어보자.

```swift
let myName: String = "긱코드"

let isTrue: Bool = true
let isFinish: Bool = false

let number: Int = 1
let minusNumber: Int = -1

let myMacBookWidth: Float = 300.53
```

위와 같이 변수이름 우측에 `: 타입`의 구조로 만들 수 있다.

# 2. 변수의 종류

이 내용물이 들어갈 공간(상자)를 변수라고 말했다. 이 상자는 두종류가 있다.

한번 넣으면 내용물을 바꿀수 없는 것과 내용물을 바꿀수 없는 것이다. 

통상적으로 전자는 상수라고 부르고, 후자는 변수 라고 부른다. 

```swift
// 상수
let finalScore = 3
// 변수
var count = 2
```

상수안에 값을 한번넣으면 그 값에는 더이상 새로운 값을 부여할 수 없다. 대신 변수는 언제든지 바꿀 수 있다.

새로운 값을 할당하려면 `변수명 = 새로운 값`의 형태로 이력하면된다.

```swift
// 상수
let finalScore = 3
finalScore = 5      // ERROR!!!!!!!
print(finalScore)   // 3

// 변수
let count = 2
count = 3
print(count)   // 3
coutn = 10
print(count)   // 10

/*
print()의 괄호안에 변수, 상수명을 넣어서 사용하면
내용물을 콘솔창에서 볼 수 있다.
*/
```

상수를 그래도 사용하려면 상수자체를 새로 다른 변수에 넣는 방법도 있다.

```swift
// 상수
let finalScore = 3
finalScore = 5      // ERROR!!!!!!!
print(finalScore)   // 3

// 새로운 변수에 담기
var newScore = finalScore
print(finalScore)   // 3
newScore = 5
print(newScore)     // 5
```

이렇게 새롭게 다른 변수에 담을 수 있다.

# 3. 연산자란? - Operator

주로 사용하는 연산자는 `대입연산자`, `사칙연산자`, `비교연산자`  등이 있다
대

## ➖ 대입연산자

위에서 상수와 변수를 선언할 때 사용한 `=`를 말한다.

## ➖ 사칙연산자

숫자 타입을 사칙연산을 할 수 있도록 도와주는 연산자이다. 

사칙연산자는 더하기`+`, 빼기`-`, 곱하기 `*`, 나누기`/` 를 할수 있다.

이때 특별히 나누기를 할 때, 나머지는 표시되지않는다.  나머지는 `%`를 통해서 볼수 있다. 

```swift
// 수학에서 사용하는 표기방법
7 / 3 = 2 ••• 1

// Swift가 표현하는 방법
print(7 / 3) // 2 -> 나머지는 기본적으로 보여주지않는다.
print(7 % 3) // 1 -> 나머지
```

### 🟰 String타입에서 `+` 사용

특별히  `+`는 String에서도 사용가능하다. 

```swift
let fullAddress = "서울시" + "마포구"
print(fullAddress)    // 서울시마포구

// 띄어쓰기도 문자열에 포함해야한다.
let otherAddress = "서울시" + " " + "영등포구"
// 혹은 "서울시 " + "영등포구" , "서울시" + " 영등포구" 도 동일하다
print(fullAddress)    // 서울시 영등포구
```

## ➖ 비교연산자

어떤 두가지를 비교하는 연산자이다. 비교하는 방법도 여러가지가 있는데 아래와 같다. 

- a `==` b → a와 b가 동일한가?
- a `!=` b → a와 b가 동일하지 않은가?
- a `>` b → a가 b보다 큰가?
- a `<` b → a가 b보다 작은가?
- a `>=` b → a가 b 이상인가?
- a `<=` b → a가 b 이하인가?

📌  비교연산자는 비교를 하기 때문에 결과값은 참 거짓을 나타내는 `Bool`일 수 밖에 없다.

```swift
let isEqual = 내밥그릇크기 == 옆사람국그릇크기
print(isEqual)        //false

let isNotEqual = 내밥그릇크기 != 옆사람국그릇크기
print(isEqual)        //true

let isLarge = 5 > 3 
print(isLarge)        //true

let isEqualOrisLarge = 2 >= 3 
print(isLarge)        //false
```

## ➖ 논리연산자

여러가지 조건을 한꺼번에 표현할 수 있다.

- a `&&` b : and
    - a 와 b 모두 true 일 때, 결과값은 `true`
    - a, b 둘중 하나라도 true가 아니라면 결과값은 `false`
    - a 와 b 모두 false 일 때, 결과값은  `false`
- a `||` b : or
    - a 와 b 모두 true 일 때, 결과값은 `true`
    - a, b 둘중 하나라도 true라면 결과값은 `true`
    - a 와 b 모두 false 일 때, 결과값은  `false`

```swift
// 나와 내 친구의 점수, 반평균점수를 선언
let myScore = 80
let frendScore = 95
let standardScore = 90

myScore > standardScore // false
frendScore > standardScore // true

// &&은 두 조건이 전부 true여야 결과로 true가 된다.
myScore > standardScore && frendScore > standardScore // false
myScore > 0 && frendScore > 0 // true

// ||은 한 조건이라도 true라면 결과로 true가 된다.
myScore > standardScore || frendScore > standardScore // true
```

# 4. 여러 개의 변수를 모아서 쓰는 컬렉션 타입

언어마다 컬렉션 타입은 다양한데, Swift는 `Array`, `Set`, `Dictionary`, `Tuple` 형태를 사용한다. 일단 Tuple은 나중에 설명

## ➖ Array (배열)

배열은 동일한 타입을 묶어놓은 형태를 말한다. 대괄호 안에 넣어서 사용한다. 또한 변수선언과 마찬가지로 타입추론이 가능하지만 되도록 타입을 적어주자. 타입을 명시할 때는 `:[ ]` 대괄호 안에 타입을 넣어준다. 혹은 `Array< >` 소괄호 안에 타입을 넣어줘도 동일하게 생성된다.  

```swift
// 문자열이 들어간 배열
let foods = ["밥", "제육볶음", "떡볶이", "미역국"]

// 타입을 넣어주는 선언
let animals: [String] = ["소", "돼지", "말", "양"]
// 혹은 let animals: Array<String> =  ["소", "돼지", "말", "양"]
let numbers: [Int] = [3, 4, 16, 30]
// 혹은 let numbers: Array<Int> = [3, 4, 16, 30]

print(animals[0])     // 소
print(numbers[4])     // 30
```

### 🟰 배열의 n번째 요소 보기

배열의 이름뒤에 대괄호를 붙이고 indexPath 숫자를 넣으면된다. 

컴퓨터는 첫번째를 `0`으로 시작하여 순서대로 올라간다. 

```swift
// animals: [String] = ["소", "돼지", "말", "양"]
print(animals[0])     // 소
print(numbers[3])     // 양
```

### 📌 배열에서 주의할 점

 순서를 지정할 때, 실제 존재하지않는 순서를 입력하면 에러가 발생한다.  안전한 방법을 위해서는 배열의 갯수를 체크해야한다. 

```swift
let animals: [String] = ["소", "돼지", "말", "양"]
// 혹은 let animals: Array<String> =  ["소", "돼지", "말", "양"]
print(animals[5])     // ERROR!!

print(animals.first)      // 소
print(animals.last)       // 양

// 배열안의 갯수 구하기
let animalsCount = animals.count
print(animalsCount)       // 4
// 마지막 요소를 구하려면 배열안의 갯수에서 1을 빼주어야 한다.
// 코딩에서 순서는 항상 0, 1, 2 의 순서로 올라가기 때문이다. 
print(animals[animalsCount-1]       // 양
```

## ➖ **딕셔너리 Dictionary**

key-value 구조를 가지고 있고, 순서가 없는 콜렉션이다.

각 key는 식별자 역할을 하며 key를 통해 value를 호출 할 수 있다.

딕셔너리 안의 요소를 볼 경우, 순서는 매번 바뀐다. 

```swift
*Dictionary*<Key, Value>
```

```swift
// 빈 Dictionary 생성
var emptyDictionary = [String: Int]()
print(emptyDictionary)

// Dictionary 생성 및 요소 추가
var dictionary = ["one": 1, "two": 2, "three": 3]
dictionary["four"] = 4
print(dictionary)

// Dictionary 요소 삭제
dictionary["three"] = nil
print(dictionary)

// Dictionary 요소 변경
dictionary.updateValue(5, forKey: "four")
print(dictionary)

// Dictionary 순회
for (key, value) in dictionary {
    print("\(key): \(value)")
}

// Dictionary 키, 값 추출
let keys = Array(dictionary.keys)
let values = Array(dictionary.values)
print(keys)
print(values)
```

## ➖ **집합 Set**

동일한 타입의 값을 저장하는 순서가 따로 없는 콜렉션이다.

Set을 사용하여 데이터를 관리하면 중복을 제거하고 고유한 요소들을 쉽게 관리할 수 있다.

```swift
// 빈 Set 생성
var emptySet = Set<Int>()
print(emptySet)

// Set 생성 및 요소 추가
var fruitSet: Set<String> = ["apple", "banana", "orange"]
fruitSet.insert("kiwi")
print(fruitSet)
// ["kiwi", "apple", "banana", "orange"]

// Set 요소 삭제
fruitSet.remove("banana")
print(fruitSet)
// ["kiwi", "apple", "orange"]

// Set 요소 검색
let contains = fruitSet.contains("orange")
print(contains)
// false

```

### Set 연산하기

- **`union()`**: 두 개의 Set을 병합하여 하나의 Set으로 만든다. 이 때 중복된 요소는 하나만 유지된다.
- **`intersection()`**: 두 개의 Set에서 공통된 요소만을 가지는 하나의 Set을 반환한다.
- **`subtracting()`**: 하나의 Set에서 다른 Set에 포함된 요소를 제외한 요소만을 가지는 하나의 Set을 반환합니다.
- **`symmetricDifference()`**: 두 개의 Set에서 공통되지 않은 요소만을 가지는 하나의 Set을 반환합니다.

```swift
// Set 연산
let setA: Set<Int> = [1, 2, 3, 4]
let setB: Set<Int> = [3, 4, 5, 6]

// 합집합
let unionSet = setA.union(setB)
print(unionSet)
// [5, 1, 2, 3, 4, 6]

// 교집합
let intersectionSet = setA.intersection(setB)
print(intersectionSet)
// [3, 4]

// 차집합
// setA에서 setB의 요소를 뺀다
let subtractSet = setA.subtracting(setB)
print(subtractSet)
// [1, 2]

// 여집합
let symmetricDifferenceSet = setA.symmetricDifference(setB)
print(symmetricDifferenceSet)
// [1, 2, 5, 6]
```

# 5. 조건문 - 조건을 가지고 분기를 하는 조건문

### 조건문의 구조의 의미

조건문이란 `~라면 ~ 한다.` 라는 내용을 표현한 것이다. 마치 언어에서 가정법과 같다. 

**내가 똑똑하다면 시험성적이 좋다.** 라는 문장을 살펴보자

- `내가 똑똑하다면` : 조건
- `시험성적이 좋다` : 결과

다만, 코딩에 있어서는 `결과`가 아니라 어떤 `행동`을 할지를 적어준다. 

조금더 코딩스러운 예문을 만들어 보면 이렇게 만들어볼 수 있다.

**내 점수가 100점이라면, 맥북을 사러간다.** 

- `내 점수가 100점이라면` : **조건**
- `맥북을 사러간다` : **행동**

보통 코딩을 할때는 이런 경우에 이런 동작을 하게 만들기 때문에 이런 구조를 갖게 된다. 

### If문

이걸 Swift문법에 맞춰서 `If문`으로 만들어면 아래와 같다.

여기서 조건은 항상 `Bool`타입의 결과를 가지고 있어야 조건문을 사용할 수 있다.

### **기본구조** `if 조건 { }`

`if` 다음에는 **조건**이 온다. 

`{ }` 내부에는 **어떤 행동을 할지** 선언한다.

```swift
let myScore = 100

if myScore == 100 {
  print("맥북 사러가자")
}
```

### 기본구조 `if 조건 { } else { }`

`else`는 **앞에서 말한 조건이 아닌 경우**를 뜻한다.  따라서 별다른 조건을 표기하지않아도된다. `앞에서 말한 조건에 전부 해당하지 않는다`는 것을 뜻한다.

`else { }` 안에는 이때들어갈 행동을 넣어준다.

```swift
let myScore = 100

if myScore == 100 {
  print("맥북 사러가자")
} else {
  print("맥북은 다음에")
}
```

### 기본구조 `if 조건 { } else if 조건 { } else { }`

`else if`는 **앞에서 말한 조건이 아닌 또 다른 조건을** 뜻한다.  따라서 `else if` 뒤에는 **새로운 조건**을 넣어준다. 

그리고 마찬가지로 `else` 는 `앞에서 말한 조건에 전부 해당하지 않는다`는 것을 뜻한다.

`else { }` 안에는 이때들어갈 행동을 넣어준다.

```swift
let myScore = 100

if myScore == 100 {
  print("맥북 사러가자")
} else if myScore > 90 {
  print("완전 아쉽다")
} else {
  print("맥북은 다음 기회에")
}
```

### **if문 안에 if문**

가끔 여러가지 조건을 충족해야하는 경우가 있다. 논리연산자로 표현할 수도 있지만 if 안에 if를 넣을 수도 있다.

아래는 다음과 같은 조건이 있다.

- 수학성적이 80점을 넘지않으면 수학시험 나머지공부
- 동시에 과학성적이 80점을 넘지않으면 과학시험 나머지공부 , 넘으면 놀러간다는 조건

```swift
let myMathScore = 85
let myScienceScore = 70

if myMathScore > 80 {
    if myScienceScore > 80 {
      print("나가놀자")

    } else {
      print("과학시험 나머지공부")
    }

} else {
    print("수학시험 나머지공부")
}
```

위와 같이 if를 여러개 중첩해서 사용할 수 있지만 가독성이 떨어질 수 있다. 이를 `네스팅`이 많아진다고 말한다.  이럴 땐 내부 조건을 함수로 분리시키거나 논리연산자를 적극적으로 사용하자.

## 3항 연산

정말 간단한 조건문이라면 `a ? b : c` 의 형태로 만들 수 있다.

아래는 if 조건문을 3항연산으로 표현한 것이다.

```swift
//예제 1
let myScore = 100

if myScore == 100 {
  print("맥북 사러가자")
} else {
  print("맥북은 다음에")
}

myScore == 100 ? print("맥북 사러가자") : print("맥북은 다음에")

//예제 2
내가 좋아하는 과일이 사과라면 오늘 점심 디저트는 사과, 내가 좋아하는 과일이 사과가 아니면 포도를 먹는다.

let apple = "사과"
let grape = "포도"
let myFavoriteFruit = "사과"

let myLunchDesert = myFavoriteFruit == apple ? apple : grape
print(myLunchDesert) // 사과
```

# 6. 반복문 - 같은 것을 반복해주는 반복문

### 반복문의 의미

`**~동안 ~ 하다**` 라는 의미로 사용한다. 

때문에 기본구조는 `범위`, 그리고 `행동`이 들어간다. 

Swift에서는 `..<`를 사용하면 범위 내에서 끝값을 제외시키며, `...`를 사용하면 끝값을 포함시킨다.

예를 들어, `1..<5`는 1부터 4까지의 범위를 나타내고, `1...5`는 1부터 5까지의 범위를 나타낸다.

### For문

### 기본구조 `for 요소 in 범위 { 행동 }`

### 콜렉션타입에서 꺼내쓰기

for 문은 범위를 하나 정해놓고 그안의 요소를 변수에 담아서 꺼내는 것을 반복한다. 

범위에는 콜렉션타입이 전부 들어갈 수 있다.

간단하게 한글로 표현을 하자면 아래와 같다.

- 바구니 안에 공들이 들어있다.
- 빨간공도 있고 노란공도 있고 파란공도 있다.
- 바구니에서 공을 하나씩 순서대로 꺼낼거다.

```swift
// 배열의 요소를 하나씩 꺼내는 방법
let 바구니 = ["빨간공", "노란공", "파란공"]
for 공 in 바구니 {
  print(공)
}
// "빨간공"
// "노란공"
// "파란공"
```

Set는 순서가 정해져있지않은 것이 특징이기 때문에 for문에 사용할경우 랜덤하게 나온다.

set이라 중복숫자는 나오진않음

```swift
var numberSet: Set<Int> = [3, 1, 4, 1, 5, 9]

for number in numberSet {
    print(number)
}
// 1
// 3
// 5
// 9
// 4
```

Dictionary를 For문에 사용하면  Key와 Value를 각각 변수로 지정해서 꺼낼 수 있다.

```swift
let prices = ["apple": 0.99, "banana": 0.25, "orange": 0.50]

for (fruit, price) in prices {
    print("\(fruit): $\(price)")
}
/*
apple: $0.99
banana: $0.25
orange: $0.5
*/
```

### 범위 연산자를 사용해 숫자를 꺼내기

콜렉션타입안에서 특정 순서대로 값을 꺼내고 싶거나, 이 콜렉션타입의 요소의 갯수를 모르는 경우, 범위연산자를 써서 숫자를 꺼내기도 한다. 그리고 단순하게 범위연산자를 넣어서 몇번 꺼낼건지 범위를 정하기도 한다. 

```swift
// 범위안의 숫자를 i에 담아 꺼내기
for i in 0 ... 5 {
    print(i)
}
/*
0
1
2
3
4
5
*/

// 범위안의 숫자를 i에 담아 꺼내기
for i in 1 ..< 5 {
    print(i)
}
/*
1
2
3
4
*/

// 범위 안의 숫자 만큼 행동을 반복하기
for i in 1 ... 3 {
    print("헬로")
}
/*
헬로
헬로
헬로
*/

// 배열의 갯수 만큼 요소 꺼내기
// 0 ..< numbers.count 와 0 ... numbers.count-1 , 1 ... numbers.count 은 모두 동일하다.
let numbers = [1, 2, 3, 4, 5]
for number in 0 ..< numbers.count {
    print(number)
}
/*
1
2
3
4
5
*/
```

### While문

### 기본구조 `while 조건 { 행동 }`

```swift
while 조건식 {
  // 조건식이 참일 때 실행할 코드
}
```

for - in 말고도 while문 이라는 것도 있다.

for - in은 범위를 넣는 반면

while에는 `조건`이 들어간다. 이 조건이 참인 경우 어떤행동을 할지 선언한다.

아래는 처음 number를 0으로 선언하고 반복할 때마다 먼저 print하고 1을 추가하는 코드이다.

**먼저 프린트, 그다음 1을 추가** 

```swift
var number = 0

while number <= 3 {
    print(number)
    number += 1
}
/*
3이하인 경우에 반복하라고 했기 때문에 number가 3가 될때에는 프린트를 하고
+=1때문에 1이 추가되어도 4은 나올 수 없다.  
만약 +=가 print보다 앞에 있었다면 4가 나왔을 것이다. 
0
1
2
3
*/

var number = 0

while number <= 3 {
    number += 1
    print(number)
}
/*
먼저 값을 추가하고 print를 하기 때문에 1은 나올수 없다.
1
2
3
4
*/

let numbers = [1, 2, 3, 4, 5]
var index = 0

while index < numbers.count {
    let number = numbers[index]
    print(number)
    index += 1
}
/*
1
2
3
4
5
*/
```

### For - Where문

이밖에도  for where문 도 있다.

for문에 where 를 사용하면 조건을 추가할 수 있다.

`범위 안에서 where 조건 을 만족하는 요소만 가져오는 것`이다.

```swift
let numbers = [1, 2, 3, 4, 5]

// 짝수만 가져오기
for number in numbers where number % 2 == 0 {
    print(number)
}
/*
2
4
*/
```

### Repeat - While문

마지막으로  while문과 반대로 쓰이는 반복문이다. 

while문은 조건이 앞에 붙고 그 조건이 참인동안 코드를 실행한다면

Repeat - While문은 먼저 코드를 실행하고 조건이 참인지 체크한다.

```swift
repeat {
    // 코드 블록 실행
} while 조건식
```

```swift
var count: Int = 0

repeat {
    print("1을 입력하세요")
    count += 1
} while count < 3

print("갯수: \(count)")
/*
1을 입력하세요
1을 입력하세요
1을 입력하세요
갯수: 3
*/
```

# 7. func - 코드를 따로 뺄 수 있도록 해주는 함수

반복되는 코드는 함수를 만들어 따로 뺴서 사용할 수 있다.

### 파라미터가 없는 함수

아래는 파라미터가 없는 아주 기본적인 함수이다.

```swift
func printMyName() {
  print("긱코드")
}

printMyName()
// 긱코드
```

### 파라미터가 있는 함수

만약 함수를 사용하는데 상황에 따라 다른 내용을 넣고 싶다면 파라미터를 만들어서 사용할 수 있다.

```swift
func printMyName(name: String) {
  print(name)
}

printMyName(name: "긱코드")
// 긱코드

printMyName(name: "리이오")
// 리이오
```

파라미터는 상황에 따라 얼마든지 추가할 수 있다.

# 8. enum - 선택지를 만들어주는 열거형

enum이란 쉽게 말해 타입을 하나 만드는 것으로 볼 수 있다. enum타입은 특정 유형의 값을 가지는 연관된 그룹을 정의하는데 사용된다.

- enum은 특별하게 따로 숫자를 정해주지 않아도 rawValue를 0부터 순서대로 가진다.
- 새롭게 숫자를 부여할 수 도 있고 그밖의 다른 값들도 들어갈 수 있다.

```swift
enum Color {
    case red
    case blue
    case green
}

var selectedColor: Color = .red

print(selectedColor) // .red
print(selectedColor.rawValue) // 0

```

# 9. switch - case의 패턴으로 나눠주는 Switch

switch도 일종의 조건문이라고 할 수 있다.

해당 값이 ~ 인경우를 정의하는 방법이다.

```swift
 enum Menu {
        case beef, pork, chicken
    }

 var myDinner: Menu = .pork

 switch myDinner {
    case .pork:
      print("pork")
    case .beef:
      print("beef")
    case .chicken:
      print("chicken")
  }

// pork

```

조건은 모두 쓰지않아도 에러가 나지않는다. 대신 이 경우 default를 넣어야한다.

만약 조건에 없다면 default를 넣어주면 조건을 명시하지않은 나머지 조건에 해당한다.

```swift
 enum Menu {
        case beef, pork, chicken
    }

 var myDinner: Menu = .beef

 switch myDinner {
    case .pork:
      print("pork")
    case .chicken:
      print("pork")
    default:
      print("다른거")
  }

// 다른거
```

위에서 나온 enum과 switch를 같이 사용할 때도 좋다.

```swift
enum Device {
    case iPhone
    case iPad
    case iMac
    case appleWatch
    
    func deviceType() -> String {
        switch self {
        case .iPhone:
            return "스마트폰"
        case .iPad:
            return "태블릿"
        case .iMac:
            return "데스크톱 컴퓨터"
        case .appleWatch:
            return "스마트워치"
        }
    }
}

let myDevice: Device = .iPhone
let deviceTypeName = myDevice.deviceType()
print(deviceTypeName) // 스마트폰
```
