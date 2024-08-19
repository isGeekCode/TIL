# 비동기처리가 필요한 이유

대부분의 앱들의 정보에 들어갈 이미지나 텍스트들은 전부 앱에서 갖고있는것이 아니라
서버로부터 가져와서 테이블 뷰를 표시하게 되는 것이다.   

### 이슈
만약 비동기처리를 하지 않는 경우, 스크롤을 할때마다 뚝뚝 끊기는 현상이 발생한다. 

이런 현상은 왜 일어날까???

아이폰의 화면 주사율 60Hz -> 아이폰은 1초에 60번 화면을 다시 그린다.  

어떠한 메커니즘에 의해 화면을 다시 그리는 것이다. 

-> 비동기처리를 하지않으면 해당 메커니즘이 제대로 동작되지못하는 것이다. 




## 코어(Core) / 스레드(Thread) / 클럭(Clock)
### 1 Core 1 Thread
예전의 컴퓨터 한개의 CPU 가 있고 직접적으로 일하는 스레드가 1개
- 1.0 GHz : 1초에 10억번 작업
-> 2.0 GHz : 1초에 20억번 작업
-> 3.0 GHz : 1초에 30억번 작업
물리적인 속도를 높이려고 진동(클럭)의 속도를 높임
-> 부작용 : 발열 / 배터리문제
그래서 이후 40억번 작업 가능한 CPU는 없음

### 2 Core 2 Thread
한 개에서 하던 작업을 나눠서 할 수 있게 됨
- 3.0 GHz
- 3.0 GHz

### 4 Core 4 Thread
코어를 늘리는 작업이 진행됨
- Core1
    - Thread1
- Core2
    - Thread1
- Core3
    - Thread1
- Core4
    - Thread1

- 4개 -> 6개 -> 8개 -> 10개



### 4 Core 8 Thread
하이퍼쓰레딩 기술로 1코어에 2개의 쓰레드가 가능해짐
- Core1
    - Thread1
    - Thread2
- Core2
    - Thread1
    - Thread2
- Core3
    - Thread1
    - Thread2
- Core4
    - Thread1
    - Thread2


원래는 쓰레드를 늘리는 기술이 먼저 시작되었음

현대의 PC
- 6코어 12쓰레드 2.6GHz -> 연산 장치 12개
- 8코어 16쓰레드 2.3GHz -> 연산 장치 16개

쓰레드만 이해하면 됨

## 소프트웨어적인 Thread 
쓰레드는 NSThread라고 불리는 객체

| - |  - | - | - | - |
| :--: | :--: |  :--: |  :--: |  :--: |
| Main Thread | Task1 | Task2 | Task3 | Task4 |
| Thread 2 | - | - | - | - |
| Thread 3 | - | - | - | - |
| Thread 4 | - | - | - | - |

빨리 종료되는 일은 1번 쓰레드에서만 처리해도 문제가 되지않는다.  

만약 Task1이 네트워크 작업을 통해 오래걸리게 된다면 다른 쓰레드를 사용하는 것이다.  

<img width="600" alt="스크린샷 2024-08-19 오후 8 32 50" src="https://github.com/user-attachments/assets/71600c7b-0f5e-48e8-b05b-e91915a8980c">
<출처 iOS앱 프로그래밍 가이드>


- main() : UIKit이 관리하여 UIApplicationMain을 생성
- UIApplicationMain() : 앱 전체를 관리하는 객체 생성
- Load mainUI : 화면 준비
- Event Loop(RunLoop) : 이벤트를 처리하기위한 무한 반복문을 실행
    - 특정한 조건에 실행처리됨
    
<img width="600" alt="스크린샷 2024-08-19 오후 8 40 58" src="https://github.com/user-attachments/assets/ead6e859-5f01-4e2b-8c02-77e1a7ac19a0">

메인 런루프 에서 특정 이벤트 들을 반복처리
- 이벤트 : 화면터치, 핀치 줌 , 화면 돌리기 등등
