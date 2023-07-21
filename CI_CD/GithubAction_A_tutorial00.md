# CI/CD - GitHub Action 사용하기 : 초기 구현하기

구현하는 데에는 아래 동작이 진행된다.

- 레포지토리에 디렉토리 생성
- 워크플로우 파일 생성
- 워크플로우 설정
- 워크플로우 커밋 및 푸시


## 레포지토리에 디렉토리 생성
레포지토리의 루트에 `.github/workflows` 디렉토리를 만든다. 

깃허브에서는 이 디렉토리에서 작업을 찾아서 실행한다.
웹에서 작성해도되지만 그냥. 만들어서 하는게 편할 수 있다.


## 워크플로우 파일 생성
`main.yml`이라는 YAML 파일을 `.github/workflows` 디렉토리에 만든다. 

이 파일은 깃허브 액션의 설정하는 파일이다.


## 워크플로우 설정
main.yml 파일 내에 워크플로우를 설정한다.

```
name: CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2

    - name: Run a one-line script
      run: echo Hello, world!

```

- name: 워크플로우의 이름
- on : 이 워크플로우가 어떤 이벤트에 의해 트리거되는지를 지정하는 부분. 여기서는 push 이벤트와 pull request 이벤트가 발생할 때 마다 이 워크 플로우가 실행되도록 설정되어있다.
- jobs : 실행할 작업들을 지정. 
    - build
        - 여기서는 `build`라는 이름의 작업 하나만 정의했지만, 여러 개의 작업을 정의하고 서로 종속성 관리를 할 수 있다. 각 작업은 독립적인 가상 환경에서 실행되고, 서로 다른 운영체제에서 실행될 수 있다.
    - runs-on : 깃헙액션 워크플로우가 어떤 환경에서 실행 될지 지정하는 부분.
        - `ubuntu-latest`라고 지정하면 워크플로우는 가장 최신버전의 Ubuntu 가상환경에서 실행된다.
        - 그 외에도 `windows-latest`, `macos-latest` 등 다양한 환경을 지정할 수 있다.

    - steps: steps는 특정 작업(job)을 구성하는 여러 동작(step)들을 나열하는 부분이다. 이들은 순차적으로 실행된다. 각 단계는 깃허브 액션(예: actions/checkout@v2)을 사용하거나 직접 스크립트를 실행(run 사용)하는 방식으로 구성된다.
        - uses : 특정 깃허브 액션을 사용하겠다고 지정하는 부분이다. 이는 액션의 레포지토리 이름 또는 Docker 이미지를 가리킨다. 위 코드의 `actions/checkout@v2`는 깃허브에서 제공하는 액션 중 하나인데, 워크플로우가 실행되는 가상 환경에 코드 레포지토리를 체크아웃하는 역할을 한다.    
        - name : 이 부분은 해당 단계(step)에 대해 설명하는 부분이다. 이 이름은 워크 플로우의 로그에서 보여진다. 또한 어떤 동작이 수행되는지 쉽게 이해할 수 있도록 돕는 부분이다. 
        - run : 이 부분은 특정 스크립트나 명령어를 실행하겠다는 것을 지정하는 부분이다. 이는 워크플로우 가상환경의 shell에서 직접 실행된다. 여기서는 echo Hello, world! 라는 간단한 명령어가 실행되도록 지정되어있다.


    - 각 작업은 steps에서 세부 동작들을 정의한다. 
    - 첫 번째 step은 깃허브에서 제공하는 actions/checkout@v2 액션을 사용하여 레포지토리를 체크아웃합니다.
- run : 실행할 커맨드를 지정한다. 여기서는 간단하게 "Hello, world!"를 출력하는 echo 커맨드를 실행합니다.

이 부분들을 모두 적용하여 주석처리해보면 아래와 같다.


```
# 워크플로우의 이름을 설정하는 부분. 이 이름은 GitHub Actions UI에서 보여진다.
name: CI 

# 이 워크플로우가 어떤 이벤트에 의해 실행될지를 정의하는 부분.
# 여기서는 push 이벤트나 pull_request 이벤트가 발생할 때마다 이 워크플로우가 실행되도록 설정하였습니다.
on: [push, pull_request] 

# 여기에서 워크플로우의 작업들을 정의하는 부분.
jobs:
  
  # 이는 "build"라는 이름의 작업을 정의하는 부분.
  build: 
    
    # 이 작업은 Ubuntu의 최신 버전 가상 환경에서 실행됩니다.
    runs-on: ubuntu-latest 

    # 작업에 포함된 단계들을 정의하는 부분.
    steps:
      
    # uses는 특정 깃허브 액션을 사용하겠다고 지정하는 부분.
    # 첫 번째 단계에서는 actions/checkout@v2 액션을 사용하여 워크플로우가 실행되는 가상 환경에 레포지토리를 체크아웃합니다.
    - uses: actions/checkout@v2 

    # 두 번째 단계의 이름을 정의하는 부분. 이 이름은 GitHub Actions UI에서 보여진다.
    - name: Run a one-line script
      
      
      # run은 실행할 커맨드를 지정하는 부분. 
      # 이 단계에서는 'echo Hello, world!'라는 명령어를 실행한다. 이 명령어는 터미널에 'Hello, world!'를 출력한다.
      run: echo Hello, world! 
```


## 워크플로우 커밋 및 푸시
일반적인 커밋과 푸시를 진행한다.

```
git add .
git commit -m "new commit"
git push
```

이제 레포지토리의 Actions 페이지를 눌러 확인해보자

## 적용한 레포지토리
[레포지토리 링크](https://github.com/isGeekCode/githubActionTutorial) 




## 세부동작 

위 코드를 커밋하면 Actions에서는 해당 커밋에 대하여 워크플로우가 실행되기 시작한다.

- Set up job
- Build `<uses에 사용한다고 표시한 gitAction 내용>`
- `<Steps 의 세부 Step에 대한 name이 표시>`
- Complete job

<img width="300" alt="스크린샷 2023-07-21 오전 9 37 22" src="https://github.com/isGeekCode/githubActionTutorial/assets/76529148/65db4f10-5b82-4864-ad73-f6e360e90594">



## History
- 230721 : 초안 작성
