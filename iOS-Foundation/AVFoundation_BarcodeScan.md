# AVFoundation - Barcode Scanner 구현하기

AVFoundation를 이용해 바코드 스캐너를 구현할 수 있다.


## 주요객체
- AVCaptureSession : 카메라 세션을 관리하는 객체
- AVCaptureVideoPreviewLayer : 카메라 영상을 표시하는 레이어


## 구현순서
- 1. AVCaptureSession 생성
- 2. 카메라 선택 및 입력 설정
    - 기본 카메라 호출 : `AVCaptureDevice.default(for: .video)`
    - `AVCaptureDeviceInput` 객체를 생성하여 가져온 카메라를 입력으로 설정
    - 카메라 입력을 AVCaptureSession에 추가 : `captureSession.addInput(input)`
- 3. 메타데이터 출력 설정
    - `AVCaptureMetadataOutput`객체를 생성하여 메타데이터 출력을 설정
    - 스캔결과를 처리할 메서드를 지정
    - `metadataObjectTypes`속성을 사용하여 인식할 바코드 유형을 세팅
- 4. 미리보기 레이어 설정 : `videoPreviewLayer`
    - `videoPreviewLayer.videoGravity`를 설정하여 비디오 스트림의 비율을 세팅
    - `videoPreviewLayer.frame`를 이용해 미리보기 레이어의 크기와 위치를 설정
    - 설정한 미리보기 레이어를 현재 뷰의 레이어에 추가
- 5. `AVCaptureSession`을 시작하여 카메라 캡쳐 시작
    - 이 작업은 global 쓰레드로 처리할것
    - 세션이 실행중인지 체크 : `captureSession.isRunning`
    - 카메라 캡처 시작 : `captureSession.startRunning()` 
- 4. UI업데이트 및 비동기처리
    - UI 업데이트를 Main쓰레드에서 처리

<br><br>

## 간단한 사용법

스레드 사용에 유의해야한다. 

```swift

class BarCodeScanViewController: UIViewController {
    
    // AVCaptureSession은 카메라 세션을 관리하는 객체
    var captureSession: AVCaptureSession?
    
    // AVCaptureVideoPreviewLayer는 카메라 영상을 표시하는 레이어
    var videoPreviewLayer: AVCaptureVideoPreviewLayer?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        setupCaptureSession()
    }

    func setupCaptureSession() {
        DispatchQueue.global(qos: .background).async {
            
            // AVCaptureSession 객체를 생성
            self.captureSession = AVCaptureSession()
            
            // 기기의 기본 카메라를 호출
            guard let captureDevice = AVCaptureDevice.default(for: .video) else { return }
            
            do {
                // 카메라 입력을 설정
                let input = try AVCaptureDeviceInput(device: captureDevice)
                self.captureSession?.addInput(input)
                
                // 메타데이터 출력을 설정
                let captureMetadataOutput = AVCaptureMetadataOutput()
                self.captureSession?.addOutput(captureMetadataOutput)
                
                // 메타데이터 출력의 델리게이트를 설정하고 인식할 바코드 유형을 설정
                captureMetadataOutput.setMetadataObjectsDelegate(self, queue: DispatchQueue.main)
                captureMetadataOutput.metadataObjectTypes = [
                    .qr, .upce, .code39, .code39Mod43, .ean13,
                    .ean8, .code93, .code128, .pdf417, .aztec,
                ]
                
                // 미리보기 레이어 생성
                self.setupVideoPreviewLayer()
                // 캡쳐 세션 시작
                self.startCaptureSession()
            } catch {
                print(error)
            }
        }
    }

    /// 미리보기 레이어 생성 메서드
    func setupVideoPreviewLayer() {
        DispatchQueue.main.async {
        
            guard let captureSession = self.captureSession else { return }

            // AVCaptureSession에서 나오는 비디오 스트림을 표시하기 위한 미리보기 레이어를 생성
            self.videoPreviewLayer = AVCaptureVideoPreviewLayer(session: self.captureSession)
            // 비디오 스트림의 비율 설정
            self.videoPreviewLayer.videoGravity = .resizeAspectFill
            // 미리보기 레이어의 프레임을 설정
            self.videoPreviewLayer.frame = self.view.layer.bounds
            // 현재 view의 레이어에 미리보기 레이어를 추가
            self.view.layer.addSublayer(self.videoPreviewLayer)
        }
    }

    /// 캡쳐 세션 시작 메서드
    func startCaptureSession() {
        DispatchQueue.global(qos: .background).async {
            if let captureSession = self.captureSession,
               !(captureSession.isRunning) {
                captureSession.startRunning()
            }
        }
    }
}    


extension BarCodeScanViewController: AVCaptureMetadataOutputObjectsDelegate {
    
    // 메타데이터 출력 델리게이트 메서드로 바코드 스캔 결과를 처리
    func metadataOutput(_ output: AVCaptureMetadataOutput, didOutput metadataObjects: [AVMetadataObject], from connection: AVCaptureConnection) {
        if let metadataObject = metadataObjects.first as? AVMetadataMachineReadableCodeObject {
            if let barcodeValue = metadataObject.stringValue {
//                print("스캔한 바코드: \(barcodeValue)")
            }
        }
    }
}
```

<br><br>


## 바코드 스캔영역을 제한하고 Dim처리하기

기존의 코드에서 Dim처리를 위한 maskLayer를 추가하는 로직이다. 

위에서 추가한 미리보기 레이어에 마스킹된 layer를 추가하는 것이다. 



```swift
/// 미리보기 레이어 생성 메서드
func setupVideoPreviewLayer() {
    DispatchQueue.main.async {
    
        // 바코드 스캔 영역 정의
        let scannerWidthMultiplier: CGFloat = 0.7
        let scannerWidth = self.view.bounds.width * scannerWidthMultiplier
        let scannerRectSize = CGSize(width: scannerWidth, height: scannerWidth)
        let scannerRectOrigin = CGPoint(x: (self.view.bounds.width - scannerWidth) / 2,
                                        y: (self.view.bounds.height - scannerWidth) / 2)
        let scanFocusRect = CGRect(origin: scannerRectOrigin, size: scannerRectSize)

        guard let captureSession = self.captureSession else { return }

        // AVCaptureSession에서 나오는 비디오 스트림을 표시하기 위한 미리보기 레이어를 생성
        self.videoPreviewLayer = AVCaptureVideoPreviewLayer(session: captureSession)
        // 비디오 스트림의 비율 설정
        self.videoPreviewLayer?.videoGravity = .resizeAspectFill
        
        // 미리보기 레이어의 프레임을 설정
        self.videoPreviewLayer?.frame = self.view.layer.bounds
        // 현재 view의 레이어에 미리보기 레이어를 추가
        self.view.layer.addSublayer(self.videoPreviewLayer!)
        
        
        // MARK: - 추가된 미리보기 레이어에 딤 처리
        
        // 딤 처리를 위한 shape Layer를 생성
        let maskLayer = CAShapeLayer()
        maskLayer.fillRule = .evenOdd
        maskLayer.frame = self.view.layer.bounds
        
        // 딤 처리할 영역을 패스로 정의
        let path = CGMutablePath()
        path.addRect(maskLayer.bounds)
        // 상단에서 정의한 부분
        path.addRect(scanFocusRect)
        maskLayer.path = path
        
        // 딤 처리 색상 및 배경 설정
        maskLayer.fillColor = UIColor.black.withAlphaComponent(0.6).cgColor
        maskLayer.backgroundColor = UIColor.clear.cgColor
        
        // 딤 처리 레이어를 미리보기 레이어에 추가
        self.videoPreviewLayer?.addSublayer(maskLayer)
    }
}

```

<br><br>

### 세부 설명
Dim처리를 위해 알아야할 객체는 `CAShapeLayer`와 `CGMutablePath`다 


1. maskLayer 생성 및 속성 설정
```swift
let maskLayer = CAShapeLayer()
maskLayer.fillRule = .evenOdd
maskLayer.frame = self.view.layer.bounds
```
- maskLayer: 딤 처리를 위한 `CAShapeLayer` 객체를 생성
- fillRule: CAShapeLayer의 패스 그리기 규칙을 설정
    - `.evenOdd`로 설정하면 두 개의 겹치는 영역에서 중첩되는 부분을 제외하고 채우게 된다.
- frame: maskLayer의 프레임을 뷰의 전체 영역으로 설정



2. 딤처리할 영역을 패스로 정의
```swift
let path = CGMutablePath()
path.addRect(maskLayer.bounds)  // 전체 영역을 패스에 추가
path.addRect(readingRect)       // 딤 처리되지 않을 바코드 스캔 영역을 패스에 추가
maskLayer.path = path
/*
    let scannerWidthMultiplier: CGFloat = 0.7
    let scannerWidth = self.view.bounds.width * scannerWidthMultiplier
    let scannerRectSize = CGSize(width: scannerWidth, height: scannerWidth)
    let scannerRectOrigin = CGPoint(x: (self.view.bounds.width - scannerWidth) / 2,
                                    y: (self.view.bounds.height - scannerWidth) / 2)
    let scanFocusRect = CGRect(origin: scannerRectOrigin, size: scannerRectSize)
*/
```

- path: 딤 처리할 영역을 정의하기 위한 패스 `CGMutablePath` 객체 생성
- addRect(maskLayer.bounds): 전체 뷰의 영역을 패스에 추가하여, maskLayer(전체 영역)이 딤 처리되도록 세팅
- addRect(readingRect): 실제 바코드 스캔이 이루어질 영역을 패스에 추가하여, 해당 영역만 바코드 스캔하도록 세팅
- maskLayer.path = path: 패스를 maskLayer의 패스로 설정하여 딤 처리할 영역을 정의

<br><br>

## 바코드스캐너를 켤때 애니메이션 효과 넣기
생각보다 바코드 스캐너로 카메라 화면이 앱에 띄워지기까지 많은 시간이 걸린다.  

화면에 올라가는 순서는 아래와 같다.  
- ViewController가 호출되고 잠시 시간이 흐른다.
- (딤처리 레이어가 먼저 생성)
- 카메라 화면이 뿅 나타난다. 

심지어 딤처리를 위해 딤처리된 layer를 추가했다면, 딤처리된 레이어가 카메라 화면보다 먼저 뜬다.  

이건.. 용납할 수 없다..  

앱을 좀더 부드럽고 예쁘게? 동작하는 걸 선호한다면 이것도 신경 써보자.

만들려는 동작은 아래와 같다.

- 스캐너를 담당하는 ViewController호출
- 화면이 검정색으로 스르륵 바뀐다. 
- 스캐너가 스르륵 나타난다

이 동작을 위해서는 아래의 단계를 거친다.

- 1. viewController.view.backgroundColor를 투명하게 시작
- 2. 첫번째 애니메이션
    - viewController.view.backgroundColor를 black 으로 변경
- 3. 스캐너 생성
    - 미리보기 레이어를 투명하게 시작
- 4. 스캐너 시작
- 5. 두번째 애니메이션
    - 미리보기 레이어의 투명도를 다시 선명하게 변경

동작을 구현하기 위한 메서드를 보자.  

<br><br>

```swift

class BarCodeScanViewController: UIViewController {

    var captureSession: AVCaptureSession?
    var videoPreviewLayer: AVCaptureVideoPreviewLayer?

    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.view.backgroundColor = .clear
        prepareTransitionAnimation()
    }
    
    /// 스캐너 생성 전 애니메이션
    func prepareTransitionAnimation() {
        UIView.animate(withDuration: 0.5, animations: {
            self.view.backgroundColor = .black  // 검정색으로 배경 변경
        }) { _ in
            // 캡쳐 세션 생성
            self.setupCaptureSession()
        }
    }
    
    /// 스캐너 생성 후  애니메이션 
    func animatePreviewLayerOpacity() {
        UIView.animate(withDuration: 0.5, animations: {
            self.videoPreviewLayer?.opacity = 1.0
        })
    }
    
    /// 미리보기 레이어 생성 메서드
    func setupVideoPreviewLayer() {

        // ... 이전 생략
        
        // opacity 설정으로 초기에 미리보기 영역을 숨김
        self.videoPreviewLayer?.opacity = 0
    }
}
```


<br><br>

## History
- 230904 : 기본 사용법
- 230905 : 바코드 스캔영역 외 Dim처리방법 추가
- 230905 : 애니메이션 효과 추가
