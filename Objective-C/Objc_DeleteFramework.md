# Objc - 라이브러리 : 직접 파일삽입된 라이브러리 제거작업

## 프레임워크 목록에서 제거
### Targets - General - Frameworks, Liabraries, and Embedded Content
이부분에 추가된 프레임워크를 `-`를 눌러서 제거한다. 

## 로컬 폴더내 파일 삭제
실제 경로에 직접 들어있는 파일을 삭제한다.
그러면 이제 파일을 못찾는다는 에러가 발생한다. 아래 항목으로 해결하자.

## Build Settings에 경로 추가
### Linking - other linker Flags

아래와 같이 정의되어있다면 
```
-force_load
$(SRCROOT)/KakaoOpenSDK.framework/KakaoOpenSDK
-ObjC
-lz
-lsqlite3.0
```

아래 부분을 삭제하자
`-force_load`
`$(SRCROOT)/KakaoOpenSDK.framework/KakaoOpenSDK`

## 관련 코드 완전히 제거

## History
- 230420 : 초안작성
