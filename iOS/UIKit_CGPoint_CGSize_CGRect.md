# CGPoint, CGSize, CGRect

**참고사이트**

개발자 소들이 블로그

[https://babbab2.tistory.com/42](https://babbab2.tistory.com/42)

---

## 0. 서론

## 1. 선행지식

📌

📌

## 2. 개념

iOS에서 View를 그리기 위해서는 위치(기준점)과 View의 크기가 필요하다.

[https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Ftu18Z%2FbtqLxuWRm3D%2FVBkP3iKHrkPeXCOE1bMUIk%2Fimg.png](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Ftu18Z%2FbtqLxuWRm3D%2FVBkP3iKHrkPeXCOE1bMUIk%2Fimg.png)

[https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbAeLQt%2FbtqLwMcpAhg%2FVhVlgRKZVaBG9aFGUGZliK%2Fimg.png](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbAeLQt%2FbtqLwMcpAhg%2FVhVlgRKZVaBG9aFGUGZliK%2Fimg.png)

- 시작점 x, y의 좌표 : View의 시작위치를 알려줌
  - x
  - y
- width. height : 시작점으로부터의 크기를 알려줌
  - width
  - height

### 1. (x, y)좌표를 설정하는 CGPoint

[https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F1iWtP%2FbtqLwMjdDFp%2FZBPHkZmcPvslkz07sZUfyk%2Fimg.png](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F1iWtP%2FbtqLwMjdDFp%2FZBPHkZmcPvslkz07sZUfyk%2Fimg.png)

CGPoint라는 구조체를 살펴보면

- CGPoint는 x, y 라는 Float 변수를 가지고 있다. → View의 위치를 나타낼 때 사용
- View 위치뿐 아니라 x, y 좌표를 나타내야할 땐 언제든 사용 가능

사용 예)

```swift
let position: CGPoint = .init(x: 50, y: 50)
```

### 2. (width, height) 사이즈를 설정하는 CGSize

[https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcIXCAs%2FbtqLC1ZM6lK%2FhDWLNP8ZcmTRyk8EAmCdTK%2Fimg.png](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcIXCAs%2FbtqLC1ZM6lK%2FhDWLNP8ZcmTRyk8EAmCdTK%2Fimg.png)

CGSize라는 구조체를 살펴보면

- width, height라는 Float변수를 가지고 있다.

사용 예)

```swift
let size: CGSize = .init(width: 100, height: 100)
```

### 2. CGSize와 CGPoint를 가지고 있는 CGRect

실제 UIView를 init할때에는 frame의 파라미터로 CGRect가 들어간다.

[https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FmNAgt%2FbtqLyKLXwJt%2FpA4Nm5tXCbcYCZfXs93J90%2Fimg.png](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FmNAgt%2FbtqLyKLXwJt%2FpA4Nm5tXCbcYCZfXs93J90%2Fimg.png)

- origin: CGPoint 타입의 변수 → x, y값을 나타냄
- size: CGSize 타입의 변수 → size를 표현

사용 예)

```swift
let rect: CGRect = .init(x: 100, y:100, width: 150, height:300)
```

## 3. 사용방법

[https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcvBgKM%2FbtqLBMPmtzc%2Fm352LMUQ7Wko7jmE07Rki1%2Fimg.png](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcvBgKM%2FbtqLBMPmtzc%2Fm352LMUQ7Wko7jmE07Rki1%2Fimg.png)

```swift
let rect: CGRect = .init(x: 100, y:200, width: 150, height:200)
let myView: UIView = .init(frame: rect)

myView.backgroundColor = .yellow
self.view.addSubView(myView)
```
