# Ruby - 버전관리 : RVM, Rbenv 사용법

## RVM

Ruby Version Manager을 줄여 RVM이라 한다.

여러 버전의 루비를 깔때, 편리하게 관리하는 프로그램이다.

개발을 할 때에 프로젝트마다 사용되는 라이브러리의 종류와 버전이 다르기때문에 이들을 따로 관리할 필요가 있다.

루비에서 쓰는 라이브러리 패키지를 gem이라고 하며, 여러가지 gem을 모아놓은것을 gemset이라고한다.

RVM은 프로젝트마다 gemset을 따로 가질수 있도록 관리가 가능하도록 해주는 툴이다.

## Rbenv
Rbenv는 루비의 버전을 독립적으로 사용할 수 있도록 도와주는 패키지다.

보통 Mac에서는 OS에 설치된 Ruby에 의존하다보니 진행하는 프로젝트에서 요구하는 버전을 사용할 때 영향을 받게 된다. 또한 여러 프로젝트를 오가려면 어쩔 수 없이 해당 루비버전을 지우고 필요한 루비버전을 다시 설치하는 일을 반복해야 했다.

이를 해결하기 위해 만들어진게 rbenv이다. 여러개의 ruby버전 설치가 가능하다.

최근 (2023기준) rvm보다 rbenv를 사용하는 사람이 많은 이유가 있다.

루비에서는 RubyGems라는 패키지관리 시스템이 있다. 이걸 통해 패키지(라이브러리)를 설치하고 관리 할 수있다.

이때 라이브러리의 버전에 대한 dependency를 관리해야 할 일이 생기는데, rbenv는 dependency를 책임지는 라이브러리가 비생성 되다보니 이 덕분에 라이브러리 dependency도 함께 설치되는 rvm에 비해 가볍다는 장점이 있다.

### Rbenv 사용법
brew를 통해 설치할 수 있다.

```
# 설치
brew update
brew install rbenv ruby-build

# 설치 확인
rbenv versions
## 혹은 
rbenv -v

# 아래의 형태로 나오면 system ruby 사용중
* system (set by /Users/...
```
rbenv를 설치하고 버전을 확인해보면 system으로 나오게 된다. 시스템에 기본적으로 설치된 버전이다.
```
# 해당 명령어를 통해 설치가능한 ruby 버전 확인
rbenv install -l

# 버전을 입력하여 루비 설치
rbenv install <version>

# 설치된 ruby들을 확인하기
rbenv versions

# 설치된 ruby들이 나오고, 선택된 루비가 표시됨
* system (set by /Users/<유저이름>/.rbenv/version)
  3.0.1
  
# 여기서 global명령어로 현재 루비버전을 변경
rbenv global 3.0.1

# Shell 설정파일 편집 진입
vi ~/.zshrc

## 아래 내용 추가
[[ -d ~/.rbenv  ]] && \
  export PATH=${HOME}/.rbenv/bin:${PATH} && \
  eval "$(rbenv init -)"

# Shell 설정파일 저장 후 적용
source ~/.zshrc
```

설치 이후에는 아래와 같이 버전만 변경하여 사용하면 된다.

### 버전 전환하기

```
# 설치된 ruby들을 확인하기
rbenv versions

# 설치된 ruby들이 나오고, 선택된 루비가 표시됨
* system (set by /Users/<유저이름>/.rbenv/version)
  3.0.1
  
# 여기서 global명령어로 현재 루비버전을 변경
rbenv global 3.0.1
```

### rbenv 사용시 주의할 점
rbenv를 사용하는 경우 버전마다 각각 설치되니 헷갈리지않도록 주의한다. rbenv로 버전을 전환해도 가끔 system의 gem에 참조되어 있는 경우가 있다. bash나 zshrc같은 shell 설정파일에 경로 설정을 했는지 꼭 체크를 해야한다.

자칫 gem관련 에러가 발생하면 brew에서 설치된 라이브러리들이 실행이 안되거나 cocoapods도 실행이 안되기도 한다. 

## 관련 링크
- [RubyGems - Package Manager :　gem 관리하기](https://github.com/isGeekCode/TIL/blob/main/Ruby/ManageGem.md)

