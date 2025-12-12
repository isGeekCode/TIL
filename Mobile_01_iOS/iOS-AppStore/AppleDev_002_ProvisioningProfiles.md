

# 인증서와 프로비저닝 프로파일 (Certificate & Provisioning Profile) 관리하기

## 왜 인증서와 프로비저닝 프로파일이 필요한가

앱 개발에서 인증서와 프로비저닝 프로파일은 필수 요소입니다.  
- **Development 프로비저닝 프로파일**: 실기기(아이폰, 아이패드 등)에 앱을 직접 설치하고 테스트할 때 필요합니다.  
- **Distribution 프로비저닝 프로파일**: 앱을 아카이빙하여 App Store에 배포하거나, 내부 배포용 설치 파일을 만들 때 사용됩니다.  

또한 인증서는 앱이 정상적으로 빌드되고 App Store Connect에 업로드될 수 있도록 보증하는 역할을 합니다. 특히 Xcode 15 이후부터는 인증서가 올바르게 설정되지 않으면 빌드 자체가 불가능해졌기 때문에, 인증서 관리의 중요성이 더욱 커졌습니다.

<br><br>

## 이건 어디서 사용할까?   


1. 보통 앱 타겟에서 Automatically manage signing에 체크가 되어있다.  

Xcode에서 Signing 옵션을 관리하는 화면은 아래와 같습니다. 이 화면에서 'Automatically manage signing' 옵션이 체크되어 있으면, Xcode가 자동으로 필요한 프로비저닝 프로파일과 인증서를 관리해줍니다.

<img width="600" alt="스크린샷 2023-03-28 오후 11 03 12" src="https://user-images.githubusercontent.com/76529148/228265752-538433b5-eb23-4541-a0e9-66dc69383785.png">

2. 배포방법에 따라 앱을 Re-sign 할때도 Automatically manage signing에 체크가 되어있다.   

배포 시에도 Xcode는 자동으로 서명 관련 리소스를 관리할 수 있는데, 아래 화면은 Re-sign 작업 시의 설정 예시입니다. 여기서도 'Automatically manage signing'이 체크되어 있으면 자동으로 처리됩니다.

<img width="600" alt="스크린샷 2023-03-29 오전 10 07 59" src="https://user-images.githubusercontent.com/76529148/228400672-effe1877-0780-4ec1-9f58-8255e7faed5a.png">

이 부분이 체크가 되어있으면 Xcode에서 자동으로 Profile, App ID, Certificate을 생성 및 업데이트 하게 되어있다.

개발자가 인식하고 있지 않더라도 위 인증작업을 Xcode뒤에서 알아서 하고 있다.

-> 2023.03.28


<br><br>

## Certificate

현실에서 계약서를 쓸때, 계약서에는 계약할 내용과 서명으로 있다.
그래서 이 계약서를 보면 누가 어떤 내용을 서로 약속했는지를 알 수가 있다.

### 코드서명
코드서명이란 말그대로 코드를 디지털 서명하는 것을 말한다. 이 서명을 통해 누가 코드를 작성했고, 서명이 이루어진 다음에는 코드가 변경되지않았다는 사실을 보증할 수 있다.

이 코드서명이라는 방식은 iOS뿐 아니라 여러 소프트웨어 보안에서 널리 사용하는 개념이다.
코드 서명에는 중요한 3가지 용어가 있다.

- 공개키
- 개인키
- 인증서


<br><br>

### 애플 발급 인증서
현실 세계에서 누군가가 당신의 개발적 지식을 증명하라고 한다면, 증거가 될 수 것들은 재직증명서나 졸업증명서 등 믿을 수 있는 기관의 보증이다. 
 
애플생태계에서 신뢰할 수 있는 기관은 당연하게도 Apple이다. 이 인증서를 통해 애플이 나를 합법적인 개발자로 인정한다는 것을 증명할 수 있게 되는 것이다. 

<br><br>

### 발급절차
애플에서 인증서를 발급받기 위해서는 키체인에서 인증기관에 인증서 요청을 클릭, 필요한 정보를 채운다.

아래는 Keychain Access에서 인증서 요청을 생성하는 화면입니다. 사용자 이메일 주소, 일반 이름 등을 입력하고 '디스크에 저장' 옵션을 선택하여 CSR 파일을 생성합니다.

- 사용자 이메일주소 : 사용하는 애플 이메일
- 일반 이름 : 사용자 이름 ( 한글도 가능 )
- `디스크에 저장`됨으로 선택


<img width="550" alt="스크린샷 2023-03-30 오후 10 08 01" src="https://user-images.githubusercontent.com/76529148/228845817-ca9773a5-47cf-4f8e-8399-ec201b4b7106.png">
<img width="550" alt="스크린샷 2023-03-30 오후 10 08 07" src="https://user-images.githubusercontent.com/76529148/228845826-ec710d1a-7121-4eb4-b20e-560f82be0198.png">

<br><br>

그러면 Certificate Signing Request (CSR)이라는 인증 서명 요청을 받을 수 있게 된다.

아래는 CSR 파일 생성 후 실제 CSR 파일 아이콘과 Keychain Access에서 CSR 파일을 확인하는 모습입니다. CSR은 인증서 발급에 필요한 정보를 담고 있습니다.

<img width="258" alt="스크린샷 2023-03-30 오후 10 08 11" src="https://user-images.githubusercontent.com/76529148/228845835-8f9a0621-60fb-41ef-a3d0-6b0bc2e60d18.png">
<img width="550" alt="스크린샷 2024-01-11 오전 10 06 12" src="https://github.com/isGeekCode/TIL/assets/76529148/4ae4f1f4-3c58-47fc-acd5-838d9d0598a3">

CSR은 인증서 발급을 위해 필요한 정보를 담고있는 데이터다. `이름, 국가, 이메일, 서명알고리즘 등등`을 담고 있고 `이 공개키가 포함된 인증서를 만들고 싶다` 라는 내용이 들어있다.

여기서 말하는 공개키는 CSR을 만들때 키체인에서 자동으로 생성하는 공개키를 말한다. 
공개키는 개인키와 하나의 쌍을 이룬다.

참고로 CSR을 만들때 생성되는 킸아에 대한 정보도 지정할 수 있다. 기본적으로 키 크기는 2048비트이고, 알고리즘은 RSA로 설정되어있다. 기본적으로 인증서는 Apple Developer Program에 가입된 사람들만 신청을 할 수 있다.

애플 개발자 사이트에서 확인할 수 있는 인증서 유형은 아래 링크를 참고
- [TIL : 인증서에 관하여](https://github.com/isGeekCode/TIL/blob/main/Integrity/Integrity_Certificate.md)  
  
  
여기서 가장 중요하다고 말한 두개의 인증서가 있다. 바로 Apple Development와 Apple Distribution 인증서이다. 

- Apple Development : 개발용
- Apple Distribution : 배포용

Run 을 하든 Archive 하든, 기본적으로 프로젝트를 빌드할 때 필요한 인증서는 Development 인증서다. 따라서 발급 받을 인증서의 종류를 Apple Development 로 선택하고, 신청서를 업로드하는 부분에 위에서 만든 CSR을 넣는다. 

아래는 Apple Developer 사이트에서 Apple Development 인증서를 신청하는 화면입니다. CSR 파일을 업로드하고 인증서 생성 과정을 진행합니다.

<img width="633" alt="스크린샷 2023-03-30 오후 10 16 35" src="https://user-images.githubusercontent.com/76529148/228848127-7185f31b-ea6d-4a0a-82af-6185bf18fa2a.png">

그리고 Continue를 누르면 생성된 인증서를 다운로드 받을 수 있다. (항상 잘 보관하자.)

아래는 인증서 다운로드 화면입니다. 생성된 인증서를 로컬에 저장합니다.

<img width="207" alt="스크린샷 2023-03-30 오후 10 17 58" src="https://user-images.githubusercontent.com/76529148/228848540-07be2e30-1418-49f0-be8d-4d25f4ef61fa.png">

이제 인증서를 더블 클릭해서 로컬에 설치하면,  
Keychain 쪽에 아까 인증서 요청을 할때 생성된 개인 키와 합쳐져 하나의 Signing Certificate (서명 인증서) 가 된다.

- Apple Development: isGeekCode(일련번호) -> 애플발급 인증서 (공개키 포함)
  - Apple Development : isGeekCode(isGeekCode) 개인키

아래는 Keychain Access에서 설치된 인증서와 개인키가 함께 보이는 모습입니다. 이렇게 하나의 Signing Certificate가 완성됩니다.

Apple Distribution 역시 마찬가지이다.  

 발급 받을 인증서의 종류를 Apple Distribution 로 선택하고, 신청서를 업로드하는 부분에 위에서 만든 CSR을 넣는다. 위와 동일하게 진행하면 완료!
 
 <img width="207" alt="스크린샷 2024-01-11 오전 10 36 46" src="https://github.com/isGeekCode/TIL/assets/76529148/c325f4ed-ea1d-4feb-afa4-467046c63cdd">

 
<br><br>
 
## 인증서 공유하기
개인적으로 사용하는경우, 다운받은 인증서와 개인키가 합쳐져 Signing Certificate(개인인증서)가 되면 끝이다.   

그러나 팀 단위 작업을 하는 경우, 키체인에서 완성된 Signing Certificate(개인인증서)를 공유해야한다.  

아래는 Keychain Access에서 인증서를 내보내는 과정입니다. 내보내기 위해서는 인증서를 선택 후 우클릭하여 내보내기를 선택합니다.

> 로그인 - 내 인증서 - 인증서 선택 - 마우스 우클릭 - 내보내기

팀정보 등의 개인정보를 가렸다.  

<img width="800" alt="스크린샷 2024-01-11 오전 10 34 30" src="https://github.com/isGeekCode/TIL/assets/76529148/77fdca4e-750a-4e1e-ab1c-0ffce1514396">

  
내보낼 인증서가 저장될 경로와 이름을 정하는 부분입니다. 기본적으로 p.12 형식으로 저장하며, 비밀번호를 설정하여 보안을 유지합니다.

<img width="400" alt="스크린샷 2024-01-11 오전 10 34 48" src="https://github.com/isGeekCode/TIL/assets/76529148/fbdeff3d-edce-4cf8-9570-9891b132bffa">

이렇게 내보낸 인증서를 아무나 사용할 수 없도록 암호를 설정한다.  
이 인증서를 받는 사람이 최초 한번 등록할 때만 사용한다.  

<img width="633" alt="스크린샷 2024-01-11 오전 10 35 22" src="https://github.com/isGeekCode/TIL/assets/76529148/0feccdc7-70fd-417c-b916-b02cfbcb71f4">

  
그러면 이제 생성된 파일을 전달하면 된다.   

<img width="207" alt="스크린샷 2024-01-11 오전 10 36 46" src="https://github.com/isGeekCode/TIL/assets/76529148/c325f4ed-ea1d-4feb-afa4-467046c63cdd">




## Certificates와 Provisioning Profiles의 관계 요약

인증서는 개발자 혹은 배포자의 신원을 증명하는 디지털 서명 도구로, 앱이 신뢰받을 수 있도록 하는 중요한 요소입니다. 프로비저닝 프로파일은 이러한 인증서와 앱 ID, 디바이스 정보를 연결하여 앱이 특정 기기에서 실행될 수 있도록 허용하는 역할을 합니다. 즉, 인증서가 '누가'인지 증명한다면, 프로비저닝 프로파일은 '어디서' 실행 가능한지를 관리하는 셈입니다. 이 두 가지가 함께 작동하여 iOS 앱의 보안과 배포를 원활하게 지원합니다.

### History
- 230330 : 애플인증서 발급절차 생성하기
- 240111 : 애플인증서 발급절차 생성하기(2) , 인증서 내보내기 추가

### 참고 링크
- 링크 1 : [Line Engineering - 심민영 : iOS 코드 서명에 대해서](https://engineering.linecorp.com/ko/blog/ios-code-signing)  
- 링크 2 : [Let'Swift 2022 - 강수진 : 인증서와 프로비저닝 프로파일](https://www.youtube.com/watch?v=Kbx_lBhhwDA)  
- 링크 3 : [Let'Swift 2022 - 강수진 : 인증서와 프로비저닝 프로파일 블로그 ](https://sujinnaljin.medium.com/ios-certificate-%EC%99%80-provisioning-profile-e1b9455e8a51)  
- 링크 4 : [TechTalk | iOS 앱 서명 개요](https://www.youtube.com/watch?v=0lJvQ-442OY&ab_channel=iLane)  
