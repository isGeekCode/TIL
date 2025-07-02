# Flutter - 기본 4가지 위젯

## 위젯이란

홈화면에 이것저것 넣을 수 있는데 이런 것을 위젯이라고 한다.

만약 글자를 넣고 싶다면 글자, 박스를 넣고 싶으면 박스 위젯을 넣는다

## 1. Text 위젯

```Dart
Text('안녕')
```


## 2. Icon 위젯
 
```Dart
Icon(Icons.star)
Icon(Icons.shop)

```
## 3. Image 위젯
 
```Dart
Image.asset('경로')
Image.asset('fileName.png')
```
### assets에 추가
파일을 assets폴더에 넣어준다

### pubspec.yaml 파일에 정의
- 폴더명/ 안에 있는 파일을 사용하겠다고 정의
```
flutter:
  assets:
    - assets/
```

## 4. Box 위젯
아래 두가지 모두 가능하다.
```
Container()
SizedBox()
```
위처럼 그냥 사용하면 아무것도 변하지않아서 아래 처럼 파라미터를 넣어준다.
```
Container( width: 50, height: 50, color: Colors.blue)
```
이 50은 px가 아니라 lp이다. 
어디서 부터 50인지를 정의해주지 않아서 부모에서 해당 내용을 정의한다.

```
Center(
  child: Container( width: 50, height: 50, color: Colors.blue),
)
```
