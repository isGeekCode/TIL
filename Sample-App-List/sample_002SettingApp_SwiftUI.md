# Sample App : 설정앱 - SwiftUI


<br>

설정앱의 기능은 아래와 같다.

- 최소기능
    - 그려질 화면
    - 섹션 분리
    - 셀타입분기처리
    - 디테일화면 이동

<br><br>

## Contents
1. [최종화면](#최종화면)
2. [Text나열](#Text나열)
3. [Section 분리](#Section-분리)
4. [Navigation 세팅하기](#Navigation-세팅하기)
    - [NavigationTitle](#NavigationTitle)
    - [NavigationLink](#NavigationLink)
    - [적용화면_1](#적용화면_1)
5.    [이미지 추가](#이미지-추가)
    - [적용화면_2](#적용화면_2)
6. [프로필 섹션 구현](#프로필-섹션-구현)
    - [프로필 섹션 UI](#프로필-섹션-UI)
    - [프로필섹션 padding 처리](#프로필섹션-padding-처리)
    - [프로필섹션 NavigationLink](#프로필섹션-NavigationLink)
    - [적용화면_3](#적용화면_3)
7. [셀 디테일](#셀-디테일)
    - [Toggle과 State](#Toggle과-State)
    - [Spacer](#Spacer)
    - [적용화면_4](#적용화면_4)
8. [리팩토링](#리팩토링)
    - [ViewBuilder를 이용해 View분리하기](#ViewBuilder를-이용해-View분리하기)
    - [셀의 타입별로 분리해보기](#셀의-타입별로-분리해보기)
        - [ViewBuilder를 이용해 View분리하기](#ViewBuilder를-이용해-View분리하기)
        - [escaping 적용하기](#escaping-적용하기)
        - [객체분리하기](#객체분리하기)
9. [최종코드](#최종코드)


<br><br>

## 최종화면
<img width="300" alt="ezgif-2-71860cf113" src="https://github.com/isGeekCode/TIL/assets/76529148/afd61568-a82d-4afa-a395-0462f2579851">

<br><br>

[[Top]](#contents)

<br><br><br>

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

<br><br>

[[Top]](#contents)

<br><br><br>

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

[[Top]](#contents)

<br><br><br>

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

[[Top]](#contents)

<br><br><br>

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

[[Top]](#contents)

<br><br><br>

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

[[Top]](#contents)

<br><br><br>

## 프로필 섹션 구현

<img width="400" alt="스크린샷 2023-11-24 오전 9 20 06" src="https://github.com/isGeekCode/TIL/assets/76529148/85e938b4-c33d-44b4-bfb8-5c2509a3fc12">

<br><br>

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

<br><br>

[[Top]](#contents)

<br><br><br>

### 프로필 섹션 UI

프로필 이미지는 다른 섹션의 일반 아이콘 이미지와 달리 동그란 이미지를 가지고 있다.   
또한 아이콘 자체가 fill로 되어있어서 배경색은 clear가 되어야한다.  

근데 만약 이 곳에. 다른 이미지가 들어간다면 이미지에 .clipShape(Circle())로 처리해야할텐데 그건 어떻게 해야할까.... 일단 나중에 생각..

- 이미지 세부설정
- VSatck 내부 폰트설정
- VStack 내부를 왼쪽정렬처리

<br><br>

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

<br><br>

[[Top]](#contents)

<br><br><br>

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

[[Top]](#contents)

<br><br><br>

### 프로필섹션 NavigationLink
 
 다른 네비게이션 링크는 Text를 눌렀을때, 네비게이션 링크가 실행되는 것이었다. 
 
 그런데 이번에는 Text도 2개이고 섹션 자체를 클릭할 때, 이동시키려고 한다.  

그래서 이번엔 Navigation Link를 이용할 때, destination파라미터를 이용한다.  

destination 부분이 이동후 보여줄 View
label부분이 네비게이션 라벨이다.  

```swift
// 사용할 이니셜라이져
NavigationLink(destination:label:)

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
        // 아이콘 이미지
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

[[Top]](#contents)

<br><br><br>


## 셀 디테일

### Toggle과 State
에어플레인 같은 경우는 토글 스위치가 들어있다.  

```swift
Toggle(titleKey:isOn:)
```

isOn이라는 Bool타입 변수를 사용하려면 State를 알아야한다.  

```swift

struct ContentView: View {
    
    @State private var isAirplainModeOn: Bool = false
    
    var body: some View { }
```

State는 body밖에서 선언을 해줘야한다.  

> SwiftUI의 View는 Struct로 되어있다.  
> Struct는 어떤 값을 변경한다고 같이 딸려서 움직이는 것이 아니라,  
> 하나의 인스턴스를 만들면 변경하기 힘들다.  
> 한번 View를 그리고 State 변수가 바뀌면 View를 다시 그린다.  

@State가 붙어있음으로 바라보고 있을 수 있게 한다.  

이 값을 사용할 땐 아래처럼 이 State를 사용한 변수앞에 $를 같이 사용한다. 

```swift
Toggle("에어플레인 모드", isOn: $isAirplainModeOn)
```



<br><br>

[[Top]](#contents)

<br><br><br>

### Spacer

Wi-fi화면 같은 경우는 기존의 Text 하나로 했던 구조와 달리,  
Text와 Text 사이에 공백이 있다.  

<br><br>

<img width="400" alt="스크린샷 2023-11-24 오후 1 33 38 2" src="https://github.com/isGeekCode/TIL/assets/76529148/caf37815-ce59-498b-b197-59dce9842c8a">

<br><br>

이걸 구현하려면  HStack안에 Text Spacer Text 순으로 배치 되어야한다.  

```swift
HStack {
    Text("Wi-Fi")
    Spacer()
    Text("SK_WKF4DJ7KD")
        .foregroundStyle(.gray)
}
```

<br><br>

그리고 이 HStack은 기존의 NavigationLink의 Label이 된다.  

```swift
//    NavigationLink("Wi-Fi") { 
//        Text("Wi-Fi")
//    }

NavigationLink { 
    // destination 에 표시될 View
    Text("Wi-Fi")
} label: { 
    // label로 표시될 View
    HStack {
        Text("Wi-Fi")
        Spacer()
        Text("SK_WKF4DJ7KD")
            .foregroundStyle(.gray)
    }
}
```

<br><br>

### 적용화면

<img width="300" alt="스크린샷 2023-11-24 오후 1 45 08" src="https://github.com/isGeekCode/TIL/assets/76529148/89f8fa17-916f-4c65-9569-088d487b301b">

<br><br>

[[Top]](#contents)

<br><br><br>

## 리팩토링
여기까지 만드는 데 200줄이 넘는 코드를 만들었다.  

<details>
<summary>토글 접기/펼치기</summary>
<div markdown="1">

```swift
import SwiftUI

struct ContentView: View {
    
    @State private var isAirplainModeOn: Bool = false
    
    var body: some View {
        VStack {
            NavigationView {
                List {
                    
                    Section {
                        NavigationLink { 
                            // destination
                            Text("프로필 화면")
                        } label: { 
                            // 네비게이션 라벨 부분
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
                        }
                    }
                    
                    Section {
                        HStack {
                            Image(systemName: "hourglass")
                                .resizable()
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
                    
                    Section {
                        HStack {
                            Image(systemName: "airplane")
                                .resizable()
                                .aspectRatio(contentMode: .fit)
                                .frame(width: 20,
                                       height: 20)
                                .padding(.all, 5)
                                .background(.orange)
                                .foregroundStyle(.white)
                                .cornerRadius(6)
                            
                            
                            // 에어플레인                            
                            Toggle("에어플레인 모드", isOn: $isAirplainModeOn)
                        }
                        
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
                                Text("Wi-Fi")
                            } label: { 
                                HStack {
                                    Text("Wi-Fi")
                                    Spacer()
                                    Text("SK_WKF4DJ7KD")
                                        .foregroundStyle(.gray)
                                }
                            }
                        }
                        
                        HStack {
                            Image(systemName: "antenna.radiowaves.left.and.right")
                                .resizable()
                                .aspectRatio(contentMode: .fit)
                                .frame(width: 20,
                                       height: 20)
                                .padding(.all, 5)
                                .background(.green)
                                .foregroundStyle(.white)
                                .cornerRadius(6)
                            
                            NavigationLink("셀룰러") { 
                                Text("셀룰러")
                            }
                        }
                        
                        HStack {
                            Image(systemName: "personalhotspot")
                                .resizable()
                                .aspectRatio(contentMode: .fit)
                                .frame(width: 20,
                                       height: 20)
                                .padding(.all, 5)
                                .background(.green)
                                .foregroundStyle(.white)
                                .cornerRadius(6)
                            
                            NavigationLink("개인용 핫스팟") { 
                                Text("개인용 핫스팟")
                            }
                        }
                        
                    }
                    
                    Section {
                        HStack {
                            Image(systemName: "gear")
                                .resizable()
                                .aspectRatio(contentMode: .fit)
                                .frame(width: 20,
                                       height: 20)
                                .padding(.all, 5)
                                .background(.gray)
                                .foregroundStyle(.white)
                                .cornerRadius(6)
                            
                            NavigationLink("일반") { 
                                Text("일반")
                            }
                        }
                        
                        HStack {
                            Image(systemName: "accessibility")
                                .resizable()
                                .aspectRatio(contentMode: .fit)
                                .frame(width: 20,
                                       height: 20)
                                .padding(.all, 5)
                                .background(.blue)
                                .foregroundStyle(.white)
                                .cornerRadius(6)
                            NavigationLink("손쉬운 사용") { 
                                Text("손쉬운 사용")
                            }
                        }
                        
                        HStack {
                            Image(systemName: "hand.raised.fill")
                                .resizable()
                                .aspectRatio(contentMode: .fit)
                                .frame(width: 20,
                                       height: 20)
                                .padding(.all, 5)
                                .background(.blue)
                                .foregroundStyle(.white)
                                .cornerRadius(6)
                            NavigationLink("개인정보 보호 및 보안") { 
                                Text("개인정보 보호 및 보안")
                            }
                        }
                    }


                    
                    Section {
                        HStack {
                            Image(systemName: "key.fill")
                                .resizable()
                                .aspectRatio(contentMode: .fit)
                                .frame(width: 20,
                                       height: 20)
                                .padding(.all, 5)
                                .background(.gray)
                                .foregroundStyle(.white)
                                .cornerRadius(6)
                            NavigationLink("암호") { 
                                Text("암호")
                            }
                        }
                        
                        HStack {
                            Image(systemName: "hammer.fill")
                                .resizable()
                                .aspectRatio(contentMode: .fit)
                                .frame(width: 20,
                                       height: 20)
                                .padding(.all, 5)
                                .background(.gray)
                                .foregroundStyle(.white)
                                .cornerRadius(6)
                            
                            NavigationLink("개발자") { 
                                Text("개발자")
                            }
                        }
                    }
                }
                .navigationTitle(Text("설정"))
            }
        }
        .padding()
    }
}

#Preview {
    ContentView()
}

```

</div>
</details>

<br><br>

[[Top]](#contents)

<br><br><br>


## ViewBuilder를 이용해 View분리하기

여기서 이제 겹치는 것들은 정리를 해주는 것이 좋다.  

일단 Profile Section 부터 시작해보자.   

분리하는 방법은 
body바깥에 `@ViewBuilder`라는 어노테이션을 이용해 View를 분리해 그려준다.  

프로필 섹션을 그렸던  View를 주석처리해서 아래로 옮겨준다.  

<br><br>

```swift
// 프로필 섹션
Section { 
    NavigationLink { 
        // destination
        Text("프로필 화면")
    } label: { 
    
        // 네비게이션 라벨 부분
//            HStack {
//                Image(systemName: "person.crop.circle.fill")
//                    .resizable()
//                    .aspectRatio(contentMode: .fit)
//                    .frame(width: 50,
//                           height: 50)
//                    .padding(.all, 4)
//                    .foregroundStyle(.gray)
//                
//                VStack(alignment: .leading, spacing: 3) {
//                    Text("방현석")
//                        .font(.system(size: 24))
//                        .fontWeight(.regular)
//                    Text("Apple ID, iCloud+ 미디어 및 구입 항목")
//                        .font(.system(size: 11))
//                }
//                .padding(.leading, 4)
//            }
//            .padding(.vertical, 10)
    }
}

    var body: some View { ... }
    
    @ViewBuilder
    private func profileCell() -> some View {
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
    }
```

<br><br>

 이제 생성한 profileCell()라는 View를 리턴하는 ViewBuilder 메서드를 다시 원위치에 넣어준다.  
 
 <br>
 
 ```swift
 // 프로필 섹션
 Section {
    NavigationLink { 
        // destination
        Text("프로필 화면")
    } label: { 
        // 네비게이션 라벨 부분
        profileCell()
    }
}
 ```

<br><br>

이러면 짧게 관리할 수 있다.  

<br><br>

[[Top]](#contents)

<br><br><br>

## 셀의 타입별로 분리해보기
전체적으로 살펴보면 이 UI는 크게 세가지로 나뉘어지는 것으로 보인다.  

1. 일반 셀
2. 토글이 있는 셀
3. 설정내용이 보이는 셀

<br><br>

<img width="400" alt="스크린샷 2023-11-24 오후 1 33 38" src="https://github.com/isGeekCode/TIL/assets/76529148/77fbfe88-5a7b-45ed-bc47-6c26b27d5bb8">

<br><br>

2번과 3번인 토글셀과 설정내용이 보이는 셀은 한번씩 쓰이고,  

일반 셀은 여러번 쓰는 것으로 보인다.  

그래서 2,3 번은 그대로 사용하고,

일반 셀은 파라미터로 이미지 이름, 배경색상, navigationLink의 라벨, destination에 넣을 View를 받아보자.  


<br><br>

2,3 번의 View는 프로필셀을 분리했던것처럼 메서드로 분리한다.  
```swift

    @ViewBuilder
    private func toggleCell() -> some View {
        HStack {
            Image(systemName: "airplane")
                .resizable()
                .aspectRatio(contentMode: .fit)
                .frame(width: 20,
                       height: 20)
                .padding(.all, 5)
                .background(.orange)
                .foregroundStyle(.white)
                .cornerRadius(6)
            
            
            // 에어플레인                            
            Toggle("에어플레인 모드", isOn: $isAirplainModeOn)
        }
    }
    
    @ViewBuilder
    private func detailCell() -> some View {
        
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
                Text("Wi-Fi")
            } label: { 
                HStack {
                    Text("Wi-Fi")
                    Spacer()
                    Text("SK_WKF4DJ7KD")
                        .foregroundStyle(.gray)
                }
            }
        }
        
        
    }
```

<br><br>

이제 여러번 사용할 일반셀을 보자.  

재사용할 내용은 아래와 같다.  
- 이미지 이름
- 배경색
- 네비게이션링크의 label View
- 네비게이션링크의 destination View

<br><br>

```swift
HStack {
    Image(systemName: "accessibility")  // 재사용필요
        .resizable()
        .aspectRatio(contentMode: .fit)
        .frame(width: 20,
               height: 20)
        .padding(.all, 5)
        .background(.blue)              // 재사용필요
        .foregroundStyle(.white)
        .cornerRadius(6)
    NavigationLink("손쉬운 사용") {        // 재사용필요
        Text("손쉬운 사용")                // 재사용필요
    }
}

```

<br><br>

그래서 이 재사용할 것들은 인자로 수정해주자. 
```swift
@ViewBuilder
private func plainCell(imageName: String,
                       backgroudColor: Color,
                       navigationLabelStr: String,
                       destination: View) -> some View {
    
    HStack {
        Image(systemName: imageName)
            .resizable()
            .aspectRatio(contentMode: .fit)
            .frame(width: 20,
                   height: 20)
            .padding(.all, 5)
            .background(backgroudColor)
            .foregroundStyle(.white)
            .cornerRadius(6)
        NavigationLink(navigationLabelStr) { 
            destination // Text("손쉬운 사용")    // ERROR!!!!!!
        }
    }
}
```

<br><br>

그런데 발생하는 문제가 있다.  View를 파라미터로 사용하려면 Generic타입으로만 사용가능하다.  

그래서 destination의 View타입을 제네릭 타입으로 명시해준다.  

```swift
private func plainCell<V: View>(imageName: String,
                       backgroudColor: Color,
                       navigationLabelStr: String,
                       destination: V) -> some View { }
```

<br><br>

[[Top]](#contents)

<br><br><br>

### escaping 적용하기

마지막으로 한가지 더! 

우리는 이걸 그냥 그대로 넣을 것이 아니라 escaping closure로 사용해야한다. 그래서

탈출클로저의  형태로 수정하자.  

<br><br>

```swift
// 변경 전
private func plainCell<V: View>(imageName: String,
                       backgroudColor: Color,
                       navigationLabelStr: String,
                       destination: V) -> some View { }

// 변경 후
    private func plainCell<V: View>(imageName: String,
                           backgroudColor: Color,
                           navigationLabelStr: String,
                           destination: @escaping () -> V ) -> some View {
        
        HStack {
            Image(systemName: imageName) 
                .resizable()
                .aspectRatio(contentMode: .fit)
                .frame(width: 20,
                       height: 20)
                .padding(.all, 5)
                .background(backgroudColor)
                .foregroundStyle(.white)
                .cornerRadius(6)
            NavigationLink(navigationLabelStr) { 
                destination() // Text("손쉬운 사용")
            }
        }
    }
```

이제 이걸 전체 적용해주자.   

<br><br><br>

### 전체코드


```swift
import SwiftUI

struct ContentView: View {
    
    @State private var isAirplainModeOn: Bool = false
    
    var body: some View {
        VStack {
            NavigationView {
                List {
                    S
                    Section {
                        NavigationLink { 
                            // destination
                            Text("프로필 화면")
                        } label: { 
                            // 네비게이션 라벨 부분
                            profileCell()
                        }
                    }
                    
                    Section {
                        plainCell(imageName: "hourglass",
                                  backgroudColor: .indigo,
                                  navigationLabelStr: "스크린타임") { 
                            Text("스크린타임")
                        }
                    }
                    
                    Section {
                        
                        toggleCell()
                        detailCell()
                        
                        plainCell(imageName: "antenna.radiowaves.left.and.right",
                                  backgroudColor: .green,
                                  navigationLabelStr: "셀룰러") { 
                            Text("셀룰러")
                        }
                        
                        plainCell(imageName: "personalhotspot",
                                  backgroudColor: .green,
                                  navigationLabelStr: "개인용 핫스팟") { 
                            Text("개인용 핫스팟")
                        }
                    }
                    
                    Section {
                        plainCell(imageName: "gear",
                                  backgroudColor: .gray,
                                  navigationLabelStr: "일반") { 
                            Text("일반")
                        }
                        
                        plainCell(imageName: "accessibility",
                                  backgroudColor: .blue,
                                  navigationLabelStr: "손쉬운 사용") { 
                            Text("손쉬운 사용")
                        }
                        
                        plainCell(imageName: "hand.raised.fill",
                                  backgroudColor: .blue,
                                  navigationLabelStr: "개인정보 보호 및 보안") { 
                            Text("개인정보 보호 및 보안")
                        }
                    }
                    
                    Section {
                        
                        plainCell(imageName: "key.fill",
                                  backgroudColor: .gray,
                                  navigationLabelStr: "암호") { 
                            Text("암호")

                        }

                        plainCell(imageName: "hammer.fill",
                                  backgroudColor: .gray,
                                  navigationLabelStr: "개발자") { 
                            Text("개발자")

                        }
                    }
                }
                .navigationTitle(Text("설정"))
            }
        }
        .padding()
    }
    
    @ViewBuilder
    private func profileCell() -> some View {
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
        
    }
    
    @ViewBuilder
    private func toggleCell() -> some View {
        HStack {
            Image(systemName: "airplane")
                .resizable()
                .aspectRatio(contentMode: .fit)
                .frame(width: 20,
                       height: 20)
                .padding(.all, 5)
                .background(.orange)
                .foregroundStyle(.white)
                .cornerRadius(6)
            
            
            // 에어플레인                            
            Toggle("에어플레인 모드", isOn: $isAirplainModeOn)
        }
    }
    
    @ViewBuilder
    private func detailCell() -> some View {
        
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
                Text("Wi-Fi")
            } label: { 
                HStack {
                    Text("Wi-Fi")
                    Spacer()
                    Text("SK_WKF4DJ7KD")
                        .foregroundStyle(.gray)
                }
            }
        }
        
        
    }
    
    @ViewBuilder
    private func plainCell<V: View>(imageName: String,
                           backgroudColor: Color,
                           navigationLabelStr: String,
                           destination: @escaping () -> V ) -> some View {
        HStack {
            Image(systemName: imageName) 
                .resizable()
                .aspectRatio(contentMode: .fit)
                .frame(width: 20,
                       height: 20)
                .padding(.all, 5)
                .background(backgroudColor)
                .foregroundStyle(.white)
                .cornerRadius(6)
            NavigationLink(navigationLabelStr) { 
                destination() // Text("손쉬운 사용")
            }
        }
    }
}

#Preview {
    ContentView()
}

```

<br><br>

이렇게 성격이 다른 UI를 메서드로 분리하는 작업을 해봤다.  

그런데 그럼에도 `1. 토글셀`, `2. 설정내용이 보이는 셀`, `3. 일반셀`에서 공통적으로 사용하는 부분이 많다.  

2번과 3번을 하나로 합쳐보자.  

```swift
    @ViewBuilder
    private func detailCell() -> some View {
        
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
                Text("Wi-Fi")
            } label: { 
                HStack {
                    Text("Wi-Fi")
                    Spacer()
                    Text("SK_WKF4DJ7KD")
                        .foregroundStyle(.gray)
                }
            }
        }
    }
    
    @ViewBuilder
    private func plainCell<V: View>(imageName: String,
                           backgroudColor: Color,
                           navigationLabelStr: String,
                           destination: @escaping () -> V ) -> some View {
        HStack {
            Image(systemName: imageName) 
                .resizable()
                .aspectRatio(contentMode: .fit)
                .frame(width: 20,
                       height: 20)
                .padding(.all, 5)
                .background(backgroudColor)
                .foregroundStyle(.white)
                .cornerRadius(6)
            NavigationLink(navigationLabelStr) { 
                destination() // Text("손쉬운 사용")
            }
        }
    }
```

<br><br>

다른 부분은 naviationLink부분이다. 이때 detailCell메서드는 선택한 내용을 텍스트로 필요로 한다. 그럼 plainCell에 추가해보자.  

 이런건 detail 정보를 파라미터로 옵셔널 처리해주면, 그걸 받느냐 마느냐에 따라 처리가 가능하다. 

<br><br>
 
```swift
    // 변경 전
    @ViewBuilder
    private func plainCell<V: View>(imageName: String,
                           backgroudColor: Color,
                           navigationLabelStr: String,
                           destination: @escaping () -> V ) -> some View {
        HStack {
            Image(systemName: imageName) 
                .resizable()
                .aspectRatio(contentMode: .fit)
                .frame(width: 20,
                       height: 20)
                .padding(.all, 5)
                .background(backgroudColor)
                .foregroundStyle(.white)
                .cornerRadius(6)
            NavigationLink(navigationLabelStr) { 
                destination() // Text("손쉬운 사용")
            }
        }
    }
    
    // 변경 후
    @ViewBuilder
    private func plainCell<V: View>(imageName: String,
                                    backgroudColor: Color,
                                    detailStr: String? = nil,
                                    navigationLabelStr: String,
                                    destination: @escaping () -> V ) -> some View {
        HStack {
            Image(systemName: imageName) 
                .resizable()
                .aspectRatio(contentMode: .fit)
                .frame(width: 20,
                       height: 20)
                .padding(.all, 5)
                .background(backgroudColor)
                .foregroundStyle(.white)
                .cornerRadius(6)
            
            if let detailStr = detailStr {
                
                NavigationLink { 
                    destination()
                } label: { 
                    HStack {
                        Text(navigationLabelStr)
                        Spacer()
                        Text(detailStr)
                            .foregroundStyle(.gray)
                    }
                }
                
            } else {
                NavigationLink(navigationLabelStr) { 
                    destination()
                }
            }
        }
    }

```

<br><br>

[[Top]](#contents)

<br><br><br>

### 객체분리하기

이제 전체 코드를 보면 총 세가지가 있다. 
- profileCell
- toggleCell
- plainCell

거의 마무리가 됐다.  

리팩토링을 할 때, 기억해야할 것은 이 코드를 가지고 나중에 

어떻게 유지보수를 할 것인지 고민해야한다는 것이다.  

그러면 현재로서 섹션에 새로운 셀을 추가할 수 있을까? -> 할 수 있다.   

그러면 디자인 수정이 필요하다면 용이할까?? 이건 좀 문제가 있다.  

아이콘 이미지가 각각 따로 있어서 일일히 메서드마다 적용해줘야하는 문제가 있기때문에 공통된 것들은 분리해서 적용해주자.  

Image에서 받아야할 것은 image이름, image 배경색이다. 

Image를 리턴할 ViewBuilder 메서드를 만들어보자.  

```swift
    @ViewBuilder
    private func iconImage(imageName: String, backgroudColor: Color) -> some View {
        Image(systemName: imageName)
            .resizable()
            .aspectRatio(contentMode: .fit)
            .frame(width: 20,
                   height: 20)
            .padding(.all, 5)
            .background(backgroudColor)
            .foregroundStyle(.white)
            .cornerRadius(6)
    }
```

자 이걸 아래 메서드에 적용할 거다.  



```swift
// 변경전
    @ViewBuilder
    private func toggleCell() -> some View {
        HStack {
            Image(systemName: "airplane")
                .resizable()
                .aspectRatio(contentMode: .fit)
                .frame(width: 20,
                       height: 20)
                .padding(.all, 5)
                .background(.orange)
                .foregroundStyle(.white)
                .cornerRadius(6)
            
            // 에어플레인                            
            Toggle("에어플레인 모드", isOn: $isAirplainModeOn)
        }
    }

    @ViewBuilder
    private func plainCell<V: View>(imageName: String,
                                    backgroudColor: Color,
                                    detailStr: String? = nil,
                                    navigationLabelStr: String,
                                    destination: @escaping () -> V ) -> some View {
        HStack {
            Image(systemName: imageName) 
                .resizable()
                .aspectRatio(contentMode: .fit)
                .frame(width: 20,
                       height: 20)
                .padding(.all, 5)
                .background(backgroudColor)
                .foregroundStyle(.white)
                .cornerRadius(6)
            
            if let detailStr = detailStr {
                
                NavigationLink { 
                    destination()
                } label: { 
                    HStack {
                        Text(navigationLabelStr)
                        Spacer()
                        Text(detailStr)
                            .foregroundStyle(.gray)
                    }
                }
                
            } else {
                NavigationLink(navigationLabelStr) { 
                    destination()
                }
            }
        }
    }
```

이제 추가된 image를 적용시킨 메서드로 적용해보자.  

```swift
    @ViewBuilder
    private func iconImage(imageName: String, backgroudColor: Color) -> some View {
        Image(systemName: imageName)
            .resizable()
            .aspectRatio(contentMode: .fit)
            .frame(width: 20,
                   height: 20)
            .padding(.all, 5)
            .background(backgroudColor)
            .foregroundStyle(.white)
            .cornerRadius(6)
    }
    
    
    @ViewBuilder
    private func toggleCell() -> some View {
        HStack {
            iconImage(imageName: "airplane",
                      backgroudColor: .orange)
            Toggle("에어플레인 모드", isOn: $isAirplainModeOn)
        }
    }

    @ViewBuilder
    private func plainCell<V: View>(imageName: String,
                                    backgroudColor: Color,
                                    detailStr: String? = nil,
                                    navigationLabelStr: String,
                                    destination: @escaping () -> V ) -> some View {
        HStack {
            
            iconImage(imageName: imageName,
                      backgroudColor: backgroudColor)
            
            if let detailStr = detailStr {
                
                NavigationLink { 
                    destination()
                } label: { 
                    HStack {
                        Text(navigationLabelStr)
                        Spacer()
                        Text(detailStr)
                            .foregroundStyle(.gray)
                    }
                }
                
            } else {
                NavigationLink(navigationLabelStr) { 
                    destination()
                }
            }
        }
    }
}

    
    
```


<br><br>

[[Top]](#contents)

<br><br><br>

## 최종코드

```swift
import SwiftUI

struct ContentView: View {
    
    @State private var isAirplainModeOn: Bool = false
    
    var body: some View {
        VStack {
            NavigationView {
                List {
                    
                    Section {
                        NavigationLink { 
                            // destination
                            Text("프로필 화면")
                        } label: { 
                            // 네비게이션 라벨 부분
                            profileCell()
                        }
                    }
                    
                    Section {
                        plainCell(imageName: "hourglass",
                                  backgroudColor: .indigo,
                                  navigationLabelStr: "스크린타임") { 
                            Text("스크린타임")
                        }
                    }
                    
                    Section {
                        
                        toggleCell()
                        plainCell(imageName: "wifi", 
                                  backgroudColor: .blue, 
                                  detailStr: "SK_WKF4DJ7KD", 
                                  navigationLabelStr: "Wi-Fi") { 
                            Text("Wi-Fi")
                        }
                        plainCell(imageName: "antenna.radiowaves.left.and.right",
                                  backgroudColor: .green,
                                  navigationLabelStr: "셀룰러") { 
                            Text("셀룰러")
                        }
                        
                        plainCell(imageName: "personalhotspot",
                                  backgroudColor: .green,
                                  navigationLabelStr: "개인용 핫스팟") { 
                            Text("개인용 핫스팟")
                        }
                    }
                    
                    Section {
                        plainCell(imageName: "gear",
                                  backgroudColor: .gray,
                                  navigationLabelStr: "일반") { 
                            Text("일반")
                        }
                        
                        plainCell(imageName: "accessibility",
                                  backgroudColor: .blue,
                                  navigationLabelStr: "손쉬운 사용") { 
                            Text("손쉬운 사용")
                        }
                        
                        plainCell(imageName: "hand.raised.fill",
                                  backgroudColor: .blue,
                                  navigationLabelStr: "개인정보 보호 및 보안") { 
                            Text("개인정보 보호 및 보안")
                        }
                    }
                    
                    Section {
                        
                        plainCell(imageName: "key.fill",
                                  backgroudColor: .gray,
                                  navigationLabelStr: "암호") { 
                            Text("암호")

                        }

                        plainCell(imageName: "hammer.fill",
                                  backgroudColor: .gray,
                                  navigationLabelStr: "개발자") { 
                            Text("개발자")

                        }
                    }
                }
                .navigationTitle(Text("설정"))
            }
        }
        .padding()
    }
    
    
    @ViewBuilder
    private func iconImage(imageName: String, backgroudColor: Color) -> some View {
        Image(systemName: imageName)
            .resizable()
            .aspectRatio(contentMode: .fit)
            .frame(width: 20,
                   height: 20)
            .padding(.all, 5)
            .background(backgroudColor)
            .foregroundStyle(.white)
            .cornerRadius(6)
    }

    
    @ViewBuilder
    private func profileCell() -> some View {
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
        
    }
    
    @ViewBuilder
    private func toggleCell() -> some View {
        HStack {
            iconImage(imageName: "airplane",
                      backgroudColor: .orange)
            Toggle("에어플레인 모드", isOn: $isAirplainModeOn)
        }
    }

    @ViewBuilder
    private func plainCell<V: View>(imageName: String,
                                    backgroudColor: Color,
                                    detailStr: String? = nil,
                                    navigationLabelStr: String,
                                    destination: @escaping () -> V ) -> some View {
        HStack {
            
            iconImage(imageName: imageName,
                      backgroudColor: backgroudColor)
            
            if let detailStr = detailStr {
                
                NavigationLink { 
                    destination()
                } label: { 
                    HStack {
                        Text(navigationLabelStr)
                        Spacer()
                        Text(detailStr)
                            .foregroundStyle(.gray)
                    }
                }
                
            } else {
                NavigationLink(navigationLabelStr) { 
                    destination()
                }
            }
        }
    }
}

#Preview {
    ContentView()
}
```

<br><br>

[[Top]](#contents)

<br><br><br>




## History
- 231123: 네비게이션링크 적용하기
- 231127: 리팩토링, 색인추가, 탑버튼 추가
