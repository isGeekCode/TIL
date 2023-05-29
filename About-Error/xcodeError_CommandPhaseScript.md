# Xcode - Command PhaseScriptExecution failed with a nonzero exit code

## 발견

단순히 `pod install`을 하고 프로젝트를 실행하려는데 빌드에러발생

## 원인

전임자에게 확인해보니 Firebase Crashlytics에 대한 runScript가 있는데 이 부분이 실행되는 것에 대한 에러라고 한다.

### 진단방법
프로젝트 설정 - Build Phase - RunScript
위 경로로 들어갔을 때, 구글에서 제공한 스크립트가 있다면 이에 해당한다. 
```
# Type a script or drag a script file from your workspace to insert its path.
"${PODS_ROOT}/FirebaseCrashlytics/run"
```

## 해결방법

- 터미널로 해당 프로젝트의 POD이 설치된 경로로 진입 
 FirebaseCrashlytics가 설치된 경로로 진입
 
- 예시: `~/프로젝트폴더의 상위폴더/프로젝트 폴더/프로젝트명/Pods/FirebaseCrashlytics` 

- 아래 코드 입력
```
chmod 777 run
chmod 777 upload-symbols
```

- 빌드

### 세부설명
chmod은 리눅스와 유닉스 기반 시스템에서 파일이나 디렉터리의 권한을 변경하는 명령어. 
권한은 파일이나 디렉터리에 대한 읽기(read), 쓰기(write), 실행(execute) 권한을 나타낸다. chmod 777은 권한을 설정하는 옵션이다.

- chmod 777 run
    - `run` 파일에 대한 권한을 변경한다.
- chmod 777 upload-symbols
    - `upload-symbols` 파일에 대한 권한을 변경한다.

여기서 777은 각 권한을 나타내는 숫자이다.

숫자가 나타내는 권한의 의미 
- 첫 번째 숫자는 소유자(owner)의 권한
- 두 번째 숫자는 그룹(group)의 권한
- 세 번째 숫자는 기타 사용자(other)의 권한

특정 사용자 클래스의 권한 자릿수는 해당 클래스에 대한 권한 값의 합계이다.
권한 번호의 각 자릿수는 4, 2, 1 및 0의 합계다.

쓰기, 읽기 및 실행 권한의 숫자 값은 다음과 같다.
```
r(읽기) = 4
w(쓰기) = 2
x(숫자) = 1
no permissions = 0

0(0+0+0) – 권한이 없다.
1(0+0+1) – 권한만 실행한다.
2(0+2+0) – 쓰기 권한만 있다.
3(0+2+1) – 쓰기 및 실행 권한을 가진다.
4(4+0+0) – 읽기 권한만 있다.
5(4+0+1) – 읽기 및 실행 권한을 가진다.
6(4+2+0) – 읽기 및 쓰기 권한을 가진다.
7(4+2+1) – 읽기, 쓰기 및 실행 권한을 가진다.
```
 
 
따라서 chmod 777 명령은 해당 파일 또는 디렉터리에 대해 모든 사용자가 읽기, 쓰기, 실행 권한을 가지도록 설정하는 것이다.

주의: chmod 777은 파일 또는 디렉터리에 대한 권한을 가장 개방적으로 설정하므로 보안에 취약할 수 있다. 적절한 권한 설정을 위해서는 보안 요구 사항을 고려하여 필요한 권한만 부여하는 것이 좋다.


### History
- 발견 / 해결 : 230530

### Reference
- https://jjeongil.tistory.com/1907
- https://88240.tistory.com/13
