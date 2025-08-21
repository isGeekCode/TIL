# Using listenables

## 개요
`ValueNotifier`는 Flutter 에서 제공하는 경량 상태 관리 도구이다. 값이 변경될 때마다 리스너들에게 알림을 보내 UI를 갱신할 수 있다.

<br><br>
---

## 시작하기 전에 알아두면 좋은 것들
- `ValueNotifier`는 값의 변경을 감지하고 리스너에게 알릴 수 있는 Flutter의 내장 클래스이다.  
- `ValueNotifier<T>`는 제네릭 클래스로 특정 타입의 값을 감시한다.
- `notifyListeners()` 호출 없이 `value` 변경만으로 UI 반영이 가능하다.
- 보통 `ValueListenableBuilder`와 함께 사용한다.
- `setState`는 `StatefulWidget` 내부에서만 사용할 수 있는 로컬 상태 관리 방식이지만, `ValueNotifier`는 별도의 상태 객체이므로 `StatelessWidget`에서도 사용할 수 있다. 즉, UI 위젯은 상태 보관 책임이 없고 외부 객체를 구독만 하면 된다.  

<br><br>
---

## 개념 정리 / 기본 구조

```dart
final counter = ValueNotifier<int>(0);

// 값 변경
counter.value++;

// 값 수신
ValueListenableBuilder<int>(
  valueListenable: counter,
  builder: (context, value, child) {
    return Text('$value');
  },
);
```


<br><br>
---

## 예제 코드로 이해하기

```dart
class CounterApp extends StatelessWidget {
  final ValueNotifier<int> counter = ValueNotifier(0);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("ValueNotifier Example")),
      body: Center(
        child: 
        
          // 값 수신
          ValueListenableBuilder<int>(
          valueListenable: counter,
          builder: (context, value, child) {
            return Text("Count: $value");
          },
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () => counter.value++,
        child: Icon(Icons.add),
      ),
    );
  }
}
```

<br><br>
---

## 실무 적용 포인트
- 단일 값 관리에 적합 (예: 카운터, 토글 상태).
- `ChangeNotifier` 대비 보일러플레이트 코드가 적다.
- 위젯 단위의 국소적 상태 관리에 유용하다.
- 기본적으로는 `StatefulWidget`과 함께 사용하여 `dispose()`에서 정리하는 패턴이 권장된다.  
  (단순한 예제나 실습에서는 `StatelessWidget`에서도 활용 가능하다.)

<br><br>

## 실습 과제
1. `ValueNotifier`를 이용해 다크 모드 On/Off 토글 버튼을 구현하라.
2. `ValueNotifier` 두 개를 사용해 합산 값을 계산하는 UI를 만들어보라.

<br><br>

---

## iOS와의 비교

### Swift / iOS에서의 유사 개념
- **Property Observer (`didSet`)**  
  단일 값 변경을 감지할 때 사용 가능하지만, 리스너 추가 불가. (ValueNotifier보다 제한적)
  
- **KVO (Key-Value Observing)**  
  NSObject 기반 프로퍼티 감시 기능. 여러 리스너 등록 가능하지만 문법이 무겁다.

- **Combine의 @Published**  
  값 변경 시 자동 이벤트 발생. 여러 subscriber 연결 가능.  
  👉 Flutter의 `ValueNotifier`와 가장 유사한 개념.
  

```swift
// Property Observer
var counter: Int = 0 {
    didSet {
        print("Counter changed to \(counter)")
    }
}


// KVO
class Counter: NSObject {
    @objc dynamic var value: Int = 0
}

let counter = Counter()
let observation = counter.observe(\.value, options: [.new]) { object, change in
    print("Counter changed to \(object.value)")
}

counter.value += 1


// Combine
class Counter: ObservableObject {
    @Published var value: Int = 0
}

let counter = Counter()
let cancellable = counter.$value.sink { newValue in
    print("Counter changed to \(newValue)")
}

counter.value += 1


```


SwiftUI에서는 `@State`, `@ObservedObject`, `@EnvironmentObject`를 사용해 상태를 관리한다.  
- `@State`는 위젯 내부 로컬 상태 관리에 적합하고,  
- `@ObservedObject`는 외부 ObservableObject를 주입받아 사용하는 경우에 쓰이며,  
- `@EnvironmentObject`는 전역적으로 공유되는 상태를 관리할 때 활용된다.  
이 개념들은 각각 Flutter의 `setState`, `ChangeNotifier`, `InheritedWidget`/`Provider`에 대응된다고 볼 수 있다.

<br><br>
---


## ChangeNotifier

앞에서 살펴본 `ValueNotifier`가 단일 값에 특화된 상태 관리 클래스라면,  
`ChangeNotifier`는 그 확장판으로 여러 값과 리스너를 관리할 수 있는 범용 상태 관리 클래스이다.  
단, `ValueNotifier`와 달리 `notifyListeners()`를 직접 호출해야 UI가 갱신된다.

ChangeNotifier 역시 더 이상 사용하지 않을 때는 `dispose()`를 호출해 리소스를 정리해야 한다.

### ChangeNotifier 기본 예시

```dart
class Counter extends ChangeNotifier {
  int _count = 0;

  int get count => _count;

  void increment() {
    _count++;
    notifyListeners();
  }
}

final counter = Counter();
```

즉, `ChangeNotifier`는 여러 상태를 묶어서 관리할 때 적합하며,  
보통 Provider 같은 패키지와 결합해 앱 전반의 상태 관리에 활용된다.

또한 `ChangeNotifier`는 상태와 비즈니스 로직을 함께 담을 수 있어, **ViewModel**로서 활용하기에도 적합하다.

### ChangeNotifier를 ViewModel로 사용하기 예시

```dart
class CounterViewModel extends ChangeNotifier {
  int _count = 0;
  int get count => _count;

  void increment() {
    _count++;
    notifyListeners();
  }
}

// 사용 예시
class CounterPage extends StatelessWidget {
  final counterVM = CounterViewModel();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: ListenableBuilder(
          listenable: counterVM,
          builder: (context, child) {
            return Text("Count: ${counterVM.count}");
          },
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: counterVM.increment,
        child: Icon(Icons.add),
      ),
    );
  }
}
```

이 예시처럼 `ChangeNotifier`를 ViewModel로 사용하면 상태와 로직을 UI와 분리해 관리할 수 있어 구조적인 코드 작성이 가능하다.

실무에서는 `ListenableBuilder`보다는 Provider 패키지의 `Consumer`나 `context.watch` 패턴을 사용하는 경우가 많다. `ListenableBuilder`는 학습용으로 이해하기에는 직관적이지만, 대규모 앱에서는 Provider나 Riverpod 같은 도구와 함께 쓰는 것이 일반적이다.

<br><br>
---

## ValueNotifier를 ViewModel로 사용하기

꼭 `ChangeNotifier`만 뷰모델로 쓸 수 있는 것은 아니다.  
일반 클래스 내부에 `ValueNotifier`를 필드로 포함시켜, 해당 클래스를 **간단한 ViewModel**처럼 활용할 수도 있다.

### 예시

```dart
class CounterVM {
  final ValueNotifier<int> counter = ValueNotifier<int>(0);

  void increment() {
    counter.value++;
  }

  void dispose() {
    counter.dispose();
  }
}
```

### 사용 예시

```dart
class CounterPage extends StatelessWidget {
  final vm = CounterVM();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("ValueNotifier VM Example")),
      body: Center(
        child: ValueListenableBuilder<int>(
          valueListenable: vm.counter,
          builder: (context, value, child) {
            return Text("Count: $value");
          },
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: vm.increment,
        child: Icon(Icons.add),
      ),
    );
  }
}
```

이렇게 구성하면 ViewModel은 여러 `ValueNotifier` 필드를 가질 수 있어,  
소규모 상태 관리에서는 충분히 유용하게 활용할 수 있다.  
단, 상태가 복잡해지면 `ChangeNotifier`나 Provider, Riverpod 같은 더 확장성 있는 도구가 적합하다.


<br><br>
---


## ChangeNotifier 과제 1. 10개의 카운터

## 🎯 목표
- 여러 개의 카운터를 하나의 ViewModel에서 관리
- 커서를 통해 현재 조작할 카운터를 선택하고, 해당 값만 변경
- Undo/Redo 버튼으로 커서를 앞뒤로 이동하여 다른 카운터를 선택 가능

## 📦 상태/모델
- `List<int> items` : 10개의 카운터 값 (초기값 0)
- int cursor : 현재 선택된 카운터의 인덱스


## ⚙️ 액션
- increment() : 현재 cursor가 가리키는 카운터 값 증가
- decrement() : 현재 cursor가 가리키는 카운터 값 감소
- undo() : cursor를 한 칸 왼쪽으로 이동 (0 이하에서는 불가)
- redo() : cursor를 한 칸 오른쪽으로 이동 (마지막 index 이상에서는 불가)


## 🎨 UI 요구사항
- items 전체 리스트를 화면에 문자열로 출력
- cursor가 가리키는 현재 카운터 값을 별도로 표시
- Increment / Decrement 버튼 → 현재 선택된 카운터만 변경
- Undo / Redo 버튼 → cursor 이동 (경계에선 비활성화)


## 🧪 체크리스트
- cursor 이동이 배열 범위를 벗어나지 않음
- cursor가 바뀌면 UI에 현재 선택된 값이 즉시 반영
- Increment/Decrement는 cursor가 가리키는 카운터만 바뀜
- Undo/Redo 버튼은 경계 조건에서 비활성화


```dart
class _MainScreenState extends State<MainScreen> {

  final viewModel = ViewModel();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ListenableBuilder(listenable: viewModel, builder: (context, child) {
              return Text(viewModel.items.toString());
            },),


            ListenableBuilder(listenable: viewModel, builder: (context, child) {
              return Text(viewModel.items[viewModel.cursor].toString());
            },),

            SizedBox(
              height: 30,
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [

                ElevatedButton(onPressed: () {
                  viewModel.decrement();
                }, child: Text("Decrement")),

                SizedBox(
                  width: 30,
                ),
                ElevatedButton(onPressed: () {
                  viewModel.increment();
                }, child: Text("Increment")),
              ],
            ),

            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [

                ElevatedButton(onPressed: () {
                  viewModel.undo();
                }, child: Text("Undo")),

                SizedBox(
                  width: 30,
                ),
                ElevatedButton(onPressed: () {
                  viewModel.redo();
                }, child: Text("Redo")),
              ],
            )
          ],
        )
      ),
    );
  }
}


class ViewModel extends ChangeNotifier {
  int _cursor = 0;
  int get cursor => _cursor;
  List<int> _items = [0,0,0,0,0, 0,0,0,0,0];
  List<int> get items => _items;


  void increment() {
    items[_cursor]++;
    notifyListeners();
  }

  void decrement() {
    items[_cursor]--;
    notifyListeners();
  }

  void undo() {
    if (_cursor > 0) {
      _cursor--;
      notifyListeners();
    }
  }

  void redo() {
    if( _cursor < items.length - 1) {
      _cursor++;
      notifyListeners();
    }
  }
}
```



## ChangeNotifier 과제2.   동적 리스트 관리하기


### 요구사항

아래의 코드를 참고하여 **할 일(To-do) 리스트 앱**을 구현하세요.

1. 화면에는 `ListView.builder`를 이용해 현재 저장된 할 일들을 출력해야 합니다.
    - 리스트는 `ViewModel`에서 관리합니다.
    - 각 항목은 `ListTile`로 표시하고, `Text`에는 `"할 일 N"` 형태로 출력합니다.
2. FloatingActionButton(+)을 누르면 새로운 항목이 추가됩니다.
    - 새로운 항목의 이름은 `"할 일 ${리스트길이+1}"` 로 자동 생성됩니다.
3. FloatingActionButton(-)을 누르면 마지막 항목이 삭제됩니다.
    - 단, 리스트가 비어있을 경우 삭제 동작이 일어나지 않도록 방어 코드를 작성하세요. 
4. ViewModel은 반드시 `ChangeNotifier`를 상속받고, `notifyListeners()`를 호출하여 UI가 갱신되도록 구현해야 합니다.
    

---

### 실행 화면 예시
- 초기 상태: `["할 일 1", "할 일 2"]` 출력
- `+` 버튼 클릭 → `["할 일 1", "할 일 2", "할 일 3"]`
- `-` 버튼 클릭 → `["할 일 1", "할 일 2"]`
    

### 힌트
- `ListenableBuilder`를 활용해 `ViewModel`의 변화를 감지하도록 하세요.
- Swift의 `guard`문과 비슷하게, Dart에서는 `if (리스트.isEmpty) return;` 패턴을 사용하여 삭제 시 안전하게 처리할 수 있습니다.



```dart
  

class _MainScreenState extends State<MainScreen> {  
  final viewModel = ViewModel();  
  @override  
  Widget build(BuildContext context) {  
    return Scaffold(  
      appBar: AppBar(title: Text('MainScreen'),),  
      body: Center(child:  
        ListenableBuilder(listenable: viewModel, builder: (context, child) {  
          // return  Text('this is ${viewModel._items.last}');  
  
          return ListView.builder(  
            itemCount: viewModel.items.length,  
            itemBuilder: (context, index) {  
            return ListTile(title: Text('this is ${viewModel.items[index]}'),);  
          },);  
        },)  
        ,),  
      floatingActionButton: Column(  
        mainAxisAlignment: MainAxisAlignment.end  
        ,  
        children: [  
          FloatingActionButton(onPressed: () {  
            viewModel.increment();  
          },child: Icon(Icons.add),),  
  
          SizedBox(height: 30,),  
          FloatingActionButton(onPressed: () {  
            viewModel.decrement();  
          },child: Icon(Icons.remove),),  
        ],  
      )  
    );  
  }  
}  
  
class ViewModel extends ChangeNotifier {  
  int _count = 0;  
  int get count => _count;  
  
  List<int> _items = [1,2];  
  List<int> get items => _items;  
  
  void increment() {  
  
    _items.add(items.length + 1);  
    notifyListeners();  
  }  
  
  void decrement() {  
    if (items.isNotEmpty) {  
      _items.removeLast();  
      notifyListeners();  
    }  
  }  
}
```



## HISTORY
- 250818 : 최초 작성
