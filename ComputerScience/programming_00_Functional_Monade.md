# Functional Programming - 모나드 이해하기

모나드를 이해하려면 크게 컨텍스트, 함수객체, 모나드에 대한 개념이 등장한다. 

먼저 Monade를 소개하기 앞서 Context라는 개념에 대해 설명하려고 한다. 


### Context
컨텍스트(Context)와 컨텐트(Content)의 관계는 다음과 같다.  
  
<img width="600" alt="0_V08xYU6Ru7K8q8kE" src="https://github.com/isGeekCode/TIL/assets/76529148/c3a9fbd7-d1f3-42ff-a6d8-e4f33dc5bda2">

<br><br>

컨텍스트는 컨텐트를 담고있는 형태로 옵셔널(Optional)을 예로 들면 Optional(2)에서 컨텍스트는 Optional, 2는 컨텐트가 된다.  

만일 옵셔널안에 값이 존재하지 않는다면 컨텍스트만 존재하는 꼴이 된다.   

### Container

우리가 흔히 사용하는 자료구조인 Array, Set, Dictionary 와 같은 자료구조들도 일종의 컨테이너라고 할 수 있다. 이들은 한 개 이상의 원소를 가질 수 있는 컨테이너들이다. 

위에서는 옵셔널도 컨텍스트의 일종이라고 했는데, 옵셔널은 그럼 컨테이너이기도 할까?  

맞다. 옵셔널도 컨테이너의 한 종류로 그 컨테이너 안에는 값이 존재할 수도 있고, 없을 수도 있다. 
> 즉, 두 가지의 경우를 담고있는 컨테이너라고 할 수 있다.


### Map

우리는 컨테이너에 매핑(Mapping)이라는 연산을 수행할 수 있다. 매핑은 일반적 의미에서 어떤 값을 다른 값에 대응시키는 과정을 총칭한다.

아래는 매핑 연산의 예시다

```
[1, 2, 3, 4] -> [2,4,6,8]

["1", "2", "3"] -> [1, 2, 3]

["Harry", "Joe", "David"] 
-> ["My name is Harry", "My name is Joe", "My name is David"]
```

이런 매핑은 내부 원소의 값의 변형에만 일어난다. 그 원소를 담고 있는 컨테이너의 변형은 일어나지 않는다.  
그말은 Array에 매핑을 한다고 Array가 Dictionary가 되는 컨테이너의 변형은 일어나지 않는 것이다. 

이렇게 값에 변형을 매핑할 수 있는 모든 것들을 Functor(함수객체)라고 한다. 그렇다면 Functor는 컨테이너와 같은 의미일까? 이에 대해서는 다양한 의견이 있다.


## Functor
Functor(함수객체)는 고차함수인 map을 적용할 수 있는 컨테이너 타입이다.

이렇게 Functor에서 매핑하는 과정을 표현해보면 아래와 같다. 

<img width="600" alt="fmap_just" src="https://github.com/isGeekCode/TIL/assets/76529148/f14a584c-7eae-43c6-a74d-2ba0fe920867">

> 여기서 중요한 점은 매핑으로 변형된 값은 다시 Functor로 감싼 후에 반환된다는 것이다. 
Swift에서 매핑의 대표 메서드가 map 함수이다. 


아래 예시를 보자
```SWIFT
var myNumber: Int? = 2

print(myNumber+3)
```
위 코드는 동작할 수가 없다. 왜냐하면 myNumber는 Optional타입 즉, Int? 타입이기 때문이다.

Int와 Int?는 다른 타입이기 때문이다.

myNumber는 상자(컨텍스트)다. 값이 있을지도, 없을지도 모르는데 거기다가 무조건 값인 3을 더할수는 없다.
그래서 이걸 꺼내는 작업이 필요하다. 그게 map이다. 

```SWIFT

var myNumber: Int? = 2

print(myNumber.map({ $0+3 }) )

//Optional(5)
```

  
map이라는게 요소 하나하나를 보면서, 값이 있나 확인하면서 있으면!! 해당 요소를 꺼낸다

해당 요소를 꺼냈다는 건? 값이라는 것이기 때문에 같은 타입이라면 +3이라는 연산이 가능해진다.

그럼 왜!!! 왜 그냥 5가 아니라 Optional(5)가 나왔냐? 

map은 이 값을 컨텍스트, 즉 상자에 넣어서 돌려주기 때문이다.


그럼 map이 어떻게 구현되어있기 때문에 이렇게 되는걸까?
한번 optional을 뜯어보면서 이해해보자.

### Optional 뜯어보기
옵셔널은 enum으로 구현되어있다. 
값이 있는경우, 값이 없는 경우로 나뉘어 있다. 

값이 있는 경우엔 some에 값을 담고, 없는 경우에는 none을 사용한다. 

옵셔널의 map 메소드는 Wrapped 타입을 파라미터로 받고 U 타입을 반환하는 함수 transform을 파라미터로 받는다. 그리고 map 메소드 자체는 U? 타입을 반환한다.

그리고 switch 문에서 self, 즉 map 메소드를 호출한 옵셔널 타입의 값을 검사하기 때문에  
map 메소드를 호출한 옵셔널 컨텍스트 안에 값이 존재한다면 
해당 값을 컨텍스트로부터 추출하여 파라미터로 받아온 transform 함수에 넘겨 값을 처리한다.

transform 메소드의 반환 결과는 U 타입이지만 옵셔널 map의 반환 타입이 U? 이므로 컴파일러가 자동으로 U?로 감싸 반환한다.

반면에 map 메소드를 호출한 옵셔널 타입의 변수에 값이 존재하지 않는다면 nil 값을 반환하는 것이다.

```SWIFT
enum Optional<T> {
    case some(Wrapped)
    case none

    func map<U>(_ transform: (Wrapped) -> U) -> Optional<U> {
        switch self {
        case .some(let value):
            return .some(transform(value))
        case .none:
            return .none
        }
    }
}

```

명심해야할 것은 위에서 언급했던 "여기서 중요한 점은 매핑으로 변형된 값은 다시 Functor로 감싼 후에 반환된다는 것이다" 라고 했던 문장이다.




## 그렇다면 Monade는 무엇일까?

모나드는 Functor(함수객체)의 일종이다. 모나드를 쉽게 설명하자면 Map 연산이 가능한 모든 것들을 우리는 모나드라고 부를 수 있다. (하아.. 뭐가 쉽게 설명이야......)

다시 정리..

- 모나드는 함수객체의 일종이라는 말
-> 이말은 `모나드에는 map을 적용 할 수 있다.`는 말이다. 

여기에 컨텍스트라는 개념을 더해보자.

> 모나드는 값이 있을 수도 있고 없을 수도 있는 컨텍스트를 가지는 함수객체 타입 

-> 모나드는 `(값이 있을수도 있고, 없을 수도 있는 컨텍스트(맥락)을 가지는)` map을 적용 할 수 있는 타입이라는 것이다.

이 두가지 조건에 부합하는 것이 옵셔널이다. 

옵셔널은 정의자체가 값이 있을수도, 없을 수도 있는 타입이고, map까지  적용할 수 있는 함수 객체였다.

그렇다면 Optional은 모나드일까? 맞다.


### 하스켈로 찾아본 functor, map

하스켈(Haskell)이라는 언어가 있다. 순수 함수형 프로그래밍 언어로, 1990년에 미국의 컴퓨터 과학자들이 개발한 고수준 프로그래밍 언어다. 

첫 단계로 알아볼 것은 functor다. functor는 하스켈에서 다음과 같이 정의된다.
```Haskell
class Functor f where  
  fmap :: (a -> b) -> f a -> f b
```

여기서 functor는 구체 타입이 아니라 타입생성자이다. Swift로 치면 Generic이라 할 수 있다.
위 구현을 보자.
- (a -> b)타입의 함수와 Functor f로 감싸진 a타입의 변수를 입력받아서 
- 다시 functor f로 감싸진 b를 반환


이걸 Swift로 변형시키면 아래와 같이 된다. 

```SWIFT
 class Functor<T> {
    func fmap<U>(_ transform: T -> U) -> Functor<U> 
}

```
이 형태는 바로 swift의 map에 해당하는 형태이다. 
즉, functor는 간단하게 생각하면 map을 적용할 수 있는 타입이다. 

functor가 값을 담을 수 있는 상자라고 생각하면, 그 상자를 풀지 않아도 map을 통해 영향을 줄수 있게된다. 이 상자는 값에 대한 추가적인 상태를 담는 그릇으로 컨텍스트라고 부른다. 




## 참고링크
- [Monad와 Swift](https://jcsoohwancho.github.io/2019-10-30-Monad%EC%99%80-Swift/)


## History
- 230808: 초안작성
