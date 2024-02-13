# Xcode Error - The CFBundleShortVersionString of an app extension (‘1.0’) must match that of its containing parent app


## 에러내용

아래 몇가지 경우지만 동일한 이유로 발생한다.  
```
// 사례 1
warning: The CFBundleVersion of an app extension (‘1’) must match that of its containing parent app (‘2’).


// 사례 2
warning: The CFBundleShortVersionString of an app extension (‘1.0’) must match that of its containing parent app (‘1.0.0’).
```



## 원인

Info.plist의 CURRENT_PROJECT_VERSION 과 MARKETING_VERSION 이 일치하지 않아 발생한다.  

해당 앱의 App Extension을 추가하게 되면, 별도의 타겟넘버를 가질 수 있게된다.    
-> 애플로그인, 리치푸시 등등 의 Extension

## 해결방법

이때 extension 의 MARKETING_VERSION가 parent앱의 MARKETING_VERSION와 일치하면 해당 에러는 사라진다.    

다만, 빌드버전이나 앱버전을 일일히 맞춰줘야한다.  


Xcode15에서 발생한 것인지는 모르겠지만 근본적인 해결방법을 확인하게되면 추가예정


## History
- 240213 : 초안작성
