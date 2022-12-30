# .ipa 파일 만들기

IPA는 앱을 엔터프라이즈 계정으로 생성하여
회사 내부적으로 설치하는 방식에 사용한다.
마치 안드로이드에서 APK파일을 사용하는 것과 같은 방식이라고 생각하면된다. 

이를 위해서는 Provisioning Profile이 있어야한다는 것을 기억하자.

## IPA파일 만드는 순서

Step1: Provisioning Profile 까지 세팅완료하기

Step2: Archive하기
- edit scheme에서 release인지 debug인지 꼭 확인하자

Step3: Enterprise로 배포

stepr4: ipa파일 export하기
- 폴더가 생성된다. 내부에 파일명.ipa 를 사용하면된다.
