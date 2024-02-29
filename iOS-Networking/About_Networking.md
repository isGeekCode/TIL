# 네트워크 통신의 이해


- 클라이언트 → **[ 내 컴퓨터 / 아이폰 ]**
- internet → **[ 웹 or www ]**
  - TCP/IP : 인터넷에 관련된 다양한 프로토콜의 집합 → 약속의 집합
    - HTTP
    - IP
    - FTP
    - UDP
    - TCP
    - IEEE 802.3
- 서버 → **[ 어딘가의 컴퓨터 ]**


<br>

### www를 구성하는 기술
- HTML : HyperText Markup Language
- HTTP : HyperText Transfer Protocol
- URL : Uniform Resource Locator

<br>

## HTTP
> 처음엔 하이퍼문서를 전송하는 것에서 시작  

현재는 이미지 / 영상 / 음성 / 파일 / JSON 등 모든 형태의 데이터를 전송 가능한 약속으로 변화

**즉, 인터넷의 모든 것은 HTTP로 이루어져 있다.**  


<br>

- HTTP 0.9
- HTTP 1.0
- HTTP 1.1 : 대부분의 기능이 내장 되어있음
- HTTP 2.0 3.0 : 단순한 성능 개선

<br>


## 네트워킹의 흐름
- App
  - 애플리케이션 : HTTP → Request
- OS
  - 트랜스포트 : TCP → 조각 / Port 붙임 
  - 인터넷 : IP → 주소
- LAN
  - 링크 : 네트워크 → MAC 주소 추가 (하드웨어 주소)





### 클라이언트 측
- HTTP 의 Request
  - 일종의 편지지이고, 정해진 형식이 있다.  

- TCP
  - OS에서는 이 Request를 조각조각 분리하고, 앱마다 다른 포트를 할당한다.  

- IP
  - 기존의 내용을 봉투에 넣고 주소를 쓴다. 

- Mac주소
  - 각각의 봉투를 택배 상자에 넣고 보낸다.  
  - 랜카드 하드웨어 주소를 찾아 전송


### 서버 측
서버에서는 역순으로 동작

- Mac주소
- IP
- TCP
- HTTP
  - 클라이언트 측으로 받은 Request를 가지고 Response를 전송


다시 HTTP - TCP - IP - Mac주소 순으로 Response를 전송



<br>

## 우리가 알아야하는 것은 HTTP

### HTTP 요청 메세지
- 시작라인 : 메소드 + 요청대상(경로) + HTTP버전
- 헤더필드 : HTTP에 필요한 모든 메타데이터
- Message Body : 실제 전송할 데이터 ( JSON / HTML / 이미지 / 영상 등)

```swift
GET /index.html HTTP /1.1
Host: wwww.naver.com
```

혹은

```swift
POST /form/entry HTTP /1.1   // 시작라인
Host: wwww.naver.com         // header 필드
Connection: Keep-alive
Content-Type: application/x-www-form-urlencoded
                            // 공백라인
name=sam&age=30            // 메세지 본문
```

### HTTP 응답 메세지
- 시작라인 : HTTP버전 + 상태코드 + 상태코드에 대한 문구
- 헤더필드 : HTTP에 필요한 모든 메타데이터
- Message Body : 실제 전송할 데이터 ( JSON / HTML / 이미지 / 영상 등)

```swift
HTTP /1.1 200 SUCCESS         // 시작라인
Date: Sun, 10 March 2022 10:30:14 GMT // header 필드
Content-Length:320
Content-Type: text/html
                            // 공백라인

<html>                      // 메세지 본문 
...
```

### 요청 메소드의 종류
10가지 넘게 있지만 실무로 사용하는 메서드
> **C** →  GET 
  - 조회 : 게시판 글 읽어오기 (데이터 표시)
> **R** → POST 
  - 등록 : 게시판 글쓰기 / 댓글달기
> **U** → PUT 
  - 데이터 대체(없으면 생성) : 게시글 수정
> **D**→ DELETE 
  - 삭제 : 게시물 삭제
> PATCH : 부분 변경

### 응답 상태 코드
> 1xx : Intormational

> 🍊 2xx : Success
  - 정상 처리 
> 3xx : Redirection
  - Request를 완료하기위해 추가 동작이 필요한 경우 
> 🍊 4xx : Client Error
  - 내 컴퓨터에서의 에러 ( 잘못된 요청 )
> 🍊 5xx : Server Error
  - 서버 내부의 문제

<br>

## API
- API의 종류 
  - 서버랑 통신하기 위한 수단
  - 기존 문법에 구현된 print같은 메서드 

##  Request
### GET메소드
Request는 query로 이루어 진다. 

```
https://www.google.com:443/search?q=swift&hl=ko
```

- 요청하기 위한 주소
  - `https://www.google.com:443/search`
    - 전체주소
  - `:443`
    - 해당 컴퓨터의 앱을 구분하기 위한 포트  
        → 기본값이 생략된 앱이 많아서 자주 생략됨
  - `/search`
    - 경로
- 쿼리파라미터
  - `?`로 시작, `&`로 추가
  - `key=value` 형태
  - `?`q=swift`&`hl=ko
    - q=swift
    - hl=ko

<br>

## Response
> 앱에서 처리하는 데이터의 형태

- 예전 : XML
- 현재 : JSON
```
{
    "name" : "geekCode",
    "age" : 25,
    "address" : "Seoul, Mapo-gu",
    "hobby" : ["swim", "BasketBall"],
    "family" : {
        "#" : 2,
        "아버지" : "철수",
        "어머니" : "영희"
    }
}
```

<br>

## REST API
REST하게 API를 작성하다.
> API란 결국 상호간 정보를 교환하기위한 Interface  
→ 요청 방식에 대한 약속  
→ 어떤 주소 / 무엇을 요청 / 결과를 어떻게 줄지

<br>

### 소통이 어려운 형식
이렇게 SOAP한 방식도 통신은 가능하다. 
```
https://naver.com/1   // 상영중 영화 목록 요청 : GET
https://naver.com/2   // 내일 오픈 예정 영화 목록 : GET
https://naver.com/3   // 실시간 영화 관객 순위 : GET
https://naver.com/4   // 영화 예약 : POST

```
<br>

### REST한 형식의 API
어느정도 추측이 가능한 형식
```
https://naver.com/movieLists   
// 상영중 영화 목록 요청 : GET

https://naver.com/movilists?open=tomorrow   
// 내일 오픈 예정 영화 목록 : GET

https://naver.com/movie-reservation  
// 영화 예약 : POST
```

[💡 REST API가 뭔가요 (얄팍한 코딩사전)](https://www.youtube.com/watch?v=iOueE9AXDQQ)  
[💡 그런 REST API로 괜찮은가 (naver d2)](https://www.youtube.com/watch?v=RP_f5dMoHFc)
