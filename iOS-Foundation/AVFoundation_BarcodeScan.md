# AVFoundation - Barcode Scanner 구현하기

AVFoundation를 이용해 바코드 스캐너를 구현할 수 있다.

## 순서

- [주요객체](#주요객체)
- [간단한 사용법](#간단한-사용법)
- [바코드 스캔영역을 제한하고 Dim처리하기](#바코드-스캔영역을-제한하고-Dim처리하기)
- [바코드스캐너를 켤때 애니메이션 효과 넣기](#바코드스캐너를-켤때-애니메이션-효과-넣기)
- [스캐너 화면에 안내 Label 추가하기](#스캐너-화면에-안내-Label-추가하기)
- [안내선 이미지 추가하기](#안내선-이미지-추가하기)
- [스캔영역 변경하기](#스캔영역-변경하기)
    - [화면의 일부만 바코드 스캐너로 사용하는 경우](#화면의-일부만-바코드-스캐너로-사용하는-경우)
    - [rectOfInterest](#rectOfInterest)
- [전체코드 최종](#전체코드-최종)
- [전체코드 적용화면](#전체코드-적용화면)


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

[[Top]](#순서)
<br>
<br>

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
        if let metadataObject = metadataObjects.first as? AVMetadataMachineReadableCodeObject,
            let barcodeValue = metadataObject.stringValue {
            print("스캔한 바코드: \(barcodeValue)")
            // 캡쳐 세션 종료
            self.captureSession?.stopRunning()
        }
    }
}
```

<br><br>
[[Top]](#순서)
<br>
<br>


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
[[Top]](#순서)
<br>
<br>

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
[[Top]](#순서)
<br>
<br>

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
    
    /// 스캐너 생성 후 애니메이션 
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


## 전체코드

```swift
class BarCodeScanViewController: JwUIViewController, HelperProtocol {
    
    // AVCaptureSession은 카메라 세션을 관리하는 객체
    var captureSession: AVCaptureSession?
    // AVCaptureVideoPreviewLayer는 카메라 영상을 표시하는 레이어
    var videoPreviewLayer: AVCaptureVideoPreviewLayer?

    lazy var closeBarButtonItem: UIBarButtonItem = {
        let imageSize = CGSize(width: 55, height: 55)
        let normalImage = UIImage(named: "btn_close_n")?.imageWithSize(imageSize)
        let rightBarButtonItem = UIBarButtonItem(image: normalImage,
                                                 style: .plain,
                                                 target: self,
                                                 action: #selector(closeBtnTapped(_:)))
        rightBarButtonItem.tintColor = .white
        return rightBarButtonItem
    }()
    
    @objc func closeBtnTapped(_ sender: UIButton) {
        self.dismiss(animated: true)
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        self.view.backgroundColor = .clear
        self.navigationItem.rightBarButtonItem = closeBarButtonItem
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
    
    
    /// 스캐너 생성 후 애니메이션 
    func animatePreviewLayerOpacity() {
        UIView.animate(withDuration: 0.5, animations: {
            self.videoPreviewLayer?.opacity = 1.0
        })
    }

    /// 캡쳐 세션 생성 메서드
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

            // 스캔 세션이 시작된 후에 미리보기 레이어의 투명도를 조절
            DispatchQueue.main.async {
                self.animatePreviewLayerOpacity()
            }
        }
    }
    
    /// 미리보기 레이어 생성 메서드
    func setupVideoPreviewLayer() {
        DispatchQueue.main.async {
            // 바코드 스캔 영역을 정의
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
            
            // 딤 처리를 위한 shape Layer를 생성
            let maskLayer = CAShapeLayer()
            maskLayer.fillRule = .evenOdd
            maskLayer.frame = self.view.layer.bounds
            
            // 딤 처리할 영역을 패스로 정의
            let path = CGMutablePath()
            path.addRect(maskLayer.bounds)
            path.addRect(scanFocusRect)
            maskLayer.path = path
            
            // 딤 처리 색상 및 배경 설정
            maskLayer.fillColor = UIColor.black.withAlphaComponent(0.6).cgColor
            maskLayer.backgroundColor = UIColor.clear.cgColor
            
            // 딤 처리 레이어를 미리보기 레이어에 추가
            self.videoPreviewLayer?.addSublayer(maskLayer)

            // opacity 설정으로 초기에 미리보기 영역을 숨김
            self.videoPreviewLayer?.opacity = 0
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
    
    // 메타데이터 출력 델리게이트 메서드로 바코드 스캔 결과를 처리합니다.
    func metadataOutput(_ output: AVCaptureMetadataOutput, didOutput metadataObjects: [AVMetadataObject], from connection: AVCaptureConnection) {
        if let metadataObject = metadataObjects.first as? AVMetadataMachineReadableCodeObject,
           let barcodeValue = metadataObject.stringValue {
            print("스캔한 바코드: \(barcodeValue)")
            // 캡쳐 세션 종료
            self.captureSession?.stopRunning()
        }
    }

}

```

<br><br>
[[Top]](#순서)
<br>
<br>

## 스캐너 화면에 안내 Label 추가하기

위에서 스캔영역을 지정했기때문에 기준으로 삼을 `CGRect`가 있다.

<br>

```swift

// 방법 1.
guideLabel.frame = CGRect(x: scanFocusRect.minX,
                          y: scanFocusRect.maxY + 65,
                          width: scanFocusRect.width,
                          height: 60)
                          
// 방법 2.
guideLabel.sizeToFit()  // 텍스트 내용에 맞게 라벨 크기 조정
guideLabel.center.x = scanFocusRect.midX  // 가로 중앙을 scanFocusRect의 가로 중앙에 맞춤
guideLabel.frame.origin.y = scanFocusRect.maxY + 65  // Y 좌표 설정
```

위 두가지 방법으로 설정이 가능하다.   

<br><br>

```swift

/// 미리보기 레이어 생성 메서드
func setupVideoPreviewLayer() {
    DispatchQueue.main.async {
        // 바코드 스캔 영역을 정의
        let scannerWidthMultiplier: CGFloat = 0.7
        let scannerWidth = self.view.bounds.width * scannerWidthMultiplier
        let scannerRectSize = CGSize(width: scannerWidth, height: scannerWidth)
        let scannerRectOrigin = CGPoint(x: (self.view.bounds.width - scannerWidth) / 2,
                                        y: (self.view.bounds.height - scannerWidth) / 2)
        let scanFocusRect = CGRect(origin: scannerRectOrigin, size: scannerRectSize)


        // 중간 생략..
        
        // 딤 처리할 영역을 패스로 정의
        let path = CGMutablePath()
        path.addRect(maskLayer.bounds)
        path.addRect(scanFocusRect)
        maskLayer.path = path
        
        // 생략..
        
        // opacity 설정으로 초기에 미리보기 영역을 숨김
        self.videoPreviewLayer?.opacity = 0
        
        // 안내 텍스트를 생성하여 미리보기 레이어 위에 추가
        let guideLabel = UILabel()
        guideLabel.text = "Place the barcode within the square"
        guideLabel.textColor = .white
        guideLabel.font = UIFont.systemFont(ofSize: 16)
        guideLabel.textAlignment = .center
        guideLabel.numberOfLines = 0
//            guideLabel.frame = CGRect(x: scanFocusRect.minX,
//                                      y: scanFocusRect.maxY + 65,
//                                      width: scanFocusRect.width,
//                                      height: 60)
        
        guideLabel.sizeToFit()  // 텍스트 내용에 맞게 라벨 크기 조정
        guideLabel.center.x = scanFocusRect.midX  // 가로 중앙을 scanFocusRect의 가로 중앙에 맞춤
        guideLabel.frame.origin.y = scanFocusRect.maxY + 65  // Y 좌표 설정

        
        self.view.addSubview(guideLabel)
    }
}

```
<br>
<br>

[[Top]](#순서)
<br>
<br>


## 안내선 이미지 추가하기

enum에 정보를 담아준다.  
CaseIterable 프로토콜을 사용하면 AllCases프로퍼티를 사용할 수 있다.
```swift
enum QRFocusPosition: CaseIterable {
    case topLeft
    case topRight
    case bottomLeft
    case bottomRight
    
    var imageName: String {
        switch self {
        case .topLeft:
            return "qr-focus-top-left"
        case .topRight:
            return "qr-focus-top-right"
        case .bottomLeft:
            return "qr-focus-bottom-left"
        case .bottomRight:
            return "qr-focus-bottom-right"
        }
    }
}
```

 이제 네개의 모서리에 배치될 이미지를 올려준다.  
이 때 FocusRect의 값을 넣어준다.  

```swift
    /// 미리보기 레이어 생성 메서드
func setupVideoPreviewLayer() {
    // 생략...

    for position in QRFocusPosition.allCases {
        let imageView = self.addQRFocusImages(scanFocusRect: scanFocusRect,
                                              type: position)
        self.view.addSubview(imageView)
    }
}

func addQRFocusImages(scanFocusRect: CGRect, type: QRFocusPosition) -> UIImageView {
    
    let qrFocusImageWidth: CGFloat = 20
    let qrFocusImageOffset: CGFloat = 3
    guard let image = UIImage(named: type.imageName) else {
        fatalError("Could not load image with name \(type.imageName)")
    }

    let imageView = UIImageView(image: image)
    imageView.frame.size = CGSize(width: qrFocusImageWidth, height: qrFocusImageWidth)

    switch type {
    case .topLeft:
        imageView.frame.origin = CGPoint(x: scanFocusRect.minX - qrFocusImageOffset,
                                         y: scanFocusRect.minY - qrFocusImageOffset)
    case .topRight:
        imageView.frame.origin = CGPoint(x: scanFocusRect.maxX - qrFocusImageWidth + qrFocusImageOffset,
                                         y: scanFocusRect.minY - qrFocusImageOffset)
    case .bottomLeft:
        imageView.frame.origin = CGPoint(x: scanFocusRect.minX - qrFocusImageOffset,
                                         y: scanFocusRect.maxY - qrFocusImageWidth + qrFocusImageOffset)
    case .bottomRight:
        imageView.frame.origin = CGPoint(x: scanFocusRect.maxX - qrFocusImageWidth + qrFocusImageOffset,
                                         y: scanFocusRect.maxY - qrFocusImageWidth + qrFocusImageOffset)
    default:
        break
    }

    return imageView
}
```

### 적용화면

<img src="https://github.com/isGeekCode/TIL/assets/76529148/03254bbe-2148-477c-96fd-ffb02a2010d2" width="300">

<br><br>

[[Top]](#순서)
<br>
<br>

## 스캔영역 변경하기
상황이 여의치않아서 네비게이션바 대신에 동일한 모양의 헤더뷰를 생성했다.

스캐너에서 영역에 대한 정보를 다시 살펴보자.

- 1. 미리보기 Layer를 지정할 CGRect
- 딤처리를 할 경우
    - 2. 딤처리의 바깥라인을 알려주는 CGRect
        - 이 사이만 딤처리가 되는 부분 
    - 3. 딤처리의 안쪽라인을 알려주는 CGRect
        - 이 안쪽은 투명해요. 스캔이 되는 영역 


그냥 화면 전체를 스캐너로 전환하여 사용할 경우, 
기존에는 `1번. 스캐너의 미리보기 영역`을 self.view.bounds로 잡아서 사용을 하면 설정이 끝이다.  

Dim처리를 하는 경우에는 `2번.딤처리를 할 바깥 영역`, `3번. 안쪽 영역`의 경계를 지정해주면 된다.   

만약 우리가 스캐너 미리보기 화면 위에 닫기 버튼도 구현하는 것은 문제가 안된다.  

문제가 되는 상황은 바로 ..  

### 화면의 일부만 바코드 스캐너로 사용하는 경우

이때에는 카메라로 보이는 영역 중에서도 아주 일부분에서만 스캔이 되는 기현상이 일어난다.  

스캔영역이 눈에 보이면 평화롭겠지만.... 그런 기능 따윈없다...ㅠ  

특히나 Dim처리를 했다면 이 안쪽에선 모두 스캔이 되야하는게 당연한건데, 역시나 영역이 의도와는 다르게 잡힌다.  

이 때 사용하는 것이 `AVCaptureMetadataOutput`객체의 `rectOfInterest` 프로퍼티다.

맨 처음 스캐너를 설정할때, 아래와 같은 과정을 진행한다. 

```swift
// 카메라 입력을 설정
let input = try AVCaptureDeviceInput(device: captureDevice)
self.captureSession.addInput(input)

// 메타데이터 출력을 설정
let output = AVCaptureMetadataOutput()
self.captureSession.addOutput(output)
 
// 미리보기 레이어 생성

// 딤 처리 레이어 생성(선택)
```

<br><br>

[[Top]](#순서)
<br>
<br>

### rectOfInterest

AVCaptureMetadataOutput 에 대한 검색영역을 제한하는데 사용된다. 

rectOfInterest에 들어가는 타입은 CGRect타입이다. 

이 속성의 기본값은 (0,0,1,1)이다. 

이 프로퍼티에 내가 포커싱한 영역값에 대한 정보를 CGRect에 담아서 넣어준다. 
아래는 안좋은 예시이다. 

```swift
let focusRect = CGRect() // 내가 포커싱한 영역값
output.rectOfInterest = focusRect
```

이렇게 넣으면 아예 스캔자체가 되지않는 현상이 발생하니 이렇게 넣으면 안되고 CGRect(0,0,1,1)의 형태로 넣어주어야한다.
각각 현재화면 대비 x,y,width,height 에 대한 비율을 0 ~ 1.0 사이의 퍼센티지로 지정을 하는 것이다. 

- 직접 비율을 넣어서 생성하기 (비추천)
```swift
// CGRectMake(x:y:width:height:)

// 사용예
let focusRect: CGRect = CGRectMake(0.222299999,0.17644451, 0.364111, 0.674111) 
output.rectOfInterest = focusRect
```

해당 값을 CGRectMake(x:y:width:height:)라는 메서드에 넣어서 리턴되는 CGRect값을 사용할 수있지만  

이렇게 하면 마치 하드코딩하는 것과 별반 다를 게 없기에  

실제로 내가 원하는 화면 대비 원하는 포커스를 대입하여 비율을 구할 수 있는 메서드가 있다.   

그래서 아래와 같은 방법을 사용한다.  

- 미리보기 레이어에 따른 타게팅Rect의 비율을 리턴하는 메서드 사용
```swift
// 사용예

// self.focusRect :::: 내가 Dim처리에서 타게팅 부분으로 잡은 CGRect값
// self.videoPreviewLayer ::: 내가 사용중인 미리보기 레이어
// metadataOutputRectConverted(fromLayerRect:) ::: CGRect(0,0,1,1)의 형태로 리턴한다.  

let rectConverted = self.videoPreviewLayer.metadataOutputRectConverted(fromLayerRect: self.focusRect)
output.rectOfInterest = rectConverted
```
이 방법은 현재 사용중인 미리보기 레이어의 metadataOutputRectConverted 메서드의 파라미터로 타게팅할 Rect를 넣어주는 방법이다. 그러면 rectOfInterest의 타입에 맞는 CGRect에 비율값이 들어가서 리턴된다. 

그러나!!!!! 이 값을 넣으면 끝이 아니다....  

### 그럼에도 에러가 납니다.

실제로 위에서 `metadataOutputRectConverted(fromLayerRect:)` 로 만든 값을 살펴보면 (0,0,0,0)이라는 값이 나온다.
x,y,width,height 모든 값을 화면대비 0으로 주겠다는 말이다.   (최악...)
 
실제로 구글링에  `rectOfInterest`을 검색하면 동일한 현상이 수두룩 뺵뺵이다.  

이 메서드를 사용하려면 특별한 조치를 해야한다.  

정상적인 값으로 리턴받기 위해서는   

바코드 스캐너를 생성시 Layout에 대한 정보가 바뀔 때마다 아래 메서드를 다시 호출해서 Rect를 갱신해줘야한다. 
좀더 자세히 말하자면 output에 대한 메타정보가 바뀔때마다 갱신해주어야한다. 
```swift
let rectConverted = self.videoPreviewLayer.metadataOutputRectConverted(fromLayerRect: self.focusRect)
output.rectOfInterest = rectConverted
```

- 정리
    - 화면마다 스캐너 영역이라는게 있다. 
    - 화면 전체롤 전부 잡을 경우, 그냥 사용하면 된다. 이때는 rectOfInterest이 기본값인 (0,0,1,1) 이다.  
    - 스캔영역을 일부분으로 지정하는경우, 스캔 영역이 어긋난다. 그래서 일부분에서만 스캔이 된다.  
    - 딤처리를 할경우, 내가 스캔하는 영역을 시각적으로 나타내지만 실제스캔영역과 차이가 생겨서 조치를 해야한다.
    - 현재 화면대비 원하는 스캔영역에 대한 비율값으로 rectOfInterest값을 갱신해야한다. 
    - 그 값을 만드는 `metadataOutputRectConverted(fromLayerRect:)`의 사용법을 지키지않으면 전혀 스캔영역이 아예 사라지게 된다. 
    
<br><br>

이제 이 메서드의 사용법을 살펴보자.  

언제든 호출을 할 수 있도록 메서드로 분리해주는 것이 좋다.  

다만 그렇게 하려면 output인 AVCaptureMetadataOutput객체를 전역변수로 만들어주어야한다.  

- 전역변수로 만들어서 선언하기

```swift
private var captureSession = AVCaptureSession()
private var videoPreviewLayer = AVCaptureVideoPreviewLayer()
private var output = AVCaptureMetadataOutput()

private func refreshFocus(focusRect: CGRect) {
    let rectConverted = self.videoPreviewLayer.metadataOutputRectConverted(fromLayerRect: focusRect)
    self.output.rectOfInterest = rectConverted
}
```

<br>

- 클로저로 선언하기
상단에 전역변수로 클로저를 선언한다.  
   
그다음 input, output을 설정하는 시점에 이 클로저에 넣어주고, 필요할 떄마다 호출한다. 

```swift
// 스캔범위 재조정을 위한 클로저
private var rectConvertedClosure: (() -> ())?

/// 캡쳐 세션 생성 메서드
private func setupCaptureSession() {
    
    DispatchQueue.global(qos: .background).async {
        DispatchQueue.main.async {

        // AVCaptureSession 객체를 생성
        self.captureSession = AVCaptureSession()
        
        do {
            // 카메라 입력을 설정
            let input = try AVCaptureDeviceInput(device: captureDevice)
            self.captureSession.addInput(input)
            
            // 메타데이터 출력을 설정
            let output = AVCaptureMetadataOutput()
            self.captureSession.addOutput(output)
            
            // 메타데이터 출력의 델리게이트를 설정하고 인식할 바코드 유형을 설정
            output.setMetadataObjectsDelegate(self, queue: DispatchQueue.main)
            output.metadataObjectTypes = [
                .qr, .upce, .code39, .code39Mod43, .ean13,
                .ean8, .code93, .code128, .pdf417, .aztec,
            ]
            
            // 미리보기 레이어 생성
            self.setupVideoPreviewLayer(scanFocusRect: self.scanFocusRect)
            
            // 제한영역 설정
            self.rectConvertedClosure = {
                let rectConverted = self.videoPreviewLayer.metadataOutputRectConverted(fromLayerRect: self.scanFocusRect)
                output.rectOfInterest = rectConverted
            }

        } catch {
            print(error)
        }
    }
}

``` 



<br><br>

위처럼 타겟 Rect가 있는 곳에서 클로저에 넣어준 다음, 아래 시점에 호출해준다. 

- viewDidLayoutSubviews 메서드가 호출될 때
- 이름이 `.AVCaptureInputPortFormatDescriptionDidChange`인 NotificationCenter 메서드가 호출될때


<br>

### viewDidLayoutSubviews 메서드가 호출되는 시점

- 뷰가 처음 생성될 때: viewDidLoad 이후에 viewDidLayoutSubviews가 호출된다.
- 뷰 컨트롤러의 루트 뷰(view)의 크기나 레이아웃이 변경될 때: 
    - 예를 들어, 기기의 회전, Split View Controller의 변경, 뷰 계층 구조 변경 등의 이벤트가 발생할 때 viewDidLayoutSubviews가 호출된다.  
- setNeedsLayout 또는 layoutIfNeeded 메서드가 호출될 때: 코드에서 명시적으로 레이아웃 업데이트를 요청하면 해당 업데이트가 완료된 후 viewDidLayoutSubviews가 호출된다.  
 
 
<br>
 
### Notification.Name.AVCaptureInputPortFormatDescriptionDidChange 가 호출되는 시점

- AVCaptureSession이 시작될 때 
- AVCaptureDevice의 입력 설정이 변경될 때
    - 예를 들어, 카메라의 해상도나 프레임 속도와 같은 입력 설정이 변경될 때 형식(description)이 변경되며 호출된다.  

그래서 위 상황에 호출하도록 세팅한 코드를 보자.  

```swift

class ViewController: UIViewController {

// MARK: - Properties
// 스캔범위 재조정을 위한 클로저
private var rectConvertedClosure: (() -> ())?


// MARK: - View's Life-Cycles Methods
override func viewDidLayoutSubviews() {
    print("viewDidLayoutSubviews")
    if let rectConvertedClosure = rectConvertedClosure {
        return rectConvertedClosure()
    }
}

    override func viewDidLoad() {
        super.viewDidLoad()
        // 노티피케이션 옵저버 추가
        NotificationCenter.default.addObserver(self,
                                               selector: #selector(inputPortFormatDescriptionDidChange(_:)),
                                               name: .AVCaptureInputPortFormatDescriptionDidChange, object: nil)
                                               
       /* 혹은 이렇게 직접 넣어도 된다. 
        
        NotificationCenter.default.addObserver(forName: .AVCaptureInputPortFormatDescriptionDidChange,
                                               object: nil,
                                               queue: .main) { _ in
            if let rectConvertedClosure = self.rectConvertedClosure {
                return rectConvertedClosure()
            }
        }
        */
    }
    
    // MARK: - Notification Method
    @objc func inputPortFormatDescriptionDidChange(_ notification: NSNotification) {
            print("Noti - AVCaptureInputPortFormatDescriptionDidChange!!!!!")
        if let rectConvertedClosure = rectConvertedClosure {
            return rectConvertedClosure()
        }
    }

    /// 캡쳐 세션 생성 메서드
    private func setupCaptureSession() {
        
        DispatchQueue.global(qos: .background).async {
            // AVCaptureSession 객체를 생성
            self.captureSession = AVCaptureSession()
            // 생략..

            do {
                // 카메라 입력을 설정
                let input = try AVCaptureDeviceInput(device: captureDevice)
                
                
                // 메타데이터 출력을 설정
                let output = AVCaptureMetadataOutput()
            
                // 생략..
                
                // 미리보기 레이어 생성 : 미리보기를 원하는 레이어 크기로 선언
                self.setupVideoPreviewLayer(scanFocusRect: self.scanFocusRect)
                
                // MARK: - 제한영역 갱신 : 지정한 미리보기 레이어 크기 대비 원하는 제한영역의 비율로 갱신할 클로저에 넣어준다. 
                self.rectConvertedClosure = {
                    let rectConverted = self.videoPreviewLayer.metadataOutputRectConverted(fromLayerRect: self.scanFocusRect)
                    output.rectOfInterest = rectConverted
                }
                
                // 생략..
            } catch {
                print(error)
            }
            
            // 생략..
        }
    }
}
```



<br>
<br>

[[Top]](#순서)
<br>
<br>


이제 적용한 전체 코드를 살펴보자. 

# 전체코드 최종

```swift
class ViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .darkGray 
        let button = UIButton()
        button.setTitle("test", for: .normal)
        button.backgroundColor = .systemTeal

        button.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(button)

        NSLayoutConstraint.activate([
            button.centerXAnchor.constraint(equalTo: self.view.safeAreaLayoutGuide.centerXAnchor),
            button.centerYAnchor.constraint(equalTo: self.view.safeAreaLayoutGuide.centerYAnchor),
            button.widthAnchor.constraint(equalToConstant: 200),
            button.heightAnchor.constraint(equalToConstant: 150),
        ])
        
        // 클로저를 사용하여 버튼 동작 추가
        button.addTarget(self, action: #selector(buttonTapped), for: .touchUpInside)
    }
    
    
    @objc func buttonTapped() {
        // 버튼이 눌렸을 때 실행할 클로저 코드
        let viewController = BarCodeScanViewController()
        viewController.modalPresentationStyle = .fullScreen
        viewController.modalTransitionStyle = .crossDissolve
        self.present(viewController, animated: true)
    }
}

//
//  BarCodeScanViewController.swift
//  nbKorea
//
//  Created by bang_hyeonseok on 2023/09/04.
//  Copyright © 2023 Sim, Jae-Won. All rights reserved.
//

import UIKit
import AVFoundation

/// 바코드 스캔 포커스 위치를 정의한 열거형
enum QRFocusPosition: CaseIterable {
    case topLeft
    case topRight
    case bottomLeft
    case bottomRight
    
    var imageName: String {
        switch self {
        case .topLeft:
            return "qr-focus-top-left"
        case .topRight:
            return "qr-focus-top-right"
        case .bottomLeft:
            return "qr-focus-bottom-left"
        case .bottomRight:
            return "qr-focus-bottom-right"
        }
    }
}


class BarCodeScanViewController: UIViewController {
    
    // MARK: - Properties

    // AVCaptureSession은 카메라 세션을 관리하는 객체
    private var captureSession = AVCaptureSession()
    // AVCaptureVideoPreviewLayer는 카메라 영상을 표시하는 레이어
    private var videoPreviewLayer = AVCaptureVideoPreviewLayer()
    // 스캔범위 재조정을 위한 클로저
    private var rectConvertedClosure: (() -> ())?
    // 스캔범위 값
    private var scanFocusRect = CGRect()
    
    // MARK: - UI Components
    
    private lazy var customNavBar: CustomNavigationBar = {
        let navBar = CustomNavigationBar()
        navBar.delegate = self
        navBar.translatesAutoresizingMaskIntoConstraints = false
        return navBar
    }()
    
    private lazy var scannerView: UIView = {
        let view = UIView()
        view.backgroundColor = .clear
        view.translatesAutoresizingMaskIntoConstraints = false
        return view
    }()
    
    private lazy var guideLabel: UILabel = {
        let label = UILabel()
        let paragraphStyle = NSMutableParagraphStyle()
        paragraphStyle.lineSpacing = 8  // 행간을 조절하려면 원하는 값으로 설정
        let text = """
                   바코드는 카메라 정가운데
                   위치 해주시면 됩니다.
                   """
        let attributedText = NSMutableAttributedString(string: text)

        attributedText.addAttribute(.paragraphStyle,
                                    value: paragraphStyle,
                                    range: NSRange(location: 0,
                                                   length: attributedText.length))
        
        label.attributedText = attributedText
        label.textColor = .white
        label.font = UIFont.systemFont(ofSize: 16)
        label.textAlignment = .center
        label.numberOfLines = 0
        label.sizeToFit()  // 텍스트 내용에 맞게 라벨 크기 조정\
        label.translatesAutoresizingMaskIntoConstraints = false
        return label
    }()

    // MARK: - View's Life-Cycles Methods
    override func viewDidLayoutSubviews() {
        print("viewDidLayoutSubviews")
        if let rectConvertedClosure = rectConvertedClosure {
            return rectConvertedClosure()
        }
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
        NotificationCenter.default.addObserver(self,
                                               selector: #selector(inputPortFormatDescriptionDidChange(_:)),
                                               name: .AVCaptureInputPortFormatDescriptionDidChange, object: nil)
        prepareTransitionAnimation()

    }
    
    // MARK: - UI Setup Methods

    private func setupUI() {
        view.backgroundColor = .clear
        setupNavigationBar()
        setupScannerView()
    }
    
    private func setupNavigationBar() {
        let navBarInfo = UIDevice.current.getNavigationBarHeight()
        let navBarHeight = navBarInfo.navBarHeight
        let topInset = navBarInfo.topInset
        
        view.addSubview(customNavBar)
        NSLayoutConstraint.activate([
            customNavBar.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            customNavBar.trailingAnchor.constraint(equalTo: view.trailingAnchor),
            customNavBar.topAnchor.constraint(equalTo: view.topAnchor),
            customNavBar.heightAnchor.constraint(equalToConstant: navBarHeight + topInset)
        ])
    }

    private func setupScannerView() {
        view.addSubview(scannerView)
        NSLayoutConstraint.activate([
            scannerView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            scannerView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
            scannerView.topAnchor.constraint(equalTo: customNavBar.bottomAnchor),
            scannerView.bottomAnchor.constraint(equalTo: view.bottomAnchor)
        ])
    }

    // MARK: - Notification Method
    @objc func inputPortFormatDescriptionDidChange(_ notification: NSNotification) {
            print("Only VC :: Noti - AVCaptureInputPortFormatDescriptionDidChange!!!!!")
        if let rectConvertedClosure = rectConvertedClosure {
            return rectConvertedClosure()
        }
    }

    // MARK: Animations
    /// 스캐너 생성 전 애니메이션
    private func prepareTransitionAnimation() {
        UIView.animate(withDuration: 0.5, animations: {
            self.view.backgroundColor = .black  // 검정색으로 배경 변경
        }) { _ in
            // 캡쳐 세션 생성
            self.checkCameraPermission()
        }
    }
    
    /// 스캐너 생성 후  애니메이션 
    private func animatePreviewLayerOpacity() {
        UIView.animate(withDuration: 0.5, animations: {
            self.videoPreviewLayer.opacity = 1.0
        })
    }

    // MARK: Request Camera Privacy Check 
    ///  카메라 권한 체크
    private func checkCameraPermission() {
        let status = AVCaptureDevice.authorizationStatus(for: .video)
        
        switch status {
        case .authorized:
            // 이미 권한이 부여된 경우, 스캐너 초기화 및 캡쳐 세션 설정을 진행할 수 있습니다.
            setupCaptureSession()
        case .notDetermined:
            // 권한이 아직 요청되지 않은 경우, 사용자에게 권한을 요청합니다.
            AVCaptureDevice.requestAccess(for: .video) { [weak self] granted in
                if granted {
                    // 권한이 부여되면 스캐너 초기화 및 캡쳐 세션 설정을 진행할 수 있습니다.
                    DispatchQueue.main.async {
                        self?.setupCaptureSession()
                    }
                } else {
                    // 권한이 거부된 경우, 사용자에게 메시지를 표시하거나 적절한 조치를 취할 수 있습니다.
                }
            }
        case .denied, .restricted:
            // 권한이 거부되거나 제한된 경우, 사용자에게 메시지를 표시하거나 적절한 조치를 취할 수 있습니다.
            // 예를 들어, 앱 설정으로 이동하도록 안내하는 등의 작업을 수행할 수 있습니다.
            // 사용자의 프라이버시를 존중하고 권장된 방식으로 처리하세요.
            break
        @unknown default:
            break
        }
    }

    // MARK: - Capture Session Setup
    /// 캡쳐 세션 생성 메서드
    private func setupCaptureSession() {
        
        DispatchQueue.global(qos: .background).async {
            DispatchQueue.main.async {
                var scannerWidth: CGFloat = 0
                    // 바코드 스캔 영역을 정의
                let scannerWidthMultiplier: CGFloat = 0.7
                    scannerWidth = self.view.bounds.width * scannerWidthMultiplier
                let scannerRectSize = CGSize(width: scannerWidth, height: scannerWidth)
                
                let scanFocusRectOriginY = self.scannerView.bounds.height * 0.24
                let scanFocusRectOriginX = (self.scannerView.bounds.width - scannerWidth) * 0.5
                let scannerRectOrigin = CGPoint(x: scanFocusRectOriginX,
                                                y: scanFocusRectOriginY)
                
                self.scanFocusRect = CGRect(origin: scannerRectOrigin,
                                       size: scannerRectSize)
            }

            // AVCaptureSession 객체를 생성
            self.captureSession = AVCaptureSession()
            
            // 기기의 기본 카메라를 호출
            guard let captureDevice = AVCaptureDevice.default(for: .video) else { return }
            
            do {
                // 카메라 입력을 설정
                let input = try AVCaptureDeviceInput(device: captureDevice)
                self.captureSession.addInput(input)
                
                // 메타데이터 출력을 설정
                let output = AVCaptureMetadataOutput()
                self.captureSession.addOutput(output)
                
                // 메타데이터 출력의 델리게이트를 설정하고 인식할 바코드 유형을 설정
                output.setMetadataObjectsDelegate(self, queue: DispatchQueue.main)
                output.metadataObjectTypes = [
                    .qr, .upce, .code39, .code39Mod43, .ean13,
                    .ean8, .code93, .code128, .pdf417, .aztec,
                ]
                
                // 미리보기 레이어 생성
                self.setupVideoPreviewLayer(scanFocusRect: self.scanFocusRect)
                // 제한영역 설정
                self.rectConvertedClosure = {
                    let rectConverted = self.videoPreviewLayer.metadataOutputRectConverted(fromLayerRect: self.scanFocusRect)
                    output.rectOfInterest = rectConverted
                    
                }
            } catch {
                print(error)
            }
            
            // 스캔 세션이 시작된 후에 미리보기 레이어의 투명도를 조절
            DispatchQueue.main.async {
                self.animatePreviewLayerOpacity()
            }
        }
    }
    
    // MARK: - Video Preview Layer Setup

    /// 미리보기 레이어 생성 메서드
    private func setupVideoPreviewLayer(scanFocusRect: CGRect){
        DispatchQueue.main.async {
            // AVCaptureSession에서 나오는 비디오 스트림을 표시하기 위한 미리보기 레이어를 생성
            self.videoPreviewLayer = AVCaptureVideoPreviewLayer(session: self.captureSession)
            // 비디오 스트림의 비율 설정
            self.videoPreviewLayer.videoGravity = .resizeAspectFill
            
            // 미리보기 레이어의 프레임을 설정
            self.videoPreviewLayer.frame = self.scannerView.bounds
            // 현재 view의 레이어에 미리보기 레이어를 추가
            self.scannerView.layer.addSublayer(self.videoPreviewLayer)
            // opacity 설정으로 초기에 미리보기 영역을 숨김
            self.videoPreviewLayer.opacity = 0
            
            // Add UI elements on the scanner view
            self.setItemOnScanView(scanFocusRect: scanFocusRect)
            // 캡쳐 세션 시작
            self.startCaptureSession()

        }
    }
    
    // MARK: - UI Elements Setup
    /// ScanView에 올라갈 UI 요소들을 추가
    private func setItemOnScanView(scanFocusRect: CGRect) {
        // Dim
        setDimLayer(focusRect: scanFocusRect)
        
        // 사이에 스캔영역이 있음
        
        // Guide Label
        scannerView.addSubview(guideLabel)
        let labelOffset = scannerView.bounds.height * 0.08
        let labelTopConstant = scanFocusRect.minY + scanFocusRect.height + labelOffset
        NSLayoutConstraint.activate([
            guideLabel.topAnchor.constraint(equalTo: scannerView.topAnchor,
                                                 constant: labelTopConstant),
            guideLabel.centerXAnchor.constraint(equalTo: scannerView.centerXAnchor)
        ])
        
        // Focus Guide Image
        for position in QRFocusPosition.allCases {
            let imageView = self.addQRFocusImages(scanFocusRect: scanFocusRect,
                                                  type: position)
            self.scannerView.addSubview(imageView)
        }
    }
    
    private func setDimLayer(focusRect: CGRect) {
        // 딤 처리를 위한 shape Layer를 생성
        let maskLayer = CAShapeLayer()
        maskLayer.fillRule = .evenOdd
        maskLayer.frame = self.scannerView.bounds
        // 딤 처리할 영역을 패스로 정의
        let path = CGMutablePath()
        path.addRect(maskLayer.frame)
        path.addRect(focusRect)
        maskLayer.path = path
        
        // 딤 처리 색상 및 배경 설정
        maskLayer.fillColor = UIColor.black.withAlphaComponent(0.6).cgColor
        maskLayer.backgroundColor = UIColor.clear.cgColor
        
        // 딤 처리 레이어를 미리보기 레이어에 추가
        self.videoPreviewLayer.addSublayer(maskLayer)
    }
    
    private func addQRFocusImages(scanFocusRect: CGRect, type: QRFocusPosition) -> UIImageView {
        
        let qrFocusImageWidth: CGFloat = 20
        let qrFocusImageOffset: CGFloat = 3
        guard let image = UIImage(named: type.imageName) else {
            fatalError("Could not load image with name \(type.imageName)")
        }

        let imageView = UIImageView(image: image)
        imageView.frame.size = CGSize(width: qrFocusImageWidth, height: qrFocusImageWidth)

        switch type {
        case .topLeft:
            imageView.frame.origin = CGPoint(x: scanFocusRect.minX - qrFocusImageOffset,
                                             y: scanFocusRect.minY - qrFocusImageOffset)
        case .topRight:
            imageView.frame.origin = CGPoint(x: scanFocusRect.maxX - qrFocusImageWidth + qrFocusImageOffset,
                                             y: scanFocusRect.minY - qrFocusImageOffset)
        case .bottomLeft:
            imageView.frame.origin = CGPoint(x: scanFocusRect.minX - qrFocusImageOffset,
                                             y: scanFocusRect.maxY - qrFocusImageWidth + qrFocusImageOffset)
        case .bottomRight:
            imageView.frame.origin = CGPoint(x: scanFocusRect.maxX - qrFocusImageWidth + qrFocusImageOffset,
                                             y: scanFocusRect.maxY - qrFocusImageWidth + qrFocusImageOffset)
        }

        return imageView
    }

    
    // MARK: - Capture Session Control
    /// 캡쳐 세션 시작 메서드
    func startCaptureSession() {
        DispatchQueue.global(qos: .background).async {
            if !(self.captureSession.isRunning) {
                self.captureSession.startRunning()
            }
        }
    }
}

// MARK: - Delegate Methods
extension BarCodeScanViewController: CustomNavigationBarDelegate {
    
    func closeButtonTapped() {
        self.dismiss(animated: true)
    }
}

extension BarCodeScanViewController: AVCaptureMetadataOutputObjectsDelegate {
    
    // 메타데이터 출력 델리게이트 메서드로 바코드 스캔 결과를 처리합니다.
    func metadataOutput(_ output: AVCaptureMetadataOutput, didOutput metadataObjects: [AVMetadataObject], from connection: AVCaptureConnection) {
        DispatchQueue.main.async { [weak self] in
            if let metadataObject = metadataObjects.first as? AVMetadataMachineReadableCodeObject,
               let barcodeValue = metadataObject.stringValue {
                self?.showBarcodeAlert(barcodeValue)
                // 캡쳐 세션 종료
                self?.captureSession.stopRunning()
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


//
//  Extensions.swift
//  nbKorea
//
//  Created by bang_hyeonseok on 2023/09/04.
//  Copyright © 2023 Sim, Jae-Won. All rights reserved.
//
extension UIApplication {
    class var appDelegate: AppDelegate {
        return UIApplication.shared.delegate as! AppDelegate
    }
    
    class func topViewController(base: UIViewController? = UIApplication.shared.keyWindow?.rootViewController) -> UIViewController? {
        if let nav = base as? UINavigationController {
            return topViewController(base: nav.visibleViewController)
        }
        
        if let tab = base as? UITabBarController {
            if let selected = tab.selectedViewController {
                return topViewController(base: selected)
            }
        }
        
        if let presented = base?.presentedViewController {
            return topViewController(base: presented)
        }
        
        return base
    }
}

extension UIImage {
    func imageWithSize(_ size: CGSize) -> UIImage {
        if #available(iOS 9.0, *) {
            UIGraphicsBeginImageContextWithOptions(size, false, UIScreen.main.scale)
        } else {
            UIGraphicsBeginImageContextWithOptions(size, true, UIScreen.main.scale)
        }
        let rect = CGRect(x: 0.0, y: 0.0, width: size.width, height: size.height);
        draw(in: rect)
        
        let resultingImage = UIGraphicsGetImageFromCurrentImageContext();
        UIGraphicsEndImageContext();
        
        return resultingImage!
    }

}


extension UIDevice {
    
    func getNavigationBarHeight() -> (navBarHeight: CGFloat, topInset: CGFloat) {
        var navBarHeight: CGFloat = 0
        var topInset: CGFloat = 0

        // navigation Bar의 높이를 구하는 부분
        if #available(iOS 13.0, *) {
            // iOS 13 이상에서는 UIWindowScene을 사용하여 현재 UIWindowScene을 찾음
            if let windowScene = UIApplication.shared.connectedScenes.first as? UIWindowScene,
               let window = windowScene.windows.first,
               let rootViewController = window.rootViewController as? UINavigationController {
                // UIWindowScene에서 네비게이션 컨트롤러 및 네비게이션 바 높이 가져오기
                navBarHeight = rootViewController.navigationBar.frame.size.height
            }
        } else {
            // iOS 12 및 이전 버전에서만 사용 가능한 코드
            if let navigationController = UIApplication.shared.keyWindow?.rootViewController as? UINavigationController {
                // 네비게이션 컨트롤러의 네비게이션 바 높이 가져오기
                navBarHeight = navigationController.navigationBar.frame.size.height
            }
        }

        // notch 만큼의 길이를 구하는 부분
        if #available(iOS 15.0, *) {
            if let windowScene = UIApplication.shared.connectedScenes.first as? UIWindowScene {
                topInset = windowScene.windows.first?.safeAreaInsets.top ?? 0
                if topInset > 20 {
                    // iOS 15 이상에서는 UIWindowScene과 safeAreaInsets를 사용하여 처리
                    navBarHeight += topInset
                }
            }
        } else if #available(iOS 13.0, *) {
            if let windowScene = UIApplication.shared.connectedScenes.first as? UIWindowScene,
               let window = windowScene.windows.first {
                topInset = window.safeAreaInsets.top
                if topInset > 20 {
                    // iOS 13 이상에서는 UIWindowScene과 safeAreaInsets를 사용하여 처리
                    navBarHeight += topInset
                }
            }
        } else {
            // iOS 12 및 이전 버전에서만 사용 가능한 코드
            if let topSafeAreaInset = UIApplication.shared.delegate?.window??.safeAreaInsets.top, topSafeAreaInset > 20 {
                // iOS 12 이하에서는 기존 방식으로 처리
                navBarHeight += topSafeAreaInset
            }
        }

        return (navBarHeight, topInset)
    }
}


```

<br><br>

[[Top]](#순서)
<br>
<br>

### 전체코드 적용화면

<img src="https://github.com/isGeekCode/TIL/assets/76529148/d2993761-d004-4435-b159-2a27fe19b7c1" width="300">

<br><br>

[[Top]](#순서)
<br>
<br>




## History
- 230904 : 기본 사용법
- 230905 : 바코드 스캔영역 외 Dim처리방법 추가
- 230905 : 애니메이션 효과 추가
- 230905 : 스캐너에 텍스트 추가
- 230905 : 스캔영역 모서리에 이미지 추가하기
- 230908 : 스캔영역 제한 방법 추가
- 230908 : 색인 추가
