# Layout - SwiftUI: NavigationView


네비게이션뷰는 보통 한카테고리에 들어와서 세부주제로 들어갈 떄 사용한다. 

이와 반대로 탭바같은 경우는 대주제에 따라 달라진다.  

그래서 일반적인 앱의 구조는 아래와 같은 구조로 진행된다.  

- 탭바
    - 1번 탭 : 네비게이션1
        - 세부뷰 1-1
            - 세부뷰 1-2
    - 2번 탭 : 네비게이션2
        - 세부뷰 2-1
            - 세부뷰 2-2


## NavigationLink의 라벨에 Text만 있는 경우

<img width="300" alt="스크린샷 2023-11-27 오후 12 38 04" src="https://github.com/isGeekCode/TIL/assets/76529148/2c9e5a34-0586-4eac-bd79-05c92a63b44d">

이런 View가 있다고 가정해보자.  

```swift
import SwiftUI

struct ContentView: View {

    var body: some View {
        // 내부 컨텐츠
        Text("설정")
    }
}
```

- Step 1 : 여기에 내부 컨텐츠를 NavigationView { }로 감싸면 된다.  
- Step 2 : 그리고 내부에 NavigationLink를 생성한다. 




> 이 때, NavigationLink("이부분") 이부분에는 네비게이션 라벨에 표시할 문자열을 넣어준다.  
> Label부분과 destination부분이 있다. 
> destination에는 이동 후 표시할 View가 들어간다.  
> NavigationLink의 생김새에 따라 여러가지 형태의 이니셜라이저가 존재한다.  

```swift
struct ContentView: View {
    var body: some View {
        
        NavigationView {
        
                NavigationLink("설정으로") { // label
                    Text("설정")            // destination
                }
        }

    }
}
```

이러면 Text자체가 버튼처럼 되면서 네비게이션이 적용된다.  

<img width="300" alt="ezgif-5-8d564753f3" src="https://github.com/isGeekCode/TIL/assets/76529148/70d6f2dc-4912-4f71-a55b-4a36fb2656da">


이런식으로 여러 View들 사이에서 독자적으로 사용가능하다.  

```swift
struct ContentView: View {
    var body: some View {
        
        NavigationView {
            
            VStack {
                Text("에어플레인 모드")
                NavigationLink("설정으로") {
                        Text("설정")
                }
            }
        }
    }
}
```

이런 경우는 아래와 같이 생성된다.  

<img width="300" alt="스크린샷 2023-11-27 오후 12 51 36" src="https://github.com/isGeekCode/TIL/assets/76529148/2095ecbe-168b-4180-852e-985c080742d4">


### List인 경우

```swift
struct ContentView: View {
    var body: some View {
        
        List {
            Text("스크린타임")
            Text("에어플레인 모드")
        }
    }
}
```

<img width="300" alt="스크린샷 2023-11-27 오후 12 37 47" src="https://github.com/isGeekCode/TIL/assets/76529148/e9c407b0-5c3d-4287-93cd-1870e966298e">

만약 화면에 이렇게 리스트로 적용이 되어있는 경우,

여기에 navigationView를 적용하면 리스트에 자동으로 disclosure indicator가 생성된다.  


```swift
struct ContentView: View {
    var body: some View {
        
        NavigationView {
            
            List {
                NavigationLink("스크린타임") {
                        Text("스크린타임 페이지")
                }
                Text("에어플레인 모드")
            }
        }
    }
}
```

<img width="300" alt="ezgif-3-b7ee197810" src="https://github.com/isGeekCode/TIL/assets/76529148/0c65b36c-2d6d-479c-b427-354de57d3aaa">

### 문자열 이외의 View인 경우

NavigationLink()의 인자로 문자열이 들어가는 경우에는 앞선 형태로 가능하지만,

상황에 따라 Image나 혹은 리스트내부의 View 자체를 클릭했을 때, 네비게이션이 실행되는 경우도 있다. 


1. Image로 이동하기

```swift
struct ContentView: View {
    var body: some View {
        
        Image(systemName: "airplane")
            .resizable()
            .frame(width: 200,
                   height: 200)


    }
}
```

<img width="300" alt="스크린샷 2023-11-27 오후 1 06 20" src="https://github.com/isGeekCode/TIL/assets/76529148/cdee5255-d68b-4520-875f-fd72e101af95">

이런 이미지가 하나 있는데, 이 자체를 네비게이션 링크로 사용하려면 아래와 같이 사용한다. 

```swift
//기존의 문자열만 가지고 사용하는 경우
struct ContentView: View {
    var body: some View {
        NavigationView {

            NavigationLink("스크린타임") {   // label
                    Text("스크린타임 페이지")  // destination
            }
        }
    }
}   

// 문자열 이외의 label
struct ContentView: View {
    var body: some View {
        NavigationView {

            NavigationLink { 
                Text("에어플레인 모드")    // destination
            } label: {                 // label
                Image(systemName: "airplane")
                    .resizable()
                    .frame(width: 200,
                           height: 200)
            }
        }
    }
}   
```

이렇게 되면 아래와 같이 된다. 

<img width="300" alt="ezgif-5-8ef0007050" src="https://github.com/isGeekCode/TIL/assets/76529148/1fbed43d-349b-4d31-99fc-03721ff88625">


이번에는 List 내부에 세팅을 해보자.
이런 모양이 있다.  
  
```swift
struct ContentView: View {
    var body: some View {
        NavigationView {
            
            List {
                HStack {
                    Image(systemName: "wifi")
                        .resizable()
                        .aspectRatio(contentMode: .fit)
                        .frame(width: 20,
                               height: 20)
                        .padding(.all, 5)
                        .background(.blue)
                        .foregroundStyle(.white)
                        .cornerRadius(6)
                    
                    // 라벨로 만들고 싶은 부분
                    HStack {
                        Text("Wi-Fi")
                        Spacer()
                        Text("SK_WKF4DJ7KD")
                            .foregroundStyle(.gray)
                    }
                }
                
                Text("설정")
                Text("개인용 핫스팟")
                
                .navigationTitle(Text("설정"))
            }
        }
    }
}

```

여기에 라벨로 만들고 싶은 부분을 통채로 NavigationLink의 label View 부분에 넣어준다.  

```swift
struct ContentView: View {
    var body: some View {
        NavigationView {
            
            List {
                HStack {
                    Image(systemName: "wifi")
                        .resizable()
                        .aspectRatio(contentMode: .fit)
                        .frame(width: 20,
                               height: 20)
                        .padding(.all, 5)
                        .background(.blue)
                        .foregroundStyle(.white)
                        .cornerRadius(6)
                    
                    
                    NavigationLink { 
                        Text("Wi-Fi")   // destination
                    } label: { 
                        
                        HStack {
                            Text("Wi-Fi")
                            Spacer()
                            Text("SK_WKF4DJ7KD")
                                .foregroundStyle(.gray)
                        }
                    }

                }
                
                Text("설정")
                Text("개인용 핫스팟")
                
                .navigationTitle(Text("설정"))
            }
        }
    }
}

```

그러면 아래와 같이 세팅된다. 

<img width="300" alt="스크린샷 2023-11-27 오후 2 37 49" src="https://github.com/isGeekCode/TIL/assets/76529148/f0ef7b2b-5c95-4945-943a-202aa66148c2">


## NavigationTitle
이건 바로 위 예제 처럼 NavigationView 클로저 안에서 

`.navigationTitle("문자열")`형태로 입력하면 된다.  

## History
- 231127: 초안작성
