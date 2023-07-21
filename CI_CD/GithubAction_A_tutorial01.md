# CI/CD - GitHub Action 사용하기2 : on 섹션 수정하기


yaml파일의 헤더부분에는 아래 두 가지가 들어있다.
- name
- on


이때 name은 워크플로우 자체의 이름을 의미한다.

## On
이 워크플로우가 어떤 이벤트에 의해 실행될지를 지정하는 부분이다. 

여러가지 예시를 통해 알아보자


```
#  push 이벤트에 의해 실행.
on: [push]

# 푸시(push) 이벤트와 풀 리퀘스트(pull_request) 이벤트가 발생할 때마다 이 워크플로우를 실행하도록 설정
on: [push, pull_request]
```

그밖에도

- schedule
    - 이 이벤트는 워크플로우를 지정된 일정에 따라 실행할 수 있다. 
    - 예를 들어, 매일 밤에 테스트를 실행하거나 매주 월요일 오전에 배포를 수행할 수 있다.

- workflow_dispatch
    - 이 이벤트는 워크플로우를 수동으로 시작할 수 있다. 
    - 이를 통해 어느 때든지 워크플로우를 실행할 수 있다.

- release
    - 이 이벤트는 GitHub에서 릴리스가 생성되거나 수정될 때 워크플로우를 실행할 수 있다.

- issue_comment
    - 이 이벤트는 GitHub 이슈에 코멘트가 작성될 때 워크플로우를 실행할 수 있다.


## 이벤트 발생 브랜치 세팅
세부적으로 명시한 이벤트가 발생할 브랜치를 지정할 수도 있다.

```
on: # 이 워크플로우가 어떤 이벤트에 응답할 것인지 정의합니다.
  push: # 'push' 이벤트에 워크플로우를 실행하도록 설정합니다.
    branches: # 'push' 이벤트가 발생하는 브랜치를 지정합니다.
      - main # 'main' 브랜치에 'push' 이벤트가 발생할 때 워크플로우를 실행하도록 설정합니다.
```

## 워크플로우가 무시할 파일 경로하기
```
on: # 이 워크플로우가 어떤 이벤트에 응답할 것인지 정의합니다.
  push: # 'push' 이벤트에 워크플로우를 실행하도록 설정합니다.
    paths-ignore: # 워크플로우가 무시할 파일 경로를 지정합니다.
      - README.md # 'README.md' 파일에 대한 변경 사항은 워크플로우를 실행시키지 않습니다.
```


이 외에도 많은 이벤트들이 있다. 전체 목록은 [GitHub Actions 공식 문서](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows)에서 확인할 수 있다. 

일단 나와있는걸 다 적어보면 이런게 있다. 이런 트리거 들이 있으니 검색해서 사용해보자

- branch_protection_rule
- check_run
- check_suite
- create
- delete
- deployment
- deployment_status
- discussion
- discussion_comment
- fork
- gollum
- issue_comment
- issues
- label
- merge_group
- milestone
- page_build
- project
- project_card
- project_column
- public
- pull_request
- pull_request_comment (use issue_comment)
- pull_request_review
- pull_request_review_comment
- pull_request_target
- push
- registry_package
- release
- repository_dispatch
- schedule
- status
- watch
- workflow_call
- workflow_dispatch
- workflow_run



## History
- 230721 : 초안 작성
