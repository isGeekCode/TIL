# Git - 현재 깃폴더에 연동한 username 확인하고 변경하기
git의 username은 해당 계정의 아이디, identifier와 같다. 

이걸 통해 깃에서 유저를 캐치할 수 있다.
기본적으로 깃허브, 깃랩, bitBucket 등등의 서비스에서는 가입시 세팅할 수 있고 이후로도 변경이 가능하다. 

## 세팅되어있는 git 유저정보 확인하기
```
git config --list
```

### username 확인하기

현재 깃에 연결된 username을 확인하려면 아래와 같이 터미널에 입력한다.
```
git config --global user.name
// isGeekCode
```
### username 변경하기

만약 변경하고 싶다면 아래와 같이 입력한다.
```
git config --global user.name "Your New Name"
```


### user email 확인하기
현재 깃에 연결된 user.eamil을 확인 하려면 아래와 같이 입력한다.
```
git config --global user.email 
// email주소 출력
```


### username 변경하기
```
git config --global user.name "yournewemail@example.com"
```

## username과 email 한꺼번에 바꾸기
```
git config --global user.name "Your New Name" && git config --global user.email "yournewemail@example.com"
```





