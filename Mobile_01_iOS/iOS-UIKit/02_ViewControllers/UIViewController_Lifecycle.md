# UIViewController Life-cycle (뷰컨트롤러의 생명주기)
-[앱의 생명주기](https://github.com/isGeekCode/TIL/blob/main/iOS-Framework-UIKit/About_UIKit_003AppLifeCycle.md)

앱이 실행되면 OS에 의해 자동으로 호출되는 메서드들이 있다.  



- Life-Cycle Method
    - ViewDidLoad
    - (*)ViewWillAppear
    - ViewDidAppear
    - ViewWillDisAppear
    - (*)ViewDidDisappear

UIViewController에서 한번 ViewDidLoad를 통해 View가 Load되면 이후로는 화면전환시 따로 deinit하지 않는 이상은 (*)표시된 부분만 순환하여 실행된다. 아래 흐름도를 참고    

### LoadView()
뷰 컨트롤러의 view 프로퍼티가 nil인 경우에 호출된다.
이 메서드를 오버라이드하여 뷰 계층 구조를 직접 구성하거나, 스토리보드와 같은 외부 리소스에서 뷰를 로드할 수 있다.

### ViewDidLoad()
- 뷰 컨트롤러의 뷰가 처음으로 메모리에 로드된 후에 한번만 호출된다.
- 뷰의 초기화 및 설정 작업을 수행하기에 적합한 부분이다.
- 주로 뷰에 관련된 초기화 코드, 데이터 로딩, 네트워크 요청 등을 처리한다.

### viewWillAppear() 
뷰 컨트롤러의 뷰가 화면에 나타나기 직전에 호출된다.
화면이 나타나기 전에 필요한 준비 작업을 수행할 수 있다.
주로 애니메이션 효과, 뷰 업데이트, 데이터 리로드 등을 처리한다.

### viewDidAppear() 
뷰 컨트롤러의 뷰가 화면에 나타난 후에 호출된다.
화면이 나타난 후 추가적인 작업이 필요한 경우에 사용된다.
주로 애니메이션 시작, 타이머 시작, 외부 서비스 호출 등을 처리한다.

### viewWillDisAppear() 
뷰 컨트롤러의 뷰가 화면에서 사라지기 직전에 호출된다.
화면이 사라지기 전에 필요한 작업을 수행할 수 있다.
주로 애니메이션 효과, 데이터 저장, 네트워크 요청 종료 등을 처리한다.

### viewDidDisappear() 
뷰 컨트롤러의 뷰가 화면에서 사라진 후에 호출된다.
화면이 사라진 후 추가적인 작업이 필요한 경우에 사용된다.
주로 애니메이션 종료, 타이머 중지, 리소스 해제 등을 처리한다.

## 흐름도

아래는 개발자가 조작할 수 있는 부분만 나타낸 흐름도이다.
### 그림(1)  
  <img width="500" alt="img1 daumcdn-4" src="https://github.com/isGeekCode/TIL/assets/76529148/23d9c401-415f-4bca-93e3-744f06224a29">  

### 그림(2)  
  <img width="600" alt="1_jb1Y17gwQCRi2XCKy7_QHQ" src="https://github.com/isGeekCode/TIL/assets/76529148/73d9eb10-f7f8-409c-8ace-913b9c785f29">  
  
    
이렇게 위 두 그링은 iOS에서 정말 많이 등장하는 그림이다.   
추가로 아래는 주로 개발자가 다루는 생명주기 함수 외에 시스템적으로 실행하는 함수들을 보여주는 그림이다.  

### 그림(3)  
  <img width="600" alt="1_aaUDpKdPrqlqX_Hmd2jHJA" src="https://github.com/isGeekCode/TIL/assets/76529148/140998e1-8620-4328-a067-465fbdea375f">  
