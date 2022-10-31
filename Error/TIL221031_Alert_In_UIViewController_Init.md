Presenting view controllers on detached view controllers is discouraged.

## 📌 상황

새로 등장하는 ViewController에서 얼럿생성시 발생하는 에러

가끔씩 UIAlertController를 생성하고 그걸 새로운 UIViewController에서 띄울 때, 아래와 같은 경고 로그를 확인 하곤한다.

`Presenting view controllers on detached view controllers is discouraged.`

![스크린샷 2022-10-31 오후 1 56 46](https://user-images.githubusercontent.com/76529148/198936669-5f235f11-e0f5-4ed4-898d-453aa8027f8d.png)

## 📌 발생이유

이런 경고 로그가 생기는 이유는 생각보다 간단한 이유때문이다.

UIAlert이 생겨야할 장소인 UIViewController가 모두 생성되어야 안전하게 Alert이 생성될 수 있기 때문이다.

Apple에서 자체적으로 UIView의 생성이 지연될때, Alert또한 지연시켜 치명적인 오류를 예방하지만, 프로그래밍을 할때 얼럿을 생성하는 시점이 View가 생성된 후가 되어야한다.

## 📌 해결방법

즉, ViewDidAppear() 이전에 UIAlertController를 사용하게 되면 에러가 발생한다.

→ VIewDidAppear() 로 이동시키면 해결된다.

참고링크 : [StackOverFlow](https://stackoverflow.com/questions/27386154/uialertcontroller-detached-view-controller)
