# Layout - SwiftUI: Spacer

아래 코드는 Image, Text, Button 이 VStack안에 구성되어있다.
<table>
  <tr>
    <td>

      ```swift
      VStack{
            Image(systemName: "bolt")
              .resizable()
              .aspectRatio(contentMode: .fit)
              .frame(width: 200)
              .background(.yellow)
              .foregroundColor(.red)
       
            Text("Bolt Icon")
            
            Button {
              print("Button Touch up")
            } label: {
              Text("Hit")
            }
          }
      ```

    </td>
    <td>
      <img width="238" alt="이미지 설명" src="https://user-images.githubusercontent.com/76529148/224518972-2bb24991-cb19-4493-b944-8f74cb1e0296.png">
    </td>
  </tr>
</table>

## VStack내부에 Spacer 넣기 - 1
Space를 Text와 Button사이에 넣어주면 그림과 같이 공간이 생긴다. 

<table>
  <tr>
    <td>

      ```swift
      VStack{
            Image(systemName: "bolt")
              .resizable()
              .aspectRatio(contentMode: .fit)
              .frame(width: 200)
              .background(.yellow)
              .foregroundColor(.red)
       
            Text("Bolt Icon")
            
            Spacer() // 공간 생성
            Button {
              print("Button Touch up")
            } label: {
              Text("Hit")
            }

          }
      ```

    </td>
    <td>
      <img width="238" alt="이미지 설명" src="https://user-images.githubusercontent.com/76529148/224518974-47efe230-51f3-47b9-a7e4-39c08251b1a6.png">
    </td>
  </tr>
</table>

## VStack내부에 Spacer 넣기 - 2
Space를 Image와 Text 사이에 동일하게 Spacer를 넣어주면 동일한 간격이 생긴다. 

<table>
  <tr>
    <td>

      ```swift
      VStack{
            Image(systemName: "bolt")
              .resizable()
              .aspectRatio(contentMode: .fit)
              .frame(width: 200)
              .background(.yellow)
              .foregroundColor(.red)
       
            Text("Bolt Icon")
            
            Spacer() // 공간 생성
            Button {
              print("Button Touch up")
            } label: {
              Text("Hit")
            }

          }
      ```

    </td>
    <td>
      <img width="238" alt="이미지 설명" src="https://user-images.githubusercontent.com/76529148/224518975-72f41eab-e1d3-4289-9e2c-a79ad7eca955.png">
    </td>
  </tr>
</table>

## VStack내부에 HStack 넣기
VStack내부에 HStack을 구성하여 이안에도 Spacer를 이용할 수 있다.

단순하게 Spacer를 넣기만 하면 HStack의 양끝까지 객체가 이동하기 때문에 아래처럼 HStack자체에 padding을 주면 그림과 같이 안여백이 생긴다. 
<table>
  <tr>
    <td>

      ```swift
      VStack{
            Image(systemName: "bolt")
              .resizable()
              .aspectRatio(contentMode: .fit)
              .frame(width: 200)
              .background(.yellow)
              .foregroundColor(.red)
       
             HStack {
                 Image(systemName: "heart")
                 Spacer()
                 Text("Heart Icon")
            }.padding(30)   

         
            Spacer() 
            Button {
              print("Button Touch up")
            } label: {
              Text("Hit")
            }

          }
      ```

    </td>
    <td>
      <img width="238" alt="이미지 설명" src="https://user-images.githubusercontent.com/76529148/224518978-71926ff4-2fda-4c24-b28f-0d36dc91d49e.png">
    </td>
  </tr>
</table>

## HStack의 범위살펴보기
HStack의 범위를 보기위해 padding에 색상을 넣어보면 아래와 같다.
<img width="225" alt="스크린샷 2023-03-12 오전 10 16 08" src="">

<table>
  <tr>
    <td>

      ```swift
      VStack{
            Image(systemName: "bolt")
              .resizable()
              .aspectRatio(contentMode: .fit)
              .frame(width: 200)
              .background(.yellow)
              .foregroundColor(.red)
       
             HStack {
                 Image(systemName: "heart")
                 Spacer()
                 Text("Heart Icon")
            }.padding(30).background(.green)
         
            Spacer() 
            Button {
              print("Button Touch up")
            } label: {
              Text("Hit")
            }
      }
      ```

    </td>
    <td>
      <img width="238" alt="이미지 설명" src="https://user-images.githubusercontent.com/76529148/224518982-69b9f132-af1f-4c05-8ff1-474ca3b7846e.png">
    </td>
  </tr>
</table>
