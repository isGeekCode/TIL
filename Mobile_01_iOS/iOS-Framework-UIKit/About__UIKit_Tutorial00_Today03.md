# [iOS App Dev Tutorials] UIKit - Today앱 만들기(3) : Displaying cell info

<br>

<img width="600" alt="스크린샷 2023-10-30 오전 9 34 03" src="https://github.com/isGeekCode/isGeekCode/assets/76529148/6d4a3c6d-e20b-4d9e-80a4-3262d0fa3a98">

<br><br> 


# Displaying cell info: 셀 정보 표시하기

Today앱에서는 나열된 셀에 reminder 데이터가 세팅된 CollectionView를 사용한다.  

이 튜토리얼에서는 각 reminder에 대한 정보를 보여줄 cell 템플릿을 표시할 collection Cell을 디자인해보자.
이 셀을 언제 표시할지, 그리고 어떻게 표시할지는 시스템을 통해 결정한다. 


<br><br>


## Section 1. Format the date and time

### 날짜 및 시간 형식 지정

<img width="400" alt="스크린샷 2023-10-30 오전 9 34 03" src="https://github.com/isGeekCode/isGeekCode/assets/76529148/56c8148b-6373-448a-a9b0-8cccd23a4812">

reminder(미리알림)의 날짜와 시간은 이 앱의 사용자에게 표시될 중요한 property들이다.  

그러나 날짜와 시간은 문화, 지리, 언어마다 다르게 표기된다.  

이번 Section에서 Foundation 프레임워크의 date-formatting API들을 사용하여 모든 사용자의 Locale에 대한 정확한 날짜 및 시간 정보를 표시해보자.  

<br><br>

- 기존에 생성했던 Models 폴더에 `Data+Today.swift`라는 파일을 생성하자. 
- Date 구조체에 extension 한다.
- `var dayAndTimeText: String {}` 라는 문자열 속성을 만들자.
    - String타입이기 때문에 { } 안에서 String을 반환할 때까지 컴파일러는 오류를 표시한다.
- `formatted(date:time:)` 메서드를 이용해 문자열을 만들고 `timeText`라는 상수에 넣는다.
    - 시스템은  현재 Locale에 대한 날짜와 시간을 기본스타일을 사용해 문자열로 반환한다.  
    -  Pass를 의미하는 .omitted를 date 스타일로 세팅하면 오직 시간만 표기하는 문자열을 생성한다.  
- 


## Section 2. Organize view controllers

### 뷰 컨트롤러 구성




<img width="400" alt="스크린샷 2023-10-30 오전 9 34 03" src="https://github.com/isGeekCode/isGeekCode/assets/76529148/2ba12fa3-7265-44dc-84ee-ed3a865d1970">




## Section 3. Change the cell background color

### 색 배경색 설정

<img width="400" alt="스크린샷 2023-10-30 오전 9 34 03" src="https://github.com/isGeekCode/isGeekCode/assets/76529148/2df88029-f540-4a95-9a93-dfe39ed39e7b">


## Section 4. Display the reminder complete status

### 알림 완료 상태 표시

<img width="400" alt="스크린샷 2023-10-30 오전 9 34 03" src="https://github.com/isGeekCode/isGeekCode/assets/76529148/3b3e71da-4842-4b51-8ee2-884d6a48444b">



## 문제


## 정답


## 여기서 익힐 수 있는 것




