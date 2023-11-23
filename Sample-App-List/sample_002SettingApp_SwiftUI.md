


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

## 여백으로 분리

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

## 네비게이션 타이틀 설정


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

## 네비게이션 링크하기

원하는 Row를 NavigationLink로 세팅하면 다음페이지로 세팅이 된다.  
전체 구조는 아래와 같다. 

> └ List
>     └ Section
>         └ NavigationLink
>             └ Text
       

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
                NavigationLink("개인용 핫스팟") { 
                    Text("개인용 핫스팟")
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


### 적용화면
<img width="300" alt="ezgif-4-98397e0be6" src="https://github.com/isGeekCode/TIL/assets/76529148/eae703b2-f21f-4980-b1fc-a9d5d11575eb">


## 이미지 추가

이제 List의 Row별로 
```swift

```


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
