# Objc - c언어와 objective-c의 차이, 발전

- 참고 사이트: [http://www.tcpschool.com/c/c_intro_basic](http://www.tcpschool.com/c/c_intro_basic)

# C언어란?

C언어는 현재 사용하고 있는 거의 모든 컴퓨터 시스템에서 사용할 수 있는 프로그래밍 언어입니다.

프로그래밍 언어란 컴퓨터의 시스템을 구동시키는 소프트웨어를 작성하기 위한 언어를 의미합니다.

이러한 프로그래밍 언어는 크게 저급 언어(low-level language)와 고급 언어(high-level language)로 나뉩니다.

저급 언어와 고급 언어는 좋고 나쁜 언어가 아니라, 기계가 이해하기 쉬운가(저급 언어), 사람이 이해하기 쉬운가(고급 언어)를 상대 적으로 나눈 개념이라고 할 수 있습니다.

저급 언어는 컴퓨터가 이해하기 쉽게 작성된 프로그래밍 언어로, 대표적인 언어로는 기계어(machine language)와 어셈블리어(assembly language) 등이 있습니다.

이 언어는 실행 속도가 매우 빠르지만, 사람이 배우기에는 매우 어려워 프로그램의 유지보수가 힘듭니다.

고급 언어는 컴퓨터보다는 사람이 알기 쉽도록 작성된 프로그래밍 언어입니다.

고급 언어는 컴파일러나 인터프리터에 의해 기계가 이해 할 수 있는 언어로 번역되어 실행 됩니다.

그래서 저급 언어보다는 상대적으로 실행 속도가 느립니다. 대표적으로 자바, 파이썬 등이 있습니다.

이 언어는 저급 언어에 비해 가독성이 높고 다루기가 쉽습니다.

C언어는 저급 언어와 고급 언어의 특징을 모두 가지고 있는 절차 지향 프로그래밍 언어(procedure-oriented programming language)입니다.

## C언어의 특징

### C언어가 가지는 장점

- C언어로 작성된 프로그램은 다양한 하드웨어로의 이식성이 좋습니다.
- C언어는 절차 지향 프로그래밍 언어로, 코드가 복잡하지 않아 상대적으로 유지보수가 쉽습니다.
- C언어는 저급 언어의 특징을 가지고 있으므로, 어셈블리어 수준으로 하드웨어를 제어할 수 있습니다.
- C언어는 코드가 간결하여, 완성된 프로그램의 크기가 작고 실행 속도가 빠릅니다.

### C언어가 가지는 단점

- C언어는 저급 언어의 특징을 가지고 있으므로, 자바와 같은 다른 고급 언어보다 배우기가 쉽지 않습니다.
- C언어는 다른 언어와는 달리 시스템 자원을 직접 제어할 수 있으므로, 프로그래밍하는데 세심한 주의를 기울여야 합니다

### C 프로그래밍

---

### 프로그래밍(programming)

프로그래밍이란 목적에 맞는 알고리즘으로부터 프로그래밍 언어를 사용하여 구체적인 프로그램을 작성하는 과정을 의미합니다.

이렇게 작성된 프로그램은 먼저 실행 파일(executable file)로 변환되어야 실행할 수 있습니다.

C언어에서 실행 파일을 생성하는 순서는 다음 그림과 같습니다.

![img_c_programming](https://user-images.githubusercontent.com/76529148/164407431-65015bf4-51aa-484e-a6a2-2a29df95f606.png)

1. 소스 파일(source file)의 작성

2. 선행처리기(preprocessor)에 의한 선행처리

3. 컴파일러(compiler)에 의한 컴파일

4. 링커(linker)에 의한 링크

5. 실행 파일(executable file)의 생성

---

### 소스 파일(source file)의 작성

프로그래밍에서 가장 먼저 해야 할 작업은 바로 프로그램을 작성하는 것입니다.

C언어를 사용하여 문법에 맞게 논리적으로 작성된 프로그램을 원시 파일 또는 소스 파일이라고 합니다.

C언어를 통해 작성된 소스 파일의 확장자는 .c 가 됩니다.

---

### 선행처리기(preprocessor)에 의한 선행처리

선행처리(preprocess)란 소스 파일 중에서도 선행처리 문자(#)로 시작하는 선행처리 지시문의 처리 작업을 의미합니다.

이러한 선행처리 작업은 선행처리기(preprocessor)가 수행합니다.

선행처리기는 코드를 생성하는 것이 아닌, 컴파일하기 전 컴파일러가 작업하기 좋도록 소스를 재구성해주는 역할만을 합니다.

선행처리에 대한 더 자세한 사항은 C언어 선행처리기 수업에서 확인할 수 있습니다.

[C언어 선행처리기 수업 확인 =>](http://www.tcpschool.com/c/c_prepro_preprocessor)

---

### 컴파일러(compiler)에 의한 컴파일

컴퓨터는 0과 1로 이루어진 이진수로 작성된 기계어만을 이해할 수 있습니다.

소스 파일은 개발자에 의해 C언어로 작성되므로, 컴퓨터는 그것을 바로 이해할 수 없습니다.

따라서 소스 파일을 컴퓨터가 알아볼 수 있는 기계어로 변환시켜야 하는데, 그 작업을 컴파일(compile)이라고 합니다.

컴파일은 컴파일러에 의해 수행되며, 컴파일이 끝나 기계어로 변환된 파일을 오브젝트 파일(object file)이라고 합니다.

이러한 오브젝트 파일의 확장자는 .o 나 .obj 가 됩니다.

---

### 링커(linker)에 의한 링크

컴파일러에 의해 생성된 오브젝트 파일은 운영체제와의 인터페이스를 담당하는 시동 코드(start-up code)를 가지고 있지 않습니다.

또한, 대부분의 C 프로그램에서 사용하는 C 표준 라이브러리 파일도 포함되어 있지 않습니다.

이때 하나 이상의 오브젝트 파일과 라이브러리 파일, 시동 코드 등을 합쳐 하나의 파일로 만드는 작업을 링크(link)라고 합니다.

링크는 링커(linker)에 의해 수행되며, 링크가 끝나면 하나의 새로운 실행 파일이나 라이브러리 파일이 생성됩니다.

이처럼 여러 개의 소스 파일을 작성하여 최종적으로 링크를 통해 하나의 실행 파일로 만드는 것을 분할 컴파일이라고 합니다.

분할 컴파일에 대한 더 자세한 사항은 C언어 분할 컴파일 수업에서 확인할 수 있습니다.

[C언어 분할 컴파일 수업 확인 =>](http://www.tcpschool.com/c/c_complie_module)

---

### 실행 파일(executable file)의 생성

소스 파일은 선행처리기, 컴파일러 그리고 링커에 의해 위와 같은 과정을 거쳐 실행 파일로 변환됩니다.

최근 사용되는 개발 툴은 대부분 위에서 소개한 선행처리기, 컴파일러, 링커를 모두 내장하고 있으므로, 소스 파일에서 한 번에 실행 파일을 생성해 줍니다.

이렇게 생성된 실행 파일의 확장자는 .exe 가 됩니다.

# objc를 공부해야하는 이유

## 장점

- 회사코드 리팩토링이 가능
- 기능검색시 굉장히 많은 비중으로 objc가 나온다
- ios 언어의 왕이 될 수 있다.

## 단점

- 어렵고 지저분
- 처음볼 때 난해하다

깊게 공부하지는 않아도 이해할 수 있을 정도 수준으로 공부하기

# 프로젝트 생성

## 1. 생성시 language 선택 : Objective -c

## 2. 프로젝트 파일의 생김새

스위프트랑 다르게 헤더 파일이 존재한다. (.h)

C언어를 확장한 언어이다.

때문에 헤더파일이 존재하고, 이 헤더파일에는 외부에서 사용할 메서드나 변수(상수)를 선언해야 한다.

참고정리

[C 언어에 대하여](https://www.notion.so/C-5a1f89e3dcc04f61864bc216778bffa0)

# ViewControlller.h 살펴보기

헤더파일 내용

```objectivec
#import <UIKit/UIKit.h>

@interface ViewController : UIViewController


@end
```

### # import

**외부 라이브러리,프레임워크** 뿐 아니라 **프로젝트 내에 선언된 클래스** 등을 불러올 때 사용

```objectivec
#import <UIKit/UIKit.h>

```

C언어에서는 #include Swift에서는 import에 해당

C언어와 다른 점은 같은 헤더파일이 여러번 불리는 것들 알아서 방지해준다.

swift의 경우 프로젝트 전체가 namespace 범위로 지정되어 있어 일일히 객체를 import하지 않아도 사용가능

하지만 외부 라이브러리나 프레임워크 (UIKitm Foundation 등)은 Swift에서도 당연히 import해야한다.

### @interface, @end

선언부를 나타낸다.

```objectivec
@interface ViewController : UIViewController

@end
```

보통 헤더파일의 존재이유는 어떤 것을 선언하기 위해서 사용한다.

- 이 `@interface` 는 클래스 선언이 시작된다 라는 부분이다. 선언부
  → 어떤 클래스를 상속받고, 어떤 변수와 메서드를 쓸건지 여기서 선언
- `@interface` 로 시작되면 꼭 끝에 `@end`가 있어야한다.

## 📌 변수선언방법

변수가 두군데에 쓰여있다.

```objectivec
@interface ViewController : UIViewController {
	 NSString *name;
}

@property NSString *alias;

@end
```

### 1. 인스턴스 변수

@interface의 괄호 안에 선언되는 변수

이 전역 변수의 기본 접근 지시자는 **protected** 이다.

따라서 **자기 자신, 혹은 상속받은 자식 클래스에서만 접근** **가능**하다.

### **외부 클래스에서도 접근 가능하게 해주려면 (잘 사용X)**

### 1.1 아래와 같이 **@public**으로 접근 지시자를 바꿔줄 수 있다.

```objectivec
@interface ViewController : UIViewController {
	 @public NSString *name;
}

@property NSString *alias;

@end
```

### 1.2 getter, setter를 직접 만들어준다.

```objectivec
- (void)setName: (NSString *)name {
		name= name;
}
- (NSString *)name {
		return name;
}

```

### 프로퍼티를 이용하여 접근

interface field 내에 @property 라는 접근 지시자를 통해 선언되는 변수는 모두  **프로퍼티**

```objectivec
#import <UIKit/UIKit.h>

@interface ViewController : UIViewController {
		NSString *name;
}

@property NSString *alias;  //프로퍼티
@end
```

### 프로퍼티의 특징

- getter, setter를 자동으로 생성 → 별도의 작업없이 외부에서 접근 가능

<aside>
🔥 헤더파일에서는 변수 초기화를 못한다.  **→ Xcode 자체에서 에러발생**

</aside>

참고 [https://babbab2.tistory.com/74](https://babbab2.tistory.com/74)

## 📌 메서드 선언방법

메서드는 별다른 것 없이 프로퍼티 선언부에 메서드 이름을 입력한다.

```objectivec
#import <UIKit/UIKit.h>

@interface ViewController : UIViewController {
		NSString *name;
}
- (void)name;		//메서드
@end
```

### 3. ViewController, UIViewController

```objectivec
           //선언할 클래스 명   // 상속받는 클래스 명
@interface ViewController : UIViewController {

@end
```

### 4. Protocol

swift와 달리 상속 외 프로토콜 채택시에는 <> 괄호(angle bracket)를 이용해서 열거해주어야한다.

```objectivec
@interface ViewController : UIViewController <UITableViewDelegate, UITableViewDataSource>
@end
```

# .m 파일 살펴보기

```objectivec
#import "ViewController.h"

@interface ViewController : UIViewController

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
}

@end
```

### # import

.m에서는 .h 헤더파일이 있다면 자신의 헤더파일을 무조건 import하고 있어야한다.

또한 헤더파일에서 import한 것은 .m 파일에서 import할 필요가 없다.

### @ interface, @end

```objectivec
@interface ViewController ()

@end
```

헤더파일의 @interface와는 달리

여기 등장한 @interface는 익명 카테고리로 Extension을 의미한다.

따라서 프로퍼티나 익스턴스 변수를 Private으로 선언하고 싶을 때 여기에 선언한다.

참고: [https://babbab2.tistory.com/73](https://babbab2.tistory.com/73)

### @ implementation, @end

```objectivec
@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
}

@end
```

interface와 마찬가지로 implementation이 끝나는 곳에도 @end가 있어야한다.

### 선언부, 구현부 정리

```objectivec

@interface ViewController ()

			// 선언부 : 외부에서 사용할 메서드 이름, 인스턴스 변수, property 선언

@end

@implementation

			// 구현부 : 메서드 구현

@end
```

### 메서드구현

```objectivec
@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
}

@end
```

### @synthesize

구현부내에 @신thㅓ사이즈 라는 게 가끔 보인다.

먼저 프로퍼티를 알아야하는데 프로퍼티는 전부 아래와같이 선언부 (interface field)에 선언한다고 했다.

```objectivec

@interface ViewController ()

			// 선언부 : 외부에서 사용할 메서드 이름, 인스턴스 변수, property 선언
			@property NSString *name; // 프로퍼티

@end

@implementation

			// 구현부 : 메서드 구현
			// name = @"GeekCode"; // 에러발생
@end
```

만약 이 프로퍼티를 구현부의 메서드 내에 사용하면 에러가 발생한다.

name이 정의되어있지않으니 \_name으로 대체하라는 내용이다.

<aside>
🔥 **Use of undeclared identifier ‘name’; did you mean ‘_name’?
Replace ‘name’ with ‘_name’**

</aside>

\_name으로 대체하지않아도 self를 통해서 접근이 가능하다.

```objectivec

@interface ViewController ()

			// 선언부 : 외부에서 사용할 메서드 이름, 인스턴스 변수, property 선언
			@property NSString *name; // 프로퍼티

@end

@implementation

			// 구현부 : 메서드 구현
			self.name = @"GeekCode";
@end

```

### 프로퍼티의 특성

- 프로퍼티는 선언부에 선언한 이름을 구현부에서 그대로 접근할 수 없다.

아래와 같이 사용한다.

```objectivec

@interface ViewController ()

			// 선언부 : 외부에서 사용할 메서드 이름, 인스턴스 변수, property 선언
			@property NSString *name; // 프로퍼티

@end

@implementation

			// 구현부 : 메서드 구현
			// self.name = @"GeekCode";
			// _name = @"GeekCode";
@end

```

하지만 \_ 와일드카드 패턴을 없애고 싶을 때, 사용하는 것이 synthesize이다.

→ 선언부에 선언된 이름 그대로 접근이 가능하게 해준다.

- **이 경우 self는 사용할 수 있지만 더이상 와일드카드패턴으로는 접근 할 수 없다.**

```objectivec

@interface ViewController ()

			// 선언부 : 외부에서 사용할 메서드 이름, 인스턴스 변수, property 선언
			@property NSString *name; // 프로퍼티

@end

@implementation
			// 구현부 : 메서드 구현
@synthesize name;

			name = @"GeekCode";
@end

```

이 내용은 프로퍼티에 한정하고, 멤버변수는 상관 없다.

참고: [https://babbab2.tistory.com/74](https://babbab2.tistory.com/74)
