# Layout - CodeUI: UILabel 고정폭 지정 이유 및 방법

## 📌 주제  
UILabel의 intrinsicContentSize로 인한 가변 폭 문제와 고정 길이 대응

<br>

## 📖 핵심 개념 요약  

`UILabel`은 기본적으로 자신의 콘텐츠 크기를 기준으로 intrinsicContentSize를 갖기 때문에 별도의 width 제약 없이도 레이아웃 설정이 가능하다.

하지만 이 크기는 **내용에 따라 가변적**이기 때문에, 동일한 위치에 배치된 레이블들이 서로 다른 크기를 가지게 된다.  
결과적으로 `UITableView`나 `UICollectionView`처럼 **반복되는 셀 구조 안에서 시각적으로 흐트러져 보이는 문제**가 발생한다.

특히 숫자처럼 **문자 폭이 가변적인 콘텐츠**는 `intrinsicContentSize`에 따라 자동 너비가 설정되면 들쭉날쭉한 UI를 유발할 수 있다. 이는 디자인적으로 불균형을 주고, 데이터 간 비교나 가독성을 떨어뜨린다.

아래 이미지를 보자.  
   

<img src="https://i.imgur.com/FDdykX6.png" width="300" />

<br>

특히 숫자가 포함되어있는 라벨인 경우, 그 오차가 심해진다. 
1이 가장 좁고 0이나 8은 가장 넓어진다. 시각적으로 구분하기 위해 색상을 넣어보자.  

<br>

<img src="https://i.imgur.com/Yj6syyD.png" width="300" />




<br><br>

## 🛠 해결 또는 적용 방식  
이 문제를 해결하기 위해 다음과 같은 방식으로 대응했다:

- **UILabel의 가로 길이를 고정값으로 제약**  
  오토레이아웃에서 `widthAnchor.constraint(equalToConstant:)`를 이용해 일정한 폭을 지정함으로써 셀 간 정렬이 맞춰지도록 함.

- **좌측 정렬 사용**  
  `label.textAlignment = .left`로 텍스트 정렬 기준을 명확히 하여 동일한 가로 폭 내에서 일관된 시각적 흐름을 유도함.

```swift
label.textAlignment = .left
label.widthAnchor.constraint(equalToConstant: 80).isActive = true
```


아래 이미지는 이제 고정 가로 길이를 적용한 이미지이다. 
파랑 라벨을 먼저 생성하고, 
해당 leading에 맞춰  노랑 라벨의 leading을 생성했다. 
노랑 라벨의 width를 고정값 추가,
이후 `-`가 표시된 부분을 추가, 빨강 라벨의 leading을 추가했다. 

<br>


<img src="https://i.imgur.com/uDfX3bd.png" width="300" />

<br>


이제 색상을 없앤 결과를 보자. 

<br>


<img src="https://i.imgur.com/ZM2Aony.png" width="300" />

<br>


들쭉 날쭉한 모습이 사라졌다.  



<br>
<br>

## 🔍 참고 자료  
- [Apple Developer Docs – UILabel](https://developer.apple.com/documentation/uikit/uilabel)

## History
- 250508: 초안작성
