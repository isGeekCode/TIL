# Architecture - IOS MVC의 한계

정말 위와 같이 역할이 명확히 구분된다면 좋겠지만 실상은 그렇지 못하다.

### 1. **Apple의 MVC는 View와 Controller가 너무 밀접하다.**

Apple의 MVC에서는 `ViewController`라는 이름에서도 볼 수 있듯이 View와 Controller가 굉장히 밀접하게 연결되어있다. ViewController는 Controller의 역할뿐만 아니라 **View의 life cycle**에도 관여하고 있는 것이 현실이다.

이때문에 Model은 분리하여 테스트를 할 수 있어도 View와 Controller는 서로 강하게 연결되어있어 테스트가 어렵다.

### 2. **뷰, 모델에 맞지 않는 모든 비즈니스 로직들은 Controller에 들어가게 된다.**

모델이나 뷰에 넣기 애매한 코드들은 모두 Controller에 들어가게 되는데 이렇다보니 Controller가 비대해질 수 있다.

이를테면 서버에서 받아온 데이터를 가공(포매팅)해서 뷰에 넘겨주는 로직이나 사용자로부터 들어온 interaction을 처리하여 모델/뷰에 넘기는 로직 등, 화면에 보이는 것과 데이터 이외에는 모두 ViewController가 처리하게 된다.

- **[Clint Jang](https://medium.com/@jang.wangsu/%EB%94%94%EC%9E%90%EC%9D%B8%ED%8C%A8%ED%84%B4-mvc-%ED%8C%A8%ED%84%B4%EC%9D%B4%EB%9E%80-1d74fac6e256)블로그에서 설명하는 MVC의 한계**

  1. MVC에서 View는 Controller에 연결되어 화면을 구성하는 단위요소이므로 다수의 View들을 가질 수 있다. 그리고 Model은 Controller를 통해서 View와 연결되어지지만, 이렇게 Controller를 통해서 하나의 View에 연결될 수 있는 Model도 여러개가 될 수 있다.

     → 뷰와 모델이 서로 의존성을 띄게 된다.

  2. 즉, 화면에 복잡한 화면과 데이터의 구성 필요한 구성이라면, Controller에 다수의 Model과 View가 복잡하게 연결되어 있는 상황이 생길 수 있다.
     ![스크린샷 2022-03-22 오전 8.40.07.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9d105bf0-5df5-4635-b2e5-d18c8e71d35a/스크린샷_2022-03-22_오전_8.40.07.png)
     > View와 Model이 많아지는 상황에서 발생할 수 있는 문제는 2번 맥락에서도 이해해볼 수 있다.
     >
     > `Controller`는 `View`에서 들어오는 사용자 입력을 처리하고, `Model`의 데이터 업데이트를 알아차린 뒤 이를 `View`에 넘기는 작업들도 수행한다고 했었다. 당연히 `Controller`에 연결된 `View`와 `Model`들이 많아지면 해당 작업들에 대한 코드들이 늘어나는 것이 당연하고 `Controller`가 커지는 것은 어찌보면 피할 수 없다.

💡 위와 같은 이유들때문에 MVC를 Massive View Controller라고 말하곤 한다. 하지만 MVC가 항상 그런 것은 아니다. **MVC도 충분히 클린하게 코드를 짤 수 있다**고 한다.

# Questions

1. _"MVC에서 View는 다른 컴포넌트를 알면 안되는데, Apple의 MVC에서는 이벤트 처리를 위해 View가 Controller를 아는 형태로 구현되지 않나요??"_

   → 날카로운 질문이다. 하지만 Apple은 이 문제를 `Delegate 디자인 패턴`이라고 하는 아주 우아한(?) 방식으로 해결하였다. `Protocol`을 선언하고`View`는 해당 `Protocol`만을 아는 형태로 만든 뒤, `Controller`로 처리할 책임을 위임하였다. 즉, **의존성 역전 원칙(DIP)**을 이용하여 `View`와 `Controller`간 의존성을 떨어뜨렸다.

   → (`View`는 `Controller`를 직접적으로 알지 못하고 오직 `Protocol`만을 알고 있다)

2. "Controller 또한 View를 알고 있는 형태로 만들어지는데, View도 Controller를 알고 있다면 reference cycle이 생기지 않나요?"

   → 결론부터 말하자면 발생하지 않는다. `UIKit`내에 있는 여러 `View` 요소들이 `Controller`를 참조하는 방식은`weak reference`이다.

   **(단, 직접 delegate pattern을 구현하여 적용하는 경우, cycle이 생기지 않도록 우리가 만들어줘야 한다)**

3. "Delegate Pattern이 아닌 Target-Action으로 View가 Controller를 알도록 하는 것은요? reference cycle 문제가 없나요?"→ [UIControl - addTarget(\_:action:for:)](https://developer.apple.com/documentation/uikit/uicontrol/1618259-addtarget) 문서에 이 질문에 대한 해답이 나와있다.

   ![https://media.vlpt.us/images/ictechgy/post/8a0194b4-5606-4001-88ae-aebe72edd0d2/image.png](https://media.vlpt.us/images/ictechgy/post/8a0194b4-5606-4001-88ae-aebe72edd0d2/image.png)

4. "Model도 다른 컴포넌트를 몰라야 한다고 하는데, 그럼 Controller는 Model의 변화를 어떻게 감지하나요??"

   → 여기에는 `KVO`, `NotificationCenter` 같은 `Observer Pattern`이나, `Delegate Pattern`등 여러가지 방법이 있겠지만 나는 **클로저를 이용한** `completionHandler`를 주로 쓴다.(callback) 특별히 뭔가를 별도로 구현해 줄 필요가 없다는 점에서 굉장히 편리하다. 👍 *(물론 capture에 따른 reference cycle은 별도로 고려해주어야 한다!)*

## 다른 패턴에서도 같은 문제가 발생할 수 있다.

위에서 말한 MVC의 이러한 문제들 때문에 다른 패턴을 쓰는 것만이 유일한 해결책인 것처럼 보일 수 있다.하지만 나는 그렇게 생각하지 않는다. 다른 패턴을 쓴다고 하더라도 비슷한 문제는 발생할 수 있다.

- 이를테면 MVVM을 쓴다고 하더라도 ViewModel이 비대해질 수 있다.
- VIPER패턴이 무엇인지는 아직 잘 모르지만 해당 패턴을 쓴다고 하더라도 Interactor가 비대해지는 문제가 생길 수 있다고 한다.

## 최선 → **비대해지는 객체를 적절히 분리**

MVC 패턴을 적용했을 때 `ViewController`가 너무 비대해진다면 해당 `ViewController`를 **단일책임원칙(SRP)**에 따라 여러개의 `ViewController`로 나누어보자!

