# Show는 push와 present의 추상화 메서드

맨처음 스토리보드로 Segue(세그웨이)의 연결을 하다보면 아래와 같은 화면을 볼 수 있다.  

<img width="300" alt="img1 daumcdn-2" src="https://github.com/isGeekCode/TIL/assets/76529148/5208ee80-82db-4a54-ae25-cf25e9e1d784">

<br><br>

위 이미지는 스토리보드에서 화면과 화면을 세그웨이로 연결할 때, 어떤 종류의 화면이동을 할지 선택하는 부분이다.  

- show
- show Detail
- Present Modally
- Present As Popover

<br><br>

여기서 Segue를 세팅할 때, 일반적으로는 show를 선택한다.  
그렇다면 Segue로 할 수 있는 화면이동 종류는 크게는 show와 present가 있는데 그게 뭘까?

그걸 이해하기 위해서는 탭, 네비게이션, subview에 대한 의미를 알아야한다. 

<br><br>

## 카테고리

일반적으로 앱에서의 대주제는 탭바를 통해 들어가게 된다.  

<img width="700" alt="스크린샷 2023-11-30 오후 2 10 02" src="https://github.com/isGeekCode/TIL/assets/76529148/ac9da53f-12b6-40fd-972d-268df6c68e55">

<br><br>

그리고 이 각각의 탭에서 해당 카테고리에 대한 소주제, 세부카테고리로 들어가게 된다.  
이 구조는 일반적으로 네비게이션 컨트롤러를 통해 구성된다.  

<br><br>

<img width="700" alt="뷰계층 1" src="https://github.com/isGeekCode/TIL/assets/76529148/f78d77c2-8b1f-4fd4-a162-081edfdb11f6">


<br><br>

## 네비게이션 스택

네비게이션컨트롤러를 사용하는 경우는 네비게이션컨트롤러라는 컨테이너 안에 navigation Stack에서 ViewController를 관리한다.  

<img width="600" alt="ezgif-3-1199988740" src="https://github.com/isGeekCode/TIL/assets/76529148/640dccf5-09d2-4e0f-bb04-8021cb3451de">

이런식으로 Navigation Stack에 ViewController가 쌓이게된다.

<br><br>

<img width="400" alt="245374018-87eefccd-c9c2-4dd5-ba8f-38cf249a68bc" src="https://github.com/isGeekCode/TIL/assets/76529148/4a5c14eb-8781-4e3b-874f-c2c22d82b29f">

<br><br>

우리는 이 viewcontroller들을 아래와 같이 접근할 수 있다.

```swift
guard let vcs = self.navigationController?.viewControllers as? [UIViewController] else { return }
```


<br><br>

이 스택이라는 데이터구조처럼 이 네비게이션 스택에 화면을 추가하고 빼는 작업은 push와 pop 형식으로 처리된다. 

```swift
// 네비게이션 스택에 추가
let settingVC = SettingViewController()
self.navigationController?.pushViewController(settingVC, animated: true)

// 네비게이션 스택에서 제거
self.navigationController?.popViewController(animated: true)
```

<br><br>

## 모달 프레젠테이션
이번엔 stack의 push / pop과 또다른 개념인 present / dismiss 를 살펴보자.

- 탭바 : 대주제간의 전환
- 네비게이션 : 대주제에서 소주제간의 수직적 이동

앞선 본질처럼  모달 프레젠테이션의 본질은 
`특정 작업이나 내용에 사용자의 주의를 집중시키기 위해 일시적으로 기존의 작업 흐름을 중단시키는 방식`이다.

<br><br>

정리하자면
> 사용자의 주의를 새로운 화면에 집중시키고자 할 때, 
> 현재 화면 위에 새로운 화면을 덮는 방식으로 화면을 표시한다.  

<br><br>

이 모달 형식은 이미 모바일에서 많이 찾아볼 수 가 있는데, 몇가지 예를 들어보면 아래와 같다.  

- 경고 및 확인 대화 상자 : 앱에서 중요한 정보를 사용자에게 알리거나 사용자의 확인을 요구하는 경우, 경고 대화 상자나 확인 대화 상자
- 입력 양식 : 사용자가 새로운 데이터를 입력하거나 기존 데이터를 편집할 때 사용되는 입력 양식이 모달로 표시
- 상세 정보 보기: 목록에서 항목을 선택했을 때, 해당 항목의 상세 정보를 보여주는 뷰 컨트롤러를 모달로 표시하는 경우도 있다.

<img width="600" alt="ezgif-3-009309e806" src="https://github.com/isGeekCode/TIL/assets/76529148/101871d2-e661-4539-9f66-3dd874ade88e">

<br><br>

이 모달 프레젠테이션을 코드로 사용한다면 아래와 같이 사용한다.  

```swift
// 추가
let settingVC = SettingViewController()
present(settingVC, animated: true)

// 제거
dismiss(animated: true)
```

<br><br>

## Show는 그럼 뭔가요

이걸위해 한참을 설명했다.  

show 메서드는 navigationController의 유무에 따라 다른 동작을 보여준다.  

- navigationController가 있는 경우 : push방식으로 동작
- navigationController가 없는 경우 : 모달방식으로 동작

<br><br>

show메서드의 사용방식을 살펴보자. 

```swift
let settingVC = SettingViewController()
show(settingVC, sender: nil)
// navigationController?.show(settingVC, sender: nil)  비추천

//네비게이션바가 없는 경우, dismiss로 제거
dismiss(animated: true)
```

<br><br>

### show가 동작하지 않는 상황

이때, 주의해야할 것은 navigationController?를 사용하면 만약 정말로 navigationController가 없는경우 옵셔널체이닝에서 끊어져서 show가 동작하지 않는다. 
그래서 `show(ViewController,sender:)`형식으로 사용해야한다.  

<br><br>

### show는 그럼 왜 사용하나요??

show 메서드는 iOS의 adaptive interface를 지원한다.  
이는 다양한 환경(예: iPhone과 iPad)에서 일관된 사용자 경험을 제공하기 위해 설계되었다.  
예를 들어, iPad에서는 split view 컨트롤러 내에서 보여줄 수도 있고, iPhone에서는 전체 화면으로 표시할 수도 있다.  

show 메서드를 사용하는 주요 이점은 뷰 컨트롤러 간의 이동을 추상화하여,  
다양한 환경에서 일관된 동작을 보장하고, 컨트롤러 간의 연결을 더 유연하게 만들어 준다.  
개발자는 구체적인 전환 방식(push 또는 present)을 신경 쓰지 않고, 시스템이 가장 적절한 방식을 선택하도록 할 수 있다.  

<br><br>

### 예외 사항
가끔  네비게이션 컨트롤러에 임베드되어있는 ViewController에서 모달형식을 띄워야하는 순간이 있다.  
이때에는 show를 사용하면 무조건 push처리가 되기 때문에,  
확정적으로 present를 사용해야 원하는 동작을 구현할 수 있다.  


<br><br>


## History
- 231130 : 초안작성
