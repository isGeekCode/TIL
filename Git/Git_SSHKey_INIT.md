# GitLab SSH키 생성하기

### 기존에 SSH 키가 존재하는지 체크
```
$ cat ~/.ssh/id_rsa.pub
/*
cat: /Users/유저이름폴더명/.ssh/id_rsa.pub: No such file or directory
*/
```

### SSH 키 생성하기
```
$ ssh-keygen
/*
Generating public/private rsa key pair.
//해당 위치에 생성할지 여부
Enter file in which to save the key (/Users/유저이름폴더명/.ssh/id_rsa):

//비밀번호 설정 - 그냥 엔터하는게 편하다
Enter passphrase (empty for no passphrase):
//비밀번호 확인 - 위와 동일
Enter same passphrase again:

// 생성한 SSH 정보 (실제값이 아닌 가상의 값 입니다.)
Your identification has been saved in /Users/유저이름폴더명/.ssh/id_rsa
Your public key has been saved in /Users/유저이름폴더명/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:21+ncDs5sP51n1+ncDs5sP51+ncDs5 유저이름@DESKTOP-072KOI6.home.e-kmall.com
The key's randomart image is:
+---[RSA 3072]----+
|     ..= o*.=    |
|        .o  .    |
|     ..= o*.=    |
|      Eo =o.o + o|
|     ..= o*.=    |
|        .o  .    |
|        .o  .    |
|        .o  .    |
|      ..=oo*..   |
+----[SHA256]-----+
*/

```

### 생성한 SSH 키 확인하기
```
$ cat ~/.ssh/id_rsa.pub
/*
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAA.....
*/
```

### 식별정보를 포함하여 암호화한 SSH키 생성
- `-t rsa`: RSA 암호화 알고리즘을 사용하여 키 쌍을 생성한다.
- `-C "GitLab"`: 주석(comment)으로 "GitLab"을 키에 포함시킨다. 주석은 생성된 키에 대한 식별 정보를 추가하는 데 사용된다.
- `-b 4096`: 4096 비트의 키를 생성한다. 비트 수가 높을수록 보안 수준이 높아진다.
```
// 키생성
ssh-keygen -t rsa -C "GitLab" -b 4096
/*

Generating public/private rsa key pair.
// 해당위치에 SSH키를 생성할지 여부
Enter file in which to save the key (/Users/유저이름폴더명/.ssh/id_rsa):

// 해당위치에 이미 SSH키가 있는데 덮어쓸지 여부
/Users/유저이름폴더명/.ssh/id_rsa already exists.
Overwrite (y/n)? 
$ y

//비밀번호 설정 - 그냥 엔터하는게 편하다
Enter passphrase (empty for no passphrase):
//비밀번호 확인 - 위와 동일
Enter same passphrase again:

// 생성 결과 메세지
Your identification has been saved in /Users/유저이름폴더명/.ssh/id_rsa
Your public key has been saved in /Users/유저이름폴더명/.ssh/id_rsa.pub

// 생성한 SSH 정보 (실제값이 아닌 가상의 값 입니다.)
The key fingerprint is:
SHA256:21+ncDs5sP51n1+ncDs5sP51+ncDs5 유저이름@DESKTOP-072KOI6.home.e-kmall.com
The key's randomart image is:
+---[RSA 3072]----+
|     ..= o*.=    |
|        .o  .    |
|     ..= o*.=    |
|      Eo =o.o + o|
|     ..= o*.=    |
|        .o  .    |
|        .o  .    |
|        .o  .    |
|      ..=oo*..   |
+----[SHA256]-----+
*/
```

### 생성한 SSH 키 확인하기
```
$ cat ~/.ssh/id_rsa.pub
/*
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAA..... GitLab
*/
```
## GitLab에 반영

- 아래 페이지 진입
    - GitLab웹페이지 - Setting - SSH Keys
- Key 부분에 붙여넣기 (자동으로 Title은 입력됨)
- Add Key 클릭

## History
- 230612 : 초안작성
