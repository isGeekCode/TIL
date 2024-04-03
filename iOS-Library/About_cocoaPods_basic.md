# CocoaPods 사용하기



### 공식페이지 링크
- [cocoapods.org](https://cocoapods.org/)


코코아프로젝트에 대한 의존성 패키지를 관리하는 도구다. 쉽게 말해 외부 라이브러리를 간단핳게 설치할 수 있게 도와주는 유틸

과거에는 개발자가 외부라이브러리를 사용하면 자동 업데이트가 이루어지지 않았기 때문에 버전 관리는 순전히 개발자의 성실성에 달려 있었다. 해당 라이브러리의 새 버전으로 업뎃하기 위해서는 개발자가 꾸준히 관심을 갖고 버전 업데이트 여부를 확인해야 했다. 간혹 소홀할 경우 버그가 발생하기도 했다.

## Pod이란

코코아팟은 루비 언어를 이용하여 만들어진 패키지 의존성 관리 도구로서, 지원하는 라이브러리들은 Pod이라는 개념으로 다룬다.

따라서 코코아팟이라는 이름은 **코코아 개발환경 + 라이브러리** 라는 의미를 나타내는 것이다.

Mac에는 이미 ruby가 설치되어있기 때문에 ruby를 추가적으로 설치해줄 필요는 없다. 다만 가끔 gem 관련 에러가 발생하여 ruby를 사용못하는 상황이 발생한다. 그러면 cocoapods도 먹통이기때문에 사용법을 이해할 필요가 있다.

<br><br>

## CocoaPods 설치된 버전 확인하기

### 현재 메인 버전 확인하기
```
pod --version
// 1.15.2
```

<br>

### 현재 pc에 설치된 버전 전부 확인하기

기본적으로 메인 버전은 설치한 버전중 가장 최신 버전이다.  
```
gem list - local | grep cocoapods

// cocoapods-core (1.15.2, 1.12.0, 1.8.0)
// cocoapods-deintegrate (1.0.5)
// cocoapods-downloader (2.1, 1.6.3)
// cocoapods-plugins (1.0.0)
// cocoapods-search (1.0.1)
// cocoapods-stats (1.1.0)
// cocoapods-trunk (1.6.0)
// cocoapods-try (1.2.0)
```

## CocoaPods 설치하기
내가 필요없는 버전은 삭제해야하는 경우가 있다.  

```
sudo gem uninstall cocoapods -v 1.8.0
```

<br><br>

## CocoaPods 설치하기
여러가지 방법으로 설치를 할 수 있다.

<br>

### RubyGems를 사용한 설치

RubyGems을 사용하여 CocoaPods를 설치하는 것이 가장 일반적인 방법

```
sudo gem install cocoapods
```

<br>

### HomeBrew를 통한 설치
먼저 RubyGems를 사용한 설치를 해도 안되면 이방법을 사용하는 것이 좋다. 

```
brew install cocoapods

```

<br><br>

## 사용방법
Cocoapods 설치를 완료하면 원하는 프로젝트의 폴더로 이동한다. 
코코아팟을 통해 라이브러리를 설치하기 위해서는 Podfile이라는 것에 직접 라이브러리 이름, 필요할 경우 특정 버전을 기입한다.
그리고 기입된 내용을 통해 라이브러리를 설치하는 것이다. 


<br>

### 팟파일 생성하기
```
pod init
```

<br>

### 팟파일 편집하기
폴더내 생성된 Podfile에 들어가 버전정보 기입한다.
타겟이 여러개인 경우, 해당 타겟에 맞게 기입한다. 

뒤에 버전은 최신버전만 사용할 경우에는 기입하지않아도된다. 
만약 버전에 민감한 앱이라면 버전을 기입해주는 것이 좋다. 
```
# Pods for <앱이름>
pod ‘KakaoSDKCommon’, ‘~> 2.14.0’
```

<br>

### 라이브러리 설치하기

터미널을 통해 설치하는 경우, Podfile이 있는 폴더경로에서 아래와 같이 입력한다. 
```
pod install
```

성공적으로 설치되면 해당 경로에 동일 프로젝트명으로  `.xcworkspace`파일이 하얀색 아이콘으로 생성된다. 코코아팟을 통해 라이브러리를 설치하면 앞으로 이 파일을 통해 프로젝트를 편집해야한다. 

### Podsfile 버전 명시하기

**Q. Podfile 에서 `~>` 는 무엇을 의미할까?**

`~>` 기호는 버전의 상한선(이보다 높을 수 없음) 을 의미한다. 버전은 `메이저.마이너.패치`로 구분한다.

```swift

- `~> 0.1.2` 버전 0.1.2 ~ 0.2 (0.2 이상 포함되지 않음)
- `~> 0.1'` 버전 0.1 (1.0 이상 포함하지 않음)
- `>` 말고도 다른 연산자도 있다
- `> 0.1` 0.1보다 큰 모든 버전
- `>= 0.1` 버전 0.1 이상
- `< 0.1` 0.1보다 낮은 모든 버전
- `<= 0.1` 버전 0.1 및 그 이하 버전
```

### Pod 명령어

**[1] Podfile.lock을 여는 명렁어**

```
open podfile.lock
```

## cocoapod 명령어

```
# 현재 버전 보기
pod --version

# 설치된 모든 cocoaPods버전 보기
sudo gem list cocoapods

# 원하는 버전으로 업데이트
sudo gem install cocoapods -v 1.9.1

# 팟을 최신 버전으로 업데이트
pod update

# 지정한 팟을 최신 버전으로 업데이트
pod update <팟 이름>

# 로컬 캐쉬리스트를 출력
pod cache list

# 로컬 캐쉬들을 모두 지우기
pod cache clean --all
```
[로컬캐시 관련 링크](https://www.stackoverflow.com/questions/46428752/how-to-clear-or-clean-specific-pod-from-the-local-cocoapods-cache)

---

## Pods 폴더 지우기
자꾸 에러가 나면 해당 폴더만지우고 다시 설치하는 게 나을 때가 있다.

```
pod repo update
sudo rm -r [프로젝트명].xcworkspace
sudo rm -r Pods
pod install
```

## 코코아팟 삭제하기

```
sudo gem uninstall cocoapods
```

## Podfile.lock 을 깃에 커밋하는 이유

`해야한다`

뭔가 확장자가 .gitignore에 포함되어야 할 느낌이지만! Podfile.lock은 Pod 파일들의 버전을 픽스시켜주는 역할을 한다.다른사람에게 프로젝트를 공유할 때, 동일한 라이브러리 환경을 제공하기 위해 필수로 필요하며, 따라서 Git 으로 함께 버전관리를 해야한다.

CocoaPod
