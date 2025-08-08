# Layout - Multi-child : ListView

<br><br>
---

## 개요

ListView는 스크롤 가능한 다중 위젯 레이아웃을 구성할 수 있는 Flutter 위젯이다.  
설정 앱, 채팅 목록, 쇼핑 아이템 목록 등에서 자주 활용할 수 있다.

<br><br>
---

## 시작하기 전에 알아두면 좋은 것들

- ListView는 여러 개의 자식 위젯을 스크롤 가능한 방향으로 나열할 수 있다.
- 주로 수직 방향으로 사용하지만, 수평으로도 구성할 수 있다.

<br><br>

---


## 3. 만드는 방식 

ListView는 생성 방식에 따라 크게 두 가지로 나뉜다:  

- 모든 항목을 한 번에 생성하는 **정적 방식**  
- 필요한 시점에 항목을 생성하는 **동적 방식**

정적방식은 미리 ListTile 등으로 위젯의 배열을 만들어서 ListView의 `childeren`에 전달하는 구조이다. 
즉, 데이터 기반으로 위젯배열을 먼저만들고 이를 한번에 렌더링한다. 

반면에 동적 방식은 ListView자체가 itemCount와 ItemBuilder 를 통해 항목 수를 판단하고,
UI에 표시되는 공간에 해당하는 항목만 위젯으로 생성하여 렌더링한다. 


|   구분    |          방식          |       생성 시점        |             추천 상황             |
|:---------:|:----------------------:|:----------------------:|:---------------------------------:|
| 정적 방식 | `generate()`, `.map()` | 미리 모두 한 번에 생성 |     항목 수가 적고 단순할 때      |
| 동적 방식 | `builder`, `separated` |    스크롤 시점 생성    | 항목 수가 많거나 무한 스크롤일 때 |


실무에서는 성능과 확장성을 고려해 대부분 동적 방식을 사용한다.


<br><br>

---



## 4. 예제 코드로 이해하기
다양한 방식으로 ListView를 구성하는 예제를 통해 실제 동작 방식을 확인할 수 있다.  
각 방식은 생성 구조, 사용 목적, 성능 측면에서 차이를 보인다.

### 4-1. 단순 텍스트 리스트
가장 단순한 생성방법이다.반복 횟수만 지정하고, index를 기반으로 항목을 생성할 수 있다.


```dart
ListView(
  children: List.generate(10, (index) {
    return ListTile(
      title: Text('Item $index'), // index 값을 포함한 텍스트 표시
    );
  }),
)
```


<br><br>

### 4-2. 데이터 리스트 기반 생성
외부에 정의된 리스트를 기반으로 `.map()`을 통해 위젯을 생성한다.
이 방식은 값만 순회하며 index는 사용하지 않는다.  

index가 필요한 경우에는 `List.generate()` 또는 `items.asMap().entries.map()`을 사용할 수 있지만,  
 특별한 이유가 없다면 `.map()` 방식이 가장 간단하고 가독성이 좋다.

```dart
final List<String> items = ['사과', '바나나', '오렌지', '포도', '수박'];

ListView(
  children: items.map((item) {
    return ListTile(
      title: Text(item), // 항목 이름 출력
    );
  }).toList(),
)
```



<br><br>

### 4-3. ListView.builder 사용 예제
- ListView.builder는 화면에 보이는 항목만 생성하며, 스크롤 시점에 항목이 동적으로 렌더링된다.
- 항목 수가 많거나 무한 스크롤이 필요한 경우에 적합하다.


```dart
final List<String> items = ['사과', '바나나', '오렌지', '포도', '수박'];

ListView.builder(
  itemCount: items.length,
  itemBuilder: (context, index) {
    return ListTile(
      title: Text(items[index]),
    );
  },
)
```


<br><br>

### 4-4. ListView.separated 사용 예제

```dart
final List<String> items = ['사과', '바나나', '오렌지', '포도', '수박'];

ListView.separated(
  itemCount: items.length,
  itemBuilder: (context, index) {
    return ListTile(
      title: Text(items[index]),
    );
  },
  separatorBuilder: (context, index) {
    return Divider(); // 각 항목 사이에 선을 추가
  },
)
```

- `ListView.separated`는 항목을 나열하면서, 각 항목 사이에 구분 요소(Divider 등)를 함께 넣을 수 있다.
- UI 구분이 명확해져 가독성이 좋아진다.



<br><br>
---

## 5. 확장 개념 / 보충 설명

### 5-1. 상태 변화를 반영한 동적 리스트 예제

리스트에 항목을 추가하거나 삭제하려면 상태 변경이 필요하므로, 해당 화면은 `StatefulWidget`으로 구성해야 한다.  
버튼을 눌러 리스트에 항목을 추가하거나 제거하면, `setState()`를 통해 UI가 자동으로 갱신된다.

아래는 추가 버튼과 삭제 버튼을 모두 포함한 예제이다:

```dart
class ItemListPage extends StatefulWidget {
  const ItemListPage({super.key});

  @override
  State<ItemListPage> createState() => _ItemListPageState();
}

class _ItemListPageState extends State<ItemListPage> {
  List<String> items = ['사과', '바나나'];

  void _addItem() {
    setState(() {
      items.add('항목 ${items.length}');
    });
  }

  void _removeItem() {
    if (items.isNotEmpty) {
      setState(() {
        items.removeLast();
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('리스트 추가 / 제거')),
      body: buildItemList(items),
      floatingActionButton: Row(
        mainAxisAlignment: MainAxisAlignment.end,
        children: [
          FloatingActionButton(
            onPressed: _addItem,
            tooltip: '추가',
            child: const Icon(Icons.add),
          ),
          const SizedBox(width: 12),
          FloatingActionButton(
            onPressed: _removeItem,
            tooltip: '삭제',
            child: const Icon(Icons.remove),
          ),
        ],
      ),
    );
  }
}

Widget buildItemList(List<String> items) {
  return ListView.builder(
    itemCount: items.length,
    itemBuilder: (context, index) {
      return ListTile(
        title: Text(items[index]),
      );
    },
  );
}

```

이처럼 동적 방식은 ListView.builder와 함께 StatefulWidget 및 setState()를 사용하여 실시간으로 UI를 갱신할 수 있다.


## HISTORY
- 250806 : 최초 작성
