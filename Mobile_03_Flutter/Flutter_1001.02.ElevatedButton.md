# Basics - ElevatedButton

<img src="https://i.imgur.com/93H27JZ.png" width="500" />

<br>

## 🗂️ Widget Catalog Index

```
├ Basics  
│   └ ✅ ElevatedButton ← 현재 문서  
├ Layout  
├ Text  
├ Input  
...
└ Accessibility  
```

<br>

## 개념

`ElevatedButton`은 Material Design에서 제공하는 기본 버튼 위젯이다.  
평면적인 레이아웃에 입체감을 주는 방식으로, **눌렀을 때 살짝 떠오르는 효과**가 있다.  
보통 **강조 버튼**이나 시각적으로 강조하고 싶은 액션에 사용된다.

이 버튼은 on/off 개념의 toggle 버튼과는 다르게, **현재 눌렸는지 여부만 판단하는 단발성 액션 버튼**이다.  
버튼을 누르면 약속된 동작을 실행한다.

<br>

## 동작 방식

- 자식으로 보통 `Text`, `Icon`, `Row` 등을 받아 레이블을 구성한다.
- 눌렸을 때 `elevation`(입체감)이 증가하며, 배경색과 전경색은 스타일로 지정 가능하다.
- `onPressed`에 콜백이 지정되지 않으면 버튼은 **비활성(disabled)** 상태가 된다.
- 스타일 지정은 `styleFrom` 또는 `ButtonStyle` 클래스를 통해 할 수 있다.
- 버튼이 눌리면 약간 떠오르는 듯한 입체 효과가 적용되며, 이는 elevation 속성을 통해 제어할 수 있다. 기본값은 2이며, 눌리면 8까지 증가한다.

<br>

## 생성자

```dart
ElevatedButton({
  Key? key,
  required VoidCallback? onPressed,
  Widget? child,
  ButtonStyle? style,
  ...
})
```

아이콘과 텍스트를 함께 넣으려면 `ElevatedButton.icon` 생성자를 사용한다.    
자세한 내용과 스타일 커스터마이징 예시는 [아이콘 버튼](#아이콘-버튼) 섹션 참고.


<br><br>


## onPressed란?

`onPressed`는 버튼이 눌렸을 때 실행할 콜백을 정의하는 속성이다.  
`ElevatedButton`에서 이 속성은 필수이며, null이면 버튼은 비활성화된다.

onPressed는 버튼이 눌렸을 때 실행되는 콜백 함수이다. 이 속성은 null이면 버튼은 비활성화되고, 사용자가 눌러도 반응하지 않는다.

```dart
ElevatedButton(
  onPressed: () {
    print("버튼이 눌렸습니다");
  },
  child: Text('Press Me'),
)
```

- `null`이면 버튼은 비활성 상태가 되며, 클릭할 수 없다.

  
```dart
ElevatedButton(
  onPressed: null,
  child: Text('Disabled'),
)

// 별도 함수로 정의하는 경우
void handleClick() {
  print("clicked");
}

ElevatedButton(
  onPressed: handleClick,
  child: Text('Press'),
)
```

> ⚠️ `onPressed`는 생략할 수 없으며, null을 명시적으로 지정해야 비활성 상태가 된다.

<br>
<br>

## Style

ElevatedButton은 Style을 `styleFrom`과 `ButtonStyle` 방식으로 구현할 수 있다.    

styleFrom은 ButtonStyle을 내부적으로 생성하는 팩토리 함수이다.  
때문에 간단하고 일괄적으로 생성할 때, 사용한다.  

ButtonStyle은 각 비주얼적인 요소마다 WidgetStateProperty를 이용해 클릭하는 경우, 마우스가 올라가는 경우 등 버튼의 상태를 체크하며 부여한다.  
 
그렇기 때문에 조건처리가 다양해질수록 길어진다.  

모든 상태 동일하게 적용하려면 ButtonStyle 에서 상태를 **.all**로 생성하거나 styleFrom을 사용하면 된다.   


아래는 대표적인 스타일 지정 예시다.

 
```dart
// styleFrom로 일괄 적용하기
ElevatedButton(
  onPressed: () {},
  style: ElevatedButton.styleFrom(
    backgroundColor: Colors.green,
    foregroundColor: Colors.white,
    elevation: 4,
    padding: EdgeInsets.symmetric(horizontal: 24, vertical: 12),
    shape: RoundedRectangleBorder(
      borderRadius: BorderRadius.circular(12),
    ),
  ),
  child: Text('StyleFrom'),
),

// ButtonStyle로 상태별 적용하기 - 일괄
ElevatedButton(
  onPressed: () {},
  style: ButtonStyle(
    // 일괄 적용
    backgroundColor: WidgetStateProperty.all(Colors.red),
    foregroundColor: WidgetStateProperty.all(Colors.white),
    shape: WidgetStateProperty.all(
      RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(16),
      ),
    ),
    
    // 상태별 적용 - 예1
    elevation:
      WidgetStateProperty.resolveWith((states) {
        return states.contains(WidgetState.pressed) ? 8 : 4;
    }),
    
    // 상태별 적용 - 예2
    overlayColor: WidgetStateProperty.resolveWith<Color?>(
                            (Set<WidgetState> states) {
        // 클릭 액션
        if (states.contains(WidgetState.pressed)) {
          return Colors.blue.withValues(alpha : 0.2);
        }
      
        // 호버 액션, 웹에서만 동작
        if (states.contains(WidgetState.hovered)) {
          return Colors.red.withValues(alpha: 0.1);
        }
      
        return null; // 기본 없음
      },
    ),
    
  ),
  child: Text('ButtonStyle'),
),



```

<br><br>

## 아이콘 버튼

아이콘이 포함된 버튼은 `ElevatedButton.icon` 생성자를 사용한다.  
텍스트와 아이콘을 나란히 배치할 수 있으며, 일반 버튼과 동일하게 스타일 지정이 가능하다.

```dart
ElevatedButton.icon(
  onPressed: () {},
  icon: Icon(Icons.thumb_up),
  label: Text('Like'),
)
```

아이콘 버튼도 `styleFrom` 또는 `ButtonStyle`로 스타일 커스터마이징이 가능하다.

```dart
// styleFrom 예시
ElevatedButton.icon(
  onPressed: () {},
  icon: Icon(Icons.thumb_up),
  label: Text('Like'),
  style: ElevatedButton.styleFrom(
    backgroundColor: Colors.indigo,
    foregroundColor: Colors.white,
    padding: EdgeInsets.symmetric(horizontal: 20, vertical: 12),
    elevation: 6,
    shape: RoundedRectangleBorder(
      borderRadius: BorderRadius.circular(12),
    ),
  ),
)
```

아이콘 버튼의 다양한 스타일 예시는 아래 [예제 2](#예제-2-아이콘-버튼)에서 확인할 수 있다.  


<br><br>


## 🧪 Sample Code

---

### 예제 1: 기본 버튼


```dart
// 1-1. 가장 기본적인 ElevatedButton
ElevatedButton(
  onPressed: () {
    print("Button pressed");
  },
  child: Text('Click Me'),
)

// 1-2. 여러 동작을 한 번에 처리
ElevatedButton(
  onPressed: () => {
    print("Button pressed"),
    print("Hello Flutter")
  },
  child: Text('Click Me'),
)

// 1-3. 동작을 별도 함수로 분리
void doSomething() {
  print('button Pressed');
}

ElevatedButton(
  onPressed: doSomething,
  child: Text('Click Me'),
)
// 버튼 동작과 비활성화 처리

ElevatedButton(
  onPressed: null,
  child: Text('Disabled'),
)
```
onPressed에는 클릭시 동작을 선언하는 곳이다.  
여기에 null이 들어가게 되면 비활성화 처리된다.  

혹은 상태변수를 두고 클릭시 비활성화 처리할 수도 있다.  

```dart
bool isEnabled = true;

ElevatedButton(
  onPressed: isEnabled ? () {
    setState(() {
      isEnabled = false;
    });
  } : null,
  child: Text('Disabled'),
)
```

아래 전체코드에서는 비동기로 1초 기다린후 다시 원래대로 돌아가는 소스가 추가되어있다. 

## 예제 2: 아이콘 버튼
### 2-1. 기본 아이콘 버튼
```dart
ElevatedButton.icon(
  onPressed: () {},
  icon: Icon(Icons.thumb_up),
  label: Text('Like'),
)
```

### 2-2. 스타일 지정 (styleFrom)
```dart
ElevatedButton.icon(
  onPressed: () {},
  icon: Icon(Icons.thumb_up),
  label: Text('Like'),
  style: ElevatedButton.styleFrom(
    backgroundColor: Colors.indigo,
    foregroundColor: Colors.white,
    padding: EdgeInsets.symmetric(horizontal: 20, vertical: 12),
    elevation: 6,
    shape: RoundedRectangleBorder(
      borderRadius: BorderRadius.circular(12),
    ),
  ),
)
```


#### 2-3. 스타일 지정 (ButtonStyle)
```dart
ElevatedButton.icon(
  onPressed: () {},
  icon: Icon(Icons.thumb_up),
  label: Text('Icon ButtonStyle'),
  style: ButtonStyle(
    backgroundColor: WidgetStateProperty.all(Colors.red),
    foregroundColor: WidgetStateProperty.all(Colors.white),
  ),
)
```

## 예제 3: 스타일 커스터마이징
  
### 3-1. styleFrom 사용  

```dart
ElevatedButton(
  onPressed: () {},
  style: ElevatedButton.styleFrom(
    backgroundColor: Colors.green,
    foregroundColor: Colors.white,
    elevation: 4,
    padding: EdgeInsets.symmetric(horizontal: 24, vertical: 12),
    shape: RoundedRectangleBorder(
      borderRadius: BorderRadius.circular(12),
    ),
  ),
  child: Text('StyleFrom'),
),

```
  
### 3-2. ButtonStyle 사용 (상태별)
```dart
  ElevatedButton(
    onPressed: () {},
    // 일괄 적용
    style: ButtonStyle(
      backgroundColor: WidgetStateProperty.all(Colors.red),
      foregroundColor: WidgetStateProperty.all(Colors.white),
      
    shape: WidgetStateProperty.all(
      RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(16),
      ),
    ),
    
    
    // 상태별 분기처리
    elevation: WidgetStateProperty.resolveWith((states) {
      return states.contains(WidgetState.pressed) ? 8 : 4;
    }),
    
    overlayColor: WidgetStateProperty.resolveWith<Color?>(
      (Set<WidgetState> states) {
        if (states.contains(WidgetState.pressed)) {
          return Colors.blue.withValues(alpha: 0.2);
        }
        if (states.contains(WidgetState.hovered)) {
          return Colors.red.withValues(alpha: 0.1);
        }
        return null;
      },
    ),
  ),
  child: Text('Custom Style'),
),
```

## 예제 4: 상태 기반 처리

### 4-1. 비활성화/활성화 (onPressed: null)
```dart
ElevatedButton(
  onPressed: null,
  child: Text('Disabled'),
)
```

### 4-2. 상태 변수로 동적 활성/비활성화
```dart
bool isEnabled = true;

ElevatedButton(
  onPressed: isEnabled ? () {
    setState(() {
      isEnabled = false;
    });
  } : null,
  child: Text('Disabled'),
)
```

### 4-3. 1초간 비활성화/로딩 처리
```dart
bool isEnabled = true;

ElevatedButton(
  onPressed: 
    isEnabled ? () {
      setState(() {
        isEnabled = false;
      });
      
      Future.delayed(Duration(seconds: 1), () {
        setState(() {
          isEnabled = true;
        });
      });
    } : null,
  child: Text(isEnabled ? 'Disable Me' : 'Disabled'),
)


// State의 변수로 선언
bool isLoading = false;

ElevatedButton(
  onPressed: isLoading ? null : () {
    debugPrint('start Loading');
    setState(() {
      isLoading = true;
    });
    Future.delayed(Duration(seconds: 1), () {
      debugPrint('stop Loading');
      setState(() {
        isLoading = false;
      });
    });
  },
  child: isLoading
      ? SizedBox(width: 16, height: 16, child: CircularProgressIndicator(strokeWidth: 2))
      : Text('Start Loading'),
)
```

---

### 예제 5: 통합 예제 (다양한 스타일, 상태, 아이콘 등)

```dart
class _MainScreenState extends State<MainScreen> {
  bool isEnabled = true;
  bool isLoading = false;

  @override
  Widget build(BuildContext context) {
    return  Scaffold(
        body: SafeArea(
            child: Center(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [

                  Text('기본 버튼'),
                  ElevatedButton(
                    onPressed: () {
                     debugPrint('Simple Click');
                    },
                    child: Text('Simple'),
                  ),

                  SizedBox(height: 30),

                  Text('Button Style 상태별 제어',
                    style: TextStyle(fontWeight: FontWeight.bold),
                  ),

                  SizedBox(height: 5),
                  Text('클릭 : elevation 변경'),
                  ElevatedButton(
                    onPressed: () {},
                    style: ButtonStyle(
                      backgroundColor: WidgetStateProperty.all(Colors.red),
                      foregroundColor: WidgetStateProperty.all(Colors.white),
                      shape: WidgetStateProperty.all(
                        RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(16),
                        ),
                      ),
                      elevation: WidgetStateProperty.resolveWith((states) {
                        return states.contains(WidgetState.pressed) ? 8 : 4;
                      }),
                    ),
                    child: Text('Elevation'),
                  ),

                  Text('호버 : red, 클릭 : blue'),

                  ElevatedButton(
                    onPressed: () {},
                    style: ButtonStyle(
                      overlayColor: WidgetStateProperty.resolveWith<Color?>(
                            (Set<WidgetState> states) {
                          // 클릭 액션
                          if (states.contains(WidgetState.pressed)) {
                            return Colors.blue.withValues(alpha : 0.2);
                          }
                          // 호버 액션, 웹에서만 동작
                          if (states.contains(WidgetState.hovered)) {
                            return Colors.red.withValues(alpha: 0.1);
                          }
                          return null; // 기본 없음
                        },
                      ),
                    ),
                    child: Text('Custom Highlight'),
                  ),

                  SizedBox(height: 20),
                  Text('StyleFrom 적용',
                    style: TextStyle(fontWeight: FontWeight.bold),
                  ),
                  ElevatedButton(
                    onPressed: () {},
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.green,
                      foregroundColor: Colors.white,
                      elevation: 4,
                      padding: EdgeInsets.symmetric(horizontal: 24, vertical: 12),
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(12),
                      ),
                    ),
                    child: Text('StyleFrom'),
                  ),

                  SizedBox(height: 30),
                  Text('Icon 버튼'),
                  ElevatedButton.icon(
                    onPressed: () {},
                    icon: Icon(Icons.thumb_up),
                    label: Text('Simple Icon'),
                  ),

                  SizedBox(height: 5),
                  Text('ButtonStyle'),
                  ElevatedButton.icon(
                    onPressed: () {},
                    icon: Icon(Icons.thumb_up),
                    label: Text('Icon ButtonStyle'),
                    style: ButtonStyle(
                      backgroundColor: WidgetStateProperty.all(Colors.red),
                      foregroundColor: WidgetStateProperty.all(Colors.white),
                    ),
                  ),

                  SizedBox(height: 5),
                  Text('StyleFrom'),
                  ElevatedButton.icon(
                    onPressed: () {},
                    icon: Icon(Icons.thumb_up),
                    label: Text('Icon StyleFrom'),
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.indigo,
                      foregroundColor: Colors.white,
                      padding: EdgeInsets.symmetric(horizontal: 20, vertical: 12),
                      elevation: 6,
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(8),
                      ),
                    ),
                  ),

                  SizedBox(height: 30),
                  Text('1초간 비활성화 모드'),
                  ElevatedButton(
                    onPressed: isEnabled
                        ? () {
                      setState(() {
                        isEnabled = false;
                      });
                      Future.delayed(Duration(seconds: 1), () {
                        setState(() {
                          isEnabled = true;
                        });
                      });
                    }
                        : null,
                    child: Text(isEnabled ? 'Disable Me' : 'Disabled'),
                  ),

                  SizedBox(height: 5),
                  Text('1초간 로딩 처리'),
                  ElevatedButton(
                    onPressed: isLoading ? null : () {
                      debugPrint('start Loading');
                      setState(() {
                        isLoading = true;
                      });

                      Future.delayed(Duration(seconds: 1), () {
                        debugPrint('stop Loading');
                        setState(() {
                          isLoading = false;
                        });
                      });
                    },
                    child: isLoading
                        ? SizedBox(width: 16, height: 16, child: CircularProgressIndicator(strokeWidth: 2))
                        : Text('Start Loading'),
                  ),

                ],
              ),
            )
        )
    );
  }
}
```
- 이 예제는 다양한 스타일, 상태 제어, 로딩 UI, 커스텀 highlight 등을 통합적으로 보여준다.

- 참고영상
<img src="https://i.imgur.com/d8HPf8d.gif" width="500" />


<br>


## ElevatedButtonTheme를 이용한 일괄 스타일 적용하기

- `ElevatedButtonTheme`를 사용하면 트리 하위의 모든 `ElevatedButton`에 공통 스타일을 지정할 수 있다.
- 앱 전체에 버튼 스타일을 일괄 적용하고 싶을 때 유용하다.

```dart
// 현재 하위에만 테마를 적용하고 싶은 경우
Column(
  children: [
    ElevatedButtonTheme(
      data: ElevatedButtonThemeData(
        style: ElevatedButton.styleFrom(backgroundColor: Colors.orange),
      ),
      child: Column(
        children: [
          ElevatedButton(onPressed: () {}, child: Text('오렌지 1')),
          ElevatedButton(onPressed: () {}, child: Text('오렌지 2')),
        ],
      ),
    ),
    ElevatedButton(onPressed: () {}, child: Text('디폴트')), // 적용 안됨
  ],
)

// 앱전체에 적용하고 싶은 경우
MaterialApp(
  theme: ThemeData(
    elevatedButtonTheme: ElevatedButtonThemeData(
      style: ElevatedButton.styleFrom(
        backgroundColor: Colors.deepPurple,
        foregroundColor: Colors.white,
        textStyle: TextStyle(fontSize: 16),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(10),
        ),
      ),
    ),
  ),
  home: MyHomePage(),
)

```

<br><br>

## ✅ FilledButton과의 차이
- `ElevatedButton`: 기본적으로 눌렀을 때 elevation이 생기며 입체감이 강조된다.
- `FilledButton`: 배경은 있으나 elevation이 없고, 평면적인 느낌이다.
→ Flat하고 미니멀한 UI를 만들고 싶다면 `FilledButton`도 고려할 수 있다.


<br><br>

### ✅ iconAlignment 속성
- `ElevatedButton.icon`에서 `iconAlignment` 속성을 통해 아이콘의 정렬 위치를 조정할 수 있다.
- 아이콘과 텍스트 배치 위치를 더 정밀하게 컨트롤하고 싶을 때 사용한다.


<br><br>



## 관련 위젯

- `TextButton` – 배경 없이 텍스트로만 구성된 버튼  
- `OutlinedButton` – 외곽선만 있는 버튼  
- `FilledButton` – 배경은 있으나 elevation은 없음  
- `IconButton` – 아이콘만 있는 버튼  
- `ButtonStyleButton` – 커스텀 버튼 구현용 베이스 클래스

<br><br>

## History
- 250708 : 초안 작성
