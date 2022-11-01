# SwiftLint 세부설정하기

# SwiftLint 세부설정하기

이전글: [SwiftLint 세팅하기](https://github.com/isGeekCode/TIL/blob/main/Library/TIL221028_SwiftLint.md)

SwiftLint를 brew로 설치해 사용하고 있다.

자동 수정세팅까지 해서 만족스럽게 사용을 하고있는데, 갑자기 AppDelegate함수가 120자 이상이라 경고 메세지가 등장하기 시작했다.

그래서 잠시 뒤로 미뤄 뒀던 SwiftLint 세부설정방법을 조사해본다.

SwiftLint를 설정하지 않은 상태에서는 이부분은 아주 자연스러운 부분이다. 특히나 여기말고도 Delegate관련 함수들은 파라미터를 포함해 3줄, 4줄까지도 가는 함수들이 많기 때문에 이건 아니다 싶어 예외처리를 해야겠다는 생각이 들었다.

`SwiftLint를 세팅하면 보이는 경고`

<img width="1286" alt="스크린샷 2022-11-01 오후 1 04 59" src="https://user-images.githubusercontent.com/76529148/199176936-089767b9-b035-4c0e-ac89-4a5cddc2cb74.png">

`아래처럼 수정할 경우, 한줄에 120자 제한 경고는 사라진다.`

<img width="1037" alt="스크린샷 2022-11-01 오후 1 06 26" src="https://user-images.githubusercontent.com/76529148/199176952-12fef861-0515-4ab8-b9da-acd135f7b17f.png">

방금전 이미지처럼 수정할 경우 경고는 없지만,, 적어도.. 나에겐 .. 이상하다는 생각이 든다.

그래서 추가로 룰을 커스텀해보자.

SwiftLint에는 두가지 룰이 있다.

## Default Rules

첫번째로는 기본적으로 **default rules**이라고 해서 말 그대로 **기본룰이다**.

대략 **90여가지가** 있는걸로 알고 있고 이는 자주 사용되는 즉 위에서 말했던 대부분의 개발자들이 대중적으로 알고 있는 그런 컨벤션 룰을 기본 룰로 채택하고 있다.

만약 기본 룰에서 제거하고 싶은 즉 **적용시키지 싫은 룰이 있다면 disabled_rules로 yml 파일을 통해 정의해줘서 배제**시킬 수도 있다.

또한 yml 파일을 통해 기본 룰에서 값들을 원하는대로 변경해줄 수 있다.

**즉 커스텀하게 설정**해줄 수도 있음.

## Opt-In Rules

그 다음으로는 **옵트인 룰** 이다

**선택적으로 추가할 수 있도록 하는 룰이**다.

기본 룰과는 달리 옵트인 룰은 하나도 심어져 있지 않기에 원하는것들을 찾아 심어줘야한다!

갯수로는 **120여가지**가 있으며 기본 룰보다 훨씬 많은 수이다.

그만큼 정말 다양한 룰을 원한다면 왠만한 룰은 다 추가할 수 있다는 말이다.

[Rule Reference](https://realm.github.io/SwiftLint/rule-directory.html) 에서 확인할 수 있고 각 룰을 클릭하면 설명을 볼 수 있다.

### 세부사항

- Identifier: 룰의 고유 id
- Enabled by default: swiftlint 기본 포맷팅으로 작동하는지
- Supports autocorrection: `swiftlint autocorrect` 명령어를 먹게 하는지
- Kind: 룰의 종류
- Minimum Swift compiler version: Swift 컴파일러 최소 지원버전
- Default configuration: warning 혹은 error로 알림

## 커스텀 룰 적용하기

룰을 커스텀하기위해 앱의 최상단에서 New File로 Empty File을 하나 생성한다. 그리고 파일명은 “.swfitlint.yml”로 저장한다.

<img width="408" alt="스크린샷 2022-11-01 오후 1 56 57" src="https://user-images.githubusercontent.com/76529148/199176986-670f8de7-3fcd-46f5-8067-93b9ecaa2e3d.png">

파일명앞에 .이 있으면 숨김파일로 인식이 되어 경고메세지가 뜨지만 Use “.”를 눌러 경고를 무시한다.

### 세팅을 위해 사용하는 4개의 옵션

```bash
disabled_rules: # 기본 활성화된 룰 중에 비활성화할 룰을 지정

opt_in_rules: # 기본(default) 룰이 아닌 룰들을 활성화

included: # swiftlint 과정에 포함할 파일 경로

excluded: # swiftlint를 적용하지 않게 설정할 파일 경로
```

적용 방법은 아래와 같다.

```bash
disabled_rules:  # 기본 활성화된 룰 중에 비활성화할 룰을 지정
- force_cast
- trailing_comma
- force_try
- identifier_name

type_body_length: 250  # 타입/함수/파일 등의 코드길이 제한을 변경하겠다는 뜻
line_length: 120
function_body_length: 50
file_length: 500
```

내가 적용한 커스텀룰

```bash
disabled_rules:                     # 기본 활성화된 룰 중에 비활성화할 룰을 지정
  - vertical_whitespace             # 세로 공백을 하나의 빈 줄로 제한

opt_in_rules:                       # 기본(default) 룰이 아닌 룰들을 활성화
  - empty_count                     # count보다 isEmpty 선호
  - closure_end_indentation         # 클로저의 끝 괄호를 시작한 행과의 들여쓰기 맞춤

excluded:                           # swiftlint를 적용하지 않게 설정할 파일 경로
  - Carthage
  - Pods

force_cast: warning     # implicitly
force_try:
  severity: warning     # explicitly

line_length: 180                    # 코드 한 줄의 글자 수 제한
type_body_length:                   # 본문의 행수 제한
  - 1000                # warning
  - 1500                # error

file_length:                        # 한 파일의 행수 제한
  warning: 1000
  error: 2000

type_name:                          # 타입 네이밍 커스텀 정의
  min_length: 2                     # default: warcning
  max_length:                       # warning and error
    warning: 80
    error: 100
  excluded: iPhone                  # excluded via string

identifier_name:                    # 식별자 네이밍 커스텀 정의
  min_length:                       # only min_length
    error: 2                        # only error
  excluded:                         # excluded via string array
    - id
    - URL
    - GlobalAPIKey
    - ad
reporter: "xcode"                    # reporter type (xcode, json, csv, checkstyle, junit, html, emoji)
```

계속해서 내게 맞는 용도의 커스텀 룰을 적용하는 것이 중요하다.

### 참고링크

- minji0801: [https://velog.io/@minji0801/SwiftLint](https://velog.io/@minji0801/SwiftLint)
- whitehyun: [https://velog.io/@whitehyun/iOS-Swiftlint-룰-적용하기](https://velog.io/@whitehyun/iOS-Swiftlint-%EB%A3%B0-%EC%A0%81%EC%9A%A9%ED%95%98%EA%B8%B0)
- Pilvi: [https://pilvi.tistory.com/3](https://pilvi.tistory.com/3)
