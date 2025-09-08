# Integrity - APN 인증키(.p8) 발급받기
푸시 서비스를 이용하기위해서 애플에서는 기본적으로 Apple 서버로부터 인증을 받아야한다.  
이때 필요한 것이 APN 인증키이다.  

<br><br>

### Apple Developer Member Center 사이트로 한다.
- [Apple Developer](https://developer.apple.com/account)  

### 프로그램 리소스 > Certificates, Identifiers & Profiles > 키 메뉴를 선택한다
<img width="800" alt="스크린샷 2024-01-29 오후 2 19 42" src="https://github.com/isGeekCode/TIL/assets/76529148/f086df7c-2cf8-4695-90f2-d60cdfa85131">

### Keys 메뉴로 이동 후 인증 키를 발급합니다. 인증 키는 최대 2개까지 생성할 수 있다.
<img width="800" alt="스크린샷 2024-01-29 오후 2 19 49" src="https://github.com/isGeekCode/TIL/assets/76529148/5cf4d825-8062-43ab-8cfa-eb8f78ba43f3">

<br><br>

## 이미 있는지 확인하기

프로젝트에 따라 기존에 이미 생성되어있을 가능성도 있다. 
최초 생성이면 아래를 참고하자.  

<br><br>

### 기존에 생성되어있는 모습

아래 그림을 보자.  

이미 생성되어있는 키를 사용하려고 해도 이게 내가 원하는 건지 알수가 없다.  
위에서 말한 것처럼 인증키는 최대 2개까지 생성할 수 있다.  

‼️‼️주의할 점‼️‼️ 내가 원하는 프로젝트가 속한 팀인지 한 번 더 확인할 것!!

아래 그림을 보면 여러 키가 있는데, 다른키에서 푸시용 APN 서비스를 이용하는 지 확인해보자.  

1. 만약 다른 키에서 이미 한개를 사용하고 있다면 ->  이 키를 사용하거나 새로 하나 생성할 수 있다.   
2. 만약 두 개의 키에서 사용하고 있다면 -> 기존의 키를 이용해야만 한다.  
<img width="800" alt="스크린샷 2024-01-29 오후 2 01 43" src="https://github.com/isGeekCode/TIL/assets/76529148/3f94f1a0-6d57-4afb-8e9f-3acdaf2bf48a">

키 목록을 보면 몇개의 서비스를 이용하는 지 밖에 알 수 없기 때문에 눌러봐야한다.  

<br><br>

### 키를 살펴보는 방법
1번 키를 한번 눌러봤다.  
<img width="800" alt="스크린샷 2024-01-29 오후 2 05 21" src="https://github.com/isGeekCode/TIL/assets/76529148/d372e0fa-6deb-46b8-ae05-33fca774b413">

- NAME : 단숝히 구분용이다.
- KEY ID : 키의 고유한 값이기 때문에 이걸 통해 구별할 수 있다.  
- SERVICES : 사용하는 서비스를 나타낸다.  

이 키는 현재 한개의 서비스를 이용하고 있고, 애플 로그인 서비스가 적용되어있다.   

<br><br>

그러면 다음 2번키도 살펴보자.  
<img width="800" alt="스크린샷 2024-01-29 오후 2 05 34" src="https://github.com/isGeekCode/TIL/assets/76529148/821f9f28-3e03-43c4-86a2-8f77f406d767">

이 키는 현재 두 개의 서비스를 이용하고 있고, APNs(푸시)서비스와 애플로그인 서비스를 적용하고 있다. 

우리가 필요한건 두번째 키를 사용해야하는 것이다.  만약 단독으로 사용하고 싶다면 아래 최초 생성하기를 이용하자. 

<br><br>

### 팀에게 인증서 요청하기
위에서 살펴본 이 키에 있어 엄청나게 중요한점이 있다.  
바로 생성한 사람만이 다시 받을 수 있다는 것이다.  

그렇기 때문에 처음 생성후 다운 받은 인증서는 고이 모셔두는게 좋다.  

그래서 보통은 저 인증키의 KEY ID를 가지고 내가 속한 팀에 공유하여 해당 KEY ID에 해당하는 p8 파일을 공유받으면 된다.  

<br><br>

## 최초생성하기



### Key Name을 입력하고, Apple Push notifications service (APNs)를 활성화한다.
<img width="800" alt="스크린샷 2024-01-29 오후 2 19 58" src="https://github.com/isGeekCode/TIL/assets/76529148/6a12af32-63e9-44d5-af68-223f51601bcb">

### Register를 누르면 인증 키가 발급 된다.
<img width="800" alt="스크린샷 2024-01-29 오후 2 20 05" src="https://github.com/isGeekCode/TIL/assets/76529148/3eba51e5-21f3-4757-853b-134a35a321d5">

### Key ID를 확인하고 다운로드 한다.
<img width="800" alt="스크린샷 2024-01-29 오후 2 20 13" src="https://github.com/isGeekCode/TIL/assets/76529148/711d2cf3-fe71-4930-80d3-2eb6b746c054">

생성한 사람외에는 다운로드를 받을 수 없으니, 다운받아서 보관하자.  

<br><br>



