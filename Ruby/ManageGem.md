# RubyGems - Package Manager

루비에서는 RubyGems라는 패키지관리 시스템이 있다. 이걸 통해 패키지(라이브러리)를 설치하고 관리 할 수있다.

rubygems.org 서버로부터 라이브러리, 애플리케이션 및 플러그인을 관리할 수 있다.

gem 명령어를 통해 설치, 업데이트, 삭제, 검색 등의 작업을 할 수 있다.

rbenv를 사용하는 경우 버전마다 각각 설치되니 헷갈리지않도록 주의한다.
rbenv로 버전을 전환해도 가끔 system의 gem에 참조되어 있는 경우가 있다. `bash`나 `zshrc`같은 shell 설정파일에 경로 설정을 했는지 꼭 체크를 해야한다. 


## 사용법

```
# 기본 명령어
gem install <gem 이름> -v 1.15.4

# gem 업데이트 -> 최신화
gem update

# 설치된 gem을 복원 
gem pristine <gem 이름>

# 설치된 gem 전체보기
gem list

# 해당 gem과 관련된 모든 버전을 보기 
gem pristine <gem 이름>
```

## 사이트 링크

[공식 사이트 rubygems.org](https://rubygems.org/)
