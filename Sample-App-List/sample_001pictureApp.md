# sample App - 그림판앱



그림판의 요소는 아래와 같다.

- 최소기능
    - 그려질 화면
    - 터치인식하여 선그리기 기능
    - 리셋
    
- 추가기능
    - 이미지 저장
    - 공유하기
    - 그리기 도구 변경
    - 그리기 색상 변경
    - 텍스트 입력
    - 이미지 붙여넣기


```swift
import UIKit

class ViewController: UIViewController {
    
    @IBOutlet weak var drawingView: UIView! // 그리기 뷰
    var lastPoint: CGPoint? // 마지막 터치 지점

    override func viewDidLoad() {
        super.viewDidLoad()
    }
    
    // MARK: Drawing 구현
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        if let touch = touches.first {
            lastPoint = touch.location(in: drawingView) // 터치 시작 지점 저장
        }
    }

    override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?) {
        if let touch = touches.first,
           let lastPoint = lastPoint {
            let currentPoint = touch.location(in: drawingView) // 현재 터치 지점
            drawLine(from: lastPoint, to: currentPoint) // 선 그리기
            print("lastPoint: \(lastPoint)")
            self.lastPoint = currentPoint
        }
    }

    func drawLine(from fromPoint: CGPoint, to toPoint: CGPoint) {
        UIGraphicsBeginImageContext(drawingView.frame.size)
        guard let context = UIGraphicsGetCurrentContext() else { return }
        drawingView.layer.render(in: context)
        context.move(to: fromPoint)
        context.addLine(to: toPoint)
        context.setLineWidth(5) // 선 굵기
        context.setStrokeColor(UIColor.black.cgColor) // 선 색상
        context.strokePath()

        drawingView.layer.contents = UIGraphicsGetImageFromCurrentImageContext()?.cgImage
        UIGraphicsEndImageContext()
    }
}


// MARK: BtnAction
extension ViewController {
    
    // 화면 캡쳐하기
    func captureDrawing() -> UIImage? {
        UIGraphicsBeginImageContext(drawingView.frame.size)
        drawingView.layer.render(in: UIGraphicsGetCurrentContext()!)
        let capturedImage = UIGraphicsGetImageFromCurrentImageContext()
        UIGraphicsEndImageContext()
        return capturedImage // 캡쳐된 이미지 반환
    }
    
    
    @IBAction func resetAction(_ sender: Any) {
        drawingView.layer.contents = nil // 그리기 뷰 리셋
    }
    
    @IBAction func saveAction(_ sender: Any) {
        if let image = captureDrawing() {
            UIImageWriteToSavedPhotosAlbum(image, nil, nil, nil) // 이미지 저장
            
            let alert = UIAlertController(title: "Saved", message: "Your drawing has been saved to Photos.", preferredStyle: .alert)
            alert.addAction(UIAlertAction(title: "OK", style: .default, handler: nil))
            present(alert, animated: true, completion: nil) // 저장 완료 알림
        }
    }
    @IBAction func shareAction(_ sender: Any) {
        if let image = captureDrawing() {
            let activityViewController = UIActivityViewController(activityItems: [image], applicationActivities: nil)
            present(activityViewController, animated: true, completion: nil) // 이미지 공유
        }
    }
}


```
<br><br>

[[top]](#-sample-app---그림판앱)

<br><br><br>


## History
- 230731 : 초안작성
