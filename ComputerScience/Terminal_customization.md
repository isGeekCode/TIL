## 터미널 - 커스텀 함수 및 환경변수 설정하기

### 환경변수 만들기
`vim ~/.zshrc`으로 편집 시작

예를 들어 `"/Users/<NyName>/Documents/TIL"` 위치에 있는 경로 자체를 변수로 만든다면 아래와 같이 사용한다.  

```
export TIL_DIR="/Users/<NyName>/Documents/TIL"
```

이렇게 하면 `TIL_DIR`이라는 변수를 생성한 것이다.  


필요에 따라 이제 함수를 만들어 사용할 수 있다.

<br><br>

### 폴더이동을 하기 위한 함수


zshrc에서 아래와 같이 입력한다. 


```
function cdtil() {
    cd "$TIL_DIR"
}

```

이후 `source ~/.zshrc`를 통해  변경사항을 저장하고 터미널에서 `cdtil` 명령어로 실행할 수 있다.  

<br><br>

### m1인경우

아래와 같이 zshrc에 입력한다.

경로를 입력한다. 
이때 원하는 폴더를 그냥 드래그 하자. 이러면 끝!!

```swift
alias cdtil='cd /Users/.... /MyProject/Profile/TIL'
```

 
 
## HISTORY

- 240214 : 터미널에서 커스텀 함수 만들어 사용하기

