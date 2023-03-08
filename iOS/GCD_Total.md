# GCD 톺아보기

## 목차
- GCD란 무엇인가요?
- GCD에서 사용되는 용어들
- GCD의 기본 개념과 동작 방식
- GCD의 큐 종류: Serial Queue와 Concurrent Queue
- GCD의 주요 API: dispatch_queue_t, dispatch_async, dispatch_sync
- GCD의 그룹 기능: dispatch_group_t, dispatch_group_async, dispatch_group_notify
- DispatchQueue 클래스: 큐 생성 및 비동기 작업 처리
- DispatchGroup 클래스: 그룹으로 묶어서 작업 관리
- DispatchSemaphore 클래스: 작업 실행 허용 개수 제한
    - dispatch_semaphore_t, dispatch_semaphore_wait, dispatch_semaphore_signal
- DispatchSource 클래스: 이벤트 모니터링 및 작업 실행
- DispatchBarrier 함수: 큐 내 작업 실행 순서 제어
    - dispatch_barrier_async, dispatch_barrier_sync
- GCD의 타이머 기능: dispatch_source_t, dispatch_source_create, dispatch_source_set_timer
- dispatchWorkItem 클래스: 작업 실행과 취소, 일시 중지, 재개, 결과값 가져오기 등
[TIL: GCD - dispatchWorkItem 정리내용](https://github.com/isGeekCode/TIL/commit/b64f10055c31d81e6249fa5f57a9f43a2b909816?short_path=ce70c04#diff-ce70c046c202de3bdcd893c84fae959478311b24ff7553d386fd19e12be98a81)

## 주요 객체
DispatchQueue 클래스: GCD 큐를 나타내며, 비동기 작업을 처리하는 데 사용된다.
DispatchGroup 클래스: 여러 개의 작업을 그룹으로 묶어서 관리하고, 모든 작업이 완료될 때까지 기다릴 수 있다.
DispatchSemaphore 클래스: 특정 작업의 실행 허용 개수를 제한하는 데 사용된다.
DispatchSource 클래스: 타이머나 파일 디스크립터 등의 이벤트를 모니터링하고, 이벤트가 발생할 때마다 작업을 실행할 수 있다.
DispatchBarrier 함수: 큐 내 작업의 실행 순서를 제어하는 데 사용된다.

