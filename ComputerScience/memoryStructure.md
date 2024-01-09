# iOS에서 메모리구조 : Code / Data / Heap / Stack



프로그램이 실행되면, 

운영체제(OS)는 메모리(RAM)에 이 프로그램을 위한 공간을 할당한다.  

이 공간은 아래 그림과 같이 4가지로 나뉘어있다.  

<img width="300" alt="스크린샷 2024-01-08 오후 12 42 37" src="https://github.com/isGeekCode/TIL/assets/76529148/7d4b0af6-bd31-4043-a876-650b05c569c7">

<br><br>

이렇게 코드영역, 데이터영역, 힙 영역, 데이터 영역으로 이루어져있다. 

## 메모리구조의 구성

### Code Area : Code(Text) 영역

- 소스코드가 기계어 형태로 저장된다.  
- 컴파일시점에 결정되며, 중간에 코드가 변경되지않도록 Read-Only형태로 저장된다. 

프로그램을 실행하면, 작성한 모든 코드가 코드영역에 올라가는 것이다.  
컴파일을 하는 동안에 이 내용이 결정이 되고, 중간에 코드가 변경되지않도록 Read-Only 형태로 저장이 된다.  

기계어란, 컴퓨터가 읽을 수 있는 가장 로우 레벨의 언어로 0,1로만 이루어진 언어다.  
우리가 코드로 선언한 모든 명령들이 기계어로 변환되어 저장이 된다.  

아래 예시를 보자.  

```swift

func main() {
    print("hello, world")
    var num1: Int = 3
    var num2: Int = 1
    var num3: Int
    
    num3 = addTwoNum(a: num1, b: num2)
    print(num3)
}

func addTwoNum(a: Int, b: Int) -> Int {
    let c = a + b
    return c
}
```

이런 프로그램이 있다고 가정해보자.  

이런 명령이 기계어로 코드영역에 쌓일 것이다.

- main
    - hello, world라는 문자열을 print
    - var num1을 3으로 할당
    - var num2를 1로 할당
    - var num: Int
    - addTwoNum 실행
    - num3에 저장
    - print 실행
- addTwoNumber
    - 임시공간 생성
    - let a에 num1 저장
    - let b에 num2 저장
    - let c: Int 생성
    - a 와 b를 더하기
    - 임시값을 c에 저장
    - c를 리턴
    
위에서 숨겨진 영역의 명령들이 있을 수 있겠지만, 대략 이런 명령들이 기계어로 번역된 상태로 코드영역에 저장된다.  

<br><br>

### Data Area : 데이터 영역

- 전역변수, static 변수가 저장된다.
- 프로그램 시작과 동시에 할당, 종료시점이 되어야 메모리 해제된다.
- 실행 중 변수값이 변경될 수 있어 Read-Write로 지정된다.  

프로그램을 시작할때, 정해지는 내용이 또 존재한다.  

전역 변수 혹은 정적 변수가 있는 경우, 이들은 데이터 영역에 저장이 된다.  
그래서 프로그램(앱)이 시작될 때 초기화되어, 종료될 때까지 메모리에 남아있게 된다.   
 
즉,  메모리에 계속 남아 프로그램의 어느 곳에서나 접근할 수 있다.  

```swift

// Global variable 전역 변수 (Data Area)
// 프로그램 전체 실행 동안 접근 가능하며 어디서든 변경하거나 참조 가능
var globalNumber: Int = 10

class Constants {
    // static constant 정적상수 (Data Area)
    // 프로그램 전체 실행 동안 메모리에 상주하며 모든 인스턴스/함수에서 공유.
    static let pi = 3.14159
}
```

위에 예시를 보자.  

- 전역변수
    - 메서드 바깥에 존재하는 globalNumber 는 데이터 영역에 저장된다.  
    - 프로그램 전체 실행 동안 접근이 가능하다.  
- 정적상수
    - 클래스 내부에 있지만 static으로 저장하는 경우, 프로그램시작시 전체 실행동안 메모리에 상주한다. 
    
    
    
<br><br>

### Heap Area : 힙 영역
- 개발자가 할당/해제하는 메모리영역
    - malloc / calloc으로 힙에 메모리를 할당할수 있고, 동적할당이라고 한다.  
    - 사용 후에는 반드시 메모리해젤르 해줘야하며, 그렇지않으면 Memory Leak이 발생한다.  
- 유일하게 런타임시에 결정이 되기 때문에 데이터의 크기가 확실하지 않을 때, 사용한다.  
- 클래스 인스턴스나 클로저 같은 참조 타입의 값들은 힙에 자동할당된다.  

그런데 iOS를 사용하면서는 Swift에서 클래스를 생성하고 난 후, 따로 메모리 해제를 하지않는다.  

왜냐하면 Swift에서는 ARC를 통해 Heap에 할당된 메모리가 더이상 사용되지않으면 자동으로 해제하기 때문이다.  

원래 Objective-c를 사용하던 시절에는 free, release같은걸로 지정을 해줬어야했다.  

     
이 Heap의 장단점은 아래와 같다. 

- 장점
    - 메모리 크기에 대한 제한이 없다. (너무 큰 경우를 제외하고는,...)
    - 본질적인 범위가 전역이기 때문에, 프로그램의 모든 함수에서 액세스가 가능하다.  
- 단점
    - 할당작업, 해제 작업으로 인한 속도 저하
    - 힙 손상(이중 해제, 해제 후 사용 등) 작업으로 인한 속도 저하
    - 힙 경합(두 개 이상 쓰레드가 동시에 접근하려 할 때 Lock이 걸림)으로 인한 속도 저하
    - 메모리를 직접 관리해야 함(해제해주지 않을 시 메모리 누수 발생)

<br><br>

### Stack Area : 스택 영역
- 함수 호출시 함수의 지역변수, 매개변수, 리턴 값 등등이 저장된다.
- 함수가 종료되면 저장된 메모리도 해제된다.  
- 컴파일 타임에 결정되는 거라 무한히 할당할 수 없다.  

스택은 프로그램이 자동으로 사용하는 임시 메모리 영역이다.  

```swift
func addTwoNum(a: Int, b: Int) -> Int {
    let c = a + b
    return c
}
```

우리가 함수를 호출하면,  
 
OS에서는 내부적으로 함수안에 선언된 파라미터, 지역변수 등을 스택에 할당한다.   

그리고 addTwoNum 메서드가 종료되는 시점에 스택에 저장된 메모리는 알아서 반환된다.  

또한 Stack구조 그대로 LIFO 형식이기 떄문에 CPU에 의해 빠르게 관리된다.  

이 Stack의 장단점은 아래와 같다. 

- 장점
    - CPU가 스택 메모리를 효율적으로 구성하기에 속도가 매우 빠르다
    - 메모리를 직접 해제하지 않아도된다.  
- 단점
    - 메모리 크기에 대한 제한이 있다.  
    - 지역 변수만 액세스가 가능하다.  
    
<br><br>

## Data / Heap / Stack 영역에 할당되는 경우 살펴보기


```swift
class Constants {
    // Static constant 정적상수 (Data Area)
    // 프로그램 전체 실행 동안 메모리에 상주하며 모든 인스턴스/함수에서 공유.
    static let pi = 3.14159
}

class Circle {
    // 객체의 생명주기가 길고 크기가 실행 시 결정되므로 힙에 저장
    var radius: Double
    
    init(radius: Double) {
        self.radius = radius
    }
    
    func area() -> Double {
        // 정적 상수 pi를 사용하여 계산
        return Constants.pi * radius * radius
    }
    
    func circumference() -> Double {
        // 정적 상수 pi를 사용하여 계산
        return 2 * Constants.pi * radius
    }
    
    
}


// Global variable 전역 변수 (Data Area)
// 프로그램 전체 실행 동안 접근 가능하며 어디서든 변경하거나 참조 가능
var globalNumber: Int = 10


class NumberClass {
    // 인스턴스 변수 (힙 영역에 저장)
    var number: Int
    
    init(number: Int) {
        self.number = number
    }
    
    func addGlobalNumber() -> Int {
        // 전역 변수 globalNumber를 인스턴스 변수 number에 더하여 반환
        return number + globalNumber
    }
}

```

<br><br>

ViewController 또한 마찬가지이다.  

```swift
// ViewController 인스턴스 (힙 영역에 저장)
// ViewController는 클래스의 인스턴스이며, 동적으로 메모리가 할된다.
// 또한 생명 주기가 길고 앱 실행 동안 지속적으로 사용될 수 있으므로 힙에 저장된다.
class ViewController: UIViewController {

    // data영역에 저장된다. 이를 갖고있는 ViewController 는 컴파일 시점에 정의되지만
    // 실제로 생성되는 시점은 클래스가 사용되는 시점이다.  
    static let num2 = 3
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Circle 인스턴스 생성 (힙 영역에 저장)
        let smallCircle = Circle(radius: 5)
        
        // 메서드 호출 - 실행을 위해 스택 영역을 사용.
        let area = smallCircle.area()
        let circumference = calculateCircumference(circle: smallCircle)
        
        print("Area of the circle is \(area)")
        print("Circumference of the circle is \(circumference)")
        
        
        // 로컬 변수 (스택 영역에 저장)
        // 함수 실행 동안만 존재하며, 함수가 끝나면 스택에서 제거된다.
        let localNumber: Int = 5

        // NumberClass 인스턴스 생성 (힙 영역에 저장)
        let numberInstance = NumberClass(number: localNumber)
        
        // 메서드 호출 - 실행을 위해 스택 영역을 사용.
        let result = numberInstance.addGlobalNumber()

        print("Result is \(result)")
    }
    
    func calculateCircumference(circle: Circle) -> Double {
        // Circle 클래스의 메서드를 호출합니다.
        // 실행을 위해 스택 영역을 사용.
        return circle.circumference()
    }

}
```

<br><br>


## 힙과 스택의 메모리관계

위에서 Heap과 Stack을 나누어서 설명했지만,  

힙과 스택은 같은 메모리 영역을 공유한다.  

<img width="400" alt="스크린샷 2024-01-08 오후 12 42 44" src="https://github.com/isGeekCode/TIL/assets/76529148/4bf07f5d-a2ab-4df6-808e-3e825e393f2f">

위 그림처럼,  Heap 영역은 낮은 메모리 주소부터 할당받고,  
Stack 영역은 높은 메모리 주소부터 할당 받는다.  

힙이 자신의 영역 외로 확장하려하면, Heap over flow가 발생하고,  
스택이  자신의 영역 외로 확장하려하면, Stack over flow가 발생한다. 


<br><br>

### Stack이 과해지는 경우


```swift
class ViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
                
        // 재귀 호출로 스택오버플로우 발생
        causeStackOverflow(0)
    }

    // 깊은 재귀 호출을 일으키는 함수
    func causeStackOverflow(_ number: Int) {
        // 스택 영역에 함수의 데이터가 계속 쌓이게 되어, 스택 오버플로우가 발생할 수 있다.
        print(number)
        causeStackOverflow(number + 1)
    }
}
```

스택 오버플로우는 스택 영역의 메모리가 넘쳐서 다른 메모리 영역을 침범하는 현상을 말한다.  
스택 오버플로우는 주로 두 가지 상황에서 발생한다.  

- 깊은 재귀 호출
    - 함수가 자신을 계속해서 호출하고, 종료 조건이 충족되지 않아 호출 스택이 너무 깊어지는 경우.
- 과도한 스택 할당
    - 한 함수에서 너무 많은 메모리를 로컬 변수로 할당하여 스택의 한계를 초과하는 경우.

<br><br>

### Heap이 과해지는 경우
반대로 Heap 오버 플로우도 일어날 수 있다

이건 프로그램이 힙 메모리 영역에서 할당할 수 있는 메모리 양을 초과하여 더 이상 새로운 객체나 데이터를 할당할 수 없을 때 발생한다. 

- 과도한 메모리 할당
    - 프로그램이 실행 중에 과도하게 많은 데이터를 힙에 할당하려고 할 때, 사용 가능한 힙 메모리가 고갈되어 힙 오버플로우가 발생할 수 있다
    - 예를 들어, 매우 큰 배열이나 리스트를 반복적으로 생성하고, 빨리 해제하지 않는 경우가 이에 해당할 수 있다
- 메모리 누수
    - 할당된 메모리 영역이 더 이상 필요하지 않음에도 불구하고 적절히 해제되지 않아 시스템의 메모리를 점차적으로 소모하는 현상을 말한다
    - 객체에 대한 참조가 여전히 남아 있어 가비지 컬렉터나 ARC(Automatic Reference Counting)가 해당 메모리를 회수하지 못할 때 발생한다
    - 메모리 누수가 계속되면 결국 사용 가능한 힙 메모리가 고갈되어 오버플로우로 이어질 수 있다

- 무한 할당 루프
    - 프로그램에 무한 루프가 있고, 이 루프 내에서 지속적으로 새로운 메모리를 할당하는 경우에도 힙 오버플로우가 발생할 수 있다.
    - 프로그램이 정상적으로 종료되지 않고 계속해서 메모리를 요구하다가 결국 사용 가능한 메모리를 모두 소모하게 된다

<br><br>

```swift
// 데이터영역에 과도한 부담을 주는 경우에도 오류가 발생할 수 있다.
class LargeDataSet {
    static let largeArray = [Int](repeating: 0, count: 1_000_000)
}

class AnotherLargeDataSet {
    static let anotherLargeArray = [String](repeating: "Some large string", count: 100_000)
    // 추가적인 대량의 더미 데이터...
}


// 이런식으로 과도하게 힙영역의 메모리를 고갈시키면 안된다.
class BigData {
    // 매우 큰 배열을 생성. 각 요소는 1MB의 데이터를 차지한다면.
    var largeArray = [UInt8](repeating: 0, count: 1_000_000)
}

class TESTViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        
        var bigDataArray: [BigData] = []
        
        while true {
            // 무한 루프 내에서 BigData 인스턴스를 계속 생성하고 배열에 추가
            // 각 인스턴스는 힙에 저장되며, 이는 메모리 사용량을 계속 증가.
            let bigData = BigData()
            bigDataArray.append(bigData)
        }
    }
}

```

<br><br>

## History
- 초안 작성
