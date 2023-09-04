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

## 간단한 사용법

스레드 사용에 유의해야한다. 

```swift

class BarCodeScanViewController: UIViewController {
    
    // AVCaptureSession은 카메라 세션을 관리하는 객체
    var captureSession: AVCaptureSession!
    
    // AVCaptureVideoPreviewLayer는 카메라 영상을 표시하는 레이어
    var videoPreviewLayer: AVCaptureVideoPreviewLayer!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        setupCaptureSession()
    }

    func setupCaptureSession() {
        DispatchQueue.global(qos: .background).async {
            
            // AVCaptureSession 객체를 생성
            self.captureSession = AVCaptureSession()
            
            // 기기의 기본 카메라를 가져옵니다.
            guard let captureDevice = AVCaptureDevice.default(for: .video) else { return }
            
            do {
                // 카메라 입력을 설정
                let input = try AVCaptureDeviceInput(device: captureDevice)
                self.captureSession.addInput(input)
                
                // 메타데이터 출력을 설정
                let captureMetadataOutput = AVCaptureMetadataOutput()
                self.captureSession.addOutput(captureMetadataOutput)
                
                // 메타데이터 출력의 델리게이트를 설정하고 인식할 바코드 유형을 설정
                captureMetadataOutput.setMetadataObjectsDelegate(self, queue: DispatchQueue.main)
                captureMetadataOutput.metadataObjectTypes = [
                    .qr,
                    .upce,
                    .code39,
                    .code39Mod43,
                    .ean13,
                    .ean8,
                    .code93,
                    .code128,
                    .pdf417,
                    .aztec,
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

    func setupVideoPreviewLayer() {
        DispatchQueue.main.async {
            // AVCaptureSession에서 나오는 비디오 스트림을 표시하기 위한 미리보기 레이어를 생성
            self.videoPreviewLayer = AVCaptureVideoPreviewLayer(session: self.captureSession)
            // 비디오 스트림의 비율 설정
            self.videoPreviewLayer.videoGravity = .resizeAspectFill
            
            self.videoPreviewLayer.frame = self.view.layer.bounds
            // 현재 view의 레이어에 미리보기 레이어를 추가
            self.view.layer.addSublayer(self.videoPreviewLayer)
        }
    }

    func startCaptureSession() {
        DispatchQueue.global(qos: .background).async {
            if !self.captureSession.isRunning {
                self.captureSession.startRunning()
            }
        }
    }
}    


extension BarCodeScanViewController: AVCaptureMetadataOutputObjectsDelegate {
    
    // 메타데이터 출력 델리게이트 메서드로 바코드 스캔 결과를 처리
    func metadataOutput(_ output: AVCaptureMetadataOutput, didOutput metadataObjects: [AVMetadataObject], from connection: AVCaptureConnection) {
        if let metadataObject = metadataObjects.first as? AVMetadataMachineReadableCodeObject {
            if let barcodeValue = metadataObject.stringValue {
                // 스캔한 바코드 정보를 얼럿으로 표시
                showBarcodeAlert(barcodeValue)
//                print("스캔한 바코드: \(barcodeValue)")

            }
        }
    }
    
    func showBarcodeAlert(_ barcodeValue: String) {
        let alertController = UIAlertController(title: "바코드 스캔 성공",
                                                message: "스캔한 바코드: \(barcodeValue)",
                                                preferredStyle: .alert)
        
        let okAction = UIAlertAction(title: "확인", style: .default) { _ in
            self.dismiss(animated: true)
        }
        alertController.addAction(okAction)
        
        DispatchQueue.main.async {
            self.present(alertController, animated: true, completion: nil)
        }
    }

}
```


## 바코드 스캔영역을 제한하고 Dim처리하기

기존의 코드에서 Dim처리를 위한 maskLayer를 추가하는 로직이다. 

```
    func setupVideoPreviewLayer() {
        DispatchQueue.main.async {
            // 바코드 스캔 영역을 정의
            let scanerWidth = 520
            let readingRect = CGRect(x: (self.view.bounds.width / 2) - (scanerWidth / 2), 
                                     y: (self.view.bounds.height / 2) - (scanerWidth / 2),
                                     width: scanerWidth,
                                     height: scanerWidth)
            // AVCaptureSession에서 나오는 비디오 스트림을 표시하기 위한 미리보기 레이어를 생성
            self.videoPreviewLayer = AVCaptureVideoPreviewLayer(session: self.captureSession)
            // 비디오 스트림의 비율 설정
            self.videoPreviewLayer.videoGravity = .resizeAspectFill
            
            // 미리보기 레이어의 프레임을 설정
            self.videoPreviewLayer.frame = self.view.layer.bounds
            // 현재 view의 레이어에 미리보기 레이어를 추가
            self.view.layer.addSublayer(self.videoPreviewLayer)
            
            // MARK: 추가된 코드
            
            // 딤 처리를 위한 shape Layer를 생성
            let maskLayer = CAShapeLayer()
            maskLayer.fillRule = .evenOdd
            maskLayer.frame = self.view.layer.bounds
            
            // 딤 처리할 영역을 패스로 정의
            let path = CGMutablePath()
            path.addRect(maskLayer.bounds)
            path.addRect(readingRect)
            maskLayer.path = path
            
            // 딤 처리 색상 및 배경 설정
            maskLayer.fillColor = UIColor.black.withAlphaComponent(0.6).cgColor
            maskLayer.backgroundColor = UIColor.clear.cgColor
            
            // 딤 처리 레이어를 미리보기 레이어에 추가
            self.videoPreviewLayer.addSublayer(maskLayer)
        }
    }

```
