# Installation: CocoaPods

코코아프로젝트에 대한 의존성 패키지를 관리하는 도구다. 쉽게 말해 외부 라이브러리를 간단핳게 설치할 수 있게 도와주는 유틸

과거에는 개발자가 외부라이브러리를 사용하면 자동 업데이트가 이루어지지 않았기 때문에 버전 관리는 순전히 개발자의 성실성에 달려 있었다. 해당 라이브러리의 새 버전으로 업뎃하기 위해서는 개발자가 꾸준히 관심을 갖고 버전 업데이트 여부를 확인해야 했다. 간혹 소홀할 경우 버그가 발생하기도 했다.

최근에는 이런 문제를 줄이고 개발 생산성 향상을 위해 주요 라이브러리를 데이터베이스화하여 관리해주는 도구들이 많이 생겨났는데, 우리는 이 유틸을 사용하여 앱 프로젝트에 원하는 라이브러리를 손쉽게 설치하고 버전까지 관리할 수 있게 되었는데, 이것을 **패키지 관리 도구** 라고 부른다.
[코코아팟 LINK](https://cocoapods.org/)

### 패키지 관리도구

이들은 내부적으로 데이터베이스화한 라이브러리 목록을 제공하고 있으며, 이중에서 원하는 라이브러리를 검색하여 간편하게 설치할 수 있다.

- **CocoaPods**
- **Carthage**
- **스위프트 패키지 관리자 (Swift Package Manager, SPM)**
- CentOS 계열의 리눅스에서 사용하는 yum
- Fedora 계열의 리눅스에서 사용하는 apt-get
- 파이썬 패키지를 관리하는 pip
- 루비 패키지를 관리하는 gem
- node.js 패키지를 관리하는 npm
- 자바의 MAVEN 등

코코아팟은 루비 언어를 이용하여 만들어진 패키지 의존성 관리 도구로서, 지원하는 라이브러리들은 Pod이라는 개념으로 다룬다.

따라서 코코아팟이라는 이름은 **코코아 개발환경 + 라이브러리** 라는 의미를 나타내는 것이다.

Mac에는 이미 ruby가 설치되어있기 때문에 따로 설치해줄 필요는 없다. 다만 가끔 gem 관련 에러가 발생하여 ruby를 사용못하는 상황이 발생한다. 그러면 cocoapods도 먹통이기때문에 사용법을 이해할 필요가 있다.

### Podsfile의 버전명시

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

**[2] cocoapod 버전 업그레이드**

아래 명령어로 현재 버전을 확인하고

```
pod --version

//설치된 모든 cocoaPods버전을 보여줌
sudo gem list cocoapods
```

원하는 버전으로 업데이트 시켜주세요

```
sudo gem install cocoapods -v 1.9.1
```

**[3] 로컬 캐쉬를 지울때**

아래 명령어로 로컬 캐쉬리스트를 출력할 수 있습니다.

```
pod cache list
```

그리고 아래 명령어로 로컬 캐쉬들을 모두 지울 수 있습니다.

```
pod cache clean --all
```

([www.stackoverflow.com/questions/46428752/how-to-clear-or-clean-specific-pod-from-the-local-cocoapods-cache](https://www.stackoverflow.com/questions/46428752/how-to-clear-or-clean-specific-pod-from-the-local-cocoapods-cache))저는 private 라이브러리가 특정 태그를 바라보게 하고, 특정 태그를 지웠는데도

"pod update 라이브러리명" 했을때 실패가 안되는 현상이 있었습니다.그때 로컬캐쉬를 지워주니까 실패가 되더라구요..!

---

**[4] Podfile과 Podfile.lock이 계속 충돌날때, /Pods 폴더 아예 지우기**

```
pod repo update
sudo rm -r [프로젝트명].xcworkspace
sudo rm -r Pods
pod install
```

[pod repo update](https://guides.cocoapods.org/terminal/commands.html#pod_repo_update)로 로컬 클론을 업데이트 해주세요

그 다음에 xcworkspace랑 Pods를 지워주고다시 pod install해주세요

---

**[5] 만약 동료들과 같은 Podfile.lock CHECKSUM을 얻는데에 실패했다면**

```
rm -rf Pods
```

```
pod install
```

[https://onelife2live.tistory.com/30](https://onelife2live.tistory.com/30)

[
[Cocoapods] pod install? pod update? 제대로 알고 쓰자
많은 사람들이 pod install 을 코코아팟 프로젝트를 처음 세팅할 때 딱 한 번 쓰고 pod update 는 그 이후에 사용된다고 생각합니다. 그러나 전혀 그렇지 않습니다! 😝 이번 포스팅에서 pod install 과 pod update..
onelife2live.tistory.com](https://onelife2live.tistory.com/30)

---

**[6] 신규 프로젝트 생성할 때**

cocoapod을 설치한 상황에서 신규 프로젝트 생성할 때.

안했으면 sudo gem install cocoapods)

1. 해당 폴더를 터미널에 끌어놓기

2. pod init 으로 podfile을 만든다.

(ls 명령어로 podfile이 생겼는지 확인하기)

3. open podfile로 podfile을 열어서 필요한 라이브러리들을 적는다.

4. pod install 한다.

=> Podfile.lock 과 xcworkspace 가 생기게 된다. (만약 3번 과정을 안하고 pod install 해도 생긴다)

**[7] 코코아팟 제거**

```swift
>sudo gem uninstall cocoapods
```

### Podfile.lock 의 버전관리 (git commit에 포함해야 하나?)

`해야한다`

뭔가 확장자가 .gitignore에 포함되어야 할 느낌이지만! Podfile.lock은 Pod 파일들의 버전을 픽스시켜주는 역할을 한다.다른사람에게 프로젝트를 공유할 때, 동일한 라이브러리 환경을 제공하기 위해 필수로 필요하며, 따라서 Git 으로 함께 버전관리를 해야한다.
