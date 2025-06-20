# Flutter Error - Entrypoint doesn't contain...

이 에러는 main 함수가 없어서 나오는 에러이다.

원래는 main함수가 아래처럼 나와있어야한다.
```dart
void main() {
  runApp(const MyApp());
}
```

상단의 시뮬레이터 부분 우측에 main.dart 부분에 빨간색 표시가 나오는 경우에는 

Edit Configurations를 눌러서 
main함수가 위치한 파일을 세팅해 주면 된다. 

아래에 표시된 부분을 그 파일로 세팅해준다.

<img width="600" alt="스크린샷 2023-05-21 오후 2 13 05" src="https://github.com/isGeekCode/TIL/assets/76529148/d1515b83-b42d-431b-9294-32d88cae1537">
