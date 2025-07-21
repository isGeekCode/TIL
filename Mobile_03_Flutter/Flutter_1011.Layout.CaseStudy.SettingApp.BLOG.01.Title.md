# 케이스 스터디 - iOS 설정앱



본 글은 iOS 설정앱 클론 코딩 시리즈 중 Part 1입니다.  
전체 레이아웃 구조와 타이틀, 검색창 UI를 먼저 구현합니다.

## ✍️ 들어가며

iOS 설정앱은 사용자에게 익숙한 디자인이죠.  
Flutter 입문자에게 실습 주제로 추천하는 이유는, 다양한 레이아웃 위젯과 스타일링 요소를 한 화면에 녹여낼 수 있기 때문입니다.   

이번 글에서는 `SafeArea`, `ClipRRect`, `Stack`, `Switch` 등을 활용하여 설정앱 UI를 구현해보며, 실전 위젯 사용법과 상태바 대응 방법까지 함께 익혀봅니다.


## 결과물 화면

![](https://i.imgur.com/YGedQEF.png)  ![](https://i.imgur.com/FK5gZGc.png)

실습 결과물을 먼저 살펴보고, 어떤 구조와 위젯이 쓰였는지 아래에서 단계별로 설명해요.


<br><br>

## 🧪 실습 목표
- Flutter로 iOS 설정앱 UI를 구성하는 방법을 실습합니다
- SafeArea, Column, Stack 등 실전 레이아웃 위젯을 사용해 봅니다
- 상태바 대응 및 리스트 스타일링을 실무 감각으로 다뤄봅니다


<br><br>

## 🔧 주요 사용 위젯
- `SafeArea`, `MediaQuery`: 상태바 영역을 대응해요
- `Column`, `Expanded`, `Spacer`: 수직 정렬과 비율 분배에 사용해요
- `ClipRRect`, `Container`: 모서리를 둥글게 만들고 박스 스타일링을 해요
- `Switch`, `ListTile`, `Icon`: 리스트 안의 설정 항목을 구성해요
- `Stack`, `Positioned`: 중첩 레이아웃을 만들 때 써요


<br><br>

## 🧱 UI 구조 및 구현 전략

각 영역은 실제 iOS 앱을 참고해서 최대한 비슷한 UI로 만들어봤어요.  
특히, `CircleAvatar`, `Spacer`, `Stack` 조합은 자주 쓰는 패턴이니 천천히 살펴보면 좋아요.

### 🔹 상단 프로필 영역
- `CircleAvatar`로 사용자 아이콘을 표현해요
- `Row`와 `Column` 조합으로 이름과 설명을 배치해요
- `Spacer()`로 오른쪽 아이콘과 간격을 맞춰요

### 🔹 설정 리스트
- `ClipRRect`로 외곽을 둥글게 만들어요
- 각 항목은 `Row`나 `ListTile` 비슷한 구조예요
- `Switch`, `Text`, `Icon`을 조합해서 기본 설정 항목을 만들어요

<br><br>
---

## ⚠️ 구현 시 주의점
- 상태바 영역은 `MediaQuery.of(context).padding.top`으로 안전하게 확보합니다
- `Expanded`를 사용할 때는 높이 제한과 overflow 오류를 주의합니다
- iOS 스타일에 가까운 디자인을 위해 `Divider`의 `indent`, `thickness` 값을 섬세하게 조정합니다

## 🚀 확장 아이디어
- `ListView`를 적용해 실제 설정 앱처럼 스크롤 가능하도록 확장할 수 있습니다
- 각 설정 항목에 기능 바인딩을 적용해 실사용 인터랙션을 구현해보세요
- `ThemeData`, 다크모드 대응 등으로 테마 시스템을 실습해보는 것도 좋습니다


## 🗺️ 이 문서는 로드맵의 다음 항목과 연계돼요
- ✅ 2.3 레이아웃 실전: 설정앱 클론 코딩
- ✅ 2.35 SafeArea와 상태바 처리
- 🔜 9.4 설정 페이지 구현 (SwitchListTile, ListView 도입할 거예요)

<br><br>

전체 구조를 이해했다면, 아래에 전체 코드를 첨부할게요.  
실습할 때 참고하거나 복사해서 직접 실행해봐요.

## Part 1 - 전체 코드 (타이틀 + 검색창 구현)

```dart
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
            MediaQuery.of(context).padding.top,
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
                )
              ],
            ),
          ),
        ),
      ),
    );
  }
}
```

<br><br>

## 🧩 마무리

이번 Part 1에서는 설정앱 스타일 UI 중 타이틀과 검색창 레이아웃까지 구현해보았습니다.

👉 다음 글인 Part 2에서는 상단 프로필, 가족, 백업 섹션 UI를 구현하며 레이아웃 구성력을 더 확장해봅니다.
