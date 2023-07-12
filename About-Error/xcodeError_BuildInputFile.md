# Xcode Error - Build input file cannot be found:

## 에러내용
```
Build input file cannot be found: '~filepath/Info.plist'.

Did you forget to declare this file as an output of a script phase or custom build rule which produces it?
```

## 원인

보통 이 문제는 Info.plist의 경로를 바꾸기 때문에 발생한다.


## 해결방법

- Target - Build Settings 로 진입

- Packaging - Info.plist File로 이동하기
여기서 Info.plist의 경로를 확인한다. 폴더 단위로 혹시 바뀐게 없는지 확인해보자


## History
- 230712 : 초안작성
