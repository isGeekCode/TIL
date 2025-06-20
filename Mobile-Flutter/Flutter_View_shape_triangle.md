# Flutter - 삼각형 View 그리기

Flutter에서 삼각형을 그리는 방법은 여러 가지가 있다. 
그중 가장 일반적인 방법 중 하나는 CustomPaint 위젯과 CustomPainter 클래스를 사용하는 것이다.

## 결과화면
<img width="500" alt="스크린샷 2023-06-11 오전 12 16 50" src="https://github.com/isGeekCode/TIL/assets/76529148/e4582d93-45d0-4dbf-98a4-2e29a032e27a">
  
  
## 전체코드
```dart
import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Triangle Example'),
        ),
        body: Center(
          child: TriangleView(),
        ),
      ),
    );
  }
}

class TriangleView extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return CustomPaint(
      painter: TrianglePainter(),
      size: Size(100, 100), // 원하는 크기 지정
    );
  }
}


// 삼각형을 그리는 클래스
class TrianglePainter extends CustomPainter {
  @override
  void paint(Canvas canvas, Size size) {
    final paint = Paint()
      ..color = Colors.red
      ..style = PaintingStyle.fill;

    final path = Path();
    path.moveTo(0, size.height); // 시작점
    path.lineTo(size.width / 2, 0); // 상단 꼭지점
    path.lineTo(size.width, size.height); // 우측 하단 점
    path.close(); // 경로 닫기

    canvas.drawPath(path, paint);
  }

  @override
  bool shouldRepaint(TrianglePainter oldDelegate) => false;
}
```

## 코드 설명
- TrianglePainter 클래스
  - CustomPainter를 상속받은 클래스입. CustomPainter는 캔버스에 그림을 그리기 위한 커스텀 페인터를 만들기 위해 사용된다.
  - paint 메서드는 실제 그림을 그리는 로직이 들어가는 메서드이다.
  - paint 메서드의 파라미터
    - Canvas 객체 : canvas.drawPath()를 통해 실제로 그린다.
    - Paint 객체 : 삼각형의 좌표를 설정
  - shouldRepaint 메서드는 페인터를 다시 그려야 할 때를 결정하는데 사용된다. 여기서는 항상 false를 반환하여 다시 그리지 않도록 설정.
- TriangleView 위젯
  - CustomPaint 위젯을 사용하여 TrianglePainter를 그리는 위젯. 
  - size 속성을 사용하여 삼각형의 크기를 지정할 수 있다.


## History
- 230611 : 초안작성
