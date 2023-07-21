# CI/CD - GitHub Action 사용하기3 : 실행할 스크립트 짜보기


yaml파일의 바디 부분에서 각 step을 구현하다보면 스크립트를 짜야하는 경우가 생긴다.


아래 스크립트를 보자
```
    - name: Generate directory list and update README
      run: |
        echo "# Directory List" > README.md
        for d in */; do
          echo "- $d" >> README.md
        done

```
- `echo "# Directory List" > README.md`
    - 이 명령은 README.md 파일을 생성하고 (또는 이미 존재한다면 내용을 덮어쓰고) 그 첫 번째 라인에 "Directory List"라는 헤더를 작성한다.
- `for d in */; do echo "- $d" >> README.md; done`
    - 이 부분은 현재 디렉토리에 있는 모든 하위 디렉토리를 리스트업한다. 각 디렉토리의 이름은 하이픈`-`을 앞에 붙여서 README.md 파일에 추가한다 
    - (기존 내용은 유지하면서 새로운 내용을 추가하기 위해 >> 연산자를 사용). 디렉토리가 없으면 아무 것도 하지 않는다.
- `*/`
    - 여기서 `*/`는 모든 하위 디렉토리를 의미하는 와일드카드 패턴이다. 
    - 이것은 현재 디렉토리에 있는 모든 하위 디렉토리에 대해 반복하라는 의미로 사용했다.
    - 단일 별표`*`는 어떠한 문자들도 가능하다는 의미이며, 마지막의 슬래시`/`는 디렉토리만을 의미한다.
- ; do
    - for loop가 시작하는 것을 나타내는 키워드다. 
    - 이 키워드는 각 디렉토리에 대해 실행할 명령어 블록의 시작을 표시한다.





이 내용을 몇가지 수정해보자


```
    - name: Generate directory list and update README
      run: |
        echo "# Directory List" > README.md
        for d in $(ls -d */); do
          if [[ $d != .* ]]; then
            echo "- $d" >> README.md
          fi
        done
```
- `for d in $(ls -d */); do`
    - 이 부분은 현재 디렉토리의 모든 하위 디렉토리를 순회하는 for loop를 시작한다. 
    - `$(ls -d */)`는 현재 디렉토리의 모든 하위 디렉토리를 나열하는 ls 명령을 실행하고 그 결과를 반환한다.

- `if [[ $d != .* ]]; then`
    - 이 부분은 현재 디렉토리의 이름이 `.`로 시작하는지 검사하는 if문이다.
    - 만약 디렉토리 이름이 `.`로 시작한다면, 이 디렉토리는 숨겨진 디렉토리라는 것을 의미하며, 이 경우 이 디렉토리는 출력에서 제외된다.
- `fi`와 `done`
    - 이 부분은 if문과 for loop를 종료합니다.


    
## History
- 230721 : 초안 작성
