# Sample App : 설정앱 - SwiftUI



## Text나열
```swift

VStack {
    Text("설정")
    Text("스크린타임")
    Text("에어플레인 모드")
    Text("Wi-Fi")
    Text("셀룰러")
    Text("개인용 핫스팟")
    Text("일반")
    Text("손쉬운 사용")
    Text("개인정보 보호 및 보안")
    Text("암호")
    Text("개발자")
}

```

## Section 분리

리스트와 섹션으로 분리


```swift
VStack {
    List {
        Section {
            Text("스크린타임")
        }
        
        Section {
            Text("에어플레인 모드")
            Text("Wi-Fi")
            Text("셀룰러")
            Text("개인용 핫스팟")
        }
        
        Section {
            Text("일반")
            Text("손쉬운 사용")
            Text("개인정보 보호 및 보안")
        }
        
        Section {
            Text("암호")
            Text("개발자")
        }
    }
}

```

<br><br>

## Navigation 세팅하기

### NavigationTitle


```swift

VStack {
    NavigationView {
        List {
            Section {
                Text("스크린타임")
            }
            
            Section {
                Text("에어플레인 모드")
                Text("Wi-Fi")
                Text("셀룰러")
                Text("개인용 핫스팟")
            }
            
            Section {
                Text("일반")
                Text("손쉬운 사용")
                Text("개인정보 보호 및 보안")
            }
            
            Section {
                Text("암호")
                Text("개발자")
            }
        }
        .navigationTitle(Text("설정"))
    }
}
```

<br><br>

### NavigationLink

원하는 Row를 NavigationLink로 세팅하면 다음페이지로 세팅이 된다.  

전체 구조는 아래와 같다.   
```
ContentView
  └ VStack
      └ NavigationView  
            └ List  
                ├ Section  
                │   └ NavigationLink  
                │       └ Text("스크린타임")
                └ Section  
                    └ NavigationLink  
                        └ Text("에어플레인 모드)
```

네비게이션 링크는 아래와 같이 세팅한다.  
NavigationLink() 괄호안에 들어가는 것이 트리거가 될 Text형태이고,

클로저 내부에 있는 부분이 이동해서 보여줄 부분이다.  

```swift
Section {
    NavigationLink("스크린타임") { 
        Text("스크린타임")
    }
}

```

이걸 전체 적용하면

```swift

VStack {
    NavigationView {
        List {
            Section {
                NavigationLink("스크린타임") { 
                    Text("스크린타임")
                }
            }
            
            Section {
                
                NavigationLink("에어플레인 모드") { 
                    Text("에어플레인 모드")
                }
                NavigationLink("Wi-Fi") { 
                    Text("Wi-Fi")
                }
                NavigationLink("셀룰러") { 
                    Text("셀룰러")
                }
                NavigationLink("개인용 핫스팟") { 
                    Text("개인용 핫스팟")
                }

            }
            
            Section {
                NavigationLink("일반") { 
                    Text("일반")
                }
                NavigationLink("손쉬운 사용") { 
                    Text("손쉬운 사용")
                }
                NavigationLink("개인정보 보호 및 보안") { 
                    Text("개인정보 보호 및 보안")
                }
            }
            
            Section {
                NavigationLink("암호") { 
                    Text("암호")
                }
                NavigationLink("개발자") { 
                    Text("개발자")
                }
            }
        }
        .navigationTitle(Text("설정"))
    }
}
```

<br><br>

### 적용화면
<img width="300" alt="ezgif-4-98397e0be6" src="https://github.com/isGeekCode/TIL/assets/76529148/eae703b2-f21f-4980-b1fc-a9d5d11575eb">

<br><br>

## 이미지 추가

이제 List의 Row별로 이미지를 만들어보자.  

자주 헷갈리는 부분이 padding의 위치이다.  

보통은 색상을 설정한 다음에 확인을 하며 패딩을 넣기 때문에 색상 아래에 넣곤 하는데  
그게 아니라 frame아래에 있어야 프레임에서 패딩이 생긴다.  


```swift
Image(systemName: "hourglass").resizable()
    .aspectRatio(contentMode: .fit)
    .frame(width: 20,
           height: 20)
    .padding(.all, 5)  // 주의
    .background(.indigo)
    .foregroundStyle(.white)
    .cornerRadius(6)

```

<br><br>

이제  이 이미지는 네비게이션 링크가 적용된  TextView의 옆에 위치해야하기 때문에
Section 안에 HStack을 만들고,   
 Image, NavigationLink 의 순서로 넣어준다.  

<br><br>

```swift
Section {
    HStack {

        Image(systemName: "hourglass").resizable()
            .aspectRatio(contentMode: .fit)
            .frame(width: 20,
                   height: 20)
            .padding(.all, 5)
            .background(.indigo)
            .foregroundStyle(.white)
            .cornerRadius(6)

        NavigationLink("스크린타임") { 
            Text("스크린타임")
        }
    }
}
```

변경된 구조는 아래와 같다.  

<br><br>

```
ContentView
  └ VStack
      └ NavigationView  
            └ List  
                ├ Section  
                │   ├ Image
                │   └ NavigationLink  
                │       └ Text("스크린타임")
                └ Section
                    ├ Image
                    └ NavigationLink  
                        └ Text("에어플레인 모드)
```


<br><br>

### 적용화면

<img width="300" alt="스크린샷 2023-11-24 오전 8 53 35" src="https://github.com/isGeekCode/TIL/assets/76529148/921e1e32-80cd-47b2-93cd-7783eaf768bc">

<br><br>

## 프로필 섹션 구현

<img width="400" alt="스크린샷 2023-11-24 오전 9 20 06" src="https://github.com/isGeekCode/TIL/assets/76529148/85e938b4-c33d-44b4-bfb8-5c2509a3fc12">

프로필 섹션 UI를 짜기 위해서는 아래 구조와 같이 된다.  
```
├ Section  // 프로필 섹션
│   └ HStack
│       ├ Image  // 프로필 사진
│       └ VStack  
│           ├ Text("방현석")
│           └ Text("Apple ID, iCloud+ 미디어 및 구입 항목")
│
└ Section // 다른 일반 섹션
    ├ Image
    └ NavigationLink  
        └ Text("에어플레인 모드)
```

### 프로필 섹션 UI

프로필 이미지는 다른 섹션의 일반 아이콘 이미지와 달리 동그란 이미지를 가지고 있다.   
또한 아이콘 자체가 fill로 되어있어서 배경색은 clear가 되어야한다.  

근데 만약 이 곳에. 다른 이미지가 들어간다면 이미지에 .clipShape(Circle())로 처리해야할텐데 그건 어떻게 해야할까.... 일단 나중에 생각..

- 이미지 세부설정
- VSatck 내부 폰트설정
- VStack 내부를 왼쪽정렬처리

```swift
HStack {
    Image(systemName: "person.crop.circle.fill")
        .resizable()
        .aspectRatio(contentMode: .fit)
        .frame(width: 50,
               height: 50)
        .foregroundStyle(.gray)
    
//    VStack {
    VStack(alignment: .leading) {
        Text("방현석")
            .font(.system(size: 24))
            .fontWeight(.regular)
        Text("Apple ID, iCloud+ 미디어 및 구입 항목")
            .font(.system(size: 11))
    }
}
```

### 프로필섹션 padding 처리

각 필요한 부분에 padding을 넣어보자.  
padding의 방향은 아래와 같은 종류가 있다.  
- .all
- .horizontal
- .vertical
- .top
- .bottom
- .leading
- .trailing

```swift
.padding(어떤 방향으로 padding을 넣을지, 값)
```

이제 적용해보자.  

```swift
HStack {
    Image(systemName: "person.crop.circle.fill")
        .resizable()
        .aspectRatio(contentMode: .fit)
        .frame(width: 50,
               height: 50)
        .padding(.all, 4)
        .foregroundStyle(.gray)
    
    VStack(alignment: .leading, spacing: 3) {
        Text("방현석")
            .font(.system(size: 24))
            .fontWeight(.regular)
        Text("Apple ID, iCloud+ 미디어 및 구입 항목")
            .font(.system(size: 11))

    }
    .padding(.leading, 4)
}
.padding(.vertical, 10)

```

<br><br>

### 프로필섹션 NavigationLink
 
 다른 네비게이션 링크는 Text를 눌렀을때, 네비게이션 링크가 실행되는 것이었다. 
 
 그런데 이번에는 Text도 2개이고 섹션 자체를 클릭할 때, 이동시키려고 한다.  

그래서 이번엔 Navigation Link를 이용할 때, destination파라미터를 이용한다.  

destination 부분이 이동후 보여줄 View
label부분이 네비게이션 라벨이다.  

```swift
// 사용할 파라미터
NavigationLink(destination: <#T##() -> View#>, label: <#T##() -> View#>)

NavigationLink { 
    Text("프로필 화면")
    
} label: { 
    // 네비게이션 라벨 부분
}
```

이 네비게이션 라벨 부분에 구현한 프로필 섹션의 HStack를 넣어준다.
이 HStack 자체가 네비게이션링크로 이동할 라벨이 되는 것이다.    


```swift
NavigationLink { 
    Text("프로필 화면")
} label: { 
    // 네비게이션 라벨 부분
    HStack {
    Image(systemName: "person.crop.circle.fill")
        .resizable()
        .aspectRatio(contentMode: .fit)
        .frame(width: 50,
               height: 50)
        .foregroundStyle(.gray)
    
    VStack(alignment: .leading) {
        Text("방현석")
            .font(.system(size: 24))
            .fontWeight(.regular)
        Text("Apple ID, iCloud+ 미디어 및 구입 항목")
            .font(.system(size: 11))
    }
}
}
```

<br><br>

### 적용화면
<img width="300" alt="ezgif-2-4b906461ad" src="https://github.com/isGeekCode/TIL/assets/76529148/cde644f3-ff2c-4dcc-a8b1-364d2cbe0fdc">

<br><br>


## History
- 231123: 네비게이션링크 적용하기




```swift

```

```swift

```
```swift

```

```swift

```

```swift

```
