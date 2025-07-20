# iOS - Setting 앱 클론


## 결과물 화면

![](https://i.imgur.com/YGedQEF.png)  ![](https://i.imgur.com/FK5gZGc.png)


<br><br>

## 🧪 실습 목표
- iOS 설정앱 UI를 Flutter로 구현하며 레이아웃 구성 방식 학습
- SafeArea, Column, ClipRRect, Stack, Expanded 등 실전 레이아웃 위젯 사용법 익히기
- 상태바/SafeArea 대응 방법 이해


<br><br>

## 🔧 주요 사용 위젯
- `SafeArea`, `MediaQuery`: 상태바 영역 대응
- `Column`, `Expanded`, `Spacer`: 수직 정렬 및 비율 분배
- `ClipRRect`, `Container`: 모서리 둥글게 처리 및 박스 스타일링
- `Switch`, `ListTile`, `Icon`: 리스트 내 설정 항목 구성
- `Stack`, `Positioned`: 중첩 레이아웃 구현


<br><br>

## 🧱 UI 구조 및 구현 전략

### 🔹 상단 프로필 영역
- `CircleAvatar`로 사용자 아이콘 표현
- `Row` + `Column` 조합으로 이름 및 설명 배치
- `Spacer()`로 우측 아이콘과 간격 정리

### 🔹 설정 리스트
- `ClipRRect`로 외곽 둥글게
- 각 항목은 `Row` 또는 `ListTile` 유사 구조
- `Switch`, `Text`, `Icon` 조합으로 기본 설정 항목 구성

<br><br>
---

## ⚠️ 구현 시 주의점
- 상태바 높이 대응: `MediaQuery.of(context).padding.top`으로 처리
- 리스트 항목 고정 높이로 `Expanded` 사용 시, height와 overflow 유의
- `Divider` 높이와 `indent` 값 조정으로 iOS 느낌 살리기

## 🚀 확장 아이디어
- 각 항목을 `ListView`로 감싸 스크롤 처리
- 각 설정 항목에 실제 기능 바인딩 추가
- 다크모드 대응 및 `ThemeData` 적용 실습으로 확장 가능


## 🗺️ 이 문서는 로드맵의 다음 항목과 연계됩니다
- ✅ 2.3 레이아웃 실전: 설정앱 클론 코딩
- ✅ 2.35 SafeArea와 상태바 처리
- 🔜 9.4 설정 페이지 구현 (SwitchListTile, ListView 도입 예정)

<br><br>

## 전체코드

```dart
import 'dart:math';  
  
import 'package:flutter/material.dart';  
import 'package:flutter/services.dart';  
  
void main() {  
  runApp(MyApp());  
}  
  
class MyApp extends StatelessWidget {  
  const MyApp({super.key});  
  
  @override  
  Widget build(BuildContext context) {  
    return MaterialApp(home: MainScreen());  
  }  
}  
  
class MainScreen extends StatelessWidget {  
  const MainScreen({super.key});  
  
  @override  
  Widget build(BuildContext context) {  
    return AnnotatedRegion<SystemUiOverlayStyle>(  
      value: SystemUiOverlayStyle.dark,  
      child: Scaffold(  
        body: Container(  
          color: Colors.grey[300],  
          padding: EdgeInsets.fromLTRB(  
            10,  
            MediaQuery  
                .of(context)  
                .padding  
                .top,  
            10,  
            0,  
          ),  
  
          child: Padding(  
            padding: const EdgeInsets.all(10.0),  
            child: Column(  
              spacing: 20,  
              mainAxisAlignment: MainAxisAlignment.start,  
              crossAxisAlignment: CrossAxisAlignment.start,  
              children: [  
                Text(  
                  '설정',  
                  style: TextStyle(  
                    fontSize: 30,  
                    fontWeight: FontWeight.bold,  
                    height: 1.0,  
                  ),  
                ),  
  
                ClipRRect(  
                  borderRadius: BorderRadius.circular(10),  
                  child: Container(  
                    color: Colors.grey[400],  
                    width: double.infinity,  
                    height: 40,  
                    padding: const EdgeInsets.fromLTRB(10, 0, 10, 0),  
                    child: Row(  
                      mainAxisAlignment: MainAxisAlignment.start,  
                      children: [  
                        Icon(Icons.search, size: 30),  
                        SizedBox(width: 10),  
                        Text('검색', style: TextStyle(fontSize: 20, height: 1.0)),  
                        Spacer(),  
                        Icon(Icons.mic, size: 30),  
                      ],  
                    ),  
                  ),  
                ),  
  
                ClipRRect(  
                  borderRadius: BorderRadius.circular(10),  
                  child: Container(  
                    color: Colors.white,  
                    width: double.infinity,  
                    padding: const EdgeInsets.fromLTRB(10, 0, 10, 0),  
                    height: 180,  
                    child: Column(  
                      mainAxisAlignment: MainAxisAlignment.start,  
                      children: [  
                        Expanded(  
                          flex: 3,  
                          child: Row(  
                            mainAxisAlignment: MainAxisAlignment.start,  
                            children: [  
                              CircleAvatar(  
                                radius: 30,  
                                backgroundColor: Colors.blue,  
                                child: Icon(  
                                  Icons.person,  
                                  color: Colors.white,  
                                  size: 35,  
                                ),  
                              ),  
  
                              SizedBox(width: 20),  
                              Column(  
                                mainAxisAlignment: MainAxisAlignment.center,  
                                crossAxisAlignment: CrossAxisAlignment.start,  
                                children: [  
                                  Text(  
                                    '홍길동',  
                                    style: TextStyle(  
                                      fontSize: 20,  
                                      fontWeight: FontWeight.bold,  
                                    ),  
                                  ),  
                                  Text(  
                                    'Apple 계정, iCloud+ 등',  
                                    style: TextStyle(fontSize: 15),  
                                  ),  
                                ],  
                              ),  
                              Spacer(),  
                              Icon(Icons.chevron_right),  
                            ],  
                          ),  
                        ),  
                        Divider(  
                          thickness: 0.2,  
                          indent: 80,  
                          height: 1,  
                          color: Colors.grey,  
                        ),  
  
                        Expanded(  
                          flex: 2,  
                          child: Row(  
                            children: [  
                              Stack(  
                                clipBehavior: Clip.none,  
                                children: [  
                                  CircleAvatar(  
                                    radius: 18,  
                                    backgroundColor: Colors.green,  
                                    child: Icon(  
                                      Icons.person,  
                                      color: Colors.white,  
                                      size: 18,  
                                    ),  
                                  ),  
                                  Positioned(  
                                    left: 30,  
                                    child: CircleAvatar(  
                                      radius: 18,  
                                      backgroundColor: Colors.orange,  
                                      child: Icon(  
                                        Icons.person,  
                                        color: Colors.white,  
                                        size: 18,  
                                      ),  
                                    ),  
                                  ),  
                                ],  
                              ),  
                              SizedBox(width: 45),  
                              Text('가족', style: TextStyle(fontSize: 15)),  
                              Spacer(),  
                              Icon(Icons.chevron_right),  
                            ],  
                          ),  
                        ),  
                        Divider(  
                          thickness: 0.2,  
                          indent: 80,  
                          height: 1,  
                          color: Colors.grey[900],  
                        ),  
                        Expanded(  
                          flex: 2,  
  
                          child: Row(  
                            children: [  
                              Text('iPhone 백업 안 됨'),  
                              Spacer(),  
                              CircleAvatar(  
                                radius: 12,  
                                backgroundColor: Colors.red,  
                                child: Text(  
                                  '1',  
                                  style: TextStyle(  
                                    fontSize: 12,  
                                    color: Colors.white,  
                                  ),  
                                ),  
                              ),  
                              Icon(Icons.chevron_right),  
                            ],  
                          ),  
                        ),  
                      ],  
                    ),  
                  ),  
                ),  
  
                ClipRRect(  
                  borderRadius: BorderRadius.circular(10),  
                  child: Container(  
                    color: Colors.white,  
                    width: double.infinity,  
                    padding: const EdgeInsets.fromLTRB(10, 0, 10, 0),  
  
                    height: 250,  
  
                    child: Column(  
                      children: [  
                        Expanded(  
                          child: Row(  
                            children: [  
                              ClipRRect(  
                                borderRadius: BorderRadius.circular(10),  
                                child: Container(  
                                  color: Colors.orange,  
                                  padding: const EdgeInsets.all(10),  
                                  child: Transform.rotate(  
                                    angle: pi / 2,  
                                    child: Icon(  
                                      Icons.flight,  
                                      color: Colors.white,  
                                    ),  
                                  ),  
                                ),  
                              ),  
                              SizedBox(width: 10),  
  
                              Text('에어플레인 모드'),  
                              Spacer(),  
                              Switch(  
                                value: false,  
                                activeTrackColor: Colors.green,  
                                onChanged: (value) {  
                                  print('test');  
                                },  
                              ),  
                            ],  
                          ),  
                        ),  
                        Divider(  
                          thickness: 0.2,  
                          indent: 80,  
                          height: 1,  
                          color: Colors.grey,  
                        ),  
                        Expanded(  
                          child: Row(  
                            children: [  
                              ClipRRect(  
                                borderRadius: BorderRadius.circular(10),  
                                child: Container(  
                                  color: Colors.blueAccent,  
                                  padding: const EdgeInsets.all(10),  
                                  child: Icon(  
                                    Icons.wifi,  
                                    color: Colors.white,  
                                  ),  
                                ),  
                              ),  
                              SizedBox(width: 10),  
  
                              Text('Wi-Fi'),  
                              Spacer(),  
                              Text('KT-wifi 35D34-5G'),  
                              Icon(Icons.chevron_right),  
  
                            ],  
                          ),  
                        ),  
  
                        Divider(  
                          thickness: 0.2,  
                          indent: 80,  
                          height: 1,  
                          color: Colors.grey,  
                        ),  
                        Expanded(  
                          child: Row(  
                            children: [  
                              ClipRRect(  
                                borderRadius: BorderRadius.circular(10),  
                                child: Container(  
                                  color: Colors.blueAccent,  
                                  padding: const EdgeInsets.all(10),  
                                  child: Icon(  
                                    Icons.bluetooth,  
                                    color: Colors.white,  
                                  ),  
                                ),  
                              ),  
                              SizedBox(width: 10),  
  
                              Text('Bluetooth'),  
                              Spacer(),  
                              Text('켬'),  
                              Icon(Icons.chevron_right),  
  
                            ],  
                          ),  
                        ),  
  
                        Divider(  
                          thickness: 0.2,  
                          indent: 80,  
                          height: 1,  
                          color: Colors.grey,  
                        ),  
                        Expanded(  
                          child: Row(  
                            children: [  
                              ClipRRect(  
                                borderRadius: BorderRadius.circular(10),  
                                child: Container(  
                                  color: Colors.green,  
                                  padding: const EdgeInsets.all(10),  
                                  child: Icon(  
                                    Icons.cell_tower,  
                                    color: Colors.white,  
                                  ),  
                                ),  
                              ),  
                              SizedBox(width: 10),  
  
                              Text('셀룰러'),  
                              Spacer(),  
                              Icon(Icons.chevron_right),  
  
                            ],  
                          ),  
                        ),  
  
                      ],  
                    ),  
                  ),  
                ),  
              ],  
            ),  
          ),  
        ),  
      ),  
    );  
  }  
}
```


