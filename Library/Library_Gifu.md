# Library - GIFu 사용하기

iOS에서 이미지파일인 PNG, JPG 확장자는 UIImage를 통해 바로바로 사용할 수 있다.

하지만 GIF파일은 사용할 수가 없다. 

만약 UIImage에 JPG나 PNG파일과 같은 방법으로 이미지를 부여하게 되면 정지된 첫 화면만 보이게된다. 

GIF파일은 여러장의 이미지를 가지고 있기 때문에 다른 페이지로 전환하는 게 필요한 이미지이다. 

결국 GIF파일을 사용하기 위해선 라이브러리를 사용하게 된다. 

이 때 사용하는 대표적인 라이브러리는 GIFu라는 라이브러리이다.

gifu를 통해 UIImage객체가 아닌 전용 객체를 생성해서 GIF를 재생시킬 수 있다.

## GitHub 소스

- [https://github.com/kaishin/Gifu](https://github.com/kaishin/Gifu)

# Installation

해당 깃허브에서는 SPM, CocoaPods, Carthage를 이용해 설치를 할 수 있고 튜토리얼에 나오지만

2023년 1월1일 기준으로 SPM은 설치가 제대로 되지않아 CocoaPods으로 설치를 진행했다. 

## CocoaPods설치하기

### Step0. CocoaPods 설치하기 ( 세팅안된경우 )

- 터미널에서 CocoaPods을 설치한다.
- `sudo gem install cocoapods`

### Step1. Pod파일 생성하기

- 터미널로 프로젝트파일이 있는 곳으로 진입
- `pod init` 입력

### Step2. Pod파일에 라이브러리 리스트업하기

- 생성된 팟파일에서 `target '프로젝트이름' do` 와 `end` 사이에 아래 코드 입력
- `pod ‘Gif’`
- 만약 특정버전이 필요할 경우 세부버전 입력하기 ( GIFU는 그냥 해도된다 )

### Step3. Pod파일 인스톨

- 아래 코드 입력으로 리스트업된 라이브러리 설치
- `pod install`

### Step4. .xcworkspace 파일로 프로젝트 사용하기

- CocoaPods라이브러리를 사용하게되면 새로생긴 .xcworkspace 파일을 사용해야한다.
- 가끔 이걸 잊고 놀랄 수 있다.

## How to use

### Step0. import

- `import Gifu`

### Step1. 변수선언

- `GIFImageView` 로 객체 생성하기

### Step2. addSubView

- view위에 추가한다.

### Step3. SetConstraint

- Constraint세팅
- 혹은 frame을 잡아준다.

### Step4. 파일세팅

프로젝트에 추가된 파일이름명으로 세팅하기

```swift
let imageView = GIFImageView(frame: CGRect(x: 0, y: 0, width: 200, height: 100))
// 파일명 세팅
imageView.animate(withGIFNamed: "mugen") {
  print("It's animating!")
}
```

## 📌 prepareForAnimation(with … ) /  Animate(with …. )

### prepareForAnimation(with … )

상황에 따라 이미지를 세팅만 하고 대기를 시킬 수 있다.

```swift
override func viewDidLoad() {
  super.viewDidLoad()
  imageView.prepareForAnimation(withGIFNamed: "mugen") {
    print("Ready to animate!")
  }
}
```

이 함수는 파라미터에 따라 다양하게 이용이 가능하다.

### startAnimatingGIF / stopAnimatingGIF

준비된 gif를 켜고 끌 수 있다.

```swift
@IBAction func toggleAnimation(_ sender: AnyObject) {
  if imageView.isAnimatingGIF {
    imageView.stopAnimatingGIF()
  } else {
    imageView.startAnimatingGIF()
  }
}
```

### isAnimatingGIF

이 프로퍼티를 이용해 위 코드처럼 현재 동작중인지 캐치가 가능하다. 

## Parameters

### animate(withGIFNamed: )

### animate(withGIFData: )

### animate(withGIFURL: )

- 

### loopCount

몇번 재생할 것인지 세팅할 수 있다.

### prepareForAnimation(withGIFNamed: "<파일명>")

파일명으로 세팅하기

### prepareForAnimation(withGIFNamed: "<파일명>")

- `[animate(withGIFNamed:loopCount:completionHandler:)](http://kaishin.github.io/Gifu/Protocols/GIFAnimatable.html#/s:4Gifu13GIFAnimatablePAAE7animateySS12withGIFNamed_Si9loopCountyycSg17completionHandlertF)` *확장 방법*
- `[animate(withGIFData:loopCount:completionHandler:)](http://kaishin.github.io/Gifu/Protocols/GIFAnimatable.html#/s:4Gifu13GIFAnimatablePAAE7animatey10Foundation4DataV11withGIFData_Si9loopCountyycSg17completionHandlertF)` *확장 방법*
- `[animate(withGIFURL:loopCount:completionHandler:)](http://kaishin.github.io/Gifu/Protocols/GIFAnimatable.html#/s:4Gifu13GIFAnimatablePAAE7animatey10Foundation3URLV10withGIFURL_Si9loopCountyycSg17completionHandlertF)` *확장 방법*
- `[prepareForAnimation(withGIFNamed:loopCount:completionHandler:)](http://kaishin.github.io/Gifu/Protocols/GIFAnimatable.html#/s:4Gifu13GIFAnimatablePAAE19prepareForAnimationySS12withGIFNamed_Si9loopCountyycSg17completionHandlertF)` *확장 방법*
- `[prepareForAnimation(withGIFData:loopCount:completionHandler:)](http://kaishin.github.io/Gifu/Protocols/GIFAnimatable.html#/s:4Gifu13GIFAnimatablePAAE19prepareForAnimationy10Foundation4DataV11withGIFData_Si9loopCountyycSg17completionHandlertF)` *확장 방법*
- `[prepareForAnimation(withGIFURL:loopCount:completionHandler:)](http://kaishin.github.io/Gifu/Protocols/GIFAnimatable.html#/s:4Gifu13GIFAnimatablePAAE19prepareForAnimationy10Foundation3URLV10withGIFURL_Si9loopCountyycSg17completionHandlertF)` *확장 방법*
