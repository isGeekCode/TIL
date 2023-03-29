# Layout - 이미지 컨텐츠 모드 (ContentMode)

매번 헷갈려서 이리저리 수정해보는 컨텐츠 모드는.. 이제 더이상 헷갈리지말자..


iOS에서 UIImageView에서 이미지를 표시할 때 사용되는 ContentMode는 이미지의 크기가 뷰의 크기와 일치하지 않을 때 이미지의 크기를 조정하는 방법을 결정한다.

ContentMode는 UIView 클래스에서 상속받고 이미지 뷰에서 사용된다. 

ContentMode는 UIViewContentMode 열거형으로 정의되며, 다양한 옵션을 제공한다. 


## 주로 사용하는 ContentMode
- Scale to Fill
    - 이미지의 비율을 유지하지 않고 뷰의 크기에 맞게 이미지를 확대 또는 축소한다.
    - 이미지가 왜곡될 수 있다.
    
- Aspect Fit
    - 이미지의 비율을 유지하면서 뷰의 크기에 맞게 이미지를 축소한다.
    - 뷰의 크기보다 이미지가 작아질 수 있다.
    
- Aspect Fill
    - 이미지의 비율을 유지하면서 뷰의 크기에 맞게 이미지를 확대한다.
    - 뷰의 크기보다 이미지가 커질 수 있다.
    
- Center
    - 이미지를 뷰의 중앙에 정렬한다. 이미지가 뷰보다 크면 이미지의 일부가 잘리게 된다.

이외에도 ContentMode에는 Top, Bottom, Left, Right 등 다양한 옵션이 있다. 개발자는 각각의 상황에 맞게 적절한 ContentMode를 선택해야한다.


## ContentMode별 이미지 표시 
<img width="955" alt="스크린샷 2023-03-29 오전 10 35 07" src="https://user-images.githubusercontent.com/76529148/228403784-d833ac70-159f-4007-b2fa-eee2518e180f.png">  

- 이미지 출처 : [핀터레스트](https://i.pinimg.com/564x/16/22/31/162231131a07dda331e720811b87f9d8.jpg)
