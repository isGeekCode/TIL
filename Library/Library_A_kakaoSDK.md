라이브러리 - 카카오 SDK 사용하기

## 설치

코코아팟 설치하기
Kakao SDK의 일부 모듈은 다른 모듈에 의존성이 있으며, 각 모듈은 설치 시 의존하는 모듈을 자동으로 함께 설치한다.



### Step0. CocoaPods 설치하기 ( 세팅안된경우 )

- 터미널에서 CocoaPods을 설치한다.
- `sudo gem install cocoapods`


### Step1. Pod파일 생성하기

터미널로 프로젝트파일이 있는 곳으로 진입
- `pod init` 입력

### Step2. Pod파일에 라이브러리 리스트업하기

- 생성된 팟파일에서 `target '프로젝트이름' do` 와 `end` 사이에 아래 코드 입력
`pod ‘KakaoSDKCommon’`

- 만약 특정버전이 필요할 경우 세부버전 입력하기
`pod ‘KakaoSDKCommon’, ‘~> 2.14.0’`

### Step3. Pod파일 인스톨

아래 코드 입력으로 리스트업된 라이브러리 설치
`pod install`

### Step4. .xcworkspace 파일로 프로젝트 사용하기

CocoaPods라이브러리를 사용하게되면 새로생긴 .xcworkspace 파일을 사용해야한다.

## 공유하기기능


V2로 마이그레이션하기


