# 프로그래밍에서 동기 비동기 개념에 대한 이해

동기와 비동기에 대해 들어가기 전에 스레드에 대해 먼저 이야기해보자.

## 스레드

PC 사양 중에 4코어 8스레드, 8코어 16스레드 라는 식의 말을 들어본 적이 있을 것이다.
<br>
스레드란 일을 하는 존재라고 생각해보자. 8스레드라면 일을 할 수 있는 존재가 8개, 16스레드라면 일을 할 수 있는 존재가 16개 라는 것이다. 
<br>
아이폰 11 Pro기준 6코어라면  일을 할 수 있는 스레드가 6개가 있다는 것이다. 
<br><br>

### 설명
Thread1이 존재한다.  아래와 같은 작업이 Thread1에 순서대로 존재한다고 생각해보자.
<br>
| Task |  내용  | 걸리는 시간(예시) |
| :--: | :--: |  :--: | 
| Task1 | - | 4 |
| Task2 | - | 3 |
| Task3 | - | 2 |
| Task4 | - | 1 |

하나 하나의 작업을 보면 걸리는 시간이 다르다.  
<br>
근데 통상적으로 일은 Thread1에서 처리하게 된다. 그러면 과부하가 생긴다.  
이걸 분산시켜서 처리를 하는 것이 동시성 프로그래밍이다. 
<br>
핸드폰에는 일을 하는 녀석이 사실 여러개가 있다.  
<br>
그렇다면 일을 다른 쓰레드로 보내서 분산 처리를 할 수 있다.  
<br>
이제 Task들을 Thread2, Thread3, Thread4 ... 다른 스레드로 보내버리는 것이다. 
<br>
이러한 내용들은 아래와 같은 순서대로 살펴보자. 

- Synchronous(동기) vs Asynchronous(비동기)
- Serial(직렬) vs Concurrent(동시)
- 동시성 (Concurrency) 프로그래밍이 필요한 이유는?

<br><br><br>

## Synchronous(동기) vs Asynchronous(비동기)

아래와 같이 Thread1에 Task가 몰려있다고 생각해보자. 

| - |  - | - | - | - |
| :--: | :--: |  :--: |  :--: |  :--: |
| Thread 1 | Task1 | Task2 | Task3 | Task4 |
| Thread 2 | - | - | - | - |
| Thread 3 | - | - | - | - |
| Thread 4 | - | - | - | - |
<br>

### 비동기처리

작업을 분산처리 할 때, 작업(Task)을 다른 스레드로 보내버리고, 보낸 시점에 바로 다음 작업을 진행하는 것을 말한다.  
이 때, 보낸 작업은 이제 신경쓰지 않는다.    
  <br>
  
  
| - |  - | - | - | - |
| :--: | :--: |  :--: |  :--: |  :--: |
| Thread 1 |     -     | Task2 | Task3 | Task4 |
|    -     | ↓↑ 즉시 리턴 | - | - | - |
| Thread 2 |   Task1   | - | - | - |
| Thread 3 | - | - | - | - |
| Thread 4 | - | - | - | - |

<br><br>
비동기 처리 후, 보내진 시점에 보낸 작업을 기다리지 않고, 다음 작업이 이어서 시작된다.  

| - |  - | - | - |
| :--: | :--: |  :--: |  :--: |
| Thread 1 | Task2 | Task3 | Task4 | 
| Thread 2 | Task1 | - | - | 
| Thread 3 | - | - | - |
| Thread 4 | - | - | - | 

<br><br>

작업을 처리하는 시간 자체가 오래걸린다고 가정해보자.
<br>
실제로 대부분의 작업중 네트워킹 때문에 오래걸리는 경우가 많다.  
<br>
이런 네트워크 처리같은 경우, 비동기 처리를 하는 것이다.  
<br>
이제 Thread1에선 그동안 다른 작업을 할 수 있는 것이다.  
`기다리지 않는다`
<br>
보내진 작업이 끝났는지 여부는 특수한 처리를 하면 알 수 있다.  


<br><br>

### 동기처리

| - |  - | - | - | - |
| :--: | :--: |  :--: |  :--: |  :--: |
| Thread 1 |     -     | Task2 | Task3 | Task4 |
|    -     | ↓ 동기 ↑  | - | - | - |
| Thread 2 |   Task1   | - | - | - |
| Thread 3 | - | - | - | - |


<br><br>
동기 처리 후, 보내진 시점에서 해당 작업이 끝날 때까지 다음 작업을 시작하지않고 기다린다.  

| - |  - | - | - | - |
| :--: | :--: |  :--: |  :--: |  :--: |
| Thread 1 |  Block  | Task2 | Task3 | Task4 |
|    -     | ↓ 동기 ↑  | - | - | - |
| Thread 2 |   Task1   | - | - | - |
| Thread 3 | - | - | - | - |


<br><br>

만약 보내진 작업이 오래걸린다면, 그동안 다른 작업을 할 수 없다.  

<br>

### 정리
작업을 다른스레드에서 하도록 시킨후, 비동기 동기 차이

- 비동기 : 보낸 작업이 끝나길 기다리지않고, 다음 작업을 진행한다. 
    - 기다리지 않아도 다음 작업을 생성할 수 있다.
- 동기 : 보낸 작업이 끝나길 기다렸다가, 다음 작업을 진행한다. 
    - 기다렸다가 다음 작업을 생성할 수 있다. 

<br><br>

### 비동기라는 개념이 일반적으로 필요한 이유
대부분은 서버와의 통신(네트워크 작업)때문이다.  

<br><br><br>

## Serial(직렬)처리 vs Concurrent(동시)처리

아래 표를 보며 살펴보자.  
동일하게 이렇게 작업이 존재한다고 가정해보자.  

| - |  - | - | - | - |
| :--: | :--: |  :--: |  :--: |  :--: |
| Thread 1 | Task1 | Task2 | Task3 | Task4 |
| Thread 2 | - | - | - | - |
| Thread 3 | - | - | - | - |
| Thread 4 | - | - | - | - |

<br><br>

### Serial(직렬) 처리
직렬처리는 스레드에 있던 작업을 다른 하나의 스레드로만 보내는 것이 직렬처리이다.   

| - |  - | - | - | - |
| :--: | :--: |  :--: |  :--: |  :--: |
| Thread 1 | - | - | - | - |
| Thread 2 | Task1 | Task2 | Task3 | Task4 |
| Thread 3 | - | - | - | - |
| Thread 4 | - | - | - | - |

<br>

### Concurrent(동시) 처리
동시처리는 스레드에 있던 작업을 다른 여러개의 스레드로 보내는 것이다.  

| - |  - | - | - | - |
| :--: | :--: |  :--: |  :--: |  :--: |
| Thread 1 | - | - | - | - |
| Thread 2 | Task1 | - | - | - |
| Thread 3 | Task2 | Task4 | - | - |
| Thread 4 | Task3 | - | - | - |

이 때, 몇개의 스레드로 분산할 지는 시스템이 알아서 결정한다. 
중요한 것은 여러개의 스레드로 분산처리한다는 것이다.  

<br><br>

### 정리
(보통 메인에서) 분산처리 시킨 작업을  
- Serial(직렬)처리 : 다른 한 개의 스레드에서 처리
- Concurrent(동시)처리 : 다른 여러개의 스레드에서 처리

<br><br>

그렇다면 무조건 동시가 좋을 거 같은데??라고 생각 할 수 있지만 작업에 순서가 필요할 수도 있다.  
<br>
- Serial(직렬)처리 : 순서가 중요한 작업을 처리할 때 사용
- Concurrent(동시)처리 : 각자 독립적이지만 유사한 여러개의 작업을 처리할 때 사용  

<br>

상용 앱 중 대부분은 이미지와 텍스트 들을 서버에서 가져온다. 
각각의 이미지, 텍스트 자체를 다운받는 일은 동시 다발적으로 비슷한 일들을 처리하는 것이다.  
이럴 때, 동시처리를 한다.  

<br><br>

### 비동기와 동시란 말이 같은 말인가??
완전히 개념이 다른 말이다.  

<br>

## 왜 동시성 프로그래밍이 필요할까?
앱에 엄청나게 이미지를 다운로드하는 경우, 별다른 동시성 프로그래밍을 하지않으면, 
스크롤시 버벅거리는 현상이 발생한다.  

<br><br>
메인스레드에서 앱을 그리는 일도 하고 있는데, 이미지를 다운로드 하는 작업도 하고 있기 때문이다.  
<br>
결국 동시성을 다루는 것은 성능 / 반응 / 최적화를 다루는 것이다.  
<br>
이를 위해 GCD / Operation 이라는 것들을 사용한다.  
