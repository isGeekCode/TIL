# 화면캡처 - 특정화면을 이미지로 저장하기

## 유의사항
이미지로 저장할 경우, `Info.plist`에  

`Privacy - Photo Library Additions Usage Description`가  

구현되어있어야한다. 

<br><br><br>

## 사용법
특정 View만 캡처하려면 지정한 View의 사이즈를 넣어준다.
화면 전체를 캡처하려면 Window를 통해 작업한다.

<br><br>
``` swift
    func captureDrawing() -> UIImage? {
        // 화면 전체를 저장
//        let window = UIApplication.shared.keyWindow
//        let screenSize = UIScreen.main.bounds.size
//        UIGraphicsBeginImageContextWithOptions(screenSize, false, 0)
//        window?.layer.render(in: UIGraphicsGetCurrentContext()!)

        // 지정한 이미지 부분만
        UIGraphicsBeginImageContext(drawingView.frame.size)
        drawingView.layer.render(in: UIGraphicsGetCurrentContext()!)
        
        
        let capturedImage = UIGraphicsGetImageFromCurrentImageContext()
        UIGraphicsEndImageContext()
        return capturedImage // 캡쳐된 이미지 반환
    }

    // 세이브 동작
    func saveAction() {
        if let image = captureDrawing() {
            UIImageWriteToSavedPhotosAlbum(image, nil, nil, nil) // 이미지 저장
            
            let alert = UIAlertController(title: "Saved", message: "Your drawing has been saved to Photos.", preferredStyle: .alert)
            alert.addAction(UIAlertAction(title: "OK", style: .default, handler: nil))
            present(alert, animated: true, completion: nil) // 저장 완료 알림
        }
    }

```

<br><br><br>

## History
- 230731: 초안작성
