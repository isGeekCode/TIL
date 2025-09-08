
<br><br>
---

## 개요  
iOS 앱에서 커스텀 폰트를 적용하는 방법에 대해 설명한다. 기본 시스템 폰트 외에 원하는 폰트를 사용하여 앱 디자인을 다양화할 수 있다.

<br><br>
---

## 시작하기 전에 알아두면 좋은 것들  
- 커스텀 폰트 파일은 주로 `.ttf` 또는 `.otf` 형식을 사용가능. 
- 폰트 파일을 프로젝트에 포함시키고 Info.plist에 등록해야 한다. 
- 폰트 이름은 폰트 파일 내에 정의된 정확한 이름을 사용해야 한다.  
- 시뮬레이터와 실제 디바이스에서 폰트가 다르게 보일 수 있으므로 주의가 필요하다.

<br><br>
---

## 개념 정리 / 기본 구조  
1. 커스텀 폰트 파일을 프로젝트에 추가한다.  
2. Info.plist 파일에 `Fonts provided by application` (또는 `UIAppFonts`) 항목을 추가하고, 폰트 파일명을 배열로 등록한다.  
3. 코드에서 사용할 땐,  `UIFont(name:size:)`를 사용해 폰트를 적용한다.

<br><br>
---

## 예제 코드로 이해하기  
```swift
// 1. 폰트를 로드하여 UILabel에 적용하는 예제
if let customFont = UIFont(name: "CustomFontName", size: 17) {
    label.font = customFont
} else {
    print("Failed to load the custom font.")
}
```

<br><br>
---

## 실무 적용 포인트  
- 폰트 이름은 Xcode에서 직접 확인하거나 macOS의 Font Book 앱에서 확인할 수 있다.  
- 폰트가 정상적으로 로드되지 않으면 파일명과 폰트 이름이 일치하는지, Info.plist에 올바르게 등록되었는지 점검한다.  
- Dynamic Type과 호환되도록 폰트를 설정하면 접근성을 높일 수 있다.

<br><br>
---

## 확장 개념 / 보충 설명  
- 커스텀 폰트를 코드에서 동적으로 로드하는 방법이 있다.  
- 여러 폰트 스타일(Regular, Bold, Italic 등)을 각각 등록하여 사용할 수 있다.  
- SwiftUI에서는 `.custom` 폰트 모디파이어를 사용해 폰트를 적용할 수 있다.

<br><br>
---

## 요약 정리  
iOS에서 커스텀 폰트를 적용하려면 폰트 파일을 프로젝트에 추가하고 Info.plist에 등록한 뒤, 코드에서 해당 폰트를 지정하면 된다. 정확한 폰트 이름 확인과 plist 설정이 중요하며, Dynamic Type 지원을 고려하면 사용자 경험을 향상시킬 수 있다.

<br><br>
---

## HISTORY  
- 2024-06-01: 최초 작성

<br><br>
---
