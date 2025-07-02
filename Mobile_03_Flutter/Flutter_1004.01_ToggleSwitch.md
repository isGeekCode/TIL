# Flutter - Toggle Switch

토글 스위치는 사용자가 특정 옵션을 켜거나 끌 수 있는 스위치로, On/Off 상태를 전환할 수 있다.


Switch 위젯을 사용하여 토글 스위치를 생성한다.

일반적으로 StatefulWidget 내에서 상태를 관리하는 방식으로 사용한다. 


```dart

import 'package:flutter/material.dart';

bool switchValue = false; // 스위치의 초기 상태 설정

Switch(
  value: switchValue,
  onChanged: (value) {
    setState(() {
      switchValue = value;
    });
  },
)

```

- value 속성: 스위치의 현재 상태를 나타낸다.
- onChanged 속성은 스위치가 전환될 때 호출되는 콜백 함수를 지정한다.
- 콜백 함수 내에서 setState 함수를 사용하여 스위치의 상태를 업데이트한다.

## 스타일

토글 스위치에 추가적인 스타일을 적용하려면 activeColor, inactiveColor, activeTrackColor, inactiveTrackColor 등의 속성을 사용할 수 있다.

- activeColor
  - 토글 스위치가 켜진 상태일 때의 색상을 지정한다. 사용자가 스위치를 켜면 해당 색상이 적용된다.
- inactiveColor
  - 토글 스위치가 꺼진 상태일 때의 색상을 지정한다. 사용자가 스위치를 끄면 해당 색상이 적용된다.
- activeTrackColor
  - 토글 스위치의 켜진 상태에서 트랙(스위치의 배경)의 색상을 지정한다. 일반적으로 activeColor와 함께 사용하여 켜진 상태에서의 시각적인 표현을 조정할 수 있다.
- inactiveTrackColor
  - 토글 스위치의 꺼진 상태에서 트랙의 색상을 지정한다. 일반적으로 inactiveColor와 함께 사용하여 꺼진 상태에서의 시각적인 표현을 조정할 수 있다.

 예를 들어, 다음과 같이 색상을 지정할 수 있다

```dart
Switch(
  value: switchValue,
  onChanged: (value) {
    setState(() {
      switchValue = value;
    });
  },
  activeColor: Colors.blue,
  activeTrackColor: Colors.lightBlueAccent,
)

```

사실 여기 있는 ThumbTintColor는 꺼져있을 때는 지정이 가능하지만 켜져있는건 기본색상이 있기에 이걸 지정하려면 커스텀 스위치를 지정해야한다. 

## 커스텀 스위치 만들기

```dart
class DeliveryCustomSwitch extends StatelessWidget {
  final bool value;
  final ValueChanged<bool> onChanged;
  final Color thumbColor;

  const DeliveryCustomSwitch({
    Key? key,
    required this.value,
    required this.onChanged,
    this.thumbColor = Colors.white,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () {
        onChanged(!value);
      },
      child: Container(
        width: 34.0,
        height: 20.0,
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(14.0),
          color: value ? Color(0xFF11A064) : Color(0xFF2A3741), // 꺼져있을 때와 켜져있을 때의 배경색 수정
        ),
        child: AnimatedAlign(
          alignment: value ? Alignment.centerRight : Alignment.centerLeft,
          duration: const Duration(milliseconds: 200),
          child: Container(
            width: 20.0,
            height: 20.0,
            decoration: BoxDecoration(
              shape: BoxShape.circle,
              color: thumbColor,
            ),
          ),
        ),
      ),
    );
  }
}
```
